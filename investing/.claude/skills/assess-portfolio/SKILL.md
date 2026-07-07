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

0. **Auto-discovery + scaffold (synchronous, runs first).** Run
   `python scripts/discover.py`, then `python scripts/scaffold.py --all-leads`.
   Discovery builds a fresh candidate pool (halal-ETF holdings + yfinance screens),
   applies the liquidity floor + Shariah/asymmetry/catalyst gates, and **writes
   `leads.md`** (machine-generated, overwritten every run). It does NOT touch
   `watchlist.md` (hand-curated). Scaffold then auto-fills a **DRAFT setup card**
   (`setups/<ticker>.md`, `status: draft`) for every lead without one — complete
   proposed trade plans (entry/stop/target/logic/invalidation) from Yahoo formula
   outputs, so the report can present them for review. Needs live Yahoo data — if
   discovery returns an empty pool / DATA_GAP (e.g. this cloud sandbox blocks
   Yahoo), say so and carry on with the existing `watchlist.md` + `setups/`; never
   fabricate names or levels. **Two invariants:** a DRAFT card can never reach
   BUY-CANDIDATE until the owner reviews it and sets `status: planned`; the scaffold
   never writes `shariah: compliant` (only a human Zoya/Musaffa screen does).

1. Run and read the JSON from:
   - `python scripts/prices.py`    → price, return vs cost, value, weights
   - `python scripts/shariah.py`   → recorded compliance, staleness, ratio pre-check
   - `python scripts/dcf.py`       → intrinsic value vs price
   - `python scripts/signals.py`   → raw review flags per position
   - `python scripts/verdict.py`   → one verb per holding + trailing stop, R-multiple,
     6m momentum, and portfolio vol-throttle notes, all driven by rules.md
   - `python scripts/recommend.py` → the PM-grade layer on top: a structured record
     per holding/watchlist idea (conviction, reward:risk, catalyst, invalidation —
     schema from the PM decision-logic note). It enforces the edge/asymmetry/catalyst
     gates mechanically but CANNOT supply a real variant view or conviction call —
     where `conviction_why` says input is missing, that's your cue to supply it
     (thesis text in the holding's `.md`, or a `why`/catalyst column in watchlist.md),
     not something to paper over.

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
     Below each verdict, add the PM-grade record from recommend.py (conviction +
     why, reward:risk, target/stop and method, time horizon, "would I buy here
     today?") — label these as mechanical proxies, not a real conviction call.
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
     `AVOID` (fails a hard rule, e.g. Shariah ratio/business knockout) / `RESEARCH`
     (no completed setup card, Shariah unverified, or no catalyst within horizon —
     underwrite before anything) / `BUY-CANDIDATE` (clears every gate; still YOUR
     call). Use `python scripts/recommend.py`'s `ideas` array as the mechanical
     first pass — it enforces EDGE_GATE (a completed `setups/<ticker>.md` card, not
     a `why` string), ASYMMETRY_GATE (reward:risk >= `reward_risk_min_swing`),
     CATALYST_GATE (a dated catalyst within `catalyst_horizon_days`), and
     SHARIAH_GATE (the card's `shariah.status` must be `compliant` and fresh) —
     then layer your web research for the actual catalyst facts and main risk on
     top. UNVERIFIED can never be BUY-CANDIDATE; discovery leads are `LEAD` until a
     card is written and the name is screened in Zoya/Musaffa. Never a price target
     framed as a promise of returns.
   - **Draft & planned setups**: render the setup cards in `setups/`.
     - **DRAFT cards** (machine-filled by scaffold.py) — show the full proposed
       plan under the verdict line
       `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`:
       setup_type, entry/stop/target with R:R, the entry-trigger / stop / target /
       invalidation logic text, the gap plan, and the Shariah pre-check comment.
       Present these as *proposals to review and edit*, never as buys. Make clear
       every level is a formula output, and that approval means editing what you
       disagree with and flipping `status: planned`.
     - **PLANNED/LIVE cards** — render as a normal PM record; this is the ONLY
       place a BUY-CANDIDATE can appear, and only when the card is complete AND
       carries a human-verified `shariah: compliant` (fresh). Draft cards can never.
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
