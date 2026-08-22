# Portfolio Assessment — 2026-08-22

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 149-name raw pool, top 50 kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (6 new DRAFT setup cards
auto-filled — PAAS, YUMC, ASND, SMCIP, XOM, JAZZ; 44 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still no `transactions.csv` (discipline guard stays
dormant).

**Since the last report (2026-08-19):** no trades recorded. Both holdings
moved with the market; the open BMNR Shariah question from last run is
unchanged and still unresolved.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$22.83**, up
**+48.0%** vs. the $15.43 cost basis. **Action Flag #1 carries over unchanged:
the mechanical Shariah business-activity pre-check still disagrees with the
recorded "compliant" status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.8:1 (DCF-derived target sits below the stop; DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (same flag as 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $22.83 price -> -96.9% (DCF model does not fit a crypto-treasury business — see caveat) |
| Trailing stop (chandelier) | $19.5901 — price ~16.5% above it |
| 6m momentum (skip last month) | -17.6% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail (same gap as last run) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$128.48**, **+11.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $128.48 price -> -6.5% (price modestly rich to the model) |
| Trailing stop (chandelier) | $111.0091 — price is ~15.7% above it |
| 6m momentum (skip last month) | -11.8% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $22.83 | 10 | $15.43 | $228.30 | +48.0% | 20.2% |
| NOW | $128.48 | 7 | $114.97 | $899.36 | +11.8% | 79.8% |

**Total value: $1,127.66** | Cost: $959.09 | **Total return: ~+17.6%** (+$168.57 unrealised)

BMNR's continued rally has pushed it back near (but still under) the 22%
`max_position_pct` cap; NOW remains the dominant weight at 79.8%, still a
function of BMNR's small share count rather than a deliberate sizing call
recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — carried over, still unresolved] BMNR's mechanical Shariah
   ratio pre-check still FAILS**, flagging `industry 'Capital Markets'
   matches 'capital markets' — core business fails screen`. This is the same
   conflict raised in the 2026-08-19 report against the recorded `compliant`
   status (broker app, screened 2026-07-07) — three days on, nothing in the
   record shows it has been re-screened. Fresh coverage this run (Aug 20-21)
   continues to describe BMNR as an Ethereum treasury vehicle: ETH holdings
   now at 5.82M tokens (~4.8% of global supply), total crypto/cash holdings
   of $11.4B, a $4B buyback (~19-21M shares repurchased), and BMNP preferred
   dividends locked in through late 2026 — the same profile (yield/treasury
   income financed partly by preferred dividends) that reads closer to a
   financial/investment vehicle than an operating tech company. Per this
   repo's own Gate 1 ("Shariah knockout — non-compliant / ratio-or-business
   flag -> AVOID/SELL, absolute"), a confirmed fail would be a hard SELL,
   independent of the +48.0% return. **`recommend.py`'s "would buy today"
   check still only reads the recorded field and stays silent on this flag.**
   This is now the second consecutive run carrying this open question — the
   same pattern that took 7 runs to resolve with FIG on the position that
   replaced it.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF caveat / BMNR]** The -96.9% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override in the holding file) does not fit a
   crypto-treasury business whose value is driven by ETH holdings and
   staking yield, not discounted operating cash flow. Treat this number as
   a data gap, not a valuation call.
4. **[Catalyst / NOW]** Next earnings confirmed **2026-10-27/28** (~66-67
   days out — outside the 60-day catalyst-horizon default, so still no
   near-term binary event). Analyst tone since last run stayed constructive:
   Bank of America initiated Buy with a $150 target (Aug 19) and Wells Fargo
   raised its target to $175 (Aug 17); Q2 2026 subscription revenue grew
   24.5% YoY with AI ACV past $1B.
   [Barchart](https://www.barchart.com/story/news/1001215/servicenow-earnings-preview-what-to-expect) ·
   [ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
5. **[Discovery] 50 leads this run, 12 clearing to LEAD tier** (up from 9
   last run — same 149-name raw pool size, `discover_top_n` still 50). New
   this run: TER, LRCX, TSLA joined the LEAD tier; PLTR dropped out of the
   discovered pool entirely (no longer surfaced — its unresolved
   government/defense question is moot for now since it isn't in this run's
   candidate set). The precious-metals/mining cluster (AGI, CDE, AR, KGC)
   is still present at RESEARCH tier with the same open
   business-activity question flagged in prior runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressively growing its core
Ethereum position (5.82M ETH, ~4.8% of global supply, per Aug 16-21
reporting) and buying back stock under the $4B plan (~19-21M shares
repurchased so far); joined the Russell 1000 this cycle. Stock up +48.0%
since the $15.43 cost basis; recorded compliance status is still "compliant".
[Timothy Sykes (Aug 20)](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/) ·
[StocksToTrade (Aug 21)](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_21/) ·
[PR Newswire — ETH holdings update](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check still disagrees with the recorded status — see
Action Flag #1, unchanged from the last run. The holding file also remains
incomplete: no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` have been filled in, six weeks after the
position was opened.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, not the price action, and it has now gone
unresolved for a second consecutive report.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 2026 subscription revenue grew 24.5% YoY; AI ACV
crossed $1B; two sell-side price-target raises this month (BofA to $150,
Wells Fargo to $175). DCF shows only a modest ~6.5% premium to intrinsic
value — not an extreme gap.
[Barchart](https://www.barchart.com/story/news/1001215/servicenow-earnings-preview-what-to-expect) ·
[ServiceNow Q2 2026 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum still
negative (-11.8%) despite the analyst enthusiasm; next earnings confirmed
for 2026-10-27/28, ~66-67 days out — still no near-term binary catalyst to
react to yet.
[Nasdaq — earnings dates](https://www.nasdaq.com/market-activity/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two straight runs of a ratio-precheck fail. Nothing in the
  automated pipeline will re-flag this on its own until the recorded status
  is updated — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $22.83 | -96.9% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $128.48 | -6.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 71 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 6 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, 149 raw names)
and rewrote **`leads.md`** (top 50 by max-benefit rank). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
without one (6 new cards — PAAS, YUMC, ASND, SMCIP, XOM, JAZZ; 44 existing
cards left unchanged). **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

12 of the 50 leads clear to LEAD tier this run (the rest are capped at
RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| ULTA | LEAD | existing | 20.0:1 | earnings 2026-08-27 | 5 |
| VICR | LEAD | existing | 19.4:1 | earnings 2026-10-20 | 59 |
| CIEN | LEAD | existing | 9.4:1 | earnings 2026-09-03 | 12 |
| SNX | LEAD | existing | 8.4:1 | earnings 2026-09-24 | 33 |
| AA | LEAD | existing | 7.0:1 | earnings 2026-10-15 | 54 |
| CRDO | LEAD | existing | 7.1:1 | earnings 2026-09-01 | 10 |
| TER | LEAD | existing | 5.7:1 | earnings 2026-10-21 | 60 |
| ZS | LEAD | existing | 5.5:1 | earnings 2026-09-03 | 12 |
| LRCX | LEAD | existing | 3.8:1 | earnings 2026-10-21 | 60 |
| TSLA | LEAD | existing | 3.5:1 | earnings 2026-10-21 | 60 |
| GWRE | LEAD | existing | 3.3:1 | earnings 2026-09-03 | 12 |
| NVDA | LEAD | existing | 3.2:1 | earnings 2026-08-26 | 4 |

New to the LEAD tier this run: TER, LRCX, TSLA (all sit at the 60-day
catalyst-horizon edge — verify the earnings date hasn't slipped before
treating any as forward-looking). Dropped off the LEAD tier since last run:
ADI (earnings already passed).

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — no longer in this run's discovered pool (dropped out of the
  top-50); its unresolved government/defense business-activity question from
  prior runs is moot for now but would resurface if it re-enters a future run.
- **CDE, AR, AGI, KGC** — the recurring precious-metals/mining cluster;
  mining-royalty financing structures raised the same open question in
  earlier runs. Still worth a real screen before spending review time on any
  of these cards.
- **38 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — second consecutive run] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has now disagreed with the recorded
   "compliant" status for two straight reports (2026-08-19 and today) on the
   business-activity question specifically. This is the largest compliance
   question in the book (20.2% weight, +48.0% return) and the automated
   pipeline will NOT re-surface it beyond flagging it every run — see the
   COMPLIANCE_GATE note above.
2. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, six weeks after the position was
   opened.
3. **[Time-boxed] NOW earnings confirmed ~2026-10-27/28** — ~66-67 days out;
   no action needed yet, but track the AI ACV / Armis integration narrative
   and the BofA/Wells Fargo target raises between now and then.
4. **[Housekeeping] 6 new DRAFT setup cards** added this run (71 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Rallies As Ethereum Treasury Strategy Takes Center Stage — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)
- [BMNR Stock Rides Ethereum Treasury And Buyback Wave — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_21/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.82 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)
- [ServiceNow Earnings Preview: What to Expect — Barchart](https://www.barchart.com/story/news/1001215/servicenow-earnings-preview-what-to-expect)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow, Inc. Common Stock (NOW) Earnings Report Dates — Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings)
