# Portfolio Assessment — 2026-07-12

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (8 fresh DRAFT setup cards auto-filled for names
without one; 12 existing cards left untouched) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` still reports 0 closed trades (no
`transactions.csv` yet — discipline guard stays dormant until you start
logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a seventh consecutive report**
(first flagged 2026-06-25). Live price **$21.11**, essentially flat vs. the
$21.43 cost basis (**-1.5%**).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.8:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09, still not re-screened) |
| DCF intrinsic value | **$15.08** vs. $21.11 price -> **-28.6%** (price is rich to the model) |
| Trailing stop (chandelier) | $18.9688 — price ~11.3% above it |
| 6m momentum (skip last month) | -45.0% |
| Portfolio note | ATR 7.03% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$107.71**, **-6.3%** vs. $114.97 cost basis — inside the 20%
`drawdown_review_pct` threshold.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — recommend.py can't self-assess without a stated thesis-vs-price edge |
| Shariah | PASS — recorded compliant (screened 2026-06-09) |
| DCF intrinsic value | **$120.42** vs. $107.71 price -> **+11.8% upside** to the model |
| Trailing stop (chandelier) | $96.6068 — price is now **11.4% above it** (back above the stop; last run it had slipped ~1.9% below) |
| 6m momentum (skip last month) | -29.1% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own thesis input |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $21.11 | 35 | $21.43 | $738.85 | -1.5% | 49.5% |
| NOW | $107.71 | 7 | $114.97 | $753.97 | -6.3% | 50.5% |

**Total value: $1,492.82** | Cost: $1,554.84 | **Total return: ~-4.0%** (-$62.02 unrealised)

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. Seventh consecutive report unresolved. COMPLIANCE_GATE
   fires -> SELL. The recorded screen is now over a month old (2026-06-09).
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF / FIG] Price is ~40% above intrinsic value** ($21.11 vs. $15.08) on
   the recorded growth/discount assumptions — independent of the compliance
   gate, another data point against treating any near-term bounce as a reason
   to stay.
4. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22** (10 days out) —
   guided subscription revenue $3.815–3.820B (~21–21.5% cc growth), EPS
   consensus $0.40 (down y/y on comp). A binary event inside the next
   two weeks for over half the book's value.
5. **[Shariah / new lead] ESE (ESCO Technologies)** — today's discovery pool
   surfaced ESE as a LEAD. Its Aerospace & Defense segment manufactures
   miniature electro-explosive devices for military ejection seats and
   missile arming devices, plus landing-gear components — a materially
   different profile from the "engineered products" framing in the
   mechanical note. This looks like a probable business-activity fail
   (defense/weapons-adjacent manufacturing) independent of the clean ratio
   pre-check here; screen skeptically, don't treat UNVERIFIED as "probably fine."

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** Citigroup initiated coverage
July 1 with a Buy rating and $36 target; Bank of America reinstated Buy at
$30, both citing AI-driven monetization (hybrid seat + usage-based AI
credits). Shares closed +2.7% on July 9. Revenue grew 41% in 2025, though the
company is still burning cash (operating income ~-$137M last quarter).

**Case to exit (compliance + DCF, both independent of each other):**
NON-COMPLIANT per your mandate — this overrides any fundamental debate; seven
consecutive cycles unresolved now, with the underlying screen itself now over
a month stale. The DCF model (30% 5y growth, 12% discount rate) puts
intrinsic value at $15.08 vs. a $21.11 price, a ~40% premium to the model
even setting compliance aside. Insider selling this week (CRO sold 8,629
shares July 6) doesn't help the fundamental case either.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (10 days out) — the
company guided subscription revenue of $3.815–3.820B (~21–21.5% cc growth)
and an operating margin of ~26.5%; analysts model EPS of $0.40. Q1 (reported
Apr 22) beat across subscription revenue, RPO, operating margin, and free
cash flow with robust large-deal activity and AI-product adoption. DCF shows
+11.8% upside to intrinsic value ($120.42) at recorded assumptions, and price
has moved back above the chandelier trailing stop this run.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-29.1%; earnings in 10 days is a binary event for the larger half of a
two-name book — a miss or guide-down could gap the position through both the
DCF cushion and the trailing stop in one session.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a seventh consecutive run.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -6.3% vs. the 20% threshold.
- **TRAIL_STOP -> NOW**: does not fire; price is back above the computed
  chandelier level this run (no longer the open question flagged last time).
- **VOL_THROTTLE note -> FIG**: ATR 7.03% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $21.11 | -28.6% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $107.71 | +11.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is currently **empty** — nothing
for step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead.

## Draft & planned setups — 8 fresh DRAFT cards, 12 unchanged

`discover.py` built a fresh candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens), applied the
liquidity floor + Shariah-ratio/asymmetry/catalyst gates, and rewrote
**`leads.md`** (top 20 by max-benefit rank; overwrites the 2026-07-07 list).
`scaffold.py --all-leads` auto-filled a **DRAFT** `setups/<ticker>.md` card
for the 8 names that didn't already have one (MSFT, ZS, STX, CLS, APH, GDDY,
JNJ, ESE); the 12 names still present from prior runs (ALKT, FICO, PLTR, LIF,
DUOL, VRNS, ULTA, MT, PAY, MU, ALAB, ADI) kept their existing unreviewed
cards untouched. **Every row below is `status: draft`, unreviewed, and
Shariah UNVERIFIED** — proposals to review and edit, never buys. None can
reach BUY-CANDIDATE until you review the card, edit anything you disagree
with, set `status: planned`, and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Setup card | Leads R:R | Score | Catalyst | Days out |
|---|---|---|---|---|---|---|
| MSFT | LEAD | new | 12.8:1 | 34.7 | earnings 2026-07-29 | 17 |
| ALKT | LEAD | existing | 20.0:1 | 33.3 | earnings 2026-07-29 | 17 |
| FICO | LEAD | existing | 8.0:1 | 36.7 | earnings 2026-07-29 | 17 |
| ZS | LEAD | new | 12.8:1 | 38.6 | earnings 2026-09-02 | 52 |
| PLTR | LEAD | existing | 8.4:1 | 28.6 | earnings 2026-08-03 | 22 |
| STX | LEAD | new | 5.5:1 | 56.0 | earnings 2026-07-28 | 16 |
| LIF | LEAD | existing | 6.8:1 | 45.7 | earnings 2026-08-10 | 29 |
| DUOL | LEAD | existing | 6.9:1 | 33.1 | earnings 2026-08-05 | 24 |
| CLS | LEAD | new | 6.2:1 | 33.1 | earnings 2026-07-27 | 15 |
| VRNS | LEAD | existing | 4.8:1 | 47.8 | earnings 2026-07-28 | 16 |
| ULTA | LEAD | existing | 8.0:1 | 33.5 | earnings 2026-08-27 | 46 |
| APH | LEAD | new | 5.4:1 | 37.1 | earnings 2026-07-29 | 17 |
| MT | LEAD | existing | 3.6:1 | 51.5 | earnings 2026-07-30 | 18 |
| PAY | LEAD | existing | 5.0:1 | 37.2 | earnings 2026-08-03 | 22 |
| MU | RESEARCH | existing | 5.7:1 | 57.0 | earnings 2026-09-23 | 73 (>60d horizon) |
| ALAB | RESEARCH | existing | 2.0:1 | 65.2 | earnings 2026-08-04 | 23 |
| GDDY | LEAD | new | 4.1:1 | 36.2 | earnings 2026-07-30 | 18 |
| ADI | LEAD | existing | 5.3:1 | 34.3 | earnings 2026-08-19 | 38 |
| JNJ | RESEARCH | new | 2.0:1 | 43.9 | earnings 2026-07-15 | 3 |
| ESE | LEAD | new | 4.3:1 | 36.1 | earnings 2026-08-10 | 29 |

All 20 cards passed the liquidity floor (`avg $vol` >= $5M, market cap >=
$500M) and cleared a clean ratio pre-check (business_ok, debt/liquid ratios
within bounds) — but the ratio pre-check is *not* a business-activity
screen. Shariah status on every card is `unverified` by construction (only a
human Zoya/Musaffa screen can set `compliant`).

**Flags worth your attention before reviewing any of these:**
- **ESE (ESCO Technologies)** — see Action flag #5 above. Aerospace & Defense
  segment manufactures military ejection-seat and missile-arming hardware.
  Likely business-activity fail; the clean ratio pre-check here can't see this.
- **PLTR (Palantir)** — carried over from prior runs; still largely
  government/defense/intelligence data analytics (Gotham, Foundry). External
  screeners split, with at least one rating it DOUBTFUL on >5% prohibited
  income. Treat as a likely fail pending your own Zoya/Musaffa screen.
- **JNJ (Johnson & Johnson)** — new lead (SPUS holding), capped at RESEARCH
  per leads.md: reward:risk 2.0:1 is below the discovery-stage floor, and its
  2026-07-15 earnings print is only 3 days out. Mechanical cap, not a
  business concern.
- **MT (near-zero engineered range)** — the existing card (unchanged from
  2026-07-07) still shows an implausibly tight $65.35 entry / $65.31 stop /
  $65.42 T1 band on a $65 stock with $2.40 ATR elsewhere in the formula.
  Still worth checking the raw ATR/52w-high inputs by hand before trusting it.
- **MU / ALAB (RESEARCH, not LEAD)** — capped by mechanical gates, not a
  business problem: MU fails the 60-day catalyst horizon (73 days to its
  print); ALAB fails the >=3.0 asymmetry floor on the discovery-stage
  reward:risk.
- **Dropped from last run's list**: AR, AU, CDE, TER, KLIC, AMD, CF, SIMO no
  longer rank in today's top 20 (pool composition shifts each run with
  price/screen changes) — not a signal on those names individually.

## Follow-ups (priority order)

1. **[Urgent — 7th report unresolved, screen now >1 month stale] FIG
   compliance**: re-screen in Zoya/Musaffa. This has been the top flag since
   2026-06-25 with no change logged.
2. **[New — Shariah] ESE**: probable business-activity fail (military
   ejection-seat/missile-arming hardware manufacturing) — screen before
   writing it up as anything beyond RESEARCH.
3. **[Carried over — Shariah] PLTR**: still likely a business-activity fail
   (government/defense/intelligence contracts) per external screeners.
4. **[Near-term] NOW earnings 2026-07-22** (10 days out) — binary event for
   >50% of book value; decide in advance whether you want to hold through
   the print at current sizing given VALUATION_RICH is still firing.
5. **[Data quality — carried over] MT setup card**: still an implausibly
   tight auto-filled entry/stop/target band; don't trust it without checking
   the raw ATR/52w-high inputs.
6. **[Housekeeping] 8 new DRAFT setup cards** added this run (MSFT, ZS, STX,
   CLS, APH, GDDY, JNJ, ESE); 12 from prior runs remain untouched and still
   unreviewed. None are `planned`, none can reach BUY-CANDIDATE yet.
7. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Figma Shares Edge Higher Thursday: What's Driving the Move? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60373502/figma-shares-edge-higher-thursday-whats-driving-the-move)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [Insider Sell: Shaunt Voskanian Sells 8,629 Shares of Figma Inc (FIG) — GuruFocus](https://www.gurufocus.com/news/8950468/insider-sell-shaunt-voskanian-sells-8629-shares-of-figma-inc-fig)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — BigGo Finance](https://finance.biggo.com/news/ir_NOW_20260701_e8087941d423)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect)
- [ESCO Technologies (ESE) Stock News & Updates — StockTitan](https://www.stocktitan.net/news/ESE/)
- [ESCO Technologies Inc — Form ARS FY2025 — SEC](https://www.sec.gov/Archives/edgar/data/866706/000110465925118056/tm2526352d2_ars.pdf)
