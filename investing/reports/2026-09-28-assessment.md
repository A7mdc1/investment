# Portfolio Assessment — 2026-09-28

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (17 new DRAFT setup cards auto-filled — BLSH, HBM,
CORZ, NTNX, FN, APA, FRO, AMKR, XOM, TS, DDOG, HPE, LLY, SMTC, DDS, NTAP, BBY
— 33 existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run — still no `transactions.csv` (discipline guard
stays dormant).

**Since the last report (2026-08-19, 40 days ago):** no trades recorded in
the repo — still just BMNR and NOW. That gap itself is worth naming: this is
the longest stretch between assessment runs so far.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.60**, up
**+78.9%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — this is now the third run in a row (2026-08-19, and now
2026-09-28) with this flag open and unresolved.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.6:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $27.61 price -> -97.4% (not meaningful — see DCF caveat) |
| Trailing stop (chandelier) | $23.5249 — price ~17.4% above it |
| 6m momentum (skip last month) | +39.4% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 >= pe_rich 50).
Live price **$131.69**, **+14.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | **REVIEW — recorded compliant but screen is >100 days old (screened 2026-06-09) — re-screen** |
| DCF intrinsic value | $120.12 vs. $131.69 price -> -8.9% |
| Trailing stop (chandelier) | $129.7891 — price is only ~1.5% above it (tightest cushion either holding has had) |
| 6m momentum (skip last month) | +39.3% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4
  names. `verdict.py` flags BMNR's daily ATR (6.44%) above the 6%
  vol-throttle threshold — size down per the throttle note if adding.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.60 | 10 | $15.43 | $276.05 | +78.9% | 23.0% |
| NOW | $131.69 | 7 | $114.97 | $921.83 | +14.5% | 77.0% |

**Total value: $1,197.88** | Cost: $959.09 | **Total return: ~+24.9%**
(+$238.79 unrealised)

NOW's weight eased slightly from 81.4% (2026-08-19) to 77.0% purely from
BMNR outrunning it (+78.9% vs. +14.5% since cost), not a rebalancing
decision recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — still open, 3rd consecutive run] BMNR's mechanical Shariah
   ratio pre-check FAILS again**, flagging `industry 'Capital Markets'
   matches 'capital markets' — core business fails screen`. Musaffa's public
   BMNR page still shows a "Halal & Shariah Compliant" verdict, but its own
   business description dates to **Q3 2025** ("blockchain technology
   company which engages in industrial scale digital asset mining,
   equipment sales, and hosting operations") — that describes BMNR's *old*
   mining-hardware business, not the ETH-treasury company it has become.
   Current reporting (Sept 27-28, 2026) has BMNR holding **6.0M ETH
   (~$16.2B) and $17.2B total crypto/cash/marketable securities**, with
   ~5.07M ETH staked for a projected **$424M/yr in staking reward income**
   — a yield-generating financial-asset treasury, which is exactly the
   profile the mechanical ratio pre-check is catching. The recorded
   "compliant" status and the public Musaffa screen both look like they may
   be screening the pre-pivot business, not the current one.
   `recommend.py`'s "would buy today" check only reads the recorded field
   and stays silent on this. Per this repo's own Gate 1 ("Shariah
   knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail would be a hard SELL independent of the
   +78.9% return. **This has now sat open for at least 40 days across two
   reports — worth resolving with a fresh Zoya/Musaffa screen specifically
   on the business-activity question before this compounds further.**
2. **[Mandate — new this run] NOW's Shariah screen is stale** (screened
   2026-06-09, >100 days old per `shariah.py`). The mechanical ratio
   pre-check itself is clean (debt ratio 1.8%, liquid-asset ratio 4.6%,
   business_ok), so this is a housekeeping re-screen, not a live compliance
   concern — but it is the largest position in the book (77.0% weight) to
   be running on a stale screen.
3. **[Valuation / NOW]** P/E ~119.02 (recorded) — rich; VALUATION_RICH
   holds. Do not add.
4. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business whose
   value is driven by ETH holdings and staking yield, not discounted
   operating cash flow. Treat this as a data-gap, not a valuation call.
5. **[Discovery] 50 leads this run, 24 clear to LEAD tier** (up sharply from
   9 last run — earnings season has pulled many catalysts inside the
   60-day horizon). One new lead, **BLSH (Bullish)**, is worth flagging
   before any review time is spent on it: it operates a regulated digital-
   asset **exchange** with a derivatives order book and market-making
   business — the same "financial exchange / capital markets" business-
   activity profile that is currently failing BMNR's pre-check, likely
   worse given the derivatives/market-making layer. Screen with that in
   mind, not just the ratio math.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continuing to build ETH treasury
aggressively — holdings crossed 6.0M ETH (~4.9-5% of global supply per
recent coverage) as of Sept 27-28, with total crypto/cash/marketable
securities at $17.2B, up from $11.4-11.6B at the last report. ~5.07M ETH is
now staked, projecting ~$424M/yr in annualized staking income at current
yield. Stock up +78.9% since the $15.43 cost basis; recorded compliance
status is "compliant." 6-month momentum (+39.4%) is now strongly positive,
a reversal from the -13.1% reading last report.
[PR Newswire — 6M ETH milestone](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-over-6-million-tokens-with-total-crypto-cash--marketable-securities-holdings-of-17-2-billion-302891056.html) ·
[GuruFocus](https://www.gurufocus.com/news/9099966/bitmine-immersion-technologies-bmnr-boosts-ethereum-treasury-to-6-million-tokens-amid-mixed-market-reaction) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16-2/)

**Case to flag (compliance, independent of the price story):** Now a
3rd-consecutive-run mechanical ratio-precheck fail (see Action Flag #1),
with fresh evidence this run that the public Musaffa "compliant" screen
itself may be stale (dated to BMNR's pre-pivot mining-hardware business
description). The holding file is still missing `thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, and `pre_mortem` — seven
weeks after the position was opened, there is still no PM-grade record to
weigh the compliance question against beyond the mechanical LOW-conviction
default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
now the oldest open item in this book and should be resolved before the
gain grows further.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 results (reported since last run) beat
consensus — revenue +24.0% YoY to $3.99B, EPS $0.90 (+$0.04 vs. consensus),
subscription revenue +24.5% YoY. AI ACV has crossed $1B with agentic
deployments up 9x in nine months. Needham raised its price target to $155
(Sept 11); Bernstein reiterated Outperform at $248, framing a path to
$30-32B ACV by 2030 with ~30% AI-related. Buy consensus across 32 analysts
as of Sept 21. DCF shows only a modest ~8.9% premium to intrinsic value —
not an extreme gap.
[ServiceNow Q2 FY2026 8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm) ·
[ServiceNow Q2 2026 press release](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx) ·
[Needham target raise](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-as-ai-focused-analyst-upgrades-and-strong-q2/70106778)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; price now sits only
~1.5% above the chandelier trailing stop ($129.79) — the tightest cushion
this position has shown; the Shariah screen is stale (>100 days); next
earnings not yet dated in the leads pool (last known target ~2026-10-28,
unconfirmed — verify before treating as a near-term catalyst).

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite three straight runs of a ratio-precheck fail. Nothing in
  the automated pipeline will re-flag this on its own until you update the
  recorded status — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); both prices sit above their chandelier levels, though
  NOW's cushion (1.5%) is now thin enough to watch closely.
- **VOL_THROTTLE -> BMNR**: fires — daily ATR 6.44% above the 6% threshold;
  size down if adding to this name.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $27.61 | -97.4% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $131.80 | -8.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 82 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 17 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one
(17 new cards: BLSH, HBM, CORZ, NTNX, FN, APA, FRO, AMKR, XOM, TS, DDOG,
HPE, LLY, SMTC, DDS, NTAP, BBY; 33 existing cards left unchanged). **Every
DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to review and
edit, never buys.**

24 of the 50 leads clear to LEAD tier this run (up sharply from 9 last
run — a wider swath of earnings catalysts now sit inside the 60-day
horizon), sorted by catalyst date:

| Ticker | Verdict | Has card | R:R | Catalyst |
|---|---|---|---|---|
| TSLA | LEAD | existing | 10.5:1 | earnings 2026-10-21 |
| LRCX | LEAD | existing | 4.1:1 | earnings 2026-10-21 |
| CORZ | LEAD | new | 18.9:1 | earnings 2026-10-23 |
| CLS | LEAD | existing | 4.3:1 | earnings 2026-10-26 |
| AMKR | LEAD | new | 4.8:1 | earnings 2026-10-26 |
| GOOGL | LEAD | existing | 16.3:1 | earnings 2026-10-28 |
| DINO | LEAD | existing | 5.2:1 | earnings 2026-10-28 |
| HBM | LEAD | new | 8.2:1 | earnings 2026-10-29 |
| CVE | LEAD | existing | 5.6:1 | earnings 2026-10-29 |
| XOM | LEAD | new | 3.2:1 | earnings 2026-10-30 |
| FN | LEAD | new | 20.0:1 | earnings 2026-11-02 |
| ALAB | LEAD | existing | 4.5:1 | earnings 2026-11-03 |
| SMCI | LEAD | existing | 3.4:1 | earnings 2026-11-03 |
| MKSI | LEAD | existing | 17.0:1 | earnings 2026-11-04 |
| TTMI | LEAD | existing | 8.6:1 | earnings 2026-11-04 |
| APA | LEAD | new | 5.8:1 | earnings 2026-11-04 |
| IONQ | LEAD | existing | 4.5:1 | earnings 2026-11-04 |
| DOCN | LEAD | existing | 4.5:1 | earnings 2026-11-04 |
| TS | LEAD | new | 3.8:1 | earnings 2026-11-04 |
| WDC | LEAD | existing | 10.5:1 | earnings 2026-11-05 |
| ASTS | LEAD | existing | 7.4:1 | earnings 2026-11-09 |
| BLSH | LEAD | new | 9.4:1 | earnings 2026-11-12 |
| KLIC | LEAD | existing | 3.9:1 | earnings 2026-11-18 |
| NTNX | LEAD | new | 6.9:1 | earnings 2026-11-25 |

All 50 cleared the liquidity floor and a clean ratio pre-check (where
computed) — not a business-activity screen. Shariah status on every card is
`unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **BLSH** — see Action Flag #5. Regulated crypto derivatives exchange +
  market-making business; likely a harder business-activity question than
  BMNR's, not just a ratio one.
- **PLTR** — dropped out of LEAD tier this run (RESEARCH, reward:risk
  1.3:1) but still carries its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **HBM (Hudbay Minerals)** — mining sector; prior runs flagged a recurring
  precious-metals/mining cluster (CDE, AR, AGI, IAG, KGC, EGO — several
  still present in this run's RESEARCH tier) over royalty/streaming
  financing structures common to the sector. Worth the same scrutiny before
  spending review time on the card.
- **Energy cluster** — CVE, XOM, APA, DINO all cleared to LEAD this run on
  the `undervalued_large_caps` screen; four correlated oil & gas names is
  one sector bet, not four, if more than one gets promoted past RESEARCH.
- **26 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — open 3 runs now] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has disagreed with the recorded "compliant" status for
   at least 40 days across two prior reports, and this run's research
   suggests the public Musaffa screen itself may be stale (dated to the
   pre-pivot business). This is the largest compliance question in the
   book (23.0% weight, +78.9% return) and the automated pipeline will NOT
   re-surface it on its own.
2. **[New] NOW Shariah re-screen** — recorded screen is >100 days old on
   the book's largest position (77.0% weight); ratio pre-check itself is
   clean, so this is routine but overdue.
3. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` all still null/empty, 7+ weeks after the position was
   opened.
4. **[Watch] NOW's price is only ~1.5% above its trailing stop** — the
   tightest cushion recorded for this position; no action required under
   current rules (`trade_type: core` exempts it from TRAIL_STOP), but worth
   tracking given the compressed distance.
5. **[Housekeeping] 17 new DRAFT setup cards** added this run (82 total in
   `setups/`); none are `planned`. Review at your own pace — BLSH and the
   energy cluster deserve the compliance/concentration scrutiny above
   before any card work.
6. **[Infrastructure — still open]** No ledger yet — start logging trades
   to `transactions.csv` (or via `/apply-trade`) to unlock the discipline
   guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach over 6 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-over-6-million-tokens-with-total-crypto-cash--marketable-securities-holdings-of-17-2-billion-302891056.html)
- [BitMine Immersion Technologies (BMNR) Boosts Ethereum Treasury to 6 Million Tokens — GuruFocus](https://www.gurufocus.com/news/9099966/bitmine-immersion-technologies-bmnr-boosts-ethereum-treasury-to-6-million-tokens-amid-mixed-market-reaction)
- [BMNR Stock Pulls Back As Traders Weigh Deep Losses And Cash Cushion — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16-2/)
- [Is Bitmine Immersion Technologies Inc - BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [ServiceNow, Inc. - Form 8-K - Q2 FY2026 — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow stock gains as AI-focused analyst upgrades and strong Q2 figures support recovery — ad-hoc-news.de](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-as-ai-focused-analyst-upgrades-and-strong-q2/70106778)
- [Bullish (BLSH) Company Profile & Description — StockAnalysis](https://stockanalysis.com/stocks/blsh/company/)
