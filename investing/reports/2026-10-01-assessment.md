# Portfolio Assessment — 2026-10-01

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is the broker app's recorded screen or a mechanical
ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads written to `leads.md`) →
`scaffold.py --all-leads` (14 new DRAFT cards: AAPL, AMKR, BLSH, DDOG, DDS, FLYW,
FN, HBM, HPE, LLY, NTAP, NTNX, TS, XOM; existing cards unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py`, all live,
no data gaps. **Not done this run:** per-holding web catalyst research (unattended
scheduled run) — catalyst fields below come from the files only. `journal.py` not
run (no `transactions.csv`).

## Verdicts (your rules resolving, not advice)

**BMNR -> HOLD** (RULE: DEFAULT). $26.68, **+72.9%** vs $15.43 cost. Trailing stop
$23.67 (~11.3% below). 6m momentum +18.7%. R-multiple n/a.
**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 — hold, do not add). $136.63,
**+18.8%** vs $114.97. Trailing stop $129.40 (~5.3% below). 6m momentum +37.4%.

Mechanical PM proxies (not a real conviction call): both LOW conviction. Their
reward:risk is negative only because the target is the DCF value (BMNR $0.72, NOW
$120.12), which sits below price; no thesis-based target is recorded for either.
Portfolio note: BMNR ATR 6.49% — size down per vol throttle. Only 2 holdings, so
concentration rules are muted.

## Snapshot (live)

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.67 | 10 | $15.43 | $266.65 | +72.8% | 21.8% |
| NOW | $136.66 | 7 | $114.97 | $956.62 | +18.9% | 78.2% |

**Total $1,223.27** (up from $1,105.51 on 2026-08-19). NOW is 78% of the book.

## Action flags (priority order)

1. **[Mandate] BMNR ratio pre-check still FAILS** — industry `Capital Markets`
   matches the business-activity knockout; this conflicts with the recorded
   `compliant` (broker app, 2026-07-07). Flagged on 2026-08-19 and still unresolved;
   the position has since risen ~30%. Re-screen in Zoya/Musaffa. `recommend.py` reads
   only the recorded field, so it still shows PASS.
2. **[Mandate — NEW] NOW's Shariah screen is stale** (screened 2026-06-09, >100
   days). `recommend.py` shows REVIEW. Pre-check is clean (debt 1.7%, liquid 4.4%,
   business OK). Re-screen and update the record.
3. NOW valuation: P/E ~119 rich; DCF $120.12 vs $136.66 (-12.1%).

## Per-holding read

- **BMNR**: case to keep — trend intact (above EMA, +18.7% 6m momentum), stop well
  below. Case to trim/exit — compliance question is open (flag 1), DCF doesn't fit a
  crypto-treasury business, no thesis/invalidation recorded, high ATR, large gain
  unprotected by a written plan. Your call.
- **NOW**: case to keep — strong momentum, durable subscription growth per recorded
  thesis, stop distance only ~5%. Case to trim — rich multiple, price above DCF,
  78% concentration, `last_review` is 2026-06-15 and the catalyst has no date.

## Rules fired

- VALUATION_RICH (NOW) -> hold, do not add.
- Vol throttle (BMNR) -> size down on any add.
If you execute anything, run /apply-trade so holdings + ledger update.

## DCF (assumptions visible)

| Ticker | Intrinsic | Price | vs price | Growth 5y / terminal / discount |
|---|---|---|---|---|
| BMNR | $0.72 | $26.67 | -97.3% | 5% / 2.5% / 10% — model not meaningful for this business |
| NOW | $120.12 | $136.66 | -12.1% | 18% / 3% / 10% |

## New ideas

`recommend.py` returned no mechanical ideas (watchlist empty/gated). Discovery
produced 50 **LEADs** (see `leads.md`) — all Shariah-UNVERIFIED, edge not supplied;
none is a BUY-CANDIDATE. Highest stated reward:risk among leads (formula outputs):
BLSH 20.0, TSLA 19.6, GDDY 17.5, GOOGL 16.0, AVGO 15.8, TS 15.5, ASTS 15.5. Note
several of these have entry within ~0.1% of stop (e.g. GOOGL) — such ratios are
artefacts of a tight chandelier stop; read them with caution.

## Draft setups awaiting review

14 new DRAFT cards (list above) — all `RESEARCH — DRAFT awaiting your review (set
status: planned to approve)`. Every level is a formula output; e.g. DDOG earnings_run:
entry $274.29 / stop $246.03 / T1 $316.68 (1.5R), catalyst 2026-11-05 earnings,
Shariah unverified. Approval = edit what you disagree with, set `status: planned`,
and screen compliant in Zoya/Musaffa. See `setups/<ticker>.md` for full plans.

## Follow-ups

1. Re-screen BMNR in Zoya/Musaffa (business activity) — before any add.
2. Re-screen NOW; refresh `last_review`, add a dated catalyst and thesis target.
3. Decide whether to write thesis/invalidation fields for BMNR.
4. Review drafts for any names with near-term earnings (late Oct–mid Nov).

Not financial advice. Verify all Shariah status in Zoya/Musaffa.
