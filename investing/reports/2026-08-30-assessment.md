# Portfolio Assessment — 2026-08-30

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 of the configured pool kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (12 new DRAFT setup cards
auto-filled — NTNX, BBY, LLY, BKR, BLSH, AAPL, SMTC, ASND, PR, EXPE, SMCIP,
APA; 38 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` still shows 0 closed trades — no
`transactions.csv` yet (discipline guard stays dormant).

**Since the last report (2026-08-19):** no new trades recorded. Both
holdings ran hard: BMNR is up another ~16% and NOW up ~13% since that run
(price only — nothing was bought or sold in between).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$23.80**, up
**+54.2%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — this is the 2nd consecutive run flagging it, unresolved since
2026-08-19.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -27.9:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $23.80 price -> -97% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.9725 — price ~3.6% above it (tightest cushion of the two holdings) |
| 6m momentum (skip last month) | -4.7% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail (see below) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50 — see
staleness note in Action Flags, the recorded P/E predates the recent rally
and likely understates the current multiple). Live price **$144.71**,
**+25.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.4:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $144.71 price -> -17% (gap to the model widened vs. last run's -6.6% — price ran faster than the DCF assumptions) |
| Trailing stop (chandelier) | $126.5009 — price is ~14.4% above it |
| 6m momentum (skip last month) | +1.9% (turned positive since last run's -5.3%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $23.80 | 10 | $15.43 | $238.00 | +54.2% | 19.0% |
| NOW | $144.71 | 7 | $114.97 | $1,012.97 | +25.9% | 81.0% |

**Total value: $1,250.97** | Cost: $959.09 | **Total return: ~+30.4%** (+$291.88 unrealised)

Both positions rallied hard since 2026-08-19 (BMNR +16%, NOW +13% price-only),
so the book's weighting barely moved (19.0%/81.0% now vs. 18.6%/81.4% then) —
NOW's dollar gain is simply much larger given its 81% weight.

## Action flags (priority order)

1. **[Mandate — still open, 2nd run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`. This has not been
   re-screened since it was first raised in the 2026-08-19 report; the
   recorded `compliant` status is unchanged (broker app, screened
   2026-07-07). Current reporting continues to describe BitMine as an
   Ethereum-treasury company funding buybacks and staking-yield distributions
   off a large financial-asset balance sheet ($14.9B combined crypto/cash/
   securities as of 2026-08-24, ~5.85M ETH staked for ~2.67% annualized
   yield) — a profile that keeps landing on the same side of the
   business-activity question a Capital-Markets classification is built to
   catch. Per this repo's own Gate 1 ("Shariah knockout — non-compliant /
   ratio-or-business flag -> AVOID/SELL, absolute"), a confirmed fail would
   be a hard SELL, independent of the +54.2% return. `recommend.py`'s
   "would buy today" check still only reads the recorded field and stays
   silent on this. This is now tracking the same multi-run pattern that
   took 7 runs to resolve with FIG — worth closing out before it repeats.
2. **[Valuation / NOW] Recorded P/E ~119 fires VALUATION_RICH — likely stale.**
   The `pe` field on the holding card was recorded against `last_price:
   $106.40`; the live price is now $144.71 (+36% higher), so the true
   current multiple is almost certainly richer than 119, not just equal to
   it. Worth refreshing the recorded P/E so the rule is measuring today's
   price, not late-June's.
3. **[DCF caveat / BMNR]** The -97% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business whose
   value tracks ETH holdings and staking yield, not discounted operating
   cash flow. Treat this as a data gap, not a valuation call.
4. **[Catalyst / NOW] Next earnings now ~2026-10-27 — inside the 60-day
   catalyst horizon (58 days out).** Q2 FY2026 was already reported (subscription
   revenue +24.5% YoY, AI ACV past $1B, RPO ~$29B) and Bank of America raised
   its price target to $150 (from $130) on 2026-08-19. The holding card's
   `catalyst.date` field is still `null` — updating it to 2026-10-27 would let
   the automated catalyst gate actually see this window instead of relying on
   this report to carry it manually.
5. **[Discovery] 50 leads this run, 18 clearing to LEAD tier** (up sharply
   from 9 last run) — see the Draft & planned setups section. **PLTR** has
   dropped out of the top 50 this run (no longer carried over). The
   precious-metals/mining cluster (CDE, AGI, KGC, AU) is still recurring —
   same open business-activity question flagged in prior runs, nothing new
   to add.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Combined crypto/cash/securities holdings
reached $14.9B as of 2026-08-24 (5.85M ETH, ~4.8-5% of global supply, 210
BTC), with 7-day annualized staking yield of 2.67% supporting ~$330M in
projected annualized staking revenue. Added to the Russell 1000 on
2026-06-26. Stock ran from $17.28 (2026-07-31) to ~$24.90 (2026-08-25), a
~40% move in under four weeks; up +54.2% since the $15.43 cost basis.
[Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-bmnr-151249411.html) ·
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-and-staking-revenues)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check still disagrees with the recorded status — see
Action Flag #1, now unresolved for a 2nd consecutive run. The holding file
remains incomplete: no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` filled in — there is still no PM-grade
record to weigh the compliance question against beyond the mechanical
LOW-conviction default, six weeks after the position was opened.

**Verdict: HOLD (no technical rule fired) — the compliance question is
still the thing to resolve first, not the price action, and it's now been
open for two consecutive review cycles.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 subscription revenue +24.5% YoY (23% cc), total
revenue +24%, AI ACV past $1B, RPO ~$29B. Bank of America raised its price
target to $150 from $130 (2026-08-19) with a Buy rating. A new partnership
with Tech Mahindra (announced 2026-08-20) extends AI-driven workflow
solutions on the platform. 6m momentum turned positive (+1.9%) since last
run's -5.3%, and DCF gap, while wider in dollar terms, reflects price
outrunning the model rather than a deteriorating fundamental picture.
[TheStreet](https://www.thestreet.com/investing/stocks/now-servicenow-stock-bank-of-america-raises-now-stock-price-target-august-2026) ·
[ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-holds-above-128-as-ai-deals-and-strong-q2-earnings/69986376)

**Case to watch:** Recorded P/E ~119 keeps VALUATION_RICH active and is
likely stale-understated given the price move since it was recorded (see
Action Flag #2); DCF now shows -17% (price further above intrinsic value
than last run). Next earnings ~2026-10-27 is inside the 60-day catalyst
horizon for the first time this cycle — a real near-term event to plan
around rather than "dead money."
[CNBC](https://www.cnbc.com/quotes/NOW) ·
[StockTitan](https://www.stocktitan.net/news/NOW/)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite the ratio-precheck fail for a 2nd straight run. Nothing in
  the automated pipeline will re-flag this on its own until the recorded
  status is updated — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add (and refresh the
  recorded P/E — see Action Flag #2).
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless, though BMNR's cushion
  (~3.6%) is now noticeably tighter than NOW's (~14.4%).
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $23.80 | -97% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $144.71 | -17% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 65 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 12 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one: 12 new cards (NTNX,
BBY, LLY, BKR, BLSH, AAPL, SMTC, ASND, PR, EXPE, SMCIP, APA); 38 existing
cards left unchanged. **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

18 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run
— the rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| CIEN | LEAD | existing | 17.7:1 | earnings 2026-09-03 | 4 |
| AA | LEAD | existing | 11.3:1 | earnings 2026-10-15 | 46 |
| STX | LEAD | existing | 9.7:1 | earnings 2026-10-27 | 58 |
| LRCX | LEAD | existing | 10.0:1 | earnings 2026-10-21 | 52 |
| CRDO | LEAD | existing | 7.6:1 | earnings 2026-09-01 | 2 |
| AGI | LEAD | existing | 7.3:1 | earnings 2026-10-28 | 59 |
| TSLA | LEAD | existing | 6.7:1 | earnings 2026-10-21 | 52 |
| UTHR | LEAD | existing | 5.7:1 | earnings 2026-10-28 | 59 |
| SNX | LEAD | existing | 5.8:1 | earnings 2026-09-24 | 25 |
| AVT | LEAD | existing | 5.6:1 | earnings 2026-10-28 | 59 |
| LLY | LEAD | new | 5.5:1 | earnings 2026-10-29 | 60 |
| GDDY | LEAD | existing | 4.6:1 | earnings 2026-10-29 | 60 |
| ZS | LEAD | existing | 4.5:1 | earnings 2026-09-03 | 4 |
| BKR | LEAD | new | 4.8:1 | earnings 2026-10-22 | 53 |
| HAS | LEAD | existing | 3.7:1 | earnings 2026-10-22 | 53 |
| MU | LEAD | existing | 4.0:1 | earnings 2026-09-30 | 31 |
| SIMO | LEAD | existing | 4.0:1 | earnings 2026-10-29 | 60 |
| CDE | LEAD | existing | 3.2:1 | earnings 2026-10-28 | 59 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** has dropped out of the top 50 this run — no longer carried over;
  its prior government/defense business-activity question is moot for now
  unless it resurfaces in a later run.
- **CDE, AGI, KGC, AU** — the recurring precious-metals/mining cluster;
  mining-royalty financing structures raised the same open question in
  earlier runs. Still worth a real screen before spending review time on
  any of these cards; size as one correlated bet if pursued.
- **32 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — unresolved 2nd run] BMNR Shariah re-screen**: the mechanical
   ratio pre-check still disagrees with the recorded "compliant" status on
   the business-activity question specifically. This is the largest
   compliance question in the book (19.0% weight, +54.2% return) and the
   automated pipeline will NOT re-surface it on its own — see the
   COMPLIANCE_GATE note above. This is the same multi-run pattern the FIG
   position took 7 runs to resolve.
2. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, six weeks after the position was
   opened.
3. **[Data hygiene] NOW's recorded P/E (~119, priced off $106.40) is stale**
   — refresh it against the live $144.71 price so VALUATION_RICH reflects
   today's multiple, and fill in `catalyst.date: 2026-10-27` now that
   earnings sit inside the 60-day horizon.
4. **[Housekeeping] 12 new DRAFT setup cards** added this run (65 total in
   `setups/`); none are `planned`. Review at your own pace — CIEN and CRDO
   (highest R:R, nearest catalysts among LEAD-tier) are the closest to
   actionable if you choose to underwrite either.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Why BitMine Immersion Technologies (BMNR) Is Up 13.1% After Targeting 5% of All Ethereum — Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-bmnr-151249411.html)
- [BitMine Highlights Massive Ethereum Treasury and Staking Revenues — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-and-staking-revenues)
- [BMNR Stock Rides Ethereum Staking Wave And Aggressive Buybacks — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)
- [BMNR Stock Jumps As Massive Ethereum Treasury Draws Traders — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_25/)
- [ServiceNow investors must consider latest alert from Bank of America — TheStreet](https://www.thestreet.com/investing/stocks/now-servicenow-stock-bank-of-america-raises-now-stock-price-target-august-2026)
- [ServiceNow stock holds above $128 as AI deals and strong Q2 earnings support outlook — ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-holds-above-128-as-ai-deals-and-strong-q2-earnings/69986376)
- [NOW: ServiceNow Inc - Stock Price, Quote and News — CNBC](https://www.cnbc.com/quotes/NOW)
- [Servicenow (NOW) Stock News & Updates — StockTitan](https://www.stocktitan.net/news/NOW/)
