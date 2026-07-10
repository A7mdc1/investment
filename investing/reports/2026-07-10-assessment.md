# Portfolio Assessment — 2026-07-10

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (7 new DRAFT cards; 13 already existed) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` still reports
0 closed trades (no `transactions.csv` yet — discipline guard stays dormant
until you start logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a seventh consecutive run**, now
spanning nearly a month (first fired 2026-06-15). Live price **$21.59**, up
slightly vs. the $21.43 cost basis (**+0.7%**).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.6:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| DCF intrinsic value | **$15.08** vs. $21.58 price -> **-30.1%** (price is rich to the model) |
| Trailing stop (chandelier) | $19.0493 — price ~13.3% above it |
| 6m momentum (skip last month) | -45.0% |
| Portfolio note | ATR 6.76% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$107.15**, **-6.8%** vs. $114.97 cost basis — inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 1.3:1 — thin skew |
| Shariah | PASS — recorded compliant (screened 2026-06-09) |
| DCF intrinsic value | **$120.42** vs. $107.13 price -> **+12.4% upside** to the model |
| Trailing stop (chandelier) | $96.6075 — price is now **~10.9% above** it (last run price had slipped below the equivalent level; the chandelier band has recalculated wider) |
| 6m momentum (skip last month) | -29.1% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own thesis input |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $21.58 | 35 | $21.43 | $755.47 | +0.7% | 50.2% |
| NOW | $107.15 | 7 | $114.97 | $750.05 | -6.8% | 49.8% |

**Total value: $1,505.52** | Cost: $1,554.84 | **Total return: ~-3.2%** (-$49.32 unrealised)

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Seventh run unresolved, now ~4 weeks running.
   COMPLIANCE_GATE fires -> SELL. This is the longest this flag has gone
   unresolved since the routine started tracking it.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF / FIG] Price is ~43% above intrinsic value** ($21.58 vs. $15.08) on
   the recorded growth/discount assumptions — another data point (beyond the
   compliance gate) against treating the recent bounce as a reason to stay.
4. **[Technical / NOW — resolved]** Last run flagged price below the
   chandelier trailing stop; this run the stop has recalculated to $96.61 and
   price ($107.15) sits comfortably above it. No action implied either way —
   `trade_type: core` still structurally exempts NOW from the mechanical
   TRAIL_STOP rule regardless.
5. **[Shariah / recurring lead] PLTR** — appears in the discovery pool again
   this run. As noted previously, external screeners are split, with at
   least one rating it DOUBTFUL/non-compliant on business-activity grounds
   (government/defense/intelligence contracts) that the ratio pre-check here
   can't see. Treat as a likely fail pending your own Zoya/Musaffa screen.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** stock has firmed since the
last run — Citigroup (Buy, $36 PT) and Bank of America (Buy, $30 PT,
reinstated) both initiated/reinstated bullish coverage in the past two
weeks, and shares are up on a more constructive AI-monetization narrative
(hybrid seat + usage-based pricing with AI credits). Still down ~81% from
its 52-week high and ~30% below its 200-day average.

**Case to exit (compliance + DCF, both independent of each other):**
NON-COMPLIANT per your mandate — this overrides any fundamental debate;
seven consecutive cycles unresolved now. The DCF model (30% 5y growth, 12%
discount rate) puts intrinsic value at $15.08 vs. a $21.58 price, a ~43%
premium to the model even setting compliance aside. Insider selling
continues (CRO Shaunt Voskanian sold 8,629 shares on 2026-07-06).

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (12 days out) —
management guides subscription revenue of $3.815–3.820B (~22.5% cc growth)
and analysts model EPS of $0.40 (down y/y on comp, not a growth-story
break). Evercore ISI (Outperform, $150 PT) and Bernstein (Outperform, $236
PT) both reiterated bullish ratings ahead of the print. DCF shows +12.4%
upside to intrinsic value ($120.42) at recorded assumptions.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m
momentum -29.1%; earnings is 12 days out and could gap either direction —
worth deciding your `earnings_plan` stance (hold-through vs. reduce-into-print)
before the print, not after.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a seventh consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -6.8% vs. the 20% threshold.
- **VOL_THROTTLE note -> FIG**: ATR 6.76% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.58 | -30.1% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $107.13 | +12.4% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is currently **empty** — nothing
for step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — 20 leads (7 fresh DRAFT cards, 13 carried over)

`discover.py` rebuilt the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 20 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a **DRAFT** `setups/<ticker>.md` card for the 7 names new to the
pool this run (**MSFT, ZS, CLS, STX, APH, JNJ, GOOGL**); the other 13 already
had cards from prior runs and were left unchanged (`--force` not passed).
**Every card below is still `status: draft`, unreviewed, and Shariah
UNVERIFIED** unless you've since edited one to `planned` — these remain
proposals to review and edit, never buys.

Note on the two reward:risk columns: **leads R:R** is discover.py's
discovery-stage estimate (drives the LEAD vs. RESEARCH gate — RESEARCH means
it failed the >=3.0 asymmetry floor or the 60-day catalyst horizon at
discovery time). **Card R:R (T1)** is the scaffolded setup card's *engineered*
target, fixed by construction at your `t1_r: 1.5` policy knob — a different
number answering a different question (locked-in trade plan vs. screening
estimate).

| Ticker | New this run? | Verdict (leads.md) | Setup type | Entry | Stop | T1 target | Card R:R (T1) | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|---|
| MSFT | **new** | LEAD | earnings_run | $385.18 | $375.66 | $399.46 | 1.5:1 | 12.2:1 | earnings 2026-07-29 | 19 |
| ALKT | carried | LEAD | earnings_run | $18.95 | $16.99 | $21.89 | 1.5:1 | 19.7:1 | earnings 2026-07-29 | 19 |
| ZS | **new** | LEAD | earnings_run | $139.37 | $133.64 | $147.97 | 1.5:1 | 12.2:1 | earnings 2026-09-02 | 54 |
| CLS | **new** | LEAD | earnings_run | $357.15 | $341.75 | $380.26 | 1.5:1 | 7.6:1 | earnings 2026-07-27 | 17 |
| LIF | carried | LEAD | earnings_run | $56.73 | $49.97 | $66.87 | 1.5:1 | 7.2:1 | earnings 2026-08-10 | 31 |
| STX | **new** | LEAD | earnings_run | $920.99 | $889.96 | $967.54 | 1.5:1 | 5.3:1 | earnings 2026-07-28 | 18 |
| FICO | carried | LEAD | earnings_run | $1286.51 | $1134.67 | $1514.28 | 1.5:1 | 7.0:1 | earnings 2026-07-29 | 19 |
| PLTR | carried | LEAD | earnings_run | $132.54 | $131.84 | $133.59 | 1.5:1 | 7.4:1 | earnings 2026-08-03 | 24 |
| VRNS | carried | LEAD | earnings_run | $45.67 | $39.71 | $54.61 | 1.5:1 | 5.5:1 | earnings 2026-07-28 | 18 |
| ULTA | carried | LEAD | earnings_run | $452.49 | $447.62 | $459.79 | 1.5:1 | 8.2:1 | earnings 2026-08-27 | 48 |
| APH | **new** | LEAD | earnings_run | $158.61 | $156.99 | $161.04 | 1.5:1 | 5.6:1 | earnings 2026-07-29 | 19 |
| DUOL | carried | LEAD | earnings_run | $129.72 | $111.80 | $156.60 | 1.5:1 | 5.9:1 | earnings 2026-08-05 | 26 |
| MU | carried | RESEARCH | pullback | $1032.92 | $949.32 | $1158.32 | 1.5:1 | 5.7:1 | earnings 2026-09-23 | 75 (>60d horizon) |
| JNJ | **new** | RESEARCH | earnings_run | $256.13 | $250.94 | $263.92 | 1.5:1 | 2.9:1 | earnings 2026-07-15 | 5 |
| MT | carried | RESEARCH | earnings_run | $65.35 | $65.31 | $65.42 | 1.75:1 | 3.0:1 | earnings 2026-07-30 | 20 |
| PAY | carried | LEAD | earnings_run | $28.15 | $25.00 | $32.87 | 1.5:1 | 4.2:1 | earnings 2026-08-03 | 24 |
| ALAB | carried | RESEARCH | earnings_run | $432.74 | $371.67 | $524.34 | 1.5:1 | 1.8:1 | earnings 2026-08-04 | 25 |
| GOOGL | **new** | LEAD | earnings_run | $355.00 | $340.92 | $376.11 | 1.5:1 | 3.8:1 | earnings 2026-07-22 | 12 |
| ADI | carried | LEAD | earnings_run | $388.83 | $386.48 | $392.35 | 1.5:1 | 5.3:1 | earnings 2026-08-19 | 40 |
| KLIC | carried | LEAD | earnings_run | $119.61 | $108.81 | $135.81 | 1.5:1 | 3.4:1 | earnings 2026-08-06 | 27 |

All 20 cards passed the liquidity floor and cleared a clean ratio pre-check
(business_ok, debt/liquid ratios within bounds) — but the ratio pre-check is
*not* a business-activity screen. Shariah status on every card is
`unverified` by construction (only a human Zoya/Musaffa screen can set
`compliant`).

**Flags worth your attention:**
- **MSFT, GOOGL, JNJ, MU** — all four are flagged `auto (SPUS holding)`,
  meaning discover.py surfaced them because they sit inside the SPUS halal
  ETF's holdings, not from the growth-screen pool. That's a useful
  index-level signal (a Shariah-index provider already includes them) but is
  still not a substitute for your own Zoya/Musaffa screen on the individual name.
- **JNJ** clears the catalyst gate easily (earnings in 5 days) but stays
  RESEARCH on the asymmetry gate (2.9:1, just under the 3.0 floor) — a
  near-miss, not a hard fail.
- **PLTR** — carried over again; still likely a business-activity fail per
  external screeners (government/defense/intelligence contracts) despite a
  clean ratio pre-check here (see Action flag #5 above).
- **MT (near-zero engineered range)** — same as last run: entry $65.35 /
  stop $65.31 / T1 $65.42 is a ~6-cent range on a $65 stock — looks like a
  formula edge case, not a tradeable setup; don't trust it without checking
  the raw ATR/52w-high inputs by hand.
- **MU / ALAB (RESEARCH)** — capped by the mechanical gates, not a business
  problem: MU fails the 60-day catalyst horizon (75 days to its print); ALAB
  fails the >=3.0 asymmetry floor (1.8:1).
- Dropped from the top-20 vs. last run: AR, AU, CDE, TER, CF, SIMO, AMD —
  discovery-pool churn (ranked out by max-benefit), not a status change on
  any card you may have already reviewed for those names.

## Follow-ups (priority order)

1. **[Urgent — 7th run unresolved, now ~4 weeks] FIG compliance**: re-screen
   in Zoya/Musaffa; this is the longest this gate has sat unresolved since
   the routine started.
2. **[New — earnings 12 days out] NOW**: decide your `earnings_plan` stance
   (hold-through vs. reduce-into-print) ahead of the 2026-07-22 print.
3. **[Recurring — Shariah] PLTR**: likely business-activity fail per external
   screeners — screen carefully before writing it up as anything beyond RESEARCH.
4. **[Recurring — data quality] MT setup card**: implausibly tight
   auto-filled band (~6 cents on a $65 stock); verify the raw inputs before trusting it.
5. **[Housekeeping] 7 new DRAFT setup cards** this run (MSFT, ZS, CLS, STX,
   APH, JNJ, GOOGL) — none are `planned`, none can reach BUY-CANDIDATE yet.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Figma Shares Edge Higher Thursday: What's Driving the Move? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60373502/figma-shares-edge-higher-thursday-whats-driving-the-move)
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [Insider Sell: Shaunt Voskanian Sells 8,629 Shares of Figma Inc (FIG) — GuruFocus](https://www.gurufocus.com/news/8950468/insider-sell-shaunt-voskanian-sells-8629-shares-of-figma-inc-fig)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenows-q2-2026-earnings-expect-121215371.html)
- [+6.31% for ServiceNow stock as Q2 2026 earnings date approaches — TradersUnion](https://tradersunion.com/news/financial-news/show/2549550-servicenow-gains-6-31percent-to-usd105-54/)
