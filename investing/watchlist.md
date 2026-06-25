# Watchlist — candidate ideas to research (NOT a buy list)

List names/themes you want the routine to research for upcoming catalysts and
Shariah compliance. The routine returns "ideas to investigate in Zoya/Musaffa",
never buy calls. You make every decision; you verify every compliance status.

## How these candidates were built (PM decision-logic pipeline)

Per docs/portfolio-manager-decision-logic.md, applied in order:
1. **Shariah knockout FIRST.** Only names that PRE-screen plausibly compliant are
   listed (permissible core business + low interest-bearing debt). This is a
   heads-up, NOT a pass — you MUST confirm each in Zoya/Musaffa before any add.
   AAOIFI 30/30/5 is stricter than this repo's 33/33 ratio pre-check; borderline
   names are flagged REVIEW, not listed.
2. **Edge test.** The `why` column is a *candidate angle to underwrite* — the
   question the market is arguing about — NOT a proven variant view. The doc is
   explicit: until you can state specifically why consensus is wrong, an idea
   cannot exceed RESEARCH. Treat every `why` below as a hypothesis to validate.
3. **Asymmetry gate.** Needs a defined target AND stop to compute reward:risk
   (>= reward_risk_min_swing). NONE are computed yet — this sandbox's market-data
   feed (Yahoo) is blocked, so recommend.py returns reward_risk=null and these
   correctly stay RESEARCH until you (or a data-enabled run) define target/stop.
4. **Catalyst-within-horizon gate.** Each has a dated HARD catalyst; ones beyond
   catalyst_horizon_days (60) are noted and will be capped by the engine.
5. **Sizing.** Initial 1-2% at risk_per_trade_pct to the stop; ~20% hard cap.

## Tickers to track
# ticker | why it's interesting (CANDIDATE angle to underwrite — not a proven edge) | catalyst (dated)
TSM  | Sole leading-edge foundry; advanced-node scarcity = pricing power. Underwrite: is 2026 capex/utilization already in the price? Low debt — plausibly compliant. | Q2 earnings 2026-07-16
ISRG | Da Vinci 5 placement ramp + procedure-volume recovery; ~zero debt. Underwrite: is installed-base growth decelerating vs expectations? | Q2 earnings 2026-07-16
AMD  | Data-center GPU (MI-series) share-gain vs Nvidia; AAOIFI ~1% debt. Underwrite: does MI400 ramp net-positive against China export curbs? | Q2 earnings 2026-08-04
QCOM | Diversification beyond handsets (auto/IoT) vs licensing-cliff fears; low debt. Underwrite: which view does Q3 guidance confirm? | Q3 FY26 earnings 2026-08-05
LLY  | GLP-1/obesity TAM + oral orforglipron data; low debt. Underwrite: is the multiple already pricing the ramp, or is supply/scripts the surprise? | Q2 earnings 2026-08-05
NVDA | AI datacenter capex super-cycle; debate is demand durability vs digestion; low debt. Underwrite YOUR variant view. NOTE: catalyst 62d out — just BEYOND the 60d horizon, so engine caps at RESEARCH. | Q2 FY27 earnings 2026-08-26

## Themes / screens to run
# - Shariah-compliant US software with accelerating revenue + low debt
# - Names within 15% of 52w low where the thesis is intact (not falling knives)
# - Upcoming catalysts in next 60 days (product launches, earnings, approvals)

## Correlation note (from the doc: "several positions in one sector are one bet")
# - TSM / AMD / QCOM / NVDA are a CORRELATED SEMICONDUCTOR cluster — size them as
#   ONE bet, not four. LLY (pharma) and ISRG (medtech) are the genuine diversifiers
#   here, and all of these sit away from your existing NOW (enterprise software).

## Hard rules (the routine must respect these)
# - Compliance is a gate, not a tiebreaker: skip anything not screened compliant.
# - No position above ~20% of the book (concentration cap).
# - "High reward" is paired with high risk — size accordingly; this is a small account.
