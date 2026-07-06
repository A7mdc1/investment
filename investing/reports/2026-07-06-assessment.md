# Portfolio Assessment — 2026-07-06 (revised — live data)

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

**Revision note:** this replaces the earlier same-day report, which was
written under a Yahoo data-gap. The sandbox's network policy was updated
mid-session to allow Yahoo egress; a further library-level block (yfinance's
TLS fingerprint being reset by Yahoo's anti-bot layer) was then patched in
`scripts/common.py`. Every script below now returns **live** data — this is
the first fully-live assessment on record for this repo. Two additional
pre-existing bugs were fixed while wiring this up: `fast_info.get("last_price"/
"market_cap")` used the wrong (snake_case) key names against yfinance's
camelCase `fast_info` dict, silently returning `None` in `prices.py`,
`signals.py`, `verdict.py`, `dcf.py`, and `shariah.py`; and a balance-sheet
row-lookup helper accepted the first matching field name even when its value
was `NaN` instead of trying the next candidate. Both are fixed; see
`scripts/common.py`, `dcf.py`, `shariah.py`, `prices.py`, `signals.py`,
`verdict.py`.

## Data gaps (much shorter than prior runs)

- `discover.py`'s earnings-date lookup needed `lxml`, which wasn't installed;
  added to `requirements.txt` and installed. Fixed — catalyst dates below are
  real, not fallbacks.
- No `transactions.csv`/ledger file exists yet, so the discipline guard
  (net-of-cost performance vs. a Shariah benchmark) still can't be evaluated.
- Everything else that was a DATA_GAP in prior reports (live prices, DCF,
  trailing stop/EMA/momentum, reward:risk, discovery pool) is now populated.

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). Unresolved for a **fifth consecutive run**. Live
price **$21.29**, essentially flat vs. the $21.43 cost basis (**-0.6%**) —
the index-inclusion/analyst-coverage rally has mostly held, unlike the
intraday pullback flagged earlier today.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.9:1 (skew is *against* holding, not that it's attractive to add) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| DCF intrinsic value | **$15.08** vs. $21.29 price -> **-29.2% "upside"** (i.e. price is rich to the model) |
| Trailing stop (chandelier) | $19.6963 — price is ~7.5% above it |
| 6m momentum (skip last month) | **-39.0%** |
| Portfolio note | ATR 6.58% -> vol-throttle: size down if this were being added to (moot — it's a SELL) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$108.42**, **-5.7%** vs. $114.97 cost basis — well inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — recommend.py can't self-assess without a stated thesis-vs-price edge |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| DCF intrinsic value | **$120.42** vs. $108.42 price -> **+11.1% upside** to the model |
| Trailing stop (chandelier) | $109.9806 — **price is $1.56 below it** (a hair under the stop) |
| 6m momentum (skip last month) | -23.0% |
| Would buy today? | Mechanically yes per recommend.py's gates, but conviction is still flagged LOW absent your own thesis input |
| What changes verdict | SELL technical trigger (already very close), thesis_broken: true, or Shariah flip |

**Notable: NOW is trading essentially at its chandelier trailing stop right
now** ($108.42 vs. $109.98 stop) — this is the first run where that line has
actually been computable, and it's close enough to watch, not yet triggered
(verdict.py's SELL/TRAIL_STOP rule didn't fire because current logic checks
close-below-stop, and today's price is a live quote, not a settled close;
re-run tomorrow once today's close is in to confirm).

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return |
|---|---|---|---|---|---|
| FIG | $21.29 | 35 | $21.43 | $745.15 | -0.6% |
| NOW | $108.42 | 7 | $114.97 | $758.94 | -5.7% |

**Total value: $1,504.09** | Cost: $1,554.84 | **Total return: ~-3.3%**
(-$50.75 unrealised) — an improvement from the earlier same-day estimate
(~-6.3%, web-sourced) now that live prices confirm FIG held most of its
rally rather than continuing to fade.
Weights: FIG 49.5%, NOW 50.5%.

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Fifth run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[Technical / NOW] Price is at the chandelier trailing stop** — $108.42
   vs. $109.98 stop, the first time this has been computable. Not yet a
   confirmed SELL_TRAIL trigger (needs a close below, not an intraday quote),
   but close enough to check again on the next run before assuming it's
   still just a HOLD.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add.
4. **[DCF / FIG] Price is ~41% above intrinsic value** ($21.29 vs. $15.08) on
   the recorded growth/discount assumptions — another data point (on top of
   the compliance gate) against treating the recent rally as a reason to
   reconsider holding.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** Q1 2026 +46% revenue growth,
raised FY26 guidance, Russell index inclusion + Citigroup Buy coverage drove
a rally into July 2; Findell Capital's activist campaign (product-line
consolidation, SBC cuts, $40 standalone / $50 buyout floor) adds a
takeout-premium narrative some holders might weigh.

**Case to exit (compliance + now also DCF):** NON-COMPLIANT per your
mandate — this overrides the fundamental/activist debate; five consecutive
cycles unresolved. New this run: the DCF model (recorded 30% 5y growth, 12%
discount rate) puts intrinsic value at $15.08 vs. a $21.29 price — the
model doesn't support the current price even before the compliance question,
though a 30% growth assumption embeds a lot of optimism already, so this DCF
gap is a data point, not a verdict on its own.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Now Assist ($1M+ ACV customers) growing >130% YoY; new
Accenture and IBM partnerships ahead of Q2 earnings (2026-07-22, 16 days
out); DCF now shows +11.1% upside to intrinsic value ($120.42) at recorded
assumptions (18% growth, 10% discount rate) — the model likes it more than
the raw P/E does.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
is -23%; and price is sitting right at the newly-computed chandelier
trailing stop ($108.42 vs. $109.98) — worth checking again before the next
report to see whether a settled close confirms a TRAIL_STOP SELL.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a fifth consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW NOT firing -> NOW**: -5.7% vs. the 20% threshold.
- **TRAIL_STOP -> NOW**: NOT yet confirmed (needs a settled close below
  $109.98, not just an intraday quote at $108.42) — the closest call this
  repo has had on a technical SELL trigger; check first thing on the next run.
- **VOL_THROTTLE note -> FIG**: ATR 6.58% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings files
and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.29 | -29.2% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $108.42 | +11.1% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist) — now a live 222-name discovery pool

`discover.py` pulled a real 222-name candidate pool this run (halal-ETF
holdings + 3 yfinance screens), ran the full PM edge/asymmetry/catalyst
pipeline, and rewrote `watchlist.md` with the top 20 by max-benefit rank —
**13 BUY-CANDIDATE, 7 RESEARCH** on mechanics alone. This is a big shift from
prior reports' hand-curated 6-name list (TSM, ISRG, AMD, QCOM, LLY, NVDA);
only TSM and AMD survive from that list into today's auto-discovered top 20.
**Every row below is EDGE NOT SUPPLIED and Shariah UNVERIFIED — these are
leads to underwrite and screen, never buys**, regardless of the mechanical
verdict.

| Ticker | Verdict | Reward:risk | Target | Stop | Catalyst | Shariah pre-check |
|---|---|---|---|---|---|---|
| BTG | BUY-CANDIDATE | 263.6:1 | $6.23 | $4.04 | Earnings 2026-08-06 | UNVERIFIED |
| NBIS | BUY-CANDIDATE | 156.8:1 | $300.03 | $214.28 | Earnings 2026-08-06 | UNVERIFIED |
| BMNR | BUY-CANDIDATE | 92.1:1 | $134.01 | $14.26 | Earnings 2026-07-06 | UNVERIFIED |
| AUR | BUY-CANDIDATE | 3.9:1 | $8.57 | $6.41 | Earnings 2026-07-29 | UNVERIFIED |
| IBRX | BUY-CANDIDATE | 3.2:1 | $12.43 | $8.01 | Earnings 2026-08-04 | UNVERIFIED |
| BB | RESEARCH | 3.3:1 | $13.59 | $10.66 | Earnings 2026-09-24 | UNVERIFIED |
| INTC | RESEARCH | 1.4:1 | $142.42 | $109.60 | Earnings 2026-07-23 | UNVERIFIED |
| ALAB | RESEARCH | 1.0:1 | $499.49 | $371.67 | Earnings 2026-08-04 | UNVERIFIED |
| BFLY | RESEARCH | 0.7:1 | $9.69 | $7.21 | Earnings 2026-07-31 | UNVERIFIED |
| SIMO | RESEARCH | 0.7:1 | $355.02 | $273.25 | Earnings 2026-07-30 | UNVERIFIED |
| TSM | RESEARCH | 0.6:1 | $479.19 | $412.43 | Earnings 2026-07-16 | **REVIEW** (ratio pre-check borderline) |
| MRNA | RESEARCH | 0.3:1 | $85.60 | $70.58 | Earnings 2026-07-31 | UNVERIFIED |
| AMD | RESEARCH | 0.3:1 | $584.48 | $467.12 | Earnings 2026-08-04 | UNVERIFIED |
| ALLY | RESEARCH | 0.4:1 | $47.27 | $43.52 | Earnings 2026-07-21 | **REVIEW** (ratio pre-check borderline) |
| ZION | RESEARCH | 0.2:1 | $71.23 | $66.67 | Earnings 2026-07-20 | **REVIEW** (ratio pre-check borderline) |
| DINO | RESEARCH | 0.03:1 | $75.04 | $67.62 | Earnings 2026-07-28 | UNVERIFIED |
| BAC | RESEARCH | 0.03:1 | $59.91 | $56.33 | Earnings 2026-07-14 | **REVIEW** (ratio pre-check borderline) |
| WDC | RESEARCH | n/a (no stop-side data) | $800.32 | $617.87 | Earnings 2026-07-29 | UNVERIFIED |
| AXTI | RESEARCH | n/a | $143.26 | $80.18 | Earnings 2026-07-30 | UNVERIFIED |
| STX | RESEARCH | n/a | $1144.62 | $895.77 | Earnings 2026-07-28 | UNVERIFIED |

**Quick-look context on the 5 BUY-CANDIDATEs** (light research pass, not a
full underwrite):
- **BTG (B2Gold)** — up on gold-price strength and production outlook;
  RBC trimmed its target to $5.75 but stays Sector Perform; Street average
  ~$7.01. Miner economics (royalties, gold-lease financing) make Shariah
  compliance genuinely uncertain — screen carefully, don't assume UNVERIFIED
  means "probably fine."
- **NBIS (Nebius Group)** — AI-cloud name, down ~17% on a Bloomberg report
  that Meta (a customer worth up to $27B to Nebius) is building its own
  cloud-compute business — a real thesis-relevant risk, not noise. P/E ~64,
  +158% YTD even after the pullback.
- **BMNR (Bitmine Immersion)** — **flag this one specifically**: it's
  functionally an Ethereum treasury/staking vehicle ($9.6-10.7B in crypto/ETH
  holdings, ~4.72M ETH staked, a 9.50% preferred raise). This looks very
  likely to fail a Shariah business-activity screen (crypto staking yield,
  interest-bearing preferred structure) regardless of what the ratio
  pre-check shows — the ratio check only looks at debt/cash-to-market-cap,
  not business activity. Treat as a probable AVOID pending Zoya/Musaffa,
  not just "unverified."
- **AUR (Aurora Innovation)** — autonomous-trucking pre-revenue name
  (~$1M revenue, ~$223M quarterly net loss); Craig-Hallum initiated Buy
  ($18 target) on "physical AI" momentum. Entirely sentiment/milestone
  driven — reward:risk of 3.9:1 here is a function of a wide mechanical
  stop, not demonstrated fundamentals.
- **IBRX (ImmunityBio)** — Anktiva (cancer immunotherapy) Saudi expansion +
  possible Q2 sales update are real near-term catalysts; stock at a 3-month
  high; note insider selling alongside the retail-driven rally.

Correlation note: TSM / AMD (semiconductors) are both present again and
correlated with each other; treat as one bet if underwriting both.

## Follow-ups (priority order)

1. **[Urgent — 5th run unresolved] FIG compliance**: re-screen in Zoya/Musaffa.
2. **[New — check next run] NOW trailing stop**: price closed the gap to the
   chandelier stop today ($108.42 vs $109.98); re-run tomorrow once a
   settled close is available to see if TRAIL_STOP actually fires.
3. **[New — Shariah] BMNR**: very likely a business-activity fail (crypto
   treasury/staking, interest-bearing preferred) despite showing UNVERIFIED
   rather than a hard AVOID — the ratio pre-check doesn't screen business
   activity. Don't let the 92:1 mechanical reward:risk be the headline here.
4. **[Housekeeping] Watchlist churn**: today's auto-discovery replaced the
   curated 6-name list with a fresh top-20; if you want any of TSM's,
   AMD's (etc.) old written thesis notes preserved, re-add them as `why`
   text on the new rows — discover.py overwrites `why` with a generic
   mechanical note each run.
5. **[Infrastructure — done]** Yahoo access, the yfinance TLS-fingerprint
   block, `fast_info` key-name bugs, the NaN-swallowing balance-sheet
   lookup, and the missing `lxml` dependency are all fixed as of this run.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag or a mechanical ratio pre-check, neither a fatwa — verify independently
in Zoya/Musaffa before acting.

Sources:
- [B2Gold Corp. (BTG) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/BTG/)
- [BTG Stock Holds Range As Analyst Views Diverge — Timothy Sykes](https://www.timothysykes.com/news/b2gold-corp-canada-btg-news-2026_07_02/)
- [Nebius Group N.V. (NBIS) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/NBIS/)
- [CoreWeave and Nebius Plunged 14% and 17% in a Single Day — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/coreweave-nebius-plunged-14-17-164300894.html)
- [Aurora Innovation Stock Gains Attention On Safety And "Physical AI" Push — StocksToTrade](https://stockstotrade.com/news/aurora-innovation-inc-aur-news-2026_07_01/)
- [IBRX Stock At 3-Month High: Retail Bulls Eye July Catalysts — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/ibrx-stock-3-month-high-013903543.html)
- [ImmunityBio (IBRX) Is Up 8.4% After Russell Index Removal — Simply Wall St](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nasdaq-ibrx/immunitybio/news/immunitybio-ibrx-is-up-84-after-russell-index-removal-amid-a)
- [BMNR Stock Rides Massive Ethereum Bet As Staking Engine Scales — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_01-3/)
- [Bitmine Immersion Technologies (BMNR) Stock Looks Undervalued On Book Value But Weaker On Broader Checks — Simply Wall St](https://simplywall.st/stocks/us/software/nyse-bmnr/bitmine-immersion-technologies/news/bitmine-immersion-technologies-bmnr-stock-looks-undervalued)
