# Portfolio Assessment — 2026-07-08

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (7 new DRAFT setup cards auto-filled: CIEN, CLS,
DLO, ZS, TSLA, GWRE, NVDA; 13 of today's 20 leads already had cards from
prior runs — untouched) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` still reports 0 closed trades (no `transactions.csv` yet —
discipline guard stays dormant until you start logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a seventh consecutive run.** Live
price **$21.92**, **+2.3%** vs. the $21.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.5:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09); independent web check confirms interest income ~6.3% of gross revenue breaches the 5% AAOIFI ceiling |
| DCF intrinsic value | **$15.08** vs. $21.92 price -> **-31.2%** (price is rich to the model) |
| Trailing stop (chandelier) | $19.215 — price ~12.5% above it |
| 6m momentum (skip last month) | -41.3% |
| Portfolio note | ATR 6.4% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$106.69**, **-7.2%** vs. $114.97 cost basis — inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | HIGH — reward:risk 4.8:1 with a stated thesis |
| Shariah | PASS — recorded compliant (screened 2026-06-09); purification 3.35% |
| DCF intrinsic value | **$120.42** vs. $106.69 price -> **+12.9% upside** to the model |
| Trailing stop (chandelier) | $103.9803 — price is ~2.5% above it (no longer breached — see note below) |
| 6m momentum (skip last month) | -23.8% |
| Would buy today? | Yes per recommend.py's gates |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

**Update on last cycle's open question:** on 2026-07-07 price had slipped
*below* the chandelier trailing stop ($107.93 vs $109.98); today price
($106.69) is back *above* the (now slightly lower, $103.98) chandelier
level. Still moot either way for a `trade_type: core` holding — `verdict.py`'s
TRAIL_STOP rule only fires for `swing`/`momentum`/`catalyst` trade types, so
this never mechanically triggers on NOW regardless of which side of the
stop price sits. **Q2 FY2026 earnings land 2026-07-22 — 14 days out** —
ServiceNow raised full-year subscription revenue guidance to
$15.735–15.775B (20.5–21.0% cc growth); consensus models EPS $0.40 (down
y/y on comp, not a growth-story break). A joint AI-security offering with
Accenture continues to support the narrative; Evercore ISI ($150 PT),
Bernstein ($236 PT), and Benchmark (raised to $130) all reiterate/raise
Outperform-equivalent ratings ahead of the print.

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $21.92 | 35 | $21.43 | $767.03 | +2.3% | 50.7% |
| NOW | $106.69 | 7 | $114.97 | $746.83 | -7.2% | 49.3% |

**Total value: $1,513.86** | Cost: $1,554.84 | **Total return: ~-2.6%** (-$40.98 unrealised)

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Seventh run unresolved. COMPLIANCE_GATE fires -> SELL.
   Independent web check: interest income ~6.3% of gross revenue vs. the 5%
   AAOIFI ceiling is the specific breach — this isn't just a broker-app flag.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF / FIG] Price is ~44% above intrinsic value** ($21.92 vs. $15.08) on
   the recorded growth/discount assumptions — a second, compliance-independent
   argument against treating the recent bounce (+2.3% vs cost, up from -1.6%
   last cycle) as a reason to stay.
4. **[Catalyst / NOW] Q2 earnings in 14 days (2026-07-22)** — guidance already
   raised; the print could move price meaningfully either direction ahead of
   your next `last_review` (still dated 2026-06-15).
5. **[Shariah / repeat lead] PLTR** — surfaced again in today's discovery pool
   (LEAD, reward:risk 10.0:1, has a setup card from a prior run). Re-confirmed
   this cycle: Musaffa rates it DOUBTFUL, Zoya flags it questionable,
   HalalWallet rates it Not Halal — all citing government/defense/intelligence
   contract exposure the ratio pre-check here can't see. Treat as a likely
   fail pending your own Zoya/Musaffa screen.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** design-platform growth story
intact; stock is now slightly positive vs. cost basis (+2.3%) after Citigroup
initiated Buy coverage ($36 PT, published ~2026-07-01) and Bank of America
reinstated Buy coverage ($30 PT); Figma also joined the Russell 1000/2500/3000
indices at the June 26 reconstitution, adding index-flow demand.

**Case to exit (compliance + DCF, both independent of each other):**
NON-COMPLIANT per your mandate — this overrides any fundamental debate; seven
consecutive cycles unresolved now. Independent research this cycle confirms
the specific mechanism: Figma parked surplus IPO cash in interest-bearing
accounts, reporting ~$15.5M in interest income (~6.3% of gross revenue),
above the 5% AAOIFI ceiling — a screen issue, not a "maybe." The DCF model
(30% 5y growth, 12% discount rate) also puts intrinsic value at $15.08 vs. a
$21.92 price, a ~44% premium to the model even setting compliance aside.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (14 days out);
ServiceNow already raised 2026 subscription-revenue guidance to
$15.735–15.775B (20.5–21.0% cc growth); DCF shows +12.9% upside to intrinsic
value ($120.42) at recorded assumptions; sell-side remains broadly
Outperform/Buy (Evercore $150, Bernstein $236, Benchmark raised to $130) with
the AI-agent (Zurich platform) and Accenture AI-security tie-up cited as
forward drivers.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-23.8%; earnings in 14 days is a binary near-term risk (consensus EPS $0.40,
down y/y on comp) that could gap price either direction before your next
scheduled re-underwrite (`last_review: 2026-06-15`, next due per
`review_cadence_days: 90` around mid-September, but earnings prints trigger
re-underwriting regardless per rules.md).

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a seventh consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -7.2% vs. the 20% threshold.
- **TRAIL_STOP -> NOW**: does NOT fire (trade_type: core exempts it from the
  technical trailing-stop rule); moot this cycle since price is back above
  the chandelier level anyway ($106.69 vs. $103.98).
- **VOL_THROTTLE note -> FIG**: ATR 6.4% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.92 | -31.2% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $106.69 | +12.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — 7 fresh DRAFT cards; 13 unchanged from prior runs

Today's discovery pool has the same 20-slot structure as recent runs, ranked
by max-benefit. Compared with 2026-07-07: **AU, CDE, MT, SIMO** (unchanged
verdict-wise) and **KLIC** dropped out of the top 20; **CIEN, CLS, DLO, ZS,
TSLA, GWRE, NVDA** are new entrants. `scaffold.py --all-leads` auto-filled a
DRAFT card for each of the 7 newcomers; the other 13 already had cards from
prior cycles and were left untouched (`--force` was not used, so no existing
review work was overwritten). **Every row below is `status: draft`,
unreviewed, and Shariah UNVERIFIED — these are proposals to review and edit,
never buys.** None of these can reach BUY-CANDIDATE until you review the
card, edit anything you disagree with, set `status: planned`, and screen the
name compliant in Zoya/Musaffa.

Note on the two reward:risk columns: **leads R:R** is discover.py's
discovery-stage estimate (drives the LEAD vs. RESEARCH gate below).
**Card R:R (T1)** is the scaffolded setup card's engineered target, fixed by
construction at your `t1_r: 1.5` policy knob — a different number answering
a different question (screening estimate vs. locked-in trade plan).

| Ticker | Verdict (leads.md) | Setup type | Entry | Stop | T1 target | Card R:R (T1) | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|---|
| AR | LEAD | earnings_run | $34.68 | $34.12 | $35.52 | 1.5:1 | 10.0:1 | earnings 2026-07-29 | 21 |
| ALKT | LEAD | earnings_run | $18.95 | $16.99 | $21.89 | 1.5:1 | 15.8:1 | earnings 2026-07-29 | 21 |
| PLTR | LEAD | earnings_run | $132.54 | $131.84 | $133.59 | 1.5:1 | 10.0:1 | earnings 2026-08-03 | 26 |
| LIF | LEAD | earnings_run | $56.73 | $49.97 | $66.87 | 1.5:1 | 8.6:1 | earnings 2026-08-10 | 33 |
| CIEN *(new)* | RESEARCH | pullback | $463.43 | $426.06 | $519.49 | 1.5:1 | 12.3:1 | earnings 2026-09-09 | 63 (>60d horizon) |
| ULTA | LEAD | earnings_run | $452.49 | $447.62 | $459.79 | 1.5:1 | 20.0:1 | earnings 2026-08-27 | 50 |
| ALAB | LEAD | earnings_run | $432.74 | $371.67 | $524.34 | 1.5:1 | 5.1:1 | earnings 2026-08-04 | 27 |
| CLS *(new)* | LEAD | earnings_run | $355.67 | $337.26 | $383.28 | 1.5:1 | 7.2:1 | earnings 2026-07-27 | 19 |
| DLO *(new)* | LEAD | earnings_run | $13.92 | $13.61 | $14.38 | 1.5:1 | 7.0:1 | earnings 2026-08-13 | 36 |
| VRNS | LEAD | earnings_run | $45.67 | $39.71 | $54.61 | 1.5:1 | 5.2:1 | earnings 2026-07-28 | 20 |
| FICO | LEAD | earnings_run | $1286.51 | $1134.67 | $1514.28 | 1.5:1 | 5.3:1 | earnings 2026-07-29 | 21 |
| ZS *(new)* | LEAD | earnings_run | $143.05 | $134.50 | $155.88 | 1.5:1 | 8.3:1 | earnings 2026-09-02 | 56 |
| SIMO | RESEARCH | earnings_run | $318.86 | $273.25 | $387.27 | 1.5:1 | 2.0:1 | earnings 2026-07-29 | 21 |
| TSLA *(new)* | LEAD | earnings_run | $394.07 | $370.94 | $428.78 | 1.5:1 | 4.6:1 | earnings 2026-07-22 | 14 |
| DUOL | LEAD | earnings_run | $129.72 | $111.80 | $156.60 | 1.5:1 | 5.2:1 | earnings 2026-08-05 | 28 |
| PAY | LEAD | earnings_run | $28.15 | $25.00 | $32.87 | 1.5:1 | 4.8:1 | earnings 2026-08-03 | 26 |
| GWRE *(new)* | LEAD | earnings_run | $135.44 | $123.81 | $152.89 | 1.5:1 | 6.6:1 | earnings 2026-09-03 | 57 |
| ADI | LEAD | earnings_run | $388.83 | $386.48 | $392.35 | 1.5:1 | 5.9:1 | earnings 2026-08-19 | 42 |
| NVDA *(new)* | LEAD | earnings_run | $200.79 | $194.16 | $210.73 | 1.5:1 | 5.4:1 | earnings 2026-08-26 | 49 |
| AMD | RESEARCH | earnings_run | $552.05 | $467.12 | $679.45 | 1.5:1 | 1.6:1 | earnings 2026-08-04 | 28 |

All 20 cards passed the liquidity floor (`avg $vol` >= $5M, market cap >=
$500M) and cleared a clean ratio pre-check — but the ratio pre-check is
*not* a business-activity screen. Shariah status on every card is
`unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR (Palantir)** — see Action flag #5 above; re-confirmed this cycle
  across three independent screeners (Musaffa DOUBTFUL, Zoya questionable,
  HalalWallet Not Halal). Treat as a likely fail, not a rubber stamp.
- **CIEN** dropped to RESEARCH (not LEAD) purely on the 60-day catalyst
  horizon gate — its earnings print (2026-09-09) is 63 days out vs. the
  `catalyst_horizon_days: 60` cutoff. Nothing wrong with the name; it's just
  not inside the window today.
- **TSLA (new entrant)** — earnings are just 14 days out (2026-07-22, same
  week as NOW's print). Standard EV/tech manufacturer profile; still needs
  its own business-activity and interest-income screen like every name here.
- **NVDA / AMD** are SPUS (halal-ETF) holdings surfacing as leads via that
  channel — a clean ratio pre-check is not the same as a completed
  business-activity screen; confirm in Zoya/Musaffa regardless of the ETF
  membership.
- **SIMO / AMD (RESEARCH, not LEAD)** — capped by the mechanical asymmetry
  gate (reward:risk 2.0:1 and 1.6:1, both under the 3.0 floor), not by a
  business problem.

## Follow-ups (priority order)

1. **[Urgent — 7th run unresolved] FIG compliance**: re-screen in
   Zoya/Musaffa; independent web research this cycle corroborates the
   broker-app flag with a specific mechanism (interest income over the 5%
   AAOIFI ceiling).
2. **[Time-sensitive] NOW earnings 2026-07-22 (14 days)**: re-underwrite the
   thesis around the print regardless of the SELL/HOLD verdict staying
   unchanged mechanically.
3. **[Repeat — Shariah] PLTR**: consistent DOUBTFUL/questionable/Not-Halal
   reads across three screeners now; screen carefully before writing it up
   as anything beyond RESEARCH.
4. **[Housekeeping] 7 new DRAFT setup cards** (CIEN, CLS, DLO, ZS, TSLA,
   GWRE, NVDA) added to `setups/` this run — 23 total draft/planned cards
   now exist; none are `planned` yet.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenows-q2-2026-earnings-expect-121215371.html)
- [+6.31% for ServiceNow stock as Q2 2026 earnings date approaches — TradersUnion](https://tradersunion.com/news/financial-news/show/2549550-servicenow-gains-6-31percent-to-usd105-54/)
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [Figma Stock Rose 9% This Week: Where FIG Could Go in 2026 — TIKR](https://www.tikr.com/blog/figma-stock-rose-9-this-week-where-fig-could-go-in-2026)
- [Is Figma (FIG) IPO stock Halal and Shariah Compliant? — Muslim Xchange](https://muslimxchange.com/news/is-figma-fig-ipo-stock-halal-and-shariah-compliant/)
- [Is Palantir Technologies (PLTR) Stock Halal or Haram? — Zoya](https://zoya.finance/stocks/pltr)
- [Is Palantir Technologies Inc - PLTR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/PLTR/)
- [Best Halal Investments — Ranked (2026) — HalalWallet](https://www.halalwallet.us/best-halal-investments)
