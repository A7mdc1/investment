---
name: screen-ideas
description: Rank the user's universe.md by short-term mechanical signals (momentum, trend, RSI, volume, volatility), then apply the PM_FRAMEWORK.md edge/asymmetry/catalyst gates before calling anything BUY-CANDIDATE. Use when the user asks to screen, rank, or find short-term trade ideas.
---

# Screen Ideas (short-term recommender)

Rank the user's own universe — never invent tickers, never predict winners, never
assert a name will be profitable. screener.py's score is a MECHANICAL pre-filter
only; per `PM_FRAMEWORK.md`'s new-idea triage (screen -> RESEARCH -> BUY-CANDIDATE
/ AVOID), a name still needs an articulated edge and a defined asymmetry before it
can be called a true BUY-CANDIDATE. Compliance is informational (verify in their
own tool) but is still the first knockout gate per `rules.md`.

## Steps
1. Run `python scripts/screener.py` and read the JSON. Treat its "BUY-CANDIDATE"
   as "cleared the mechanical bar" only — not yet the PM-grade label.
2. For each name that cleared the mechanical bar, research (web) for a near-term
   catalyst (hard: dated event, or soft: time/re-rating) and try to articulate a
   variant view — specifically why the market might have this priced wrong
   (informational / analytical / behavioral edge). Cite sources.
3. Apply the gates from `rules.md` to reclassify each into the PM vocabulary:
   - **AVOID** — fails compliance, or fails a hard knockout (no catalyst at all /
     untrustworthy data / outside what you can analyze).
   - **RESEARCH** — cleared the mechanical bar but no variant view can yet be
     articulated, OR reward:risk can't be computed/cleared `min_reward_risk`
     (`min_reward_risk_swing` for short-horizon setups), OR no catalyst within
     the holding horizon. This is most names — that's expected, not a failure.
   - **BUY-CANDIDATE** — clears compliance AND has a stated variant view AND a
     computable reward:risk >= the relevant threshold AND a catalyst inside the
     horizon AND a defined stop. Show all four explicitly; if any is missing, it
     is RESEARCH, regardless of the mechanical score.
4. Present a ranked table: rank, ticker, PM label, mechanical score, and the key
   signals (3m/6m momentum, RSI, rel-volume, ATR%, vs-EMA50, distance from 52w
   high). Call out when a high-ranked name is overbought (RSI>80) or high-vol
   (ATR% high).
5. State plainly: BUY-CANDIDATE here means it cleared the user's pre-committed
   gates, NOT a prediction it will rise; compliance must still be verified in
   their own tool and the decision is theirs. For any name they act on, point to
   /apply-trade — and remind them a stop, target, and pre-mortem belong in the
   new holding file at entry.

## Rules
- Rank only universe.md. If it's empty, ask the user to populate it.
- Show signals, not conclusions. No price targets framed as forecasts, no return promises.
- Never call something BUY-CANDIDATE on the mechanical score alone — the edge,
  asymmetry, and catalyst gates must all be shown to clear, explicitly.
- Note honestly that short-term trading usually trails buy-and-hold after costs.
