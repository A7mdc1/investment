# Portfolio Assessment — 2026-10-17

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is the broker app's recorded screen or a mechanical
ratio/business pre-check, not a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo, top 50 leads) -> `scaffold.py --all-leads` (20 new
DRAFT cards: AAPL AEM APA BBY BKR DDOG EXPE FLYW FRO FSLR HPE LLY NTAP NTNX PBF
PR SNA TECK TS XOM; existing cards unchanged) -> `prices/shariah/dcf/signals/
verdict/recommend` — all live, no data gaps. Unattended run: **no per-holding web
catalyst research was done** this cycle; catalyst fields below are from the
cards/holdings only. `journal.py` not run (no `transactions.csv`).

## Action flags (priority order)
1. **BMNR — Shariah conflict.** Recorded `compliant` (broker app, screened
   2026-07-07, now stale >100d) but the mechanical business pre-check **fails**
   (industry `Capital Markets`, core business fails screen). Re-screen in
   Zoya/Musaffa; do not add until resolved. (Same flag as 2026-08-19, still open.)
2. **BMNR — price below its trailing stop.** Price $21.66 vs chandelier trailing
   stop $24.21 (fast EMA $24.45), about 10.5% under it; verdict.py still resolves
   HOLD because the position is typed `core` (no rule fired). Your own stop
   discipline may deserve a look. ATR 7.16% — vol-throttle note says size down.
3. **NOW — Shariah screen stale** (2026-06-09, >100d). Ratio pre-check clean
   (debt 1.6%, liquid 4.3%). Re-screen.
4. **NOW — concentration 82.1%** of a $1,210 book (concentration rules muted <4
   names). P/E ~119 -> VALUATION_RICH: hold, do not add.

## Verdicts (YOUR rules resolving, not advice)
| Ticker | Verdict | Price | Return | Weight | Trail stop | 6m mom | Rule |
|---|---|---|---|---|---|---|---|
| BMNR | HOLD | $21.66 | +40.4% | 17.9% | $24.21 (price below) | +4.1% | DEFAULT |
| NOW | HOLD | $141.97 | +23.5% | 82.1% | $136.23 (+4.0% above) | +43.3% | VALUATION_RICH |

PM records (mechanical proxies, not a conviction call): both conviction LOW.
BMNR: no reward:risk or stated thesis; "would buy today" mechanically yes but it
reads the recorded Shariah field, not the failed pre-check. NOW: reward:risk
-3.8:1 (DCF target $120.12 under price); stop distance only 4.0%.

## Snapshot
Total $1,210.39 — BMNR 10 sh @ $15.43 cost, value $216.60; NOW 7 sh @ $114.97,
value $993.79.

## DCF (assumptions visible)
- NOW: intrinsic $120.12 vs $141.97 -> -15.4% (growth 18% 5y, terminal 3%, disc 10%).
- BMNR: $0.72 vs $21.66 -> -96.7% (growth 5%, terminal 2.5%, disc 10%). The DCF
  does not fit a crypto-treasury business; treat as non-informative.

## Suggested actions (from your rules)
- Rule VALUATION_RICH fired on NOW (P/E ~119 >= pe_rich) -> hold, do not add.
- Vol throttle fired on BMNR (ATR 7.16%) -> size down.
- If you execute anything, run /apply-trade so holdings + ledger update.

## New ideas
`recommend.py` returned **no ideas** (watchlist empty of gated names). Discovery
produced 50 **LEAD**s in `leads.md` (none BUY-CANDIDATE: no card is `planned`
and none is Shariah-verified). Top by reward-risk: AEM 15.4:1 (earnings
10-28), TSLA 20.0:1 (10-21, existing card), GOOGL 15.0:1 (10-28), SNA 9.9:1,
BKR 8.9:1, UTHR 7.6:1. Several are at/near earnings within days — a gap risk the
cards' default `earnings_plan: exit_before` is meant to handle.

## Draft & planned setups
All new cards are `status: draft` — **RESEARCH — DRAFT awaiting your review (set
status: planned to approve)**; every level is a formula output, Shariah
`unverified`. Full plans are in `setups/<ticker>.md`.
- **Check FSLR first:** the scaffolded stop ($180.54, chandelier off the
  22-day high) is *above* the entry ($172.64) and target is null — an invalid
  plan as generated; edit or discard. Other drafts with stop >= entry or null
  target (see `leads.md` row for PAY: stop 33.51 > entry 31.54) deserve the same check.
- Review, edit, screen compliant, then flip to `planned`.

## Follow-ups
1. Re-screen BMNR (business-activity) and NOW in Zoya/Musaffa; record on holdings.
2. Decide BMNR vs its $24.21 trailing stop.
3. Fix/discard invalid drafts (FSLR, PAY); review the rest.
4. Add catalyst dates / thesis fields to holdings so conviction can be assessed.

Not financial advice. Verify Shariah status in Zoya/Musaffa.
