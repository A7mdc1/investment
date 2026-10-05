# Portfolio Assessment — 2026-10-05

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status is a recorded broker-app screen or a mechanical pre-check, not a
fatwa — verify in Zoya/Musaffa before acting.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (15 new DRAFT
cards: AAPL, AMKR, APA, BLSH, CORZ, FLYW, FN, HBM, JBL, LLY, NUE, PR, TECK, TS, XOM)
→ `prices` / `shariah` / `dcf` / `signals` / `verdict` / `recommend`. Yahoo returned
live data (one crumb 429, non-blocking). **Not done:** per-holding web catalyst
research (no web tool in this scheduled run) — catalyst dates below come only from
Yahoo/discovery. `journal.py` not run; no `transactions.csv`.

## Verdicts (your rules resolving, not advice)
**BMNR -> HOLD** (DEFAULT). $26.33, +70.7% vs $15.43 cost. Trailing stop $23.62
(~10% below); 6m momentum +28.4%; ATR 6.63% — vol-throttle note: size down.
- Mechanical proxies: conviction LOW (DCF target $0.72 < price; the DCF does not fit a
  crypto-treasury business — ignore its R:R of -9.4).
- **Shariah conflict still open:** recorded `compliant` (broker app, 2026-07-07), but
  the ratio pre-check FAILS (industry "Capital Markets" = core-business flag). Same
  flag as 2026-08-19 — a Zoya/Musaffa re-screen is still outstanding.

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 — hold, do not add). $135.50, +17.9% vs
$114.97. Trailing stop $129.75 (~4.3% below); 6m momentum +42.1%.
- DCF $120.12 vs $135.50 → -11.4% (assumptions: 18% 5y growth, 3% terminal, 10% discount).
- **Shariah record is STALE** (screened 2026-06-09, >100d) — re-screen needed (mandate flag).
- `last_review` 2026-06-15 is also old.

Portfolio: only 2 holdings; concentration rules muted (<4 names).

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.33 | 10 | $15.43 | $263.35 | +70.7% | 21.7% |
| NOW | $135.50 | 7 | $114.97 | $948.50 | +17.9% | 78.3% |
Total $1,211.85. NOW is 78% of the book.

## Action flags (priority)
1. Mandate: BMNR ratio pre-check fails vs recorded compliant — re-screen.
2. Mandate: NOW Shariah screen stale — re-screen.
3. Valuation: NOW P/E ~119 rich.
4. NOW concentration (78%) — informational while <4 names.

## Suggested actions (your rules)
- VALUATION_RICH fired on NOW -> your pre-set action: hold, do not add.
- BMNR vol-throttle note -> size down on any add.
If you execute anything, run /apply-trade.

## New ideas
Top-50 leads in `leads.md`; all are **LEAD/RESEARCH** — none BUY-CANDIDATE (no
planned + human-compliant card). Highest mechanical R:R with dated catalysts (formula
outputs, thin stops make R:R look inflated — treat skeptically): CORZ 20:1 (earn.
10-23), BLSH 20:1 (11-12), GDDY 17.2:1 (10-29), ASTS 14.3:1 (11-09), JBL 11.6:1
(12-16), WDC 10.4:1 (11-05), IONQ 10.0:1 (11-04). Earliest catalysts: HAS 10-20,
TSLA/LRCX 10-21, CORZ 10-23. Crypto/AI-miner names (CORZ, BLSH) carry the same
business-screen risk as BMNR. Every name needs a Zoya/Musaffa screen first.

## Draft & planned setups
15 new DRAFT cards (list above) plus existing drafts — each is a formula-built
proposal: RESEARCH — DRAFT awaiting your review (set status: planned to approve).
Levels are mechanical; edit what you disagree with. No planned/live cards gate through.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; update the cards.
2. Decide whether NOW's 78% weight is acceptable.
3. Review drafts for names with catalysts in the next 3 weeks (HAS, TSLA, LRCX, CORZ, GDDY).
4. Record any trade via /apply-trade.

Not financial advice; verify Shariah status in Zoya/Musaffa.
