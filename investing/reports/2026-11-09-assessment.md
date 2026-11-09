# Portfolio Assessment — 2026-11-09

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status is the broker app's recorded screen or a mechanical pre-check, not a
fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo; top 50 leads written to `leads.md`) → `scaffold.py --all-leads`
(25 new DRAFT cards; existing cards unchanged) → `prices`, `shariah`, `dcf`, `signals`,
`verdict`, `recommend` (all live; Yahoo logged some 401/429 crumb warnings on
sub-calls but every script returned data). **No web catalyst research was done this
run** (automated run) — catalyst dates below come only from the scripts. `journal.py`
not run (no `transactions.csv`).

## Verdicts
**BMNR -> HOLD** (DEFAULT, no rule fired). $18.92, +22.6% vs $15.43 cost. Trailing
stop $20.11 (price is *below* it, but `trade_type: core` exempts it from TRAIL_STOP);
6m momentum +4.4%. Conviction LOW (mechanical proxy — no thesis/stop/target in file).

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 — hold, do not add). $104.37, **-9.2%** vs
$114.97 cost. Trailing stop $137.08 (price ~24% below; core exempt); 6m momentum +54.0%
(script value, looks inconsistent with price being near the 52w low — treat with
caution). Conviction LOW (mechanical).

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $18.92 | 10 | $15.43 | $189.18 | +22.6% | 20.6% |
| NOW | $104.37 | 7 | $114.97 | $730.61 | -9.2% | 79.4% |

Total **$919.80** (down from $1,105.51 on 2026-08-19). NOW is 79% of the book.

## Action flags
1. **[Mandate] Both Shariah screens are stale** (>100 days): BMNR screened 2026-07-07,
   NOW 2026-06-09. Re-screen in Zoya/Musaffa. The ratio pre-check passed for both this
   run (BMNR's industry/business check returned no data: `business_ok: null`, no debt
   rows; the 2026-08-19 run flagged BMNR's business activity as 'Capital Markets' —
   that question is still open and unresolved by the recorded field).
2. **[Concentration/Vol]** NOW 79% of the book; ATR 7.2% (NOW) and 7.9% (BMNR) —
   vol-throttle notes say size down.
3. **[Valuation / NOW]** P/E ~119 rich; price at ~15th percentile of 52w range.
4. **[PM records incomplete]** Neither holding has conviction, variant view, stop,
   target or pre-mortem filled in (owner fields).

## DCF
| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $18.91 | -96.2% | 5%/2.5%/10% defaults — model doesn't fit a crypto-treasury business; data gap, not a valuation call |
| NOW | $119.65 | $104.38 | +14.6% | growth 18%, terminal 3%, discount 10% |

## Suggested actions (your rules)
- VALUATION_RICH fired -> NOW: hold, do not add.
- Stale Shariah screens -> re-screen both (recommend.py shows status REVIEW).
- No other rules fired. If you execute anything, run `/apply-trade`.

## New ideas
`watchlist.md` empty. `recommend.py` ideas: **0 BUY-CANDIDATE** (no card is
`status: planned`).

## Leads / draft setups (50 leads, 25 new DRAFT cards)
Only 3 of 50 clear to LEAD tier; the rest are capped at RESEARCH by asymmetry/catalyst gates.

| Ticker | Tier | Card | R:R | Catalyst |
|---|---|---|---|---|
| LIF | LEAD | existing | 11.8:1 | earnings 2026-11-09 (today) |
| ADI | LEAD | existing | 5.1:1 | earnings 2026-11-24 |
| DLO | LEAD | existing | 3.6:1 | earnings 2026-11-12 |

Notable RESEARCH-tier by R:R (levels are formula outputs, not predictions): FSLR 20.0:1,
FICO 18.6:1, HL 18.3:1, FTI 12.4:1, DIOD 8.3:1, LSCC 7.9:1. Several rows show
"n/a" R:R or stop above entry (e.g. DELL, NTAP, KLIC, ASTS) — formula artifacts to
review before trusting those cards. Full table with entry/target/stop: `leads.md`;
new cards are in `setups/` as `status: draft`, Shariah `unverified`. Approval = you
edit and set `status: planned`, and screen in Zoya/Musaffa.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa (both stale; BMNR business-activity open).
2. Decide on NOW sizing (79% weight, -9% vs cost) and fill in stop/target/invalidation.
3. Review LIF/ADI/DLO draft cards ahead of their earnings dates.

*Not financial advice. Verify Shariah status in Zoya/Musaffa.*
