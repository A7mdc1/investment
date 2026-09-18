# Portfolio Assessment — 2026-09-18

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (13 new DRAFT setup cards auto-filled — AMKR, CORZ,
NTNX, DDOG, NTR, TS, PR, BLSH, XOM, FRO, HPE, APA, AAPL; 63 existing cards
left unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run (Yahoo's
crumb endpoint was rate-limited on `shariah.py` but the fallback path still
returned full data). `journal.py` not run — `transactions.csv` still doesn't
exist (discipline guard stays dormant; no trades logged since the last
report).

**Since the last report (2026-08-19):** no trades — still just BMNR and NOW,
unchanged share counts. Both positions are up since last run: BMNR +33.1% →
+66.5% on cost, NOW +11.8% → +18.9% on cost.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.70**, up
**+66.5%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check disagrees with the recorded "compliant" status
for the second consecutive run — see Action Flag #1.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.7:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not yet stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (same flag as 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $25.70 price -> -97.2% (not a meaningful signal — DCF doesn't fit a crypto-treasury business) |
| Trailing stop (chandelier) | $21.2975 — price ~20.7% above it |
| 6m momentum (skip last month) | -4.3% |
| Vol throttle | ATR 7.37% (above the 6% threshold) — size down per `portfolio_notes` |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check only reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$136.70**, **+18.9%** vs. $114.97 cost basis. **New this run: the
recorded Shariah screen is now stale (>100 days since 2026-06-09) — see
Action Flag #2.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah (recorded) | **REVIEW** — recorded compliant but screen is >100 days old; re-screen |
| DCF intrinsic value | $120.12 vs. $136.70 price -> -12.1% (price more rich to the model than last run's -6.6%) |
| Trailing stop (chandelier) | $130.1518 — price ~4.8% above it (tighter cushion than last run's 17.9%) |
| 6m momentum (skip last month) | +12.3% (flipped positive from -5.3% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping (it just did) |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.70 | 10 | $15.43 | $256.99 | +66.5% | 21.2% |
| NOW | $136.70 | 7 | $114.97 | $956.90 | +18.9% | 78.8% |

**Total value: $1,213.89** | Cost: $959.09 | **Total return: ~+26.6%** (+$254.80 unrealised)

Concentration in NOW eased slightly (81.4% → 78.8%) purely because BMNR
appreciated faster this cycle, not from any rebalancing action.

## Action flags (priority order)

1. **[Mandate — persists, 2nd run] BMNR's mechanical Shariah ratio pre-check
   still FAILS** — same flag as 2026-08-19: `industry 'Capital Markets'
   matches 'capital markets' — core business fails screen`. This still
   conflicts with the recorded `compliant` status (broker app, screened
   2026-07-07). Independent reporting this run continues to describe BMNR
   as an Ethereum treasury vehicle rather than an operating tech company:
   holdings have grown to **5.96M ETH (~4.9% of total supply, ~$15.8B in
   total crypto/cash)**, with the company explicitly chasing a "5% of ETH
   supply" target and running its own institutional staking platform
   (MAVAN). That's a larger, more concentrated financial-asset/yield
   profile than at the last review — if anything strengthening the case
   that this needs a real business-activity re-screen, not just a ratio
   check. Per this repo's Gate 1 ("Shariah knockout — non-compliant /
   ratio-or-business flag -> AVOID/SELL, absolute"), a confirmed fail would
   be a hard SELL independent of the now +66.5% return. `recommend.py`'s
   "would buy today" check still only reads the recorded field and is
   silent on this. **This is now two consecutive runs unresolved — the
   longer it's deferred, the larger the unrealized gain riding on an
   unresolved compliance question.**
2. **[Mandate — NEW this run] NOW's Shariah screen is now stale** — recorded
   `compliant`, screened 2026-06-09, which is >100 days old (past the
   ~1-quarter staleness threshold). `recommend.py` now shows `REVIEW`
   instead of `PASS` for this reason alone. Re-screen and update
   `screened:` in `holdings/now-servicenow.md`.
3. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH
   holds, and DCF gap widened to -12.1% (from -6.6% last run). Do not add.
4. **[DCF caveat / BMNR]** The -97.2% DCF "downside" remains not a
   meaningful signal — the model doesn't fit a crypto-treasury business
   whose value tracks ETH holdings and staking yield, not discounted
   operating cash flow. Treat as a data gap, not a valuation call.
5. **[Catalyst / NOW]** Next earnings now land **~2026-10-28 (40 days
   out)** — inside the 60-day catalyst-horizon default (last run this was
   72 days out and outside it). Stock has drifted sharply higher off the
   July 22 print; watch for guidance commentary on AI ACV growth and Armis
   integration heading into the print.
6. **[Discovery] 50 leads this run, 33 clear to LEAD tier** — up sharply
   from 9/50 last run (higher scores and reward:risk this cycle). **PLTR**
   again carries an unresolved government/defense business-activity
   question from prior runs — still nothing new to add, still open. The
   **precious-metals/mining cluster (CDE, AGI, IAG, EGO)** also reappears,
   all at LEAD tier this run — same open financing-structure question
   flagged previously.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH holdings grew from 5.82M to 5.96M tokens
since last run (~4.9% of Ethereum's total supply), total crypto/cash position
now ~$15.8B, and management is within ~144,000 ETH of its self-stated "5% of
supply" target. Analysts continue raising price targets on the accumulation
story. Stock up +66.5% since the $15.43 cost basis; recorded compliance
status is still "compliant."
[Benzinga](https://www.benzinga.com/crypto/cryptocurrency/26/09/61823316/bmnr-5-percent-ethereum) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_17/) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877165.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status for a second
straight run — see Action Flag #1. The holding file is still missing
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, and
`pre_mortem` — six weeks after the position opened, there's still no
PM-grade record to weigh the compliance question against beyond the
mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — the compliance question is
still the thing to resolve first, and it's now overdue.**

### NOW — ServiceNow, Inc
**Case to keep:** 6-month momentum has flipped positive (+12.3%, from -5.3%
last run); the stock has continued its run since the July 22 Q2 print
(reported EPS beat, $0.90 vs. $0.76 est.). Next earnings land 2026-10-28,
now inside the 60-day catalyst window.
[TipRanks](https://www.tipranks.com/stocks/now/earnings) ·
[ServiceNow Newsroom — Q2 2026 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active and the DCF gap
widened to -12.1% (price further above intrinsic value than last run); the
trailing-stop cushion has compressed to ~4.8% (from ~17.9% last run) as the
stock has run up faster than the chandelier stop has trailed; and the
Shariah screen just went stale (Action Flag #2) — a housekeeping item, not
a compliance failure, but one that's now due.
[Nasdaq — earnings dates](https://www.nasdaq.com/market-activity/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: still only reads the *recorded*
  `shariah.status` field (`compliant`), so it stays silent despite two
  runs of ratio-precheck failures. Nothing in the pipeline will re-flag
  this on its own — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices remain
  above their computed chandelier levels, though NOW's cushion has
  compressed materially since last run.
- **VOL_THROTTLE -> BMNR**: fires this run (`portfolio_notes`: "BMNR ATR
  7.37% — size down per vol throttle"); did not fire last run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.70 | -97.2% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $136.70 | -12.1% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — every card in `setups/`
is still `status: draft`; none has been reviewed and flipped to `planned`).

## Draft & planned setups — 50 leads, 12 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and rewrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one —
**13 new cards this run** (AMKR, CORZ, NTNX, DDOG, NTR, TS, PR, BLSH, XOM,
FRO, HPE, APA, AAPL); 63 existing cards were left unchanged. **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.**

33 of the 50 leads clear to LEAD tier this run (up sharply from 9/50 last
run — the rest are capped at RESEARCH by the asymmetry or catalyst-horizon
gate):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| MSFT | existing | 10.7:1 | earnings 2026-10-28 | 40 |
| GDDY | existing | 12.0:1 | earnings 2026-10-29 | 41 |
| FOX | existing | 12.0:1 | earnings 2026-10-29 | 41 |
| TER | existing | 11.3:1 | earnings 2026-10-21 | 33 |
| CDE | existing | 10.6:1 | earnings 2026-10-28 | 40 |
| AGI | existing | 11.0:1 | earnings 2026-10-28 | 40 |
| AMKR | new | 14.9:1 | earnings 2026-10-26 | 38 |
| IONQ | existing | 20.0:1 | earnings 2026-11-04 | 47 |
| WDC | existing | 20.0:1 | earnings 2026-11-05 | 48 |
| TTMI | existing | 15.5:1 | earnings 2026-11-04 | 47 |
| VICR | existing | 7.6:1 | earnings 2026-10-20 | 32 |
| IAG | existing | 7.6:1 | earnings 2026-11-03 | 46 |
| ASTS | existing | 20.0:1 | earnings 2026-11-09 | 52 |
| CORZ | new | 8.1:1 | earnings 2026-10-23 | 35 |
| TSLA | existing | 6.8:1 | earnings 2026-10-21 | 33 |
| APH | existing | 7.0:1 | earnings 2026-10-28 | 40 |
| MU | existing | 3.2:1 | earnings 2026-09-30 | 12 |
| STX | existing | 6.2:1 | earnings 2026-10-27 | 39 |
| ALAB | existing | 5.8:1 | earnings 2026-11-03 | 46 |
| EGO | existing | 5.0:1 | earnings 2026-10-29 | 41 |
| DOCN | existing | 3.6:1 | earnings 2026-11-04 | 47 |
| NVDA | existing | 3.1:1 | earnings 2026-11-17 | 60 |
| GOOGL | existing | 4.6:1 | earnings 2026-10-28 | 40 |
| PLTR | existing | 3.6:1 | earnings 2026-11-02 | 45 |
| (9 more LEAD-tier names in leads.md, not reproduced here) | | | | |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carries over again with its unresolved government/defense
  business-activity question from prior runs. Still `status: draft`.
- **CDE, AGI, IAG, EGO** — the recurring precious-metals/mining cluster;
  mining-royalty financing structures raised the same open question in
  earlier runs, and all four are now LEAD tier (higher visibility than
  when they were RESEARCH-capped last run). Still worth a real screen
  before spending review time on any of these cards.
- **17 RESEARCH-tier leads** this run (down from 41 last run, since more
  names now clear the asymmetry/catalyst gates) — full list in `leads.md`;
  not reproduced here in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now 2 runs unresolved] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status on the business-activity question for two consecutive monthly
   runs now. This is the largest compliance question in the book (21.2%
   weight, +66.5% return, growing) and the pipeline will not re-surface it
   on its own.
2. **[New this run] NOW Shariah re-screen** — recorded screen is now >100
   days old; update `screened:` in `holdings/now-servicenow.md` once
   re-verified.
3. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are still null/empty, six weeks after the
   position was opened.
4. **[Time-boxed] NOW earnings ~2026-10-28** — now 40 days out and inside
   the catalyst horizon; watch AI ACV / Armis integration commentary into
   the print, and note the trailing-stop cushion has compressed to ~4.8%.
5. **[Housekeeping] 12 new DRAFT setup cards** added this run (78 total in
   `setups/`, including template/README files); none are `planned`. Review
   at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades
   to `transactions.csv` (or via `/apply-trade`) to unlock the discipline
   guard. Still zero trades logged since the BMNR buy / FIG sale.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Nears Tom Lee's 5% Ethereum Goal — Benzinga](https://www.benzinga.com/crypto/cryptocurrency/26/09/61823316/bmnr-5-percent-ethereum)
- [BMNR Stock Rides Ethereum Wave As Analysts Hike Targets — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_17/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877165.html)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow, Inc. Common Stock (NOW) Earnings Report Dates — Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings)
