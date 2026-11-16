# Portfolio Assessment — 2026-11-16

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data) → `scaffold.py --all-leads` (**29 new DRAFT
cards**; 21 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live. Yahoo
returned HTTP 429 on the crumb fetch for several scripts but continued
without it; every script returned full data. No `transactions.csv` /
`journal.csv` exists yet, so the discipline guard stays dormant.

**Since the last report (2026-08-19, ~3 months ago):** no trades recorded.
NOW fell from $128.63 to **$101.35 (-21%)**, mostly on a record one-day
drop after Q3 earnings on 2026-10-29. BMNR fell from $20.54 to **$16.65
(-19%)**. Book value is down from $1,105.51 to **$876.00**. Both recorded
Shariah screens are now **stale** (>100 days old).

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically, not advice.
Portfolio note: only 2 holdings, so concentration rules stay muted until
there are at least 4 names. **Vol throttle (new this run):** BMNR ATR 8.97%
and NOW ATR 6.79%, both above the 6% `vol_throttle_atr_pct`, so the rule
says size down on any adds.

**NOW -> HOLD** (RULE: VALUATION_RICH — recorded P/E ~119 >= `pe_rich` 50; hold, do not add).
Price **$101.35**, **-11.8%** vs. $114.97 cost. Trailing stop (chandelier)
$138.87 — **price is ~27% BELOW it**, but `trade_type: core` exempts NOW from
TRAIL_STOP, so it does not fire. 6m momentum (skip last month) +37.3%
(the lookback window predates the October drop). R-multiple: n/a (no `initial_stop`).

| PM-grade record (recommend.py — mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW — "missing reward:risk or a stated thesis"; `variant_view`, `initial_stop`, `target_price`, `invalidation`, `pre_mortem` are all still null in the holding file |
| Shariah | **REVIEW** — recorded compliant, but screened 2026-06-09 (stale); ratio pre-check clean (debt 2.3%, liquid 6%) |
| Target / method | $119.65 / DCF intrinsic value (+18.1%) |
| Stop | $138.87 chandelier, which is above price and so meaningless as a downside level here |
| Time horizon | core |
| Would buy today? | Mechanically "yes" — but this check reads the recorded Shariah field, which is stale |

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Price **$16.65**,
**+7.9%** vs. $15.43 cost. Trailing stop $20.06 — **price is ~17% BELOW it**
(`core` exemption again). 6m momentum +15.6%. R-multiple n/a.

| PM-grade record (recommend.py — mechanical proxy) | |
|---|---|
| Conviction | LOW — no thesis, target or stop in the holding file |
| Shariah (recorded) | **REVIEW** — broker_app compliant, screened 2026-07-07, now stale |
| Shariah (mechanical pre-check) | **FAIL, 2nd run in a row** — industry `Capital Markets`, core business fails the screen |
| Target / method | -$6.53 / DCF (not meaningful for a crypto treasury; see DCF) |
| Would buy today? | Mechanically "yes" — reads only the recorded field; it **cannot see** the business-activity fail |

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| NOW | $101.35 | 7 | $114.97 | $709.45 | -11.8% | 81.0% |
| BMNR | $16.65 | 10 | $15.43 | $166.55 | +7.9% | 19.0% |

**Total value: $876.00** | Cost: $959.09 | **Total return: -8.7%** (-$83.09 unrealised).
Last report: $1,105.51 (+15.3%).

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are now stale.** NOW was screened
   2026-06-09 and BMNR 2026-07-07, both past the ~1-quarter freshness
   window. `recommend.py` has moved both to Shariah `REVIEW`. Re-screen both
   in Zoya/Musaffa.
2. **[Mandate — still open from last run] BMNR business-activity pre-check
   FAILS** (`Capital Markets` — core business fails screen). Current
   reporting still describes an ETH-treasury model: 6.07M ETH plus $14.3B
   total crypto/cash/securities as of Nov 8, with ~5.23M ETH staked and
   staking yield projected at $309–359M a year
   ([Finviz/PRN](https://finviz.com/news/419085/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-607-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-143-billion),
   [Yellow](https://yellow.com/press-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-6-07-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-14-3-billion)).
   Per Gate 1, a confirmed business-activity fail is an absolute SELL. The
   automated COMPLIANCE_GATE will not fire until you update the recorded
   status, so resolving this is on you.
3. **[Thesis check — NEW] NOW's Q3 print touched your own "what would change
   my mind" line.** Your holding file says: *"Subscription growth
   decelerating meaningfully below current ~21-22% YoY, or a guidance cut."*
   On 2026-10-29 NOW guided Q4 cRPO growth to **18.5%** (constant
   currency). The CFO said early renewals pulled deals into Q3 and accounted
   for about half of the cRPO beat. The stock fell ~27%, its worst day on
   record ([CNBC](https://www.cnbc.com/2026/10/29/servicenow-now-earnings-q3-2026.html),
   [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-stock-falls-crpo-growth-144947961.html)).
   It is your call whether 18.5% counts as "meaningfully below". Full-year
   subscription guidance was raised slightly, not cut. `thesis_broken` is
   not set, so the engine has not reacted.
4. **[Data hygiene] NOW holding file is stale.** Its `catalyst` still reads
   "Q2 FY2026 earnings" with `date: null`, and `last_review` is 2026-06-15,
   which passes the 90-day `review_cadence_days`. `last_price` (106.40) and
   the recorded P/E 119 that drives VALUATION_RICH were written before the
   drop.
5. **[Valuation / NOW]** VALUATION_RICH is still active on the recorded P/E,
   so the rule says do not add.
6. **[Card hygiene — NEW] Some carried-over setup cards point at prints that
   have already happened.** The LEAD-tier names AVGO, ADI and SNX have cards
   from earlier runs whose entry triggers reference Aug/Sep 2026 prints and
   old levels. The AVGO card's stop ($384.52) sits *above* its entry
   ($364.41), so it has no valid R. The scaffold does not overwrite existing
   cards without `--force`. Rewrite these, or re-scaffold them with
   `python scripts/scaffold.py <TICKER> --force`, before relying on them.

## Per-holding read

### NOW — ServiceNow, Inc
**Case to keep:**
- Q3 revenue (~$4.11B) was in line.
- RPO grew 22.5% to $29.7B and cRPO grew 21% to $13.65B.
- Free cash flow rose to $822M from $592M.
- Full-year subscription outlook was nudged up, and new AI contract value rose sharply.
- DCF ($119.65, 18% growth / 10% discount) now sits ~18% *above* price,
  versus ~7% below price last run.
- Price is at 13% of its 52-week range.
- Some commentators frame the drop as an overreaction
  ([Motley Fool](https://www.fool.com/investing/2026/11/01/why-the-27-crash-in-servicenows-stock-looks-like-a/)).

**Case to trim/exit:**
- The Q4 cRPO guide of 18.5% is below the ~21–22% growth rate your thesis
  is anchored to, and half of the Q3 beat was pulled-forward renewals.
- Non-GAAP EPS of $1.00 missed the $1.02 estimate.
- The selloff reflects "AI disrupts seat-based SaaS" fears, which challenge
  the core of the thesis.
- No buyback in the quarter, versus $584M a year earlier.
- At 81% of the book, NOW dominates the portfolio's outcome.

Sources: [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/10/62691088/servicenow-posts-downbeat-q3-earnings-joins-sprouts-farmers-market-alphabet-and-other-big-stocks-moving-lower-in-thursdays-pre-market-session) ·
[Chartmill](https://www.chartmill.com/news/NOW/Chartmill-57112-ServiceNow-NYSENOW-Stock-Tumbles-After-Q3-Earnings-Miss-and-Soft-Guidance) ·
[Traders Union](https://tradersunion.com/news/stocks/show/4016773-servicenow-shares-q3-earnings-miss/).
Next earnings are ~late January 2027, outside the 60-day horizon (no date confirmed in this run's research).

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep:**
- Still above cost (+7.9%).
- Continues to add ETH (6.07M tokens) and stakes most of it.
- Joined the Russell 1000 in June 2026.

**Case to flag:**
- The compliance question above is unresolved for a second run.
- The share price is down ~55% over the past year per Benzinga, and the
  latest holdings value fell with the ETH price
  ([Benzinga](https://www.benzinga.com/quote/BMNR/charts)).
- The position has the highest ATR in the book (8.97%).
- The holding file is still essentially empty: no thesis, stop, target or
  pre-mortem.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW:** HOLD, do not add.
- **VOL_THROTTLE fired -> BMNR, NOW:** ATR% above 6, so size down per the throttle.
- **COMPLIANCE_GATE did not fire:** it reads only recorded `shariah.status`
  (both `compliant`). The staleness and BMNR's business-activity fail sit
  outside this rule, and only a re-screen by you resolves them.
- **TRAIL_STOP did not fire:** both names are `core` and exempt. Both
  prices are already well below their chandelier levels, so this rule would
  have fired for both if they were swing/momentum trades.
- **DRAWDOWN_REVIEW did not fire:** NOW is -11.8% vs. cost, under the 20% threshold.
- **Review cadence (90d) lapsed -> NOW:** `last_review` is 2026-06-15.
  Re-underwrite: "would I buy this here today?"

*If you execute anything from this report, run `/apply-trade` so the holdings files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $101.35 | +18.1% | growth_5y 18%, terminal 3%, discount 10% |
| BMNR | -$6.53 | $16.65 | n/m | growth_5y 5% (default), terminal 2.5%, discount 10% — a cash-flow model does not fit an ETH-treasury business; treat as a data gap |

The NOW figure assumes 18% five-year growth. If the cRPO deceleration
persists, that input is optimistic, and the "upside" shrinks accordingly.

## New ideas (watchlist.md)

`watchlist.md` is still **empty**, so there is nothing hand-curated to
research. `recommend.py`'s `ideas` array returned **0 BUY-CANDIDATEs**. That
is expected: no card in `setups/` is `planned`/`live`; all are `draft`.

## Draft & planned setups — 50 leads, 29 fresh DRAFT cards

Discovery wrote `leads.md` (top 50). Only **3 clear to LEAD tier**:

| Ticker | Tier | R:R (discovery) | Entry / target / stop (estimate) | Catalyst | Card |
|---|---|---|---|---|---|
| AVGO | LEAD | 9.2:1 | ~334.96 / 493.32 / 317.75 | earnings 2026-12-09 (23d) | stale (see flag 6) |
| ADI | LEAD | 4.4:1 | ~388.03 / 444.48 / 375.23 | earnings 2026-11-24 (8d) — needs a gap plan | stale |
| SNX | LEAD | 6.0:1 | ~239.44 / 298.19 / 229.68 | earnings 2027-01-07 (52d) | stale |

The other 47 are capped at RESEARCH, mostly by the catalyst-horizon gate:
next earnings fall after 2027-01-15. High-R:R RESEARCH names include KLAC,
AMAT, SANM and VIAV (20:1, a formula ceiling), LIF, FN, COHR and EVR.

**Shariah business-activity heads-up for review:** several new leads are
in businesses that typically fail a business screen. These include EVR,
PNFP, TRV, ALL and ACGL (finance/insurance), HST (hotels/REIT, alcohol
revenue), BF-B (alcohol) and FOX (media). They came from the
`undervalued_large_caps` screen. Expect AVOID once screened.

**RESEARCH — DRAFT awaiting your review (set `status: planned` to approve).**
The 29 new cards are:

ACGL, ALL, AMAT, ANET, APA, ASND, BBY, BF-B, COHR, DIOD, EVR, FN, FRO, HST,
HSY, KEYS, KLAC, LSCC, NTAP, NTNX, PNFP, SANM, SMTC, SNA, TRV, TS, TXN, UI,
VIAV

Every level on them is a Yahoo formula output: chandelier stop, EMA/breakout
entry, and an R-multiple target. Examples:

- **KLAC (pullback):** entry $156.23, stop $144.61, T1 $173.66 (1.5R), T2 $191.09 (3R).
- **AMAT (pullback):** entry $387.14, stop $355.05, T1 $435.27, T2 $483.41.

All 29 have `earnings_plan` set to the machine default and Shariah
**unverified**. They are proposals to edit, never buys. Approval means
fixing what you disagree with, screening the name in Zoya/Musaffa, and
flipping `status: planned`.

## Follow-ups (prioritized)

1. Re-screen **BMNR** in Zoya/Musaffa on the *business-activity* question,
   then update `shariah.status`. Gate 1 is absolute if it fails.
2. Re-screen **NOW** (stale since 2026-06-09).
3. Re-underwrite **NOW** against your own invalidation line, given the
   18.5% cRPO guide. Fill in `initial_stop`, `target_price`, `invalidation`
   and `pre_mortem`, update `catalyst`/`last_review`, and set
   `thesis_broken: true` if you conclude it is broken.
4. Fill in BMNR's holding file (thesis, stop, target), or decide it is not a position worth a thesis.
5. Refresh the stale AVGO/ADI/SNX cards before treating them as live leads.
   ADI's print is 8 days out.
6. Start logging trades via `/apply-trade` so the journal/discipline guard has data.

---
*Not financial advice. Decision support only. Verify every Shariah status in Zoya/Musaffa before acting.*
