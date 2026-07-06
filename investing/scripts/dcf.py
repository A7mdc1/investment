"""dcf.py — transparent 2-stage free-cash-flow DCF.

Per-holding assumptions live in each holding's front-matter under `dcf:`
(growth_5y, terminal_growth, discount_rate). Missing values fall back to the
defaults below. Output: intrinsic value/share vs current price -> upside %.

This is a simple model meant for *your* judgment, not a recommendation.
Garbage in, garbage out — sanity-check the FCF base and the assumptions.
"""
from __future__ import annotations
import json
import sys
import yfinance as yf
from common import load_holdings

DEFAULTS = {"growth_5y": 0.05, "terminal_growth": 0.025, "discount_rate": 0.10}
YEARS = 5


def base_fcf(t: yf.Ticker) -> float | None:
    """Latest free cash flow = operating cash flow - capex."""
    try:
        cf = t.cashflow
        def row(*names):
            for n in names:
                if n in cf.index:
                    v = float(cf.loc[n].iloc[0])
                    if v == v:  # skip NaN, try the next candidate name
                        return v
            return None
        fcf = row("Free Cash Flow")
        if fcf is not None:
            return fcf
        ocf = row("Operating Cash Flow", "Total Cash From Operating Activities")
        capex = row("Capital Expenditure", "Capital Expenditures")
        if ocf is not None and capex is not None:
            return ocf + capex  # capex is reported negative
    except Exception as e:
        print(f"[warn] fcf failed: {e}", file=sys.stderr)
    return None


def dcf(ticker: str, a: dict) -> dict:
    try:
        t = yf.Ticker(ticker)
        fcf = base_fcf(t)
        fi = t.fast_info
        shares = fi.get("shares")
        price = fi.get("lastPrice")
        if not fcf or not shares:
            return {"ok": False, "note": "missing FCF or share count"}
        g, tg, r = a["growth_5y"], a["terminal_growth"], a["discount_rate"]
        pv, cf = 0.0, fcf
        for yr in range(1, YEARS + 1):
            cf *= (1 + g)
            pv += cf / (1 + r) ** yr
        terminal = cf * (1 + tg) / (r - tg)
        pv += terminal / (1 + r) ** YEARS
        net_debt = 0.0
        try:
            bs = t.balance_sheet
            def b(*n):
                for x in n:
                    if x in bs.index:
                        v = float(bs.loc[x].iloc[0])
                        if v == v:  # skip NaN, try the next candidate name
                            return v
                return 0.0
            net_debt = b("Total Debt", "Long Term Debt") - b(
                "Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments")
        except Exception:
            pass
        equity = pv - net_debt
        iv = equity / shares
        upside = ((iv - price) / price * 100) if price else None
        return {"ok": True, "intrinsic_value": round(iv, 2), "price": price,
                "upside_pct": round(upside, 1) if upside is not None else None,
                "assumptions": a}
    except Exception as e:
        return {"ok": False, "note": str(e)}


def main() -> None:
    out = []
    for h in load_holdings():
        m = h["meta"]
        a = {**DEFAULTS, **(m.get("dcf") or {})}
        out.append({"ticker": m["ticker"], "name": m.get("name", m["ticker"]),
                    "dcf": dcf(m["ticker"], a)})
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
