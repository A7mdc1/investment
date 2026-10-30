# Portfolio Assessment — 2026-10-30

Not financial advice. Decision support only; every call is yours. Shariah status here is a recorded broker-app screen or a mechanical pre-check, not a fatwa — verify in Zoya/Musaffa.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (23 new DRAFT cards; existing unchanged) → prices / shariah / dcf / signals / verdict / recommend. No data gaps. Web research was thin (see below). `journal.py` not run (no `transactions.csv`).

## Verdicts (YOUR rules resolving, not advice)
- **BMNR -> HOLD** (DEFAULT, no rule fired). $19.95, +29.3% vs $15.43 cost. Trailing stop $23.89 (price is *below* it, but verdict.py did not fire a stop rule — worth checking the rule config). 6m momentum +22.2%. Conviction LOW (mechanical proxy; no thesis/reward:risk on file).
- **NOW -> HOLD** (VALUATION_RICH, P/E ~119, hold, don't add). $104.41, **-9.2%** vs $114.97 cost. Trailing stop $136.61 — price ~24% below it; 15th percentile of 52w range. Conviction LOW (mechanical proxy).
- Portfolio notes: only 2 holdings (concentration muted); both ATR >7% — size down per vol throttle.

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $19.95 | 10 | $15.43 | $199.49 | +29.3% | 21.4% |
| NOW | $104.39 | 7 | $114.97 | $730.76 | -9.2% | 78.6% |
Total $930.26. NOW is ~79% of the account.

## Action flags (priority)
1. **Mandate:** both recorded Shariah screens are stale (>100d: NOW 2026-06-09, BMNR 2026-07-07). Re-screen both.
2. **BMNR ratio pre-check FAILS** again (industry "Capital Markets" — core business fails screen) while recorded status is "compliant". Unresolved since the 08-19 report; recommend.py's gate cannot see this. Do not add until re-screened.
3. **NOW fell ~10% today** (121.50 → ~109 close on 10-30 per Yahoo; 104.4 at run time). I could not confirm the cause: web search found no Q3 2026 earnings coverage. Pre-earnings note from Oct 13 had it at $139.71 with a positive Oppenheimer channel-check. Verify the news yourself before acting.
4. NOW valuation flag: P/E ~119.

## Per-holding read (no pick made)
- **NOW** — Keep: DCF $119.65 vs $104.41 (+14.6%; assumptions 18% 5y growth, 3% terminal, 10% discount); thesis (subscription growth, AI agents) not yet shown broken. Trim/review: price far under trailing stop, 79% concentration, high ATR, P/E still ~119, and a sharp drop whose cause is unconfirmed; thesis "what would change my mind" (growth < ~21% YoY or guidance cut) needs checking against the latest print.
- **BMNR** — Keep: +29% and positive 6m momentum. Trim/review: Shariah pre-check fail, stale screen, DCF ($0.72) does not fit an ETH-treasury business (ignore as signal), no thesis written. Sources are thin: one item (July) cites ~5.7M ETH held and a 9.5% Series A preferred; an undated listing suggests earnings ~2026-11-23 (unverified).

## Suggested actions from your rules
- Rule VALUATION_RICH fired (NOW) -> hold, do not add. Vol-throttle note fired for both -> size down on any add.
- No SELL/TRIM rules fired. If you execute anything, run /apply-trade.

## DCF
BMNR $0.72 vs $19.95 (-96.4%; growth 5%, terminal 2.5%, discount 10%) — model not meaningful here. NOW $119.65 vs $104.41 (+14.6%).

## New ideas
`recommend.py` ideas array is empty: no card is `planned` + compliant, so **no BUY-CANDIDATE**. Discovery leads (all LEAD/RESEARCH, Shariah UNVERIFIED), with near-term catalysts: FOX (R:R 13.3, earnings 11-02), FICO (20.0, 11-04), PAY (5.2, 11-02), EXPE (5.0, 11-04), LIF (5.2, 11-09). Many other leads have R:R < 2 (e.g. AAPL 0.4, XOM 0.1, FLYW 0.2) and fail the asymmetry bar. Full list: `leads.md`. Note ORCL-PD looks like a preferred share, not a common stock.

## Draft setups
23 new DRAFT cards scaffolded (aapl, apa, asnd, bby, ddog, expe, flyw, fro, fslr, hst, keys, lly, ntap, ntnx, nue, orcl-pd, pr, smtc, sna, stld, ts, txn, xom). All are formula-output proposals — RESEARCH, "DRAFT awaiting your review (set status: planned to approve)". Review levels in `setups/<ticker>.md`, edit what you disagree with, then flip status and screen in Zoya/Musaffa.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; resolve the BMNR Capital Markets conflict.
2. Check why NOW dropped; revisit its invalidation and fill `variant_view`/`initial_stop`/`target_price`.
3. Decide on NOW concentration (79%).
4. Triage the draft cards with near-term earnings first.
5. Check why BMNR/NOW at prices below trailing stop returned HOLD.

Not financial advice. Verify Shariah status in Zoya/Musaffa before acting.

Sources: [Nasdaq: ServiceNow shares fall 18% (Q1)](https://www.nasdaq.com/articles/servicenow-shares-fall-18-solid-earnings-fail-impress-investors), [Money365: Oppenheimer on Q3](https://www.money365.market/news/latest/servicenow-shares-fall-0-43-as-oppenheimer-cites-positive-q3-edd91149), [MarketBeat BMNR](https://www.marketbeat.com/earnings/reports/2026-7-14-bitmine-immersion-technologies-inc-stock/), [VT Markets BMNR](https://www.vtmarkets.com/zh-ca/discover/51413/)
