# Portfolio Assessment — 2026-08-19

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 149-name raw pool, top 50 kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (33 new DRAFT setup cards
auto-filled; 17 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run (Yahoo was heavily rate-limited; discovery took ~2 runs and
several minutes to complete but returned a full pool). `journal.py` not run
separately — still no `transactions.csv` (discipline guard stays dormant).

**Since the last report (2026-07-13):** FIG was sold — the 7-run compliance
flag is closed (realized P/L +$54.95) — and BMNR was bought as a new
position. That trade is exactly why this run's top finding below matters.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$20.54**, up
**+33.1%** vs. the $15.43 cost basis. **But see Action Flag #1 — the
mechanical Shariah business-activity pre-check now disagrees with the
recorded "compliant" status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.2:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $20.54 price -> -96.5% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $17.3509 — price ~18.4% above it |
| 6m momentum (skip last month) | -13.1% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail (see below) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$128.63**, **+11.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.4:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $128.63 price -> -6.6% (price modestly rich to the model) |
| Trailing stop (chandelier) | $109.1415 — price is ~17.9% above it |
| 6m momentum (skip last month) | -5.3% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $20.54 | 10 | $15.43 | $205.45 | +33.1% | 18.6% |
| NOW | $128.63 | 7 | $114.97 | $900.06 | +11.8% | 81.4% |

**Total value: $1,105.51** | Cost: $959.09 | **Total return: ~+15.3%** (+$146.42 unrealised)

The book is far more concentrated in NOW (81.4%) than it was in the FIG/NOW
split last run — a function of BMNR's small share count (10 shares) relative
to the NOW position, not a deliberate sizing decision recorded anywhere in
the files.

## Action flags (priority order)

1. **[Mandate — NEW this run] BMNR's mechanical Shariah ratio pre-check
   FAILS**, flagging `industry 'Capital Markets' matches 'capital markets' —
   core business fails screen`. This conflicts with the recorded
   `compliant` status (broker app, screened 2026-07-07). Independent web
   research this run supports treating this as a real question, not a
   false positive: BMNR's public reporting describes it as an Ethereum
   *treasury* company — ~98% of last-quarter revenue came from ETH staking,
   it holds $11.4-11.6B in crypto/cash/marketable securities, and it funds
   a $4B buyback plus scheduled preferred-share (BMNP) dividends. That
   profile (yield income off a large financial-asset treasury, financed
   partly through preferred dividends) is close to what a business-activity
   screen is built to catch — closer to a financial/investment vehicle than
   an operating tech company. Per this repo's own Gate 1
   ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail here would be a hard SELL,
   independent of the +33.1% return. **`recommend.py`'s "would buy today"
   check only reads the recorded field and cannot see this — it is silent
   on the new flag.** Re-screen in Zoya/Musaffa on the business-activity
   question specifically, not just the ratio math, before adding to this
   position or treating "compliant" as settled. This is the same category
   of issue that took 7 runs to resolve with FIG, on a position that just
   replaced FIG in the book.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF caveat / BMNR]** The -96.5% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override in the holding file) does not fit a
   crypto-treasury business whose value is driven by ETH holdings and
   staking yield, not discounted operating cash flow. Treat this number as
   a data gap, not a valuation call.
4. **[Catalyst / NOW]** Next earnings land **~2026-10-28** (72 days out —
   outside the 60-day catalyst-horizon default, so no near-term binary
   event). Growth narrative reporting since last run is constructive: AI
   Annual Contract Value crossed $1B with agentic deployments up 9x over
   nine months, and Wells Fargo raised its price target to $175 from $160.
   [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60634491/servicenow-ai-contract-value-crosses-1-billion-milestone-stock-soars) ·
   [24/7 Wall St.](https://247wallst.com/investing/2026/08/12/wall-street-may-be-sleeping-on-this-ai-growth-story-the-stock-has-97-upside/)
5. **[Discovery] 50 leads this run** (up from 20 last run — `discover_top_n`
   was raised to 50 in rules.md), only 9 clearing to LEAD tier; the rest
   capped at RESEARCH by the asymmetry/catalyst gates. **PLTR** carries over
   again with its still-unresolved government/defense business-activity
   question flagged in prior runs — nothing new to add, still open.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Actively growing its core Ethereum position
(5.82M ETH, ~4.8% of global supply per Aug 17 reporting) while returning
capital aggressively — over 20.8M shares repurchased since July 1 under a
$4B buyback, and management projects ~$287M in annualized ETH staking
revenue. Stock up +33.1% since the $15.43 cost basis; recorded compliance
status is "compliant."
[Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_17/) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_17/)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status this run — see
Action Flag #1. Separately, the holding file itself is incomplete: no
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, or
`pre_mortem` have been filled in, so there is no PM-grade record to weigh
the compliance question against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
the thing to resolve first, not the price action.**

### NOW — ServiceNow, Inc
**Case to keep:** Up 57% off its 52-week low per recent coverage; AI ACV
crossed $1B with agentic deployments up 9x in nine months; Wells Fargo raised
its price target to $175; Armis acquisition continues to extend the
AI-security platform story. DCF shows only a modest ~6.6% premium to
intrinsic value — not an extreme gap.
[Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60634491/servicenow-ai-contract-value-crosses-1-billion-milestone-stock-soars) ·
[24/7 Wall St.](https://247wallst.com/investing/2026/08/12/wall-street-may-be-sleeping-on-this-ai-growth-story-the-stock-has-97-upside/)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum still
negative (-5.3%) despite the rally; next earnings not until ~2026-10-28, so
no near-term binary catalyst to react to yet.
[TipRanks](https://www.tipranks.com/stocks/now/earnings) ·
[MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite this run's ratio-precheck fail. That gap is worth naming
  explicitly: nothing in the automated pipeline will re-flag this on its
  own until you update the recorded status — the follow-up is on you.
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
| BMNR | $0.72 | $20.54 | -96.5% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $128.63 | -6.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 63 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 33 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, 149 raw names)
and wrote **`leads.md`** (top 50 by max-benefit rank — `discover_top_n` was
raised from 20 to 50 since last run). `scaffold.py --all-leads` auto-filled a
DRAFT `setups/<ticker>.md` card for every lead without one (33 new cards; 17
existing cards — ULTA, ALAB, CRDO, TSLA, ADI, ZS, AMD, PAY, MU, MSFT, GDDY,
TER, SIMO, AR, CDE, CF, PLTR — left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

Only 9 of the 50 leads clear to LEAD tier this run (the rest are capped at
RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| AA | LEAD | new | 14.4:1 | earnings 2026-10-15 | 57 |
| CIEN | LEAD | new | 8.4:1 | earnings 2026-09-03 | 15 |
| CRDO | LEAD | existing | 5.7:1 | earnings 2026-09-01 | 13 |
| GWRE | LEAD | new | 3.6:1 | earnings 2026-09-03 | 15 |
| ULTA | LEAD | existing | 10.1:1 | earnings 2026-08-27 | 8 |
| ADI | LEAD | existing | 3.5:1 | earnings 2026-08-19 | 0 (today) |
| ZS | LEAD | existing | 4.6:1 | earnings 2026-09-03 | 15 |
| SNX | LEAD | new | 4.1:1 | earnings 2026-09-24 | 36 |

(ADI's earnings date is today per the discovery snapshot — if still accurate,
that catalyst has effectively already arrived; verify before treating the
lead as forward-looking.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI, IAG, KGC, EGO** — the recurring precious-metals/mining
  cluster; mining-royalty financing structures raised the same open question
  in earlier runs. Still worth a real screen before spending review time on
  any of these cards.
- **41 RESEARCH-tier leads** (up sharply from prior runs' smaller pools,
  since `discover_top_n` moved from 20 to 50) — full list in `leads.md`;
  not reproduced here in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — new this run] BMNR Shariah re-screen**: the mechanical
   ratio pre-check disagrees with the recorded "compliant" status on the
   business-activity question specifically. This is now the largest
   compliance question in the book (18.6% weight, +33.1% return) and the
   automated pipeline will NOT re-surface it on its own — see the
   COMPLIANCE_GATE note above.
2. **[Housekeeping] BMNR holding file is missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, five weeks after the position was
   opened.
3. **[Time-boxed] NOW earnings ~2026-10-28** — 72 days out; no action needed
   yet, but track the AI ACV / Armis integration narrative between now and
   then.
4. **[Housekeeping] 33 new DRAFT setup cards** added this run (63 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.
   The FIG sale and BMNR buy should be logged there if not already.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Grinds Higher As Massive Ethereum Bet Draws Traders — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_17/)
- [BMNR Stock Rides Ethereum Treasury Bet And Massive Buybacks — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_17/)
- [BitMine Immersion Technologies (BMNR) – Ethereum's Largest Treasury Company — CoinGecko](https://www.coingecko.com/learn/what-is-bmnr-bitmine-ethereum-treasury-tom-lee)
- [ServiceNow AI Contract Value Crosses $1 Billion Milestone, Stock Soars — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60634491/servicenow-ai-contract-value-crosses-1-billion-milestone-stock-soars)
- [Wall Street May Be Sleeping on This AI Growth Story — 24/7 Wall St.](https://247wallst.com/investing/2026/08/12/wall-street-may-be-sleeping-on-this-ai-growth-story-the-stock-has-97-upside/)
- [ServiceNow (NOW) Is Spending $7.75 Billion On AI Security — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/servicenow-now-spending-7-75-151535988.html)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [NOW Earnings Dates, Upcoming and Historical — MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)
