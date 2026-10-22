# Portfolio assessment — 2026-10-22

Decision support, not advice. Every verdict below is your own `rules.md` resolving mechanically.
Shariah status must be verified in Zoya/Musaffa. Web catalyst research was NOT performed in this
automated run (scripts/Yahoo data only); no catalysts or news are asserted beyond what the files record.

## Verdicts
- **BMNR -> HOLD** (DEFAULT: no rule fired). Price 22.23, weight 16.9%, return +44.0%. Trailing stop 24.07 — price is **below** it (~8% under); 6m momentum +24.8%. Vol throttle: ATR 6.72% — size down.
- **NOW -> HOLD** (VALUATION_RICH: P/E ~119, hold, do not add). Price 155.87, weight 83.1%, return +35.6%. Trailing stop 139.83 (10.3% below); 6m momentum +66.1%.

PM-grade proxies (mechanical, not a conviction call): both conviction LOW. NOW reward:risk -2.2:1 vs DCF target 120.12; BMNR has no stated thesis/reward:risk (DCF 0.72 is not meaningful for this business).

## Snapshot
Total value $1,313.11 — NOW $1,090.81 (83.1%), BMNR $222.30 (16.9%). Only 2 holdings: concentration check muted until >= 4 names, but NOW at 83% is very concentrated.

## Action flags (priority order)
1. **Mandate — Shariah stale:** both BMNR (screened 2026-07-07) and NOW (2026-06-09) are >100d old — re-screen.
2. **Mandate — BMNR pre-check fails:** industry "Capital Markets" matches a core-business knockout, despite recorded `compliant` (broker_app). Verify in Zoya/Musaffa before holding/adding.
3. BMNR trading below its trailing stop (24.07); note the stop did not produce a SELL verdict under current rules.
4. NOW valuation: P/E ~119; DCF 120.12 vs 155.87 (-22.9%).

## Per-holding read
- **NOW** — keep: durable subscription growth, strong momentum, above trailing stop. Trim: 83% of account, rich P/E, DCF below price, stale Shariah screen. Your call.
- **BMNR** — keep: +44% gain, positive 6m momentum. Trim/exit: below trailing stop, high vol, Shariah pre-check flag, no written thesis.

## Suggested actions (your rules)
- Rule VALUATION_RICH fired on NOW -> hold, do not add.
- Vol throttle note on BMNR -> size down.
If you execute anything, run /apply-trade.

## DCF (assumptions visible)
- NOW: intrinsic 120.12 vs 155.87 (-22.9%); growth 18% 5y, terminal 3%, discount 10%.
- BMNR: intrinsic 0.72 vs 22.22; growth 5%, terminal 2.5%, discount 10% — not meaningful for this asset type.

## New ideas
`recommend.py` ideas array is empty: no card is `planned` + Shariah-verified, so **no BUY-CANDIDATE**. Discovery wrote 50 LEADs to `leads.md` (all UNVERIFIED Shariah).
Highest reward:risk leads (formula estimates): FICO 10.2:1 (earnings 11-04), ADI 8.8:1 (11-24), TS 7.1:1 (11-04), DDOG 5.5:1 (11-04), TSLA 4.8:1, PAY/LIF 3.8:1, STLD 3.4:1, MSFT 3.3:1 (10-28).

## Draft & planned setups
19 new DRAFT cards scaffolded today — each is **RESEARCH — DRAFT awaiting your review (set status: planned to approve)**; all levels are formula outputs, Shariah `unverified`:
AAPL, AEM, APA, ASND, BBY, BKR, DDOG, EXPE, FLYW, FRO, FSLR, LLY, NTAP, NTNX, PR, SNA, STLD, TS, XOM (see `setups/<ticker>.md` for entry/stop/target/logic/invalidation/gap plan).
**Review before use — several drafts have stop >= entry** (AEM, BKR, FRO, FSLR, NTAP, NTNX, SNA): the chandelier stop sits above the entry, so target is null and R:R is undefined; these are not usable plans as written. SNA's earnings date is today (2026-10-22). Entry-near-print cards carry gap risk; stops do not execute through an earnings gap.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; resolve BMNR's Capital Markets flag.
2. Decide on NOW concentration (83%) and BMNR vs its trailing stop.
3. Review/edit the DRAFT cards you care about; fix the stop>=entry ones before promoting.
4. Screen any promoted name in Zoya/Musaffa, then rerun recommend.py.

Not financial advice. Verify Shariah compliance in Zoya/Musaffa.
