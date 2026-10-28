# Portfolio Assessment — 2026-10-28

Not financial advice. Decision support only — every buy/sell/hold call is yours. Shariah status below is the recorded broker-app screen or a mechanical pre-check, not a fatwa; verify in Zoya/Musaffa.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (25 new DRAFT cards) → `prices / shariah / dcf / signals / verdict / recommend`. No data gaps. `journal.py` not run (no `transactions.csv`; discipline guard dormant). `recommend.py` returned no new-idea records (`ideas` empty), so there are no BUY-CANDIDATEs this run.

## Verdicts
| Ticker | Verdict | Price | Return | Weight | Trailing stop | 6m mom |
|---|---|---|---|---|---|---|
| BMNR | HOLD (DEFAULT) | $21.26 | +37.8% | 16.8% | $23.91 (price is *below* it) | +29.4% |
| NOW | HOLD (VALUATION_RICH, P/E ~119) | $150.23 | +30.7% | 83.2% | $141.90 (5.5% below price) | +46.2% |

These are your own rules resolving, not advice. recommend.py proxies: BMNR conviction LOW (no stated thesis / reward:risk); NOW conviction LOW (reward:risk -3.6:1). Portfolio note: BMNR ATR 6.73% — vol throttle says size down. Total value **$1,264.21**.

## Action flags
1. **[Mandate] BMNR ratio pre-check still FAILS** — industry "Capital Markets" ("core business fails screen") vs recorded `compliant` (broker app, 2026-07-07, now **stale**). Flagged last run (2026-08-19) and still unresolved. Per Gate 1 a confirmed fail is a hard SELL regardless of return. Re-screen the business activity in Zoya/Musaffa.
2. **[Mandate] NOW Shariah record is stale** (screened 2026-06-09). Pre-check clean (debt 1.5%, liquid 4%).
3. **[Catalyst — today] NOW reports Q3 2026 after the close today (Oct 28)** ([company release](https://investor.servicenow.com/news/news-details/2026/ServiceNow-to-Announce-Third-Quarter-2026-Financial-Results-on-October-28/default.aspx)). NOW is 83% of the book; last quarter the stock fell 3.7% after the print. The card/holding has no earnings gap plan — a stop will not execute through an overnight gap (rules assume a ~25% adverse gap for sizing).
4. **[Concentration]** NOW 83% vs `max_position_pct` 22 — muted only because the book has <4 names.
5. **[BMNR trend]** Price $21.26 is under the $23.91 chandelier stop and EMA20 ($23.11); verdict.py did not fire because trade_type is `core` with no stop recorded. Next earnings est. 2026-11-23 (unconfirmed, third-party calendar). No Oct 2026 company news found in search.

## DCF (assumptions shown)
- NOW: $120.12 vs $150.23 → -20.0% (growth 18%/5y, terminal 3%, discount 10%).
- BMNR: $0.72 → -96.6% (5%/2.5%/10%). Model does not fit a crypto-treasury business; treat as a data gap.

## Suggested actions (rules fired)
- VALUATION_RICH (NOW): hold, do not add.
- Vol throttle (BMNR): size down.
- Nothing mechanical forces a SELL/TRIM. If you execute anything, run /apply-trade.

## New ideas
`leads.md` refreshed: 50 leads, 20 at LEAD tier, rest RESEARCH (asymmetry/catalyst gates). All are **LEAD/RESEARCH only** — EDGE not supplied, Shariah UNVERIFIED. Top by rank, all with earnings inside ~2 weeks (binary-event risk): GDDY, AEM, FOX, AGI, PAY, KGC, FSLR, EXPE, CORZ. Several quoted R:R values (≈18–20:1) come from very tight formula stops and should be treated skeptically.

### Draft setups (proposals to review, never buys)
25 new DRAFT cards, each `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`: AEM, ALL, AMG, APA, BBY, BKR, CORZ, DDOG, EVR, EXPE, FLYW, FRO, FSLR, HPE, HST, JBL, NTAP, NTNX, PNFP, PR, SMTC, SNA, STLD, TECK, TS. Every level is a Yahoo formula output; approve by editing what you disagree with and setting `status: planned` after a Zoya/Musaffa screen. No planned/live cards exist.

## Follow-ups
1. Decide on NOW before/after tonight's print; consider whether to record a gap plan and stop.
2. Re-screen BMNR in Zoya/Musaffa (business activity) and refresh NOW's screen date.
3. Record a stop/thesis on BMNR (price below its computed trailing stop).
4. Review the draft cards you care about; ignore the rest.

*Not financial advice. Verify Shariah status in Zoya/Musaffa.*
