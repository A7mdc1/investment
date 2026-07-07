"""apply_txn.py — record an executed trade and UPDATE the holding .md files.

This is bookkeeping only. It never decides anything — you tell it what you did.

Examples:
  python scripts/apply_txn.py --ticker NOW --action buy  --shares 3   --price 108.20
  python scripts/apply_txn.py --ticker FIG --action sell --shares all --price 19.30
  python scripts/apply_txn.py --ticker AVGO --action buy --shares 2 --price 195 --name "Broadcom"

Behaviour:
  buy  : weighted-average cost recomputed; new ticker -> new holding stub created
         with shariah.status=unknown (so it's GATED until you screen it).
  sell : avg-cost method; realized P/L logged; shares==all (or ->0) closes the
         position (file moved to holdings/closed/ with a realized-P/L note).
         --exit-reason stop|target|invalidation|discretionary (inferred if omitted).
All trades append to transactions.csv AND to journal.csv (richer per-trade record
with stop/target/expected-R/setup_type/benchmark, read by journal.py for
per-setup expectancy). The journal is measurement only — no caps, no enforcement.
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import glob
import io
import os
import shutil
from ruamel.yaml import YAML

import journal as journal_mod

HERE = os.path.dirname(__file__)
HOLDINGS = os.path.join(HERE, "..", "holdings")
CLOSED = os.path.join(HOLDINGS, "closed")
LEDGER = os.path.join(HERE, "..", "transactions.csv")
yaml = YAML()
yaml.preserve_quotes = True


def _benchmark_price(symbol: str):
    """Same-day benchmark price (best-effort; None offline)."""
    if not symbol:
        return None
    try:
        import yfinance as yf
        p = yf.Ticker(symbol).fast_info.get("lastPrice")
        return round(float(p), 4) if p else None
    except Exception:
        return None


def journal_log(row: dict):
    """Append one row to journal.csv (schema in journal.py)."""
    path = journal_mod.JOURNAL
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=journal_mod.JOURNAL_FIELDS)
        if new:
            w.writeheader()
        w.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in journal_mod.JOURNAL_FIELDS})


def _last_open_entry(ticker: str):
    """Most recent BUY row for a ticker from journal.csv (the entry side)."""
    entry = None
    for r in journal_mod.load_rows():
        if (str(r.get("ticker", "")).upper() == ticker.upper()
                and str(r.get("action", "")).lower() == "buy"):
            entry = r
    return entry


def _setup_meta(ticker: str) -> dict:
    """Front-matter of setups/<ticker>.md if present (for stop/target/setup_type)."""
    try:
        from common import setups_by_ticker
        s = setups_by_ticker().get(ticker.upper())
        return s["meta"] if s else {}
    except Exception:
        return {}


def read_md(path: str):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return yaml.load(fm), body
    return {}, text


def write_md(path: str, meta: dict, body: str):
    buf = io.StringIO()
    yaml.dump(meta, buf)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n" + buf.getvalue() + "---" + body)


def find(ticker: str):
    for p in glob.glob(os.path.join(HOLDINGS, "*.md")):
        if os.path.basename(p).startswith("_"):
            continue
        meta, _ = read_md(p)
        if str(meta.get("ticker", "")).upper() == ticker.upper():
            return p, meta
    return None, None


def log(row: dict):
    new = not os.path.exists(LEDGER)
    with open(LEDGER, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "ticker", "action", "shares",
                                          "price", "realized_pl", "note"])
        if new:
            w.writeheader()
        w.writerow(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--action", required=True, choices=["buy", "sell"])
    ap.add_argument("--shares", required=True)  # int or "all"
    ap.add_argument("--price", required=True, type=float)
    ap.add_argument("--name", default=None)
    ap.add_argument("--exit-reason", dest="exit_reason", default=None,
                    choices=["stop", "target", "invalidation", "discretionary"],
                    help="on SELL: how the trade ended (inferred from stop/target if omitted)")
    a = ap.parse_args()
    today = dt.date.today().isoformat()
    cfg = journal_mod.load_cfg()
    bench = cfg.get("journal_benchmark", "SPUS")
    path, meta = find(a.ticker)

    if a.action == "buy":
        n = int(a.shares)
        if meta is None:  # brand-new position -> create a GATED stub
            os.makedirs(HOLDINGS, exist_ok=True)
            path = os.path.join(HOLDINGS, f"{a.ticker.lower()}.md")
            meta = {"ticker": a.ticker.upper(), "name": a.name or a.ticker.upper(),
                    "shares": 0, "cost_basis": 0.0, "currency": "USD",
                    "shariah": {"source": "pending", "status": "unknown",
                                "screened": today}}
            body = ("\n\n## Thesis\nNEW position — screen compliance in Zoya/Musaffa "
                    "before adding more.\n\n## Risks\n\n## Notes\n")
        else:
            _, body = read_md(path)
        old_sh, old_cb = meta.get("shares", 0) or 0, meta.get("cost_basis", 0) or 0
        new_sh = old_sh + n
        meta["shares"] = new_sh
        meta["cost_basis"] = round((old_sh * old_cb + n * a.price) / new_sh, 4)
        write_md(path, meta, body)
        log({"date": today, "ticker": a.ticker.upper(), "action": "buy",
             "shares": n, "price": a.price, "realized_pl": "",
             "note": f"avg cost -> {meta['cost_basis']}"})
        # Journal the entry: setup card supplies stop/target/setup_type/plan.
        sm = _setup_meta(a.ticker)
        stop, target = sm.get("stop_price"), sm.get("target_price")
        exp_r = (round((target - a.price) / (a.price - stop), 3)
                 if (stop and target and a.price > stop) else None)
        journal_log({"date": today, "ticker": a.ticker.upper(), "action": "buy",
                     "shares": n, "entry_price": a.price, "stop": stop, "target": target,
                     "expected_r": exp_r, "setup_type": sm.get("setup_type"),
                     "earnings_plan": sm.get("earnings_plan"),
                     "card_ref": (f"setups/{a.ticker.lower()}.md" if sm else ""),
                     "benchmark": bench, "benchmark_entry": _benchmark_price(bench)})
        print(f"BUY {n} {a.ticker.upper()} @ {a.price} | shares {old_sh}->{new_sh}, "
              f"avg cost {old_cb}->{meta['cost_basis']}")
        return

    # sell
    if meta is None:
        raise SystemExit(f"No holding found for {a.ticker}")
    _, body = read_md(path)
    held = meta.get("shares", 0) or 0
    cb = meta.get("cost_basis", 0) or 0
    n = held if str(a.shares).lower() == "all" else int(a.shares)
    if n > held:
        raise SystemExit(f"Can't sell {n}; only {held} held")
    realized = round(n * (a.price - cb), 2)
    remaining = held - n
    if remaining == 0:  # close it out
        os.makedirs(CLOSED, exist_ok=True)
        meta["shares"] = 0
        meta["closed"] = today
        meta["realized_pl"] = realized
        dest = os.path.join(CLOSED, os.path.basename(path))
        write_md(path, meta, body + f"\n\n## Closed {today}\nRealized P/L: {realized}\n")
        shutil.move(path, dest)
        where = f"closed -> {os.path.relpath(dest, os.path.join(HERE,'..'))}"
    else:
        meta["shares"] = remaining
        write_md(path, meta, body)
        where = f"shares {held}->{remaining}"
    log({"date": today, "ticker": a.ticker.upper(), "action": "sell",
         "shares": n, "price": a.price, "realized_pl": realized, "note": where})
    # Journal the exit: pair against the most recent entry to get realized R,
    # holding days, and the exit reason (arg, else inferred from stop/target).
    entry = _last_open_entry(a.ticker)
    e_price = journal_mod._num(entry.get("entry_price")) if entry else None
    e_stop = journal_mod._num(entry.get("stop")) if entry else None
    e_target = journal_mod._num(entry.get("target")) if entry else None
    realized_r = (round((a.price - e_price) / (e_price - e_stop), 3)
                  if (e_price is not None and e_stop is not None and (e_price - e_stop) > 0) else None)
    holding_days = None
    if entry and entry.get("date"):
        try:
            holding_days = (dt.date.fromisoformat(today) - dt.date.fromisoformat(entry["date"])).days
        except ValueError:
            pass
    reason = a.exit_reason
    if not reason:
        if e_stop is not None and a.price <= e_stop:
            reason = "stop"
        elif e_target is not None and a.price >= e_target:
            reason = "target"
        else:
            reason = "discretionary"
    journal_log({"date": today, "ticker": a.ticker.upper(), "action": "sell",
                 "shares": n, "entry_price": e_price, "exit_price": a.price,
                 "stop": e_stop, "target": e_target,
                 "expected_r": (entry.get("expected_r") if entry else None),
                 "realized_r": realized_r, "realized_pl": realized,
                 "holding_days": holding_days,
                 "setup_type": (entry.get("setup_type") if entry else None),
                 "exit_reason": reason,
                 "earnings_plan": (entry.get("earnings_plan") if entry else None),
                 "card_ref": (entry.get("card_ref") if entry else ""),
                 "benchmark": bench,
                 "benchmark_entry": (entry.get("benchmark_entry") if entry else None),
                 "benchmark_exit": _benchmark_price(bench)})
    print(f"SELL {n} {a.ticker.upper()} @ {a.price} | realized P/L {realized} | "
          f"{where} | R {realized_r if realized_r is not None else 'n/a'} | exit {reason}")


if __name__ == "__main__":
    main()
