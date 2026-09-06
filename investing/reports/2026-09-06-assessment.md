# Portfolio Assessment — 2026-09-06

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (16 new DRAFT setup cards auto-filled — NTNX, XOM,
HBM, NTAP, AAPL, BLSH, TECK, TS, FLYW, APA, FRO, PR, SMTC, BBY, SNA, ASND; 34
existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run separately — still no `transactions.csv`
(`journal.csv`/`transactions.csv` are gitignored personal ledgers and don't
exist in this workspace; the discipline guard stays dormant until you log
trades).

**Since the last report (2026-08-19):** no new trades recorded in the
holdings files — same two positions, both up further on price.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.97**, up
**+61.8%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — this is now the fourth run flagging it (07-07 screen, 08-19,
09-06).** New this run: BMNR's daily ATR is 6.02%, just over the
`vol_throttle_atr_pct: 6` threshold — `verdict.py` now surfaces a
**size-down** portfolio note that was not present last run.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -9.4:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from last two runs) |
| DCF intrinsic value | $0.72 vs. $24.97 price -> -97.1% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $22.3972 — price ~11.5% above it |
| 6m momentum (skip last month) | -3.1% |
| Vol throttle | **NEW — ATR 6.02% > 6% threshold: size down per `verdict.py`'s portfolio note** |
| Would buy today? | Mechanically yes per `recommend.py`'s gates — it only reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$141.26**, **+22.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $141.26 price -> -15.0% (richer to the model than last run's -6.6% — the gap has widened as price ran ahead of the DCF, which used the same fixed assumptions) |
| Trailing stop (chandelier) | $130.0182 — price ~8.0% above it |
| 6m momentum (skip last month) | -5.6% |
| Would buy today? | Mechanically yes per `recommend.py`'s gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- **New this run:** `verdict.py` surfaced `portfolio_notes: ["BMNR ATR 6.02% — size down per vol throttle"]` — the first time the vol-throttle note has fired for either position.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.97 | 10 | $15.43 | $249.70 | +61.8% | 20.2% |
| NOW | $141.26 | 7 | $114.97 | $988.82 | +22.9% | 79.8% |

**Total value: $1,238.52** | Cost: $959.09 | **Total return: ~+29.1%** (+$279.43 unrealised)

Both positions are up meaningfully since 08-19 (BMNR +21.6% in three weeks,
NOW +9.8%). Weighting is essentially unchanged (BMNR 20.2% vs 18.6% before) —
still a function of BMNR's small 10-share count relative to NOW, not a
deliberate rebalance recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — still open, 4th run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, same flag as 08-19 and earlier:
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. This still conflicts with the recorded `compliant` status
   (broker app, screened 2026-07-07 — now stale by calendar time even if
   `shariah.py`'s staleness check hasn't tripped). Current reporting (Sept
   2026) continues to describe BMNR as a pure Ethereum-treasury vehicle:
   ~5.9M ETH held (4.8% of total supply, 97% of the way to a stated 5%
   target), $15.6B in combined crypto/cash/marketable securities, and its
   value driven by ETH price and staking yield rather than an operating
   business. That is the same profile that triggered the original flag —
   nothing in this run's research resolves it either way. Per this repo's
   Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL,
   independent of the now +61.8% return. **`recommend.py`'s "would buy
   today" check still only reads the recorded field and stays silent on
   this.** Re-screen the business-activity question specifically in
   Zoya/Musaffa before adding to this position or treating "compliant" as
   settled — the position has grown from 18.6% to 20.2% of the book while
   this has sat open.
2. **[New this run] Vol throttle fired for BMNR** — ATR 6.02% just crossed
   the `vol_throttle_atr_pct: 6` de-risk threshold in `rules.md`. This is a
   sizing signal from your own pre-set rule, not a sell signal — it says any
   *addition* to BMNR should be sized down for volatility, not that the
   existing position must be trimmed.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still
   holds. Do not add. The DCF gap widened to -15.0% (from -6.6% last run) as
   price ran further ahead of the model's fixed growth/discount assumptions.
4. **[DCF caveat / BMNR]** The -97.1% DCF "downside" is still not a
   meaningful signal — the model's cash-flow assumptions (5% growth, 10%
   discount, no BMNR-specific override) don't fit a crypto-treasury business
   whose value tracks ETH holdings and staking yield, not discounted
   operating cash flow. Treat as a data gap, not a valuation call.
5. **[Catalyst / NOW]** Q2 FY2026 earnings (beat, reported 2026-07-22) are
   already in the price; **next earnings land 2026-10-28** (52 days out —
   inside the 60-day catalyst-horizon default now, unlike last run's 72-day
   read). AI ACV surpassed $1B with agentic deployments up 9x in nine
   months and Now Assist NNACV beating internal forecasts per the Q2 call;
   Armis/Veza/Moveworks acquisitions continue extending the AI-native
   security/identity platform story.
6. **[Discovery] 50 leads this run, 20 clearing to LEAD tier** — a sharp
   jump from 08-19's 9 LEAD-tier names (rest capped at RESEARCH by the
   asymmetry or catalyst-horizon gate). **PLTR** carries over again with its
   still-unresolved government/defense business-activity question. The
   precious-metals/mining cluster (**AU, AGI, EGO, HBM, KGC, IAG, AR, CDE**)
   is larger this run too — same open financing-structure question flagged
   in prior runs, still unresolved.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continued aggressive ETH accumulation —
5.9M ETH held (~4.8% of total supply), 97% of the way to chairman Tom Lee's
stated "5% of ETH supply" goal reached in 14 months; combined crypto/cash/
marketable-securities holdings of $15.6B. B. Riley raised its price target to
$30 from $25 on 2026-09-03, and the stock gained ~14.7% that day on Ethereum
sentiment (Lee projecting ETH could reach $6,000). Stock up +61.8% since the
$15.43 cost basis; recorded compliance status is still "compliant."

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check has now disagreed with the recorded status for
three consecutive runs — see Action Flag #1. The holding file is still
missing PM-grade fields (`thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, `pre_mortem` all null/empty, ~9 weeks after the position
opened), and volatility has now crossed the vol-throttle threshold — a
second reason to size any addition carefully, on top of the open compliance
question.

**Verdict: HOLD (no technical rule fired) — the compliance question is still
the thing to resolve first, and it has only gotten larger as the position's
weight and return have grown.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 beat (EPS $0.90 vs. $0.76 est.; subscription
revenue +24.5% YoY, total revenue +24% YoY) reported 2026-07-22. AI Annual
Contract Value crossed $1B with agentic AI deployments up 9x in nine months
and AI Control Tower adoption past 500 customers in six months. Management
says AI demand continues to exceed internal expectations. DCF shows a wider
but still moderate ~15.0% premium to intrinsic value.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum still
negative (-5.6%) despite the rally; next earnings land 2026-10-28 (52 days
out, now inside the 60-day catalyst horizon) — the Armis/Veza/Moveworks
integration narrative is the thing to track into that print.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite three straight runs of ratio-precheck failure. That gap
  won't close on its own — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE fired -> BMNR (new this run)**: ATR 6.02% > 6% threshold —
  size down any addition; this is a sizing note, not a sell signal.

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
and flipped to `status: planned` yet; all 96 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank, unchanged `discover_top_n: 50`). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
without one — 16 new cards this run (NTNX, XOM, HBM, NTAP, AAPL, BLSH, TECK,
TS, FLYW, APA, FRO, PR, SMTC, BBY, SNA, ASND); the other 34 leads already had
cards from prior runs and were left unchanged. **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

20 of the 50 leads clear to LEAD tier this run (up sharply from 08-19's 9;
the rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate),
sorted by catalyst proximity:

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| AA | LEAD | existing | 13.6:1 | earnings 2026-10-15 | 39 |
| LRCX | LEAD | existing | 17.8:1 | earnings 2026-10-21 | 45 |
| TSLA | LEAD | existing | 12.3:1 | earnings 2026-10-21 | 45 |
| HAS | LEAD | existing | 11.4:1 | earnings 2026-10-22 | 46 |
| CLS | LEAD | existing | 17.0:1 | earnings 2026-10-26 | 50 |
| STX | LEAD | existing | 10.6:1 | earnings 2026-10-27 | 51 |
| AGI | LEAD | existing | 6.6:1 | earnings 2026-10-28 | 52 |
| MSFT | LEAD | existing | 3.9:1 | earnings 2026-10-28 | 52 |
| EGO | LEAD | existing | 7.8:1 | earnings 2026-10-29 | 53 |
| FOX | LEAD | existing | 8.9:1 | earnings 2026-10-29 | 53 |
| HBM | LEAD | new | 7.5:1 | earnings 2026-10-29 | 53 |
| GDDY | LEAD | existing | 5.5:1 | earnings 2026-10-29 | 53 |
| XOM | LEAD | new | 8.7:1 | earnings 2026-10-30 | 54 |
| PLTR | LEAD | existing | 3.3:1 | earnings 2026-11-02 | 57 |
| ALAB | LEAD | existing | 9.4:1 | earnings 2026-11-03 | 58 |
| AMD | LEAD | existing | 6.4:1 | earnings 2026-11-03 | 58 |
| IAG | LEAD | existing | 4.2:1 | earnings 2026-11-03 | 58 |
| TTMI | LEAD | existing | 20.0:1 | earnings 2026-11-04 | 59 |
| WDC | LEAD | existing | 18.7:1 | earnings 2026-11-05 | 60 |
| AU | LEAD | existing | 6.4:1 | earnings 2026-11-05 | 60 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **AU, AGI, EGO, HBM, KGC, IAG, AR, CDE** — the recurring precious-metals/
  mining cluster, larger this run than 08-19's smaller list; mining-royalty
  financing structures raised the same open question in earlier runs. Still
  worth a real screen before spending review time on any of these cards.
- **30 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now open 3+ runs] BMNR Shariah re-screen**: the mechanical
   ratio pre-check keeps disagreeing with the recorded "compliant" status on
   the business-activity question. The position is now 20.2% of the book at
   +61.8% — the largest this question has ever been in dollar terms. The
   automated pipeline will NOT re-surface it on its own.
2. **[New] BMNR vol-throttle note** — ATR crossed 6%; size any addition down
   accordingly per your own rule.
3. **[Housekeeping] BMNR holding file is missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, ~9 weeks after the position was
   opened.
4. **[Time-boxed] NOW earnings ~2026-10-28** — 52 days out, now inside the
   60-day catalyst horizon; track the AI ACV / Armis-Veza-Moveworks
   integration narrative into the print.
5. **[Housekeeping] 16 new DRAFT setup cards** added this run (96 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [B. Riley raises Bitmine Immersion price target — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_01/)
- [Bitmine Immersion Technologies (BMNR) Stock News — StockTitan](https://www.stocktitan.net/news/BMNR/)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
