# Portfolio Assessment — 2026-07-11

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (8 new DRAFT setup cards auto-filled: MSFT, ZS, STX,
CLS, APH, GDDY, JNJ, ESE — one Yahoo lookup errored with a transient HTTP 500
and was skipped, not fabricated) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps on the
two holdings. `journal.py` still reports 0 closed trades (no
`transactions.csv` yet — discipline guard stays dormant until you start
logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a seventh consecutive run** (first
flagged on the 2026-06-09 screen). Live price **$21.11**, essentially flat
vs. the $21.43 cost basis (**-1.5%**).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.8:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| DCF intrinsic value | **$15.08** vs. $21.11 price -> **-28.6%** (price is rich to the model) |
| Trailing stop (chandelier) | $18.9688 — price ~10.1% above it |
| 6m momentum (skip last month) | -45.0% |
| Portfolio note | ATR 7.03% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$107.71**, **-6.3%** vs. $114.97 cost basis — inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 1.1:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| DCF intrinsic value | **$120.42** vs. $107.71 price -> **+11.8% upside** to the model |
| Trailing stop (chandelier) | $96.6068 — price is $11.10 above it (no longer breached; see note below) |
| 6m momentum (skip last month) | -29.1% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own thesis input |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

**Update on the open question from 2026-07-07:** that report flagged NOW
trading *below* its computed chandelier trailing stop ($107.93 vs. $109.98).
This run the stop has recalculated to **$96.6068** — well below the current
$107.71 price — so the "breach" has resolved itself as the trailing level
recalculated on updated volatility/price data, not because you took any
action. Worth remembering this rule is structurally inert for NOW regardless:
`trade_type: core` exempts it from `verdict.py`'s TRAIL_STOP rule, so even a
future breach won't mechanically fire a SELL/REVIEW on this position.

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $21.11 | 35 | $21.43 | $738.85 | -1.5% | 49.5% |
| NOW | $107.71 | 7 | $114.97 | $753.97 | -6.3% | 50.5% |

**Total value: $1,492.82** | Cost: $1,554.84 | **Total return: ~-4.0%** (-$62.02 unrealised)

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. **Seventh run unresolved.** COMPLIANCE_GATE fires -> SELL.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF / FIG] Price is ~40% above intrinsic value** ($21.11 vs. $15.08) on
   the recorded growth/discount assumptions — another data point (beyond the
   compliance gate) against treating the recent analyst-driven bounce as a
   reason to stay.
4. **[Catalyst / NOW] Q2 FY2026 earnings confirmed for 2026-07-22** (11 days
   out, after market close) — first hard date for this print; prior reports
   only had a soft/unconfirmed date on the holding card. Worth updating
   `holdings/now-servicenow.md`'s `catalyst.date` field.
5. **[Shariah / recurring lead] PLTR** — reappears as a LEAD again this run
   (unchanged draft card from prior cycles). External screeners remain split,
   with at least one rating it business-activity non-compliant on
   government/defense/intelligence contract exposure. Still UNVERIFIED here —
   don't read that as "probably fine."
6. **[Data quality / MT] Near-zero engineered range persists** — entry
   $65.35 / stop $65.31 / target $65.42, a ~6-11 cent band on a $65 stock,
   flagged as a likely formula edge case in the prior report and still
   present unchanged this run (card not yet reviewed).

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** three major banks (Citigroup,
Bank of America, and a third per the July rally coverage) initiated or
resumed bullish coverage in late June/early July, citing AI-credit
monetization (75% of enterprise accounts bought supplementary AI credits past
their threshold) and enterprise traction ($100K+ ARR accounts +48% y/y, net
dollar retention 139%). Stock has grinded up off its June lows near $16.84
into the low-$20s on this coverage.

**Case to exit (compliance + DCF, both independent of each other and of the
above):** NON-COMPLIANT per your mandate — this overrides any fundamental
debate; seven consecutive cycles unresolved now. The DCF model (30% 5y
growth, 12% discount rate) puts intrinsic value at $15.08 vs. a $21.11 price,
a ~40% premium to the model even setting compliance aside — the bullish
analyst narrative doesn't change either gate.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings are now confirmed for **2026-07-22**
after market close (11 days out) — the prior report only had this catalyst
as unconfirmed/soft. DCF shows +11.8% upside to intrinsic value ($120.42) at
recorded assumptions. Business fundamentals (Armis integration, AI-agent
expansion) unchanged since the last review.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-29.1% (worse than the -23% read on 07-07); the recalculated chandelier stop
sits well below price now ($96.61 vs. $107.71), which reads as a wider,
looser trail, not a tighter one — worth noting the earnings print lands 11
days out and can gap either direction, and this position's `trade_type: core`
tag means no mechanical trailing-stop protection either way.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a seventh consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -6.3% vs. the 20% threshold.
- **TRAIL_STOP -> NOW**: does not fire (trade_type: core exempts it from the
  technical trailing-stop rule); the computed level moved from just above
  price (07-07) to well below price (today) purely from recalculation, not
  action taken.
- **VOL_THROTTLE note -> FIG**: ATR 7.03% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.11 | -28.6% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $107.71 | +11.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is currently **empty** — nothing
for step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — 20 leads, 8 fresh DRAFT cards this run

`discover.py` rebuilt the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens), applied the
liquidity floor + Shariah-ratio/asymmetry/catalyst gates, and rewrote
**`leads.md`** (top 20 by max-benefit rank). Compared to 2026-07-07's pool,
**MSFT, ZS, STX, CLS, APH, GDDY, JNJ, and ESE are new this run** (AR, AU,
CDE, TER, SIMO, AMD, KLIC dropped out of the top 20). `scaffold.py
--all-leads` auto-filled a **DRAFT** `setups/<ticker>.md` card for each of
the 8 newcomers that lacked one; the 12 repeat names already had cards from
prior runs and were left untouched. **Every row below is `status: draft`,
unreviewed, and Shariah UNVERIFIED — these are proposals to review and edit,
never buys.** None can reach BUY-CANDIDATE until you review the card, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa.

Note on the two reward:risk columns: **leads R:R** is discover.py's
discovery-stage estimate (drives the LEAD vs. RESEARCH gate below).
**Card R:R (T1)** is the scaffolded setup card's engineered target, fixed by
construction at your `t1_r: 1.5` policy knob for nearly every name — two
different numbers answering two different questions.

| Ticker | Verdict (leads.md) | Setup type | Entry | Stop | T1 target | Card R:R (T1) | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|---|
| MSFT | LEAD (new) | earnings_run | $385.10 | $375.65 | $399.27 | 1.5:1 | 12.8:1 | earnings 2026-07-29 | 18 |
| ALKT | LEAD | earnings_run | $18.95 | $16.99 | $21.89 | 1.5:1 | 20.0:1 | earnings 2026-07-29 | 18 |
| FICO | LEAD | earnings_run | $1286.51 | $1134.67 | $1514.28 | 1.5:1 | 8.0:1 | earnings 2026-07-29 | 18 |
| ZS | LEAD (new) | earnings_run | $139.27 | $133.57 | $147.82 | 1.5:1 | 12.8:1 | earnings 2026-09-02 | 53 |
| PLTR | LEAD | earnings_run | $132.54 | $131.84 | $133.59 | 1.5:1 | 8.4:1 | earnings 2026-08-03 | 23 |
| STX | LEAD (new) | earnings_run | $910.34 | $889.96 | $940.91 | 1.5:1 | 5.5:1 | earnings 2026-07-28 | 17 |
| LIF | LEAD | earnings_run | $56.73 | $49.97 | $66.87 | 1.5:1 | 6.8:1 | earnings 2026-08-10 | 30 |
| DUOL | LEAD | earnings_run | $129.72 | $111.80 | $156.60 | 1.5:1 | 6.9:1 | earnings 2026-08-05 | 25 |
| CLS | LEAD (new) | earnings_run | $359.85 | $341.49 | $387.39 | 1.5:1 | 6.2:1 | earnings 2026-07-27 | 16 |
| VRNS | LEAD | earnings_run | $45.67 | $39.71 | $54.61 | 1.5:1 | 4.8:1 | earnings 2026-07-28 | 17 |
| ULTA | LEAD | earnings_run | $452.49 | $447.62 | $459.79 | 1.5:1 | 8.0:1 | earnings 2026-08-27 | 47 |
| APH | LEAD (new) | earnings_run | $159.06 | $156.96 | $162.21 | 1.5:1 | 5.4:1 | earnings 2026-07-29 | 18 |
| MT | LEAD | earnings_run | $65.35 | $65.31 | $65.42 | 1.75:1 | 3.6:1 | earnings 2026-07-30 | 19 |
| MU | RESEARCH | pullback | $1032.92 | $949.32 | $1158.32 | 1.5:1 | 5.7:1 | earnings 2026-09-23 | 74 (>60d horizon) |
| PAY | LEAD | earnings_run | $28.15 | $25.00 | $32.87 | 1.5:1 | 5.0:1 | earnings 2026-08-03 | 23 |
| ALAB | RESEARCH | earnings_run | $432.74 | $371.67 | $524.34 | 1.5:1 | 2.0:1 | earnings 2026-08-04 | 24 |
| GDDY | LEAD (new) | earnings_run | $88.92 | $79.43 | $103.16 | 1.5:1 | 4.1:1 | earnings 2026-07-30 | 19 |
| ADI | LEAD | earnings_run | $388.83 | $386.48 | $392.35 | 1.5:1 | 5.3:1 | earnings 2026-08-19 | 39 |
| JNJ | RESEARCH (new) | earnings_run | $256.98 | $250.94 | $266.05 | 1.5:1 | 2.0:1 | earnings 2026-07-15 | 4 |
| ESE | LEAD (new) | earnings_run | $329.12 | $321.45 | $340.62 | 1.5:1 | 4.3:1 | earnings 2026-08-10 | 30 |

All 20 cleared the liquidity floor (`avg $vol` >= $5M, market cap >= $500M)
and a clean ratio pre-check — not a business-activity screen. Shariah status
on every card is `unverified` by construction (only a human Zoya/Musaffa
screen can set `compliant`).

**Flags worth your attention before reviewing any of these:**
- **PLTR (Palantir)** — same recurring flag as prior runs: government/
  defense/intelligence data analytics business; at least one external
  screener rates it non-compliant on business-activity grounds despite a
  clean ratio pre-check here. Screen skeptically, not as a rubber stamp.
- **MT (near-zero engineered range)** — unchanged from 07-07: entry $65.35 /
  stop $65.31 / T1 $65.42 is a few-cent range on a $65 stock, still looking
  like a formula edge case rather than a tradeable setup. Don't trust this
  card's levels without checking the underlying ATR/52w-high inputs by hand.
- **JNJ / SPUS-holding leads (MSFT, MU, JNJ)** — these three source from
  `discover_etfs: [SPUS]`, i.e. they're already inside the halal ETF you'd
  benchmark against, not independent discoveries; JNJ caps at RESEARCH on the
  asymmetry gate (2.0:1 < 3.0 floor) despite its catalyst landing in just 4
  days.
- **MU (RESEARCH, not LEAD)** — still capped by the 60-day catalyst horizon
  (74 days to its print), same as 07-07; nothing changed structurally.
- **8 newcomers (MSFT, ZS, STX, CLS, APH, GDDY, JNJ, ESE) are unreviewed** —
  first appearance in the top-20 pool this run; treat their DRAFT cards with
  the same scrutiny as any other before considering `status: planned`.

## Follow-ups (priority order)

1. **[Urgent — 7th run unresolved] FIG compliance**: re-screen in Zoya/Musaffa.
2. **[Housekeeping] NOW catalyst date**: Q2 FY2026 earnings now confirmed for
   2026-07-22 — update `holdings/now-servicenow.md`'s `catalyst.date` field
   (currently `null`).
3. **[Recurring — Shariah] PLTR**: likely business-activity fail (government/
   defense/intelligence contracts) per external screeners despite a clean
   ratio pre-check here — screen carefully before writing it up as anything
   beyond RESEARCH.
4. **[Recurring — data quality] MT setup card**: still an implausibly tight
   entry/stop/target band; don't trust it without checking raw ATR/52w-high
   inputs.
5. **[New] 8 fresh DRAFT setup cards** (MSFT, ZS, STX, CLS, APH, GDDY, JNJ,
   ESE) added this run; review at your own pace alongside the 12 carried
   over from prior cycles — none are `planned` yet.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [Figma (FIG) Stock Surges as Three Major Banks Turn Bullish on AI Potential — Parameter](https://parameter.io/figma-fig-stock-surges-as-three-major-banks-turn-bullish-on-ai-potential/)
- [Figma (FIG) Leads Software Stocks with 9% Surge Amid Sector Rally — GuruFocus](https://www.gurufocus.com/news/8941429/figma-fig-leads-software-stocks-with-9-surge-amid-sector-rally)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — Business Wire](https://www.businesswire.com/news/home/20260701382890/en/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect)
