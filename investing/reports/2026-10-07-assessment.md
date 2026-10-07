# Portfolio assessment — 2026-10-07

Decision support, not advice. Every verdict below is YOUR `rules.md` resolving
mechanically; buy/sell/hold calls stay with you. Live Yahoo data worked this run
(discovery pool populated). Web research was a light standard search only.

## Verdicts

| Ticker | Verdict | Rule | Price | Trailing stop | Dist. to stop | R-multiple | 6m mom | Return |
|---|---|---|---|---|---|---|---|---|
| BMNR | HOLD | DEFAULT (no rule fired) | 24.55 | 23.93 | -2.5% | n/a | +15.1% | +59.1% |
| NOW | HOLD | DEFAULT (no rule fired) | 139.74 | 131.01 | -6.3% | n/a | +37.7% | +21.6% |

Portfolio notes: BMNR ATR 6.7% — vol throttle says size down. Only 2 holdings, so
concentration rules are muted (NOW is 79.9% of the book vs the 22% cap; BMNR 20.1%).

PM records (mechanical proxies only, not a real conviction call):
- **BMNR** — conviction LOW (reward:risk -29:1 because the DCF target of $0.72 is
  far below price; a DCF is a poor fit for a crypto-treasury vehicle). Stop 23.93.
  `would_buy_today` flag = true. Holding file still has no thesis, variant view,
  stop, target or pre-mortem.
- **NOW** — conviction LOW (reward:risk -2.2:1: DCF value 120.12 < price 139.74).
  Catalyst: Q3 earnings, est. 2026-10-28 (21 days; soft/undated in the holding file).

## Snapshot

Total value $1,223.60. NOW $978.15 (79.9%, +21.6% vs cost 114.97); BMNR $245.45
(20.1%, +59.1% vs cost 15.43). BMNR's weight is up from 18.6% in the 08-19 report.

## Action flags (priority)

1. **Mandate — BMNR Shariah conflict, still open.** Recorded `compliant`
   (broker app, 2026-07-07) but the ratio pre-check fails the business screen:
   industry "Capital Markets". The automated pipeline does not re-surface this on
   its own. Re-screen in Zoya/Musaffa before holding or adding. This has now been
   open across multiple runs.
2. **Mandate — NOW Shariah record is stale** (screened 2026-06-09). Ratios pass
   (debt 1.7%, liquid 4.3%). Refresh the screen.
3. **Valuation — NOW P/E ~119**: rich; growth must keep delivering.
4. DCF shows both holdings above intrinsic value (see below).

## Per-holding read (case for each side, no pick)

**NOW** — Keep: +21.6% vs cost, above its 20-EMA (135.9) and stop (131.0), 6m
momentum +37.7%, Q3 print ~10-28 with AI contract value narrative; revenue +24%
YoY and a Q2 beat (EPS 0.90 vs 0.86 est.). Trim: 79.9% of the book against a 22%
cap, P/E ~119, DCF 14% below price, and earnings in 21 days can gap through the
stop.

**BMNR** — Keep: +59% vs cost, 6m momentum +15%, still above the trailing stop.
Trim/review: price sits below its 20-EMA (25.82) and only 2.5% above the stop,
ATR 6.7%, unresolved Shariah business-activity flag, no written thesis or
invalidation, ETH-treasury value tracks ETH and the mNAV premium. Latest news I
could find is from Aug 2026 (5.8M ETH held; ~$11.3B holdings); nothing from
October surfaced — not verified further.

## Suggested actions (from YOUR rules)

No rule fired: both verdicts are DEFAULT HOLD. Not-fired but worth noting:
`max_position_pct` 22 — NOW at 79.9% would breach it if the concentration rule
were active (muted below 4 names by `min_names_for_concentration`); BMNR
`vol_throttle_atr_pct` 6 exceeded (ATR 6.7%). If you execute anything, run
`/apply-trade` so holdings and the ledger update.

## DCF

| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| BMNR | 0.72 | 24.55 | -97.1% | 5y growth 5%, terminal 2.5%, discount 10% |
| NOW | 120.12 | 139.74 | -14.0% | 5y growth 18%, terminal 3%, discount 10% |

The BMNR DCF is not meaningful (treasury asset, not an operating cash-flow story).

## New ideas

`recommend.py` returned no BUY-CANDIDATE ideas. discover.py produced 50 leads:
24 LEAD + 26 RESEARCH-tier. None can be a BUY-CANDIDATE — all cards are
`status: draft` and Shariah is `unverified` by construction. Leads were
refreshed in `leads.md`; top by reward:risk: IONQ 20.0, GDDY 17.8, LIF 15.6,
JBL 14.7, STX 13.0, VICR 11.3. Earliest catalysts: VICR / HAS 2026-10-20,
LRCX / TSLA / TER 2026-10-21, AMKR 10-26, STX 10-27, GOOGL 10-28.
Reward:risk numbers are formula outputs from tight ATR stops and can look
extreme (stops a few % under entry); treat >10:1 skeptically.

Recurring questions carried forward: PLTR (government/defense business
activity) and the precious-metals/mining cluster (CDE, AR, AGI, IAG, KGC, EGO).
New lead names this run include XOM, APA, TECK (energy/materials — check
business and debt screens) and LLY, AAPL, DDOG, FRO.

## Draft & planned setups

14 new DRAFT cards scaffolded this run: AAPL, AMKR, APA, DDOG, FLYW, FN, FRO,
HBM, JBL, LLY, SMTC, TECK, TS, XOM (77 cards total, up from 63). None are
`planned`. Each is **RESEARCH — DRAFT awaiting your review (set status: planned
to approve)**. Example, AAPL (`earnings_run`): entry $336.38, stop $325.46
(chandelier 22d HH $345.34 − 3×ATR $6.63), T1 $352.76 (1.5R), holding window
21d, catalyst earnings 2026-11-02, invalidation "no positive drift 5 sessions
pre-print / gives back >1 ATR". Every level is a formula output; edit what you
disagree with, then flip to `planned` and screen in Zoya/Musaffa. Full plans are in
`setups/<ticker>.md`. No PLANNED/LIVE cards exist, so no BUY-CANDIDATE appears.

## Follow-ups

1. **[Urgent] Re-screen BMNR in Zoya/Musaffa** (industry flag: Capital Markets).
2. **[Time-boxed] NOW earnings ~2026-10-28 (21 days)** — decide ahead of time
   how you'll treat the gap risk; refresh NOW's stale Shariah screen.
3. **[Housekeeping] Fill BMNR's PM fields** (thesis, variant view, stop, target,
   pre-mortem) — still empty ~3 months after entry.
4. **[Housekeeping]** 14 new draft cards; review at your own pace.
5. **[Infrastructure — still open]** No `transactions.csv` ledger exists, so the
   discipline guard (net-of-cost vs benchmark) cannot run. Log the FIG sale and
   BMNR buy via `/apply-trade`.

Not a financial advisor. Shariah status shown is a recorded broker-app flag or a
mechanical pre-check, not a fatwa — verify in Zoya/Musaffa before acting.

Sources:
- [ServiceNow earnings date / Q2 2026 — TipRanks](https://www.tipranks.com/stocks/now/earnings/q2-2026-report)
- [ServiceNow Earnings Preview — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-earnings-preview-expect-103513109.html)
- [BMNR — MarketBeat](https://www.marketbeat.com/earnings/reports/2026-7-14-bitmine-immersion-technologies-inc-stock/)
