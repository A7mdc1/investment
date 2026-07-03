# Portfolio Assessment — 2026-07-03

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps
- Yahoo egress is still blocked in this sandbox (curl 403 via the proxy tunnel);
  `discover.py`, `dcf.py`, and the technical block of `verdict.py`/`recommend.py`
  (chandelier trailing stop, EMA, 6m momentum, R-multiple, reward:risk) did not run.
  This is the fourth consecutive run with this gap — see follow-up #4.
- `prices.py` returned `null` for both tickers; this report uses secondary-source
  web prices (sourced below) — directional, not exact. Confirm in your brokerage.
  - **FIG**: ~$21.34 (day range $19.29–$21.88)
  - **NOW**: ~$106.32 (day range $103.84–$107.68)
- `signals.py` and `verdict.py` fell back to the stale `last_price` values in
  the holding files (FIG $19.26, NOW $106.40) — all figures below use the
  web-sourced prices instead for accuracy.

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). Verdict unchanged for the fourth consecutive run. At the
web-sourced price (~$21.34), return vs $21.43 cost basis is approximately **-0.4%**
— FIG has rallied ~12% since the June 30 report (~$19.08 -> ~$21.34) but the
compliance flag, not the price, drives this verdict.

| PM-grade record | |
|---|---|
| Conviction | LOW — COMPLIANCE_GATE overrides all fundamental analysis |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09, now 24 days stale) |
| Reward:risk | null (DATA_GAP, and moot given COMPLIANCE_GATE) |
| Catalyst | No new hard catalyst; next scheduled event is Q2 earnings (date TBA) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 (stale) ≥ pe_rich 50 — hold, do
not add). At the web-sourced price (~$106.32) vs $114.97 cost basis, return is
approximately **-7.5%** — well below the `drawdown_review_pct` (20%) threshold;
DRAWDOWN_REVIEW is not firing.

| PM-grade record | |
|---|---|
| Conviction | LOW — DATA_GAP; no live reward:risk computable |
| Shariah | PASS — recorded compliant (screened 2026-06-09, now 24 days stale) |
| Reward:risk | null (DATA_GAP) |
| Catalyst | Q2 FY26 earnings confirmed **2026-07-22** (~19 days out) |
| Would buy today? | Mechanically yes per `recommend.py`, but DATA_GAP on reward:risk means BUY-CANDIDATE gate not cleared |
| What changes verdict | SELL technical trigger, thesis_broken: true, or Shariah flip |

- Trailing stop / R-multiple / 6m momentum: unavailable (data gap as above).
- Portfolio note: only 2 holdings — concentration rules muted until ≥ 4 names.
- Shariah screens for both holdings are now 24 days old (screened 2026-06-09) —
  still under the quarterly staleness threshold, but worth a refresh soon.

## Snapshot

| Ticker | Stale `last_price` | Web price (approx.) | Shares | Cost basis | Approx. return |
|---|---|---|---|---|---|
| FIG | $19.26 | ~$21.34 | 35 | $21.43 | ~-0.4% |
| NOW | $106.40 | ~$106.32 | 7 | $114.97 | ~-7.5% |

Approx. portfolio value: (35 × $21.34) + (7 × $106.32) = $746.90 + $744.24 = **~$1,491.14**
Cost: (35 × $21.43) + (7 × $114.97) = $750.05 + $804.79 = **$1,554.84**
Approx. total return: **~-4.1%** ($-63.70 unrealised) — an improvement from
~-12% on June 30, driven mostly by FIG's rally.
Weights (approx.): FIG ~50.1%, NOW ~49.9% (roughly balanced again, vs.
FIG 49% / NOW 51% on June 30).

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate, independent
   of price. Fourth run unresolved. COMPLIANCE_GATE fires -> SELL.
2. **[New / FIG] Continued rally on Findell Capital activism** — the activist is
   now specifically pushing Figma to cut its product lineup from 8 to 4 apps
   (keep Design, Dev Mode, FigJam, Make; sunset the rest), citing stock-based
   comp at 27% of revenue vs. 8% at Adobe. Findell's standalone 12-month target
   is $40/share, with a stated buyout floor of ~$50/share (Microsoft/Alphabet
   named as logical acquirers) if the board doesn't act. Positive for the
   fundamental case; does not change the compliance gate.
3. **[Watch / FIG] August 31, 2026 lock-up expiration** — an Extended Lock-Up
   Agreement covering ~54.1% of Class A shares (over $6B in low-cost-basis stock)
   expires then; commonly cited as a supply-overhang risk for the price, separate
   from the compliance issue.
4. **[Valuation / NOW] P/E ~119 (stale)** — rich; VALUATION_RICH holds. Do not add.
5. **[Catalyst / NOW] Q2 earnings confirmed for July 22, 2026** — market is
   pricing a ±13.3% (~$12.22) move on the print; consensus EPS $0.86, revenue
   ~$3.97B. Thesis-validation event in ~19 days.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):**
- Findell Capital's campaign has intensified: it's now asking the board to trim
  the product portfolio to 4 apps and cut R&D/SBC overhead, with a $40 standalone
  target and a ~$50 buyout floor if the board doesn't act.
- Q1 2026 results remain the fundamental anchor: +46% revenue growth to $333M,
  139% net dollar retention, +54% YoY paid customers, $89M free cash flow (27%
  margin) — though GAAP operating loss (~-$137M) and net loss (~-$142M) persist.
- Citigroup's Buy/$36 target (initiated late June) still stands.
- Stock is up ~12% since the June 30 report (~$19.08 -> ~$21.34).

**Case to exit (compliance + structural):**
- NON-COMPLIANT per your mandate — this overrides the entire fundamental debate.
  Under your rules, you do not average up/down, hold for activist catalysts, or
  wait for a buyout when the compliance gate is closed. Fourth consecutive
  unresolved run (screened 2026-06-09).
- The August 31, 2026 lock-up expiration (~54% of Class A shares, $6B+ low-cost
  basis stock) is a known supply overhang still ahead — a headwind independent of
  the compliance question.
- Governance overhang: the activist is also demanding an independent board probe
  into whether Anthropic (whose board seat was vacated just before Claude Design
  launched) misused confidential Figma information — an unresolved governance risk.
- AI-native competition (Adobe, Canva, Anthropic's Claude Design) is unchanged.

### NOW — ServiceNow, Inc.
**Case to keep:**
- Durable subscription growth thesis intact (~21% rev / ~23% earnings growth in
  2025); AI-agent platform (Zurich) remains the forward driver.
- New joint AI-powered cybersecurity offering with Accenture, announced this
  period, broadens the enterprise portfolio and supports bullish sentiment.
- Analyst consensus remains Strong Buy (44 buy / 1 sell), average 12-month target
  ~$141, well above the current ~$106 price.
- Q2 earnings confirmed for July 22 — a clear, near-dated catalyst to test the
  thesis (consensus EPS $0.86, revenue ~$3.97B).

**Case to trim/watch:**
- P/E still rich (~119 on stale data) — VALUATION_RICH holds; any growth
  deceleration would hit the multiple hard, and the market is already pricing a
  ±13% earnings-day swing.
- Position remains ~7.5% underwater vs. cost basis; no new information changes
  the thesis, but the July 22 print is the next real test.

## Suggested actions (from YOUR rules)

Per `rules.md` (Stage 1/Stage 3), applied to today's data:
- **COMPLIANCE_GATE fired -> FIG SELL** (exit; determine purification per
  Zoya/Musaffa). Supporting fact: recorded non-compliant since 2026-06-09,
  unresolved four runs running.
- **VALUATION_RICH fired -> NOW HOLD, do not add.** Supporting fact: P/E ~119
  (stale) ≥ `pe_rich` (50).
- No SELL trigger fired for NOW (no HARD_STOP/TRAIL_STOP/EMA_BREAK data available
  — data gap — and no `thesis_broken` flag set in the holding file).
- DRAWDOWN_REVIEW did not fire for either holding (FIG -0.4%, NOW -7.5%, both
  under the 20% threshold).
- Concentration/rebalance rules are muted (`min_names_for_concentration: 4`,
  only 2 holdings).

If you execute anything from these, run `/apply-trade` so holdings + ledger update.

## DCF

Not available — `dcf.py` failed on both tickers (Yahoo blocked in this sandbox,
curl 403). Front-matter assumptions on file for reference only (not recomputed
this run):
- **FIG**: growth_5y 30%, terminal growth 3%, discount rate 12%.
- **NOW**: growth_5y 18%, terminal growth 3%, discount rate 10%.

## New ideas (from watchlist.md; unchanged list — `discover.py` could not refresh it)

`recommend.py`'s mechanical pass caps every idea at **RESEARCH** — all lack a
live price feed (DATA_GAP), so reward:risk cannot be computed and the
ASYMMETRY_GATE cannot pass regardless of catalyst timing. None are BUY-CANDIDATE
or AVOID; all are UNVERIFIED for Shariah (pre-check only, not a Zoya/Musaffa
screen).

| Ticker | Candidate angle (unverified) | Catalyst | Verdict | Days out |
|---|---|---|---|---|
| TSM | Sole leading-edge foundry; advanced-node pricing power | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | 13 |
| ISRG | Da Vinci 5 placement ramp; ~zero debt | Q2 earnings 2026-07-16 | RESEARCH (DATA_GAP) | 13 |
| AMD | DC GPU share-gain vs Nvidia; MI400 ramp | Q2 earnings 2026-08-04 | RESEARCH (DATA_GAP) | 32 |
| QCOM | Auto/IoT diversification vs licensing fears | Q3 FY26 earnings 2026-08-05 | RESEARCH (DATA_GAP) | 33 |
| LLY | GLP-1 TAM + oral orforglipron | Q2 earnings 2026-08-05 | RESEARCH (DATA_GAP) | 33 |
| NVDA | AI datacenter super-cycle | Q2 FY27 earnings 2026-08-26 | RESEARCH (DATA_GAP) | 54 |

**TSM and ISRG remain the nearest catalysts (July 16, 13 days out)** — priority
to underwrite (target/stop -> reward:risk) if a live data feed becomes available,
then screen in Zoya/Musaffa. Note NVDA's catalyst window has now moved to 54
days — inside the 60-day horizon — but the DATA_GAP still caps it at RESEARCH.

Correlation note: TSM / AMD / QCOM / NVDA are a correlated semiconductor
cluster — size as ONE bet if adding any. LLY and ISRG are the genuine
diversifiers, and none of these overlap sector-wise with the existing NOW
(enterprise software) holding.

## Discipline guard

No `transactions.csv`/ledger file exists yet in this repo, so there is no
closed-trade sample to compare net-of-cost performance against a Shariah
benchmark. Nothing to flag here until trades are logged via `/apply-trade`.

## Follow-ups (priority order)

1. **[Urgent — 4th run unresolved] FIG compliance**: Re-screen in Zoya/Musaffa.
   If still non-compliant, execute exit and determine purification amount. The
   activist campaign and lock-up overhang are fundamental noise relative to this.
2. **[Monitor — 19 days] NOW Q2 earnings confirmed for 2026-07-22**: Market is
   pricing a ±13.3% move. Re-examine reward:risk before then using a live data
   source.
3. **[Opportunity — 13 days] TSM / ISRG earnings 2026-07-16**: Soonest watchlist
   catalysts. Define target/stop and screen compliance before the earnings window.
4. **[Infrastructure] Run `dcf.py` / `verdict.py` / `discover.py` locally** (needs
   unrestricted Yahoo access) — this sandbox has now blocked the feed across
   four consecutive runs.
5. **[Refresh]** Both holdings' Shariah screens are 24 days old (screened
   2026-06-09) — consider a re-screen given the accumulating FIG governance
   news (Anthropic conflict-of-interest probe demand).
6. NOW DRAWDOWN_REVIEW watch-level unchanged: alert if price falls below ~$92.

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag, not a fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Figma, Inc. (FIG) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/FIG/)
- [ServiceNow, Inc. (NOW) Stock Price — Yahoo Finance](https://finance.yahoo.com/quote/NOW/)
- [Figma Stock 2026: Why $89M in Cash Flow Can't Stop the Slide — Memeburn](https://memeburn.com/figma-stock-2026-cash-flow/)
- [Activist Findell seeks changes at 'Adobe slayer' Figma — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/activist-findell-seeks-changes-adobe-133153489.html)
- [Dealroom.co: Findell pushes Figma to cut products from 8 to 4](https://app.dealroom.co/news/feed/activist-findell-pushes-figma-to-cut-products-from-8-to-4-probe-anthropic-ai-conflict)
- [Figma (FIG) Extends Lock-Up Covering 54.1% of Class A Shares — StockTitan](https://www.stocktitan.net/sec-filings/FIG/8-k-figma-inc-reports-material-event-8e2472f3bc44.html)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — BusinessWire](https://www.businesswire.com/news/home/20260701382890/en/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22)
- [+6.31% for ServiceNow stock as Q2 2026 earnings date approaches — TradersUnion](https://tradersunion.com/news/financial-news/show/2549550-servicenow-gains-6-31percent-to-usd105-54/)
