# Portfolio Assessment — 2026-11-23

Not financial advice. This is decision support only. Every buy, sell and hold
call is yours. The Shariah status shown below is either the broker app's
recorded screen or a mechanical ratio/business-activity pre-check. Neither is a
fatwa. Verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

- **Pipeline:** `discover.py`, then `scaffold.py --all-leads`, then `prices.py`,
  `shariah.py`, `dcf.py`, `signals.py`, `verdict.py` and `recommend.py`. All ran
  on live Yahoo data.
- **Rate limiting:** Yahoo heavily rate-limited the run (several hundred
  401/429 responses). The SPUS halal-ETF holdings fetch failed, so the
  discovery pool came only from the yfinance screens (170 names).
- **No ledger:** `journal.py` was not run because `transactions.csv` still
  doesn't exist.

**Pipeline bug found and fixed this run.** The first discovery pass let five
names with clearly non-compliant core businesses into `leads.md` marked
"ratio pre-check clean":

| Ticker | Business | Tier it reached |
|---|---|---|
| BF-B | distiller | LEAD |
| TRV | insurer | LEAD |
| ALL | insurer | RESEARCH |
| ACGL | insurer | RESEARCH |
| EVR | investment bank | RESEARCH |

- **Cause:** `shariah.ratio_precheck()` returned `ok: True` when clean
  debt/cash ratios combined with a business check that came back *unknown*. The
  business check is unknown whenever the sector/industry lookup is rate-limited.
- **Fix:** an unknown business screen now makes the whole pre-check unknown
  (`ok: None`), never a pass. A regression test was added in
  `tests/test_fixes.py`, and both offline test suites pass.
- **Clean-up:** discovery and scaffold were re-run. None of the five names
  appear in the final `leads.md`, and their five DRAFT cards (all created this
  run) were deleted.
- **Gap that remains:** a lead whose business screen is unknown can still reach
  LEAD tier. It is now labelled "pre-check unavailable" instead of "clean". No
  final lead carries that label this run.

## Verdicts (lead with this)

These are YOUR rules resolving mechanically, not advice.

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50).

- **Price and return:** live price **$92.44**, **-19.6%** vs the $114.97 cost
  basis.
- **Drawdown rule:** DRAWDOWN_REVIEW (threshold 20%) misses by about 0.4 pt, so
  it did not fire. `signals.py` rounds the move and *does* flag "Down -20% vs
  cost — revisit whether the thesis still holds."
- **Chandelier stop:** the trailing stop is **$139.52**, so the price is about
  34% *below* it. Your rules don't act on this because the position is
  `trade_type: core`, which exempts it from the trailing-stop rule.
- **Momentum:** 6m momentum (skip last month) is +59.1%. It doesn't yet reflect
  the November collapse.
- **Position:** 7th percentile of the 52-week range.

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW: missing reward:risk or a stated thesis edge |
| Shariah | **REVIEW: recorded compliant, but the screen (2026-06-09) is >100 days old** |
| DCF intrinsic value | $119.65 vs $92.44, so +29.5% (assumptions below) |
| Would buy today? | Mechanically yes, but that check can't see the stale screen or the missing thesis fields |
| What changes verdict | `thesis_broken: true`, a SELL trigger, or the Shariah screen flipping |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired).

- **Price and return:** live price **$14.81**, **-4.0%** vs the $15.43 cost.
  It was +33% at the last report.
- **Chandelier stop:** the trailing stop is $18.61, so the price is about 20%
  below it. The `core` exemption applies here too.
- **Momentum:** 6m momentum is +16.7%.

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW: no thesis, stop, target or pre-mortem recorded |
| Shariah (recorded) | **REVIEW: compliant per broker app 2026-07-07, now >100 days old, so stale** |
| Shariah (mechanical pre-check) | **FAIL, second run in a row:** industry `Capital Markets` |
| DCF intrinsic value | -$6.53 (not meaningful: a DCF does not model an ETH-treasury company) |
| Would buy today? | recommend.py says yes, but it reads only the recorded field. See Action Flag #1 |

`verdict.py` portfolio notes:
- Vol throttle: BMNR ATR is 9.95% and NOW ATR is 7.21%. Both are flagged as
  "size down per vol throttle".
- Concentration rules are muted because the portfolio has only 2 holdings.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $14.81 | 10 | $15.43 | $148.10 | -4.0% | 18.6% |
| NOW | $92.44 | 7 | $114.97 | $647.11 | -19.6% | 81.4% |

**Total value: $795.22** | Cost: $959.09 | **Total return: about -17.1%**
(-$163.87 unrealised). On 2026-08-19 it was +15.3% (+$146.42).

## Action flags (priority order)

1. **[Mandate] BMNR Shariah is now both stale and mechanically FAILING.**
   - **Staleness:** the recorded "compliant" screen (2026-07-07) is past the
     100-day freshness window.
   - **Business check:** for the second consecutive run, the business-activity
     check classifies BMNR as `Capital Markets`. The company's own reporting
     describes it as an ETH treasury vehicle. Most of its revenue is staking
     yield on ~6.09M ETH (about 5.23M staked, about $245M projected annualized
     staking revenue). It reported a $6.31B FY net loss driven by fair-value
     marks on ETH.
   - **What your rules say:** Gate 1 treats a confirmed business-activity fail
     as an absolute SELL. COMPLIANCE_GATE only reads the recorded field, so it
     will stay silent until you re-screen in Zoya/Musaffa and record the
     result.
2. **[Mandate] NOW Shariah screen is stale.** It was screened 2026-06-09 (167
   days ago). The ratio pre-check is still clean: debt 2.5% and liquid assets
   6.5% of market cap, business OK. This is housekeeping, but under your gates
   a stale screen is REVIEW.
3. **[Drawdown / NOW] -19.6% vs cost, 0.4 pt from DRAWDOWN_REVIEW.**
   - **What happened:** NOW fell from about $154.60 to $105.12 the day after
     its fiscal Q3 2026 results in late October. It then slid further in a
     sector-wide software selloff: -6.5% on Nov 17, when Salesforce fell 9.5%
     and Atlassian 6.0%. Commentary blames fears that AI erodes seat-based
     software pricing.
   - **No company news:** no company-specific filing was tied to the Nov 17
     move.
   - **Review overdue:** the holding's `last_review` is 2026-06-15, which is
     past your 90-day `review_cadence_days`. `verdict.py` does not enforce that
     rule mechanically.
4. **[Valuation / NOW]** VALUATION_RICH still fires on the recorded P/E of
   ~119. That P/E is a stale front-matter value set at a much higher price.
   The live DCF now shows +29.5% to intrinsic value, so the two valuation
   signals point in opposite directions. Refresh `pe` and `last_price` in the
   holding file.
5. **[Price vs trailing stop] Both holdings trade well below their chandelier
   stops** (NOW about 34% below, BMNR about 20% below). Your `core` designation
   exempts both. Whether "core" is still the right label for a 10-share ETH
   treasury stock is your call.
6. **[Discovery]** 50 leads; 3 at LEAD tier, 47 RESEARCH. See below.

## Per-holding read

### NOW — ServiceNow, Inc
**Case to keep:**
- The recorded thesis (durable enterprise-workflow subscription growth, with AI
  agents as the forward driver) has not been formally broken by anything in the
  files.
- The November decline looks largely sector-wide (software multiple
  compression) rather than company-specific.
- The live DCF (18% 5-yr growth, 10% discount) puts intrinsic value about 29%
  above the price.

**Case to trim or exit:**
- The stock lost roughly a third of its value from the post-Q3 level in about
  four weeks.
- The market reaction to Q3 itself was severe (about -32% the next day).
- The AI-disruption-of-seats narrative goes directly at a seat-priced business.
- The position is 81% of the book with no `initial_stop`, `invalidation` or
  `pre_mortem` recorded, so there is no pre-committed level to check against.
- Both technical exit signals (chandelier and the near-miss drawdown) are
  firing or close to it.

Sources: [24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/) ·
[GuruFocus](https://www.gurufocus.com/news/9205950/servicenow-now-shares-drop-65-amid-market-selloff-trading-well-below-gf-value) ·
[Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/63358717/servicenow-stock-drops-7-as-software-sell-off-deepens) ·
[Trefis (promotional source, treat with caution)](https://www.trefis.com/stock/now/articles/626283/what-is-driving-servicenow-stock/2026-11-18)

Next earnings: not confirmed this run. Historically it falls in late January.
Add the date to the holding's `catalyst.date` once ServiceNow IR posts it.

### BMNR — Bitmine Immersion Technologies
**Case to keep:**
- It keeps accumulating ETH: 6.09M ETH after buying 7,819 this past week.
- It is staking about 86% of its holdings.
- The stock jumped 17% on Nov 23 as crypto stabilized.

**Case to exit or flag:**
- The compliance question in Flag #1 comes first, independent of price.
- Fundamentally, the stock is a leveraged proxy on ETH. ETH slid toward $1.6K
  around Nov 20, and the stock sits about 47% below its September peak near
  $29.
- The holding file still has no thesis, stop, target or pre-mortem, four
  months after entry.

Sources: [The Block](https://theblock.co/news/business/2026-11-23-bitmine-adds-7819-eth-tom-lee-makes-hard-money-case-444948) ·
[Benzinga](https://www.benzinga.com/crypto/cryptocurrency/26/11/63538880/bitmine-buys-7819-ethereum-as-bmnr-surges-17-whats-going-on) ·
[FX Leaders](https://www.fxleaders.com/news/2026/11/20/bitmine-bmnr-drops-8-6-to-13-7-as-eth-slides-to-1-6k/) ·
[GuruFocus](https://www.gurufocus.com/news/9215049/bitmine-immersion-bmnr-reports-111b-in-total-assets-including-609m-ethereum-holdings)

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired, NOW:** HOLD, do not add. Note that it rests on a
  stale P/E field.
- **DRAWDOWN_REVIEW did not fire, NOW:** the drawdown is -19.6% against a 20%
  threshold, about 0.4 pt short.
- **COMPLIANCE_GATE did not fire:** both recorded statuses are still
  `compliant`. Both are stale, and BMNR fails the mechanical business check.
  The rule cannot fire until you record a re-screen.
- **TRAIL_STOP did not fire for either holding:** both are exempt as `core`,
  even though both trade below their chandelier levels.
- **Review cadence (90 days):** overdue for NOW (last 2026-06-15). BMNR has
  never been reviewed.
- **VOL_THROTTLE:** notes surfaced for both names (ATR 9.95% / 7.21%).

*If you execute anything from this report, run `/apply-trade` so the holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $92.38 | +29.5% | growth_5y 18%, terminal 3%, discount 10% |
| BMNR | -$6.53 | $14.81 | n/m | growth_5y 5% (default), terminal 2.5%, discount 10%. A cash-flow model doesn't fit an ETH treasury, so treat this as a data gap |

## New ideas (watchlist.md)

`watchlist.md` is still empty, so there was nothing hand-curated to research.
`recommend.py` returned 0 ideas and **0 BUY-CANDIDATEs**. No setup card in
`setups/` has `status: planned`; all 91 are `draft`.

## Draft & planned setups — 50 leads, 28 new DRAFT cards

After the fix, discovery wrote **`leads.md`** with the top 50 names:
- **3 LEAD-tier leads** (listed below).
- **47 RESEARCH leads**, capped by the asymmetry gate (3:1) or the 60-day
  catalyst-horizon gate. Most of the pool's next earnings fall in late Jan or
  Feb 2027, outside the window.

| Ticker | Verdict | R:R (discovery estimate) | Catalyst | Days out |
|---|---|---|---|---|
| AVGO | LEAD | 18.3:1 | earnings 2026-12-09 | 16 |
| SNX | LEAD | 11.8:1 | earnings 2027-01-07 | 45 |
| ADI | LEAD | 5.7:1 | earnings 2026-11-24 | 1 (tomorrow) |

**All three LEAD-tier cards are STALE drafts.** The scaffold never overwrites an
existing card, so it did not refresh them:

| Card | Scaffolded | What's stale on it |
|---|---|---|
| AVGO | 2026-08-19 | Entry $364.41 and catalyst "2026-09-02 earnings" are both past. It has no target because its stop sits above its entry, so it can't be approved as-is |
| SNX | 2026-08-19 | Entry $252.66 and catalyst 2026-09-24 are both past. Discovery's current estimate is entry ~$232, target ~$298, stop ~$228 |
| ADI | 2026-07-07 | Catalyst 2026-08-19 is past, and the card's R is $2.35 on a $389 stock |

To get a fresh formula plan for any of these, run
`python scripts/scaffold.py --force <TICKER>`.

`RESEARCH — DRAFT awaiting your review (set status: planned to approve)`
applies to every card. Every level is a formula output. Every card is
`shariah: unverified` and is a proposal, not a buy.

New DRAFT cards this run (28):
- **Semis and hardware:** AAPL, ANET, COHR, DIOD, FN, JBL, KEYS, KLAC, LSCC,
  NTAP, NTNX, PENG, SANM, SMTC, TXN, UI, VIAV.
- **Energy:** APA, PR, PSX, VLO, XOM. The PSX and VLO refiners are worth a
  check of their revenue breakdown in Zoya/Musaffa.
- **Other:** ASND, BBY, FRO, HSY, LLY, SNA.

**Flags before spending review time:**
- **PLTR:** carries over again with its unresolved government/defense
  business-activity question.
- **FOX:** media/broadcast. Its revenue mix needs a real business screen.
- **The five purged names** (BF-B, TRV, ALL, ACGL, EVR): any earlier run under
  rate-limiting may have had the same leak. Older cards in `setups/` were not
  re-audited this run.

## Follow-ups (priority order)

1. **[Urgent] Re-screen BMNR in Zoya/Musaffa** on the business-activity
   question. It is stale and mechanically failing two runs running. Record the
   result in `holdings/bmnr.md`.
2. **[Urgent] Re-screen NOW.** The screen is 167 days old.
3. **[Decision] NOW re-underwrite.** It is at -19.6%, review is overdue, and
   there is no stop or invalidation on 81% of the book. Fill in `initial_stop`,
   `invalidation` and `pre_mortem`, and refresh the stale `pe` and
   `last_price`.
4. **[Housekeeping] BMNR holding file:** add the thesis and PM fields, or
   reconsider the `core` label.
5. **[Housekeeping]** Refresh the stale AVGO, SNX and ADI cards with `--force`
   if you want to review those leads.
6. **[Infrastructure — still open]** No `transactions.csv`. Log the FIG sale and
   BMNR buy via `/apply-trade` to unlock the discipline guard.
7. **[Environment note for future runs]** In this sandbox, `python` is 3.11
   without the dependencies installed. The scripts were run with `python3.13`.

---

Not a financial advisor. The Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa. Verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Just Dropped 30% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [ServiceNow Shares Drop 6.5% Amid Market Selloff — GuruFocus](https://www.gurufocus.com/news/9205950/servicenow-now-shares-drop-65-amid-market-selloff-trading-well-below-gf-value)
- [ServiceNow Stock Drops 7% As Software Sell-Off Deepens — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/63358717/servicenow-stock-drops-7-as-software-sell-off-deepens)
- [ServiceNow Stock Drops Amid Anthropic's New AI Tools — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/11/63116691/servicenow-stock-drops-amid-anthropics-new-ai-tools)
- [What Is Driving ServiceNow Stock? — Trefis](https://www.trefis.com/stock/now/articles/626283/what-is-driving-servicenow-stock/2026-11-18)
- [Bitmine adds 7,819 ETH — The Block](https://theblock.co/news/business/2026-11-23-bitmine-adds-7819-eth-tom-lee-makes-hard-money-case-444948)
- [Bitmine Buys 7,819 Ethereum as BMNR Surges 17% — Benzinga](https://www.benzinga.com/crypto/cryptocurrency/26/11/63538880/bitmine-buys-7819-ethereum-as-bmnr-surges-17-whats-going-on)
- [Bitmine (BMNR) Drops 8.6% as ETH Slides to $1.6K — FX Leaders](https://www.fxleaders.com/news/2026/11/20/bitmine-bmnr-drops-8-6-to-13-7-as-eth-slides-to-1-6k/)
- [BitMine Reports $11.1B in Total Assets — GuruFocus](https://www.gurufocus.com/news/9215049/bitmine-immersion-bmnr-reports-111b-in-total-assets-including-609m-ethereum-holdings)
