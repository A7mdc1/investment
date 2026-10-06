# Portfolio Assessment — 2026-10-06

Not financial advice. Decision support only — every buy/sell/hold call is yours. Shariah status is either the broker app's recorded screen or a mechanical pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo, 158-name pool; 69 dropped by Shariah ratio flag, 1 by liquidity, 3 no price; top 50 kept: 26 LEAD / 24 RESEARCH) → `scaffold.py --all-leads` (14 new DRAFT cards: CORZ, AAPL, AMKR, APA, FLYW, FN, HBM, JBL, LLY, NUE, PR, TECK, TS, XOM) → `prices / shariah / dcf / signals / verdict / recommend` — all live, no data gaps. `journal.py` not run (no `transactions.csv`). **Not done this run:** per-holding web catalyst research (unattended run) — nothing below is sourced from news; verify catalysts yourself.

## Verdicts
**BMNR -> HOLD** (RULE: DEFAULT). $26.47, **+71.5%** vs $15.43 cost. Trailing stop $24.01 (~9.3% below), 6m momentum +23.8%. Vol throttle: ATR 6.11% — size down. PM record (mechanical proxy): conviction LOW (DCF-target $0.72 below price → R:R -10.5:1, a DCF-doesn't-fit-crypto-treasury artefact). Shariah recorded PASS (broker app, 2026-07-07) **but the mechanical pre-check still FAILS** (industry 'Capital Markets').

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 — hold, do not add). $137.59, **+19.7%** vs $114.97. Trailing stop $130.53 (~5.1% below), 6m momentum +40.5%. DCF $120.12 → -12.7% vs price. Conviction LOW (R:R -2.5:1). **Shariah screen is now STALE (screened 2026-06-09, >100d) — recommend.py shows REVIEW.**

These are your rules resolving, not advice. Only 2 holdings — concentration rules muted (<4 names).

## Snapshot (live)
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.47 | 10 | $15.43 | $264.65 | +71.5% | 21.6% |
| NOW | $137.59 | 7 | $114.97 | $963.13 | +19.7% | 78.4% |

**Total $1,227.78**, cost $959.09, ~+28.0% unrealised (+$268.69). NOW is 78% of the book.

## Action flags (priority order)
1. **[Mandate] NOW Shariah screen stale** — re-screen in Zoya/Musaffa. Ratio pre-check is clean (debt 1.7%, liquid 4.4%) but that is not the screen of record.
2. **[Mandate] BMNR pre-check FAIL still open** (flagged 2026-08-19, unresolved): business classed 'Capital Markets'. Per Gate 1 a confirmed fail = SELL regardless of the +71.5% gain. recommend.py reads only the recorded field, so it does not surface this. Re-screen the business-activity question specifically before adding or treating 'compliant' as settled. BMNR's holding file also still lacks thesis, variant view, stop, target, pre-mortem.
3. **[Valuation] NOW** P/E ~119 rich; do not add.
4. **[DCF caveat] BMNR** DCF -97% is a data gap, not a signal.
5. **[Risk] BMNR** ATR 6.1% — vol throttle says size down.

## Suggested actions (your rules)
- Rule VALUATION_RICH fired on NOW -> hold, do not add (P/E ~119 >= 50).
- Vol throttle note on BMNR -> size down (ATR 6.11%).
- No SELL/TRIM rule fired. If you execute anything, run /apply-trade.

## DCF (assumptions visible)
| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $26.47 | -97.3% | growth 5%, terminal 2.5%, discount 10% (model doesn't fit) |
| NOW | $120.12 | $137.59 | -12.7% | growth 18%, terminal 3%, discount 10% |

## New ideas — top 20 of 50 leads
All LEAD/RESEARCH only; Shariah UNVERIFIED and EDGE not supplied on every row; no BUY-CANDIDATE (none has a planned card with a verified screen).

| # | Ticker | Verdict | R:R | Card | Entry / Target / Stop | Catalyst |
|---|---|---|---|---|---|---|
| 1 | STX | LEAD | 12.4:1 | yes | ~808.29 / 1143.27 / 784.24 | earnings 2026-10-27 |
| 2 | GDDY | LEAD | 17.6:1 | yes | ~98.34 / 139.49 / 96.29 | earnings 2026-10-29 |
| 3 | CORZ | LEAD | 18.4:1 | no (new draft) | ~16.77 / 26.31 / 16.26 | earnings 2026-10-23 |
| 4 | LIF | LEAD | 12.7:1 | yes | ~41.27 / 58.56 / 39.92 | earnings 2026-11-09 |
| 5 | DLO | LEAD | 8.4:1 | yes | ~14.60 / 16.50 / 14.37 | earnings 2026-11-11 |
| 6 | IONQ | LEAD | 8.3:1 | yes | ~43.19 / 69.38 / 40.05 | earnings 2026-11-04 |
| 7 | UTHR | LEAD | 7.5:1 | yes | ~539.95 / 609.42 / 530.73 | earnings 2026-10-28 |
| 8 | JBL | RESEARCH | 12.0:1 | no (new draft) | ~304.36 / 428.67 / 294.02 | earnings 2026-12-16 |
| 9 | GOOGL | LEAD | 6.9:1 | yes | ~347.20 / 407.99 / 338.37 | earnings 2026-10-28 |
| 10 | DOCN | LEAD | 7.0:1 | yes | ~131.72 / 187.37 / 123.76 | earnings 2026-11-04 |
| 11 | PR | LEAD | 5.9:1 | no (new draft) | ~22.45 / 24.49 / 22.43 | earnings 2026-11-04 |
| 12 | LRCX | LEAD | 4.9:1 | yes | ~333.15 / 437.78 / 311.68 | earnings 2026-10-21 |
| 13 | CVE | LEAD | 5.3:1 | yes | ~31.46 / 34.09 / 31.13 | earnings 2026-10-29 |
| 14 | CNQ | LEAD | 5.8:1 | yes | ~48.27 / 51.84 / 48.16 | earnings 2026-11-05 |
| 15 | TSLA | LEAD | 4.0:1 | yes | ~380.96 / 498.65 / 351.15 | earnings 2026-10-21 |
| 16 | ULTA | LEAD | 6.4:1 | yes | ~546.25 / 690.11 / 523.71 | earnings 2026-12-03 |
| 17 | NUE | LEAD | 4.1:1 | no (new draft) | ~251.41 / 279.34 / 244.52 | earnings 2026-10-26 |
| 18 | LLY | LEAD | 3.7:1 | no (new draft) | ~1161.80 / 1292.32 / 1126.82 | earnings 2026-10-29 |
| 19 | AMKR | LEAD | 4.8:1 | no (new draft) | ~54.34 / 78.88 / 49.20 | earnings 2026-10-26 |
| 20 | ASTS | LEAD | 5.6:1 | yes | ~62.33 / 102.03 / 55.29 | earnings 2026-11-09 |

Full 50 in `leads.md`. Names here are mechanical formula outputs to investigate, not buys.

## Draft setups
14 new DRAFT cards were scaffolded (CORZ, AAPL, AMKR, APA, FLYW, FN, HBM, JBL, LLY, NUE, PR, TECK, TS, XOM); 36 leads already had cards. Every draft is `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`; all levels are formula outputs — edit what you disagree with, then flip `status: planned` and screen in Zoya/Musaffa. See `setups/<ticker>.md` for entry/stop/target, logic, gap plan and Shariah pre-check comment.

## Follow-ups
1. Re-screen NOW (stale) and BMNR (business-activity) in Zoya/Musaffa.
2. Fill BMNR's thesis/stop/target/pre-mortem fields.
3. Review drafts for the leads with nearest catalysts (LRCX/TSLA 10-21, CORZ 10-23, NUE 10-26, STX 10-27).
4. NOW is 78% of the book; consider before adding anything.

Not financial advice. Verify all Shariah status in Zoya/Musaffa.
