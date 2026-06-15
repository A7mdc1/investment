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
All trades append to transactions.csv.
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

HERE = os.path.dirname(__file__)
HOLDINGS = os.path.join(HERE, "..", "holdings")
CLOSED = os.path.join(HOLDINGS, "closed")
LEDGER = os.path.join(HERE, "..", "transactions.csv")
yaml = YAML()
yaml.preserve_quotes = True


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
    a = ap.parse_args()
    today = dt.date.today().isoformat()
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
    print(f"SELL {n} {a.ticker.upper()} @ {a.price} | realized P/L {realized} | {where}")


if __name__ == "__main__":
    main()
