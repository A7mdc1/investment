# Portfolio Assessment — 2026-10-16

Not financial advice. Decision support only — every buy/sell/hold call is
yours. Shariah status below is the recorded broker-app screen or a mechanical
ratio pre-check, not a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 per `discover_top_n`) -> `scaffold.py
--all-leads` (20 new DRAFT cards; existing cards unchanged) -> `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py`, all
live, no data gaps. **Not done this run:** the per-holding live web research
(catalysts/news) was skipped — the automated routine ran without web search,
so no catalyst facts below are newer than the 2026-08-19 report. `journal.py`
not run (no `transactions.csv`).

## Verdicts (your rules resolving, not advice)

**BMNR -> HOLD** (DEFAULT — no rule fired). $21.82, +41.4% vs $15.43 cost.
- Trailing stop (chandelier) **$24.25 is ABOVE the live price ($21.81)** and
  EMA-fast is $24.47, yet no SELL rule fired. Worth checking how
  `verdict.py` treats price < trailing stop for a `core` holding — as written
  it did not trigger. Mechanical proxy only.
- Shariah: recorded compliant (broker app, screened 2026-07-07) but now
  **STALE (>100d)**. Ratio pre-check clean this run (liquid ratio 3.9%, debt
  rows unknown, business screen not evaluated). Last report's business-
  activity fail (industry "Capital Markets") did not reproduce in the
  pre-check this run — still unresolved; re-screen in Zoya/Musaffa.
- 6m momentum +4.1%; ATR 7.04% -> vol-throttle note: size down.
- PM record (mechanical): conviction LOW (no reward:risk / thesis on file);
  DCF $0.72 is a model mismatch for a crypto-treasury business — data gap,
  not a valuation call.

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 — hold, do not add). $140.49,
+22.2% vs $114.97 cost.
- Trailing stop $136.23 (~3.0% below price); 6m momentum +43.3%.
- Shariah: recorded compliant, screened 2026-06-09 — **STALE**, re-screen.
- DCF $120.12 vs $140.46 -> -14.5% (growth 18%, terminal 3%, discount 10%).
  Mechanical reward:risk -4.8:1 (target below price) -> conviction LOW.
- Next earnings ~2026-10-28 (12 days) — inside the catalyst window, with the
  stop only ~3% below price: a gap through the stop is the main risk.

Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $21.82 | 10 | $15.43 | $218.15 | +41.4% | 18.2% |
| NOW | $140.49 | 7 | $114.97 | $983.40 | +22.2% | 81.8% |

**Total value $1,201.55** (vs $1,105.51 on 2026-08-19).

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale** (BMNR 2026-07-07, NOW
   2026-06-09). Policy issue, not a price call. Re-screen both.
2. **[Price vs stop / BMNR]** Price below the computed trailing stop with a
   HOLD verdict — see above.
3. **[Catalyst / NOW]** Earnings ~2026-10-28 with a tight (~3%) trailing stop.
4. **[Valuation / NOW]** P/E ~119, DCF -14.5% — do not add.
5. **[Concentration]** NOW is 81.8% of the book (muted rule, 2 names).
6. **[Missing inputs]** BMNR has no thesis, variant view, stop, target or
   pre-mortem; NOW's `last_review` is 2026-06-15 (4 months old).

## Fired rules (from rules.md)

- NOW: VALUATION_RICH -> hold, do not add.
- Vol throttle: BMNR ATR 7.04% -> size down on any add.

## New ideas

Discovery returned 50 leads (see `leads.md`). `recommend.py` produced no
BUY-CANDIDATEs: all 83 setup cards are `draft` (one `planned`), and no card
carries a human-verified `shariah: compliant`, so every idea caps at
**RESEARCH — DRAFT awaiting your review (set status: planned to approve)**.
Top leads by mechanical reward:risk (formula outputs — proposals to review,
not buys; every level is a Yahoo-formula estimate):

| Ticker | R:R | Entry / Target / Stop | Catalyst |
|---|---|---|---|
| AEM | 20.0 | 187.13 / 251.18 / 185.41 | earnings |
| GOOGL | 15.1 | 341.26 / 408.21 / 337.48 | 2026-10-28 |
| SNA | 12.7 | 366.26 / 420.51 / 361.98 | earnings |
| LIF | 10.6 | 40.70 / 56.75 / 39.19 | earnings |
| BKR | 8.3 | 55.80 / 69.92 / 54.10 | earnings |
| UTHR | 7.3 | 535.93 / 609.02 / 526.06 | earnings |

Very high R:R values with stops <1% from entry (AEM, SNA, GOOGL) are
artifacts of tight formula stops — expect gap-through-stop risk. New DRAFT
cards this run: AAPL, AEM, APA, BBY, BKR, DDOG, EXPE, FLYW, FRO, FSLR, HPE,
LLY, NTAP, NTNX, PBF, PR, SNA, TECK, TS, XOM. Edit what you disagree with,
screen in Zoya/Musaffa, then set `status: planned`.

## Follow-ups

1. Re-screen BMNR and NOW in Zoya/Musaffa; update `holdings/*.md`.
2. Decide how to handle NOW into the ~10-28 earnings (gap risk vs ~3% stop).
3. Fill in BMNR's thesis/stop/target; review the `verdict.py` price<stop case.
4. Review any DRAFT cards of interest; screen before promoting.
5. If you execute anything, run `/apply-trade`.

Not financial advice. Verify Shariah status independently in Zoya/Musaffa.
