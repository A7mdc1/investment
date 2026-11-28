# Portfolio Assessment — 2026-11-28

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 169-name raw pool, top 50 kept) →
`scaffold.py --all-leads` (28 new DRAFT cards; 22 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py`. All of them ran on live data with no gaps.
`journal.py` was not run because there is still no `transactions.csv`, so the
discipline guard stays off.

Environment note: the sandbox's `pip` points at Python 3.13 while `python` is
3.11. The first run failed with `No module named 'yfinance'` until the
requirements were installed with `python -m pip install -r requirements.txt`.
This is not a repo bug, but future runs should install that way.

**Since the last report (2026-08-19):** no trades are recorded, and the holdings
files are unchanged. The book has fallen sharply. NOW gapped down about 27%
after its Oct 28 print and slid further in a software-sector selloff. BMNR gave
back all of its gain as ETH fell.

## Verdicts (lead with this)

These are YOUR rules resolving, not advice.

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50).
Live price **$92.80**, **-19.3%** vs. the $114.97 cost basis. That is **0.7 pts
short of your `drawdown_review_pct: 20` REVIEW trigger**, and signals.py already
raises the drawdown flag.

| PM-grade record (recommend.py, live — mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW — "missing reward:risk or a stated thesis — cannot self-assess conviction" |
| Shariah | **REVIEW** — recorded compliant, but screened 2026-06-09 (>100 days old, stale). The ratio pre-check is clean (debt 2.5%, liquid 6.5%) |
| Target / method | $119.65 DCF intrinsic value (+28.9%) |
| Trailing stop (chandelier) | $135.64. Price is **~32% below it**. The 22-day high still includes the pre-earnings ~$150 close |
| 6m momentum (skip last month) | +20.7%. This lags: the skip-month window excludes November's slide |
| Time horizon | core |
| Would buy today? | recommend.py says yes mechanically, but it can't see the stale-screen REVIEW (see flags) |
| What changes verdict | Price under ~$91.98 (-20% vs cost) fires DRAWDOWN_REVIEW. `thesis_broken: true` or the Shariah re-screen also change it |

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$13.88**,
**-10.0%** vs. the $15.43 cost basis. It was +33.1% at the last report.

| PM-grade record (recommend.py, live — mechanical proxy) | |
|---|---|
| Conviction | LOW — no thesis, stop or target recorded in the holding file |
| Shariah (recorded) | **REVIEW** — broker_app compliant, screened 2026-07-07, now stale (>100 days) |
| Shariah (mechanical ratio pre-check) | **FAIL — second run in a row**: industry `Capital Markets` matches the core-business exclusion |
| Target / method | DCF -$6.53 (-147%). Not meaningful: the model doesn't fit a crypto-treasury business |
| Trailing stop (chandelier) | $17.85. Price is **~22% below it** |
| 6m momentum (skip last month) | +14.4% |
| Would buy today? | recommend.py says yes mechanically. It reads only the recorded field, not the ratio-precheck fail or the stale date |
| What changes verdict | A Zoya/Musaffa business-activity re-screen |

- verdict.py note: only 2 holdings, so concentration rules stay muted until there are 4 or more names.
- **Portfolio notes (VOL_THROTTLE fired for both):** BMNR ATR 10.9%, NOW
  ATR 7.01%. Both are above `vol_throttle_atr_pct: 6`, which means "size down per
  vol throttle". This is new this run.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $13.88 | 10 | $15.43 | $138.80 | -10.0% | 17.6% |
| NOW | $92.80 | 7 | $114.97 | $649.60 | -19.3% | 82.4% |

**Total value: $788.40** | Cost: $959.09 | **Total return: -17.8%** (-$170.69 unrealised)

At the last report the book was worth $1,105.51 (+15.3%). It has fallen about
29% since. NOW is still 82% of the book.

## Action flags (priority order)

1. **[Mandate — NEW] Both Shariah screens are now stale.** NOW was screened
   2026-06-09 and BMNR 2026-07-07, and both are past one quarter.
   `rules.md` → COMPLIANCE_SCREEN says a screen older than one quarter means
   "REVIEW before any add". recommend.py reports `shariah_status: REVIEW` for
   both, **but verdict.py still prints HOLD**. The holding verb doesn't reflect
   your own COMPLIANCE_SCREEN rule. That is a gap in the pipeline worth fixing
   or at least knowing about.
2. **[Mandate — carried over, still open] BMNR business-activity pre-check FAILS**
   for the second run in a row (`Capital Markets`). The facts behind it haven't
   changed. Bitmine describes itself as the #1 Ethereum treasury, with about
   6.09M ETH, about 5.2M of it staked. It reports total crypto, cash and
   securities of $11.1B as of Nov 23, down from $14.5B on Nov 2. It now pays a
   $0.01/share cash dividend (declared Nov 25, record date Dec 8). Under your
   Gate 1, a confirmed fail is an absolute SELL regardless of P/L. The re-screen
   was the top follow-up last run and has not been recorded.
   [Nasdaq PR](https://www.nasdaq.com/press-release/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens) ·
   [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm)
3. **[Drawdown / NOW] -19.3% vs cost, 0.7 pts from DRAWDOWN_REVIEW.**
   signals.py raised the drawdown flag: "revisit whether the thesis still holds."
   Price sits at 7% of its 52-week range.
4. **[Valuation data quality / NOW]** The P/E of ~119 that drives
   VALUATION_RICH is a hand-recorded front-matter value next to
   `last_price: 106.40`. It has not been refreshed. The rule's input is stale,
   so treat the HOLD/"do not add" driver with that in mind.
5. **[Vol throttle] Both names are above the 6% ATR threshold.** This matters
   only if you plan to add or open anything: size down.
6. **[Discovery] 50 leads, only 4 at LEAD tier** (AVGO, SNX, APH, RCL).
   **24 of 50 show `reward-risk n/a`**, because the formula stop sits above the
   entry price in a falling tape. See the Draft & planned setups section.

## Per-holding read

### NOW — ServiceNow, Inc

**Facts for the case to keep:** The fiscal Q3 2026 print (Oct 28) was not a
fundamental miss on the thesis metric. Subscription revenue was $3,988M,
+21% YoY (20.5% cc), above guidance of $3,975–3,980M. cRPO was $13.65B
(+20.5%) and RPO $29.7B (+22%). Full-year subscription guidance was raised to
$15.785B at the midpoint, the FCF margin target was raised to 36%, and the AI
ACV target was raised to $1.7B. Your recorded invalidation ("subscription
growth decelerating meaningfully below ~21–22% YoY") has not clearly occurred:
Q4 subscription guidance is +21.5% cc. The DCF now shows +28.9% to intrinsic
value under your 18% growth assumption.
[ServiceNow IR](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Third-Quarter-2026-Financial-Results/default.aspx) ·
[Quartr](https://quartr.com/events/servicenow-now-q3-2026_3gnKPsN5)

**Facts for the case to cut or trim:** The market punished the print anyway. The
stock fell about 27% the next day, from $150.13 to $109.67, its worst day since
2012, on Q4 cRPO guidance of about 18.5% vs. 20.5%. It then lost about $59B of
market cap in 14 trading days. Market cap is now below $100B, and the stock is
down about 39% YTD vs. the S&P +6.8%. The Nov 17 leg (-6.5%) was sector-wide:
25 of 28 systems-software peers fell, alongside Salesforce and Workday, on
fears that AI will erode seat-based pricing. That fear goes straight at a
seat-licensed workflow platform. Armis is expected to drag about 125 bps off
full-year subscription growth. Price is about 32% below the chandelier stop.
Your core exemption keeps TRAIL_STOP from firing, but the trend is plainly down.
The position is 82% of the book.
[24/7 Wall St. (Nov 17)](https://247wallst.com/investing/2026/11/17/servicenow-has-lost-about-59-billion-in-value-in-14-trading-days-since-a-report-where-revenue-beat/) ·
[24/7 Wall St. (Nov 28)](https://247wallst.com/investing/2026/11/28/servicenows-market-cap-just-fell-below-100-billion/) ·
[GuruFocus](https://www.gurufocus.com/news/9205950/servicenow-now-shares-drop-65-amid-market-selloff-trading-well-below-gf-value) ·
[Trefis](https://www.trefis.com/stock/now/articles/627538/how-risky-is-servicenow-stock-in-a-falling-market/2026-11-22)

**The question the facts leave you with:** your thesis metric (subscription
growth) is intact, but the leading indicator (cRPO guide) decelerated. The
market is re-rating the whole seat-based category. Whether that is a variant
opportunity or a broken thesis is exactly the `variant_view` field that is still
empty. **No catalyst is dated within 60 days.** Next earnings are around late
January 2027, outside `catalyst_horizon_days`. `last_review: 2026-06-15` is more
than 160 days old, past `review_cadence_days: 90`, and the Oct 28 print
required a re-underwrite under your discipline guards.

### BMNR — Bitmine Immersion Technologies

**Facts for the case to keep:** It is still growing its ETH stack (6.06M → 6.09M
in November), runs its own staking platform (MAVAN), and has started a small
cash dividend. Headlines say management is capping ETH buying at a 5%-of-supply
limit and "doubling down" after a $655M weekly drawdown. Those are headline
text only and unverified.

**Facts for the case to cut:** It is a leveraged proxy on ETH, which is about
$1,713 per Bitmine's own Nov 22 figure. Treasury value fell about 23% in three
weeks ($14.5B → $11.1B). The position has swung from +33% to -10% since the
last report. ATR is 10.9%/day, the highest in the book. Above all, the
compliance question (flag #2) is unresolved, and the holding file still has no
thesis, stop, target or pre-mortem.
[SEC 8-K filings via search](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226053668/ex99-1.htm)

**Verdict: HOLD mechanically. The compliance re-screen comes before any price
reasoning.**

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_SCREEN matches -> NOW and BMNR**: both screens are more than one
  quarter old. Your pre-set action is "REVIEW before any add". verdict.py does
  not surface this (see flag #1).
- **COMPLIANCE_GATE does NOT fire -> BMNR**: it reads only the recorded status
  (`compliant`). The ratio-precheck FAIL will not escalate automatically.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add. Its P/E input is stale (flag #4).
- **DRAWDOWN_REVIEW -> NOW**: not fired yet (-19.3% vs the 20% threshold). It
  fires at about $91.98.
- **TRAIL_STOP -> NOW / BMNR**: does not fire because `trade_type: core` exempts
  both. Both prices are well **below** their chandelier levels ($135.64 / $17.85).
  If either were tagged swing or momentum, this rule would read SELL.
- **VOL_THROTTLE fired -> both**: size down on any new risk.
- **Re-underwrite guard** (review_cadence_days 90 + "on every earnings print"):
  NOW is overdue. Its last review was 2026-06-15, and the Oct 28 print passed
  with no recorded review.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $92.80 | +28.9% | growth_5y 18%, terminal 3%, discount 10% (holding-file override) |
| BMNR | -$6.53 | $13.88 | -147% (not meaningful — model doesn't fit a crypto treasury) | growth_5y 5% (default), terminal 2.5%, discount 10% |

The NOW upside depends entirely on the 18% five-year growth assumption holding.
The market's re-rating is a bet that it won't.

## New ideas (watchlist.md)

`watchlist.md` is still empty, so step 4 has nothing to research.
recommend.py's `ideas` array returned **0 entries / 0 BUY-CANDIDATEs**.
None of the 91 cards in `setups/` is `planned`.

## Draft & planned setups — 50 leads, 28 fresh DRAFT cards

Leads at **LEAD** tier (all of them `RESEARCH — DRAFT awaiting your review`,
Shariah UNVERIFIED, every level a formula output):

| Ticker | Card | R:R | Entry / Target / Stop | Catalyst |
|---|---|---|---|---|
| AVGO | existing (stale) | 17.4:1 | ~312.34 / 493.43 / 307.38 | earnings 2026-12-09 |
| SNX | existing | 12.2:1 | ~225.47 / 298.24 / 224.82 | earnings 2027-01-07 |
| APH | existing | 3.8:1 | ~75.14 / 89.88 / 71.27 | earnings 2027-01-27 |
| RCL | existing | 3.2:1 | ~315.35 / 350.78 / 304.15 | earnings 2027-01-26 |

**Card-staleness caveat:** scaffold.py never overwrites an existing card
without `--force`. All four LEAD names already had cards from earlier runs, so
the cards carry the old levels, not the leads.md levels above. For example,
`setups/avgo.md` still targets a 2026-09-02 print, with entry $364.41 and a stop
of $384.52 sitting *above* entry, so it has no target. Re-scaffold
(`scaffold.py --force <ticker>`) or hand-edit before reviewing any of them.

New DRAFT cards this run (28): KLAC, SANM, VIAV, FN, DIOD, ANET, TS, UI,
LSCC, NTAP, COHR, TXN, FRO, LLY, HST, JBL, BBY, APA, NUE, ASND, AAPL, PSX,
PR, VLO, STLD, XOM, KEYS, NTNX. All are RESEARCH tier. The full list is in
`leads.md`.

**Flags before spending review time:**
- **24 of 50 leads show `reward-risk n/a`**: the chandelier stop is above
  entry because these names have pulled back below their 22-day-high minus 3×ATR.
  Mechanically, these setups have no defined risk yet. Nearly the whole
  energy/refiner cluster (XOM, PSX, VLO, APA, PR, CNQ, CVE, DINO, AR) is in
  this bucket.
- **HST** (Host Hotels, a REIT) passed the ratio pre-check, but hotel REITs
  usually carry business-activity issues (alcohol and other impermissible
  revenue). Screen it first.
- **PLTR** is back again with its long-running government/defense
  business-activity question still open.
- **FRO** (tankers) and the refiners: check the business screen and how they
  are financed before relying on the clean ratio pre-check.

## Follow-ups (priority order)

1. **[Urgent — 2nd run] Re-screen BMNR in Zoya/Musaffa** on the business
   activity specifically. Record the result and date in `holdings/bmnr.md`.
2. **[Mandate — new] Re-screen NOW.** The screen is stale, so per
   COMPLIANCE_SCREEN, no adds until it is refreshed.
3. **[Decision — NOW] Re-underwrite now.** It is 0.7 pts from DRAWDOWN_REVIEW,
   past the review cadence, and the Oct 28 print went by unreviewed. Fill in
   `variant_view`, `initial_stop`, `invalidation` and `last_review`, and refresh
   `pe` / `last_price` in the front-matter.
4. **[Housekeeping] Fill BMNR's PM fields** (thesis, stop, target,
   pre-mortem). They have been empty about 4.5 months.
5. **[Pipeline] Make verdict.py honour COMPLIANCE_SCREEN** (stale screen →
   REVIEW) so the holding verb matches recommend.py and your rules.
6. **[Pipeline] Re-scaffold stale cards** for leads that already have cards,
   starting with AVGO, SNX, APH and RCL.
7. **[Infrastructure — still open] Start a ledger** (`/apply-trade`) so the
   discipline guard can run. The FIG sale and BMNR buy are still unlogged.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Reports Third Quarter 2026 Financial Results — ServiceNow IR](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Third-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow Form 8-K (Q3 FY26) — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm)
- [ServiceNow (NOW) Q3 2026 earnings summary — Quartr](https://quartr.com/events/servicenow-now-q3-2026_3gnKPsN5)
- [ServiceNow Has Lost About $59 Billion in Value in 14 Trading Days — 24/7 Wall St.](https://247wallst.com/investing/2026/11/17/servicenow-has-lost-about-59-billion-in-value-in-14-trading-days-since-a-report-where-revenue-beat/)
- [ServiceNow Just Dropped 30% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [ServiceNow's Market Cap Just Fell Below $100 Billion — 24/7 Wall St.](https://247wallst.com/investing/2026/11/28/servicenows-market-cap-just-fell-below-100-billion/)
- [ServiceNow Shares Drop 6.5% Amid Market Selloff — GuruFocus](https://www.gurufocus.com/news/9205950/servicenow-now-shares-drop-65-amid-market-selloff-trading-well-below-gf-value)
- [How Risky Is ServiceNow Stock In A Falling Market? — Trefis](https://www.trefis.com/stock/now/articles/627538/how-risky-is-servicenow-stock-in-a-falling-market/2026-11-22)
- [What Is Driving ServiceNow Stock? — Trefis](https://www.trefis.com/stock/now/articles/626283/what-is-driving-servicenow-stock/2026-11-18)
- [Bitmine ETH Holdings Reach 6.06 Million Tokens — Nasdaq](https://www.nasdaq.com/press-release/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens)
- [Bitmine Form 8-K (Nov 2026) — SEC](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm)
- [Bitmine Form 8-K (Nov 2026) — SEC](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226053668/ex99-1.htm)
