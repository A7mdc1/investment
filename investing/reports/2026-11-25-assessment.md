# Portfolio Assessment — 2026-11-25

Not financial advice. This is decision support only. Every buy/sell/hold call
is yours. The Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, and neither is a
fatwa. Verify in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo, 168-name raw pool, 4 dropped on liquidity, 77
dropped on the Shariah ratio pre-check, top 50 kept). Then
`scaffold.py --all-leads` (26 new DRAFT cards, 24 existing cards left
unchanged). Then `prices.py`, `shariah.py`, `dcf.py`, `signals.py`,
`verdict.py` and `recommend.py`, all live.

**Data caveat:** Yahoo rate-limited the session (HTTP 429 on the crumb fetch).
Holding prices came through fine. However, **35 of the 50 leads came back with
reward:risk = n/a** because their technicals didn't load. As a result, **0
leads cleared to LEAD tier**, compared with 9 last run. That is a data gap,
not a signal about the market. Re-run `/discover` locally to get a full read.

`journal.py` was not run because there is still no `transactions.csv`.

**Since the last report (2026-08-19):** this is the first run in ~14 weeks.
No trades are recorded in `holdings/`. Both positions have swung from gains
to losses of about 19–21%.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically. They are not advice.

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW, down -20.8% vs cost; VALUATION_RICH
also active). Live price **$91.08** vs the $114.97 cost basis.

| PM-grade record (recommend.py — mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW: no reward:risk or variant view recorded, so it can't self-assess |
| Shariah (recorded) | **REVIEW**: broker_app compliant, screened 2026-06-09, **now STALE (>100 days)** |
| Shariah (ratio pre-check) | Clean (debt 2.5%, liquid 6.6%, business OK) |
| DCF intrinsic value | $119.65 vs $91.08 → +31.3% (model assumes 18% 5y growth, see DCF) |
| Trailing stop (chandelier) | $137.39, **above** current price. It's stale relative to the collapse; `trade_type: core` exempts NOW from TRAIL_STOP |
| 6m momentum (skip last month) | +42.4% (this mechanical figure skips the most recent month, which is when the drop happened) |
| Price position | 6% of its 52-week range, near the lows |
| Would buy today? | **No** (recommend.py) |
| What changes the verdict | Your re-underwrite: set `thesis_broken`, or record a refreshed thesis/stop/target |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Live price **$12.57** vs the
$15.43 cost basis → **-18.5%**, just under the -20% drawdown trigger.

| PM-grade record (recommend.py — mechanical proxy) | |
|---|---|
| Conviction | LOW: the holding file has no thesis, stop, target or pre-mortem |
| Shariah (recorded) | **REVIEW**: broker_app compliant, screened 2026-07-07, **now STALE** |
| Shariah (ratio pre-check) | **FAIL**: industry `Capital Markets`, so the core business fails the screen (2nd consecutive run) |
| DCF intrinsic value | -$6.53, which is not meaningful because the DCF model doesn't fit a crypto-treasury company |
| Trailing stop (chandelier) | $17.89, and **price is ~30% below it**. `trade_type: core` exempts BMNR from TRAIL_STOP. If this were a swing position, it would have been stopped out |
| 6m momentum (skip last month) | +12.3% |
| Would buy today? | Mechanically "yes", but that check only reads the recorded Shariah field and misses both the stale screen and the pre-check fail |

**Portfolio notes:** There are only 2 holdings, so the concentration rules are muted.
VOL_THROTTLE notes: BMNR ATR 11.9% and NOW ATR 7.2%, so size down per the vol throttle.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $12.57 | 10 | $15.43 | $125.75 | -18.5% | 16.5% |
| NOW | $91.08 | 7 | $114.97 | $637.56 | -20.8% | 83.5% |

**Total value: $763.31** | Cost: $959.09 | **Total return: -20.4%** (-$195.78 unrealised).
The last report showed +$146.42 unrealised, so the swing since then is about -$342.

## Action flags (priority order)

1. **[Mandate] Both recorded Shariah screens are STALE.** NOW was screened
   2026-06-09 and BMNR 2026-07-07. Re-screen both in Zoya/Musaffa. This is a
   policy issue, independent of price.
2. **[Mandate, carried over] BMNR fails the business-activity pre-check**
   (`Capital Markets`) for the second run in a row. It is still unresolved and
   the recorded field still says `compliant`. Under Gate 1, a confirmed fail
   is a hard SELL regardless of P/L. BMNR still behaves like an ETH treasury
   vehicle: it reports ~5.23M staked ETH (about $9B at $1,713/ETH as of Nov 22)
   and declared a $0.01 dividend on Nov 25.
   [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm) ·
   [GuruFocus](https://www.gurufocus.com/news/9218715/bitmine-immersion-technologies-inc-bmnr-stock-down-86-but-still-overvalued-gf-score-49100)
3. **[Drawdown / NOW] DRAWDOWN_REVIEW fired at -20.8%.** It is 83.5% of the book.
4. **[Drawdown / BMNR] -18.5%, just short of the -20% trigger.** The stock is
   down ~51.5% YTD, and the Nov 24 close was $13.18 (-8.6% on the day). It
   tracks ETH.
5. **[Valuation / NOW]** The P/E ~119 in the holding file is a *recorded* value
   from June. At $91 the live multiple is likely much lower. Refresh `pe:` and
   `last_price:` in `holdings/now-servicenow.md`, or VALUATION_RICH will keep
   firing on stale data.

## Per-holding read

### NOW — ServiceNow
**What happened:** Q3 FY26 was reported on 2026-10-28. Subscription revenue
was $3.99B, up 21% YoY and above the top of guidance. However, adjusted EPS of
$1.00 missed the $1.02 consensus, ending a six-quarter beat streak, and Q4
cRPO guidance of 18.5% (constant currency) came in below the ~19.8% expected.
The stock had its worst day on record (~-27%). It then kept sliding into
November on AI-disruption worries, including competition from Anthropic's
workplace products, and a third 2026 layoff round was announced.
[SEC 8-K Q3](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm) ·
[Investing.com transcript](https://ng.investing.com/news/stock-market-news/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-2765235) ·
[Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/servicenow-now-stock-price-sinks-as-q3-results-expose-profit) ·
[FX Leaders](https://www.fxleaders.com/news/2026/11/10/now-stock-faces-the-last-support-on-anthropic-workplace-news-as-servicenow-shares-decline-following-third-quarter-earnings-report/) ·
[SalesforceBen](https://www.salesforceben.com/servicenow-lays-off-more-staff-after-q3-earnings-fail-to-impress-wall-street/)

**Case to keep:**
- Your recorded "what would change my mind" is *subscription growth
  decelerating meaningfully below ~21–22%*. Q3 printed 21%, so that test has
  **not** clearly tripped yet.
- The DCF shows +31% upside under the 18%-growth assumption.
- Some commentary frames the selloff as overdone.
  [Motley Fool](https://www.fool.com/investing/2026/11/01/why-the-27-crash-in-servicenows-stock-looks-like-a/)

**Case to trim/exit:**
- The forward indicator (cRPO guide 18.5%) points toward the deceleration
  your invalidation describes.
- The AI-disruption narrative goes straight at the "AI-agent expansion is the
  forward driver" thesis.
- At 83.5% of the book, the position is far above any risk-sized level.
- The holding file still has no stop, target, invalidation level or pre-mortem
  to anchor this decision.
  [24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)

**Next catalyst:** Q4 earnings, likely late January 2027 (not confirmed). That
is roughly 60+ days out.

### BMNR — Bitmine Immersion Technologies
**Case to keep:** It keeps accumulating and staking ETH, pays a token
dividend, and if ETH recovers it carries the upside.

**Case to exit:** The business-activity Shariah question is unresolved and the
recorded screen is now stale. The price is ~30% under its chandelier stop.
The holding file has no thesis at all ("NEW position — screen compliance…").
The value is driven by ETH (~$1,713) rather than operating cash flow.

The compliance re-screen comes before any price-based decision.

## Suggested actions (from YOUR rules, rules.md)

- **Rule DRAWDOWN_REVIEW fired → NOW.** Your pre-set action is REVIEW: re-underwrite
  "would I buy this here today?" and record the outcome (`last_review`, and
  `thesis_broken` if applicable).
- **Rule VALUATION_RICH fired → NOW.** Your pre-set action is HOLD, do not add.
  Note that it is reading a stale recorded P/E.
- **COMPLIANCE_GATE / stale-screen → NOW, BMNR.** recommend.py now marks both
  `shariah_status: REVIEW`, so re-screen both.
- **TRAIL_STOP:** It does not fire because both positions are `trade_type: core`
  and exempt. For reference, both prices sit *below* their chandelier levels.
- **VOL_THROTTLE:** It is active for both names (high ATR). Size any new
  risk down.

*If you execute anything from this report, run `/apply-trade` so the holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $91.08 | +31.3% | growth_5y 18%, terminal 3%, discount 10%. If growth slows toward the 18.5% cRPO guide, this holds; a sharper slowdown cuts it materially |
| BMNR | -$6.53 | $12.57 | n/m | The default 5%/2.5%/10% model doesn't fit an ETH-treasury business. Treat it as a data gap |

## New ideas

`watchlist.md` is still empty. recommend.py's `ideas` array returned 0
entries, which means 0 BUY-CANDIDATEs. That is expected, because every card in
`setups/` (89 of them) is still `draft`.

## Draft setups — 50 leads, 26 new DRAFT cards

`leads.md` was refreshed. **All 50 are RESEARCH tier this run**, for two
reasons: 35 have reward:risk = n/a because of the rate limiting, and most of
the rest have their next earnings date more than 60 days out, since we are
between earnings seasons. Every DRAFT level is a formula output, and every
card is Shariah **UNVERIFIED**. They are proposals to review and edit, not buys.

The leads with a computed R:R ≥ 3 that were blocked only by the catalyst
window:

| Ticker | R:R | Next earnings | Days | Card |
|---|---|---|---|---|
| COHR | 20.0:1 | 2027-02-03 | 70 | new |
| TSLA | 10.2:1 | 2027-01-27 | 63 | existing |
| UI | 9.7:1 | 2027-02-05 | 72 | new |
| NET | 8.6:1 | 2027-02-09 | 76 | existing |
| CF | 6.0:1 | 2027-02-17 | 84 | existing |
| RCL | 3.8:1 | 2027-01-26 | 62 | existing |
| FOX | 3.4:1 | 2027-02-04 | 71 | existing |
| HSY | 3.1:1 | 2027-02-04 | 71 | new |

The near-dated catalysts that are missing R:R data (worth re-running locally)
are NTAP and CRDO (12-01), AVGO (12-09), CIEN (12-10), JBL (12-16) and
MU (12-17).

These were the 26 new DRAFT cards: AAPL, ADM, ANET, APA, ASND, BKR, COHR,
DDOG, EXPE, FRO, HSY, JBL, KEYS, LLY, NTAP, NTNX, NUE, ONON, PR, PSX, STLD,
TS, TXN, UI, VLO, XOM.

**Flags before reviewing:**
- **PLTR:** its government/defense business-activity question is still open.
- **Energy cluster** (APA, PR, PSX, VLO, XOM, DINO, CVE, CNQ, BKR, FRO, TS):
  this is a heavy energy tilt in this pool. Confirm each business screen.
- **ASND:** no earnings date was found, and R:R is 0.7.

## Follow-ups (priority order)

1. **Re-screen NOW and BMNR in Zoya/Musaffa.** Both screens are stale, and
   BMNR's business-activity question is now 2 runs old.
2. **Re-underwrite NOW (DRAWDOWN_REVIEW).** Decide whether Q3 and the
   18.5% cRPO guide break your recorded "what would change my mind" test. Then
   fill in `initial_stop`, `invalidation`, `pre_mortem`, `last_review`, and
   refresh `pe`/`last_price`.
3. **Fill in BMNR's holding file** (thesis, stop, target, pre-mortem). It is
   still empty 20 weeks after entry.
4. **Re-run `/discover` locally.** The rate-limited run left 35 leads without
   R:R.
5. **[Still open] Start `transactions.csv`** via `/apply-trade` to unlock the
   discipline guard. This book's swing from +15% to -20% in 14 weeks is the
   kind of sample that guard exists for.

---

Not a financial advisor. The Shariah compliance shown here is a broker-app
recorded flag or a mechanical pre-check, neither a fatwa. Verify independently
in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Q3 FY26 8-K — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm)
- [ServiceNow Q3 FY26 8-K/A — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000095/erq3fy262.htm)
- [Earnings call transcript: ServiceNow Q3 2026 — Investing.com](https://ng.investing.com/news/stock-market-news/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-2765235)
- [ServiceNow Stock Price Sinks As Q3 Results Expose Profit Strain — Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/servicenow-now-stock-price-sinks-as-q3-results-expose-profit)
- [NOW Stock Faces the Last Support on Anthropic Workplace News — FX Leaders](https://www.fxleaders.com/news/2026/11/10/now-stock-faces-the-last-support-on-anthropic-workplace-news-as-servicenow-shares-decline-following-third-quarter-earnings-report/)
- [ServiceNow Just Dropped 30% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [Why the 27% Crash in ServiceNow's Stock Looks Like a Golden Opportunity — Motley Fool](https://www.fool.com/investing/2026/11/01/why-the-27-crash-in-servicenows-stock-looks-like-a/)
- [ServiceNow Lays Off More Staff After Q3 Earnings — SalesforceBen](https://www.salesforceben.com/servicenow-lays-off-more-staff-after-q3-earnings-fail-to-impress-wall-street/)
- [BMNR Stock Down 8.6% — GuruFocus](https://www.gurufocus.com/news/9218715/bitmine-immersion-technologies-inc-bmnr-stock-down-86-but-still-overvalued-gf-score-49100)
- [Bitmine 8-K (Nov 2026) — SEC](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm)
- [BMNR Stock Price History — StockAnalysis](https://stockanalysis.com/stocks/bmnr/history/)
