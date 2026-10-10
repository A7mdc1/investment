# Portfolio Assessment — 2026-10-10

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status is the broker app's recorded screen or a mechanical pre-check,
neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (new DRAFT
cards: AAPL, AEM, AMKR, APA, DDOG, EXPE, FN, HBM, JBL, SMTC, … ; existing cards
untouched) → `prices / shariah / dcf / signals / verdict / recommend` — all live.
Crumb fetch was rate-limited (HTTP 429) but data returned. **Web catalyst research
was not performed this run** (automated run); no catalysts below beyond the dated
earnings in `leads.md` / the data. `journal.py` not run — no `transactions.csv`.

## Verdicts (your rules resolving, not advice)
| Ticker | Verdict | Price | vs cost | Weight | Trailing stop | 6m mom |
|---|---|---|---|---|---|---|
| BMNR | HOLD (DEFAULT) | $24.03 | +55.7% | 19.6% | $23.96 (**0.3% away**) | +13.7% |
| NOW | HOLD (VALUATION_RICH, P/E ~119 — hold, do not add) | $140.86 | +22.5% | 80.4% | $131.36 (6.7% away) | +58.0% |

Portfolio value $1,226.32. Portfolio note: BMNR ATR 6.79% > 6% — size-down per vol
throttle. Concentration check muted (< 4 names), but NOW is 80% of the book vs
`max_position_pct: 22` — that rule is dormant only because of the small-book carve-out.

Mechanical PM proxies (not a conviction call): both LOW conviction — DCF-derived
targets sit below price (BMNR $0.72, NOW $120.12 = −14.7%; DCF assumptions: growth
5%/18%, terminal 2.5%/3%, discount 10%). The BMNR DCF does not fit a crypto-treasury
business and should be ignored as a valuation.

## Action flags (priority order)
1. **BMNR — Shariah mismatch (policy flag).** Recorded `compliant` (broker app,
   2026-07-07) but the mechanical business pre-check fails: industry `Capital Markets`.
   Re-screen in Zoya/Musaffa. This was also flagged 2026-08-19 and remains unresolved.
2. **NOW — screen stale.** Recorded compliant 2026-06-09, now >100 days old. Re-screen
   before any add (ratio pre-check itself is clean: debt 1.7%, liquid 4.3%).
3. **BMNR — price within 0.3% of its chandelier stop** ($23.96) and below its 20-EMA
   ($25.51). A close below the stop/EMA is when your REVIEW/SELL rules would fire.
4. NOW — valuation: P/E ~119, rich.

## Suggested actions (from YOUR rules)
No SELL/TRIM rule fired. VALUATION_RICH on NOW → hold, do not add. Vol-throttle note
on BMNR. If you execute anything, run `/apply-trade` so holdings + ledger update.

## New ideas
`recommend.py` `ideas` array is empty: no planned setup card carries a fresh
human-verified `shariah: compliant`, so nothing can be BUY-CANDIDATE. All 50 leads
are LEAD/RESEARCH; every DRAFT card is Shariah-UNVERIFIED. Highest-ranked leads by
the mechanical score with dated catalysts inside 60 days (formula outputs only):
LRCX (earnings 10-21), ALAB (11-03), AEM (10-28, no card until now), TER (10-21),
KLIC (11-18), TTMI/MKSI (11-04). Several show implausible reward:risk (15–20:1)
because stop ≈ entry; treat those levels with skepticism. DELL (score 72.1), DINO,
NET, SMTC, DDOG have R:R < 1 → cannot clear the asymmetry gate.

## Draft setups
All new/existing DRAFT cards: `RESEARCH — DRAFT awaiting your review (set status:
planned to approve)`. Every level (entry/stop/target, chandelier stop, 1.5R/3R targets)
is a formula output; edit what you disagree with, flip `status: planned`, and screen
in Zoya/Musaffa. See `setups/<ticker>.md`.

## Follow-ups
1. Re-screen BMNR (business-activity) in Zoya/Musaffa — decide on the mismatch.
2. Re-screen NOW; update `shariah.screened` in `holdings/now-servicenow.md`.
3. Decide BMNR plan if it closes under $23.96.
4. Consider whether NOW's 80% weight fits your intent.
5. Review draft cards only for names you'd actually trade.

Not financial advice. Verify Shariah status in Zoya/Musaffa.
