# How a Senior Portfolio Manager Reasons About Buy / Hold / Trim / Sell — and How to Encode It

## TL;DR

- A senior PM does not “rate” stocks; they make **capital-allocation decisions** built on four pillars — a falsifiable thesis, a *variant perception* (a well-founded view different from consensus that is also correct), an explicit reward-to-risk skew (commonly demanding ~3:1 upside-to-downside), and a position size scaled to conviction — and every decision label is the output of those pillars, not a score.
- Your seven labels map cleanly onto this logic: **SELL** = thesis broken / target reached / better use of capital; **TRIM** = conviction or skew has decayed or position has outgrown its risk budget; **REVIEW** = a trigger has fired and the thesis must be re-underwritten; **HOLD** = passes the “would I buy it here today?” test; **BUY-CANDIDATE** = cleared the bar, awaiting entry/sizing; **RESEARCH** = promising but not yet underwritten; **AVOID** = fails a knockout criterion.
- For a Shariah-compliant Saudi swing trader, the PM discipline that matters most is *process over outcome*, pre-written sell/invalidation rules, and asymmetry — but be honest: institutional process raises decision quality, it does not guarantee returns, and the documented retail short-term-trading odds (the majority lose money net of costs) still apply. A Shariah knockout screen should sit *first* in the pipeline as an absolute AVOID filter.

## Key Findings

**1. PMs decide, analysts rate.** The single most important distinction in your task: a *sell-side* analyst issues Buy/Hold/Sell ratings relative to a price target over 6–12 months and is incentivized to generate activity; a *buy-side* PM makes a decision with “skin in the game” and real monetary consequences, is longer-horizon, and is far more focused on *risk* — stress-testing the thesis and asking “what could go wrong” rather than just identifying upside. Your engine should behave like the buy-side: every label is a position decision, not an opinion.

**2. The thesis must be falsifiable and built on a variant perception.** Howard Marks’ “second-level thinking” frames it: first-level thinking says “good company, buy it”; second-level thinking asks “is the goodness already in the price, and what do I see that the consensus has wrong?” Mispricing — what Marks calls the only source of superior performance — comes from “mistakes, things the market misprices,” which “come from ignorance and prejudice.” Sonkin & Johnson make this operational: a genuine mispricing requires you to demonstrate an **informational, analytical, or trading advantage**  — in Sonkin’s exact words, “You either have an informational advantage, an analytical advantage, or a cost or trading advantage. There’s no fourth advantage.” This is rooted in Fama: a mispricing can only arise if information fails to be “adequately disseminated, processed absent any systematic bias, and then incorporated into the stock price.” If you cannot say specifically why the consensus is wrong and why you are right, you probably haven’t found a mispricing.

**3. Conviction is edge × evidence, and it drives size.** Professional sizing is conviction-weighted, frequently Kelly-influenced but never full-Kelly. The practitioner consensus: compute Kelly as a *ceiling/reference*, then apply fractional Kelly (half or third) plus hard caps for estimation error, volatility, correlation, and drawdown. Real funds cap single positions: high-conviction names commonly top out around 10%, with initial positions of 1–2%.

**4. The buy bar is an asymmetric payoff.** PMs require the upside to be a multiple of the downside — a widely cited minimum is **3:1**. Crucially, asymmetry is *engineered* (predefined downside via exit discipline, entry price, sizing), not merely asserted because a stock “looks cheap.”

**5. Selling is the weakest muscle — for pros and retail alike.** Per Li An & Bronson Argyle, “Overselling Winners and Losers” (*Journal of Financial Markets*, Sept 2021; 1980–2018 data): “Given an unrealised gain and loss of the same magnitude, mutual fund managers are 1.8 times as likely to sell the gain as to sell the loss” — and they exhibit a “V-shaped disposition effect,” more likely to sell *both* big winners and big losers. Marks’ “Selling Out” memo argues you should *not* sell merely because a price is up or down; you sell on thesis change, relative opportunity, or valuation reaching fair value. The PM antidote is **pre-written sell rules and thesis-invalidation triggers set at entry**, before emotion is engaged.

**6. Process over outcome is the governing philosophy.** Mauboussin: “We have no control over outcomes, but we can control the process.”  Good decisions sometimes lose; bad decisions sometimes win; over time process dominates. This justifies judging your engine by the quality of its documented reasoning, not by any single trade’s P&L — and it is the strongest argument for the structured, field-by-field output you want.

## Details

### 1. Conviction and decision frameworks

**Conviction levels and their meaning.** PMs typically run three conviction tiers — high / medium / low — and translate them directly into weight. Conviction is not enthusiasm; it is the product of (a) the *size* of the gap between price and value, and (b) the *strength of evidence* that your variant view is correct. Sonkin & Johnson’s variant-perception rule captures the tension precisely: “the farther away your view is from the consensus, the bigger the price difference… and the greater the opportunity, but the harder it is to prove that you are right.”  High conviction therefore requires *both* a large mispricing *and* strong, specific evidence — not one or the other. They define variant perception itself (borrowing Michael Steinhardt’s framework) as holding “a view that is different from the consensus and you are right” — both conditions must hold.

**Edge has exactly three sources.** Per Sonkin & Johnson (and echoed by Mauboussin and Bill Miller): an **informational** advantage (you know something legally that others don’t, or you assemble a mosaic), an **analytical** advantage (same public data, superior interpretation — this *is* variant perception), or a **trading/cost** advantage (you can transact or hold when others can’t).  Mauboussin adds a fourth practical category, *behavioral* edge (discipline when others panic). For a retail swing trader competing against institutions, the honest available edges are mostly **analytical and behavioral** — your engine’s value is enforcing behavioral discipline systematically.

**Good company ≠ good investment.** Marks: “No asset is so good that it can’t be a bad investment if bought at too high a price,”  and conversely bargains live “in things that are controversial or performing poorly.”  The engine must always separate business quality from the *expectations embedded in the price*. Mauboussin’s “expectations investing” formalizes this: start from the price, decode what the market is implying about future cash flows, and only invest where your well-founded expectations differ. 

**Thesis and pre-defined invalidation.** A professional thesis is a falsifiable claim: *what* is mispriced, *why* the market has it wrong (which crowd-failure condition is in play), and *what would prove me wrong*. Invalidation criteria must be of the *same type* as the thesis — if you bought for an earnings re-rating, you exit on evidence the re-rating won’t happen, not on an unrelated price wiggle.  Invalidation (thesis broken) is distinct from a stop-loss (defensive price limit); sophisticated processes use both. 

### 2. The recommendation / investment-memo structure

The institutional-grade stock pitch has a stable skeleton across hedge-fund memos, the Sohn-style pitch, and buy-side one-pagers:

1. **Recommendation / verdict** — direction, current price, target, and conviction, up front (BLUF).
1. **Business in one or two lines** — what it does, how it makes money, key figures.
1. **Investment thesis** — the 2–3 reasons the market is mispricing it, and *why* the market is wrong.
1. **Variant perception** — explicitly, your view vs. consensus and the evidence.
1. **Catalyst(s)** — the event(s) that will close the price-to-value gap, with timing.
1. **Valuation / target** — method and the upside it implies.
1. **Risks and mitigants** — the 2–3 things that break the thesis, and how you’d limit damage.
1. **Reward-to-risk** — base / upside / downside scenarios and the skew.
1. **Sizing and time horizon** — entry weight, max weight, expected holding period.
1. **What would change my mind** — the invalidation triggers.

Sonkin & Johnson compress the entire pitch into **four questions every pitch must answer**: “How much can I make? How much can I lose? Why is it trading at [this price]? How’s the market going to figure it out?”  Their single most important craft point is the **time-allocation inversion** — in Paul Johnson’s words: “If you inverted the time allocation and spend 90% of your time explaining what the market is missing and why the stock is mispriced, rather than 90% of your time trying to justify your valuation… the portfolio manager will listen intently.” Their catalyst definition is the cleanest available: “any event that begins to close the gap between the stock price and your estimate of intrinsic value”  — split into **hard catalysts** (a specific dated event) and **soft catalysts** (time itself).  They also frame the three components of return as the **price you pay, your estimate of intrinsic value, and the estimated time horizon** — noting most investors over-focus on intrinsic value and badly neglect time horizon.

**Institutional vs. amateur.** What separates the two: a falsifiable thesis with explicit invalidation; an articulated consensus view and why it’s wrong; quantified reward/risk rather than “lots of upside”; pre-defined sizing and exit; and language discipline — Sonkin & Johnson note hedge words (“may,” “might,” “could”) “destroy credibility.” Be clear on the buy-side/sell-side difference: sell-side “Hold” is often a soft “Sell”; your engine has no such political constraints and should say what it means.

### 3. Each decision, as a PM reasons it

**BUY / initiate (→ BUY-CANDIDATE then BUY).** Required conditions: a clear thesis + variant perception; an identified edge; an asymmetric payoff (commonly ≥3:1 upside:downside); at least one catalyst with a timeframe; and a defined entry and size. A PM enters at a fraction of target weight and adds as the thesis confirms. The minimum-skew hurdle is the gate: if downside isn’t both *defined* and *much smaller* than upside, it’s not a buy.

**HOLD.** Holding is an *active* decision, not inertia. The governing test: **“Knowing what I know now, would I buy this at today’s price?”** If yes, hold. If you’d neither buy nor sell, that’s the inertia trap — flag it for REVIEW. Holding always carries opportunity cost: a HOLD implicitly claims this position beats the best alternative use of the capital.

**TRIM / scale down.** Triggers: (a) conviction has fallen but thesis isn’t broken; (b) price has reached part of the target / reward:risk has compressed as the gap closed; (c) the position has grown beyond its risk budget (position-size discipline / rebalancing); (d) risk management — taking partial profits to de-risk. Trimming is how a PM stays invested in a winner while respecting max-position limits.

**SELL / exit.** Legitimate reasons: **thesis break** (the *why* is now false); **catalyst failure** (the event won’t happen or has passed with no re-rating); **valuation target reached** (price ≈ value, edge gone); **better opportunity** (capital reallocation to a higher reward:risk idea); or **stop/risk discipline** breached. Marks’ caution: don’t sell *just* because the price moved. The discipline cuts both ways — sell losers when the thesis breaks (don’t ride them down hoping), and sell winners when value is realized (don’t anchor to a high-water mark).

**New-idea triage.** The funnel: **screen → RESEARCH → BUY-CANDIDATE / AVOID.**

- **RESEARCH** = passed the screen, deserves a deep dive / underwriting; thesis not yet proven.
- **BUY-CANDIDATE** = cleared the full bar (thesis, edge, skew, catalyst) and sits “on the bench” awaiting entry price, sizing, or timing.
- **AVOID** = fails a **knockout criterion**. Typical knockouts: fails the Shariah screen (absolute, for this user); no identifiable edge / can’t articulate why the market is wrong; reward:risk below the minimum skew; no catalyst within the horizon (“dead money”); broken or fraudulent accounting / untrustworthy management; un-analyzable (outside competence); or a crowded/over-owned trade where you’re “late to the party.”

### 4. Risk management and sizing as a PM

- **Conviction-weighted sizing**, often Kelly-influenced. Kelly (f* = edge/odds) is best used as a *theoretical ceiling and discipline*, not a literal target;  practitioners apply **fractional Kelly** (½ or ⅓) to cushion estimation error. The same stock can deserve 2% in one book and 15% in another depending on edge and the rest of the portfolio. 
- **Hard caps.** Real funds cap single names — high-conviction positions commonly around 10%, initial positions 1–2%. Caps exist because “anyone can stumble”  and to survive estimation error.
- **Volatility-weighting and the 1% rule.** Swing traders commonly risk a fixed fraction (often ~1%) of equity per trade, sizing the position from the distance to the stop.  This is the retail-scale analogue of institutional risk budgeting and is directly codifiable.
- **Portfolio construction.** Watch correlation and factor exposure — several positions in one sector are one bet, not several. Diversify enough to survive being wrong; concentrate enough for winners to matter (a common professional sweet spot is ~20–25 names for a long-only book;  a swing book may hold fewer).
- **Drawdown discipline.** Pre-set portfolio-level risk reduction thresholds (e.g., scale down after a defined drawdown).
- **The core asymmetry.** Cut losers, let winners run. The disposition effect pushes the opposite; written rules counteract it.
- **The concentration debate (present both sides).** Tiger-cub managers (e.g., Lee Ainslie’s Maverick) run concentrated, high-conviction books  and obsess over management quality;  others argue most investors over-concentrate and that periodic rebalancing of a more equal-weighted book quietly harvests winners. There is no settled answer — the engine should let the user pick a stance and then enforce it consistently.

### 5. Catalysts and time horizon

- **Hard vs. soft catalysts.** Hard = dated, specific (earnings, product launch, regulatory decision, M&A close). Soft = the passage of time and gradual recognition. A PM wants at least one catalyst within the holding horizon; for a swing trader the catalyst should be near-term and the position has an implied *temporal* deadline.
- **Target price and method.** Set a target with an explicit method (multiple re-rating, DCF, sum-of-parts, technical level for short-term trades) and the upside it implies; revisit it as facts change.
- **Time horizon as a falsification condition.** A breakout or event thesis is *temporally bounded by its own logic* — if the expected move hasn’t occurred within the window the thesis implied, that is evidence against the thesis, structurally equivalent to hitting a price stop.  Record the time limit at entry. 
- **“Dead money” / opportunity cost.** Even with the thesis intact, capital tied up in a non-performing position with no near catalyst should trigger a REVIEW or TRIM — the opportunity cost of not deploying into a live idea is itself a reason to act. 

### 6. Behavioral discipline and process

- **The biases to guard against:** disposition effect (sell winners early, ride losers), anchoring (to purchase price or past highs), confirmation bias (seeking only supporting evidence), and sunk-cost/escalation (averaging down to justify a prior decision).
- **Pre-mortem.** Before entry, assume the trade has already failed and list why. The technique rests on Mitchell, Russo & Pennington (1989), “Back to the Future” (Wharton/Cornell/Univ. of Colorado), as cited in Gary Klein’s 2007 *Harvard Business Review* article: “prospective hindsight—imagining that an event has already occurred—increases the ability to correctly identify reasons for future outcomes by 30%.” Encode a mandatory pre-mortem field at entry. (Notably, Sonkin, Johnson and Klein co-authored a paper on the *misuse* of pre-mortems on Wall Street — do it as independent written generation, not a group brainstorm dominated by the loudest voice.)
- **Investment journal + decision/outcome separation.** Record the thesis, expected catalyst, target, invalidation, and pre-mortem at entry; review against outcomes later to calibrate.  Judge decisions by *process quality*, not just P&L (Mauboussin).
- **Review cadence.** Schedule periodic re-underwriting (e.g., on each earnings print, on catalyst dates, and at a fixed calendar interval). A REVIEW verdict is the engine’s way of forcing the “would I buy it here today?” test on a trigger.

### 7. Encodable output — recommended schema

For **every holding or idea**, the engine should emit a structured record. This is the deterministic, PM-grade documentation layer:

```
TICKER / NAME
VERDICT            : SELL | TRIM | REVIEW | HOLD | BUY-CANDIDATE | RESEARCH | AVOID
CONVICTION         : HIGH | MEDIUM | LOW   (+ one-line rationale)
SHARIAH_STATUS     : PASS | FAIL | REVIEW  (business screen + ratio screen; FAIL ⇒ AVOID)
THESIS_ONE_LINER   : the claim in one sentence
VARIANT_VIEW       : my view vs. consensus + which edge (info / analytical / behavioral)
CATALYST           : description | type (HARD/SOFT) | expected date/window
TARGET_PRICE       : level | method | implied upside %
DOWNSIDE           : level | implied downside %
REWARD_RISK        : ratio (require ≥ 3:1 for BUY-CANDIDATE)
TIME_HORIZON       : expected holding period / temporal deadline
POSITION / WEIGHT  : current % | target % | max %
RISK_PER_TRADE     : % of equity at risk to the stop
KEY_RISKS          : top 2–3
INVALIDATION       : the precise trigger(s) that break the thesis (same type as thesis)
STOP               : price-based defensive level (distinct from invalidation)
WHAT_CHANGES_MIND  : conditions that would flip the verdict
PRE_MORTEM         : top 2–3 reasons this fails (recorded at entry)
LAST_REVIEW / NEXT : dates + "would I buy here today?" Y/N
```

**Example PM-grade phrasing per label** (the tone your output should hit):

- **BUY-CANDIDATE (HIGH):** “Cleared the bar. Thesis: margins inflect as the new capacity ramps while consensus still models flat margins — analytical edge. Hard catalyst: Q-report in 5 weeks. Target X (re-rating to peer multiple), +35% vs. −10% downside to support = 3.5:1. Awaiting entry on a pullback to the breakout level; initial 2%, max 8%. Invalidates if gross margin prints flat or down.”
- **RESEARCH:** “Screened in on valuation + improving order book, but I can’t yet articulate why the market is wrong. Underwrite the channel and verify the backlog before it earns a verdict. Not investable today.”
- **AVOID (knockout):** “Fails Shariah ratio screen (debt > 30% of market cap). Absolute exclusion regardless of setup. Re-test after next audited statements.”
- **HOLD (MEDIUM):** “Thesis intact, catalyst (regulatory approval) still pending. Would I buy here today? Yes, marginally — reward:risk now ~2:1 after the run. Hold at current 6%; do not add. Next review at the decision date.”
- **TRIM:** “Hit two-thirds of target; reward:risk compressed from 3:1 to 1.3:1 and the position has grown to 11% — above the 8% cap. Trim to 6%, bank partial profit, let the rest run into the catalyst. Thesis unchanged.”
- **REVIEW:** “Trigger fired: guidance cut on soft demand. Thesis not yet broken but the variant view is in question. Re-underwrite within 48 hours; pending that, no adds, tighten stop.”
- **SELL:** “Thesis broken — the margin inflection reversed and management withdrew the target. The *why* is now false; this is no longer a hold-and-hope. Exit in full; redeploy to the highest-ranked BUY-CANDIDATE.”

## Recommendations

**Stage 1 — Build the pipeline in this order (deterministic):**

1. **Shariah knockout first.** Apply the AAOIFI Shariah Standard No. 21 (“Financial Papers (Shares and Bonds),” issued May 2004) screen as an absolute gate: the business-activity screen (impermissible core business ⇒ AVOID) plus the three ratio tests — the **“30/30/5” rule**: interest-bearing debt < 30% of market cap; cash + interest-bearing securities < 30% of market cap; impermissible (e.g., interest) income < 5% of revenue. AAOIFI applies these as strict, no-buffer thresholds (a firm at 30.01% debt is non-compliant) — *stricter* than the 33%/33.33% used by the Dow Jones Islamic Market, S&P Shariah and MSCI Islamic indices, so pick and document which methodology you implement. (Note AAOIFI Standard No. 59 removed the older minimum-tangible-asset/liquidity ratio.) Any breach ⇒ AVOID, with a dividend-purification note where relevant. Re-test on each audited statement, since compliance can change quarter to quarter. 
1. **Edge test.** If the engine cannot populate VARIANT_VIEW with a specific reason the market is wrong, the idea cannot exceed RESEARCH.
1. **Asymmetry gate.** Compute REWARD_RISK from target and stop/downside; require ≥3:1 for BUY-CANDIDATE (you may relax toward ~2:1 for short-horizon swing setups, but make the threshold an explicit, logged parameter).
1. **Catalyst-within-horizon gate.** No catalyst inside the holding window ⇒ at most RESEARCH, or “dead money” ⇒ TRIM/REVIEW for existing holdings.
1. **Sizing.** Size from conviction × the 1%-risk rule and a hard max-position cap; never let one position or one correlated cluster dominate.

**Stage 2 — Encode the sell/exit logic explicitly,** because it’s where both pros and retail fail. Write invalidation triggers (thesis-type) AND a price stop (defensive) at entry, plus a time-stop equal to the thesis’s implied window. Make SELL fire automatically on thesis break, target reached, time-stop, or a higher-ranked idea needing capital.

**Stage 3 — Force the behavioral guards.** Mandatory PRE_MORTEM and “would I buy here today?” fields; a fixed review cadence that auto-sets REVIEW on catalyst dates and earnings; and a journal that scores *process*, not just outcome.

**Benchmarks that should change the rules:** If realized win-rate × average-win / average-loss (your actual edge) is below 1 after a meaningful sample, tighten the asymmetry gate and cut size — the data is telling you the edge isn’t there. If the engine’s REVIEW/HOLD outputs consistently fail the “buy here today?” test, your entry discipline is too loose. If post-cost returns trail simply holding a Shariah-compliant index, the honest recommendation is to reduce trading frequency.

## Caveats

- **Process is not a profit guarantee.** Mauboussin’s own framing is explicit: a good process maximizes the *chance* of good outcomes but can still lose; over a short sample, luck dominates skill. Institutional rigor improves decision *quality* — it does not repeal uncertainty.
- **The retail short-term-trading odds are real and adverse.** The most rigorous single-market study — Chague, De-Losso & Giovannetti, “Day Trading for a Living?” (Univ. of São Paulo Working Paper No. 2019-47), tracking all 19,646 individuals who began day-trading mini-Ibovespa futures 2013–2015 — found that “97% of all individuals who persisted for more than 300 days lost money. Only 1.1% earned more than the Brazilian minimum wage and only 0.5% earned more than the initial salary of a bank teller — all with great risk,” with “no evidence of learning.” Broader estimates across markets put the majority of retail day traders in the red within a year. Frequent trading also magnifies transaction costs and the disposition effect. A PM-grade *process* mitigates but does not eliminate these structural problems; the engine should surface this honestly rather than imply that good documentation creates an edge.
- **Concentration vs. diversification and stops vs. fundamental exits are genuinely contested** among professionals. The engine should treat these as user-set parameters, not settled truths, and enforce whichever stance is chosen consistently.
- **Some sources are practitioner blogs and book summaries.** The verbatim Sonkin & Johnson frameworks (four questions, three advantages, variant perception, catalyst definition) are well-corroborated from the authors’ own interviews; some enumerated lists and sizing figures come from reader summaries and practitioner compilations and should be treated as directional rather than canonical.
- **Shariah interpretation varies.** AAOIFI Standard 21 is widely used but individual scholars and boards apply different thresholds and purification rules;  the engine’s screen should be transparent about which methodology it implements and flag borderline (“REVIEW”) cases for human/scholarly judgment.