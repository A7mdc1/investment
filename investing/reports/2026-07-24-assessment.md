# Portfolio assessment — 2026-07-24

Not a financial advisor. This is decision support only: mechanical rules
resolving your own pre-set policy (`rules.md`), plus flags for you to weigh.
Every buy/sell/hold call is yours. Shariah status shown here is a broker-app
recorded flag or a mechanical ratio pre-check — **neither is a fatwa**; verify
independently in Zoya/Musaffa before acting on anything.

Prior assessment: 2026-07-13 (11 days ago). Discovery + scaffold ran live
against Yahoo data this run (not blocked).

## Verdicts (lead with this)

### BMNR — Bitmine Immersion Technologies, Inc → **HOLD**
- Price $15.90 · weight 18.9% of book · return +2.9% vs cost · trailing stop $14.98 (chandelier, ATR-based)
- 6m momentum: -51.5% · R-multiple: n/a (no `initial_stop` on the card)
- Driver: `DEFAULT` — no rule fired.
- **PM record (mechanical proxy, not a real conviction call):** conviction LOW
  (`reward:risk -16.7:1 — skew too thin`, driven by DCF intrinsic value of
  $0.72 vs a $15.90 price — see DCF caveat below); target $0.72 (DCF method,
  clearly not meaningful for this name — see below); stop $14.98; would-buy-today
  flag says yes but that's a mechanical default, not a real underwrite.
- **DCF is not meaningful here.** BMNR is an Ethereum-treasury vehicle
  (~5.78M ETH, ~$10.9B, plus 207 BTC and ~$385M cash — $11.5B total per its
  July 20 update); a discounted-cash-flow model built for an operating
  business produces a near-zero "intrinsic value" against a stock priced on
  its crypto NAV and staking yield, not free cash flow. Treat the DCF
  reward:risk of -16.7:1 as a script artifact, not a real signal — the actual
  investment case here is a call on ETH's price and Bitmine's NAV premium/discount.

### NOW — ServiceNow, Inc → **HOLD**
- Price $97.43-97.49 · weight 81.1% of book · return -15.2% to -15.3% vs cost
- Trailing stop $96.16 (price is still above it, ~1.3% of headroom)
- 6m momentum: -27.0% · Driver: **VALUATION_RICH** — P/E ~119 ≥ `pe_rich` (50) → hold, do not add
- **PM record:** conviction HIGH (`reward:risk 7.7:1 with a stated thesis`);
  target $120.12 (DCF intrinsic value, +23.3% upside); stop $96.16 (-1.3%);
  time horizon core; would-buy-today: yes (mechanical).
- **Material update since the last assessment: Q2 FY2026 earnings reported
  2026-07-22.** Beat estimates — revenue $3.99B, EPS $0.90 vs ~$0.76 consensus
  (+18%), subscription guidance raised to $3.815-3.820B (21-21.5% YoY CC),
  cRPO +19.5% CC, AI now >$1B in annual contract value. Initial reaction was a
  ~4% pop, but the stock reversed to close -3.7% the next session on a
  "sell-the-news" read: the implied 2H subscription guide came in ~$44.5M
  below prior street expectations, and the stock still trades well below its
  200-day average after a ~38% YTD decline coming into the print.
  **Read against your thesis**: the stated growth rate (21-21.5%) is still in
  your own "~21-22% YoY" range — this is *not* your `invalidation` trigger
  (guidance decelerating meaningfully below that band). It's a softer-than-hoped
  2H guide, not a broken thesis. Worth its own line item to watch next quarter,
  not a HOLD-changing fact today.

*Only 2 holdings — concentration rule (`min_names_for_concentration: 4`) is
muted; both names carry a vol-throttle note (BMNR ATR 6.83-6.84%, NOW ATR
6.03%, both above the `vol_throttle_atr_pct: 6` size-down threshold).*

## Snapshot

| Ticker | Price | Shares | Cost basis | Value | Weight | Return |
|---|---|---|---|---|---|---|
| BMNR | $15.90 | 10 | $15.43 | $158.95 | 18.9% | +3.0% |
| NOW | $97.49 | 7 | $114.97 | $682.43 | 81.1% | -15.2% |
| **Total** | | | | **$841.38** | 100% | |

## Action flags (priority order)

1. **[Compliance — new, needs your attention] BMNR ratio pre-check flags a
   business-activity conflict.** The card records `shariah.status: compliant`
   (broker_app, screened 2026-07-07, not stale), but the mechanical
   ratio/business pre-check this run returned `ok: false`:
   *"industry 'Capital Markets' matches 'capital markets' — core business
   fails screen"* (Yahoo classifies BMNR under Financial Services / Capital
   Markets). This is a genuine tension worth resolving, not just a script
   quirk: Bitmine's business model today is an ETH-treasury/staking vehicle
   — holding, staking, and generating yield on a large crypto balance sheet
   — which is a materially different (and more scrutiny-worthy) activity than
   what "compliant, screened 2026-07-07" may have been based on when the
   position was smaller/newer. The last assessment closed a 7-run-unresolved
   compliance flag on FIG the same way this one could linger — recommend
   re-screening BMNR specifically on its treasury/staking business model in
   Zoya/Musaffa before adding to it further, per the holding's own thesis note
   ("screen compliance in Zoya/Musaffa before adding more").
2. **NOW drawdown** (signals.py, priority 2): down -15% vs cost — thesis
   revisit flag. Per the read above, the underlying growth thesis (21%+
   subscription growth) is still intact post-print; the flag is about
   the price move, not a fundamental break.
3. **NOW valuation** (signals.py, priority 3): P/E ~119 — rich; already
   reflected in the VALUATION_RICH verdict driver (hold, don't add).

## Per-holding read

**BMNR — case to keep**: New position (opened 2026-07-13), small gain, index
inclusion (Russell 1000, effective this run's window) should broaden the
institutional buyer base and liquidity; still holds a huge net-cash/crypto
balance sheet with a growing staking-yield stream (~$235-284M annualized
projected). **Case to trim/reconsider**: it's a leveraged, single-asset (ETH)
proxy wrapped in an operating-company shell — B. Riley just cut its price
target to $25 from $33 (still Buy) reflecting ETH-sensitivity and
capital-structure dilution risk; the DCF/reward:risk numbers are not usable
here (see above) so there's no engineered stop/target on the card yet
(`initial_stop`/`target_price` are both null) — an ATR-based trailing stop
($14.98) is the only defined risk line right now. And the compliance
ratio-flag above is unresolved. Neither case is a recommendation — the
Zoya/Musaffa re-screen is the actual gating fact missing here.

**NOW — case to keep**: durable ~21%+ subscription grower, AI-agent (Zurich)
and Armis security-workflow integration are real forward drivers, Q2 beat
cleanly on EPS and revenue, cRPO still growing ~19.5% CC — this is
consensus-in-line-to-slightly-better execution, not deterioration. **Case to
trim/reconsider**: P/E ~119 prices in a lot of that growth already: the
"sell the news" reaction on a softer 2H subscription guide shows the market
has zero patience for anything short of a raise; stock is still ~38% off its
2026 high and well below its 200-day average, meaning momentum (6m: -27%) has
not turned even after a beat; and this one position is 81% of a very small,
2-name book — any position-level shock is a book-level shock.

## Suggested actions (from your own rules — `rules.md`)

- **VALUATION_RICH fired on NOW** (P/E 119.02 ≥ `pe_rich` 50) → your pre-set
  rule says: hold, do not add. No other rule fired for either name this run
  (no HARD_STOP, TRAIL_STOP, MOMENTUM_STOP, EMA_BREAK, THESIS_BREAK,
  TARGET_REACHED, or TIME_STOP triggered — both prices remain above their
  trailing stops).
- Neither holding has a completed `initial_stop`/`target_price`/`invalidation`
  filled in on its own card (BMNR: none of the three; NOW: `initial_stop`,
  `target_price`, `target_method`, `invalidation`, and `conviction` are all
  still `null`/TODO). Per your own PM_FRAMEWORK schema, filling these in is
  what turns the mechanical HOLD into a real, falsifiable position review —
  worth doing for NOW especially given its 81% weight.
- If you execute anything based on this review, run `/apply-trade` so
  holdings + the ledger update.

## DCF

| Ticker | Intrinsic value | Price | Upside | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $15.89 | -95.5% | growth_5y 5%, terminal 2.5%, discount 10% — **not meaningful**, see note above; BMNR isn't a cash-flow-generating operating business in the sense this model assumes |
| NOW | $120.12 | $97.45 | +23.3% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (discovery — leads.md, 50 rows, none are buys)

Discovery ran live this run (2026-07-24) and rebuilt `leads.md` from scratch
(halal-ETF holdings pool + 2 yfinance screens, liquidity-floored). **Every
row is LEAD or RESEARCH by construction — discovery output can never be a
BUY-CANDIDATE**; `recommend.py`'s own `ideas` array is empty because it reads
`watchlist.md` (currently empty — no hand-curated names yet), not `leads.md`.
Scaffold auto-filled 29 new DRAFT setup cards this run for leads that didn't
have one (58 DRAFT cards + 1 already-`planned` template/README exist in
`setups/` in total now); none are reviewed, none carry a human Shariah
screen, none can reach BUY-CANDIDATE without your `status: planned` flip.

Highest-asymmetry / nearest-catalyst LEADs worth a first look (top by
reward:risk among LEAD-labeled rows with a catalyst inside ~3 weeks):

| Ticker | R:R | Score | Catalyst | Days out | Setup card |
|---|---|---|---|---|---|
| BKR | 3.2:1 | 37.4 | earnings 2026-07-26 | 2 | none yet |
| VRNS | 4.9:1 | 51.1 | earnings 2026-07-28 | 4 | HAS card |
| STX | 6.7:1 | 56.7 | earnings 2026-07-28 | 4 | none yet |
| AR | 4.2:1 | 38.4 | earnings 2026-07-29 | 5 | HAS card |
| AGI | 10.5:1 | 16.5 | earnings 2026-07-29 | 5 | none yet |
| FICO | 9.7:1 | 30.1 | earnings 2026-07-29 | 5 | HAS card |
| KGC | 5.2:1 | 22.8 | earnings 2026-07-29 | 5 | none yet |
| MSFT | 8.2:1 | 30.3 | earnings 2026-07-29 (SPUS holding) | 5 | HAS card |
| HBM | 4.7:1 | 27.8 | earnings 2026-07-29 | 5 | none yet |
| GDDY | 5.8:1 | 42.7 | earnings 2026-07-30 | 6 | HAS card |
| AU | 6.9:1 | 23.3 | earnings 2026-07-31 | 7 | HAS card |
| PAY | 4.9:1 | 40.8 | earnings 2026-08-03 | 9 | HAS card |
| ZS | 10.4:1 | 23.1 | earnings 2026-09-02 | 40 | HAS card |
| DUOL | 11.1:1 | 30.0 | earnings 2026-08-05 | 12 | HAS card |
| CDE | 20.0:1 | 19.9 | earnings 2026-08-05 | 12 | HAS card |
| AEM | 20.0:1 | 21.8 | earnings 2026-07-29 | 5 | none yet |
| CLS | 13.8:1 | 23.9 | earnings 2026-07-27 | 3 | none yet |
| PLTR | 16.2:1 | 21.5 | earnings 2026-08-03 | 9 | HAS card |

All cleared the liquidity floor and a clean ratio pre-check only — not a
business-activity screen. Shariah on every card is `unverified` by
construction; `EDGE` is not supplied (score/momentum alone is not a variant
view). Full 50-row list in `leads.md`.

**Notable RESEARCH-capped rows (asymmetry gate failed, i.e. reward:risk below
the discovery floor of 3.0:1) despite otherwise-high mechanical scores:**
DELL (score 81.2 but R:R 0.3:1), DINO (R:R 1.1:1), AAPL (R:R 0.1:1), AMD
(R:R 0.8:1), MT (R:R 1.0:1), LLY (R:R 0.7:1) — a high signal score is not an
edge or an asymmetric setup; these stay RESEARCH until the numbers change.

**Watchlist**: `watchlist.md` has no hand-curated tickers yet — it's still
just the template/instructions. If there are specific names/themes to track
beyond the machine's discovery pool, they belong there.

## Follow-ups (priority order)

1. **[New — compliance] Re-screen BMNR in Zoya/Musaffa on its actual
   business model** (ETH-treasury + staking, not just a generic ratio
   check) — the pre-check's "Capital Markets" business-activity flag is a
   real signal to run down before adding to this position, echoing the FIG
   pattern from the last two reports (an unresolved flag that grew larger
   as the position did).
2. **[Time-boxed, already past] NOW earnings** — reported 2026-07-22, beat
   on EPS/revenue, raised subscription guidance, but 2H guide came in softer
   than hoped and the stock sold off -3.7% the next session. Not a thesis
   break against your own ~21-22% YoY bar; worth a specific note in the
   holding's `.md` (currently has no `variant_view` or `conviction` filled
   in) on what would change your mind given the "sell the news" pattern.
3. **[Housekeeping] Fill in NOW's TODO fields** — `conviction`,
   `variant_view`, `initial_stop`, `target_price`/`target_method`,
   `invalidation`, `pre_mortem` are all still null on the card despite this
   being 81% of the book; BMNR is missing `initial_stop`/`target_price` too.
   These aren't scored against you, but until they're filled the "PM record"
   above is a mechanical placeholder, not a real underwrite.
4. **[Housekeeping] 29 new DRAFT setup cards** added this run (58 total in
   `setups/`, none `planned`). Review at your own pace; earnings dates for
   several land in the next 1-3 weeks (see table above).
5. **[Infrastructure — still open]** No ledger yet (`transactions.csv`
   absent, `journal.py` reports 0/20 closed trades) — start logging trades
   via `/apply-trade` to unlock the discipline guard (net-of-cost vs. SPUS
   benchmark) and per-setup expectancy reporting.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion (BMNR) Reports $11.5B in Crypto and Securities Holdings — GuruFocus](https://www.gurufocus.com/news/8966985/bitmine-immersion-bmnr-reports-115b-in-crypto-and-securities-holdings)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.78 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-78-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-5-billion-302829332.html)
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Traders — Timothy Sykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20/)
- [ServiceNow Q2 2026 Earnings Results: Beat, Raise, Now Stock Rally — IndMoney](https://www.indmoney.com/blog/us-stocks/servicenow-q2-earnings-now-stock-analysis)
- [ServiceNow Inc. (NYSE:NOW) Shares Drop 3.7% After 2026 Outlook Hints at Weaker H2 — ts2.tech](https://ts2.tech/en/servicenow-inc-nysenow-shares-drop-3-7-after-2026-outlook-hints-at-weaker-h2/)
- [ServiceNow (NOW) Rallies As AI-Fueled Q2 Earnings Crush Expectations — Timothy Sykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_07_23/)
