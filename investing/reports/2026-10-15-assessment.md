# Portfolio Assessment — 2026-10-15

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is the broker app's recorded screen or a mechanical
pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo, top 50 kept) → `scaffold.py --all-leads` (21 new DRAFT
cards; existing cards unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py`, all live, no data gaps.
**Not done this run:** web catalyst/news research (unattended run) — no catalyst
claims below beyond what the scripts return. `journal.py` not run (no
`transactions.csv`; discipline guard dormant). Last report: 2026-08-19.

## Verdicts
- **BMNR -> HOLD** (DEFAULT, no rule fired). $22.76, **+47.5%** vs $15.43 cost.
  Chandelier trail **$24.38 is ABOVE the price** (≈6.7% below it), yet no
  TRAIL_STOP SELL fired — the holding is `trade_type: core`, so confirm that
  is the intent (rules.md lists `price < chandelier -> SELL`). 6m momentum +1.6%.
  Vol throttle: ATR 6.55% — size down.
- **NOW -> HOLD** (VALUATION_RICH: P/E ~119 — hold, do not add). $147.48, **+28.3%**
  vs $114.97. Trail $131.97 (≈10.5% below price). 6m momentum n/a in output.

PM-grade records are mechanical proxies, not a conviction call: both **LOW**
(BMNR: no R:R or thesis on file; NOW: R:R -1.8:1). Neither holding file has
`variant_view`, `initial_stop`, `target_price` or `pre_mortem` filled.

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $22.76 | 10 | $15.43 | $227.65 | +47.5% | 18.1% |
| NOW | $147.48 | 7 | $114.97 | $1,032.36 | +28.3% | 81.9% |

**Total $1,260.01** (was $1,105.51 on 08-19). Concentration rules muted (<4 names)
but NOW is ~82% of the book.

## Action flags (priority)
1. **[Mandate] NOW Shariah screen is STALE** — recorded compliant, screened
   2026-06-09. Re-screen in Zoya/Musaffa before any further action.
2. **[Mandate] BMNR ratio pre-check still FAILS** (`Capital Markets` — core
   business fails screen) vs. recorded `compliant` (broker app, 2026-07-07). Open
   since the 08-19 report. A confirmed fail is a Gate-1 hard SELL regardless of
   +47.5%. `recommend.py` reads only the recorded field, so its "would buy today:
   yes" does not see this. Screen the business-activity question in Zoya/Musaffa.
3. **[Stop] BMNR trades below its chandelier** (see Verdicts) — decide whether
   `core` exempts it, or set an explicit `initial_stop`.
4. **[Valuation] NOW** P/E ~119; DCF intrinsic $120.12 vs $147.55 → **-18.6%**
   (assumptions: 5y growth 18%, terminal 3%, discount 10%). Do not add.
5. **[DCF caveat] BMNR** DCF $0.72 (-96.8%; 5% growth/2.5%/10%) is not meaningful
   for a crypto-treasury business — treat as a data gap.
6. **[Catalyst] NOW** `catalyst.date` is still null in the holding file (earnings
   typically late Oct) — confirm the date from ServiceNow IR and record it.

## Suggested actions (your rules fired)
- VALUATION_RICH -> NOW: hold, do not add.
- No SELL/TRIM/REVIEW rule fired mechanically. If you execute anything, run /apply-trade.

## New ideas / leads
Discovery: 50 leads (`leads.md`). Top by tier (all **LEAD**/RESEARCH — Shariah
UNVERIFIED, no human-reviewed edge): FOX, SNA, TSLA, AR, LIF, GOOGL, NTAP, GDDY,
TECK, TS, RCL, ADI (LEAD tier); PLTR, PBF, UTHR, DINO, CVE, MSFT, HAS, DLO, EXPE,
LLY, PAY, AAPL, APA, FRO, XOM (RESEARCH — thin R:R or no card/catalyst).
`recommend.py` returned no BUY-CANDIDATE ideas. PLTR's government/defense
business-activity question remains open.

## Draft setups
**21 new DRAFT cards** (all formula outputs, `status: draft`, Shariah `unverified`):
AAPL, AEM, APA, BBY, BKR, DDOG, EXPE, FLYW, FRO, FSLR, HBM, LLY, NBIX, NTAP, NTNX,
PBF, PR, SNA, TECK, TS, XOM. All are `earnings_run`, default `earnings_plan:
exit_before`. Verdict for each: **RESEARCH — DRAFT awaiting your review (set
status: planned to approve)**. Example, SNA: enter ~$365.75 ahead of 10-22 print,
stop $362.90 (HH22 $379.60 − 3×ATR $5.57), T1 $370.03 (+1.5R), 21-day window,
invalidation: no positive drift in 5 sessions / gives back >1 ATR.

**Review warning:** for several drafts the chandelier stop is *above or at* the
entry price (e.g. AEM entry 184.82 / stop 185.23, BKR 53.84/54.08, FSLR
136.93/141.48, HBM 23.82/24.81, NBIX 263.14/264.65, FRO 52.86/53.16, NTAP, PR,
BKR) — price already sits under its trail, so the plan is internally
inconsistent. Do not approve these without rewriting the stop; any computed R:R
for them is an artifact. These drafts can never reach BUY-CANDIDATE unaided.

## Follow-ups
1. Re-screen NOW (stale) and BMNR (business-activity) in Zoya/Musaffa.
2. Decide on BMNR vs. its trailing stop; fill `initial_stop`/`target`/`pre_mortem`.
3. Record NOW's earnings date in the holding file.
4. Review/edit draft cards you care about; fix stop>entry ones first.
5. Consider whether ~82% NOW is intended.
6. Consider a scaffold guard to skip/flag drafts where stop >= entry.

Not financial advice; verify Shariah status in Zoya/Musaffa.
