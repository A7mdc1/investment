# Portfolio Assessment — 2026-07-09

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (6 fresh DRAFT setup cards auto-filled: STX, CLS,
FORM, GDDY, TSLA, GOOGL; 14 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` still reports
0 closed trades (no `transactions.csv` yet — discipline guard stays dormant
until you start logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a seventh consecutive run.** Live
price **$21.81**, essentially flat vs. the $21.43 cost basis (**+1.8%**).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.6:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| DCF intrinsic value | **$15.08** vs. $21.81 price -> **-30.8%** (price is rich to the model) |
| Trailing stop (chandelier) | $19.172 — price ~13.7% above it |
| 6m momentum (skip last month) | -43.7% |
| Portfolio note | ATR 6.49% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$107.63**, **-6.4%** vs. $114.97 cost basis — inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 1.4:1 — skew too thin for recommend.py to call high conviction absent your own thesis input |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| DCF intrinsic value | **$120.42** vs. $107.63 price -> **+11.9% upside** to the model |
| Trailing stop (chandelier) | $98.5424 — price is now ~9.2% above it (stop has trailed down since the 07-07 run, when price sat *below* the then-current level) |
| 6m momentum (skip last month) | -23.3% |
| Would buy today? | Yes per recommend.py's mechanical gates; conviction still flagged LOW absent your own thesis input |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- **Earnings in 13 days:** ServiceNow reports Q2 FY2026 results after market
  close **2026-07-22** (confirmed via company press release) — inside the
  current holding window; no `earnings_plan` is recorded on NOW's card
  (it's a `core`-tagged holding, not a setup card, so the gap-plan gate
  doesn't mechanically apply — still worth your own read on position size
  into the print).

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $21.82 | 35 | $21.43 | $763.53 | +1.8% | 50.3% |
| NOW | $107.63 | 7 | $114.97 | $753.38 | -6.4% | 49.7% |

**Total value: $1,516.90** | Cost: $1,554.84 | **Total return: ~-2.4%** (-$37.94 unrealised)

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Seventh run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Catalyst / NOW] Q2 earnings in 13 days (2026-07-22)** — confirmed date;
   no gap plan recorded on the holding since it's `core`, not a setup card —
   your call on how to size through the print.
4. **[DCF / FIG] Price is ~31% above intrinsic value** ($21.82 vs. $15.08) on
   the recorded growth/discount assumptions — another data point (beyond the
   compliance gate) against treating the recent bounce as a reason to stay.
5. **[Data quality / GDDY new lead]** GoDaddy's ratio pre-check is FLAGGED —
   debt/market-cap ≈33%, right at the AAOIFI 33% threshold — this is not a
   clean pass like the rest of today's pool; treat as likely fail pending
   Zoya/Musaffa, not "probably fine."
6. **[Shariah / new leads] TSLA, GOOGL** — both surfaced today as SPUS-holding
   LEADs with earnings 2026-07-22 (13 days out). External screeners
   (Zoya, Musaffa) currently rate both compliant under AAOIFI methodology,
   though GOOGL's status has flipped between compliant/doubtful across
   sources this year given its AI-driven borrowing — re-verify at screen time,
   don't treat last quarter's read as durable.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** Q1 2026 revenue grew 46% y/y
to $333M (accelerating from 40% prior quarter), net dollar retention 139%
(highest in 2+ years), paid customers +54% y/y to ~690K. Citigroup initiated
Buy coverage July 1 with a $36 target; Bank of America resumed coverage Buy
at $30. Stock is up sharply off its June lows on this news flow.

**Case to exit (compliance + DCF, both independent of each other):**
NON-COMPLIANT per your mandate — this overrides any fundamental debate; seven
consecutive cycles unresolved now. The DCF model (30% 5y growth, 12%
discount rate) still puts intrinsic value at $15.08 vs. a $21.82 price, a
~31% premium to the model even setting compliance aside — the recent rally
has made the valuation gap *wider*, not narrower.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings confirmed for **2026-07-22** (13 days
out, after market close) — analyst expectations center on continued ~21%
subscription growth; DCF shows +11.9% upside to intrinsic value ($120.42) at
recorded assumptions; Armis security-workflow integration (closed April
2026) remains the stated forward driver alongside AI-agent expansion.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-23.3%; price sits roughly 9% above the chandelier trailing stop today (the
stop level itself has fallen sharply since 07-07, from ~$109.98 to $98.54,
reflecting the wider recent range) — worth your own judgment on sizing given
the earnings print is 13 days away and could gap either direction on a
`core`-tagged position with no recorded gap plan.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a seventh consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -6.4% vs. the 20% threshold.
- **VOL_THROTTLE note -> FIG**: ATR 6.49% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.82 | -30.8% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $107.63 | +11.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — 20 leads, 6 fresh DRAFT cards + 14 unchanged

`discover.py` refreshed the pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 20 by max-benefit rank). Turnover vs. 07-07: **AU, CDE,
MT, TER, SIMO, AMD dropped**; **STX, CLS, FORM, GDDY, TSLA, GOOGL are new**.
`scaffold.py --all-leads` filled DRAFT cards for the 6 new names only —
existing cards were left untouched (`--force` would be needed to
regenerate them). **Every row below is `status: draft`, unreviewed, and
Shariah UNVERIFIED — these are proposals to review and edit, never buys.**
None of these can reach BUY-CANDIDATE until you review the card, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa.

Note on the two reward:risk columns (same caveat as prior runs): **leads
R:R** is discover.py's discovery-stage estimate (drives the LEAD vs.
RESEARCH gate). **Card R:R (T1)** is the scaffolded setup card's *engineered*
target, fixed by construction at your `t1_r: 1.5` policy knob — reads ~1.5:1
for nearly every name regardless of the discovery-stage number.

| Ticker | Verdict (leads.md) | Setup type | Entry | Stop | T1 target | Card R:R (T1) | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|---|
| ALKT | LEAD | earnings_run | $18.95 | $16.99 | $21.89 | 1.5:1 | 14.8:1 | earnings 2026-07-29 | 20 |
| ULTA | LEAD | earnings_run | $452.49 | $447.62 | $459.79 | 1.5:1 | 18.4:1 | earnings 2026-08-27 | 49 |
| STX *(new)* | LEAD | earnings_run | $913.53 | $892.44 | $945.16 | 1.5:1 | 5.5:1 | earnings 2026-07-28 | 19 |
| PLTR | LEAD | earnings_run | $132.54 | $131.84 | $133.59 | 1.5:1 | 7.5:1 | earnings 2026-08-03 | 25 |
| AR | LEAD | earnings_run | $34.68 | $34.12 | $35.52 | 1.5:1 | 6.0:1 | earnings 2026-07-29 | 20 |
| LIF | LEAD | earnings_run | $56.73 | $49.97 | $66.87 | 1.5:1 | 6.2:1 | earnings 2026-08-10 | 32 |
| CLS *(new)* | LEAD | earnings_run | $360.52 | $341.39 | $389.23 | 1.5:1 | 6.0:1 | earnings 2026-07-27 | 18 |
| FICO | LEAD | earnings_run | $1286.51 | $1134.67 | $1514.28 | 1.5:1 | 5.8:1 | earnings 2026-07-29 | 20 |
| VRNS | LEAD | earnings_run | $45.67 | $39.71 | $54.61 | 1.5:1 | 4.2:1 | earnings 2026-07-28 | 19 |
| FORM *(new)* | LEAD | earnings_run | $122.12 | $118.66 | $127.30 | 1.5:1 | 5.6:1 | earnings 2026-07-29 | 20 |
| DUOL | LEAD | earnings_run | $129.72 | $111.80 | $156.60 | 1.5:1 | 5.0:1 | earnings 2026-08-05 | 27 |
| GDDY *(new)* | LEAD | earnings_run | $87.58 | $79.13 | $100.26 | 1.5:1 | 4.8:1 | earnings 2026-07-30 | 21 |
| PAY | LEAD | earnings_run | $28.15 | $25.00 | $32.87 | 1.5:1 | 5.2:1 | earnings 2026-08-03 | 25 |
| ALAB | RESEARCH | earnings_run | $432.74 | $371.67 | $524.34 | 1.5:1 | 1.2:1 | earnings 2026-08-04 | 26 |
| ADI | LEAD | earnings_run | $388.83 | $386.48 | $392.35 | 1.5:1 | 5.4:1 | earnings 2026-08-19 | 41 |
| KLIC | LEAD | earnings_run | $119.61 | $108.81 | $135.81 | 1.5:1 | 3.6:1 | earnings 2026-08-06 | 28 |
| TSLA *(new)* | LEAD | earnings_run | $404.46 | $373.80 | $450.44 | 1.5:1 | 3.1:1 | earnings 2026-07-22 | 13 |
| GOOGL *(new)* | LEAD | earnings_run | $356.78 | $340.70 | $380.90 | 1.5:1 | 3.2:1 | earnings 2026-07-22 | 13 |
| CF | LEAD | earnings_run | $113.20 | $106.79 | $122.81 | 1.5:1 | 3.4:1 | earnings 2026-08-05 | 27 |
| MU | RESEARCH | pullback | $1032.92 | $949.32 | $1158.32 | 1.5:1 | 3.6:1 | earnings 2026-09-23 | 76 (>60d horizon) |

All 20 cards passed the liquidity floor (`avg $vol` >= $5M, market cap >=
$500M). Shariah status on every card is `unverified` by construction (only a
human Zoya/Musaffa screen can set `compliant`).

**Flags worth your attention before reviewing any of these:**
- **GDDY (GoDaddy, new today)** — ratio pre-check FLAGGED: debt/market-cap
  ≈33%, sitting right at the AAOIFI 33% threshold rather than comfortably
  under it. This is the only name in today's pool that didn't clean-pass the
  ratio pre-check; screen skeptically.
- **TSLA / GOOGL (new today, both SPUS holdings)** — both currently rated
  compliant by Zoya and Musaffa under AAOIFI methodology (Tesla: interest-
  bearing debt 0.6% of market cap, cash+securities 3.0%, both well inside the
  30% thresholds; Alphabet: inside AAOIFI limits as of the latest quarter),
  but Alphabet's status has flipped between compliant and doubtful across
  sources this year given AI-driven borrowing, and both report earnings the
  same day (2026-07-22, 13 days out) as your existing NOW holding —
  correlated timing risk if you're considering either alongside NOW.
- **PLTR (carried over)** — still worth the same caution as prior runs:
  external screeners are split on its government/defense/intelligence
  revenue exposure; don't let "UNVERIFIED" here read as "probably fine."
- **AR (carried over)** — natural-gas E&P; still needs its own
  business-activity and hedging-structure screen beyond the ratio pre-check.
- **KLIC flipped from RESEARCH to LEAD** — discovery-stage reward:risk
  improved to 3.6:1 (from 1.5:1 on 07-07), clearing the asymmetry floor.
  Mechanical change, not a new business signal — worth a fresh look if you'd
  dismissed it before.
- **MU (carried over, RESEARCH)** — still capped by the 60-day catalyst
  horizon gate (76 days to its 2026-09-23 print), same as last run.

## Follow-ups (priority order)

1. **[Urgent — 7th run unresolved] FIG compliance**: re-screen in Zoya/Musaffa.
2. **[New — timing] NOW earnings 2026-07-22 (13 days)**: confirmed date;
   decide your sizing/gap approach into the print — no `earnings_plan` is
   recorded since this is a `core` holding, not a setup card.
3. **[New — data quality] GDDY ratio flag**: debt/market-cap at the 33%
   AAOIFI threshold — don't treat this card's UNVERIFIED status as a
   near-pass; verify carefully.
4. **[New — Shariah] TSLA / GOOGL**: both currently screen compliant
   externally but GOOGL's status is not stable across sources — re-verify at
   screen time; note both share NOW's 2026-07-22 earnings date if you're
   weighing correlated exposure.
5. **[Carried over — Shariah] PLTR**: likely business-activity fail
   (government/defense/intelligence contracts) per external screeners
   despite a clean ratio pre-check here.
6. **[Housekeeping] 20 DRAFT setup cards in `setups/`** (14 unchanged, 6 new
   today) — none are `planned`, none can reach BUY-CANDIDATE yet. Review at
   your own pace; the earnings dates they're built around mostly land over
   the next 2-7 weeks.
7. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [Figma Stock Rose 9% This Week: Where FIG Could Go in 2026 — TIKR](https://www.tikr.com/blog/figma-stock-rose-9-this-week-where-fig-could-go-in-2026)
- [Figma (FIG) Leads Software Stocks with 9% Surge Amid Sector Rally — GuruFocus](https://www.gurufocus.com/news/8941429/figma-fig-leads-software-stocks-with-9-surge-amid-sector-rally)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
- [ServiceNow to report Q2 earnings on July 22 — Investing.com](https://ca.investing.com/news/stock-market-news/servicenow-to-report-q2-earnings-on-july-22-93CH-4716549)
- [Is Alphabet (GOOGL) Stock Halal or Haram? Shariah Compliance Explained — Zoya](https://zoya.finance/stocks/googl)
- [Is Alphabet Inc - GOOGL Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/GOOGL/)
- [Alphabet Surges with AI... But is Google a halal stock? — Tabadulat](https://tabadulat.com/blog/alphabet-surges-with-ai-but-is-google-a-halal-stock)
- [Is Tesla (TSLA) Stock Halal or Haram? Shariah Compliance Explained — Zoya](https://zoya.finance/stocks/tsla)
- [Is Tesla Inc - TSLA Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/TSLA/)
