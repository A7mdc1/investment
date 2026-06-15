---
name: assess-portfolio
description: Assess the portfolio in holdings/*.md (price, performance, Shariah compliance, DCF), produce review flags and catalyst research, and surface Shariah-compliant ideas from watchlist.md. Use when the user asks to review/assess their portfolio or find new ideas.
---

# Assess Portfolio

Act as a careful analyst producing DECISION SUPPORT, not advice. Surface facts,
flags, and trade-offs; leave every buy/sell/hold call to the user. Never phrase
output as a recommendation or a promise of returns. State that you are not a
financial advisor and that Shariah status must be verified in Zoya/Musaffa.

## Steps

1. Run and read the JSON from:
   - `python scripts/prices.py`    → price, return vs cost, value, weights
   - `python scripts/shariah.py`   → recorded compliance, staleness, ratio pre-check
   - `python scripts/dcf.py`       → intrinsic value vs price
   - `python scripts/signals.py`   → raw review flags per position
   - `python scripts/verdict.py`   → one verb per holding + trailing stop, R-multiple,
     6m momentum, and portfolio vol-throttle notes, all driven by rules.md

2. Read each holding's thesis/risks/notes for context the numbers miss.

3. For each holding, do brief CURRENT research (web): upcoming catalysts (earnings,
   launches, approvals) in the next ~60 days, and any thesis-breaking news. Cite sources.

4. Idea generation from `watchlist.md`: research the user's tickers/themes for
   near-term catalysts AND likely Shariah compliance. Output an "ideas to
   investigate" list — candidates the user should screen in Zoya/Musaffa — NOT buys.
   Respect the hard rules in watchlist.md (compliance is a gate; concentration cap;
   small account => risk-sized).

5. Write `reports/YYYY-MM-DD-assessment.md`:
   - **Verdicts (lead with this)**: one line per holding from verdict.py —
     `TICKER -> VERB  (RULE: why)`, plus its trailing stop and distance to it,
     R-multiple, and 6m momentum. State plainly these are YOUR rules resolving,
     not advice. Surface verdict.py's `note` and any `portfolio_notes` (vol throttle).
   - **Snapshot**: total value, weights, per-name return.
   - **Action flags (priority order)**: from signals.py. Lead with mandate
     (non-compliant / stale) flags — these are policy issues, not price calls.
   - **Per-holding read**: does the recorded thesis still hold given numbers +
     catalysts? Lay out the case to keep vs the case to trim, with the facts for
     each. Do NOT pick one for the user.
   - **Suggested actions (from YOUR rules)**: read `rules.md`; for each rule whose
     condition matches current data, list it as "Rule <NAME> fired -> <your pre-set
     action>", with the supporting fact. These are the user's own pre-committed
     rules, not advice from the tool. The routine never auto-trades.
   - **DCF**: intrinsic vs price, with the assumptions stated.
   - **New ideas**: from step 4, give each a verb too —
     `AVOID` (fails a hard rule, e.g. not compliant) / `RESEARCH` (compliance
     unverified — screen before anything) / `BUY-CANDIDATE` (passes your gates;
     still YOUR call). A BUY-CANDIDATE must show 2+ entry confirmations (momentum/
     breakout+volume/pullback/catalyst), a defined initial stop, and a size at
     risk_per_trade_pct. Show the catalyst and the main risk. Never a price target
     or a promise of returns.
   - **Follow-ups**: short prioritized checklist.

## Rules
- Compliance is a GATE, not a tiebreaker. A non-compliant holding is flagged top
  regardless of return; never suggest adding to anything not screened compliant.
- "High reward" always stated with its paired risk. Never imply a stock will "explode".
- If a data/web fetch fails, say so; never invent numbers, catalysts, or compliance status.
- Keep DCF assumptions visible whenever you cite upside.
- After listing fired rules, remind the user: if they execute anything,
  run /apply-trade so holdings + ledger update.
- Discipline guard: if logged net-of-cost performance (transactions.csv) trails a
  Shariah benchmark over a meaningful sample, say so and suggest lower turnover /
  longer holds — short-term trading usually loses to buy-and-hold after costs.
- End with the not-financial-advice + verify-in-Zoya/Musaffa note.
