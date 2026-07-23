# Portfolio Assessment — 2026-07-23

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (18 new DRAFT setup cards auto-filled for names
without one; the rest left unchanged) → `prices.py` / `shariah.py` / `dcf.py`
/ `signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` still shows 0 closed trades — `transactions.csv` is
gitignored (never committed) and hasn't been started locally, so the
discipline guard stays dormant.

Since the last run (2026-07-13) the book changed: **FIG was sold in full**
(closed on the seventh-run compliance flag) and a **new BMNR position was
opened**. This is now a 2-name book: BMNR + NOW.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$16.46**, up
**+6.7%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-11.2:1** (DCF-vs-stop skew argues against holding, not for adding) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see flag #1 below**: the mechanical ratio pre-check FAILS on business activity |
| DCF intrinsic value | **$0.72** vs. $16.46 price -> **-95.6%** — see caveat under DCF below; a standard cash-flow DCF is likely not a meaningful model for this business |
| Trailing stop (chandelier) | $15.0134 — price ~9.6% above it |
| 6m momentum (skip last month) | -48.4% |
| Portfolio note | ATR 6.55% — vol-throttle note |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW; no thesis/stop/target recorded on the card at all |
| What changes verdict | A completed PM record (conviction/stop/target/pre_mortem — all currently blank), or the Shariah ratio flag getting resolved |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$94.61**, **-17.7%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — recommend.py can't self-assess without a stated thesis-vs-price edge |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $94.61 price -> **+27.3% upside** to the model |
| Trailing stop (chandelier) | $96.6661 — price is **$2.06 BELOW it** (see flag #2) |
| 6m momentum (skip last month) | -23.4% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $16.46 | 10 | $15.43 | $164.60 | +6.7% | 19.9% |
| NOW | $94.61 | 7 | $114.97 | $662.27 | -17.7% | 80.1% |

**Total value: $826.87** | Cost: $958.09 | **Total return: ~-13.7%** (-$131.22 unrealised)

NOW is now the overwhelming majority of the book (80%) after the FIG close
shrank total capital deployed. NOW itself is down another sharp leg since
2026-07-13 ($112.72 -> $94.61, -16.1% in ten days) even as the underlying
business reported a strong quarter (see flag #3) — the technical trend and
the fundamental print are pulling in opposite directions right now.

## Action flags (priority order)

1. **[Shariah — new, needs your attention] BMNR's mechanical ratio pre-check
   FAILS**, flagging `industry 'Capital Markets' — core business fails
   screen`, even though the broker app recorded it compliant on 2026-07-07.
   This is a real, substantive conflict, not noise: BMNR's actual business is
   an Ethereum treasury — it holds ~5.77M ETH (~4.8% of total supply) and
   **stakes roughly 4.9M of those tokens for a projected ~$235-284M/yr in
   staking revenue** ([Timothy Sykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20/),
   [PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)).
   A treasury company whose core economics are staking-yield income is
   exactly the kind of business-activity/interest-income question a
   Shariah screen is built to catch — recommend re-verifying this
   specifically in Zoya/Musaffa rather than resting on the broker's
   "compliant" tag, especially since this is now ~20% of the book.
2. **[Technical / NOW] Price is now BELOW the chandelier trailing stop**
   ($94.61 vs. $96.6661) for the first time since this series of reports
   began. Because `trade_type: core`, the mechanical TRAIL_STOP rule does
   not fire (core positions are exempt by design) — this is the same
   structural gap noted last run, except it's no longer hypothetical: the
   stop is actually breached now, not just "close." Worth a conscious
   decision on whether `trade_type` should still read `core` for a position
   you're also tracking a trailing stop on.
3. **[Data caveat / NOW] Live price may lag the post-earnings move.** NOW
   reported Q2 FY2026 results on 2026-07-22 (after last close): subscription
   revenue **$3.877B, +24.5% y/y**, non-GAAP EPS **$0.90** (beat), operating
   margin 29.5% (3pts above guidance), full-year subscription guidance
   **raised** to $15.76-15.78B ([gurufocus](https://www.gurufocus.com/news/8973045/servicenow-now-reports-strong-q2-earnings-boosts-revenue-outlook),
   [gurufocus](https://www.gurufocus.com/news/8974525/servicenow-now-shares-surge-5-following-strong-q2-2026-earnings)).
   Multiple outlets report the stock **up 5-7% in the session following the
   print**, but the price this run's scripts pulled from yfinance ($94.61)
   is essentially flat vs. the pre-earnings level (~$95.66) — i.e. the
   figures above (weight, return, trailing-stop distance) may understate
   where the stock actually trades right now. Don't fabricate the corrected
   number; re-run `prices.py` before acting, or check a live quote directly.
4. **[Drawdown / NOW] -17.7% vs. cost** — approaching but not yet past the
   `drawdown_review_pct` 20% threshold that would force a REVIEW.
5. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
6. **[New this run — correlated cluster] Five precious-metals/mining LEADs**
   appeared together: **AGI, CDE, AU, KGC, HBM** (gold/silver miners,
   `undervalued_large_caps` screen). If any of these get reviewed, size them
   as ONE correlated bet, not five independent ones — same logic as the
   existing semiconductor-cluster note in `watchlist.md`. AU and CDE carry
   the same mining-royalty/financing-structure business-activity question
   flagged in prior runs; nothing new there, still open.
7. **[Housekeeping / BMNR] The holding's PM record is essentially blank** —
   no `conviction`, `initial_stop`, `target_price`, `invalidation`, or
   `pre_mortem` filled in on `holdings/bmnr.md`. recommend.py is working off
   the DCF stop/target only because nothing else is there. Worth filling in
   before this compounds into another multi-run open flag like FIG's was.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** the position is up +6.7% since the $15.43 entry. ETH
holdings and staking scale keep growing (5.74M -> 5.77M tokens,
$11.1B -> $11.3B total crypto/cash in two weeks per the company's own
releases), the stock was recently added to the Russell 1000 (more
institutional visibility/liquidity), and analyst commentary stays
constructive (B. Riley cut its price target to $25 from $33 but **kept a
Buy rating**) ([timothysykes.com](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20-2/)).

**Case to trim/review:** the DCF model puts intrinsic value at **$0.72**
against a $16.46 price — but a discounted-cash-flow model built for an
operating business is a poor fit for a treasury vehicle whose value is
mostly driven by ETH holdings (NAV), not discounted operating cash flow;
treat that -95.6% figure as a model-mismatch artifact, not a real read on
fair value, and don't cite it as a reason to sell on its own. The real,
substantive question is the Shariah ratio pre-check failure on
"Capital Markets" business activity plus the staking-yield income stream
(flag #1) — that is the actual case for a closer look, independent of price.
Note also the company issued a **correction** to one of its holdings
press releases this month — a minor operational-discipline data point on a
young, fast-moving disclosure cadence.

**COMPLIANCE_GATE status: recorded compliant, but the mechanical flag
disagrees with the broker tag on business activity — re-verify in
Zoya/Musaffa before treating this as settled.**

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 was a clean beat-and-raise — 24.5% subscription
growth, EPS beat, margin 3pts above guidance, ServiceNow AI crossed $1B ACV
with a path to $1.5B by year-end, 123 seven-figure-plus deals (+40% y/y)
([gurufocus](https://www.gurufocus.com/news/8973045/servicenow-now-reports-strong-q2-earnings-boosts-revenue-outlook)).
DCF still shows +27.3% upside to intrinsic value at recorded assumptions.
Reported market reaction was a 5-7% pop, not a selloff.

**Case to trim/watch closely:** despite the beat, the stock had been down
**-37.6% YTD** heading into the print ([247wallst.com](https://247wallst.com/investing/2026/07/22/live-will-servicenows-q2-earnings-tonight-drive-a-rebound-after-38-ytd-decline/))
and the price this run's data pulled is still below the chandelier trailing
stop — a real tension between "the fundamentals just got better" and "the
technical trend/stop discipline says something's wrong." P/E ~119 remains
VALUATION_RICH; 6m momentum -23.4%. Given the core/TRAIL_STOP exemption gap
(flag #2), this is a case where the mechanical engine will stay silent on
the technical breach unless you decide otherwise.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -17.7% vs. the 20% threshold — close, not there yet.
- **TRAIL_STOP does NOT fire -> NOW**: `trade_type: core` exempts it from the
  mechanical rule even though price ($94.61) is now below the computed level
  ($96.6661) — see flag #2; this is a policy decision you haven't made, not
  a bug.
- **VOL_THROTTLE note -> BMNR, NOW**: both ATR ~6.5-6.6% — informational
  size-down note.
- **No rule fired -> BMNR**: verdict defaults to HOLD; see housekeeping
  flag #7 on the missing PM fields.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $16.46 | -95.6% | growth_5y 5%, terminal 2.5%, discount 10% — **likely not a meaningful model for a crypto-treasury business; see per-holding read** |
| NOW | $120.42 | $94.61 | +27.3% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet).

## Draft & planned setups — 50 leads, 18 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank, widened from 20 last run per
`discover_top_n: 50`). `scaffold.py --all-leads` auto-filled 18 new DRAFT
cards for names without one (FN, HAS, CIEN, GWRE, BKR, STX, KEYS, SMCI, ARW,
CLS, ESE, SFD, TS, P, AAPL, DLO, DINO, DELL, AVGO, LLY, NVDA, BBY — several
of these already existed and were left unchanged; see script output for the
exact list). **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.**

Top of the pack by mechanical rank (LEAD verdict, has a setup card):

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| FICO | LEAD | existing | 20.0:1 | earnings 2026-07-29 | 6 |
| DUOL | LEAD | existing | 14.4:1 | earnings 2026-08-05 | 13 |
| MSFT | LEAD | existing | 9.7:1 | earnings 2026-07-29 | 6 |
| LIF | LEAD | existing | 20.0:1 | earnings 2026-08-10 | 18 |
| CDE | LEAD | existing | 20.0:1 | earnings 2026-08-05 | 13 |
| AU | LEAD | existing | 9.5:1 | earnings 2026-07-31 | 8 |
| PLTR | LEAD | existing | 20.0:1 | earnings 2026-08-03 | 11 |
| VRNS | LEAD | existing | 5.5:1 | earnings 2026-07-28 | 5 |
| ZS | LEAD | existing | 10.6:1 | earnings 2026-09-02 | 41 |
| PAY | LEAD | existing | 5.4:1 | earnings 2026-08-03 | 11 |
| ULTA | LEAD | existing | 4.9:1 | earnings 2026-08-27 | 35 |
| CRDO | LEAD | existing | 3.6:1 | earnings 2026-09-02 | 41 |

Dropped off this run vs. 2026-07-13 (no longer in the top-50 pool as ranked):
TSLA, GOOGL, JNJ, GDDY. New names not seen last run include the five
precious-metals miners (flag #6) plus FN, HAS, UTHR, KEYS, SMCI, ESE, SFD,
TER.

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, CDE, MT** — carried over from prior runs (government/defense
  business-activity question for PLTR; mining/royalty financing structure
  questions for precious-metals names; MT's tight engineered entry/stop/target
  band). Nothing new to add.
- **AGI, KGC, HBM (new)** — same mining-royalty/financing-structure question
  as AU/CDE; group all five as one correlated cluster if reviewed (flag #6).
- **MSFT, PLTR (SPUS holdings, mega-caps)** — standard ratio pre-check clean,
  but each carries its own business-activity nuance (interest income,
  government contracts) worth the actual Zoya/Musaffa screen, not an
  assumption from "SPUS holds it."

## Follow-ups (priority order)

1. **[New, needs your attention] BMNR Shariah ratio-precheck failure** —
   re-screen in Zoya/Musaffa specifically on the ETH-staking business
   model/income, don't rely on the broker's compliant tag alone (flag #1).
2. **[New] NOW technical trailing-stop breach** — decide whether `trade_type:
   core` should still exempt this position from the mechanical TRAIL_STOP
   rule now that it's actually triggered, not hypothetical (flag #2).
3. **[Verify] NOW live price** — re-check against a live quote; this run's
   data may be understating a post-earnings pop reported elsewhere (flag #3).
4. **[Housekeeping] Fill in BMNR's PM record** — conviction, initial_stop,
   target_price, invalidation, pre_mortem are all still blank (flag #7).
5. **[Housekeeping] 18 new DRAFT setup cards** added this run; none are
   `planned`, none can reach BUY-CANDIDATE. Review at your own pace.
6. **[Ongoing] Precious-metals cluster (AGI/CDE/AU/KGC/HBM)** — resolve the
   mining-royalty business-activity question once, apply it to all five.
7. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow (NOW) Reports Strong Q2 Earnings, Boosts Revenue Outlook — GuruFocus](https://www.gurufocus.com/news/8973045/servicenow-now-reports-strong-q2-earnings-boosts-revenue-outlook)
- [ServiceNow (NOW) Shares Surge 5% Following Strong Q2 2026 Earnings — GuruFocus](https://www.gurufocus.com/news/8974525/servicenow-now-shares-surge-5-following-strong-q2-2026-earnings)
- [Live: Will ServiceNow's Q2 Earnings Tonight Drive a Rebound After 38% YTD Decline? — 24/7 Wall St.](https://247wallst.com/investing/2026/07/22/live-will-servicenows-q2-earnings-tonight-drive-a-rebound-after-38-ytd-decline/)
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Traders — Timothy Sykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20/)
- [BMNR Stock Climbs As Massive Ethereum Bet Takes Center Stage — Timothy Sykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20-2/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
