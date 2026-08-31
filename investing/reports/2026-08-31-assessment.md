# Portfolio Assessment — 2026-08-31

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 153-name raw pool, top 50 kept per
`discover_top_n: 50`; 67 names dropped by the Shariah ratio-flag filter, 2 by
liquidity, 2 for no price) → `scaffold.py --all-leads` (13 new DRAFT setup
cards auto-filled: NTNX, TS, XOM, SMTC, BLSH, BKR, AAPL, EXPE, ASND, TECK,
SMCIP, APA, PR; 37 existing cards left unchanged) → `prices.py` / `shariah.py`
/ `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run (discovery was slow under Yahoo rate-limiting but completed with
a full pool). `journal.py` not run — still no `transactions.csv` (discipline
guard stays dormant; no trades logged since the FIG sale / BMNR buy on the
last report).

**Since the last report (2026-08-19):** no trades. Both positions ran
further: BMNR +20.3% in price, NOW +14.9% in price. The BMNR compliance
question flagged last run is unresolved and unchanged.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.72**, up
**+60.2%** vs. the $15.43 cost basis. **The mechanical Shariah business-
activity pre-check still disagrees with the recorded "compliant" status —
same flag as last run, now on a materially larger gain.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -14.6:1 (DCF target sits far below the stop; DCF doesn't fit this business — see caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL — unchanged from 2026-08-19** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $24.72 price -> -97.1% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $23.0502 — price ~7.2% above it |
| 6m momentum (skip last month) | -15.3% |
| Would buy today? | Mechanically yes per recommend.py's gates — it only reads the *recorded* field, still blind to this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$147.77**, **+28.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); ratio pre-check also clean this run (business_ok, debt ratio 1.6%, liquid ratio 4.1%) |
| DCF intrinsic value | $120.12 vs. $147.77 price -> -18.7% (price more stretched vs. the model than last run's -6.6%) |
| Trailing stop (chandelier) | $129.843 — price is ~13.8% above it |
| 6m momentum (skip last month) | +1.7% (turned positive since last run's -5.3%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.72 | 10 | $15.43 | $247.15 | +60.2% | 19.3% |
| NOW | $147.77 | 7 | $114.97 | $1,034.39 | +28.5% | 80.7% |

**Total value: $1,281.54** | Cost: $959.09 | **Total return: ~+33.7%**
(+$322.45 unrealised) — up from $1,105.51 on 2026-08-19.

## Action flags (priority order)

1. **[Mandate — unresolved from last run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`. This is the same
   business-activity question raised on 2026-08-19 and nothing has changed
   in the holding file or the recorded status since — it has not been
   re-screened. Current web reporting (Aug 30) puts total crypto/cash/
   marketable-securities holdings at **$15.6B**, ETH stake at 5.07M tokens
   (~$390M annualized staking revenue projected), funded by continued share
   issuance/buybacks — a profile that still reads as a financial/treasury
   vehicle rather than an operating tech company. Per this repo's own Gate 1
   ("Shariah knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail would be a hard SELL, independent of the
   +60.2% return. **`recommend.py`'s "would buy today" check still cannot
   see this — it only reads the recorded field.** This is now the second
   consecutive run flagging it, on a position up 60% and unchanged in the
   file for six weeks since it was opened.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Catalyst / NOW — status change] Earnings confirmed 2026-10-28 — now
   58 days out**, inside the 60-day `catalyst_horizon_days` window for the
   first time (was 72 days/outside on 2026-08-19). Since last run: BofA
   raised its price target to $150 (from $130) and Wells Fargo to $175 (from
   $160), citing a broad software re-rating and eased AI-disruption fears;
   ServiceNow expanded its "Autonomous Security" suite (six unified security
   solutions in the AI Control Tower) and deepened the Tech Mahindra AI
   partnership; a new CMO (Simon Mouyal) was appointed. Stock is up ~27%
   from $114.19 (Aug 3) to $144.62 (Aug 28) on this news flow.
4. **[DCF caveat / BMNR]** The -97.1% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business whose
   value tracks ETH holdings and staking yield, not discounted operating
   cash flow. Treat this number as a data gap, not a valuation call.
5. **[Discovery] 50 leads this run**, 16 clearing to LEAD tier (up from 9 on
   2026-08-19): SNX, CRDO, LRCX, AA, XOM, AGI, ZS, MU, UTHR, HAS, AVT, SIMO,
   GDDY, TSLA, CDE, BKR. 67 of 153 raw names were dropped outright by the
   Shariah ratio-flag filter this run (a new discover.py stat surfaced —
   worth noting how much of the pool a pure ratio screen removes before any
   human review). **PLTR** carries over again with its still-unresolved
   government/defense business-activity question. The recurring
   precious-metals/mining cluster (CDE, AGI, KGC, AR, AU, IAG, EGO) is
   present again — same open compliance question as prior runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressively growing its ETH
treasury — 5.07M ETH staked (~$12.7B), total crypto/cash/marketable
securities at $15.6B as of Aug 30, ~4.9% of global ETH supply. Tom Lee
(Chairman) points to the mid-September CLARITY Act vote as a potential
positive catalyst plus a possible 4-year crypto-cycle bottom. Stock up
+60.2% since the $15.43 cost basis; recorded compliance status is still
"compliant."
[PRNewswire — $15.6B holdings](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-90-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-6-billion-302864579.html) ·
[Timothy Sykes, Aug 24](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_24/) ·
[Timothy Sykes, Aug 25](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_25/)

**Case to flag (compliance, independent of the price story):** Second
consecutive run where the mechanical ratio pre-check disagrees with the
recorded status on the business-activity question. The holding file remains
incomplete — no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` — six weeks after the position was opened,
so there is still no PM-grade record to weigh the compliance question
against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, and it has now gone two full cycles
without action.**

### NOW — ServiceNow, Inc
**Case to keep:** Broad-based bullish news flow since last run — two analyst
price-target hikes (BofA to $150, Wells Fargo to $175), expanded
"Autonomous Security" product suite, deepened Tech Mahindra AI partnership,
new CMO hire. 6m momentum turned positive (+1.7%, from -5.3% last run).
Earnings (Oct 28) now fall inside the 60-day catalyst window.
[Timothy Sykes, Aug 28](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_08_28/) ·
[StocksToTrade, Aug 28](https://stockstotrade.com/news/servicenow-inc-now-news-2026_08_28/) ·
[TradingKey, Aug 28](https://www.tradingkey.com/news/market-movers/262138961-market-movers-now-20260828)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active — do not add at this
multiple. DCF gap widened to -18.7% (was -6.6% on 2026-08-19) as price ran
faster than the model's intrinsic-value estimate. The position is now 80.7%
of the book — a concentration outcome of BMNR being the small leg, not a
deliberate sizing decision recorded anywhere in the files.
[TipRanks — earnings date](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (still `compliant`), so it stays silent
  despite two straight runs of a ratio-precheck fail. Nothing in the
  automated pipeline will re-flag this on its own until the recorded status
  is updated — the follow-up is still on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); both prices sit above their chandelier levels regardless
  (BMNR ~7.2% above, NOW ~13.8% above).
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.72 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $147.77 | -18.7% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** this run (expected — no card has been reviewed and flipped
to `status: planned` yet; all 76 working cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 13 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, 153 raw names,
67 dropped by the Shariah ratio-flag filter, 2 by liquidity) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (13
new cards: NTNX, TS, XOM, SMTC, BLSH, BKR, AAPL, EXPE, ASND, TECK, SMCIP,
APA, PR; 37 existing cards left unchanged). **Every DRAFT card is unreviewed
and Shariah UNVERIFIED — proposals to review and edit, never buys.**

16 of the 50 leads clear to LEAD tier this run (rest capped at RESEARCH by
the asymmetry or catalyst-horizon gate):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| SNX | existing | 10.7:1 | earnings 2026-09-24 | 24 |
| CRDO | existing | 8.3:1 | earnings 2026-09-01 | 1 |
| LRCX | existing | 16.9:1 | earnings 2026-10-21 | 51 |
| AA | existing | 15.5:1 | earnings 2026-10-15 | 45 |
| XOM | new | 8.3:1 | earnings 2026-10-30 | 60 |
| AGI | existing | 8.8:1 | earnings 2026-10-28 | 58 |
| ZS | existing | 3.6:1 | earnings 2026-09-03 | 3 |
| MU | existing | 3.9:1 | earnings 2026-09-30 | 30 |
| UTHR | existing | 7.6:1 | earnings 2026-10-28 | 58 |
| HAS | existing | 5.7:1 | earnings 2026-10-22 | 52 |
| AVT | existing | 5.7:1 | earnings 2026-10-28 | 58 |
| SIMO | existing | 5.0:1 | earnings 2026-10-29 | 59 |
| GDDY | existing | 4.9:1 | earnings 2026-10-29 | 59 |
| TSLA | existing | 3.5:1 | earnings 2026-10-21 | 51 |
| CDE | existing | 4.1:1 | earnings 2026-10-28 | 58 |
| BKR | new | 3.4:1 | earnings 2026-10-22 | 52 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AGI, KGC, AR, AU, IAG, EGO** — the recurring precious-metals/mining
  cluster; mining-royalty/financing-structure questions raised in earlier
  runs remain open. Still worth a real screen before spending review time on
  any of these cards.
- **34 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now two runs unresolved] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status on the business-activity question for two consecutive assessment
   cycles (2026-08-19 and 2026-08-31). This is the largest compliance
   question in the book (19.3% weight, +60.2% return) and the automated
   pipeline will not re-surface it on its own — see the COMPLIANCE_GATE note
   above. Recommend prioritizing an actual Zoya/Musaffa business-activity
   screen before the next cycle.
2. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, six weeks after
   the position was opened.
3. **[Time-boxed — status change] NOW earnings ~2026-10-28** — now 58 days
   out and inside the catalyst-horizon window; track the AI ACV / Autonomous
   Security / Tech Mahindra narrative into the print.
4. **[Housekeeping] 13 new DRAFT setup cards** added this run (76 working
   cards total in `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.90 Million Tokens, Total Holdings $15.6B — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-90-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-6-billion-302864579.html)
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Traders — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_24/)
- [BMNR Stock Jumps As Massive Ethereum Treasury Draws Traders — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_25/)
- [ServiceNow (NOW) Stock Draws Bullish Targets As AI Partnership Expands — Timothy Sykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_08_28/)
- [ServiceNow (NOW) Stock Climbs As Wall Street Hikes Targets — StocksToTrade](https://stockstotrade.com/news/servicenow-inc-now-news-2026_08_28/)
- [ServiceNow Inc (NOW) Market Movers, Aug 28 — TradingKey](https://www.tradingkey.com/news/market-movers/262138961-market-movers-now-20260828)
- [ServiceNow (NOW) Earnings Dates — TipRanks](https://www.tipranks.com/stocks/now/earnings)
