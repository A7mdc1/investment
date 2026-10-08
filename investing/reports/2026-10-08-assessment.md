# Portfolio Assessment — 2026-10-08

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is a recorded broker-app screen or a mechanical pre-check,
neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran
`discover.py` (live Yahoo, top 50 kept) → `scaffold.py --all-leads` (**15 new DRAFT
cards**: AMKR, BBY, DDOG, DDS, EXPE, FLYW, FN, JBL, LLY, PBF, PENG, PR, TECK, TS, XOM;
existing cards left unchanged) → prices / shariah / dcf / signals / verdict / recommend, all live,
no data gaps. `recommend.py` returned an empty `ideas` array (nothing in watchlist.md
passed to it), so there are no BUY-CANDIDATEs. No `transactions.csv`/`journal.csv` exists,
so the discipline guard stays dormant.

## Verdicts (your rules resolving, not advice)

**BMNR -> HOLD** (DEFAULT, no rule fired). $23.58, +52.8% vs $15.43 cost.
Trailing stop $23.87 — price is **~1.2% below it** (mechanical proxy; verdict.py still
resolved HOLD — see note). EMA-fast $25.62, 6m momentum +14.8%. Portfolio note: ATR 7.05% — size
down per vol throttle. Mechanical PM record: conviction LOW (no thesis/R:R recorded), DCF
$0.72 (model does not fit a crypto-treasury business — ignore as a valuation).

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 — hold, do not add). $137.72, +19.8% vs $114.97.
Trailing stop $131.26 (4.7% below), EMA-fast $135.92, 6m momentum +46.0%. PM record:
conviction LOW, reward:risk -2.7:1 against DCF target.

Only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $23.58 | 10 | $15.43 | $235.75 | +52.8% | 19.7% |
| NOW | $137.72 | 7 | $114.97 | $964.04 | +19.8% | 80.3% |

**Total $1,199.79** (cost $959.09, ~+25.1% unrealised; prior report $1,105.51).

## Action flags (priority order)
1. **[Mandate] BMNR: ratio pre-check still FAILS** (`industry 'Capital Markets'` — core
   business fails screen) vs recorded `compliant` (broker app, 2026-07-07). Unresolved since
   the 08-19 report. Web: Zoya's BMNR page lists it compliant but with a blank "as of" date
   and contradictory wording across language versions ([Zoya](https://zoya.finance/stocks/bmnr)).
   Business is an ETH treasury with staking income (5.82M ETH, ~5.07M staked, 2.61% yield per
   [Benzinga, Aug 2026](https://www.benzinga.com/node/49617005)). Re-screen in Zoya/Musaffa and record the result.
2. **[Mandate] NOW: Shariah screen stale** (2026-06-09, >100 days). Ratio pre-check clean
   (debt 1.7%, liquid 4.4%). Re-screen.
3. **BMNR sits just under its chandelier trailing stop** ($23.87 vs $23.58) — your own
   stop level; verdict.py did not escalate it, so check how the rule treats a close vs intraday.
4. NOW valuation rich (P/E ~119; DCF $120.12 → -12.8%; DCF assumptions: growth_5y 18%,
   terminal 3%, discount 10%).

## Per-holding read
**BMNR** — Keep: +52.8% gain, 6m momentum positive, ETH accumulation continuing. Trim/exit:
compliance is unresolved (gate, not tiebreaker), price at/below trailing stop, ATR 7% means a
10-share position moves ~$16/day, and no thesis/invalidation is written on the card.
**NOW** — Keep: +46% 6m momentum, durable subscription growth, above stop and EMA. Trim: 80%
of the book, P/E ~119, DCF below price, stale Shariah screen. Next catalyst: Q3 earnings,
**date unconfirmed** — estimates Oct 26 ([Earnings Whispers](https://beta.earningswhispers.com/go/w/NOW))
to Oct 28 ([TipRanks](https://www.tipranks.com/stocks/now/earnings)); watch for the company's announcement.

## Suggested actions (your rules)
- Rule VALUATION_RICH fired (NOW, P/E ~119) -> hold, do not add.
- Vol throttle fired (BMNR, ATR 7.05%) -> size down.
If you execute anything, run /apply-trade so holdings + ledger update.

## New ideas
No BUY-CANDIDATEs and none possible: every card is `status: draft` and Shariah `unverified`.
Discovery leads (top by benefit, all LEAD / RESEARCH): LRCX (earnings 10-21), AR (10-28), TER
(10-21), ALAB (11-03), MKSI (11-04), TTMI (11-04), AMKR (10-26, new), LIF (11-09), EXPE
(11-04, new), KLIC (11-18), UTHR (10-28), TSLA (10-21). Full list in `leads.md`.
Reward:risk figures in leads.md are discovery-stage and optimistic; the cards' own plans
are formula outputs (see below).

## Draft setups awaiting review (RESEARCH — DRAFT awaiting your review; set status: planned to approve)
All levels are formula outputs, not recommendations. Newly scaffolded this run (entry / stop /
target, ~1.5R, catalyst, gap plan):
| Ticker | Type | Entry | Stop | Target | Catalyst | Gap plan |
|---|---|---|---|---|---|---|
| XOM | earnings_run | 168.36 | 158.44 | 183.24 | 10-30 | no_earnings_in_window |
| DDOG | earnings_run | 272.90 | 252.65 | 303.28 | 11-05 | no_earnings_in_window |
| EXPE | earnings_run | 267.01 | 261.77 | 274.89 | 11-04 | no_earnings_in_window |
| AMKR | earnings_run | 50.75 | 49.14 | 53.16 | 10-26 | exit_before |
| FN | earnings_run | 484.73 | 437.78 | 555.15 | 11-02 | no_earnings_in_window |
| FLYW | earnings_run | 18.24 | 16.93 | 20.20 | 11-03 | no_earnings_in_window |
| LLY | earnings_run | 1147.75 | 1120.07 | 1189.28 | 10-29 | exit_before |
| PBF | earnings_run | 87.98 | 73.85 | 109.17 | 10-29 | exit_before |
| TECK | earnings_run | 64.90 | 64.71 | 65.18 | 10-29 | exit_before |
| TS | earnings_run | 56.69 | 54.55 | 59.89 | 11-04 | no_earnings_in_window |
| PR | earnings_run | 22.87 | 22.36 | 23.63 | 11-04 | no_earnings_in_window |
| BBY | earnings_run | 88.50 | 87.85 | 89.48 | 11-24 | no_earnings_in_window |
| DDS | earnings_run | 645.51 | 626.56 | 673.93 | 11-12 | no_earnings_in_window |
| JBL | pullback | 305.32 | 292.41 | 324.68 | 12-16 | no_earnings_in_window |
| PENG | pullback | 58.66 | 64.66 | none | 2027-01-05 | stop above entry — invalid plan |

Data-quality flags on the card set:
- ~35 older draft cards (e.g. ADI, ALAB, AMD, KLIC, TER, PLTR, MSFT, NVDA) carry **past
  catalyst dates** (July–Sept) and stale entry levels; `scaffold` leaves existing cards unchanged.
  Regenerate with `scaffold.py --force` for names you still care about (e.g. LRCX/TER/AR have
  10-21..10-28 prints in leads.md while their cards show older numbers).
- Invalid plans (stop >= entry, no target): AGI, AVGO, FOX, IAG, KGC, PENG, SMCI.
- Several cards have stop within ~1% of entry (AR, AU, CNQ, MT, PLTR, TECK, TER, ADI): 
  gap/slippage risk dominates the nominal 1.5R.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; record on the holdings.
2. Decide how BMNR's under-stop print is handled under your rule.
3. Confirm NOW's earnings date when announced; decide pre-print exposure.
4. Review draft cards for names you want; refresh stale ones; fix the 7 invalid plans.

Not financial advice. Verify Shariah status in Zoya/Musaffa.
