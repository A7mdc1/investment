# Portfolio Assessment — 2026-11-07

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status is the broker app's recorded screen or a mechanical pre-check,
neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (20 new DRAFT
cards, existing cards unchanged) → `prices / shariah / dcf / signals / verdict /
recommend` (all live, no data gaps). **Not done this run:** per-holding web
research on upcoming catalysts and thesis-breaking news (unattended run); the
catalyst fields below are therefore only what is recorded in the holdings files.
`journal.py` skipped — no `transactions.csv`.

## Verdicts (your rules resolving, not advice)
| Ticker | Verdict | Rule | Price | Return | Weight | Trailing stop | 6m mom |
|---|---|---|---|---|---|---|---|
| BMNR | HOLD | DEFAULT | $18.76 | +21.6% | 20.8% | $20.12 (**price is ~6.8% below it**) | +8.4% |
| NOW | HOLD | VALUATION_RICH (P/E ~119 ≥ 50; hold, do not add) | $101.97 | −11.3% | 79.2% | $136.54 (**price is ~25% below it**) | +53.3% |

Total value **$901.39**. Portfolio notes: BMNR ATR 7.94% and NOW ATR 7.5% — size
down per the vol throttle; concentration check muted (< 4 names).

PM-grade record (mechanical proxies only): both conviction LOW (no reward:risk or
thesis input); BMNR DCF $0.72 (−96%, DCF does not fit a crypto-treasury business);
NOW DCF $119.65 (+17.3%; growth 18%, terminal 3%, discount 10%).

## Action flags (priority order)
1. **Shariah — both recorded screens are stale.** BMNR screened 2026-07-07, NOW
   2026-06-09 (>100 days) → re-screen both in Zoya/Musaffa.
2. **BMNR ratio pre-check still FAILS** (industry `Capital Markets` = core-business
   knockout) against a recorded "compliant" status. Unresolved since the 08-19
   report. Compliance is a gate: do not add until re-screened.
3. **Stops vs verdicts look inconsistent — please check.** Both prices sit below
   the computed chandelier trailing stop, yet verdict.py returns HOLD (NOW: 25%
   below; BMNR: 6.8% below). Either the stop is being computed from a stale high
   or the SELL trigger isn't comparing price to it. Worth a look at `verdict.py`
   before relying on it. (Not investigated this run.)
4. NOW valuation: P/E ~119 rich; price at 13% of its 52-week range.
5. Both holdings lack `initial_stop`, `target_price`, `invalidation`, `variant_view`.

## Per-holding read
- **BMNR** — Keep: +21.6% vs cost, 6m momentum positive. Trim/exit: below trailing
  stop, ratio pre-check fails, compliance screen stale, no written thesis/stop.
- **NOW** — Keep: DCF $119.65 above price, strong momentum score, durable
  subscription growth per your thesis note. Trim/exit: −11.3% vs cost, 79% of the
  account in one name, rich P/E, price far under trailing stop, last review
  2026-06-15 (needs re-underwrite). Catalyst date still unset in the card.

## Suggested actions (from YOUR rules.md)
- VALUATION_RICH fired on NOW → pre-set action: hold, do not add.
- No other rule fired. If you execute anything, run `/apply-trade`.

## New ideas
No lead clears to BUY-CANDIDATE: `recommend.py` returned no ideas, and every lead
is RESEARCH/LEAD (EDGE unsupplied, Shariah UNVERIFIED). Top leads by discovery
rank, all formula-level and unscreened: CDE (R:R 16.2, earnings 2027-02-17),
LIF (4.8, earnings 2026-11-09), DLO (5.5, 2026-11-12), KGC (12.1), FICO (20.0),
FSLR (6.5), AGI (4.9), GDDY (3.5). Several rows show `n/a` or odd R:R (stop above
entry, e.g. P, DELL, NTAP, FRO) — treat those levels as unreliable. Full list: `leads.md`.

## Draft setups (awaiting your review — set `status: planned` to approve)
20 new DRAFT cards this run: aapl, aem, anet, apa, asnd, bby, fro, fslr, keys, lly,
ntap, ntnx, pr, psx, smtc, sna, ts, txn, vlo, xom (plus earlier drafts in `setups/`).
All levels are Yahoo formula outputs — proposals, never buys; `shariah` stays
`unverified`. Open each card for entry/stop/target, logic, invalidation, gap plan.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; resolve the BMNR business-activity fail.
2. Check the trailing-stop vs verdict inconsistency (flag 3).
3. Fill thesis/stop/target/invalidation on both holdings; set NOW catalyst date.
4. Review near-dated drafts (LIF 11-09, DLO 11-12) only if you intend to trade them.

Not financial advice. Verify all Shariah status in Zoya/Musaffa.
