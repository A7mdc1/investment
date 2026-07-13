# Portfolio Assessment — 2026-07-13

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 20-name pool by max-benefit rank) →
`scaffold.py --all-leads` (11 new DRAFT setup cards auto-filled for names
without one; 9 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run separately — still 0 closed trades (no
`transactions.csv` yet — discipline guard stays dormant until you start
logging via `/apply-trade`).

## Verdicts (lead with this)

**FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
irrespective of price). **Unresolved for a seventh consecutive run** (first
flagged 2026-06-15, six days ago it was already six runs unresolved). Live
price **$23.45**, up **+9.4%** vs. the $21.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.9:1 (skew argues against holding, not for adding) |
| Shariah | FAIL — recorded non-compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$15.08** vs. $23.45 price -> **-35.7%** (price is rich to the model) |
| Trailing stop (chandelier) | $18.9508 — price ~23.7% above it |
| 6m momentum (skip last month) | -46.9% |
| Portfolio note | ATR 6.54% — vol-throttle note (moot; this is a SELL, not a candidate to add) |
| Would buy today? | No |
| What changes verdict | Shariah screen flipping to compliant in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$112.67**, **-2.0%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $112.67 price -> **+6.9% upside** to the model |
| Trailing stop (chandelier) | $97.3885 — price is **$15.28 above it** (last cycle it had briefly dipped below; now clear again) |
| 6m momentum (skip last month) | -27.5% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| FIG | $23.45 | 35 | $21.43 | $821.45 | +9.4% | 51.0% |
| NOW | $112.72 | 7 | $114.97 | $789.04 | -2.0% | 49.0% |

**Total value: $1,610.49** | Cost: $1,554.84 | **Total return: ~+3.6%** (+$55.65 unrealised)

Both names are up since last run (2026-07-07): FIG +11.2% in six days
(rebounding on Citigroup/BofA Buy-rating coverage — see below), NOW +4.4%.
The portfolio flipped from -4.0% to +3.6% over the week, driven almost
entirely by FIG's bounce — which is exactly why the compliance gate matters
here: the position that's rallying hardest is the one flagged to exit.

## Action flags (priority order)

1. **[Mandate] FIG NON-COMPLIANT** — off-policy for a Shariah mandate,
   independent of price. **Seventh run unresolved**, and now FIG is not just
   your largest position (51% of the book) but also your only unrealised
   gain (+9.4%) — the compliance question is getting more expensive to leave
   open, not less.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF / FIG] Price is ~55% above intrinsic value** ($23.45 vs. $15.08 on
   the recorded growth/discount assumptions) — a second, independent
   argument (beyond compliance) against treating the rally as a reason to
   add or hold longer.
4. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22 — 9 days out.**
   Analysts model subscription revenue of $3.815-3.820B (~21-21.5% cc
   growth) and EPS of $0.40 (down y/y on comp, not a growth-story break).
   Reported headwind: ~75bp subscription-growth drag from delayed
   Middle-East on-prem deal closings tied to regional conflict — worth
   watching on the call. [Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect)
5. **[New leads this run]** Two SPUS-holding LEADs from today's discovery pool
   not seen last week: **TSLA** (earnings 2026-07-22, same day as NOW) and
   **GOOGL** (earnings 2026-07-22). Both are UNVERIFIED Shariah (ratio
   pre-check only) — standard mega-cap ratio profile, but confirm the
   business-activity screen yourself before treating either as more than a
   LEAD.

## Per-holding read

### FIG — Figma, Inc.
**Case to keep (fundamental, NOT compliance):** the rebound this run has a
catalyst behind it, not just noise — Citigroup initiated coverage 2026-07-01
with a Buy rating and $36 target, and Bank of America reinstated a Buy at
$30, both citing the Q1 print (46% revenue growth y/y, 139% net dollar
retention, the highest in two years, paid customers +54% y/y to ~690K).
[Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60373502/figma-shares-edge-higher-thursday-whats-driving-the-move) ·
[StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)

**Case to exit (compliance + DCF, both independent of each other and of the
fundamental story above):** NON-COMPLIANT per your mandate — this overrides
the fundamental debate entirely; seven consecutive cycles unresolved now.
The DCF model (30% 5y growth, 12% discount rate) puts intrinsic value at
$15.08 vs. a $23.45 price, a ~55% premium to the model — a materially wider
gap than last run's ~40%, since the price rallied while the model didn't
move. Stock is still ~81% below its 12-month high per one tracker, so the
rebound is off a very depressed base, not a return to prior highs.

**COMPLIANCE_GATE verdict: SELL — exit/timing is your decision; cure/purify per Zoya/Musaffa.**
The longer this sits open while the position both grows as a share of the
book (51%, up from 49% last week) and posts your only gain, the more a
"wait and see" default is itself a decision.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (9 days out) — same
guided subscription-revenue and EPS figures as last run; the AI-security
joint offering with Accenture continues to extend the enterprise-security
narrative; DCF shows +6.9% upside to intrinsic value ($120.42) at recorded
assumptions; consensus remains "Strong Buy" (36/44 analysts per one
tracker); price has moved back above the chandelier trailing stop after
briefly dipping below it last run.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-27.5% (worse than last run's -23.0%); reported ~75bp subscription-growth
headwind from delayed Middle-East deal closings tied to regional conflict —
a real, dated data point to listen for on the 2026-07-22 call, not
speculation. [Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenows-q2-2026-earnings-expect-121215371.html)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE fired -> FIG**: SELL, unresolved for a seventh
  consecutive run — flagging again rather than repeating the case: see
  Action flag #1.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -2.0% vs. the 20% threshold.
- **TRAIL_STOP -> NOW**: does NOT fire (`trade_type: core` exempts it from
  the technical trailing-stop rule); price is now comfortably above the
  computed level again ($112.67 vs. $97.39), so last run's open question is
  moot for now but the structural gap (core positions never get a
  mechanical TRAIL_STOP) still stands as a policy decision you haven't made.
- **VOL_THROTTLE note -> FIG**: ATR 6.54% — informational only since FIG is
  already a SELL, not an add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| FIG | $15.08 | $23.45 | -35.7% | growth_5y 30%, terminal 3%, discount 12% |
| NOW | $120.42 | $112.72 | +6.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run — expected, since no card has
been reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 20 leads, 11 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 20 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead that didn't
already have one (9 cards — LIF, ALKT, MT, PLTR, FICO, DUOL, VRNS, ULTA,
SIMO, PAY — already existed from last run and were left unchanged; 11 new
DRAFT cards written: CNQ, RCL, TSLA, ZS, CVE, MSFT, GOOGL, CRDO, JNJ, GDDY).
**Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to
review and edit, never buys.** None can reach BUY-CANDIDATE until you
review the card, edit anything you disagree with, set `status: planned`,
and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| CNQ | LEAD | new | 13.4:1 | earnings 2026-08-06 | 24 |
| LIF | LEAD | existing | 13.5:1 | earnings 2026-08-10 | 28 |
| ALKT | LEAD | existing | 11.9:1 | earnings 2026-07-29 | 16 |
| RCL | LEAD | new | 9.2:1 | earnings 2026-07-28 | 15 |
| TSLA | LEAD | new | 6.8:1 | earnings 2026-07-22 | 9 |
| ZS | LEAD | new | 8.9:1 | earnings 2026-09-02 | 51 |
| MT | LEAD | existing | 5.1:1 | earnings 2026-07-30 | 17 |
| PLTR | LEAD | existing | 6.1:1 | earnings 2026-08-03 | 21 |
| CVE | LEAD | new | 4.1:1 | earnings 2026-07-30 | 17 |
| MSFT | LEAD | new | 5.0:1 | earnings 2026-07-29 | 16 |
| FICO | LEAD | existing | 5.2:1 | earnings 2026-07-29 | 16 |
| GOOGL | LEAD | new | 4.0:1 | earnings 2026-07-22 | 9 |
| DUOL | LEAD | existing | 4.9:1 | earnings 2026-08-05 | 23 |
| VRNS | RESEARCH | existing | 3.0:1 | earnings 2026-07-28 | 15 |
| ULTA | LEAD | existing | 6.3:1 | earnings 2026-08-27 | 45 |
| SIMO | RESEARCH | existing | 2.0:1 | earnings 2026-07-29 | 16 |
| CRDO | LEAD | new | 4.9:1 | earnings 2026-09-02 | 51 |
| JNJ | RESEARCH | new | 1.7:1 | earnings 2026-07-15 | 2 |
| GDDY | LEAD | new | 3.4:1 | earnings 2026-07-30 | 17 |
| PAY | LEAD | existing | 3.2:1 | earnings 2026-08-03 | 21 |

All 20 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, CDE, MT** — carried over from last run's flags (government/
  defense business-activity question for PLTR; mining/royalty financing
  structure questions for precious-metals names; MT's implausibly tight
  engineered entry/stop/target band). Nothing new to add — still open,
  still worth checking before you spend review time on the cards.
- **TSLA / GOOGL / MSFT (new this run, SPUS holdings)** — mega-caps with
  generally clean debt/liquidity ratios on the pre-check, but each carries
  its own business-activity nuance worth a real Zoya/Musaffa screen rather
  than assuming "SPUS holds it, so it's fine": Tesla's financing-arm
  interest income, Alphabet's ad/interest-bearing cash mix, and Microsoft's
  interest income and any gaming/finance-adjacent lines. Standard names,
  still need the actual screen.
- **JNJ (2 days to catalyst, RESEARCH not LEAD)** — capped by the asymmetry
  gate (reward:risk 1.7:1 < 3.0 floor) despite the near-term catalyst; not a
  business problem, just doesn't clear the bar today.

## Follow-ups (priority order)

1. **[Urgent — 7th run unresolved, and now the top-weighted, only-gaining
   position] FIG compliance**: re-screen in Zoya/Musaffa. The longer this
   stays open, the larger a share of the book it represents.
2. **[Time-boxed] NOW earnings 2026-07-22** — 9 days out; the ~75bp
   Middle-East deal-delay headwind is a concrete thing to listen for on the
   call, distinct from the general VALUATION_RICH flag.
3. **[Ongoing] TSLA / GOOGL business-activity screen** — both share NOW's
   earnings date (2026-07-22); if either is being considered, get the actual
   Zoya/Musaffa screen done before, not after, that date.
4. **[Housekeeping] 11 new DRAFT setup cards** added this run (20 total in
   `setups/`); none are `planned`, none can reach BUY-CANDIDATE. Review at
   your own pace — the earnings dates they're built around (several in the
   next 2-3 weeks) don't wait.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Figma Shares Edge Higher Thursday: What's Driving the Move? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60373502/figma-shares-edge-higher-thursday-whats-driving-the-move)
- [FIG Stock Pops As Citigroup Launches Bullish Coverage — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01/)
- [FIG Stock Rises As Citigroup Targets $36 Upside — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_07_01-2/)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenows-q2-2026-earnings-expect-121215371.html)
- [+6.31% for ServiceNow stock as Q2 2026 earnings date approaches — TradersUnion](https://tradersunion.com/news/financial-news/show/2549550-servicenow-gains-6-31percent-to-usd105-54/)
