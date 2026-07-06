"""shariah.py — Shariah pre-screen.

Two layers:
  1. Surfaces the verdict you recorded from Zoya/Musaffa + flags when it's stale.
  2. A *rough* financial-ratio pre-check (AAOIFI-style) computed from yfinance,
     so you get an early warning before re-screening in Zoya/Musaffa.

IMPORTANT: this is NOT a substitute for Zoya/Musaffa. The business-activity
screen and non-compliant-income (<5%) test need their data; treat ratios here
as a heads-up only. Thresholds default to 33% (configurable).
"""
from __future__ import annotations
import datetime as dt
import json
import sys
import yfinance as yf
from common import load_holdings

DEBT_MAX = 0.33          # interest-bearing debt / market cap
LIQUID_MAX = 0.33        # (cash + short-term investments) / market cap
STALE_DAYS = 100         # re-screen if recorded verdict older than ~1 quarter


def ratio_precheck(ticker: str) -> dict:
    try:
        t = yf.Ticker(ticker)
        mcap = t.fast_info.get("marketCap")
        bs = t.balance_sheet
        def row(*names):
            for n in names:
                if n in bs.index:
                    v = float(bs.loc[n].iloc[0])
                    if v == v:  # skip NaN, try the next candidate name
                        return v
            return 0.0
        debt = row("Total Debt", "Long Term Debt") + row("Current Debt", "Short Long Term Debt")
        cash = row("Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments")
        if not mcap:
            return {"ok": None, "note": "no market cap"}
        debt_r, liq_r = debt / mcap, cash / mcap
        flags = []
        if debt_r > DEBT_MAX: flags.append(f"debt/mcap {debt_r:.0%} > {DEBT_MAX:.0%}")
        if liq_r > LIQUID_MAX: flags.append(f"liquid/mcap {liq_r:.0%} > {LIQUID_MAX:.0%}")
        return {"ok": not flags, "debt_ratio": round(debt_r, 3),
                "liquid_ratio": round(liq_r, 3), "flags": flags}
    except Exception as e:
        print(f"[warn] ratio precheck failed for {ticker}: {e}", file=sys.stderr)
        return {"ok": None, "note": str(e)}


def main() -> None:
    today = dt.date.today()
    out = []
    for h in load_holdings():
        m = h["meta"]
        s = m.get("shariah", {}) or {}
        screened = s.get("screened")
        stale = None
        if screened:
            d = screened if isinstance(screened, dt.date) else dt.date.fromisoformat(str(screened))
            stale = (today - d).days > STALE_DAYS
        out.append({
            "ticker": m["ticker"], "name": m.get("name", m["ticker"]),
            "recorded_status": s.get("status", "unknown"),
            "source": s.get("source", "—"),
            "screened": str(screened) if screened else None,
            "stale": stale,
            "ratio_precheck": ratio_precheck(m["ticker"]),
        })
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
