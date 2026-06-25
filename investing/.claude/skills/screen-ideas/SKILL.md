---
name: screen-ideas
description: Rank the user's universe.md by short-term mechanical signals (momentum, trend, RSI, volume, volatility) and return candidates to research. Use when the user asks to screen, rank, or find short-term trade ideas.
---

# Screen Ideas (short-term recommender)

Rank the user's own universe — never invent tickers, never predict winners, never
assert a name will be profitable. This surfaces facts and orders them by the
weights in rules.md. Compliance is informational (verify in their own tool).

## Steps
1. Run `python scripts/screener.py` and read the JSON — this is the pure mechanical
   rank (momentum/trend/RSI/volume/volatility) over universe.md.
2. Run `python scripts/recommend.py` and read its `ideas` array — this layers the
   PM-grade gates from the decision-logic note on top of watchlist.md entries:
   EDGE_GATE (is there a stated reason the market is wrong — the `why` column?),
   ASYMMETRY_GATE (reward:risk vs `reward_risk_min_swing` in rules.md, computed off
   a technical target/stop), CATALYST_GATE (a dated catalyst within
   `catalyst_horizon_days`). A screener.py score alone does NOT clear these gates —
   it's a signal, not an edge.
3. Optionally research the top BUY-CANDIDATE names for a near-term catalyst (web)
   and surface the catalyst AND the main risk side by side. Cite sources.
4. Present a ranked table: rank, ticker, verdict, score, and the key signals
   (3m/6m momentum, RSI, rel-volume, ATR%, vs-EMA50, distance from 52w high).
   Call out when a high-ranked name is overbought (RSI>80) or high-vol (ATR% high).
   For names also on watchlist.md, append recommend.py's verdict + the gate that
   capped it (e.g. "RESEARCH — no catalyst within 60d").
5. State plainly: BUY-CANDIDATE = cleared the mechanical bar the user set, NOT a
   prediction it will rise; each must be verified for compliance in their own tool
   and is their decision. For any name they act on, point to /apply-trade.

## Rules
- Rank only universe.md. If it's empty, ask the user to populate it.
- Show signals, not conclusions. No price targets, no return promises.
- Note honestly that short-term trading usually trails buy-and-hold after costs.
