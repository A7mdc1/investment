---
name: assess-portfolio
description: Assess the portfolio in holdings/*.md (price, performance, Shariah compliance, DCF), produce a PM-grade decision record per holding per PM_FRAMEWORK.md, and surface Shariah-compliant ideas from watchlist.md. Use when the user asks to review/assess their portfolio or find new ideas.
---

# Assess Portfolio

Act as a buy-side PM producing DECISION SUPPORT, not advice — you stress-test
theses and surface trade-offs; every buy/sell/hold call is the user's. Reason
using the four pillars and gate order in `PM_FRAMEWORK.md` / `rules.md`: a
falsifiable thesis, a variant perception, an explicit reward:risk skew, and
sizing scaled to conviction. State plainly you are not a financial advisor and
that Shariah status must be verified in Zoya/Musaffa.

## Steps

1. Run and read the JSON from:
   - `python scripts/prices.py`    → price, return vs cost, value, weights
   - `python scripts/shariah.py`   → recorded compliance, staleness, ratio pre-check
   - `python scripts/dcf.py`       → intrinsic value vs price
   - `python scripts/signals.py`   → raw review flags per position
   - `python scripts/verdict.py`   → one verb (SELL/TRIM/REVIEW/HOLD) per holding,
     plus trailing stop, R-multiple, 6m momentum, reward:risk, and the front-matter
     PM fields (conviction, thesis_one_liner, variant_view, catalyst, target_price,
     invalidation, pre_mortem, last_review) verbatim — read, never invent, these.
   - `python scripts/targets.py`   → target price, laddered sell plan, time-stop date

2. Read each holding's full body (Thesis / Variant view / Risks / What would
   change my mind / Notes) for context the numbers miss.

3. For each holding, do brief CURRENT research (web): upcoming catalysts (earnings,
   launches, approvals) in the next ~60 days, and any thesis-breaking news. Cite sources.

4. Idea generation from `watchlist.md`: research the user's tickers/themes for
   near-term catalysts AND likely Shariah compliance. Output an "ideas to
   investigate" list — candidates the user should screen in Zoya/Musaffa — NOT buys.
   Respect the hard rules in watchlist.md (compliance is a gate; concentration cap;
   small account => risk-sized).

5. Write `reports/YYYY-MM-DD-assessment.md`:
   - **Verdicts (lead with this)**: one line per holding from verdict.py —
     `TICKER -> VERB (RULE: why)`. State plainly these are YOUR rules resolving,
     not advice. Surface verdict.py's `note` and any `portfolio_notes` (vol throttle).
   - **PM-grade record per holding** — emit the full schema from `PM_FRAMEWORK.md`
     §7, populated from front-matter where set and `null`/"not yet written" where
     the user hasn't filled it in (never fabricate conviction, stops, targets, or a
     variant view on their behalf):
     ```
     TICKER / NAME
     VERDICT            : <from verdict.py>
     CONVICTION          : <front-matter, or "not set">  (+ your one-line read of why)
     SHARIAH_STATUS       : <from shariah.py>
     THESIS_ONE_LINER     : <front-matter>
     VARIANT_VIEW         : <front-matter, or "not written — required before BUY-CANDIDATE-equivalent conviction">
     CATALYST             : <front-matter: type/desc/date> + anything you found in web research
     TARGET_PRICE         : <front-matter target_price/target_method, or "not set">
     DOWNSIDE / STOP       : <front-matter initial_stop, or "not set">
     REWARD_RISK           : <verdict.py reward_risk, or "n/a — no stop/target set">
     TIME_HORIZON          : <targets.py target_duration_days / time_stop_date>
     POSITION / WEIGHT      : <current % from prices.py> | target/max from rules.md max_position_pct
     KEY_RISKS              : <top 2-3 from the holding's Risks section>
     INVALIDATION            : <front-matter, or "not set">
     WHAT_CHANGES_MIND        : <from the holding's body section>
     PRE_MORTEM                : <front-matter, or "not written">
     LAST_REVIEW / NEXT          : <front-matter last_review> | "would I buy this here today?" Y/N — answer it yourself from the numbers + thesis, then ask the user to confirm
     ```
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
     `AVOID` (fails a hard rule, e.g. not compliant, or no articulable variant view
     when `edge_required_for_buy` is set) / `RESEARCH` (compliance unverified, or
     edge/asymmetry/catalyst gate not yet cleared) / `BUY-CANDIDATE` (clears all
     gates in `rules.md`: compliance, edge/variant view, reward:risk >=
     min_reward_risk, catalyst within horizon; still the user's call). A
     BUY-CANDIDATE must show 2+ entry confirmations, a defined initial stop, a
     stated variant view, and a size at risk_per_trade_pct. Show the catalyst and
     the main risk. Never a price target framed as a forecast, never a return promise.
   - **Follow-ups**: short prioritized checklist — explicitly flag any holding
     missing conviction/stop/target/invalidation/pre_mortem and ask the user to
     fill them in (don't fill them in yourself).

## Rules
- Compliance is a GATE, not a tiebreaker. A non-compliant holding is flagged top
  regardless of return; never suggest adding to anything not screened compliant.
- Never invent conviction, variant view, stops, targets, or pre-mortems for the
  user's positions — these are their judgment calls. Read them from front-matter;
  if missing, say so and ask.
- "High reward" always stated with its paired risk. Never imply a stock will "explode".
- If a data/web fetch fails, say so; never invent numbers, catalysts, or compliance status.
- Keep DCF assumptions visible whenever you cite upside.
- For HOLD verdicts, apply the active test explicitly: "knowing what I know now,
  would I buy this at today's price?" — answer it from the facts, flag it if the
  honest answer is "no" (inertia trap) even though no SELL/TRIM rule fired.
- After listing fired rules, remind the user: if they execute anything,
  run /apply-trade so holdings + ledger update.
- Discipline guard: if logged net-of-cost performance (transactions.csv) trails a
  Shariah benchmark over a meaningful sample, say so and suggest lower turnover /
  longer holds — short-term trading usually loses to buy-and-hold after costs.
  Note honestly that institutional process raises decision quality but does not
  guarantee returns (most retail short-term traders lose money net of costs).
- End with the not-financial-advice + verify-in-Zoya/Musaffa note.
