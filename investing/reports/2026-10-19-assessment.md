# Portfolio assessment — 2026-10-19

Decision support, not financial advice. Every level below is a mechanical/formula output; Shariah status must be verified in Zoya/Musaffa. Discovery ran on live Yahoo data.

## Verdicts (your rules resolving, not advice)
- **BMNR -> HOLD** (DEFAULT: no rule fired). Price 21.60, return +40.0%, weight 17.6%. Trailing stop 24.34 is **above** the current price (-12.7%), 6m momentum +15.4%, ATR 6.97% (vol-throttle: size down). Verdict.py did not fire a SELL on this — worth checking whether the stop/exit rule should trigger.
- **NOW -> HOLD** (VALUATION_RICH: P/E ~119, hold, do not add). Price 144.59, return +25.8%, weight 82.4%. Trailing stop 136.30 (5.7% below), 6m momentum +35.9%.
- Portfolio value $1,227.75. Concentration check muted (<4 names), but NOW is 82% of the account.

## Action flags (mandate first)
1. **BMNR Shariah:** recorded compliant (broker_app, 2026-07-07) but the screen is >100d old, and the ratio pre-check now **fails** (industry "Capital Markets" — core business knockout). Re-screen in Zoya/Musaffa now; do not add until resolved.
2. **NOW Shariah:** recorded compliant (2026-06-09), stale (>100d). Pre-check OK (debt 1.6%, liquid 4.2%). Re-screen.
3. NOW valuation: P/E ~119, rich.

## DCF (assumptions: 5y growth / terminal / discount)
- BMNR: intrinsic 0.72 vs 21.60 (-96.7%) at 5% / 2.5% / 10% — DCF is not meaningful for this business model.
- NOW: intrinsic 120.12 vs 144.59 (-16.9%) at 18% / 3% / 10%.

## PM records (mechanical proxies)
Both holdings: conviction LOW (BMNR: no reward:risk/thesis recorded; NOW: reward:risk -3.0:1 vs DCF target). Neither has a catalyst date or invalidation beyond `thesis_broken`. Supply a real thesis/variant view in the holding files.

## New ideas
recommend.py `ideas` array is empty — no planned, compliant cards, so **no BUY-CANDIDATE**. All leads are LEAD/RESEARCH. External web research on catalysts was not performed in this automated run; only dated catalysts from discovery are listed.

Top leads (leads.md, all UNVERIFIED Shariah): AEM (earnings 10-28), SNA (10-22), TSLA (10-21), BKR (10-27), GOOGL (10-28), TECK (10-29), PLTR (11-02), ADI (11-24), DDOG (11-04), FOX (11-02), ASND (no catalyst), LIF (11-09). See leads.md for entry/target/stop.

## Draft setup cards
New DRAFT cards scaffolded this run (status: draft, RESEARCH — awaiting your review; set `status: planned` to approve): AAPL,AEM,APA,ASND,BBY,BKR,DDOG,EXPE,FLYW,FRO,LLY,NBIX,NTAP,NTNX,PR,SNA,TECK,TS,XOM. Each carries a formula-derived entry/stop/target, earnings_plan default `exit_before`, and `shariah: unverified`. Some (e.g. NBIX) have no target because entry<=stop — edit before use.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; update holding files.
2. Decide on BMNR given price below its trailing stop and the failed business pre-check.
3. NOW is 82% of the account — your call on sizing.
4. Review drafts for names with near earnings (TSLA 10-21, SNA 10-22); if you trade, run /apply-trade.
