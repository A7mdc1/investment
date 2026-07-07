"""journal.py — trade journal + per-setup EXPECTANCY (measurement, not limits).

apply_txn.py writes one row per buy/sell to journal.csv; this reads the CLOSED
(sell) rows and reports, per the swing refactor spec:

  - overall: hit rate, avg win R, avg loss R, expectancy per trade (R and $),
    total P&L vs a same-dates-into-benchmark counterfactual;
  - per setup_type: the same stats broken out — THIS table is the product. It
    tells you which setups pay YOU and which to stop trading;
  - slippage line: average (planned stop - actual exit) on stopped trades —
    measures gap/slippage reality vs the R:R math;
  - while closed trades < journal_min_trades: "sample too small for conclusions"
    (a NOTE, not a restriction).

No caps, no enforcement. Volume and sizing are the owner's domain; the journal
only makes the results undeniable. `report()` is a pure function (offline-testable).
"""
from __future__ import annotations
import csv
import json
import os

HERE = os.path.dirname(__file__)
JOURNAL = os.path.join(HERE, "..", "journal.csv")
RULES = os.path.join(HERE, "..", "rules.md")

JOURNAL_FIELDS = [
    "date", "ticker", "action", "shares", "entry_price", "exit_price",
    "stop", "target", "expected_r", "realized_r", "realized_pl", "holding_days",
    "setup_type", "exit_reason", "earnings_plan", "card_ref",
    "benchmark", "benchmark_entry", "benchmark_exit",
]


def load_cfg() -> dict:
    import yaml
    txt = open(RULES, encoding="utf-8").read()
    return (yaml.safe_load(txt.split("---", 2)[1]) or {}) if txt.startswith("---") else {}


def _num(v):
    """Coerce a CSV cell to float, or None if blank/unparseable."""
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def _stats(trades: list[dict]) -> dict:
    """Expectancy stats over a list of closed-trade dicts (already coerced)."""
    n = len(trades)
    rs = [t["realized_r"] for t in trades if t["realized_r"] is not None]
    wins = [r for r in rs if r > 0]
    losses = [r for r in rs if r <= 0]
    pls = [t["realized_pl"] for t in trades if t["realized_pl"] is not None]
    return {
        "trades": n,
        "hit_rate": round(len(wins) / len(rs), 3) if rs else None,
        "avg_win_r": round(_mean(wins), 2) if wins else None,
        "avg_loss_r": round(_mean(losses), 2) if losses else None,
        "expectancy_r": round(_mean(rs), 3) if rs else None,
        "expectancy_currency": round(_mean(pls), 2) if pls else None,
        "total_pl": round(sum(pls), 2) if pls else None,
        "avg_holding_days": round(_mean([t["holding_days"] for t in trades]), 1)
                            if any(t["holding_days"] is not None for t in trades) else None,
    }


def _benchmark_counterfactual(trades: list[dict]) -> dict:
    """What the same capital, same dates, would have done in the benchmark."""
    total_cf, total_real, covered = 0.0, 0.0, 0
    for t in trades:
        be, bx = t["benchmark_entry"], t["benchmark_exit"]
        sh, ep, pl = t["shares"], t["entry_price"], t["realized_pl"]
        if None in (be, bx, sh, ep) or be == 0:
            continue
        capital = sh * ep
        total_cf += capital * (bx - be) / be
        total_real += pl if pl is not None else 0.0
        covered += 1
    return {"trades_covered": covered,
            "trade_pl": round(total_real, 2) if covered else None,
            "benchmark_pl": round(total_cf, 2) if covered else None,
            "excess_vs_benchmark": round(total_real - total_cf, 2) if covered else None}


def report(rows: list[dict], cfg: dict | None = None) -> dict:
    """Pure: build the journal report from raw journal rows (strings or numbers)."""
    cfg = cfg or {}
    min_trades = int(cfg.get("journal_min_trades", 20))

    closed = []
    for r in rows:
        if str(r.get("action", "")).lower() != "sell":
            continue
        closed.append({
            "ticker": r.get("ticker"),
            "setup_type": (r.get("setup_type") or "unspecified"),
            "exit_reason": (r.get("exit_reason") or "discretionary"),
            "shares": _num(r.get("shares")),
            "entry_price": _num(r.get("entry_price")),
            "exit_price": _num(r.get("exit_price")),
            "stop": _num(r.get("stop")),
            "realized_r": _num(r.get("realized_r")),
            "realized_pl": _num(r.get("realized_pl")),
            "holding_days": _num(r.get("holding_days")),
            "benchmark_entry": _num(r.get("benchmark_entry")),
            "benchmark_exit": _num(r.get("benchmark_exit")),
        })

    # Slippage: on stopped trades, planned stop vs actual exit (positive = worse,
    # i.e. gapped/slipped through the stop). This is the R:R-vs-reality check.
    stop_slips = [t["stop"] - t["exit_price"] for t in closed
                  if t["exit_reason"] == "stop" and t["stop"] is not None
                  and t["exit_price"] is not None]

    # Per-setup expectancy — the product. Normalize the key so a stray case/space
    # doesn't split a bucket.
    by_setup: dict[str, list] = {}
    for t in closed:
        key = str(t["setup_type"]).strip().lower().replace(" ", "_") or "unspecified"
        by_setup.setdefault(key, []).append(t)

    out = {
        "closed_trades": len(closed),
        "sample_note": (None if len(closed) >= min_trades else
                        f"sample too small for conclusions ({len(closed)}/{min_trades} closed trades)"),
        "overall": _stats(closed),
        "benchmark_counterfactual": _benchmark_counterfactual(closed),
        "slippage_on_stops": {
            "stopped_trades": len(stop_slips),
            "avg_stop_minus_exit": round(_mean(stop_slips), 4) if stop_slips else None,
            "note": "positive = filled worse than the planned stop (gap/slippage)",
        },
        "by_setup_type": {k: _stats(v) for k, v in sorted(by_setup.items())},
        "disclaimer": ("Measurement only — no caps, no enforcement. Volume and sizing "
                       "are your decisions. Keep what pays, cut what doesn't; if net-of-cost "
                       "returns trail the benchmark, trade less."),
    }
    return out


def load_rows(path: str = JOURNAL) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    print(json.dumps(report(load_rows(), load_cfg()), indent=2, default=str))


if __name__ == "__main__":
    main()
