# Portfolio Assessment — 2026-10-09

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is either the broker app's recorded screen or a mechanical
ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo; 161-name pool, 71 dropped by Shariah ratio/business flag,
1 by liquidity, 2 no price; top 50 kept) → `scaffold.py --all-leads` (17 new DRAFT
cards; existing cards unchanged) → `prices` / `shariah` / `dcf` / `signals` /
`verdict` / `recommend` — all ran live, no data gaps. **Web catalyst research was
not performed this run** (unattended scheduled run); catalyst dates below are
Yahoo's auto-fetched earnings dates only — verify before relying on them.
`journal.py` not run: still no `transactions.csv`.

## Verdicts

**BMNR -> HOLD** (RULE: DEFAULT). $24.09, **+56.1%** vs $15.43 cost. Trailing stop
$23.96 — price is only ~0.5% above it (and below EMA20 $25.51). Core trade_type
exempts it from TRAIL_STOP, but it is right at the line. Vol throttle: ATR 6.78% —
size down. Mechanical proxy: conviction LOW (DCF target $0.72 — the DCF model does
not fit a crypto-treasury business; treat as data gap). 6m momentum +13.7%.

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 >= 50 — hold, do not add). $139.91,
**+21.7%** vs $114.97 cost. Trailing stop $131.36 (~6.1% below). DCF $120.12 vs
price -> -14.1% (price rich to model). 6m momentum +58.0%. Conviction LOW (mechanical
proxy; no variant view recorded).

These are your own rules resolving, not advice.

## Snapshot

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.09 | 10 | $15.43 | $240.90 | +56.1% | 19.7% |
| NOW | $139.91 | 7 | $114.97 | $979.37 | +21.7% | 80.3% |

Total $1,220.27 vs cost $959.09 (~+27.2%, +$261.18 unrealised). Only 2 names, so
concentration rules are muted (< 4 names).

## Action flags (priority order)

1. **[Mandate — carried over, still open] BMNR ratio pre-check FAILS**
   (`industry 'Capital Markets'` — core business fails screen) while the recorded
   status is `compliant` (broker app, 2026-07-07). Per Gate 1 a confirmed fail is a
   hard SELL regardless of return. COMPLIANCE_GATE reads only the recorded field, so
   the pipeline stays silent on this; it was first raised 2026-08-19 and is unresolved.
   Re-screen the business-activity question in Zoya/Musaffa.
2. **[Mandate] NOW recorded Shariah screen is STALE** (screened 2026-06-09). Ratio
   pre-check is clean (debt 1.7%, liquid 4.3%), but the recorded screen needs a refresh.
3. **[Stop proximity] BMNR sits ~0.5% above its chandelier stop** ($23.96).
4. **[Valuation] NOW P/E ~119** — VALUATION_RICH holds; do not add.
5. **[Catalyst] NOW earnings ~2026-10-28 (19 days)** per Yahoo-based discovery — inside
   the window; not independently confirmed this run.

## Suggested actions (from YOUR rules)

- VALUATION_RICH fired -> NOW: HOLD, do not add.
- COMPLIANCE_GATE does NOT fire for BMNR (reads recorded field only) — see flag 1.
- STALE shariah -> NOW: refresh the screen (flag 2).
- TRAIL_STOP not applied to either (`core` exempt); DRAWDOWN_REVIEW not firing.
- VOL_THROTTLE: BMNR ATR 6.78% > 6% — size down note.

If you execute anything, run `/apply-trade` so holdings + ledger update.

## DCF (live)

| Ticker | Intrinsic | Price | vs price | Notes |
|---|---|---|---|---|
| BMNR | $0.72 | $24.09 | not meaningful | default 5% growth, model doesn't fit |
| NOW | $120.12 | $139.91 | -14.1% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas

`watchlist.md` is hand-curated and empty/unchanged; ideas come from discovery.
`recommend.py` returned **0 BUY-CANDIDATEs** (no card is `status: planned` yet).

## Leads / DRAFT cards — 50 leads (29 LEAD, 21 RESEARCH)

All are DRAFT proposals (formula-driven levels), Shariah UNVERIFIED, edge NOT
supplied. None is a buy. Ratio pre-check clean is not a business screen.
Highest reward:risk LEADs (R:R shown with its stop; earnings = catalyst):

| Ticker | R:R | Earnings (days) | Card |
|---|---|---|---|
| LRCX | 16.1 | 2026-10-21 (12) | existing |
| AEM | 20.0 | 2026-10-28 (19) | new |
| KLIC | 20.0 | 2026-11-18 (40) | existing |
| AMKR | 20.0 | 2026-10-26 (17) | new |
| ALAB | 13.6 | 2026-11-03 (25) | existing |
| TTMI | 12.3 | 2026-11-04 (26) | existing |
| MKSI | 10.6 | 2026-11-04 (26) | existing |
| TER | 7.3 | 2026-10-21 (12) | existing |
| DOCN | 7.6 | 2026-11-04 (26) | existing |
| EXPE | 7.5 | 2026-11-04 (26) | new |
| SMCI | 6.9 | 2026-11-03 (25) | existing |
| SIMO | 6.5 | 2026-10-28 (19) | existing |

Remaining LEADs: ARW, CVE, NUE, TSLA, NVDA, LIF, GDDY, CLS, BBY, FN, GOOGL, UTHR,
HBM, RCL, ADI, CRDO, ULTA. R:R of 16–20:1 on a formula stop is often a very tight
stop (e.g. LRCX stop $311.94 vs entry $319.31) that an earnings gap would blow
through — check the gap plan on each card. RESEARCH names are capped by the
asymmetry gate (R:R < 3) or catalyst gate (JBL 68d, AVGO 61d, MU 75d, PENG 88d).
Full list in `leads.md`. Recurring open compliance questions: PLTR, and the
mining cluster (CDE, AR, AGI, IAG, KGC, EGO) if they reappear.

New DRAFT cards this run: AEM, AMKR, APA, BBY, DDOG, EXPE, FN, HBM, JBL, LLY, NUE,
PBF, PENG, PR, SMTC, TECK, TS.

## Follow-ups

1. Re-screen BMNR (business activity) in Zoya/Musaffa; decide given it sits at its stop.
2. Refresh NOW's stale Shariah screen.
3. BMNR holding file still lacks thesis/variant view/initial stop/target/pre-mortem.
4. NOW earnings ~10-28; no web verification done this run.
5. Review DRAFT cards at your pace (none `planned`); start `transactions.csv` via
   `/apply-trade` to unlock the discipline guard.

---
Not a financial advisor. Verify compliance independently in Zoya/Musaffa.
