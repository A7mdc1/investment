# Portfolio Assessment — 2026-07-20

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (25 new DRAFT setup cards auto-filled for leads
without one; 24 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run separately — still 0 logged trades in
`transactions.csv` (the 2026-07-13 FIG sale / BMNR buy were recorded directly
in `holdings/*.md`, not via `/apply-trade`, so the discipline guard stays
dormant — see Follow-ups).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$16.64**, up
**+7.8%** vs. the $15.43 cost basis (opened 2026-07-07).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.8:1 (skew is thin/negative on the DCF-implied target) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but the mechanical ratio pre-check flags it**: industry classified "Capital Markets," which fails the business-activity screen outright. See Action flag #1 below — this is the top item this run. |
| DCF intrinsic value | $0.72 vs. $16.64 price -> -95.7% — **caveat: a discounted-cash-flow model built for an operating growth company is not a meaningful yardstick for BMNR, which is functionally a crypto-treasury/staking vehicle (see per-holding read below), not an operating business with projectable FCF. Treat this number as noise, not signal.** |
| Trailing stop (chandelier) | $13.9171 — price ~19.6% above it |
| 6m momentum (skip last month) | -49.1% (extremely volatile name) |
| Portfolio note | ATR 6.43% — vol-throttle note; already the vol-driver of the book |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW, and the Shariah conflict above should be resolved before treating this as more than a hold |
| What changes verdict | Shariah screen resolving one way or the other (this is unresolved, not confirmed), a SELL technical trigger, or thesis_broken |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$103.98**, **-9.6%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | MEDIUM — reward:risk 2.25:1 (moderate skew) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); ratio pre-check also clean (debt ratio 2.2%, liquid ratio 5.9%) |
| DCF intrinsic value | **$120.42** vs. $103.98 price -> **+15.8% upside** to the model |
| Trailing stop (chandelier) | $96.7732 — price is $7.21 above it |
| 6m momentum (skip last month) | -27.2% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction MEDIUM |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $16.64 | 10 | $15.43 | $166.35 | +7.8% | 18.6% |
| NOW | $103.98 | 7 | $114.97 | $727.87 | -9.6% | 81.4% |

**Total value: $894.22** (tracked positions only). Note: the FIG sale on
2026-07-13 realized ~$805 in proceeds against a $154.30 BMNR buy — roughly
$650 of that is now sitting outside anything tracked in `holdings/`. If
that cash is uninvested, it isn't reflected in this report's total.

Since the last run (2026-07-13, which still held FIG + NOW): the portfolio
composition changed entirely — FIG was sold (compliance exit, +9.4% locked
in) and BMNR opened. NOW alone is down another ~7.9pp this week ($112.72 ->
$103.98), now the dominant 81% of the tracked book by weight — a
concentration outcome that isn't a policy breach (min_names_for_concentration
= 4) but is worth naming plainly given the P/E is still VALUATION_RICH and
6m momentum is negative.

## Action flags (priority order)

1. **[Mandate — new this run] BMNR Shariah conflict.** Recorded
   **compliant** by the broker app (screened 2026-07-07), but the mechanical
   ratio pre-check flags the business-activity line: Yahoo classifies BMNR's
   industry as **"Capital Markets,"** which fails the business screen
   outright (this is the same kind of hard-knockout category — conventional
   finance — the ratio pre-check treats as an absolute flag, not a soft
   score). Independent of the SIC classification, BMNR's actual business
   this quarter is an Ethereum treasury: ~5.77M ETH held (~4.8% of total ETH
   supply), ~4.9M ETH staked generating a projected **$284M/year in staking
   rewards** — a yield stream that is exactly the kind of interest-like
   income a Shariah screen exists to catch.
   [PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
   This is a **conflict between the recorded screen and the mechanical
   pre-check that didn't exist for either holding last run** — worth an
   actual Zoya/Musaffa re-screen before this sits for multiple cycles the
   way FIG's flag did.
2. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH
   holds. Do not add.
3. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22 — 2 days out**,
   after market close. Consensus: revenue ~$3.92B (+22% y/y), EPS ~$0.86.
   This is the first full quarter under ServiceNow's new all-in AI licensing
   model — flagged by multiple outlets as a real test of whether the recent
   share-price weakness is overdone. Now Assist's 2026 target was raised
   from $1B to $1.5B intra-quarter (a sign consumption is ahead of plan).
   [Zacks via Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-set-report-q2-earnings-151900170.html) ·
   [ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
4. **[Data quality] BMNR's DCF (-95.7%) is not a usable signal** — see the
   verdict table caveat above. A standard FCF-growth DCF misprices a
   crypto-treasury holding company; don't let that number drive a decision
   either way.
5. **[Infrastructure — carried over] No trade ledger yet.** The FIG
   sale/BMNR buy on 2026-07-13 were hand-edited into `holdings/*.md` rather
   than logged via `/apply-trade`, so `transactions.csv`/`journal.csv` still
   don't exist and the discipline guard (net-of-benchmark performance check)
   stays dormant.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** the position is up +7.8% since the 2026-07-07 entry.
Bitmine continues scaling its Ethereum treasury — total crypto/cash holdings
reported at **$11.3B** as of 2026-07-13, ETH holdings at 5.77M tokens (96%
of the way to a stated goal of 5% of total ETH supply), plus smaller equity
stakes in Beast Industries ($180M) and Eightco Holdings ($69M).
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_14/)
The stock jumped ~8.4% on the holdings announcement, and management is
actively pushing investor-communication material (a July 16 investor
presentation/video) to keep the story in front of the market.

**Case to trim / re-underwrite:** this is not a software or industrial
business — it is a leveraged bet on ETH price plus staking yield. 6m
momentum is -49.1% despite the recent bounce (extreme volatility, ATR
6.43%), the DCF is not a meaningful check on this kind of vehicle, and —
most importantly — the Shariah picture is genuinely unresolved: recorded
compliant by the broker app, but the mechanical pre-check flags the
business-activity line ("Capital Markets"), and the core activity
(accumulating and **staking** a cryptocurrency for yield) is a substantive
question for a Shariah screen, not a formality. The holding file itself
still reads "NEW position — screen compliance in Zoya/Musaffa before adding
more" — that screen hasn't been confirmed independently yet, two weeks in.

**HOLD stands mechanically (no rule fired), but this is the flag to resolve
first** — see Action flag #1.

### NOW — ServiceNow, Inc.
**Case to keep:** DCF shows +15.8% upside to intrinsic value ($120.42) at
recorded assumptions (18% 5y growth, 3% terminal, 10% discount); Now
Assist's 2026 revenue target was just raised 50% intra-quarter ($1B ->
$1.5B); the Armis acquisition ($7.75B) closed 2026-04-20 and is now
integrated into the AI Control Tower / security-workflow story per SEC
filings. [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000056/now-20260331.htm)
Consensus into Wednesday's print: +22% y/y revenue growth, $0.86 EPS.

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-27.2% (roughly in line with last run); the stock fell 5.8% (~$6.7B market
cap) earlier this month after IBM's warning that AI infrastructure spend is
squeezing enterprise software budgets broadly — a sector-wide read-through,
not NOW-specific, but worth listening for on the call. The Armis deal is
also expected to compress margins near-term (~25bp subscription gross
margin, ~75bp operating margin, ~200bp FCF margin) even as it adds >$340M
recurring revenue growing 50%+.
[ts2.tech](https://ts2.tech/en/servicenow-stock-slides-as-ibm-budget-warning-turns-july-earnings-into-a-core-growth-test/) ·
[ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/ueberblick/servicenow-s-high-wire-act-margin-squeeze-vs-ai-momentum-in-the-run-up/69683001)

**VALUATION_RICH verdict: HOLD, do not add** — the 2026-07-22 print is the
single biggest near-term swing factor for this position; it lands in 2 days.

## Suggested actions (from YOUR rules, rules.md)

- **DEFAULT (no rule fired) -> BMNR**: HOLD mechanically; the open item is
  the Shariah ratio-pre-check conflict (Action flag #1), which is a mandate
  question, not a rule the engine resolves for you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -9.6% vs. the 20% threshold.
- **VOL_THROTTLE note -> BMNR**: ATR 6.43% — size down per the vol throttle
  if adding; already your most volatile position.
- **TRAIL_STOP -> both**: `trade_type: core` on NOW exempts it from the
  technical trailing-stop rule; BMNR has no `trade_type` set in its
  front-matter (defaults apply) — worth setting explicitly given how far
  this diverges in character from a "core" holding.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $16.64 | -95.7% | growth_5y 5%, terminal 2.5%, discount 10% — **not a meaningful model for a crypto-treasury vehicle; see caveat above** |
| NOW | $120.42 | $103.98 | +15.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run (expected — no card has been
reviewed and flipped to `status: planned` yet).

## Draft & planned setups — 50 leads, 25 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank — the pool widened from 20 to 50
on 2026-07-13). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead that didn't already have one: **25
new cards** (UTHR, P, AVGO, DELL, SFD, STX, DINO, LLY, NVDA, FLYW, WDC, AAPL,
DLO, GWRE, TS, ARW, TTMI, BKR, BBY, APH, AMKR, ESE, FSLR, PDFS, CLS); **24
existing cards** left unchanged (ALKT, FICO, LIF, GOOGL, DUOL, AMD, GDDY,
VRNS, MSFT, PLTR, MT, CVE, ZS, SIMO, JNJ, PAY, CNQ, CF, ALAB, RCL, TSLA,
KLIC, MU, TER). **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.** None can reach BUY-CANDIDATE
until you review the card, edit anything you disagree with, set
`status: planned`, and screen the name compliant in Zoya/Musaffa.

Top 20 by max-benefit rank (full 50 in `leads.md`):

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| UTHR | LEAD | new | 10.9:1 | earnings 2026-07-29 | 9 |
| ALKT | LEAD | existing | 7.9:1 | earnings 2026-07-29 | 9 |
| FICO | LEAD | existing | 6.6:1 | earnings 2026-07-29 | 9 |
| P | LEAD | new | 13.7:1 | earnings 2026-08-26 | 37 |
| LIF | LEAD | existing | 7.3:1 | earnings 2026-08-10 | 21 |
| AVGO | LEAD | new | 7.1:1 | earnings 2026-09-03 | 45 |
| DELL | LEAD | new | 3.5:1 | earnings 2026-09-03 | 45 |
| GOOGL | LEAD | existing | 3.9:1 | earnings 2026-07-22 | 2 |
| DUOL | LEAD | existing | 3.8:1 | earnings 2026-08-05 | 16 |
| AMD | RESEARCH | existing | 2.1:1 | earnings 2026-08-04 | 15 |
| GDDY | LEAD | existing | 3.8:1 | earnings 2026-07-30 | 10 |
| VRNS | RESEARCH | existing | 2.6:1 | earnings 2026-07-28 | 8 |
| SFD | RESEARCH | new | 2.7:1 | earnings 2026-07-28 | 8 |
| MSFT | LEAD | existing | 3.8:1 | earnings 2026-07-29 | 9 |
| PLTR | LEAD | existing | 4.2:1 | earnings 2026-08-03 | 14 |
| MT | RESEARCH | existing | 1.4:1 | earnings 2026-07-30 | 10 |
| CVE | RESEARCH | existing | 1.5:1 | earnings 2026-07-30 | 10 |
| STX | RESEARCH | new | n/a | earnings 2026-07-28 | 8 |
| ZS | LEAD | existing | 4.3:1 | earnings 2026-09-02 | 44 |
| SIMO | RESEARCH | existing | n/a | earnings 2026-07-29 | 9 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **GOOGL / TSLA — earnings 2026-07-22, same day as NOW.** If either is
  under active consideration, get the Zoya/Musaffa business-activity screen
  done before that date, not after — same "ratio pre-check isn't the whole
  screen" caveat as BMNR above applies to any interest-bearing-cash-heavy
  mega-cap.
- **PLTR** — carried the government/defense business-activity question from
  prior runs; nothing new to add, still open.
- **MT** — carried an implausibly tight engineered entry/stop/target band
  flag from prior runs.
- **AVGO, MSFT, LLY, NVDA, AAPL (SPUS-holding sourced)** — "held by a
  halal-labeled ETF" is a starting point, not a substitute for your own
  screen; several of these carry real nuance (interest income, non-core
  segments) worth checking directly.

## Follow-ups (priority order)

1. **[New — top priority] BMNR Shariah re-screen.** The ratio pre-check
   flags a business-activity conflict ("Capital Markets") against the
   broker app's recorded `compliant`, and BMNR's actual quarter (ETH
   accumulation + staking for yield) makes this a substantive question, not
   a technicality. Confirm one way or the other in Zoya/Musaffa before this
   becomes a multi-run open item the way FIG's flag did.
2. **[Time-boxed] NOW earnings 2026-07-22** — 2 days out, after close; first
   quarter under the new AI licensing model, watched closely given the
   IBM-budget-warning-driven pullback earlier this month.
3. **[Housekeeping] 25 new DRAFT setup cards** added this run (50 total
   leads, 49 in `setups/` counting existing). None are `planned`, none can
   reach BUY-CANDIDATE. Review at your own pace.
4. **[Infrastructure — still open]** No ledger yet — start logging trades
   (including the 2026-07-13 FIG sale/BMNR buy, retroactively if useful) to
   `transactions.csv` via `/apply-trade` to unlock the discipline guard.
5. **[Concentration — informational]** NOW is now 81.4% of the tracked
   book. Concentration rules are muted below 4 names per `rules.md`, so
   nothing fires mechanically, but it's worth knowing plainly.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [BMNR Stock Climbs As Ethereum Treasury Bet Scales To $11.3B — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_14/)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
- [ServiceNow Set to Report Q2 Earnings: Buy, Sell or Hold the Stock? — Yahoo Finance / Zacks](https://finance.yahoo.com/markets/stocks/articles/servicenow-set-report-q2-earnings-151900170.html)
- [ServiceNow, Inc. — Form 10-Q FY2026 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000056/now-20260331.htm)
- [ServiceNow stock slides as IBM budget warning turns July earnings into a core-growth test — ts2.tech](https://ts2.tech/en/servicenow-stock-slides-as-ibm-budget-warning-turns-july-earnings-into-a-core-growth-test/)
- [ServiceNow's High-Wire Act: Margin Squeeze vs. AI Momentum in the Run-Up to Q2 — ad-hoc-news.de](https://www.ad-hoc-news.de/boerse/news/ueberblick/servicenow-s-high-wire-act-margin-squeeze-vs-ai-momentum-in-the-run-up/69683001)
