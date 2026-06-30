# Portfolio Assessment — 2026-06-30

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps
- Yahoo egress still blocked in this sandbox (curl 403); `discover.py`, `dcf.py`,
  and the technical block of `verdict.py` (chandelier trailing stop, EMA, 6m
  momentum, R-multiple) did not run.
- `prices.py` returned `null` for both tickers; this report uses secondary-source
  web prices (sourced below) — directional, not exact. Confirm in your brokerage.
  - **FIG**: ~$19.08 (day range $18.52–$19.30)
  - **NOW**: ~$99.97 (day range $99.47–$103.21)
- `signals.py` and `verdict.py` fell back to the stale `last_price` values in
  the holding files (FIG $19.26, NOW $106.40) — all rule verdicts below use the
  web-sourced prices instead for accuracy.

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). Verdict unchanged for the third consecutive run. At the
web-sourced price (~$19.08), return vs $21.43 cost basis is approximately **-11%**.

| PM-grade record | |
|---|---|
| Conviction | LOW — COMPLIANCE_GATE overrides all fundamental analysis |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09) |
| Reward:risk | null (DATA_GAP, and moot given COMPLIANCE_GATE) |
| Catalyst | Config 2026 ~2026-06-24 (elapsed); no new hard catalyst |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 ≥ pe_rich 50 — hold, do not add).
At the web-sourced price (~$99.97) vs $114.97 cost basis, return is approximately
**-13%** — BELOW the `drawdown_review_pct` (20%) threshold. This is an improvement
vs. the June 26 report, which had NOW approaching/breaching that line at ~$89-94.
The DRAWDOWN_REVIEW flag is not confirmed firing today.

| PM-grade record | |
|---|---|
| Conviction | LOW — DATA_GAP; no live reward:risk computable |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| Reward:risk | null (DATA_GAP) |
| Catalyst | Q2 earnings ~2026-07-22 (~22 days out) |
| Would buy today? | Mechanically yes per `recommend.py` output, but DATA_GAP on reward:risk means BUY-CANDIDATE gate not cleared |
| What changes verdict | SELL technical trigger, thesis_broken: true, or Shariah flip |

- Trailing stop / R-multiple / 6m momentum: unavailable (data gap as above).
- Portfolio note: only 2 holdings — concentration rules muted until ≥ 4 names.

## Snapshot

| Ticker | Stale `last_price` | Web price (approx.) | Shares | Cost basis | Approx. return |
|---|---|---|---|---|---|
| FIG | $19.26 | ~$19.08 | 35 | $21.43 | ~-11% |
| NOW | $106.40 | ~$99.97 | 7 | $114.97 | ~-13% |

Approx. portfolio value: (35 × $19.08) + (7 × $99.97) = $667.80 + $699.79 = **~$1,367.59**
Cost: (35 × $21.43) + (7 × $114.97) = $750.05 + $804.79 = **$1,554.84**
Approx. total return: **~-12%** ($-187.25 unrealised)
Weights (approx.): FIG ~49%, NOW ~51%

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate, independent
   of price. Third run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[New / FIG] Activist campaign (Findell Capital)** — pressing Figma's board to
   rework governance and its Anthropic ties. Stock reacted positively (+6–11% at
   peak on June 26), but compliance status is unchanged. Activist pressure does
   not affect the Shariah gate.
3. **[New / FIG] Citigroup Buy coverage** — $36 price target. Positive for
   fundamentals, neutral for the mandate decision.
4. **[Valuation / NOW] P/E ~119** — rich; VALUATION_RICH holds. Do not add.
5. **[Relief / NOW] Drawdown no longer at threshold** — NOW has recovered from
   ~$89-94 (June 26) to ~$100 today; the DRAWDOWN_REVIEW trigger (−20% vs cost)
   is NOT confirmed firing. Continue to monitor.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):**
- Q1 2026 earnings: +46% revenue growth to $333M, accelerating from +40% the prior
  quarter. Net dollar retention reached 139% (highest in >2 years); paid customers
  +54% YoY to ~690,000.
- Citigroup initiated coverage with Buy/$36 target, citing AI product roadmap, MCP
  server, and growing AI-credit usage among enterprise customers.
- Findell Capital activist campaign is pressuring the board to rework Anthropic
  investment ties and improve governance — market read this as potentially unlocking
  value; stock jumped 6–11% on the news around June 26.
- Analyst sentiment is turning: average target ~$36.78 vs ~$19 spot implies
  significant upside on the fundamentals view.

**Case to exit (compliance + technical):**
- NON-COMPLIANT per your mandate — this overrides the entire fundamental debate.
  Under your rules, you do not average down, hold for a recovery, or wait for an
  activist to turn things around when the compliance gate is closed.
- Stock is at ~$19.08, ~87% below the 52-week high of ~$142.92 — sustained
  selling pressure is ongoing despite Q1 beats and activist news.
- The compliance flag has been unresolved since 2026-06-09 — three assessment
  cycles. Cost of continued drift increases.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:**
- Stock has recovered from ~$89-94 (June 26) back to ~$100 — the sharp
  early-June drawdown (from ~$136 on June 1 to a low near $81) is showing some
  stabilisation.
- IBM partnership announced: watsonx, Red Hat, Instana, Ansible integrated into
  the ServiceNow AI Platform; first joint solutions due H2 2026 — a concrete
  near-term catalyst lane.
- Benchmark raised target $125 → $130 (Buy); consensus avg ~$140.63, Strong Buy
  — significant analyst-implied upside from current ~$100.
- Q2 earnings ~2026-07-22 (~22 days out): no TIME_STOP issue; catalyst is well
  within the 60-day horizon.
- Thesis intact: enterprise workflow + AI-agent expansion continues to attract
  institutional coverage and partnership momentum.

**Case to trim / hold off adding:**
- Still down ~13% from your $114.97 cost basis. While not at the DRAWDOWN_REVIEW
  threshold, the pullback from the $136 June high to $100 today is ~26% — a
  significant drawdown from the recent trading range, not just from cost.
- P/E ~119 (VALUATION_RICH) — growth must keep accelerating to sustain the
  multiple. Any Q2 guidance miss would likely accelerate selling.
- 52-week range now ~$81.24–$211.48; current price is only ~12% above the 52w low —
  limited downside buffer if thesis cracks.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: "screened non-compliant -> SELL (exit;
  cure/purify per Zoya/Musaffa)." Unresolved for third consecutive run.
- **VALUATION_RICH fired -> NOW**: "P/E ≥ pe_rich (50) -> HOLD, do not add."
- **DRAWDOWN_REVIEW NOT confirmed firing -> NOW**: return is ~-13% today vs the
  20% threshold — no thesis-review requirement triggered. Continue monitoring;
  if NOW retraces below ~$92 (~-20% from $114.97), the rule fires.
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
from the auto-discovered June 25 list. All six remain at **RESEARCH** per
`recommend.py` (DATA_GAP blocks reward:risk computation). All Shariah statuses
remain **UNVERIFIED**.

| Ticker | Candidate angle | Catalyst | Engine verdict | Catalyst in horizon? |
|---|---|---|---|---|
| TSM | Sole leading-edge foundry; pricing power | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | Yes — 16 days |
| ISRG | Da Vinci 5 placement ramp; ~zero debt | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | Yes — 16 days |
| AMD | DC GPU share-gain vs Nvidia; MI400 ramp | Q2 earnings 2026-08-04 | RESEARCH (DATA_GAP) | Yes — 35 days |
| QCOM | Auto/IoT diversification vs licensing fears | Q3 FY26 earnings 2026-08-05 | RESEARCH (DATA_GAP) | Yes — 36 days |
| LLY | GLP-1 TAM + oral orforglipron | Q2 earnings 2026-08-05 | RESEARCH (DATA_GAP) | Yes — 36 days |
| NVDA | AI datacenter super-cycle | Q2 FY27 earnings 2026-08-26 | RESEARCH (CATALYST_GATE) | No — 57 days |

**TSM and ISRG have the nearest catalysts (July 16, 16 days out)** — if you have
access to a live data feed, these two are the priority to underwrite (define
target/stop → reward:risk → BUY-CANDIDATE gate check), then screen in Zoya/Musaffa.

Correlation note: TSM / AMD / QCOM / NVDA are a correlated semiconductor cluster —
size as ONE bet if adding any. LLY and ISRG are the genuine diversifiers.

## Follow-ups (priority order)

1. **[Urgent — 3rd run unresolved] FIG compliance**: Re-screen in Zoya/Musaffa.
   If still non-compliant, execute exit and determine purification amount.
2. **[Monitor — 22 days] NOW Q2 earnings ~2026-07-22**: Thesis validation event.
   Re-examine the reward:risk before then using a live data source.
3. **[Opportunity] TSM / ISRG earnings 2026-07-16**: Soonest catalysts in the
   watchlist. Define target/stop and screen compliance before the earnings window.
4. **[Infrastructure] Run `dcf.py` / `verdict.py` / `discover.py` locally** (needs
   unrestricted Yahoo access) — this sandbox has blocked the feed across four
   consecutive runs.
5. NOW DRAWDOWN_REVIEW watch-level: alert if price falls below ~$92.

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag, not a fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Figma, Inc. (FIG) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/FIG/)
- [ServiceNow, Inc. (NOW) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/NOW/)
- [FIG Stock Jumps As Wall Street And Activists Pile In — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_06_26/)
- [FIG Stock Jumps As Activist Targets Figma–Anthropic Ties — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_06_17/)
- [Figma Stock jumped 11% in a Day — TIKR](https://www.tikr.com/blog/figma-stock-jumped-11-in-a-day-but-its-still-down-87-heres-where-it-could-go-in-2026)
- [ServiceNow Stock Builds AI Momentum As Analysts Boost Targets — StocksToTrade](https://stockstotrade.com/news/servicenow-inc-now-news-2026_06_26-2/)
- [ServiceNow (NOW) Extends AI Lead As Analysts Boost Targets — TimothySykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_06_26/)
- [ServiceNow Stock Draws Bullish Targets As AI Deals Pile Up — StocksToTrade](https://stockstotrade.com/news/servicenow-inc-now-news-2026_06_26/)
