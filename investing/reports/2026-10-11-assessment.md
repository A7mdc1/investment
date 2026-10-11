# Portfolio assessment — 2026-10-11

Decision support, not advice. Every verdict below is your own `rules.md` resolving mechanically.
Live Yahoo data worked this run. **Web catalyst research (SKILL step 3) was not performed** in this
automated run — catalyst dates below come only from Yahoo/discovery; verify before relying on them.

## Verdicts
- **BMNR -> HOLD** (DEFAULT: no rule fired). Price 24.03, trailing stop 23.96 (0.3% below price), 6m momentum +13.7%.
  Portfolio note: ATR 6.79% — size down per vol throttle. PM fields (thesis, variant view, stop, target, pre-mortem) are still empty.
- **NOW -> HOLD** (VALUATION_RICH: P/E ~119 — hold, do not add). Price 140.86, trailing stop 131.36 (6.7% below), 6m momentum +58.0%.
  Concentration check is muted (only 2 holdings).
Mechanical PM proxies (not a real conviction call): both LOW conviction because reward:risk from DCF targets is negative (BMNR -28.6:1, NOW -2.2:1).

## Snapshot
Total value $1,226.32 — NOW 80.4% ($986.02, +22.5%), BMNR 19.6% ($240.30, +55.7%).

## Action flags
1. **BMNR Shariah (policy):** recorded compliant (broker app, 2026-07-07) but the ratio pre-check fails the business screen
   (industry "Capital Markets"). Unresolved since the last report — re-screen in Zoya/Musaffa.
2. **NOW Shariah stale:** recorded compliant, screened 2026-06-09 (>100 days) — re-screen.
3. NOW valuation: P/E ~119.

## Per-holding read
- **NOW** — Keep: +58% 6m momentum, price above fast EMA (136.57), trailing stop not close. Trim/not-add: DCF intrinsic 120.12 vs 140.86 (-14.7%), P/E ~119, 80% of the book. Next earnings ~2026-10-28 (17 days; Yahoo date, unverified), i.e. a gap risk the trailing stop won't protect.
- **BMNR** — Keep: +55.7% return, momentum positive. Trim/exit: price sits 0.3% above the trailing stop and below fast EMA (25.51), so a small move triggers your stop rule; DCF is not meaningful for this business (0.72 intrinsic); compliance unresolved.

## Rules fired
VALUATION_RICH (NOW: hold, do not add); vol throttle (BMNR: size down). If you execute anything, run /apply-trade.

## DCF (assumptions: 5y growth / terminal / discount)
- NOW: 120.12 vs 140.86 (-14.7%); 18% / 3% / 10%.
- BMNR: 0.72 vs 24.03 (-97%); 5% / 2.5% / 10% — not meaningful for a crypto-treasury style company.

## New ideas
No ideas in `watchlist.md` cleared recommend.py's gates (0 BUY-CANDIDATE). Discovery produced 50 leads (all LEAD/RESEARCH, Shariah UNVERIFIED);
top 15 by max-benefit rank:

| Ticker | Verb | R:R | Catalyst | Entry / target / stop (formula) |
|---|---|---|---|---|
| LRCX | LEAD | 17.2:1 | earnings 2026-10-21 | entry ~318.84 / target 437.97 / stop 311.94 |
| ALAB | LEAD | 13.4:1 | earnings 2026-11-03 | entry ~342.21 / target 499.58 / stop 331.45 |
| AEM | LEAD | 18.8:1 | earnings 2026-10-28 | entry ~189.02 / target 252.26 / stop 185.65 |
| IAG | LEAD | 16.1:1 | earnings 2026-11-05 | entry ~18.80 / target 24.87 / stop 18.78 |
| TER | LEAD | 8.2:1 | earnings 2026-10-21 | entry ~402.68 / target 487.51 / stop 392.36 |
| KLIC | LEAD | 20.0:1 | earnings 2026-11-18 | entry ~92.01 / target 131.13 / stop 90.20 |
| TTMI | LEAD | 13.5:1 | earnings 2026-11-04 | entry ~121.01 / target 195.64 / stop 115.49 |
| MKSI | LEAD | 9.4:1 | earnings 2026-11-04 | entry ~264.50 / target 377.40 / stop 252.51 |
| AMKR | LEAD | 20.0:1 | earnings 2026-10-26 | entry ~49.12 / target 74.59 / stop 48.92 |
| NUE | LEAD | 5.7:1 | earnings 2026-10-26 | entry ~250.33 / target 279.39 / stop 245.21 |
| ARW | LEAD | 5.3:1 | earnings 2026-10-29 | entry ~227.90 / target 249.34 / stop 224.99 |
| SMCI | LEAD | 5.2:1 | earnings 2026-11-03 | entry ~41.86 / target 58.55 / stop 38.65 |
| SIMO | LEAD | 5.3:1 | earnings 2026-10-28 | entry ~263.90 / target 354.23 / stop 246.89 |
| CVE | LEAD | 5.3:1 | earnings 2026-10-29 | entry ~31.39 / target 34.08 / stop 31.08 |
| AVGO | LEAD | 8.6:1 | earnings 2026-12-09 | entry ~361.54 / target 466.67 / stop 349.30 |

Full list in `leads.md`. Low-R:R names among the 15 new draft cards (AAPL 0.8:1, DDOG 0.0:1, LLY 1.9:1) fail the asymmetry gate.

## Draft setups
15 new DRAFT cards scaffolded this run (setups/: aapl, aem, amkr, apa, ddog, expe, fn, hbm, jbl, lly, nue, pr, smtc, teck, ts), joining the existing drafts.
Each is `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`; all levels are formula outputs, Shariah `unverified`.
None is `planned`, so none can be a BUY-CANDIDATE. Previously flagged recurring questions (PLTR defense exposure; precious-metals/mining names AEM, AGI, IAG, KGC, EGO, CDE, AR) still need a real business-activity screen.

## Follow-ups
1. Re-screen BMNR (ratio pre-check conflict) and NOW (stale) in Zoya/Musaffa.
2. Fill BMNR PM fields (thesis, variant view, stop, target, pre-mortem).
3. NOW earnings ~2026-10-28: decide gap plan; BMNR stop is 0.3% away.
4. Review draft cards at your pace.
5. No `transactions.csv` ledger yet — log trades via /apply-trade to enable the discipline guard.

Not a financial advisor. Verify Shariah status independently in Zoya/Musaffa.
