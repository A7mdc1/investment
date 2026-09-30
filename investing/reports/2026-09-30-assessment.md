# Portfolio Assessment — 2026-09-30

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status is a broker-app record or a mechanical pre-check, not a fatwa —
verify in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo, top 50 kept) -> `scaffold.py --all-leads` (15 new
DRAFT cards: AAPL, AMKR, BBY, BLSH, DDOG, FLYW, FN, FRO, HBM, HPE, LLY, NTNX,
TECK, TS, XOM) -> `prices` / `shariah` / `dcf` / `signals` / `verdict` /
`recommend`, all live, no data gaps. **Per-holding web research (catalysts,
news) was NOT done this run** (unattended scheduled run) — no catalyst or news
claims are made below. `transactions.csv` still absent, so the discipline
guard is dormant.

## Verdicts

**BMNR -> HOLD** (DEFAULT, no rule fired). $26.79, **+73.6%** vs $15.43 cost.
Trailing stop $23.58 (~12% below), 6m momentum +28.0%. Vol throttle: ATR 6.57%
— size down. *But the ratio pre-check still FAILS (see flag #1).*

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 — hold, do not add). $134.15,
**+16.7%** vs $114.97. Trailing stop $131.28 (~2.1% below price), 6m momentum
+41.5%.

PM-grade records (mechanical proxies, not a conviction call): both LOW
conviction, `would_buy_today: true` per recommend.py. BMNR R:R -8.1:1 and NOW
R:R -4.6:1 are driven by DCF-derived targets below price — not meaningful
signals. No thesis/variant view/pre-mortem on BMNR; NOW has no variant view,
target or invalidation filled in.

Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.79 | 10 | $15.43 | $267.91 | +73.6% | 22.2% |
| NOW | $134.15 | 7 | $114.97 | $939.02 | +16.7% | 77.8% |

**Total $1,206.93** (up from $1,105.51 on 2026-08-19).

## Action flags (priority order)

1. **[Mandate] BMNR ratio pre-check FAILS** — `industry 'Capital Markets'`,
   core business fails screen — vs recorded `compliant` (broker app, screened
   2026-07-07). Second consecutive run flagging this. Per Gate 1 a confirmed
   fail is a hard SELL regardless of the +73.6% return. COMPLIANCE_GATE only
   reads the recorded field, so the pipeline will not re-flag it on its own.
   Re-screen the business activity in Zoya/Musaffa; do not add until resolved.
2. **[Mandate] NOW Shariah screen is stale** — recorded 2026-06-09 (>100 days);
   ratio pre-check clean (debt 1.7%, liquid 4.5%). Re-screen.
3. **[Valuation] NOW P/E ~119** — VALUATION_RICH; do not add. Price is only
   ~2.1% above its trailing stop.
4. **[Data] DCF for BMNR ($0.72) is not meaningful** — model doesn't fit a
   crypto-treasury business. NOW DCF $120.12 vs $134.15 (-10.5%; growth 18%,
   terminal 3%, discount 10%).

## Suggested actions (from YOUR rules)

- VALUATION_RICH fired -> NOW: hold, do not add.
- VOL_THROTTLE note -> BMNR: size down (ATR 6.57%).
- COMPLIANCE_GATE silent for BMNR (reads recorded status only) — see flag #1.
- TRAIL_STOP not applicable (both `trade_type: core`).

If you execute anything, run `/apply-trade`.

## New ideas

`watchlist.md` has no curated tickers. `recommend.py` ideas: **0
BUY-CANDIDATE** (all 79 cards in `setups/` are `draft`; none `planned`).
Discovery: **26 LEAD / 24 RESEARCH**. Top LEADs by R:R (formula outputs,
Shariah UNVERIFIED, earnings in window): TSLA 20.0, LIF 20.0, GDDY 18.6,
BLSH 17.2, HAS 15.0, TTMI 9.7, FLYW 7.1, TS 6.9, WDC 6.7, HBM 6.3. Full list
with entry/target/stop and catalyst dates is in `leads.md`. Recurring open
questions (PLTR defense business; mining cluster) — PLTR is RESEARCH (R:R 1.3).
BLSH (crypto exchange) and LLY/AAPL/XOM are new cards; screen business
activity before spending review time.

## Draft setups

All cards are DRAFT — RESEARCH, awaiting your review (edit, set
`status: planned`, screen compliant). Levels are Yahoo formula outputs, never
buys. Card details: `setups/<ticker>.md`.

## Follow-ups

1. BMNR Shariah re-screen (urgent); NOW re-screen (stale).
2. Fill BMNR PM fields (thesis, stop, target, pre-mortem); NOW target/invalidation.
3. Review draft cards at your pace; none are `planned`.
4. Start logging trades via `/apply-trade` to enable the discipline guard.

Not a financial advisor — verify Shariah status in Zoya/Musaffa.
