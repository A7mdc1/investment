# Portfolio Assessment — 2026-11-10

Not financial advice. This is decision support only. Every buy, sell or hold
call is yours. The Shariah status below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, and neither is a
fatwa. Verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

All of these ran on live Yahoo data: `prices.py`, `shariah.py`, `dcf.py`,
`signals.py`, `verdict.py` and `recommend.py`, then `discover.py` and
`scaffold.py --all-leads` (see the Discovery section for how that went).
`journal.py` was not run because there is still no `transactions.csv`, so the
discipline guard is still dormant.

**Since the last report (2026-08-19):** there are no new trades in the
holdings files. The book is still BMNR plus NOW. The big event was **NOW's
Q3 FY2026 print on 2026-10-28/29**, which took the stock down about 27% in
one session.

## Verdicts (lead with this)

These are your own rules in `rules.md` resolving mechanically. They are not
advice.

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50).
Live price is **$99.29**, which is **-13.6%** against the $114.97 cost basis.
Last report it was +11.8%.

| PM-grade record (recommend.py, live; mechanical proxies) | |
|---|---|
| Conviction | LOW: no reward:risk or stated variant view on file, so the engine cannot self-assess |
| Shariah (recorded) | **REVIEW**: broker_app compliant, but screened 2026-06-09, which is over 100 days old, so it needs a re-screen |
| Shariah (ratio pre-check, this run) | Clean: debt 2.3%, liquid 6.1%, business OK |
| DCF intrinsic value | $119.65 vs $99.29 -> +20.5% (assumes 18% 5-year growth; see DCF caveat) |
| Trailing stop (chandelier, 3x ATR22) | **$137.00, which sits about 28% ABOVE the current price**. The stop has been gapped through (see Flag #1) |
| 6m momentum (skip last month) | +57.7%. This is stale: the skip-month window excludes the post-earnings crash |
| ATR% | 7.55%, above vol_throttle 6%, so the rules say to size down |
| Would buy today? | The engine says yes mechanically. It reads the recorded Shariah field and VALUATION_RICH says "do not add", so treat this as noise |
| What changes the verdict | `thesis_broken: true`, or the Shariah re-screen flipping |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Live price is **$17.49**,
which is **+13.3%** against the $15.43 cost basis. Last report it was +33.1%,
and it peaked around $27.5 in late September.

| PM-grade record (recommend.py, live; mechanical proxies) | |
|---|---|
| Conviction | LOW: the holding file has no thesis, stop, target or pre-mortem |
| Shariah (recorded) | **REVIEW**: broker_app compliant, screened 2026-07-07, which is now over 100 days old and stale |
| Shariah (ratio pre-check, this run) | **FAIL**, again: industry `Capital Markets`, so the core business fails the screen. Unresolved since August |
| DCF intrinsic value | $0.72 vs $17.49 (-95.9%). This is not meaningful because the DCF model doesn't fit an ETH-treasury company |
| Trailing stop (chandelier) | **$20.00, about 14% above the current price**. Price has broken it |
| 6m momentum (skip last month) | +10.0% |
| ATR% | 8.65%, above vol_throttle 6%, so the rules say to size down |
| What changes the verdict | A Zoya/Musaffa business-activity re-screen in either direction |

- Portfolio note: there are only 2 holdings, so concentration rules stay muted until there are at least 4 names.
- `portfolio_notes`: **BMNR ATR 8.65%, NOW ATR 7.55%. Both say to size down per the vol throttle.**

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.49 | 10 | $15.43 | $174.85 | +13.3% | 20.1% |
| NOW | $99.29 | 7 | $114.97 | $695.04 | -13.6% | 79.9% |

**Total value: $869.89**. Cost: $959.09. **Total return: -9.3%** (-$89.20
unrealised). At the last report it was +$146.42, so that is a swing of about
-$236 since 2026-08-19.

## Action flags (priority order)

1. **[Price / NOW, NEW] Post-earnings collapse, with the position now under
   water.** On 2026-10-29 NOW fell **about 27%**, which CNBC called the worst
   day in the company's history. Revenue was in line ($4.107B vs $4.095B
   expected) and adjusted EPS of $1.00 missed the $1.02 estimate by $0.02.
   The guidance did the damage: Q4 cRPO growth was guided to **18.5% cc vs
   about 19.8% expected**. Management blamed timing, saying early renewals
   pulled deals from Q4 into Q3. Reported operating margin fell to 9.4% from
   16.8% a year earlier. On the positive side, the AI contract target was
   raised to at least $1.7B. The company has since announced further layoffs.
   The stock has kept drifting from $109.67 at the earnings-day close to
   $99.29 today.
   [Trefis](https://www.trefis.com/stock/now/articles2/621573/what-is-behind-the-move-in-servicenow-stock/2026-10-30) ·
   [MarketBeat](https://www.marketbeat.com/instant-alerts/price-servicenow-nyse-now-shares-down-268-after-earnings-miss-2026-10-29/) ·
   [INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook) ·
   [Salesforce Ben](https://www.salesforceben.com/servicenow-lays-off-more-staff-after-q3-earnings-fail-to-impress-wall-street/)
   - **Your own thesis tripwire is close.** The holding file's "What would
     change my mind" reads: *"Subscription growth decelerating meaningfully
     below current ~21-22% YoY, or a guidance cut tied to AI-agent or Armis
     traction."* A cRPO guide of 18.5% is a deceleration below that band.
     Whether it is "meaningful", and whether it is timing or trend, is your
     call. The engine can't make it, and nothing will fire until you set
     `thesis_broken: true` or `invalidation_hit: true`.
   - **The verdict engine is structurally blind here.** `trade_type: core`
     exempts NOW from TRAIL_STOP. DRAWDOWN_REVIEW needs a 20% loss against
     cost and NOW is at -13.6%. The 6m-momentum figure (+57.7%) skips the
     last month, which is exactly the month of the crash. So VALUATION_RICH
     -> HOLD is the only rule that fires, and that verdict reflects how the
     rules are set up, not a judgement on the fresh information.
   - **Concentration:** 79.9% of the book sits in a single name. The
     concentration rules are muted because the book has fewer than 4 names.
2. **[Mandate] Both Shariah screens are now stale (more than 100 days).**
   recommend.py sets `shariah_status: REVIEW` on both. Re-screen both in
   Zoya/Musaffa.
3. **[Mandate / BMNR, carried over from 2026-08-19, still unresolved] The
   business-activity pre-check FAILS** (`Capital Markets`). The holding file
   still records `compliant`, its thesis is still the placeholder "NEW
   position — screen compliance in Zoya/Musaffa before adding more", and
   none of the PM fields have been filled in. COMPLIANCE_GATE only reads the
   recorded field, so it stays silent. The re-screen above is the moment to
   settle the business-activity question specifically.
4. **[Price / BMNR] Trend broken.** BMNR is down about 37% from its
   late-September high (about $27.5 to $17.49). It is below its chandelier
   stop ($20.00) and below EMA20 ($20.96). TRAIL_STOP is exempt because of
   `trade_type: core`. The **next earnings date is about 2026-11-23** (per
   Earnings Whispers), which is inside the holding window, and the file has
   no gap plan.
   [Earnings Whispers](https://beta.earningswhispers.com/go/w/BMNR)
5. **[Vol throttle] Both names are above 6% ATR.** That is a de-risk note
   under your rules. It is not a sell signal.

## Per-holding read

### NOW — ServiceNow, Inc
**Case to keep:** Revenue was in line, and management describes the cRPO
shortfall as timing (renewals pulled into Q3), which is a claim that can be
checked next quarter. The AI contract target was raised to at least $1.7B,
up from the $1B milestone noted last report. The ratio pre-check is clean
(debt 2.3%). At $99, the stock sits about 17% below the DCF value in your
own file ($119.65 at 18% growth), whereas in August it traded at a premium
to that value. The recorded P/E of ~119 is from June and is stale. The
trailing multiple has compressed with the price.

**Case to cut or trim:** Guidance has decelerated below the growth band your
own invalidation text names. Operating margin roughly halved year on year,
and there have been further layoffs after the print. Price is about 28% below
the volatility stop and still falling a week and a half after earnings, with
no bounce. The name is 80% of the book. With no `initial_stop` on file,
there is no pre-committed exit level at all.

Both cases rest on facts. Which one wins depends on whether you read Q4 cRPO
as timing or trend, and that is your edge to supply. Updating
`variant_view`, `invalidation` and `last_review` (now 148 days old, against a
90-day cadence) in `holdings/now-servicenow.md` is the concrete
re-underwrite.

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep:** It is still +13% against cost. It is an ETH-treasury
vehicle, so its price is largely an ETH-beta call. Earnings around 2026-11-23
are a near-term catalyst.

**Case to flag:** The compliance question is unresolved for a second
straight cycle, the recorded screen is now stale too, the trend is broken
(below the chandelier and EMA20), and there is no thesis or stop on file. The
same pattern took 7 runs to close on FIG.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add. The P/E input is the
  stale June value.
- **TRAIL_STOP -> NOW / BMNR**: price is below the chandelier level on
  **both**, but the rule does **not** fire because `trade_type: core` exempts
  them. If either was really a swing position, this rule would have said
  SELL.
- **DRAWDOWN_REVIEW (20%)**: not firing. NOW is at -13.6% against cost.
- **COMPLIANCE_GATE**: silent, because it reads the recorded `compliant`.
  recommend.py separately flags both as stale (REVIEW).
- **VOL_THROTTLE fired -> BMNR, NOW**: size down per the throttle note.
- **Review cadence (90 days)**: overdue for NOW (last_review 2026-06-15). BMNR
  has never been reviewed.

*If you execute anything from this report, run `/apply-trade` so the
holdings files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $99.29 | +20.5% | growth_5y 18%, terminal 3%, discount 10%. 18% is now roughly the guided cRPO growth, so there is little cushion if growth decelerates further |
| BMNR | $0.72 | $17.49 | -95.9% (not meaningful) | default 5% growth. The model does not fit an ETH-treasury business |

## New ideas (watchlist.md)

`watchlist.md` is still **empty**, so there are no hand-curated names to
research. `recommend.py`'s `ideas` array returned **0 BUY-CANDIDATEs**. That
is expected, because no card in `setups/` has been flipped to
`status: planned`.

## Discovery & draft setups

`discover.py` ran on live data. The pool was 160 names. **SPUS ETF holdings
failed with HTTP 401**, so the pool came from the two yfinance screens only.
68 names were dropped by the Shariah ratio flag and 3 by the liquidity floor,
leaving **50 leads: 3 at LEAD tier and 47 capped at RESEARCH**. Most of the
47 fail the catalyst-horizon gate: their next earnings dates fall in
Jan–Mar 2027, outside the 60-day window. `scaffold.py --all-leads` wrote
**26 new DRAFT cards** and left the 24 existing cards unchanged. Every card
is unreviewed and Shariah UNVERIFIED. They are proposals to review, never
buys.

| Ticker | Verdict | Card | R:R | Entry / target / stop (formula) | Catalyst |
|---|---|---|---|---|---|
| AVGO | LEAD | existing | 15.0:1 | ~325.56 / 476.03 / 315.55 | earnings 2026-12-09 (29d) |
| ADI | LEAD | existing | 4.8:1 | ~389.43 / 444.55 / 377.92 | earnings 2026-11-24 (14d) |
| DLO | LEAD | existing | 3.1:1 | ~14.18 / 16.14 / 13.54 | earnings 2026-11-12 (2d) |

Every level above is a formula output. AVGO's 15:1 comes from a stop only
about 3% below entry against a 46% target, and that is a formula artifact,
not an honest asymmetry. Every lead with earnings in the window needs an
`earnings_plan` (gap plan) before it could ever clear.

New DRAFT cards: ACGL, AEM, ALL, ANET, ASND, BBY, BF-B, DIOD, EVR, FTI,
HST, KEYS, LSCC, NTAP, NTNX, PNFP, PSX, SMTC, SNA, STLD, TECK, TRV, TS, TXN,
UI, VLO.

**Business-activity flags.** These passed the ratio pre-check, but their core
business is very likely to fail a real screen. Don't spend review time on
them before Zoya/Musaffa:
- **BF-B** (Brown-Forman: alcohol). Clear knockout.
- **ACGL, ALL, TRV** (conventional insurance), **PNFP** (bank) and **EVR**
  (investment bank). These are conventional finance.
- **HST** (hotel REIT). Hotel revenue typically includes alcohol, and the
  REIT carries debt.
- **PLTR** (carried over), with its open defense question, and the
  precious-metals cluster (**CDE, AGI, KGC, AU, AEM**), with its open
  streaming/royalty-financing question.

This shows the ratio pre-check misses business-activity knockouts that
yfinance doesn't tag as `Capital Markets`, the same gap seen with BMNR.

## Follow-ups (priority order)

1. **[Urgent] NOW re-underwrite.** Decide whether the Q4 cRPO guide of
   18.5% trips your own "What would change my mind" line. Set `initial_stop`,
   `invalidation`, `variant_view` and `last_review` in
   `holdings/now-servicenow.md`. As things stand, no rule in the engine can
   fire on this position below a 20% loss against cost, and that position is
   80% of the book.
2. **[Mandate] Re-screen BMNR and NOW in Zoya/Musaffa.** Both screens are now
   stale. For BMNR, settle the business-activity question specifically. It
   is unresolved for a second cycle.
3. **[Time-boxed] BMNR earnings around 2026-11-23.** The position is below
   its chandelier stop and has no stop, thesis or gap plan on file.
4. **[Infrastructure] SPUS holdings fetch returned 401**, so the halal-ETF
   base pool was missing this run. Worth checking whether yfinance's
   ETF-holdings endpoint needs a fix in `discover.py`.
5. **[Housekeeping] 26 new DRAFT cards** were added this run, and none are
   `planned`. Skip the business-activity flags above.
6. **[Infrastructure, still open] There is no ledger yet.** Log trades via
   `/apply-trade` to unlock the discipline guard.

---

*Not financial advice. Verdicts are your own rules resolving mechanically.
Verify all Shariah status in Zoya/Musaffa. Sources: Trefis, MarketBeat,
INDmoney, Salesforce Ben and Earnings Whispers, as linked above.*
