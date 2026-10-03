# Portfolio Assessment — 2026-10-03

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status is the broker app's recorded screen or a mechanical pre-check, not a
fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (16 new DRAFT
cards: AAPL, AMKR, APA, BBY, BLSH, CORZ, DDS, FLYW, FN, HBM, JBL, LLY, NTNX, TECK, TS,
XOM; existing cards unchanged) → `prices/shariah/dcf/signals/verdict/recommend`, all
live, no data gaps. **Not done this run:** per-holding web catalyst research (scheduled,
unattended run). `journal.py` skipped — no `transactions.csv`.

## Verdicts
**BMNR -> HOLD** (DEFAULT, no rule fired). $26.27, **+70.3%** vs $15.43 cost, weight 21.8%.
Trailing stop $23.66 (~9.9% below), 6m momentum +18.6%, ATR 6.59% (vol-throttle note:
size down). **Mandate flag:** recorded "compliant" (broker app, 2026-07-07) but the
mechanical pre-check still fails on business activity (`Capital Markets`) — unresolved
since the 2026-08-19 report. Re-screen in Zoya/Musaffa.

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 ≥ 50: hold, do not add). $134.38, **+16.9%**
vs $114.97, weight 78.2%. Trailing stop $129.37 (~3.7% below), 6m momentum +34.0%.
**Mandate flag:** recorded Shariah screen (2026-06-09) is now >100 days old — stale,
re-screen.

Mechanical PM proxies (not a real conviction call): both LOW conviction; reward:risk
negative because the DCF target sits below price (BMNR -9.8:1, NOW -2.85:1).

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.27 | 10 | $15.43 | $262.70 | +70.3% | 21.8% |
| NOW | $134.38 | 7 | $114.97 | $940.66 | +16.9% | 78.2% |

Total **$1,203.36** (was $1,105.51 on 2026-08-19). Concentration rules muted (<4 names),
but NOW is 78% of the book.

## Action flags (priority)
1. BMNR: ratio/business pre-check FAIL vs recorded compliant — resolve in Zoya/Musaffa.
2. NOW: Shariah screen stale (>100d) — re-screen.
3. BMNR vol throttle (ATR 6.59%).
4. NOW valuation rich (P/E ~119).

## Rules fired (your own)
- NOW: VALUATION_RICH -> hold, do not add.
- BMNR: vol throttle -> size down note.
No SELL/TRIM/REVIEW triggers.

## DCF
BMNR $0.72 vs $26.27 (-97.3%); NOW $120.12 vs $134.38 (-10.6%). Assumptions: 5y growth
5% (BMNR) / 18% (NOW), terminal 2.5% / 3%, discount 10%. The DCF doesn't fit a
crypto-treasury business, so the BMNR figure is not meaningful.

## New ideas
`recommend.py` returned no ideas (watchlist empty of gated names): nothing is a
BUY-CANDIDATE. All 50 discovery rows are LEAD/RESEARCH — no edge supplied, Shariah
unverified. Top by max-benefit rank (see `leads.md` for entry/target/stop and
earnings dates): GOOGL, LLY, GDDY, CORZ, BLSH, JBL, HAS, ASTS, FLYW, STX.

## Draft setups awaiting your review (formula outputs, not buys)
All `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`.
New this run (entry / stop / T1, next print):
- AAPL 333.69 / 324.31 / 347.76 (10-29) · AMKR 56.02 / 49.17 / 66.29 (10-26)
- APA 43.68 / 42.81 / 44.98 (11-04) · BBY 87.97 / 87.59 / 88.54 (11-24)
- BLSH 34.23 / 33.69 / 35.04 (11-12) · CORZ 16.45 / 16.10 / 16.98 (10-23)
- DDS 654.11 / 637.43 / 679.13 (11-12) · FLYW 17.58 / 17.49 / 17.71 (11-03)
- FN 463.69 / 410.84 / 542.96 (11-02) · HBM 27.20 / 25.84 / 29.25 (10-29)
- JBL pullback 307.34 / 292.73 / 329.26 · LLY 1142.85 / 1126.73 / 1167.03 (10-29)
- NTNX 72.29 / 67.17 / 79.96 (11-25) · TECK 68.56 / 65.10 / 73.75 (10-29)
- TS 55.99 / 54.45 / 58.31 (11-04) · XOM 164.01 / 158.65 / 172.05 (10-30)

Caution: several drafts (APA, BBY, BLSH, CORZ, FLYW, LLY, TS) have a stop only 0.2–1.5%
from entry — those tiny R values make the headline reward:risk look huge but sit inside
normal noise and would not survive an earnings gap (`earnings_gap_assumption_pct: 25`).
Treat the leads' R:R figures for them skeptically.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa.
2. Decide whether NOW at 78% of the book fits your intent.
3. Review/edit drafts you care about; only you flip `status: planned`.
4. If you trade anything, run /apply-trade.

Not financial advice; verify Shariah status in Zoya/Musaffa.
