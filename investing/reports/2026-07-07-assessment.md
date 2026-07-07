# Portfolio Assessment — 2026-07-07

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (20 DRAFT setup cards auto-filled) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` still reports
0 closed trades (no `transactions.csv` yet — discipline guard stays dormant
until you start logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a sixth consecutive run.** Live
price **$21.08**, essentially flat vs. the $21.43 cost basis (**-1.6%**).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -4.3:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| DCF intrinsic value | **$15.08** vs. $21.08 price -> **-28.5%** (price is rich to the model) |
| Trailing stop (chandelier) | $19.6963 — price ~7.0% above it |
| 6m momentum (skip last month) | -39.0% |
| Portfolio note | ATR 6.65% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$107.93**, **-6.1%** vs. $114.97 cost basis — inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — recommend.py can't self-assess without a stated thesis-vs-price edge |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| DCF intrinsic value | **$120.42** vs. $107.93 price -> **+11.6% upside** to the model |
| Trailing stop (chandelier) | $109.9805 — **price is now $2.05 below it** |
| 6m momentum (skip last month) | -23.0% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own thesis input |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

**Closing yesterday's open question on NOW's trailing stop:** price is now
*below* the computed chandelier level ($107.93 vs. $109.98), yet
`verdict.py` still returns HOLD, not SELL. This is not a data lag — it's
structural: `verdict.py`'s TRAIL_STOP rule only fires for
`trade_type in (swing, momentum, catalyst)`, and NOW's holding record is
tagged `trade_type: core`. Core-tagged positions never get a mechanical
TRAIL_STOP regardless of price, by design. Worth a deliberate decision on
your end: either that's the policy you want for a long-horizon "core"
holding (trailing stops are a swing-trading tool; core positions are meant
to ride through this), or the front-matter `trade_type` on NOW should be
revisited if you actually want the technical stop enforced.

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $21.08 | 35 | $21.43 | $737.80 | -1.6% | 49.4% |
| NOW | $107.93 | 7 | $114.97 | $755.51 | -6.1% | 50.6% |

**Total value: $1,493.31** | Cost: $1,554.84 | **Total return: ~-4.0%** (-$61.53 unrealised)

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Sixth run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[Technical / NOW] Price is now below the chandelier trailing stop**
   ($107.93 vs. $109.98) — but see the note above: this doesn't mechanically
   trigger anything for a `core`-tagged holding. Flagging it here so it
   doesn't get missed just because the rule engine stays silent on it.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
4. **[DCF / FIG] Price is ~40% above intrinsic value** ($21.08 vs. $15.08) on
   the recorded growth/discount assumptions — another data point (beyond the
   compliance gate) against treating any near-term bounce as a reason to stay.
5. **[Shariah / new lead] PLTR** — today's discovery pool surfaced Palantir as
   a LEAD (see below); external screeners are split, with at least one
   (Musaffa) rating it DOUBTFUL and another citing >5% prohibited income tied
   to government/defense/intelligence contracts, which the ratio pre-check
   here can't see (it only checks debt/cash-to-market-cap, not business
   activity). Treat as a likely fail pending your own Zoya/Musaffa screen —
   don't let "UNVERIFIED" read as "probably fine."

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** design-platform growth story
intact per its last reported quarter; nothing new in the news flow this run
that changes the fundamental picture materially.

**Case to exit (compliance + DCF, both independent of each other):**
NON-COMPLIANT per your mandate — this overrides any fundamental debate; six
consecutive cycles unresolved now. The DCF model (30% 5y growth, 12%
discount rate) puts intrinsic value at $15.08 vs. a $21.08 price, a ~40%
premium to the model even setting compliance aside.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (15 days out) —
analysts model subscription revenue of $3.815–3.820B (~21–21.5% cc growth)
and EPS of $0.40 (down y/y on comp, not a growth story break); a joint
AI-security offering with Accenture launched this quarter extends the
enterprise-security narrative; DCF shows +11.6% upside to intrinsic value
($120.42) at recorded assumptions. Consensus remains "Strong Buy" (36/44
analysts per one tracker).

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-23%; and price has now slipped *below* the chandelier trailing stop
($107.93 vs. $109.98) — mechanically inert for a `core` position (see note
above), but worth your own judgment call given the earnings print is 15 days
away and could gap either direction.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a sixth consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -6.1% vs. the 20% threshold.
- **TRAIL_STOP -> NOW**: does NOT fire (trade_type: core exempts it from the
  technical trailing-stop rule) even though price is now below the computed
  level — a policy gap worth a deliberate look, not a bug to silently trust.
- **VOL_THROTTLE note -> FIG**: ATR 6.65% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.08 | -28.5% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $107.93 | +11.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is currently **empty** — nothing
for step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — 20 fresh DRAFT cards from today's discovery

`discover.py` built a fresh candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens), applied the
liquidity floor + Shariah-ratio/asymmetry/catalyst gates, and wrote
**`leads.md`** (top 20 by max-benefit rank). `scaffold.py --all-leads` then
auto-filled a **DRAFT** `setups/<ticker>.md` card for every one of them —
complete proposed plans (entry/stop/T1/T2, gap plan, invalidation) from
Yahoo formula outputs. **Every row below is `status: draft`, unreviewed, and
Shariah UNVERIFIED — these are proposals to review and edit, never buys.**
None of these can reach BUY-CANDIDATE until you review the card, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa.

Note on the two reward:risk columns: **leads R:R** is discover.py's
discovery-stage estimate (drives the LEAD vs. RESEARCH gate below —
RESEARCH means it failed the >=3.0 asymmetry floor or the 60-day catalyst
horizon at discovery time). **Card R:R (T1)** is the scaffolded setup card's
*engineered* target, which is fixed by construction at your `t1_r: 1.5`
policy knob (1.5x the stop distance) — so it reads ~1.5:1 for nearly every
name regardless of the discovery-stage number. That's not a bug; it's two
different numbers answering two different questions (screening estimate vs.
locked-in trade plan), but they shouldn't be read as the same figure.

| Ticker | Verdict (leads.md) | Setup type | Entry | Stop | T1 target | Card R:R (T1) | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|---|
| AR | LEAD | earnings_run | $34.68 | $34.12 | $35.52 | 1.5:1 | 18.4:1 | earnings 2026-07-29 | 22 |
| PLTR | LEAD | earnings_run | $132.54 | $131.84 | $133.59 | 1.5:1 | 20.0:1 | earnings 2026-08-03 | 27 |
| AU | LEAD | earnings_run | $84.05 | $83.31 | $85.16 | 1.5:1 | 17.9:1 | earnings 2026-07-31 | 24 |
| CDE | LEAD | earnings_run | $16.99 | $16.07 | $18.38 | 1.5:1 | 11.7:1 | earnings 2026-08-05 | 29 |
| ULTA | LEAD | earnings_run | $452.49 | $447.62 | $459.79 | 1.5:1 | 20.0:1 | earnings 2026-08-27 | 51 |
| MT | LEAD | earnings_run | $65.35 | $65.31 | $65.42 | 1.75:1 | 6.0:1 | earnings 2026-07-30 | 23 |
| MU | RESEARCH | pullback | $1032.92 | $949.32 | $1158.32 | 1.5:1 | 5.3:1 | earnings 2026-09-23 | 78 (>60d horizon) |
| TER | LEAD | earnings_run | $379.52 | $375.76 | $385.16 | 1.5:1 | 5.8:1 | earnings 2026-07-29 | 22 |
| VRNS | LEAD | earnings_run | $45.67 | $39.71 | $54.61 | 1.5:1 | 3.0:1 | earnings 2026-07-28 | 21 |
| CF | LEAD | earnings_run | $113.20 | $106.79 | $122.81 | 1.5:1 | 4.4:1 | earnings 2026-08-05 | 29 |
| DUOL | LEAD | earnings_run | $129.72 | $111.80 | $156.60 | 1.5:1 | 4.9:1 | earnings 2026-08-05 | 29 |
| SIMO | RESEARCH | earnings_run | $318.86 | $273.25 | $387.27 | 1.5:1 | 0.8:1 | earnings 2026-07-30 | 23 |
| LIF | LEAD | earnings_run | $56.73 | $49.97 | $66.87 | 1.5:1 | 4.7:1 | earnings 2026-08-10 | 34 |
| ALAB | RESEARCH | earnings_run | $432.74 | $371.67 | $524.34 | 1.5:1 | 1.1:1 | earnings 2026-08-04 | 28 |
| ADI | LEAD | earnings_run | $388.83 | $386.48 | $392.35 | 1.5:1 | 5.8:1 | earnings 2026-08-19 | 43 |
| ALKT | LEAD | earnings_run | $18.95 | $16.99 | $21.89 | 1.5:1 | 4.2:1 | earnings 2026-07-29 | 22 |
| FICO | LEAD | earnings_run | $1286.51 | $1134.67 | $1514.28 | 1.5:1 | 3.5:1 | earnings 2026-07-29 | 22 |
| AMD | RESEARCH | earnings_run | $552.05 | $467.12 | $679.45 | 1.5:1 | 0.4:1 | earnings 2026-08-04 | 28 |
| KLIC | RESEARCH | earnings_run | $119.61 | $108.81 | $135.81 | 1.5:1 | 1.5:1 | earnings 2026-08-06 | 30 |
| PAY | LEAD | earnings_run | $28.15 | $25.00 | $32.87 | 1.5:1 | 3.5:1 | earnings 2026-08-03 | 27 |

All 20 cards passed the liquidity floor (`avg $vol` >= $5M, market cap >=
$500M) and cleared a clean ratio pre-check (business_ok, debt/liquid ratios
within bounds) — but the ratio pre-check is *not* a business-activity
screen. Shariah status on every card is `unverified` by construction (only a
human Zoya/Musaffa screen can set `compliant`).

**Flags worth your attention before reviewing any of these:**
- **PLTR (Palantir)** — see Action flag #5 above. Business is largely
  government/defense/intelligence data analytics (Gotham, Foundry; contracts
  include military and ICE work). At least one Shariah screener rates it
  DOUBTFUL/non-compliant on business-activity grounds (~5.7% prohibited
  income, over the 5% threshold), independent of the clean ratio pre-check
  here. Screen this one skeptically, not as a rubber stamp.
- **AU (AngloGold Ashanti) / CDE (Coeur Mining)** — precious-metals miners;
  like the gold names flagged in prior reports, mining/royalty economics can
  raise Shariah questions (financing structures, hedging/derivatives use)
  that a debt-ratio check alone won't catch. Confirm business-activity
  screen, not just the ratio.
- **MT (near-zero engineered range)** — entry $65.35 / stop $65.31 / T1
  $65.42 is a ~6-cent range on a $65 stock (ATR $2.40 elsewhere in the
  formula doesn't reconcile with this tight a chandelier band) — this looks
  like a formula edge case, not a tradeable setup. Don't treat MT's card as
  reliable without checking the underlying ATR/52w-high inputs by hand.
- **MU / SIMO / ALAB / AMD / KLIC (RESEARCH, not LEAD)** — capped by the
  mechanical gates, not by a business problem: MU fails the 60-day catalyst
  horizon (78 days to its print); the other four fail the >=3.0 asymmetry
  floor on the discovery-stage reward:risk. Nothing wrong with these names,
  just not clearing the bar today.
- **AR (Antero Resources)** confirmed as the natural-gas E&P (not a
  financial-services or other ambiguous "AR" ticker) — Q1 2026 results beat
  on revenue ($1.95B vs. $1.71B est.), production +21% y/y. Standard
  oil-and-gas-producer profile; still needs its own business-activity and
  hedging-structure screen.

## Follow-ups (priority order)

1. **[Urgent — 6th run unresolved] FIG compliance**: re-screen in Zoya/Musaffa.
2. **[New — policy decision] NOW trailing stop**: price is below the
   computed chandelier level but `trade_type: core` structurally exempts it
   from `verdict.py`'s TRAIL_STOP rule. Decide whether that's the policy you
   want, or whether NOW's `trade_type` should change.
3. **[New — Shariah] PLTR**: likely business-activity fail (government/
   defense/intelligence contracts) per external screeners despite a clean
   ratio pre-check here — screen carefully before writing it up as anything
   beyond RESEARCH.
4. **[New — data quality] MT setup card**: the auto-filled entry/stop/target
   band is implausibly tight (~6 cents on a $65 stock); don't trust it
   without checking the raw ATR/52w-high inputs.
5. **[Housekeeping] 20 DRAFT setup cards now exist** in `setups/` from
   today's first `--all-leads` scaffold run — none are `planned`, none can
   reach BUY-CANDIDATE yet. Review at your own pace; they don't expire, but
   the earnings dates they're built around (mostly late July/early August)
   do.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [Figma Stock 2026: Why $89M in Cash Flow Can't Stop the Slide — Memeburn](https://memeburn.com/figma-stock-2026-cash-flow/)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect)
- [+6.31% for ServiceNow stock as Q2 2026 earnings date approaches — TradersUnion](https://tradersunion.com/news/financial-news/show/2549550-servicenow-gains-6-31percent-to-usd105-54/)
- [Is Palantir Technologies (PLTR) Stock Halal or Haram? — Zoya](https://zoya.finance/stocks/pltr)
- [Is Palantir Technologies Inc. (PLTR) Stock Halal? — HalalScreener](https://halalscreener.app/en/stock/PLTR)
- [Is Palantir Technologies Inc - PLTR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/PLTR/)
- [Antero Resources Announces First Quarter 2026 Financial and Operating Results](https://www.anteroresources.com/investors/press-releases/detail/257/antero-resources-announces-first-quarter-2026-financial-and)
