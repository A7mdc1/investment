# Portfolio Assessment — 2026-09-29

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is the broker app's recorded screen or a mechanical
pre-check, not a fatwa — verify in Zoya/Musaffa before acting.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (16 new DRAFT
cards: AAPL AMKR BBY BLSH CORZ DDOG FN FRO HBM HPE LLY NTNX NUE SMTC TS XOM) →
`prices / shariah / dcf / signals / verdict / recommend`. All data live.
**Not done this run:** per-holding web catalyst research and watchlist web
research (unattended run) — no catalysts are asserted beyond what the files hold.

## Verdicts (your rules resolving, not advice)
- **BMNR -> HOLD** (DEFAULT). $26.54, +72.0% vs $15.43 cost, 22.6% weight. Trailing stop 23.55 (11.3% away), 6m momentum +30.1%. Vol throttle: ATR 6.67% — size down.
- **NOW -> HOLD** (VALUATION_RICH: P/E ~119, hold, do not add). $129.58, +12.7% vs $114.97, 77.4% weight. Trailing stop 131.20 — **price is below its trailing stop** (-1.3%), yet no SELL rule fired; check how you want that stop treated. 6m momentum +37.9%.
- Portfolio note: only 2 names, concentration rule muted; NOW is 77% of the book.

PM records (mechanical proxies only): both conviction LOW. BMNR R:R -8.6:1 (DCF target $0.72 vs price — DCF is meaningless for this asset); NOW R:R missing, no dated catalyst, DCF $120.12.

## Snapshot
Total $1,175.66 — NOW $906.78 (77.4%, +12.7%), BMNR $265.45 (22.6%, +72.0%).

## Action flags (priority)
1. **BMNR Shariah conflict (persisting since 2026-08-19):** recorded `compliant` (broker app, screened 2026-07-07) but the ratio pre-check fails — Yahoo industry "Capital Markets" matches a core-business knockout. recommend.py shows PASS because it reads only the recorded status. Re-screen in Zoya/Musaffa; per your rules compliance is a gate.
2. **NOW Shariah screen stale:** recorded 2026-06-09 (>100d). Pre-check itself passes (debt 1.8%, liquid 4.7%). Re-screen.
3. NOW valuation: P/E ~119; DCF $120.12 vs $129.58 (-7.3%).

## DCF (assumptions visible)
- NOW: intrinsic $120.12, upside -7.3% (growth 18% 5y, terminal 3%, discount 10%).
- BMNR: intrinsic $0.72, upside -97.3% (growth 5%, terminal 2.5%, discount 10%) — not a valid model for a crypto-treasury company; ignore.

## Suggested actions from your rules
- VALUATION_RICH fired on NOW -> hold, do not add.
- BMNR vol throttle -> size down on any add.
- Nothing auto-traded. If you execute anything, run /apply-trade.

## New ideas
`recommend.py` ideas array is empty: no planned/compliant card clears the gates. No BUY-CANDIDATEs. All cards are DRAFT or unverified -> **RESEARCH — DRAFT awaiting your review (set status: planned to approve)**; every level is a formula output.
Top leads by discovery rank (LEAD/RESEARCH only, Shariah UNVERIFIED — see `leads.md` for entry/target/stop):
GOOGL (R:R 16.6, earnings 2026-10-28), BLSH (15.5, 11-12), TSLA (20.0, 10-21), TS (10.6, 11-04), WDC (9.4, 11-05), HBM (7.9, 10-29), CORZ (19.0, 10-23), MU (2.0, earnings **2026-09-30**, tomorrow), AVGO (9.4, 12-09), CIEN (18.0, 12-10).
Very high R:R on tight stops (e.g. GOOGL stop 339.42 vs entry 339.47) reflects formula output, not edge — treat sceptically. Full card details in `setups/`.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; record result on the holdings.
2. Decide how to treat NOW below its trailing stop.
3. Fill in NOW/BMNR thesis fields (conviction, target, invalidation, pre-mortem) — currently null.
4. Review draft cards you care about; edit and set `status: planned`.
5. No transactions.csv yet — discipline guard dormant.

Not a financial advisor. Verify Shariah status in Zoya/Musaffa.
