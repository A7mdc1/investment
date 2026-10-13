# Portfolio Assessment — 2026-10-13

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is a broker-app record or a mechanical ratio/business
pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo; 159-name pool, 72 dropped by Shariah ratio/business flag,
50 kept) -> `scaffold.py --all-leads` (24 new DRAFT cards; 41 existing unchanged) ->
`prices / shariah / dcf / signals / verdict / recommend` (all live, no data gaps).
**No web catalyst research this run** (automated routine; catalyst dates below are
Yahoo-derived only). `journal.py` not run: still no `transactions.csv`.

## Verdicts
**BMNR -> HOLD** (DEFAULT, no rule fired). $23.77, +54.1% vs $15.43 cost.
Trailing stop (chandelier) $24.33 — price is ~2.4% *below* it; `trade_type: core`
exempts it from TRAIL_STOP, so no rule fires. 6m momentum +19.9%. ATR 6.34% ->
vol-throttle note (size down). Conviction LOW (no reward:risk / thesis stated).
**Shariah: recorded compliant (2026-07-07) but the mechanical pre-check still FAILS**
(`industry 'Capital Markets'`) — open since the 2026-08-19 report, unresolved.

**NOW -> HOLD** (VALUATION_RICH, P/E ~119). $139.28, +21.1% vs $114.97. Trailing
stop $131.05 (~6% below price). 6m momentum +62.1%. Conviction LOW (reward:risk
-2.3:1 vs DCF). **Shariah recorded screen (2026-06-09) is now >100 days old -> stale,
re-screen.**

These are your own rules resolving, and the PM fields are mechanical proxies.

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $23.77 | 10 | $15.43 | $237.70 | +54.1% | 19.6% |
| NOW | $139.28 | 7 | $114.97 | $974.96 | +21.1% | 80.4% |

Total **$1,212.66** (up from $1,105.51 on 2026-08-19). Only 2 holdings; concentration
rules muted until >= 4 names, but NOW is 80% of the book.

## Action flags
1. **[Mandate] BMNR business-activity pre-check fail vs recorded "compliant"** — still
   open; `recommend.py`/COMPLIANCE_GATE only read the recorded field and stay silent.
   A confirmed fail would be an absolute SELL under Gate 1. Re-screen in Zoya/Musaffa.
2. **[Mandate] NOW Shariah screen stale (>100d)** — re-screen (new this run).
3. **[Catalyst] NOW earnings expected ~2026-10-28** (~15 days) — inside the window,
   with a rich P/E; the pre-print gap risk is yours to size. Not verified this run.
4. **[Valuation] NOW P/E ~119** — hold, do not add. DCF $120.12 vs $139.35 (-13.8%;
   growth 18%, terminal 3%, discount 10%).
5. **[DCF caveat] BMNR DCF $0.72 (-97%)** — default 5% growth model does not fit a
   crypto-treasury business; treat as a data gap, not a valuation call.

## Suggested actions (from YOUR rules)
- VALUATION_RICH fired -> NOW: hold, do not add.
- Vol throttle -> BMNR (ATR 6.34%): size down on any add.
- COMPLIANCE_GATE silent on BMNR (reads recorded status only) — see flag 1.
- TRAIL_STOP not applicable (core). DRAWDOWN_REVIEW not firing (both up).
If you execute anything, run `/apply-trade`.

## New ideas
`watchlist.md` is empty; `recommend.py` returned **0 BUY-CANDIDATEs** (no card is
`planned`/Shariah-verified). Discovery: 50 leads, 20 at LEAD tier, rest RESEARCH
(asymmetry/catalyst gate). All Shariah UNVERIFIED, EDGE not supplied.

| LEAD | Mechanical basis |
|---|---|
| DOCN | reward:risk 13.3:1, catalyst 22d out |
| HBM | reward:risk 11.5:1, catalyst 16d out |
| EXPE | reward:risk 9.1:1, catalyst 22d out |
| CLS | reward:risk 13.6:1, catalyst 13d out |
| BKR | reward:risk 10.6:1, catalyst 14d out |
| AR | reward:risk 6.0:1, catalyst 15d out |
| CRDO | reward:risk 16.9:1, catalyst 48d out |
| AVGO | reward:risk 15.9:1, catalyst 57d out |
| CIEN | reward:risk 16.7:1, catalyst 58d out |
| GDDY | reward:risk 5.3:1, catalyst 16d out |
| TSLA | reward:risk 5.8:1, catalyst 8d out |
| ARW | reward:risk 5.0:1, catalyst 16d out |
| LIF | reward:risk 6.0:1, catalyst 27d out |
| AMD | reward:risk 4.7:1, catalyst 21d out |
| NUE | reward:risk 3.8:1, catalyst 13d out |
| SMTC | reward:risk 5.2:1, catalyst 41d out |
| UTHR | reward:risk 4.0:1, catalyst 15d out |
| BBY | reward:risk 5.8:1, catalyst 42d out |
| GOOGL | reward:risk 3.2:1, catalyst 15d out |
| RCL | reward:risk 3.2:1, catalyst 14d out |

**Draft cards** (24 new this run: AAPL, AEM, APA, BBY, BKR, DDOG, EXPE, FLYW, HBM, HPE,
JBL, KEYS, LLY, NTNX, NUE, ORCL-PD, PBF, PR, SMCIP, SMTC, SNA, TECK, TS, XOM) are
`RESEARCH — DRAFT awaiting your review (set status: planned to approve)`. Every level is
a formula output; they are proposals to edit, never buys. See `setups/<ticker>.md` and
`leads.md`. Carried-over open questions: PLTR (government/defense), the mining/royalty
cluster (AR, AGI, CDE, KGC, EGO), and energy/refiners (XOM, APA, PBF) need a real
business screen. ORCL-PD and SMCIP are preferred-share tickers with no earnings date —
likely junk leads.

## Follow-ups
1. BMNR Zoya/Musaffa business-activity re-screen (urgent, open 2 runs).
2. NOW re-screen and pre-earnings (~10-28) sizing decision.
3. BMNR holding file still lacks thesis / stop / target / pre_mortem.
4. Review the 65 draft cards at your pace; none are `planned`.
5. No ledger yet — log FIG sale / BMNR buy via `/apply-trade` to enable the discipline guard.

---
Not a financial advisor. Verify Shariah status in Zoya/Musaffa before acting.
