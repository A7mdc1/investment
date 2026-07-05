# Portfolio Assessment — 2026-07-05

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps
- Yahoo egress is still blocked in this sandbox (curl 403 via the egress proxy —
  an organization policy block, not something to retry around). `discover.py`
  returned an empty candidate pool again; `dcf.py` and the technical block of
  `verdict.py`/`recommend.py` (chandelier trailing stop, EMA, 6m momentum,
  R-multiple, live reward:risk) did not run.
- `prices.py` returned `null` for both tickers (no front-matter fallback in that
  script). `signals.py`/`verdict.py` fell back to the stale `last_price` values
  recorded in the holding files (FIG $19.26, NOW $106.40, both dated to the
  2026-06-09 screen). This report uses secondary-source web prices instead
  (sourced below) for the snapshot/return figures — directional, not exact;
  confirm in your brokerage.
- No `transactions.csv`/ledger file exists in this repo yet, so the discipline
  guard (net-of-cost performance vs. a Shariah benchmark) cannot be evaluated
  this run.
- P/E for NOW (119.02) is the recorded front-matter value, not recomputed
  live — treat as approximate given the price has moved since the screen date.

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). Verdict unchanged for the **fourth consecutive run**
(2026-06-25, 06-26, 06-30, 07-05). At the web-sourced price (~$21.34, July 2
close), return vs the $21.43 cost basis is approximately **-0.4%** — a sharp
improvement from ~-11% at the last report, driven by a fundamentals/analyst
rally, not a compliance change.

| PM-grade record | |
|---|---|
| Conviction | LOW — COMPLIANCE_GATE overrides all fundamental analysis |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| Reward:risk | null (DATA_GAP, and moot given COMPLIANCE_GATE) |
| Catalyst | Next earnings ~2026-08-18; no compliance-relevant catalyst pending |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50 — hold,
do not add). At the web-sourced price (~$105.57, July 5) vs $114.97 cost basis,
return is approximately **-8.2%** — still well below the `drawdown_review_pct`
(20%) threshold; DRAWDOWN_REVIEW is not confirmed firing.

| PM-grade record | |
|---|---|
| Conviction | LOW — DATA_GAP; no live reward:risk computable |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| Reward:risk | null (DATA_GAP) |
| Catalyst | Q2 FY26 earnings **2026-07-22** (~17 days out) |
| Would buy today? | Mechanically yes per `recommend.py`, but DATA_GAP on reward:risk means the BUY-CANDIDATE gate isn't cleared |
| What changes verdict | SELL technical trigger, thesis_broken: true, or Shariah flip |

- Trailing stop / R-multiple / 6m momentum: unavailable (data gap as above).
- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot

| Ticker | Stale `last_price` | Web price (approx.) | Shares | Cost basis | Approx. return |
|---|---|---|---|---|---|
| FIG | $19.26 | ~$21.34 (Jul 2 close) | 35 | $21.43 | ~-0.4% |
| NOW | $106.40 | ~$105.57 (Jul 5) | 7 | $114.97 | ~-8.2% |

Approx. portfolio value: (35 x $21.34) + (7 x $105.57) = $746.90 + $738.99 = **~$1,485.89**
Cost: (35 x $21.43) + (7 x $114.97) = $750.05 + $804.79 = **$1,554.84**
Approx. total return: **~-4.4%** (-$68.95 unrealised) — a meaningful improvement
from ~-12% at the 2026-06-30 report, driven almost entirely by FIG's rally.
Weights (approx.): FIG ~50%, NOW ~50%.

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Fourth run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[New / FIG] Citigroup Buy coverage + Russell reconstitution** — FIG jumped
   +9.5% on 2026-07-02 after Citigroup initiated coverage (Buy, $36 target) and
   Figma was added to the Russell 1000/2500/3000 indices (index-fund buying).
   Positive for fundamentals, neutral for the mandate decision.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add.
4. **[Watch / NOW] AI-disruption narrative easing** — NOW is down ~31-33% YTD
   on fears that AI agents cannibalize software subscriptions, but management
   reports Now Assist customers >$1M ACV grew >130% YoY; the stock has already
   rallied ~30% off its recent low. Q2 earnings (2026-07-22) is the next test.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):**
- Q1 2026: +46% revenue growth to $333.4M (accelerating from +40% prior
  quarter); FY26 guidance raised to $1.422-1.428B (~35% growth) on AI-product
  traction (Figma Make, MCP, Weave).
- Citigroup initiated Buy coverage with a $36 target (2026-07-01/02), and
  index inclusion (Russell 1000/2500/3000) added a structural buyer.
- Stock has recovered from deep 2026 lows (~-49% YTD, an -86% peak drawdown
  around June 25) to a two-day, +9-11% move.

**Case to exit (compliance + track record):**
- NON-COMPLIANT per your mandate — this overrides the fundamental debate.
  Under your own rules, you do not hold for a rally or an activist outcome
  when the compliance gate is closed.
- The compliance flag has been unresolved since 2026-06-09 — four consecutive
  assessment cycles with no re-screen recorded.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:**
- Thesis intact: Now Assist ($1M+ ACV customers) growing >130% YoY per CEO
  commentary — the market's "AI eats SaaS" fear looks, so far, overstated
  relative to actual bookings.
- Q2 FY26 earnings land 2026-07-22 (~17 days out) — within the 60-day horizon,
  no TIME_STOP issue; a concrete near-term thesis-validation event.
- Return vs cost (~-8.2%) is well inside the 20% DRAWDOWN_REVIEW threshold.

**Case to trim / hold off adding:**
- Recorded P/E ~119 (VALUATION_RICH) — growth must keep delivering to justify
  the multiple; any Q2 guidance miss would likely reaccelerate selling.
- Down ~31-33% YTD on AI-disruption fears; margin pressure from recent
  acquisitions (e.g. Armis) and Middle East geopolitical headwinds are cited
  as ongoing risks even by bulls.
- Stock is still well below its 52-week high — limited evidence yet that the
  AI-disruption debate is fully resolved either way.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: "screened non-compliant -> SELL (exit;
  cure/purify per Zoya/Musaffa)." Unresolved for a fourth consecutive run.
- **VALUATION_RICH fired -> NOW**: "P/E >= pe_rich (50) -> HOLD, do not add."
- **DRAWDOWN_REVIEW NOT confirmed firing -> NOW**: return is ~-8.2% today vs
  the 20% threshold — no thesis-review requirement triggered.
- No Stage 4 SELL triggers evaluable — technical data (chandelier, EMA,
  momentum) still unavailable from Yahoo in this sandbox.

*If you execute anything from this report, run `/apply-trade` so holdings files
and ledger stay in sync.*

## DCF
Unavailable — Yahoo feed blocked. Recorded assumptions for reference:
- **FIG**: growth_5y 30%, terminal growth 3%, discount rate 12%.
- **NOW**: growth_5y 18%, terminal growth 3%, discount rate 10%.

## New ideas (watchlist)

`discover.py` returned an empty pool again (Yahoo blocked). Watchlist unchanged
from the auto-discovered list. All six remain at **RESEARCH** per
`recommend.py` (DATA_GAP blocks reward:risk computation). All Shariah statuses
remain **UNVERIFIED**.

| Ticker | Candidate angle | Catalyst | Engine verdict | Catalyst in horizon? | Recent news |
|---|---|---|---|---|---|
| TSM | Sole leading-edge foundry; pricing power | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | Yes — 11 days | Stock +45% YTD; guiding $39.0-40.2B Q2 revenue, 65.5-67.5% gross margin; focus is AI/HPC demand + 2nm ramp commentary |
| ISRG | Da Vinci 5 placement ramp; ~zero debt | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | Yes — 11 days | Down ~28% in 2026 on competitive/regulatory concerns post-Q1; several sell-side downgrades, but Goldman raised target to $558 |
| AMD | DC GPU share-gain vs Nvidia; MI400 ramp | Q2 earnings 2026-08-04 (also "Advancing AI 2026" event 2026-07-23) | RESEARCH (DATA_GAP) | Yes — 30 days | Up ~150% YTD; MI400/MI455X launching 2H 2026, ~$7.2B revenue estimate for the series in 2026 |
| QCOM | Auto/IoT diversification vs licensing fears | Q3 FY26 earnings 2026-08-05 | RESEARCH (DATA_GAP) | Yes — 31 days | Down 4 straight sessions into early July; analyst downgrades to Hold on margin/execution risk and Apple in-house-modem threat; new $20B buyback + dividend hike announced |
| LLY | GLP-1 TAM + oral orforglipron | Q2 earnings 2026-08-05 | RESEARCH (DATA_GAP) | Yes — 31 days | Orforglipron (branded Foundayo) FDA-approved for obesity; Medicare GLP-1 Bridge Program launched 2026-07-01 ($50/mo, ~20M eligible patients) — a real incremental catalyst already in the tape |
| NVDA | AI datacenter super-cycle | Q2 FY27 earnings 2026-08-26 | RESEARCH (DATA_GAP) | Yes — 52 days (watchlist.md's "62 days/beyond horizon" note is now stale — recompute; doesn't change the verdict since EDGE/ASYMMETRY gates already cap at RESEARCH) | Stock nearly flat in 2026 (+5% YTD) despite AI capex growth; poached a Microsoft exec for field operations |

**TSM and ISRG have the nearest catalysts (July 16, 11 days out)** — if you have
access to a live data feed, these two are the priority to underwrite (define
target/stop -> reward:risk -> BUY-CANDIDATE gate check), then screen in
Zoya/Musaffa.

Correlation note: TSM / AMD / QCOM / NVDA are a correlated semiconductor
cluster — size as ONE bet if adding any. LLY and ISRG are the genuine
diversifiers.

## Follow-ups (priority order)

1. **[Urgent — 4th run unresolved] FIG compliance**: Re-screen in Zoya/Musaffa.
   If still non-compliant, execute exit and determine purification amount.
2. **[Near-term — 11 days] TSM / ISRG earnings 2026-07-16**: Soonest watchlist
   catalysts. Define target/stop and screen compliance before the earnings
   window if you want to underwrite either.
3. **[Monitor — 17 days] NOW Q2 earnings 2026-07-22**: Thesis-validation event
   for the AI-disruption debate. Re-examine reward:risk with a live data
   source before then.
4. **[Watchlist housekeeping] NVDA catalyst-horizon note in watchlist.md is
   stale** ("62 days/beyond horizon") — now 52 days out and within
   `catalyst_horizon_days` (60); doesn't change the RESEARCH verdict today, but
   update the note so it doesn't mislead on a future run.
5. **[Infrastructure] Run `dcf.py` / `verdict.py` / `discover.py` locally**
   (needs unrestricted Yahoo access) — this sandbox has blocked the feed
   across five consecutive runs.
6. **[Infrastructure] No ledger yet** — if you want the discipline guard
   (net-of-cost performance vs. a Shariah benchmark) evaluated in future
   reports, start logging trades to `transactions.csv` (or via `/apply-trade`).

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag, not a fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Figma, Inc. (FIG) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/FIG/)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [Figma Stock Rose 9% This Week: Where FIG Could Go in 2026 — TIKR](https://www.tikr.com/blog/figma-stock-rose-9-this-week-where-fig-could-go-in-2026)
- [ServiceNow, Inc. (NOW) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/NOW/)
- [ServiceNow Stock Is Down 36% in 2026: Is the Market Making a Category Error on AI? — TIKR](https://www.tikr.com/blog/servicenow-stock-is-down-36-in-2026-is-the-market-making-a-category-error-on-ai)
- [Is ServiceNow Stock a Buy After Its Brutal First Half? — The Motley Fool](https://www.fool.com/investing/2026/07/01/is-servicenow-stock-a-buy-after-its-brutal-first-h/)
- [TSMC Stock Price Forecast — Top Analysts Raise Targets Ahead of Q2 Earnings — TipRanks](https://www.tipranks.com/news/tsmc-stock-price-forecast-top-analysts-raise-targets-ahead-of-q2-earnings)
- [Intuitive Surgical Is Down 28%, and Wall Street Is Piling On — The Motley Fool](https://www.fool.com/investing/2026/07/03/intuitive-surgical-is-down-28-and-wall-street-is/)
- [AMD MI400 Series: $7.2B AI GPU Challenging Nvidia — Tech Insider](https://tech-insider.org/amd-mi400-series-ai-gpu-data-center-2026/)
- [Qualcomm Inc Stock (QCOM) Moved Down by 5.10% on Jul 2 — TradingKey](https://www.tradingkey.com/news/market-movers/262007912-market-movers-qcom-20260702)
- [Lilly Up Around 7% in a Week: Should You Buy, Sell or Hold the Stock? — TradingView](https://www.tradingview.com/news/zacks:489a1f7c5094b:0-lilly-up-around-7-in-a-week-should-you-buy-sell-or-hold-the-stock/)
- [Nvidia Stock Is Nearly Flat for 2026. Time to Cash Out, or Load Up on Shares? — The Motley Fool](https://www.fool.com/investing/2026/07/04/nvidia-stock-is-flat-for-2026-time-to-cash-out-or/)
