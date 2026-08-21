# Portfolio Assessment — 2026-08-21

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50 names kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (5 new DRAFT setup cards auto-filled — PAAS, SMCIP,
ASND, EXPE, XOM; 45 existing cards left unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` not run separately — still no
`transactions.csv` (discipline guard stays dormant).

**Since the last report (2026-08-19):** no trades. Both positions are up
modestly on price; the open item from last run — BMNR's mechanical Shariah
ratio pre-check disagreeing with its recorded "compliant" status — is
**still unresolved and unchanged**.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$22.98**, up
**+48.9%** vs. the $15.43 cost basis. **Action Flag #1 carries over
unchanged: the mechanical Shariah business-activity pre-check still
disagrees with the recorded "compliant" status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.1:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $22.98 price -> -96.9% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $19.3051 — price ~19.0% above it |
| 6m momentum (skip last month) | -17.6% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail (see below) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$129.82**, **+12.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $129.82 price -> -7.5% (price modestly rich to the model) |
| Trailing stop (chandelier) | $111.0214 — price is ~14.5% above it |
| 6m momentum (skip last month) | -11.8% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $22.98 | 10 | $15.43 | $229.75 | +48.9% | 20.2% |
| NOW | $129.85 | 7 | $114.97 | $908.95 | +12.9% | 79.8% |

**Total value: $1,138.70** | Cost: $959.09 | **Total return: ~+18.7%** (+$179.61 unrealised)

Concentration eased slightly vs. last run (BMNR 18.6% -> 20.2%, NOW 81.4% ->
79.8%) purely from BMNR's larger price gain — still no deliberate sizing
decision recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — carried over, unchanged] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`, against the recorded
   `compliant` status (broker app, screened 2026-07-07 — now 45 days old).
   This is the same open question flagged 2026-08-19: BMNR's own reporting
   describes an Ethereum-treasury business model (ETH staking revenue,
   large crypto/cash treasury, buyback + preferred dividends funded off
   that treasury) — a profile closer to a financial/investment vehicle than
   an operating tech company, and exactly what a business-activity screen
   is built to catch. Per Gate 1 ("Shariah knockout — non-compliant /
   ratio-or-business flag -> AVOID/SELL, absolute"), a confirmed fail would
   be a hard SELL, independent of the now +48.9% return. **This is the
   second consecutive report carrying this flag with no re-screen done —
   the position has grown from +33.1% to +48.9% while the compliance
   question sits open.**
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF caveat / BMNR]** The -96.9% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model does not fit a crypto-treasury
   business whose value is driven by ETH holdings and staking yield, not
   discounted operating cash flow. Treat as a data gap, not a valuation call.
4. **[Catalyst / NOW]** Next earnings still land **~2026-10-28** (68 days
   out — outside the 60-day catalyst-horizon default). Since last run: Bank
   of America raised its price target to $150 (from $130, buy rating) on
   2026-08-20, and ServiceNow announced an expanded multi-year Tech Mahindra
   partnership the same day to push enterprise AI from pilots into
   production. Stock gained ~2.0% on the news.
   [The Motley Fool](https://www.fool.com/investing/2026/08/20/why-servicenow-stock-topped-the-market-on-thursday/) ·
   [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/08/61337127/servicenow-stock-shows-strong-momentum-whats-happening-today)
5. **[Discovery] 50 leads this run**, 9 clearing to LEAD tier (ULTA, CIEN,
   CRDO, DELL, ZS, SNX, VICR, GWRE, AA); the rest capped at RESEARCH by the
   asymmetry/catalyst gates. ADI dropped out of LEAD tier this run (its
   next earnings moved out to 2026-11-24, past the catalyst horizon); DELL
   and VICR are new to the LEAD tier. The precious-metals/mining cluster
   (AGI, AR, CDE, KGC, EGO, IAG) still sits at RESEARCH — same open
   business-activity question flagged in prior runs. PLTR fell out of the
   top-50 pool this run (no longer scored) — its prior government/defense
   flag is simply not re-surfaced, not resolved.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continuing to grow its core Ethereum
position — bought another 9,926 ETH on 2026-08-17, taking total holdings to
5.82M ETH (~$13.2B) — while continuing the $4B buyback. Stock traded up
~5.0% on 2026-08-20 on sector-wide crypto-mining strength. Up +48.9% since
the $15.43 cost basis; recorded compliance status is still "compliant."
[StocksToTrade — Aug 20](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check still disagrees with the recorded status — see
Action Flag #1, unchanged since the last report. The holding file remains
incomplete: no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` filled in, five-plus weeks after the
position was opened — there is still no PM-grade record to weigh the
compliance question against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — the compliance question is
still the thing to resolve first, not the price action, and it is now two
reports old.**

### NOW — ServiceNow, Inc
**Case to keep:** Fresh sell-side support this run — Bank of America raised
its price target to $150 (from $130) on 2026-08-20, and the newly expanded
Tech Mahindra partnership targets moving enterprise AI from pilot to
production scale. DCF shows only a modest ~7.5% premium to intrinsic
value — not an extreme gap.
[The Motley Fool](https://www.fool.com/investing/2026/08/20/why-servicenow-stock-topped-the-market-on-thursday/)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum still
negative (-11.8%) despite the rally; next earnings not until ~2026-10-28, so
still no near-term binary catalyst to react to.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite the ratio-precheck fail — same gap flagged last run, still
  open. Nothing in the automated pipeline will re-flag this on its own
  until the recorded status is updated.
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
| BMNR | $0.72 | $22.98 | -96.9% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $129.82 | -7.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 70 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 5 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for the 5 leads without one
(PAAS, SMCIP, ASND, EXPE, XOM); 45 existing cards were left unchanged.
**Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to
review and edit, never buys.**

9 of the 50 leads clear to LEAD tier this run (the rest are capped at
RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| ULTA | LEAD | existing | 17.8:1 | earnings 2026-08-27 | 6 |
| CIEN | LEAD | existing | 10.0:1 | earnings 2026-09-03 | 13 |
| CRDO | LEAD | existing | 7.3:1 | earnings 2026-09-01 | 11 |
| DELL | LEAD | existing | 3.7:1 | earnings 2026-09-01 | 11 |
| ZS | LEAD | existing | 6.7:1 | earnings 2026-09-03 | 13 |
| SNX | LEAD | existing | 6.6:1 | earnings 2026-09-24 | 34 |
| VICR | LEAD | existing | 19.4:1 | earnings 2026-10-20 | 60 |
| GWRE | LEAD | existing | 3.3:1 | earnings 2026-09-03 | 13 |
| AA | LEAD | existing | 6.2:1 | earnings 2026-10-15 | 55 |

ADI dropped out of the LEAD tier this run — its next earnings moved to
2026-11-24, past the 60-day catalyst horizon (last run's "earnings today"
snapshot has rolled forward). DELL and VICR are new entrants to LEAD tier.

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** fell out of the top-50 discovery pool this run — its prior
  government/defense business-activity question from earlier runs is
  simply not being re-surfaced, not resolved; worth remembering if it
  reappears in a future run.
- **AGI, AR, CDE, KGC, EGO, IAG** — the recurring precious-metals/mining
  cluster, all RESEARCH tier this run; the mining-royalty financing
  question raised in earlier runs is still open and still worth a real
  screen before spending review time on any of these cards.
- **41 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now two reports old] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status for two consecutive runs (2026-08-19, 2026-08-21) on the
   business-activity question specifically. This is the largest compliance
   question in the book (20.2% weight, now +48.9% return) and the
   automated pipeline will NOT re-surface it further without a screen
   update — see the COMPLIANCE_GATE note above.
2. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, five-plus weeks
   after the position was opened.
3. **[Time-boxed] NOW earnings ~2026-10-28** — 68 days out; no action
   needed yet, but track the AI ACV / Tech Mahindra partnership / Armis
   integration narrative between now and then.
4. **[Housekeeping] 5 new DRAFT setup cards** added this run (70 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Rides Ethereum Staking Wave And Aggressive Buybacks — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)
- [Is Bitmine Immersion Technologies Inc - BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [Why ServiceNow Stock Topped the Market on Thursday — The Motley Fool](https://www.fool.com/investing/2026/08/20/why-servicenow-stock-topped-the-market-on-thursday/)
- [ServiceNow Stock Shows Strong Momentum: What's Happening Today? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/08/61337127/servicenow-stock-shows-strong-momentum-whats-happening-today)
