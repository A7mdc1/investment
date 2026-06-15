---
name: screen-ideas
description: Rank the user's universe.md by short-term mechanical signals (momentum, trend, RSI, volume, volatility) and return candidates to research. Use when the user asks to screen, rank, or find short-term trade ideas.
---

# Screen Ideas (short-term recommender)

Rank the user's own universe — never invent tickers, never predict winners, never
assert a name will be profitable. This surfaces facts and orders them by the
weights in rules.md. Compliance is informational (verify in their own tool).

## Steps
1. Run `python scripts/screener.py` and read the JSON.
2. Optionally research the top BUY-CANDIDATE names for a near-term catalyst (web)
   and surface the catalyst AND the main risk side by side. Cite sources.
3. Present a ranked table: rank, ticker, verdict, score, and the key signals
   (3m/6m momentum, RSI, rel-volume, ATR%, vs-EMA50, distance from 52w high).
   Call out when a high-ranked name is overbought (RSI>80) or high-vol (ATR% high).
4. State plainly: BUY-CANDIDATE = cleared the mechanical bar the user set, NOT a
   prediction it will rise; each must be verified for compliance in their own tool
   and is their decision. For any name they act on, point to /apply-trade.

## Rules
- Rank only universe.md. If it's empty, ask the user to populate it.
- Show signals, not conclusions. No price targets, no return promises.
- Note honestly that short-term trading usually trails buy-and-hold after costs.
