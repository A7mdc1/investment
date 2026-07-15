# Portfolio Assessment — 2026-07-15

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (26 new DRAFT setup cards auto-filled for names
without one; the rest left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run separately — still 0 closed trades (no
`transactions.csv` yet — discipline guard stays dormant until you start
logging via `/apply-trade`).

This is the first assessment run since the FIG→BMNR swap (FIG sold, BMNR
bought, recorded 2026-07-07 per the prior report's compliance-flag closure).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$15.95**,
**+3.4%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -10.6:1 (skew argues against adding, not for it) |
| Shariah | recorded PASS (broker app, screened 2026-07-07, not stale) — **but see flag below** |
| DCF intrinsic value | **$0.76** vs. $15.95 price -> **-95.2%** (model implies the stock is wildly rich — see caveat) |
| Trailing stop (chandelier) | $14.5267 — price ~9.8% above it |
| 6m momentum (skip last month) | -48.2% |
| Portfolio note | ATR 6.88% > 6% throttle — size down per vol throttle |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW, and DCF/asymmetry both argue against |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**DCF caveat:** BMNR is functionally an Ethereum treasury/staking vehicle,
not an operating-earnings business — a standard 5-year-growth DCF (5%
growth, 2.5% terminal, 10% discount) is the wrong tool for a company whose
value is mark-to-market crypto holdings ($11.3B in crypto + cash per its
latest release) rather than discounted cash flow. Treat the -95.2% "upside"
number as a model-mismatch artifact, not a real valuation signal — book
value / crypto-NAV would be the more relevant lens, which this pipeline
doesn't compute.

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$104.88**, **-8.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | MEDIUM — reward:risk 2.0:1 (moderate skew) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $104.88 price -> **+14.8% upside** to the model |
| Trailing stop (chandelier) | $96.9832 — price is **$7.90 above it** |
| 6m momentum (skip last month) | -28.4% |
| Would buy today? | Mechanically yes per recommend.py's gates |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.96 | 10 | $15.43 | $159.60 | +3.4% | 17.9% |
| NOW | $104.76 | 7 | $114.97 | $733.32 | -8.9% | 82.1% |

**Total value: $892.93** | Cost: $959.09 | **Total return: ~-6.9%** (-$66.16 unrealised)

The book is now heavily concentrated in NOW (82% of value) after the FIG
exit and small BMNR add — NOW's -8.8% drawdown since cost basis is doing
almost all the damage to the total, while BMNR is the only green position.

## Action flags (priority order)

1. **[Mandate — new this run] BMNR business-activity flag.** The mechanical
   ratio pre-check now flags BMNR's industry as `Capital Markets`, which
   "matches 'capital markets' — core business fails screen." This directly
   corroborates the concern raised in the 2026-07-06 report *before* this
   position was opened: "functionally an Ethereum treasury/staking vehicle
   ($9.6-10.7B in crypto/ETH holdings, ~4.72M ETH staked, a 9.50% preferred
   raise) ... very likely to fail a Shariah business-activity screen (crypto
   staking yield, interest-bearing preferred structure) ... Treat as a
   probable AVOID pending Zoya/Musaffa, not just 'unverified.'" The position
   was opened 2026-07-07 recorded `compliant` via broker app — that recorded
   status and the mechanical pre-check now disagree. This is 17.9% of the
   book. Re-screen in Zoya/Musaffa is the highest-priority follow-up this run.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Catalyst / NOW] Q2 FY2026 earnings confirmed for 2026-07-22 — 7 days
   out**, reported after market close with a call at 2pm PT.
   [ServiceNow investor release](https://www.stocktitan.net/news/NOW/service-now-to-announce-second-quarter-2026-financial-results-on-m5cdholl37f1.html)
   The holding's front-matter `catalyst.date` is still `null` — worth
   updating now that IR has posted a date.
4. **[Momentum / BMNR] ATR 6.88%** exceeds the 6% vol-throttle threshold —
   informational size-down note, not a verdict change.
5. **[New leads this run]** 50-name discovery pool (up from 20 last run,
   `discover_top_n` unchanged at 50 in rules.md — prior runs likely
   truncated display). See the setups table below.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** Up +3.4% since cost basis and +10.6% in the single most
recent session on continued momentum — ETH holdings now at 5.77M tokens
(4.8% of total ETH supply), total crypto + cash holdings of $11.3B, staked
ETH at 4.92M ($9.0B), annualized staking revenue ~$242M, and inclusion in
the Russell 1000 as of 2026-06-26 (index-fund flows are a real, if modest,
technical tailwind).
[PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_14/)

**Case to trim/exit:** The Shariah business-activity question flagged
*before* this position was opened has now shown up mechanically too
(industry: Capital Markets, ratio pre-check fails the business screen). The
company's economics are ETH staking yield and a 9.50% interest-bearing
preferred raise (BMNP) — both structurally hard to reconcile with a
Shariah-compliant mandate independent of price action. DCF is not a useful
counter-argument here (see caveat above) since this isn't a cash-flow
business. 6m momentum (skip last month) is -48.2% despite the recent bounce
— a volatile, momentum-negative name on a longer window.

**No hard verdict change yet** (recorded status is still `compliant`), but
this is now a live disagreement between the recorded screen and the
mechanical pre-check on a name that was already called out as a probable
fail before purchase — re-screening is the clear next step, not a
"wait and see."

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings confirmed for **2026-07-22** (7 days
out); DCF shows +14.8% upside to intrinsic value ($120.42) at recorded
assumptions; price is back above the chandelier trailing stop
($104.88 vs. $96.98).
[BigGo](https://finance.biggo.com/news/ir_NOW_20260701_e8087941d423) ·
[Investing.com](https://m.in.investing.com/news/stock-market-news/servicenow-to-report-q2-earnings-on-july-22-93CH-5479033?ampMode=1)

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m
momentum -28.4% (worse than the 07-13 run's -27.5%); the position is down
-8.8% since cost basis and now 82% of the book — a concentration level that
would trigger CONCENTRATION/TRIM under `max_position_pct` (22%) if the
rules recognized a 2-name book (they don't, below `min_names_for_concentration`).
Worth a deliberate look regardless of whether the mechanical rule fires.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **VOL_THROTTLE note -> BMNR**: ATR 6.88% > 6% — size down if adding, informational only otherwise.
- **CONCENTRATION not firing (structurally muted) -> NOW at 82.1% of a
  2-name book**: the rule is silent below `min_names_for_concentration: 4`,
  but 82% in one name is a policy question worth revisiting by eye, not
  waiting for the rule to catch up.
- **DRAWDOWN_REVIEW not firing -> NOW**: -8.8% vs. the 20% threshold.
- **TRAIL_STOP -> both**: does NOT fire (`trade_type: core` exempts both
  from the technical trailing-stop rule); both are currently above their
  computed chandelier levels anyway.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.76 | $15.96 | -95.2% | growth_5y 5%, terminal 2.5%, discount 10% — **model mismatch, see caveat** |
| NOW | $120.42 | $104.89 | +14.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run — expected, since no card has
been reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 50 leads, 26 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank — the pool widened from 20 to 50
this run per `discover_top_n` in rules.md). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead that didn't
already have one: **26 new cards** — UTHR, CIEN, LLY, DELL, AVGO, DINO, STX,
GWRE, FLYW, AAPL, PSX, NVDA, WDC, ARW, DLO, TTMI, BKR, TS, PDFS, BBY, APH,
FSLR, AMKR, CLS, FORM, AA. 24 cards already existed (FICO, ALKT, CNQ, TSLA,
JNJ, ULTA, LIF, SIMO, CF, MT, CVE, MSFT, VRNS, GDDY, DUOL, PLTR, AMD, ZS,
PAY, GOOGL, ALAB, KLIC, RCL, TER) and were left unchanged.
**Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to
review and edit, never buys.** None can reach BUY-CANDIDATE until you
review the card, edit anything you disagree with, set `status: planned`,
and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| FICO | LEAD | existing | 20.0:1 | earnings 2026-07-29 | 14 |
| CNQ | LEAD | existing | 12.7:1 | earnings 2026-08-06 | 22 |
| ALKT | LEAD | existing | 10.7:1 | earnings 2026-07-29 | 14 |
| ULTA | LEAD | existing | 10.3:1 | earnings 2026-08-27 | 43 |
| CIEN | RESEARCH | new | 13.0:1 | earnings 2026-09-09 | 56 |
| TSLA | LEAD | existing | 7.3:1 | earnings 2026-07-22 | 7 |
| UTHR | RESEARCH | new | 8.0:1 | earnings 2026-07-29 | 14 |
| JNJ | LEAD | existing | 5.9:1 | earnings 2026-07-15 | 0 |
| LIF | LEAD | existing | 6.2:1 | earnings 2026-08-10 | 26 |
| LLY | RESEARCH | new | 5.7:1 | earnings 2026-08-05 | 21 |
| CF | LEAD | existing | 5.2:1 | earnings 2026-08-05 | 21 |
| ZS | LEAD | existing | 5.2:1 | earnings 2026-09-02 | 49 |
| AVGO | LEAD | new | 4.7:1 | earnings 2026-09-03 | 50 |
| PLTR | LEAD | existing | 4.5:1 | earnings 2026-08-03 | 19 |
| GWRE | RESEARCH | new | 4.3:1 | earnings 2026-09-03 | 50 |
| MSFT | LEAD | existing | 4.1:1 | earnings 2026-07-29 | 14 |
| GDDY | LEAD | existing | 4.2:1 | earnings 2026-07-30 | 15 |
| DUOL | LEAD | existing | 4.2:1 | earnings 2026-08-05 | 21 |
| SIMO | LEAD | existing | 3.8:1 | earnings 2026-07-29 | 14 |
| CVE | LEAD | existing | 3.8:1 | earnings 2026-07-30 | 15 |
| MT | LEAD | existing | 3.6:1 | earnings 2026-07-30 | 15 |
| PAY | LEAD | existing | 3.2:1 | earnings 2026-08-03 | 19 |
| VRNS | RESEARCH | existing | 3.0:1 | earnings 2026-07-28 | 13 |
| DELL | RESEARCH | new | 2.6:1 | earnings 2026-09-03 | 50 |
| NVDA | RESEARCH | new | 2.0:1 | earnings 2026-08-26 | 42 |
| DLO | RESEARCH | new | 1.4:1 | earnings 2026-08-13 | 29 |
| AMD | RESEARCH | existing | 1.3:1 | earnings 2026-08-04 | 20 |
| GOOGL | RESEARCH | existing | 1.2:1 | earnings 2026-07-22 | 7 |
| PSX | RESEARCH | new | 0.7:1 | earnings 2026-08-05 | 21 |
| DINO | RESEARCH | new | 0.2:1 | earnings 2026-07-28 | 13 |
| FLYW | RESEARCH | new | 0.1:1 | earnings 2026-08-04 | 20 |
| BBY | RESEARCH | new | 0.1:1 | earnings 2026-08-27 | 43 |
| AAPL | RESEARCH | new | 0.0:1 | earnings 2026-07-30 | 15 |
| STX / WDC / ARW / ALAB / TTMI / BKR / TS / KLIC / PDFS / RCL / APH / FSLR / AMKR / CLS / FORM / AA | RESEARCH (or LEAD for AA) | mixed | n/a (no computable R:R) | various | see leads.md |

All 50 cleared the liquidity floor and a clean-or-flagged ratio pre-check —
not a full business-activity screen. Shariah status on every card is
`unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **JNJ (0 days to catalyst — earnings today, 2026-07-15)**: LEAD with a
  5.9:1 R:R, but the catalyst window is essentially closed by the time this
  report is read; treat as informational, not actionable, this cycle.
- **TSLA / GOOGL (7 days to catalyst, same date as NOW's earnings,
  2026-07-22)**: carried over from prior runs' business-activity caveats
  (Tesla's financing-arm interest income; Alphabet's ad/interest-bearing
  cash mix) — still need the actual Zoya/Musaffa screen, not an assumption
  from SPUS membership.
- **AMD / GOOGL (reward:risk < 2:1, flagged RESEARCH not LEAD)**: capped by
  the asymmetry gate despite being SPUS holdings — mechanical, not a
  business problem.

## Follow-ups (priority order)

1. **[Urgent — new this run] BMNR Shariah re-screen**: the mechanical
   ratio pre-check now flags the business activity ('Capital Markets') as a
   likely fail, matching the explicit warning issued *before* this position
   was opened. 17.9% of the book. Re-screen in Zoya/Musaffa before adding
   to it, and treat the recorded `compliant` status as unresolved rather
   than settled.
2. **[Time-boxed] NOW earnings 2026-07-22** — 7 days out, confirmed date;
   update the holding's `catalyst.date` front-matter field from `null`.
3. **[Concentration] NOW is 82.1% of a 2-name book** — the mechanical
   CONCENTRATION rule is muted below 4 names, but this is worth a
   deliberate look rather than assuming the rule would catch it.
4. **[Housekeeping] 26 new DRAFT setup cards** added this run (46+ total in
   `setups/`); none are `planned`, none can reach BUY-CANDIDATE. Review at
   your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Traders — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_14/)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — StockTitan](https://www.stocktitan.net/news/NOW/service-now-to-announce-second-quarter-2026-financial-results-on-m5cdholl37f1.html)
- [ServiceNow to report Q2 earnings on July 22 — Investing.com](https://m.in.investing.com/news/stock-market-news/servicenow-to-report-q2-earnings-on-july-22-93CH-5479033?ampMode=1)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — BigGo Finance](https://finance.biggo.com/news/ir_NOW_20260701_e8087941d423)
