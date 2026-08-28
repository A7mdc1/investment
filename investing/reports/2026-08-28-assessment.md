# Portfolio Assessment — 2026-08-28

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, full pool, top 50 kept per `discover_top_n:
50`) → `scaffold.py --all-leads` (10 new DRAFT setup cards auto-filled: LLY,
BLSH, BKR, ASND, AAPL, SMTC, PR, APA, SMCIP, TECK; 40 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run — still no `transactions.csv` (discipline guard stays dormant).

No trades recorded since the last report (2026-08-19); holdings are
unchanged (BMNR, NOW).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.13**, up
**+56.4%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — this is now the second consecutive run flagging it, and it remains
unresolved.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -20.4:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $24.15 price -> -97.0% (model doesn't fit a crypto-treasury business — see caveat) |
| Trailing stop (chandelier) | $23.008 — price ~4.7% above it (tightened materially since last run's 18.4% cushion) |
| 6m momentum (skip last month) | -4.7% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check only reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction), or price closing below $23.01 |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$143.73**, **+25.0%** vs. $114.97 cost basis — up sharply (+11.7%)
since the last report's $128.63.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.35:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $143.73 price -> -16.4% (price now meaningfully rich to the model, wider than -6.6% last run) |
| Trailing stop (chandelier) | $126.294 — price ~12.1% above it |
| 6m momentum (skip last month) | +1.9% (flipped positive from -5.3% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.13 | 10 | $15.43 | $241.30 | +56.4% | 19.3% |
| NOW | $143.73 | 7 | $114.97 | $1,006.11 | +25.0% | 80.7% |

**Total value: $1,247.41** | Cost: $959.09 | **Total return: ~+30.1%** (+$288.32 unrealised)

Both positions gained since 2026-08-19 (+$141.90 combined). Concentration in
NOW is essentially unchanged (80.7% vs 81.4%) — still a function of BMNR's
small share count, not a deliberate sizing decision recorded anywhere.

## Action flags (priority order)

1. **[Mandate — unresolved, 2nd run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`, against the recorded
   `compliant` status (broker app, screened 2026-07-07, now seven weeks
   old). Fresh web research this run: BMNR's ETH treasury grew to ~5.85M ETH
   (~$14.8B, ~4.8% of ETH supply), staking revenue is now projected at
   ~$250-287M annualized, and buybacks have passed 19M shares repurchased
   since July 1 — the profile (yield income off a large financial-asset
   treasury) is unchanged from last run's read and still resembles what a
   business-activity screen is built to catch. Per this repo's own Gate 1
   ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL regardless
   of the now +56.4% return. **recommend.py's "would buy today" check still
   only reads the recorded field and stays silent on this.** No evidence of
   a re-screen since last report — this is the priority follow-up.
   [The Block](https://www.theblock.co/treasuries/bmnr) ·
   [StocksToTrade (Aug 24)](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_24-2/)
2. **[Valuation / NOW] P/E ~119 (recorded) still rich** — VALUATION_RICH
   holds. Note the recorded `pe: 119.02` and `last_price: 106.40` fields in
   `now-servicenow.md` are stale (live price is $143.73, +35% above the
   recorded figure) — the real trailing P/E is now higher than 119, not
   lower, so this flag understates rather than overstates. Worth refreshing
   those fields.
3. **[DCF caveat / BMNR]** The -97.0% DCF "downside" is still not a
   meaningful signal — the model (5% growth, 10% discount, no BMNR-specific
   override) doesn't fit a crypto-treasury business valued on ETH holdings
   and staking yield, not discounted operating cash flow.
4. **[Catalyst / NOW]** Confirmed via web research: Q3 FY2026 earnings land
   **2026-10-28** (61 days out — outside the 60-day catalyst-horizon
   default by one day). Q2 results (reported since last run's writeup)
   showed subscription revenue +24.5% YoY, AI ACV past $1B, and full-year
   subscription guidance raised to $15.76-15.78B (+22.5% YoY); the stock is
   reported up ~29% over the trailing month.
   [24/7 Wall St. (Aug 25)](https://247wallst.com/investing/2026/08/25/servicenow-just-ripped-29-in-a-month-what-would-it-take-to-get-now-stock-up-to-150/) ·
   [ServiceNow Newsroom Q2 2026](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
5. **[Discovery] 50 leads this run**, only 10 clearing to LEAD tier (up from
   9 last run) — the rest capped at RESEARCH by the asymmetry/catalyst
   gates. **PLTR dropped out of the top-50 pool entirely this run** (was
   carried in prior runs with an unresolved defense/government
   business-activity question — nothing to re-flag since it's no longer
   surfaced, but the underlying question was never resolved, only mooted by
   ranking). The precious-metals/mining cluster (CDE, AR, AGI, IAG, KGC,
   EGO) is still present at RESEARCH tier with the same open
   royalty-financing compliance question raised in prior runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH treasury continues to scale — ~5.85M ETH
held (~$14.8B, ~4.8% of global ETH supply) as of late August, staking
revenue projected at ~$250-287M annualized, and the buyback program has
repurchased 19M+ shares since July 1. Stock up +56.4% since the $15.43 cost
basis; recorded compliance status is "compliant."
[The Block](https://www.theblock.co/treasuries/bmnr) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_24-2/)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check has now disagreed with the recorded "compliant"
status for two consecutive runs with no re-screen in between. The holding
file is still missing PM-grade fields — no `thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, or `pre_mortem` — so there is
still no independent conviction record to weigh against the compliance
question. The trailing stop has also tightened to just 4.7% below price,
narrower than last run's 18.4% cushion, worth noting given `trade_type:
core` exempts this position from the technical TRAIL_STOP rule.

**Verdict: HOLD (no technical rule fired) — the compliance question is
seven weeks old and still the thing to resolve first, not the price action.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 2026 beat with subscription revenue +24.5% YoY, AI ACV
past $1B, and full-year guidance raised to $15.76-15.78B subscription
revenue (+22.5% YoY); stock reported up ~29% over the trailing month as the
market re-rates the agentic-AI narrative. 6m momentum flipped positive
(+1.9%) this run.
[24/7 Wall St.](https://247wallst.com/investing/2026/08/25/servicenow-just-ripped-29-in-a-month-what-would-it-take-to-get-now-stock-up-to-150/) ·
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 (recorded, now stale-low) keeps VALUATION_RICH
active; DCF gap widened to -16.4% (from -6.6% last run) as price outran the
model; next earnings confirmed 2026-10-28, 61 days out — just past the
60-day catalyst-horizon default, so still no near-term binary event inside
the window.
[Nasdaq earnings calendar](https://www.nasdaq.com/market-activity/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: still only reads the *recorded*
  Shariah field, so it stays silent on the ratio-precheck fail for a second
  straight run. Nothing in the automated pipeline will re-flag this on its
  own — the follow-up is still on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does not fire for either (`trade_type: core`
  exempts both); BMNR's cushion to its chandelier stop has narrowed to 4.7%
  this run, worth watching even though the rule is exempted.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.15 | -97.0% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $143.73 | -16.4% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 74 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 10 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one — 10 new cards this run
(LLY, BLSH, BKR, ASND, AAPL, SMTC, PR, APA, SMCIP, TECK); 40 existing cards
left unchanged. **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.**

10 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| CIEN | existing | 17.7:1 | earnings 2026-09-03 | 6 |
| CRDO | existing | 7.8:1 | earnings 2026-09-01 | 4 |
| STX | existing | 9.5:1 | earnings 2026-10-27 | 60 |
| ZS | existing | 4.3:1 | earnings 2026-09-03 | 6 |
| AA | existing | 14.5:1 | earnings 2026-10-15 | 48 |
| LRCX | existing | 8.8:1 | earnings 2026-10-21 | 54 |
| MU | existing | 4.9:1 | earnings 2026-09-30 | 33 |
| SNX | existing | 5.4:1 | earnings 2026-09-24 | 27 |
| TSLA | existing | 7.8:1 | earnings 2026-10-21 | 54 |
| BKR | new (draft) | 5.0:1 | earnings 2026-10-22 | 55 |

STX is new to LEAD tier this run (was RESEARCH last run at 4.5:1 R:R —
now 9.5:1 as price and target formulas moved).

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — no longer in the top-50 pool this run; its prior
  defense/government business-activity question was never resolved, only
  dropped from view by ranking. Re-check if it resurfaces.
- **CDE, AR, AGI, IAG, KGC, EGO** — the recurring precious-metals/mining
  cluster, still RESEARCH tier; the mining-royalty financing structure
  question from earlier runs remains open.
- **40 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — unresolved for 2 runs] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has now disagreed with the recorded
   "compliant" status across this run and last (2026-08-19). This is the
   largest compliance question in the book (19.3% weight, +56.4% return)
   and the automated pipeline will not re-surface it on its own.
2. **[Housekeeping] BMNR holding file still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, seven weeks after the position was
   opened.
3. **[Housekeeping] NOW holding file has stale price/PE fields** —
   `last_price: 106.40` and `pe: 119.02` are well behind the live $143.73;
   refresh so signals.py's valuation flag reflects the real multiple.
4. **[Time-boxed] NOW earnings confirmed 2026-10-28** — 61 days out; no
   action needed yet, track the AI ACV / subscription-guidance narrative
   between now and then.
5. **[Housekeeping] 10 new DRAFT setup cards** added this run (74 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [BMNR Stock Rallies As Ethereum Treasury Strategy Scales Up — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_24-2/)
- [BMNR Stock Rides Ethereum Treasury And Buyback Wave — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_21/)
- [ServiceNow Just Ripped 29% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/08/25/servicenow-just-ripped-29-in-a-month-what-would-it-take-to-get-now-stock-up-to-150/)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow, Inc. Common Stock (NOW) Earnings Report Dates — Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings)
