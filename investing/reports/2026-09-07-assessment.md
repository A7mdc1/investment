# Portfolio Assessment — 2026-09-07

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (16 new DRAFT setup cards auto-filled: AAPL, APA,
ASND, BBY, BLSH, FLYW, FRO, HBM, NTAP, NTNX, PR, SMTC, SNA, TECK, TS, XOM; the
other 34 leads already had cards, left unchanged) → `prices.py` / `shariah.py`
/ `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` still returns 0 closed trades — no
`transactions.csv` activity since last run, discipline guard stays dormant.

**Since the last report (2026-08-19):** no trades recorded. Same two
holdings, same open compliance question on BMNR (see Action Flag #1 —
**still unresolved, second consecutive run**).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.97**, up
**+61.8%** vs. the $15.43 cost basis. **Action Flag #1 carries over
unresolved: the mechanical Shariah ratio/business-activity pre-check still
disagrees with the recorded "compliant" status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -9.4:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL, unchanged** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $24.97 price -> -97.1% (not a meaningful signal for a crypto-treasury business — see caveat) |
| Trailing stop (chandelier) | $22.3972 — price ~11.5% above it |
| 6m momentum (skip last month) | -3.1% |
| Vol throttle | ATR 6.02% — `verdict.py` flags "size down per vol throttle" (new note this run) |
| Would buy today? | Mechanically yes per recommend.py's gates — that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$141.26**, **+22.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $141.26 price -> -15.0% (price more stretched to the model than last run's -6.6%) |
| Trailing stop (chandelier) | $130.0182 — price is ~8.5% above it |
| 6m momentum (skip last month) | -5.6% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- New this run: `verdict.py`'s `portfolio_notes` flags BMNR's ATR at 6.02% for
  a vol-throttle size-down note (didn't fire last run).

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.97 | 10 | $15.43 | $249.70 | +61.8% | 20.2% |
| NOW | $141.26 | 7 | $114.97 | $988.82 | +22.9% | 79.8% |

**Total value: $1,238.52** | Cost: $959.09 | **Total return: ~+29.1%** (+$279.43 unrealised)

Weighting is essentially unchanged from last run (BMNR 18.6% -> 20.2%, NOW
81.4% -> 79.8%) — both positions have simply run up together; no rebalancing
trigger from concentration (still muted, <4 names).

## Action flags (priority order)

1. **[Mandate — STILL OPEN, 2nd consecutive run] BMNR's mechanical Shariah
   ratio pre-check FAILS**, same flag as 2026-08-19:
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. Recorded status is still `compliant` (broker app, screened
   2026-07-07 — now 62 days old). This has not been re-screened since it was
   first flagged three weeks ago. Per this repo's own Gate 1 ("Shariah
   knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail would be a hard SELL, independent of the
   +61.8% return — and the position has grown, not shrunk, while the
   question sat open. `recommend.py`'s "would buy today" check only reads
   the recorded field and stays silent on this. **Re-screen in Zoya/Musaffa
   on the business-activity question specifically before treating
   "compliant" as settled or adding to this position.**
2. **[New this run] BMNR vol throttle** — `verdict.py` now flags ATR 6.02%
   (above the `vol_throttle_atr_pct: 6` knob) with a "size down" note. This
   is a sizing signal, not a sell trigger.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still
   holds. Do not add. DCF gap widened to -15.0% (from -6.6% last run) after
   the ~28% one-month rally — see per-holding read below.
4. **[DCF caveat / BMNR]** The -97.1% DCF "downside" remains not a
   meaningful signal — the model (5% growth, 10% discount, no BMNR-specific
   override) does not fit a crypto-treasury business valued on ETH holdings
   and staking yield, not discounted operating cash flow.
5. **[Housekeeping / BMNR]** Still missing `thesis_one_liner`,
   `variant_view`, `initial_stop`, `target_price`, `pre_mortem` — same gap
   flagged last run, now unresolved for two months since the position opened.
6. **[Discovery] 50 leads this run, 20 clear to LEAD tier** (up from 9 last
   run) — see the leads table below. PLTR carries over again with its
   still-unresolved government/defense business-activity question from prior
   runs; the CDE/AR/AGI/IAG/KGC/EGO precious-metals/mining cluster also
   recurs with the same open financing-structure question.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressive ETH accumulation — a
65-week buying streak, adding 53,501 ETH (~$131M) last week for a total of
~5.9M ETH — while holding ~$340.3M cash and virtually no long-term debt.
Shares soared 46.5% in August alone.
[The Motley Fool](https://www.fool.com/investing/2026/09/03/why-bitmine-immersion-technologies-soared-465-in-a/) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_01/)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check has now disagreed with the recorded "compliant"
status for two consecutive runs with no re-screen in between. The holding
file itself is still missing every PM-grade field (thesis, variant view,
stop, target, pre-mortem) two months after entry, so there's no recorded
conviction to weigh the open compliance question against beyond the
mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
now the oldest open item in the book and the position has grown while it
sat unresolved.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 revenue $3.99B (+24% YoY); 123 transactions
>$1M net-new ACV (+~40% YoY); cRPO $13.20B (+21% YoY); agentic AI
deployments up 9x in nine months; management now guides AI ACV above
$1.5B. Stock rallied ~28% over the past month on this momentum.
[24/7 Wall St.](https://247wallst.com/investing/2026/09/03/servicenow-just-rallied-28-in-a-month-take-profits-or-buy-more/) ·
[ServiceNow Newsroom — Q2 FY2026 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; DCF gap widened to
-15.0% (price has run further ahead of the model's intrinsic value than
last run); 6m momentum still negative (-5.6%) despite the rally; stock is
still 11% red year-to-date per recent coverage, so the one-month move is a
partial recovery, not a new high. Next earnings not yet confirmed on a hard
date in this run's data.
[24/7 Wall St.](https://247wallst.com/investing/2026/09/03/servicenow-just-rallied-28-in-a-month-take-profits-or-buy-more/)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two straight runs of a ratio-precheck fail. Nothing in the
  automated pipeline will re-flag this on its own until the recorded status
  is updated — this follow-up is on you, and it's now overdue.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **New: vol-throttle note -> BMNR**: ATR 6.02% above the 6% knob; a sizing
  consideration if adding, not a sell signal on the existing position.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.97 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $141.26 | -15.0% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 81 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for the 16 leads without one
(AAPL, APA, ASND, BBY, BLSH, FLYW, FRO, HBM, NTAP, NTNX, PR, SMTC, SNA, TECK,
TS, XOM); the other 34 leads already had cards from prior runs and were left
unchanged. **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.**

20 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
asymmetry/catalyst gates loosened as more names picked up near-term earnings
dates):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| WDC | existing | 18.7:1 | earnings 2026-11-05 | 59 |
| TTMI | existing | 20.0:1 | earnings 2026-11-04 | 58 |
| LRCX | existing | 17.8:1 | earnings 2026-10-21 | 44 |
| CLS | existing | 17.0:1 | earnings 2026-10-26 | 49 |
| AA | existing | 13.6:1 | earnings 2026-10-15 | 38 |
| TSLA | existing | 12.3:1 | earnings 2026-10-21 | 44 |
| HAS | existing | 11.4:1 | earnings 2026-10-22 | 45 |
| STX | existing | 10.6:1 | earnings 2026-10-27 | 50 |
| ALAB | existing | 9.4:1 | earnings 2026-11-03 | 57 |
| FOX | existing | 8.9:1 | earnings 2026-10-29 | 52 |
| XOM | new (this run) | 8.7:1 | earnings 2026-10-30 | 53 |
| EGO | existing | 7.8:1 | earnings 2026-10-29 | 52 |
| HBM | new (this run) | 7.5:1 | earnings 2026-10-29 | 52 |
| AGI | existing | 6.6:1 | earnings 2026-10-28 | 51 |
| AMD | existing | 6.4:1 | earnings 2026-11-03 | 57 |
| AU | existing | 6.4:1 | earnings 2026-11-05 | 59 |
| GDDY | existing | 5.5:1 | earnings 2026-10-29 | 52 |
| MSFT | existing | 3.9:1 | earnings 2026-10-28 | 51 |
| IAG | existing | 4.2:1 | earnings 2026-11-03 | 57 |
| PLTR | existing | 3.3:1 | earnings 2026-11-02 | 56 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI, IAG, KGC, EGO, AU, HBM** — the recurring precious-metals/
  mining cluster (8 of the 20 LEAD-tier names this run); the same
  mining-royalty financing-structure question flagged in earlier runs is
  still open. Worth a real screen before spending review time on any of
  these cards, and note this cluster's earnings dates bunch heavily in the
  last week of October — treat it as one correlated timing bet, not eight.
- **30 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  to keep this report readable.

## Follow-ups (priority order)

1. **[Overdue — 2nd consecutive run] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status for three weeks now with no action taken. This is the largest
   open item in the book (20.2% weight, +61.8% return, growing) and the
   automated pipeline will NOT re-surface it on its own.
2. **[Housekeeping — 2 months open] BMNR holding file is still missing
   PM-grade fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` remain null/empty.
3. **[Time-boxed] NOW's next earnings date is not yet confirmed in this
   run's data** — track the AI ACV guidance (>$1.5B) and Q3 print timing.
4. **[Housekeeping] 16 new DRAFT setup cards** added this run (81 total in
   `setups/`); none are `planned`. Review at your own pace, with the mining
   cluster and PLTR as the compliance-question priority names.
5. **[Infrastructure — still open]** No ledger activity since the FIG
   sale/BMNR buy — start logging any new trades to `transactions.csv` (or
   via `/apply-trade`) to keep the discipline guard live once trade count
   grows.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Why Bitmine Immersion Technologies Soared 46.5% In August — The Motley Fool](https://www.fool.com/investing/2026/09/03/why-bitmine-immersion-technologies-soared-465-in-a/)
- [BMNR Stock Stalls After Sharp Run, But Volatility Stays High — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_01/)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow Just Rallied 28% in a Month: Take Profits, or Buy More? — 24/7 Wall St.](https://247wallst.com/investing/2026/09/03/servicenow-just-rallied-28-in-a-month-take-profits-or-buy-more/)
