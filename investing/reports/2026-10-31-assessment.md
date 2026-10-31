# Portfolio assessment — 2026-10-31

Decision support only, not financial advice. Verify all Shariah status in Zoya/Musaffa.
Verdicts below are YOUR rules.md resolving, not recommendations. Web catalyst research was
NOT performed in this automated run; no catalysts are asserted beyond what the scripts/leads show.

## Snapshot
Total value $937.64.

| Ticker | Price | Cost | Return | Weight |
|---|---|---|---|---|
| NOW | 105.12 | 114.97 | -8.6% | 78.5% |
| BMNR | 20.18 | 15.43 | +30.8% | 21.5% |

## Action flags (mandate first)
1. **BMNR — Shariah ratio pre-check FAILS**: Yahoo industry "Capital Markets" matches the core-business knockout. Recorded status is "compliant" (broker_app, 2026-07-07) but the screen is >100d stale. Re-screen in Zoya/Musaffa now; the knockout is absolute if confirmed.
2. **NOW — Shariah screen stale** (2026-06-09, >100d). Ratio pre-check passes (debt 2.2%, liquid 5.8%). Re-screen.
3. NOW valuation: P/E ~119 — "hold, do not add" (VALUATION_RICH).
4. Both names ATR ~7.2% > 6% vol-throttle: size-down note.
5. Concentration cap (22%) is muted (<4 names), but NOW is 78.5% of the book.

## Verdicts
- BMNR -> HOLD (DEFAULT: no rule fired). Trailing stop 23.86, EMA20 22.77, 6m mom +22.2%.
- NOW -> HOLD (VALUATION_RICH: hold, do not add). Trailing stop 136.60, EMA20 139.82, 6m mom +51.1%.

**Data oddity to check:** both prices sit well below their computed trailing stops (BMNR 20.18 vs 23.86; NOW 105.12 vs 136.60) yet verdicts are HOLD. NOW's stop/EMA look inconsistent with a 105 price (possible split-adjustment mismatch in history, or stop logic not firing on a gap). Verify before relying on the stop levels.

PM-grade proxies (mechanical, not a real conviction call): both LOW conviction (no reward:risk or stated variant view); `would_buy_today` true for both by proxy.

## DCF (assumptions: growth_5y / terminal / discount)
- NOW: intrinsic $119.65 vs $105.12 (+13.8%); 18% / 3% / 10%.
- BMNR: intrinsic $0.72 vs $20.18 (-96.4%); 5% / 2.5% / 10%. DCF is not meaningful for this business model; ignore.

## Per-holding read
- **BMNR**: Case to keep: +30.8% gain, positive 6m momentum. Case to trim/exit: pre-check business-knockout flag, stale screen, price below trailing stop, no thesis recorded.
- **NOW**: Case to keep: DCF +13.8%, strong 6m momentum, durable subscription thesis (last reviewed 2026-06-15). Case to trim: -8.6% vs cost, 78.5% of book, P/E ~119, below trailing stop/EMA20, stale thesis review.

## New ideas
discover.py refreshed `leads.md` (top 50; Yahoo reachable this run). `recommend.py` returned no mechanical idea records (ideas array empty). Every lead is LEAD/RESEARCH only: no card is `planned`, none Shariah-verified, so **no BUY-CANDIDATE**. Highest stated reward:risk among leads (formula outputs, unverified): FICO 20.0:1 (earnings 2026-11-04), HSY 20.0:1 (earnings 2027-02-04), FOX 13.4:1 (earnings 2026-11-02), ORCL-PD 13.1:1 (no dated catalyst), SNA 11.9:1, BKR 9.6:1. Earnings inside the window need a valid gap plan (stops do not execute through gaps).
New DRAFT cards scaffolded: HSY, ORCL-PD (status: draft, shariah unverified). Review and edit before setting `status: planned`.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; update `shariah` on the holding files.
2. Investigate the price-vs-trailing-stop inconsistency.
3. Decide on NOW concentration (78.5%) — your call.
4. Review new draft cards (HSY, ORCL-PD) if interested.
5. If you execute anything, run /apply-trade.

Not financial advice. Short-term trading usually trails buy-and-hold after costs; consider lower turnover.
