# Portfolio Assessment — 2026-07-06

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps

- Yahoo egress is still blocked in this sandbox (curl 403 via the egress proxy —
  an organization policy block, not something to retry around, 6th consecutive
  run). `discover.py` returned an empty candidate pool again; `dcf.py` and the
  technical block of `verdict.py`/`recommend.py` (chandelier trailing stop, EMA,
  6m momentum, R-multiple, live reward:risk) did not run.
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
irrespective of price). Verdict unchanged for the **fifth consecutive run**
(2026-06-25, 06-26, 06-30, 07-05, 07-06). At the web-sourced intraday price
(~$20.49, July 6 morning), return vs the $21.43 cost basis is approximately
**-4.4%** — down from the +9.5%-driven rally that put FIG at ~$21.34 on
July 2; today's pullback (-4.0% intraday) looks like partial fade of that
index-inclusion/analyst-coverage pop, not a compliance change.

| PM-grade record | |
|---|---|
| Conviction | LOW — COMPLIANCE_GATE overrides all fundamental analysis |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| Reward:risk | null (DATA_GAP, and moot given COMPLIANCE_GATE) |
| Catalyst | Next earnings ~2026-08-18; no compliance-relevant catalyst pending |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50 — hold,
do not add). At the web-sourced price (~$105.74, July 6) vs $114.97 cost
basis, return is approximately **-8.0%** — still well below the
`drawdown_review_pct` (20%) threshold; DRAWDOWN_REVIEW is not confirmed
firing.

| PM-grade record | |
|---|---|
| Conviction | LOW — DATA_GAP; no live reward:risk computable |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| Reward:risk | null (DATA_GAP) |
| Catalyst | Q2 FY26 earnings **2026-07-22** (~16 days out) |
| Would buy today? | Mechanically yes per `recommend.py`, but DATA_GAP on reward:risk means the BUY-CANDIDATE gate isn't cleared |
| What changes verdict | SELL technical trigger, thesis_broken: true, or Shariah flip |

- Trailing stop / R-multiple / 6m momentum: unavailable (data gap as above).
- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot

| Ticker | Stale `last_price` | Web price (approx.) | Shares | Cost basis | Approx. return |
|---|---|---|---|---|---|
| FIG | $19.26 | ~$20.49 (Jul 6, intraday) | 35 | $21.43 | ~-4.4% |
| NOW | $106.40 | ~$105.74 (Jul 6) | 7 | $114.97 | ~-8.0% |

Approx. portfolio value: (35 x $20.49) + (7 x $105.74) = $717.15 + $740.18 = **~$1,457.33**
Cost: (35 x $21.43) + (7 x $114.97) = $750.05 + $804.79 = **$1,554.84**
Approx. total return: **~-6.3%** (-$97.51 unrealised) — a step back from
~-4.4% at the 2026-07-05 report, driven almost entirely by FIG giving back
part of its index-inclusion/analyst-coverage rally.
Weights (approx.): FIG ~49%, NOW ~51%.

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Fifth run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[New / FIG] Findell Capital activist details firming up** — Findell is
   pushing Figma to cut its product portfolio from eight apps to four
   (Design, Dev Mode, FigJam, Make), rein in stock-based comp (~27% of
   revenue vs. Adobe's ~8%), and address governance/conflict-of-interest
   concerns around its Anthropic relationship (Anthropic's new "Claude
   Design" competes directly). Findell's published targets: $40/share
   standalone, $50/share buyout floor (Microsoft/Alphabet named as logical
   suitors). None of this changes the compliance verdict.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add.
4. **[Watch / NOW] Partnership news ahead of Q2 earnings** — Accenture x
   ServiceNow launched an AI-driven cybersecurity/risk-modernization
   offering, and ServiceNow expanded its IBM collaboration (legacy-system
   AI-readiness, solutions expected late 2026). Guggenheim has NOW at Buy
   with a $125 target; Street average target ~$141. Q2 earnings
   (2026-07-22) remains the next real test of the AI-disruption debate.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):**
- Q1 2026: +46% revenue growth to $333.4M; FY26 guidance raised to
  $1.422-1.428B (~35% growth) on AI-product traction (Figma Make, MCP,
  Weave).
- Russell 1000/2500/3000 index inclusion (effective after the 2026-06-26
  close) and Citigroup's Buy initiation ($36 target) drove a two-day,
  +9-11% rally into July 2.
- Even after today's pullback, the stock remains well above its June 25
  closing low (~$16.84).

**Case to exit (compliance + track record):**
- NON-COMPLIANT per your mandate — this overrides the fundamental debate.
  Under your own rules, you do not hold for a rally, an activist campaign,
  or a takeout rumor when the compliance gate is closed.
- The compliance flag has been unresolved since 2026-06-09 — five
  consecutive assessment cycles with no re-screen recorded.
- Today's -4.0% intraday move shows the stock giving back part of last
  week's rally, consistent with a name still trading on event-driven
  flows (index add, activist headlines) rather than a settled thesis —
  more reason a compliance-driven exit shouldn't wait for a "better" price.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:**
- Thesis intact: Now Assist ($1M+ ACV customers) growing >130% YoY per CEO
  commentary — the market's "AI eats SaaS" fear looks, so far, overstated
  relative to actual bookings.
- New enterprise partnerships (Accenture cybersecurity offering, expanded
  IBM legacy-modernization deal) add fresh distribution ahead of Q2
  earnings (2026-07-22, ~16 days out) — within the 60-day horizon, no
  TIME_STOP issue.
- Return vs cost (~-8.0%) is well inside the 20% DRAWDOWN_REVIEW threshold.

**Case to trim / hold off adding:**
- Recorded P/E ~119 (VALUATION_RICH) — growth must keep delivering to
  justify the multiple; any Q2 guidance miss would likely reaccelerate
  selling.
- Down roughly 31-33% YTD on AI-disruption fears; the stock is still well
  below its 52-week high, and the debate isn't resolved until an actual
  earnings print.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: "screened non-compliant -> SELL (exit;
  cure/purify per Zoya/Musaffa)." Unresolved for a fifth consecutive run.
- **VALUATION_RICH fired -> NOW**: "P/E >= pe_rich (50) -> HOLD, do not add."
- **DRAWDOWN_REVIEW NOT confirmed firing -> NOW**: return is ~-8.0% today vs
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
| TSM | Sole leading-edge foundry; pricing power | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | Yes — 10 days | Guiding $39.0-40.2B Q2 revenue (+32% YoY midpoint), 65.5-67.5% gross margin; Citi raised its target on expected 2026 guidance upgrade and reported advanced-node price hikes; stock showed neutral-to-choppy momentum into earnings, with combined Apr/May sales growth (+24% YoY) trailing the Street's +35% bar |
| ISRG | Da Vinci 5 placement ramp; ~zero debt | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | Yes — 10 days | Down ~26-28% YTD on post-Q1 sell-side downgrades (Deutsche Bank, BofA, JPMorgan, HSBC) over instrument-lifetime changes; Goldman Sachs raised its target to $558, arguing the panic misreads the lifetime-change math; stock ticking up into earnings on positioning |
| AMD | DC GPU share-gain vs Nvidia; MI400 ramp | Q2 earnings 2026-08-04 (also "Advancing AI 2026" event 2026-07-23) | RESEARCH (DATA_GAP) | Yes — 29 days | New 52-week high (~$567); Japanese AV startup Turing began running ~10% of its AI training on AMD GPUs (with an AMD venture investment) instead of Nvidia; Wells Fargo/Cantor Fitzgerald raised targets on AI-datacenter CPU demand; stock now +154% YTD |
| QCOM | Auto/IoT diversification vs licensing fears | Q3 FY26 earnings 2026-08-05 | RESEARCH (DATA_GAP) | Yes — 30 days | Fourth straight down session as of early July; analysts downgraded to Hold post-Investor Day on execution/margin risk; Citi placed QCOM on a 30-day negative-catalyst watch (Neutral, $198 target) citing Xiaomi cutting 2026 shipment guidance ~30%; SpaceX AI-phone rumor was debunked by Musk, reversing a brief rally |
| LLY | GLP-1 TAM + oral orforglipron | Q2 earnings 2026-08-05 | RESEARCH (DATA_GAP) | Yes — 30 days | Up ~6.7% over the past week, new 52-week high on 2026-06-26; Medicare GLP-1 coverage expansion live since 2026-07-01 (Walmart/CVS assisting seniors); Leerink raised its target to $1,232 (from $1,119, Outperform) |
| NVDA | AI datacenter super-cycle | Q2 FY27 earnings 2026-08-26 | RESEARCH (DATA_GAP) | Yes — 51 days | Roughly flat YTD (~+5%), drifted down to ~$194.83 on 2026-07-02 (-1.4%); poached a Microsoft exec to lead "Field Operations"; announced an initiative to help emerging cloud firms acquire AI chips; Kyber NVL144 rack-scale system delayed to 2028, pressuring supplier sentiment |

**TSM and ISRG have the nearest catalysts (July 16, 10 days out)** — if you have
access to a live data feed, these two are the priority to underwrite (define
target/stop -> reward:risk -> BUY-CANDIDATE gate check), then screen in
Zoya/Musaffa.

Correlation note: TSM / AMD / QCOM / NVDA are a correlated semiconductor
cluster — size as ONE bet if adding any. LLY and ISRG are the genuine
diversifiers.

## Follow-ups (priority order)

1. **[Urgent — 5th run unresolved] FIG compliance**: Re-screen in Zoya/Musaffa.
   If still non-compliant, execute exit and determine purification amount —
   note the Findell activist campaign (buyout floor $50, standalone target
   $40) makes timing more consequential than usual; this is still a mandate
   decision, not a price call.
2. **[Near-term — 10 days] TSM / ISRG earnings 2026-07-16**: Soonest watchlist
   catalysts. Define target/stop and screen compliance before the earnings
   window if you want to underwrite either.
3. **[Monitor — 16 days] NOW Q2 earnings 2026-07-22**: Thesis-validation event
   for the AI-disruption debate. Re-examine reward:risk with a live data
   source before then.
4. **[Infrastructure] Run `dcf.py` / `verdict.py` / `discover.py` locally**
   (needs unrestricted Yahoo access) — this sandbox has blocked the feed
   across six consecutive runs.
5. **[Infrastructure] No ledger yet** — if you want the discipline guard
   (net-of-cost performance vs. a Shariah benchmark) evaluated in future
   reports, start logging trades to `transactions.csv` (or via `/apply-trade`).

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag, not a fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Figma, Inc. (FIG) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/FIG/)
- [FIG Stock Jumps As Wall Street And Activists Pile In — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_06_26/)
- [Figma Stock Rose 9% This Week: Where FIG Could Go in 2026 — TIKR](https://www.tikr.com/blog/figma-stock-rose-9-this-week-where-fig-could-go-in-2026)
- [Activist Findell seeks changes at 'Adobe slayer' Figma — Investing.com](https://www.investing.com/news/stock-market-news/activist-findell-seeks-changes-at-adobe-slayer-figma-4714498)
- [How AI Strategy And Activist Scrutiny At Figma (FIG) Has Changed Its Investment Story — Simply Wall St News](https://simplywall.st/stocks/us/software/nyse-fig/figma/news/how-ai-strategy-and-activist-scrutiny-at-figma-fig-has-chang)
- [ServiceNow, Inc. (NOW) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/NOW/)
- [ServiceNow (NOW) Stock Chart and Price History — MarketBeat](https://www.marketbeat.com/stocks/NYSE/NOW/chart/)
- [TSMC Stock Analysis: Neutral Momentum Before Q2 Earnings on July 16 — Cryptonomist](https://en.cryptonomist.ch/2026/07/06/tsmc-stock-reverses-27-intraday-as-selling-builds-before-q2-earnings/)
- [Intuitive Surgical Is Down 28%, and Wall Street Is Piling On — The Motley Fool](https://www.fool.com/investing/2026/07/03/intuitive-surgical-is-down-28-and-wall-street-is/)
- [Intuitive Surgical Gains as Investors Appear to Position for Mid-July Earnings — QuiverQuant](https://www.quiverquant.com/news/Intuitive+Surgical+Gains+as+Investors+Appear+to+Position+for+Mid-July+Earnings)
- [AMD (AMD) Stock Trades Up, Here Is Why — StockStory / FinancialContent](https://markets.financialcontent.com/stocks/article/stockstory-2026-7-6-amd-amd-stock-trades-up-here-is-why)
- [Up 140% YTD, Three Catalysts Will Take AMD to New Highs In 2026 — 24/7 Wall St.](https://247wallst.com/investing/2026/07/03/up-140-ytd-three-catalysts-will-take-amd-to-new-highs-in-2026/)
- [Qualcomm Inc Stock (QCOM) Moved Down by 5.10% on Jul 2 — TradingKey](https://www.tradingkey.com/news/market-movers/262007912-market-movers-qcom-20260702)
- [QUALCOMM (QCOM) Stock Just Lost Its Place In Several Russell Indices — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/qualcomm-qcom-stock-just-lost-111028928.html)
- [Lilly Up Around 7% in a Week: Should You Buy, Sell or Hold the Stock? — TradingView](https://www.tradingview.com/news/zacks:489a1f7c5094b:0-lilly-up-around-7-in-a-week-should-you-buy-sell-or-hold-the-stock/)
- [Nvidia Stock Analysis July 2026: AI Chip Demand & Investment Outlook — Intellectia](https://intellectia.ai/blog/nvidia-stock-analysis-july-2026)
- [NVIDIA's AI Compute Partnership Boosts Cloud Firms — GuruFocus](https://www.gurufocus.com/news/8944672/nvidias-ai-compute-partnership-boosts-cloud-firms-stock-ticker-nvda)
