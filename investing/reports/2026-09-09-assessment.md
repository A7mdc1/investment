# Portfolio Assessment — 2026-09-09

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 152-name raw pool, top 50 kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (16 new DRAFT setup cards
auto-filled; 34 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run — still no `transactions.csv` (discipline
guard stays dormant).

**Since the last report (2026-08-19):** no trades were logged in `holdings/`
(still just BMNR + NOW). The BMNR Shariah ratio-precheck disagreement flagged
last run has **not** been resolved — see Action Flag #1, carried forward.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.56**, up
**+59.1%** vs. the $15.43 cost basis — a large move since last report's
+33.1%. **The mechanical Shariah business-activity pre-check still disagrees
with the recorded "compliant" status — unresolved for a second run.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -10.9:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry `Capital Markets`, sector `Financial Services`; core business fails screen (unchanged from 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $24.56 price -> -97.1% (not a meaningful signal — DCF doesn't fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.3699 — price ~9.8% above it |
| 6m momentum (skip last month) | -12.7% |
| Vol throttle | **New this run** — ATR 6.16% > `vol_throttle_atr_pct` (6%) fired a portfolio note: size down |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not the ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$131.26**, **+14.2%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); mechanical ratio pre-check also clean this run (debt ratio 1.8%, liquid ratio 4.6%) |
| DCF intrinsic value | $120.12 vs. $131.26 price -> -8.5% (more rich than last run's -6.6%) |
| Trailing stop (chandelier) | $130.2735 — **price is only ~0.7% above it**, down sharply from ~17.9% cushion last report |
| 6m momentum (skip last month) | +9.3% (flipped positive from -5.3% last report) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, the Shariah screen going stale, or price closing below the chandelier stop |

- **`trade_type: core` exempts both positions from the technical TRAIL_STOP
  rule**, so neither verdict flips on stop proximity alone — but NOW sitting
  0.7% above a level the file itself computes is worth your own read, not
  just the tool's silence on it.
- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.56 | 10 | $15.43 | $245.55 | +59.1% | 21.1% |
| NOW | $131.26 | 7 | $114.97 | $918.82 | +14.2% | 78.9% |

**Total value: $1,164.37** | Cost: $959.09 | **Total return: ~+21.4%** (+$205.28 unrealised)

Weighting is essentially unchanged from last report (BMNR 21.1% vs 18.6%,
NOW 78.9% vs 81.4%) — still a function of BMNR's small share count, not a
deliberate rebalancing decision recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — carried over, still open] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, same flag as 2026-08-19:
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. This is now a **second consecutive run** with the recorded
   `compliant` status unreconciled against the mechanical read, on a position
   that has since grown from +33.1% to +59.1% and now holds 5.93M ETH
   (~4.9% of ETH supply) and $15.7B in total crypto/cash/marketable
   securities per its Sep 8 disclosure — a profile that leans further into
   "financial/treasury vehicle" the larger it gets. Per this repo's own
   Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL regardless
   of the return. **`recommend.py`'s "would buy today" check still only
   reads the recorded field and stays silent on this.** This is the same
   category of issue that took 7 runs to resolve with FIG — worth
   prioritizing a real Zoya/Musaffa business-activity screen this cycle
   rather than letting it carry a third time.
2. **[New this run] Vol throttle fired on BMNR** — ATR 6.16% exceeds
   `vol_throttle_atr_pct` (6%), surfaced as a `portfolio_notes` entry:
   "size down per vol throttle." This didn't fire last run; it's a
   volatility-driven sizing note, not a compliance or price call.
3. **[New this run] NOW is trading close to its own trailing stop** — price
   $131.26 vs. chandelier stop $130.27 (~0.7% cushion), down from ~17.9%
   last report, despite the stock being up on the quarter. `trade_type: core`
   means TRAIL_STOP doesn't mechanically fire, so this is a note for your own
   judgment, not an automated flag.
4. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
5. **[DCF caveat / BMNR]** The -97.1% DCF "downside" is still not a
   meaningful signal — the cash-flow model doesn't fit a crypto-treasury
   business whose value tracks ETH holdings and staking yield, not
   discounted operating cash flow. Treat as a data gap, not a valuation call.
6. **[Catalyst / NOW — housekeeping]** ServiceNow's next earnings is now
   publicly dated **~2026-10-28** (49 days out — inside the 60-day
   `catalyst_horizon_days` window, unlike last report's 72-day estimate).
   The holding file's `catalyst.date` field is still `null`, so
   `recommend.py`/`verdict.py` can't see this — worth filling in so the
   mechanical catalyst gate reflects it.
7. **[Discovery] 50 leads this run, 21 clearing to LEAD tier** (up from 9
   last run — a materially wider pool of names passing the mechanical
   asymmetry+catalyst gates this cycle). **PLTR** carries over again with its
   still-unresolved government/defense business-activity question. The
   precious-metals/mining cluster (**AGI, AR, IAG, CDE** at LEAD; **KGC,
   EGO** at RESEARCH) is also back — same open compliance question on
   mining-royalty financing structures flagged in prior runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH holdings grew to 5.93M tokens (~4.9% of
global supply) with total crypto/cash/marketable securities at $15.7B as of
Sep 8 — up from 5.82M ETH / $11.4-11.6B a month ago. Staked ETH (5.07M, at a
2.61% 7-day yield) projects to ~$386M in annualized staking revenue. Average
daily dollar volume ~$1.10B (top-100 US name by liquidity), so size is not a
liquidity constraint here.
[Chainwire](https://chainwire.org/2026/09/08/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion/) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_01/)

**Case to flag (compliance, independent of the price story):** Two runs in a
row, the mechanical ratio pre-check disagrees with the recorded status — see
Action Flag #1. The holding file is still missing `thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, and `pre_mortem` — two months
into the position, there is still no PM-grade record to weigh the compliance
question against.

**Verdict: HOLD (no technical rule fired) — the compliance question is still
the thing to resolve first, and it's now waited two full cycles.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 EPS beat ($0.90 vs $0.76 est., +18.4%); shares up
~25% over the trailing three months on AI momentum; BTIG raised its price
target to $170 from $150 with a fresh Buy rating. 6-month momentum has
flipped positive (+9.3%, from -5.3% last report).
[BTIG rating / Robinhood](https://robinhood.com/us/en/stocks/NOW/) ·
[Earnings preview — Barchart](https://www.barchart.com/story/news/1001215/servicenow-earnings-preview-what-to-expect)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; DCF premium widened
to -8.5% (from -6.6%); price now sits only ~0.7% above its own computed
chandelier stop after the run-up, even though `trade_type: core` keeps that
from mechanically firing; next earnings ~2026-10-28 (49 days out, inside the
catalyst horizon) but not yet recorded in the holding file's `catalyst.date`.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent for a second run despite the ratio-precheck fail. Nothing in the
  automated pipeline will re-flag this on its own until you update the
  recorded status — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **VOL_THROTTLE fired -> BMNR** (new this run): size down per the note;
  no forced action, but it's now an active flag where it wasn't last cycle.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT mechanically fire for either
  (`trade_type: core` exemption); NOW's price sits just 0.7% above its
  computed level regardless — worth your own read even though the rule stays silent.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.56 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $131.26 | -8.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** this run — expected, since no card has been reviewed and
flipped to `status: planned` yet; all cards in `setups/` remain `draft`.

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, 152 raw names,
up from 149) and wrote **`leads.md`** (top 50 by max-benefit rank).
`scaffold.py --all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for
every lead without one — **16 new cards** (AAPL, DDOG, NTNX, NTAP, FLYW, HPE,
BLSH, HBM, TECK, TS, XOM, ASND, APA, FRO, PR, SMCIP); 34 existing cards left
unchanged. **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.**

21 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| ALAB | LEAD | existing | 18.4:1 | earnings 2026-11-03 | 55 |
| TTMI | LEAD | existing | 15.2:1 | earnings 2026-11-04 | 56 |
| UTHR | LEAD | existing | 14.7:1 | earnings 2026-10-28 | 49 |
| DDOG | LEAD | new | 10.3:1 | earnings 2026-11-05 | 57 |
| MSFT | LEAD | existing | 10.7:1 | earnings 2026-10-28 | 49 |
| TER | LEAD | existing | 10.0:1 | earnings 2026-10-21 | 42 |
| WDC | LEAD | existing | 9.7:1 | earnings 2026-11-05 | 57 |
| AAPL | LEAD | new | 9.2:1 | earnings 2026-10-29 | 50 |
| AA | LEAD | existing | 9.3:1 | earnings 2026-10-15 | 36 |
| LRCX | LEAD | existing | 9.1:1 | earnings 2026-10-21 | 42 |
| PLTR | LEAD | existing | 7.4:1 | earnings 2026-11-02 | 54 |
| AGI | LEAD | existing | 6.2:1 | earnings 2026-10-28 | 49 |
| FLYW | LEAD | new | 5.5:1 | earnings 2026-11-03 | 55 |
| TSLA | LEAD | existing | 5.0:1 | earnings 2026-10-21 | 42 |
| STX | LEAD | existing | 4.5:1 | earnings 2026-10-27 | 48 |
| CLS | LEAD | existing | 4.6:1 | earnings 2026-10-26 | 47 |
| AR | LEAD | existing | 4.0:1 | earnings 2026-10-28 | 49 |
| IAG | LEAD | existing | 3.8:1 | earnings 2026-11-03 | 55 |
| CDE | LEAD | existing | 3.4:1 | earnings 2026-10-28 | 49 |
| APH | LEAD | existing | 3.2:1 | earnings 2026-10-28 | 49 |
| SNX | LEAD | existing | 3.0:1 | earnings 2026-09-24 | 15 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **AGI, AR, IAG, CDE (LEAD), KGC, EGO (RESEARCH)** — the recurring
  precious-metals/mining cluster; mining-royalty financing structures raised
  the same open question in earlier runs. Four of six now clear to LEAD tier
  (up from being mostly RESEARCH-capped before) — still worth a real screen
  before spending review time on any of these cards.
- **29 RESEARCH-tier leads** this run — full list in `leads.md`; not
  reproduced here in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — carried over, now 2 runs open] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status for two consecutive cycles now, on a position that has grown to
   21.1% of the book and +59.1% return. The automated pipeline will not
   re-surface this on its own — see Action Flag #1 / COMPLIANCE_GATE note.
2. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, nearly two months
   after the position was opened.
3. **[New] NOW's chandelier stop cushion has compressed to ~0.7%** — not an
   automated trigger (`trade_type: core`), but worth your own check given how
   much the buffer shrank from ~17.9% last report despite the price rally.
4. **[Housekeeping] Fill in NOW's `catalyst.date`** (~2026-10-28 is now
   public) so the mechanical catalyst gate reflects the confirmed date.
5. **[Housekeeping] 16 new DRAFT setup cards** added this run (79 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.93 Million Tokens — Chainwire](https://chainwire.org/2026/09/08/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion/)
- [BMNR Stock Stalls After Sharp Run, But Volatility Stays High — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_01/)
- [ServiceNow (NOW) Stock — Robinhood](https://robinhood.com/us/en/stocks/NOW/)
- [ServiceNow Earnings Preview — Barchart](https://www.barchart.com/story/news/1001215/servicenow-earnings-preview-what-to-expect)
