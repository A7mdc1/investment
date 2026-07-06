"""signals.py — turn position data into REVIEW FLAGS.

These are decision-support signals for the user to act on themselves, NOT
buy/sell instructions. Each flag states a fact and why it's worth a look.
Highest-priority flags first: mandate (Shariah) > drawdown > valuation > position.
"""
from __future__ import annotations
import json
import sys
import yfinance as yf
from common import load_holdings

PE_RICH = 50           # P/E above this -> "rich multiple, growth must deliver"
DRAWDOWN_REVIEW = 0.15 # position down > this fraction -> review thesis
NEAR_LOW = 0.10        # within this % of 52w low -> note it


def price(ticker: str):
    try:
        return yf.Ticker(ticker).fast_info.get("lastPrice")
    except Exception as e:
        print(f"[warn] price {ticker}: {e}", file=sys.stderr)
        return None


def main() -> None:
    out = []
    for h in load_holdings():
        m = h["meta"]
        px = price(m["ticker"]) or m.get("last_price")
        flags = []

        # 1. Mandate: Shariah compliance is the highest-priority check.
        status = (m.get("shariah") or {}).get("status", "unknown")
        if status == "non-compliant":
            flags.append({"priority": 1, "type": "mandate",
                          "msg": "Flagged NON-compliant — off-policy for a Shariah mandate, "
                                 "independent of price. Decide on exit/timing; verify in Zoya/Musaffa."})
        elif status in ("doubtful", "unknown"):
            flags.append({"priority": 1, "type": "mandate",
                          "msg": f"Compliance status '{status}' — re-screen before adding."})
        pur = (m.get("shariah") or {}).get("purification_pct")
        if pur and pur >= 5:
            flags.append({"priority": 2, "type": "purification",
                          "msg": f"Purification ratio {pur}% is high — more income to purify."})

        # 2. Drawdown vs cost.
        cost = m.get("cost_basis")
        if px and cost:
            dd = (px - cost) / cost
            if dd <= -DRAWDOWN_REVIEW:
                flags.append({"priority": 2, "type": "drawdown",
                              "msg": f"Down {dd:.0%} vs cost — revisit whether the thesis still holds."})

        # 3. Valuation.
        pe = m.get("pe")
        if pe and pe >= PE_RICH:
            flags.append({"priority": 3, "type": "valuation",
                          "msg": f"P/E ~{pe:g}: rich; growth has to keep delivering to justify it."})

        # 4. Position vs 52-week range.
        lo, hi = m.get("week52_low"), m.get("week52_high")
        if px and lo and hi:
            span = hi - lo
            if span > 0:
                pos = (px - lo) / span
                if px <= lo * (1 + NEAR_LOW):
                    flags.append({"priority": 3, "type": "range",
                                  "msg": f"Near 52w low (${lo:g}-${hi:g}) — could be value or a falling knife; check why."})
                out_pos = round(pos * 100)
            else:
                out_pos = None
        else:
            out_pos = None

        out.append({"ticker": m["ticker"], "name": m.get("name"), "price": px,
                    "pct_of_52w_range": out_pos,
                    "flags": sorted(flags, key=lambda f: f["priority"])})
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
