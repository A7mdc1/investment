"""prices.py — current price, return vs cost basis, position value, portfolio weight.

Usage:  python scripts/prices.py
Output: JSON to stdout (so the skill / Claude can read it).
Tadawul tickers use the .SR suffix, e.g. 2222.SR for Aramco.
"""
from __future__ import annotations
import json
import sys
import yfinance as yf
from common import load_holdings


def fetch_price(ticker: str) -> float | None:
    try:
        t = yf.Ticker(ticker)
        # fast_info is cheaper/more reliable than .info
        px = t.fast_info.get("last_price")
        if px is None:
            hist = t.history(period="5d")
            px = float(hist["Close"].iloc[-1]) if not hist.empty else None
        return float(px) if px is not None else None
    except Exception as e:
        print(f"[warn] price fetch failed for {ticker}: {e}", file=sys.stderr)
        return None


def main() -> None:
    rows, total = [], 0.0
    for h in load_holdings():
        m = h["meta"]
        px = fetch_price(m["ticker"])
        shares = m.get("shares", 0) or 0
        cost = m.get("cost_basis")
        value = (px * shares) if (px and shares) else None
        if value:
            total += value
        ret = ((px - cost) / cost * 100) if (px and cost) else None
        rows.append({
            "ticker": m["ticker"], "name": m.get("name", m["ticker"]),
            "price": px, "shares": shares, "cost_basis": cost,
            "return_pct": round(ret, 2) if ret is not None else None,
            "value": round(value, 2) if value else None,
            "currency": m.get("currency", "USD"),
        })
    for r in rows:  # portfolio weight needs the total, so do a second pass
        r["weight_pct"] = round(r["value"] / total * 100, 2) if (r["value"] and total) else None
    print(json.dumps({"total_value": round(total, 2), "positions": rows}, indent=2))


if __name__ == "__main__":
    main()
