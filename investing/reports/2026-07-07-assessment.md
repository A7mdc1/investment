# Portfolio Assessment — 2026-07-07

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

**Second run today** — this revises the morning report (11:43 UTC) with live
afternoon data (~17:10 UTC). `discover.py` (live Yahoo data, fresh 20-name
pool by max-benefit rank) → `scaffold.py --all-leads` (6 new DRAFT setup
cards for leads that entered the pool since this morning) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` still reports 0 closed trades (no
`transactions.csv` yet — discipline guard stays dormant until you start
logging via `/apply-trade`).

**Headline change since this morning:** both holdings ran up hard intraday —
FIG **+9.5%** ($21.08 → $23.08) and NOW **+5.1%** ($107.93 → $113.51). No
single confirmed catalyst surfaced for either move in today's news search
(see Sources) — treat as a strong intraday session, not a verified news
event, until you find a specific driver. One consequence worth flagging:
**NOW's trailing-stop breach from this morning has resolved** — price is
now back above the chandelier level.

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a sixth consecutive daily report.**
Live price **$23.08**, now **+7.7%** vs. the $21.43 cost basis (was -1.6%
this morning) — the compliance gate does not care about this move.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.2:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| DCF intrinsic value | **$15.08** vs. $23.06 price -> **-34.6% downside** (price is rich to the model; gap widened from -28.5% this morning as price ran up) |
| Trailing stop (chandelier) | $19.3745 — price ~19% above it |
| 6m momentum (skip last month) | -40.1% |
| Portfolio note | ATR 6.11% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$113.51**, **-1.3%** vs. $114.97 cost basis (was -6.1% this morning) —
well inside the 20% `drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — recommend.py can't self-assess without a stated thesis-vs-price edge |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| DCF intrinsic value | **$120.42** vs. $113.51 price -> **+6.1% upside** to the model (was +11.6% this morning; the gap to intrinsic value narrowed as price ran up) |
| Trailing stop (chandelier) | $107.3659 — **price is now $6.14 above it** (resolved: this morning's breach at $107.93 vs $109.98 no longer applies) |
| 6m momentum (skip last month) | -19.1% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own thesis input |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

**Resolving this morning's open question on NOW's trailing stop:** the price
has since moved back above the chandelier level ($113.51 vs. $107.37), so the
question of whether `trade_type: core` should exempt NOW from a mechanical
TRAIL_STOP is moot again for now — but the same structural point stands for
next time price dips near the stop: `verdict.py`'s TRAIL_STOP rule only fires
for `trade_type in (swing, momentum, catalyst)`, and NOW is tagged `core`, so
it will never fire mechanically regardless of price. Still worth a deliberate
decision on whether that's the policy you want.

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $23.08 | 35 | $21.43 | $807.63 | +7.7% | 50.4% |
| NOW | $113.46 | 7 | $114.97 | $794.23 | -1.3% | 49.6% |

**Total value: $1,601.85** | Cost: $1,554.84 | **Total return: ~+3.0%** (+$47.01 unrealised)

*(This morning: total value $1,493.31, return ~-4.0%. Both positions ran up
intraday — a swing of roughly +$108 / +7 points of return in one session.)*

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Sixth consecutive daily report unresolved.
   COMPLIANCE_GATE fires -> SELL. The intraday rally makes this more costly
   to keep sitting on, not less — the mandate question doesn't improve with
   price.
2. **[DCF / FIG] Price is now ~35% above intrinsic value** ($23.06 vs.
   $15.08) on the recorded growth/discount assumptions — wider than this
   morning's ~29% gap. Another data point (beyond the compliance gate)
   against treating today's bounce as a reason to stay.
3. **[Technical / NOW] Resolved** — price is back above the chandelier
   trailing stop ($113.51 vs. $107.37); this morning's breach note no longer
   applies. No action implied either way.
4. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still
   holds. Do not add.
5. **[Shariah / new lead] PLTR** — still in today's discovery pool (see
   below); unchanged from this morning — external screeners split, at least
   one (Musaffa) rating it DOUBTFUL on business-activity grounds
   (government/defense/intelligence contracts) independent of the clean
   ratio pre-check here. Treat as a likely fail pending your own
   Zoya/Musaffa screen.
6. **[Shariah / new leads] ESE, PSX** — two names new to today's afternoon
   pool worth flagging before review: ESE (ESCO Technologies) carries a
   named Aerospace & Defense segment alongside its utility/RF-shielding
   businesses — confirm the defense-revenue share in Zoya/Musaffa before
   treating it as a clean pass. PSX (Phillips 66) is oil & gas refining/
   midstream — sector treatment varies by screener (some differentiate
   upstream vs. downstream); confirm the business-activity screen, not just
   the ratio pre-check.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** design-platform growth story
intact; no news found today that changes the fundamental picture materially
(see Sources — no confirmed catalyst identified for today's +9.5% move).

**Case to exit (compliance + DCF, both independent of each other):**
NON-COMPLIANT per your mandate — this overrides any fundamental debate; six
consecutive daily reports unresolved now. The DCF model (30% 5y growth, 12%
discount rate) puts intrinsic value at $15.08 vs. a $23.06 price, now a ~35%
premium to the model, even setting compliance aside — the rally made the
valuation case *for* exiting stronger, not weaker.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (15 days out);
DCF still shows +6.1% upside to intrinsic value ($120.42) at recorded
assumptions even after today's rally; consensus remains predominantly "Buy"
per prior analyst tracking (unchanged from this morning's research, no new
analyst action found today).

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
still negative (-19.1%) despite today's bounce; the reward:risk to the DCF
target has compressed to 1.1:1 (was implicitly wider this morning) as price
closed the gap toward intrinsic value — worth watching if it keeps running,
since REWARD_RISK_COMPRESSED-style logic would argue for trimming a swing
position at this point (NOW is tagged `core`, so this doesn't mechanically
fire, but it's a relevant fact for your own judgment call ahead of the
2026-07-22 print).

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a sixth consecutive
  daily report.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -1.3% vs. the 20% threshold (well
  inside; drawdown narrowed sharply from -6.1% this morning).
- **TRAIL_STOP -> NOW**: does NOT fire (trade_type: core exempts it from the
  technical trailing-stop rule); moot again this run since price is back
  above the computed level, but the same structural gap applies if price
  revisits the stop later.
- **VOL_THROTTLE note -> FIG**: ATR 6.11% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $23.06 | -34.6% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $113.51 | +6.1% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — refreshed discovery pool (6 new DRAFT cards)

`discover.py` re-ran with live afternoon data (same SPUS holdings +
`growth_technology_stocks` / `undervalued_large_caps` screens, same
liquidity + Shariah-ratio/asymmetry/catalyst gates) and rewrote
**`leads.md`**. The top-20 by max-benefit rank shifted: **AU, CDE, MT, MU,
TER, and ADI dropped out** of today's pool (their setup cards from this
morning still exist in `setups/` but are no longer active leads); **CLS,
AVGO, APH, GDDY, PSX, and ESE are new** and `scaffold.py --all-leads` just
auto-filled DRAFT cards for all six. **Every row below is `status: draft`,
unreviewed, and Shariah UNVERIFIED** — proposals to review and edit, never
buys. None can reach BUY-CANDIDATE until you review the card, edit anything
you disagree with, set `status: planned`, and screen the name compliant in
Zoya/Musaffa.

As before, **leads R:R** is discover.py's discovery-stage estimate (drives
LEAD vs. RESEARCH); **card R:R (T1)** is the scaffolded card's engineered
target, fixed by construction near your `t1_r: 1.5` policy knob — the two
numbers answer different questions and shouldn't be read as the same figure.

| Ticker | Verdict (leads.md) | Setup type | Entry | Stop | T1 target | Card R:R (T1) | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|---|
| AR | LEAD | earnings_run | $34.68 | $34.12 | $35.52 | 1.5:1 | 10.8:1 | earnings 2026-07-29 | 22 |
| CLS | LEAD | earnings_run (new) | $348.11 | $344.42 | $353.65 | 1.5:1 | 9.2:1 | earnings 2026-07-27 | 20 |
| AVGO | LEAD | earnings_run (new) | $371.84 | $363.71 | $384.04 | 1.5:1 | 11.8:1 | earnings 2026-09-03 | 58 |
| ULTA | LEAD | earnings_run | $452.49 | $447.62 | $459.79 | 1.5:1 | 20.0:1 | earnings 2026-08-27 | 51 |
| KLIC | LEAD | earnings_run | $119.61 | $108.81 | $135.81 | 1.5:1 | 5.9:1 | earnings 2026-08-06 | 30 |
| ALAB | LEAD | earnings_run | $432.74 | $371.67 | $524.34 | 1.5:1 | 3.5:1 | earnings 2026-08-04 | 28 |
| PLTR | LEAD | earnings_run | $132.54 | $131.84 | $133.59 | 1.5:1 | 6.3:1 | earnings 2026-08-03 | 27 |
| LIF | LEAD | earnings_run | $56.73 | $49.97 | $66.87 | 1.5:1 | 5.7:1 | earnings 2026-08-10 | 34 |
| SIMO | RESEARCH | earnings_run | $318.86 | $273.25 | $387.27 | 1.5:1 | 2.3:1 | earnings 2026-07-30 | 23 |
| APH | LEAD | earnings_run (new) | $159.01 | $156.38 | $162.97 | 1.5:1 | 5.3:1 | earnings 2026-07-29 | 22 |
| VRNS | RESEARCH | earnings_run | $45.67 | $39.71 | $54.61 | 1.5:1 | 2.7:1 | earnings 2026-07-28 | 21 |
| FICO | LEAD | earnings_run | $1286.51 | $1134.67 | $1514.28 | 1.5:1 | 3.8:1 | earnings 2026-07-29 | 22 |
| ALKT | LEAD | earnings_run | $18.95 | $16.99 | $21.89 | 1.5:1 | 4.3:1 | earnings 2026-07-29 | 22 |
| CF | LEAD | earnings_run | $113.20 | $106.79 | $122.81 | 1.5:1 | 3.7:1 | earnings 2026-08-05 | 29 |
| DUOL | LEAD | earnings_run | $129.72 | $111.80 | $156.60 | 1.5:1 | 4.0:1 | earnings 2026-08-05 | 29 |
| GDDY | LEAD | earnings_run (new) | $90.37 | $79.00 | $107.42 | 1.5:1 | 3.6:1 | earnings 2026-07-30 | 23 |
| PAY | LEAD | earnings_run | $28.15 | $25.00 | $32.87 | 1.5:1 | 3.8:1 | earnings 2026-08-03 | 27 |
| PSX | RESEARCH | earnings_run (new) | $177.19 | $172.06 | $184.89 | 1.5:1 | 2.9:1 | earnings 2026-08-05 | 29 |
| AMD | RESEARCH | earnings_run | $552.05 | $467.12 | $679.45 | 1.5:1 | 1.1:1 | earnings 2026-08-04 | 28 |
| ESE | LEAD | earnings_run (new) | $332.24 | $322.64 | $346.64 | 1.5:1 | 3.2:1 | earnings 2026-08-10 | 34 |

All 20 cards passed the liquidity floor (`avg $vol` >= $5M, market cap >=
$500M) and cleared a clean ratio pre-check (business_ok, debt/liquid ratios
within bounds) — but the ratio pre-check is *not* a business-activity
screen. Shariah status on every card is `unverified` by construction (only a
human Zoya/Musaffa screen can set `compliant`).

**Flags worth your attention before reviewing any of these:**
- **PLTR (Palantir)** — unchanged from this morning: business is largely
  government/defense/intelligence data analytics (Gotham, Foundry; contracts
  include military and ICE work). At least one Shariah screener rates it
  DOUBTFUL/non-compliant on business-activity grounds (~5.7% prohibited
  income, over the 5% threshold), independent of the clean ratio pre-check
  here. Screen this one skeptically, not as a rubber stamp.
- **ESE (ESCO Technologies)** — new to the pool this run. Has a named
  Aerospace & Defense segment alongside utility-solutions and RF-shielding
  businesses — a debt/liquidity ratio pre-check won't catch defense-revenue
  exposure. Confirm the business-activity screen (and the prohibited-revenue
  percentage) in Zoya/Musaffa before treating this as more than RESEARCH.
- **PSX (Phillips 66)** — new to the pool this run; capped at RESEARCH by
  the asymmetry gate already (2.9:1 < 3.0 floor). Oil & gas refining/
  midstream — some Islamic screens differentiate upstream E&P from
  downstream refining; confirm the business-activity treatment, not just the
  clean ratio pre-check.
- **AVGO (Broadcom)** — new to the pool this run, sourced as a current SPUS
  (halal-ETF) holding, which is a reasonable starting signal for the
  business screen, but still confirm independently — ETF constituency isn't
  itself a fatwa.
- **AU / CDE / MT / MU / TER / ADI dropped out of today's pool** — no longer
  clearing the discovery-stage gates as of this afternoon's data (mostly
  asymmetry/catalyst-horizon shifts as prices moved); their DRAFT cards from
  this morning still exist in `setups/` if you want to revisit them by hand,
  but they're not part of today's fresh discovery output.
- **AMD, VRNS, SIMO, PSX (RESEARCH, not LEAD)** — capped by the mechanical
  gates, not a business problem: all four sit below the >=3.0 discovery-stage
  asymmetry floor today. Nothing wrong with these names, just not clearing
  the bar this cycle.

## Follow-ups (priority order)

1. **[Urgent — 6th daily report unresolved] FIG compliance**: re-screen in
   Zoya/Musaffa. The intraday rally strengthens the DCF case for exiting; it
   does nothing for the compliance question either way.
2. **[Standing — policy decision] NOW trailing stop**: resolved for now
   (price is back above the chandelier level), but `trade_type: core`
   structurally exempts NOW from `verdict.py`'s TRAIL_STOP rule regardless of
   price. Decide whether that's the policy you want for a long-horizon
   "core" holding, or whether NOW's `trade_type` should change.
3. **[New — Shariah] PLTR, ESE, PSX**: business-activity screens needed
   before treating any of these as more than RESEARCH — see flags above.
4. **[Housekeeping] Leads pool refreshed intraday** — AU, CDE, MT, MU, TER,
   ADI dropped out; CLS, AVGO, APH, GDDY, PSX, ESE are new. 6 fresh DRAFT
   cards exist; none are `planned`, none can reach BUY-CANDIDATE yet.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Figma Stock Rose 9% This Week: Where FIG Could Go in 2026 — TIKR](https://www.tikr.com/blog/figma-stock-rose-9-this-week-where-fig-could-go-in-2026)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [Figma Stock 2026: Why $89M in Cash Flow Can't Stop the Slide — Memeburn](https://memeburn.com/figma-stock-2026-cash-flow/)
- [ServiceNow (NOW) Stock Trades Up, Here Is Why — StockStory](https://stockstory.org/us/stocks/nyse/now/news/why-up-down/servicenow-now-stock-trades-up-here-is-why-7)
- [ServiceNow Was the SaaS Stock AI Was Supposed to Kill. Its Numbers Say Otherwise. — 24/7 Wall St.](https://247wallst.com/investing/2026/07/06/servicenow-was-the-saas-stock-ai-was-supposed-to-kill-its-numbers-say-otherwise/)
- [ServiceNow (NOW) Stock Still Looks Above Fair Value Despite Fresh AI Partnership News — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-stock-still-looks-201533388.html)
- [Is Palantir Technologies (PLTR) Stock Halal or Haram? — Zoya](https://zoya.finance/stocks/pltr)
- [Is Palantir Technologies Inc. (PLTR) Stock Halal? — HalalScreener](https://halalscreener.app/en/stock/PLTR)
- [Is Palantir Technologies Inc - PLTR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/PLTR/)
