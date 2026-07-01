# Portfolio Assessment — 2026-07-01

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps
- Yahoo egress is still blocked in this sandbox (curl 403): `discover.py`,
  `dcf.py`, and the technical block of `verdict.py`/`recommend.py` (chandelier
  trailing stop, EMA, 6m momentum, R-multiple, reward:risk) did not run.
- `prices.py` returned `null` for both tickers; this report uses secondary-source
  web prices (sourced below) — directional, not exact. Confirm in your brokerage.
  - **FIG**: ~$18.09 (+2.47% intraday)
  - **NOW**: ~$105.47 (prev close $99.28, day range $101.77–$105.67, +4.05% intraday)
- `signals.py` and `verdict.py` fell back to the stale `last_price` values in the
  holding files (FIG $19.26, NOW $106.40) — all figures below use the web-sourced
  prices instead for accuracy.
- No `transactions.csv`/ledger exists yet (no trades logged) — the discipline
  guard (net-of-cost performance vs. a Shariah benchmark) is not evaluable.

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). Verdict unchanged for the fourth consecutive run. At the
web-sourced price (~$18.09), return vs $21.43 cost basis is approximately **-15.6%**.

| PM-grade record | |
|---|---|
| Conviction | LOW — COMPLIANCE_GATE overrides all fundamental analysis |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| Reward:risk | null (DATA_GAP, and moot given COMPLIANCE_GATE) |
| Catalyst | Next earnings 2026-09-09 (~70 days out — beyond the 60-day horizon; moot given the gate) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 ≥ pe_rich 50 — hold, do not add).
At the web-sourced price (~$105.47) vs $114.97 cost basis, return is approximately
**-8.3%** — well below the `drawdown_review_pct` (20%) threshold. Stock is up
~4% intraday on a cluster of analyst upgrades (see below); this is the second
consecutive report showing recovery off the early-June low.

| PM-grade record | |
|---|---|
| Conviction | LOW — DATA_GAP; no live reward:risk computable |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| Reward:risk | null (DATA_GAP) |
| Catalyst | Q2 2026 earnings **2026-07-22** (~21 days out — within the 60-day horizon) |
| Would buy today? | Mechanically yes per `recommend.py`, but DATA_GAP on reward:risk means the BUY-CANDIDATE gate isn't cleared |
| What changes verdict | SELL technical trigger, thesis_broken: true, or Shariah flip |

- Trailing stop / R-multiple / 6m momentum: unavailable (data gap as above).
- Portfolio note: only 2 holdings — concentration rules muted until ≥ 4 names.

## Snapshot

| Ticker | Stale `last_price` | Web price (approx.) | Shares | Cost basis | Approx. return |
|---|---|---|---|---|---|
| FIG | $19.26 | ~$18.09 | 35 | $21.43 | ~-15.6% |
| NOW | $106.40 | ~$105.47 | 7 | $114.97 | ~-8.3% |

Approx. portfolio value: (35 × $18.09) + (7 × $105.47) = $633.15 + $738.29 = **~$1,371.44**
Cost: (35 × $21.43) + (7 × $114.97) = $750.05 + $804.79 = **$1,554.84**
Approx. total return: **~-11.8%** ($-183.40 unrealised)
Weights (approx.): FIG ~46%, NOW ~54%

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate, independent
   of price. Fourth run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[Valuation / NOW] P/E ~119 (from last recorded fundamentals)** — rich;
   VALUATION_RICH holds. Do not add.
3. **[New / NOW] Analyst-upgrade cluster** — Guggenheim upgraded Neutral -> Buy
   ($125 target); Benchmark raised target to $130 (Buy); BTIG reiterated Buy
   ($150 target), citing a "substantial" shift in the market's AI narrative.
   Stock reacting +4% intraday. Positive for fundamentals; does not change the
   VALUATION_RICH rule.
4. **[New / NOW] Partnership news** — new AI-powered security/migration offering
   with Accenture, alongside the expanded IBM partnership (joint solutions due
   2H 2026). Adds near-term catalyst density ahead of July 22 earnings.
5. **[Relief / FIG] Modest bounce** — FIG up ~2.5% intraday to ~$18.09, but this
   does not touch the compliance decision.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):**
- Q1 2026 earnings: +46% revenue growth to $333M, accelerating from +40% the prior
  quarter; net dollar retention 139% (highest in >2 years); paid customers +54% YoY.
- Citi's Buy/$36 target and continued average analyst rating of "Buy" (12-mo target
  ~$36) imply large fundamentals-based upside from ~$18.
- Recent launches (Code Layers, Motion, AI agents) aim to defend against AI-native
  design competitors and support AI-credit monetization.

**Case to exit (compliance + technical):**
- NON-COMPLIANT per your mandate — this overrides the entire fundamental debate.
  Under your rules you do not average down, hold for recovery, or wait out an
  activist/analyst turn when the compliance gate is closed.
- RBC cut its target to $22 from $28, citing AI-monetization concerns — not every
  analyst view is bullish.
- Stock is at ~$18.09, ~87% below the 52-week high of ~$142.92; still down ~49%
  YTD despite Q1 beats.
- The compliance flag has been unresolved since 2026-06-09 — four assessment
  cycles. Cost of continued drift increases.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:**
- Stock up ~4% today on a cluster of analyst actions (Guggenheim upgrade to Buy
  $125, Benchmark $130, BTIG $150) — sell-side increasingly framing the pullback
  as a valuation opportunity rather than a thesis break.
- New Accenture AI-security/migration partnership plus the expanded IBM tie-up
  (joint solutions 2H 2026) add concrete near-term catalyst lanes beyond the
  July 22 print.
- Q2 earnings land 2026-07-22 (~21 days out) — squarely inside the 60-day
  catalyst horizon; thesis (durable subscription growth + AI-agent expansion)
  remains the frame going into that print.

**Case to trim / hold off adding:**
- Still down ~8.3% from your $114.97 cost basis; P/E remains rich (~119 on last
  recorded fundamentals) — VALUATION_RICH says hold, don't add, and growth must
  keep delivering to justify the multiple.
- 52-week range ~$81.24–$211.48; current price is only ~30% above the 52w low —
  a guidance miss on July 22 would have real room to re-test the lows.
- Today's rally is largely sentiment/analyst-driven (no new fundamental data
  point yet) — the actual test is the July 22 print, not today's move.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: "screened non-compliant -> SELL (exit;
  cure/purify per Zoya/Musaffa)." Unresolved for fourth consecutive run.
- **VALUATION_RICH fired -> NOW**: "P/E ≥ pe_rich (50) -> HOLD, do not add."
- **DRAWDOWN_REVIEW NOT firing -> NOW**: return is ~-8.3% today vs the 20%
  threshold — no thesis-review requirement triggered.
- No Stage 4 SELL triggers evaluable — technical data (chandelier, EMA, momentum)
  still unavailable from Yahoo.

*If you execute anything from this report, run `/apply-trade` so holdings files
and ledger stay in sync.*

## DCF
Unavailable — Yahoo feed blocked. Recorded assumptions for reference:
- **FIG**: growth_5y 30%, terminal growth 3%, discount rate 12%.
- **NOW**: growth_5y 18%, terminal growth 3%, discount rate 10%.

## New ideas (watchlist)

`discover.py` returned an empty pool again (Yahoo blocked). Watchlist unchanged
from the auto-discovered list. All six remain at **RESEARCH** per `recommend.py`
(DATA_GAP blocks reward:risk computation regardless of catalyst timing). All
Shariah statuses remain **UNVERIFIED**. Catalyst countdowns recomputed from today:

| Ticker | Candidate angle | Catalyst | Engine verdict | Days out |
|---|---|---|---|---|
| TSM | Sole leading-edge foundry; pricing power | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | 15 |
| ISRG | Da Vinci 5 placement ramp; ~zero debt | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | 15 |
| AMD | DC GPU share-gain vs Nvidia; MI400 ramp | Q2 earnings 2026-08-04 | RESEARCH (DATA_GAP) | 34 |
| QCOM | Auto/IoT diversification vs licensing fears | Q3 FY26 earnings 2026-08-05 | RESEARCH (DATA_GAP) | 35 |
| LLY | GLP-1 TAM + oral orforglipron | Q2 earnings 2026-08-05 | RESEARCH (DATA_GAP) | 35 |
| NVDA | AI datacenter super-cycle | Q2 FY27 earnings 2026-08-26 | RESEARCH (DATA_GAP) | 56 |

**TSM and ISRG have the nearest catalysts (July 16, 15 days out)** — if you have
access to a live data feed, these two are the priority to underwrite (define
target/stop → reward:risk → BUY-CANDIDATE gate check), then screen in Zoya/Musaffa.
NVDA's catalyst is now inside the 60-day horizon (56 days) — the CATALYST_GATE cap
noted in prior reports no longer applies, though DATA_GAP still caps it at RESEARCH.

Correlation note: TSM / AMD / QCOM / NVDA are a correlated semiconductor cluster —
size as ONE bet if adding any. LLY and ISRG are the genuine diversifiers.

## Follow-ups (priority order)

1. **[Urgent — 4th run unresolved] FIG compliance**: Re-screen in Zoya/Musaffa.
   If still non-compliant, execute exit and determine purification amount.
2. **[Monitor — 21 days] NOW Q2 earnings 2026-07-22**: Thesis validation event,
   now with an added tailwind of analyst upgrades — re-examine reward:risk before
   then using a live data source.
3. **[Opportunity] TSM / ISRG earnings 2026-07-16**: Soonest catalysts in the
   watchlist. Define target/stop and screen compliance before the earnings window.
4. **[Infrastructure] Run `dcf.py` / `verdict.py` / `discover.py` locally** (needs
   unrestricted Yahoo access) — this sandbox has blocked the feed across five
   consecutive runs.
5. NOW DRAWDOWN_REVIEW watch-level: alert if price falls below ~$92 (unchanged).

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag, not a fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Figma, Inc. (FIG) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/FIG/)
- [Figma (FIG) Stock Price & Overview — stockanalysis.com](https://stockanalysis.com/stocks/fig/)
- [Wall Street Just Cut Figma's Price Target — The Motley Fool](https://www.fool.com/investing/2026/05/31/wall-street-just-cut-figmas-price-target/)
- [Figma Stock Jumped 11% in a Day — TIKR](https://www.tikr.com/blog/figma-stock-jumped-11-in-a-day-but-its-still-down-87-heres-where-it-could-go-in-2026)
- [ServiceNow, Inc. (NOW) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/NOW/)
- [ServiceNow (NOW) Upgraded to Buy, Shares Rise 4.5% — GuruFocus](https://www.gurufocus.com/news/8940838/servicenow-now-upgraded-to-buy-shares-rise-45)
- [ServiceNow Stock Rides AI Partnerships And Price Target Hike — TimothySykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_07_01/)
- [Why is ServiceNow stock rallying today? — Investing.com](https://www.investing.com/news/stock-market-news/why-is-servicenow-stock-rallying-today-93CH-4769781)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — MarketScreener](https://www.marketscreener.com/news/servicenow-to-announce-second-quarter-2026-financial-results-on-july-22-ce7f5fd2db89f624)
