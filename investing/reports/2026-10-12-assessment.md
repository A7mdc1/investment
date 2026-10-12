# Portfolio assessment — 2026-10-12

Decision support, not financial advice. Verdicts below are your own `rules.md`
resolving mechanically. Shariah status must be verified in Zoya/Musaffa.
Web catalyst research was **not performed** this run (automated run); catalyst
dates below come only from Yahoo earnings data via discover.py. Yahoo was partly
rate-limited (HTTP 429/401 on crumb/earnings calls) — prices, DCF and discovery
completed; some earnings-date lookups failed.

## Verdicts
- **BMNR -> HOLD** (DEFAULT: no rule fired). $23.85, +54.6% vs $15.43 cost, 19.4% weight.
  Trailing stop $24.06 — **price is $0.20 (0.8%) BELOW it**; TRAIL_STOP does not fire
  because the holding is `trade_type: core`. EMA20 $25.35 (price below). 6m mom +16.4%.
  ATR 6.71% -> vol-throttle note (size down).
- **NOW -> HOLD** (VALUATION_RICH: P/E ~119, hold, do not add). $141.16, +22.8% vs $114.97,
  80.6% weight. Trailing stop $131.48 (6.9% below). EMA20 $137.00. 6m mom +48.8%.

PM records (mechanical proxies, not a conviction call): both conviction LOW.
NOW reward:risk -2.2:1 (DCF $120.12 vs price, -14.9%; growth 18%, terminal 3%, 10% discount).
BMNR has no R:R; DCF $0.72 (-97%) is not meaningful for an ETH-treasury company
(default 5% growth assumption, no override in holding file).

## Snapshot
Total $1,226.53 — NOW $987.98 (80.6%), BMNR $238.55 (19.4%). Only 2 names, so
concentration rule is muted (needs >= 4); NOW is above the 22% `max_position_pct`
cap in spirit — your call.

## Action flags (priority order)
1. **[Mandate] BMNR Shariah mismatch**: shariah.py ratio pre-check flags industry
   "Capital Markets" (core business fails screen), while the card records
   `compliant` (broker_app, 2026-07-07). Same flag as the 2026-08-19 report. Re-screen
   in Zoya/Musaffa. COMPLIANCE_GATE reads only the recorded status, so it won't fire.
2. **[Mandate] NOW screen is stale**: recorded 2026-06-09 (>100 days). Re-screen.
3. **[Risk] BMNR below trailing stop** (see above). Your rules call it HOLD only
   because it is tagged `core`; if it's really a momentum/swing position, the tag decides the verdict.
4. **[Housekeeping] Reviews overdue**: NOW `last_review` 2026-06-15 (119 days >
   `review_cadence_days` 90). BMNR has no thesis, catalyst, stop, target or
   last_review fields — PM record is empty.
5. **[Valuation] NOW** P/E ~119, DCF below price.

## Suggested actions (from YOUR rules)
- VALUATION_RICH fired -> NOW: hold, do not add (P/E ~119).
- Vol throttle -> BMNR: ATR 6.71% > 6% — size down.
- No SELL/TRIM/REVIEW rule fired. If you execute anything, run /apply-trade.

## New ideas
`recommend.py` ideas array is empty (watchlist.md has no cleared names). No
BUY-CANDIDATE. Discovery produced 50 LEADS (leads.md refreshed; pool 159 names).
Every lead is Shariah UNVERIFIED with EDGE not supplied.

Top leads (reward:risk is a formula output, often inflated by very tight
ATR-based stops — treat the stop distance as the real risk):
| Ticker | R:R | Entry / Target / Stop | Earnings |
|---|---|---|---|
| AR (card) | 16.1 | 36.41 / 45.75 / 35.84 | 2026-10-28 |
| SIMO (card) | 13.2 | 247.89 / 354.12 / 246.65 | 2026-10-28 |
| AEM (new draft) | 20.0 | 188.68 / 249.43 / 186.39 | 2026-10-28 |
| SNA (new draft) | 19.4 | 363.50 / 420.23 / 363.47 | 2026-10-22 |
| BKR (new draft) | 17.2 | 56.38 / 69.94 / 55.58 | 2026-10-27 |
| FN (new draft) | 20.0 | 454.75 / 684.60 / 446.04 | 2026-11-02 |
| DOCN (card) | 11.8 | 129.54 / 187.47 / 124.64 | 2026-11-04 |
| EXPE (new draft) | 10.7 | 269.57 / 341.66 / 262.80 | 2026-11-04 |
Full list: `leads.md`. Several stops sit within ~0.1–1% of entry (e.g. SNA $363.47
vs $363.50), so a normal tick would stop you out — review before trusting any R:R.

## Draft & planned setups
21 new DRAFT cards scaffolded this run (all `status: draft`, `shariah: unverified`):
AAPL, AEM, APA, BKR, DDOG, EXPE, FLYW, FN, HBM, HPE, JBL, LLY, NUE, PBF, PR,
SMCIP, SMTC, SNA, TECK, TS, XOM.
Each: RESEARCH — DRAFT awaiting your review (set status: planned to approve).
Example, AEM: earnings_run, enter ~$188.66 ahead of 2026-10-28 print, stop $186.39
(chandelier HH22 - 3x ATR), T1 $192.06 (1.5R), T2 $195.46 (3R), exit_before the
print (machine default), invalidation = no drift 5 sessions pre-print / give-back
> 1 ATR. All levels are formula outputs; edit what you disagree with.
Note: the AEM draft's T1 target ($192.06) is far below the lead-table target
($249.43) — the card uses R-multiples, the lead uses a structure target.
SMCIP looks like a preferred share (earnings lookup failed, "possibly delisted") —
likely not a meaningful tradeable lead. ORCL-PD likewise.
Existing planned/live cards: unchanged; none is BUY-CANDIDATE (none has a fresh
human `compliant` screen verified this run).

## DCF
NOW $120.12 vs $141.16 (-14.9%); BMNR $0.72 vs $23.85 (-97%, not meaningful).
Assumptions listed under Verdicts.

## Follow-ups
1. Re-screen BMNR (business-line flag) and NOW (stale) in Zoya/Musaffa.
2. Decide BMNR's trade_type and fill its thesis/stop/target — it is under its trailing stop.
3. Refresh NOW's review (overdue 29 days).
4. Review the 21 draft cards; delete junk (SMCIP) and flip chosen ones to `planned`.
5. Earnings cluster 2026-10-22 to 10-30 (SNA, BKR, AEM, AR, SIMO, GDDY, ARW, FORM, CLS) —
   gap plan required before any hold-through.
6. Short-term trading usually trails buy-and-hold after costs; keep turnover low.

Not financial advice. Verify every name in Zoya/Musaffa.
