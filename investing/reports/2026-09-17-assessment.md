# Portfolio Assessment — 2026-09-17

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (14 new DRAFT setup cards auto-filled — APA, BLSH,
CORZ, DDOG, FSLR, HPE, NTAP, NTNX, NTR, ORCL-PD, PR, TECK, TS, XOM; 36
existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run — still no `transactions.csv` (discipline guard
stays dormant).

**Since the last report (2026-08-19):** no trades recorded in this repo
(holdings unchanged: BMNR 10 sh @ $15.43, NOW 7 sh @ $114.97). Both the
BMNR compliance question and the missing PM-grade fields flagged last run
are still open, one month later.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.42**, up
**+58.1%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — same open flag as last run, still unresolved.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -8.1:1 (DCF-derived target sits far below the stop; DCF doesn't fit this business — see caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $24.40 price -> -97.1% (not meaningful — see caveat) |
| Trailing stop (chandelier) | $21.4842 — price ~13.6% above it |
| 6m momentum (skip last month) | -14.6% |
| Portfolio note | ATR 7.49% -> vol-throttle: size down |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$138.52**, **+20.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.2:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale), ratio pre-check also clean this run (debt 1.7%, liquid 4.4%) |
| DCF intrinsic value | $120.12 vs. $138.50 price -> -13.3% (price moderately rich to the model) |
| Trailing stop (chandelier) | $130.2245 — price ~6.4% above it |
| 6m momentum (skip last month) | +5.1% (turned positive since last run's -5.3%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.42 | 10 | $15.43 | $243.95 | +58.1% | 20.1% |
| NOW | $138.52 | 7 | $114.97 | $969.64 | +20.5% | 79.9% |

**Total value: $1,213.59** | Cost: $959.09 | **Total return: ~+26.5%** (+$254.50 unrealised)

Both positions are up materially since last run (BMNR +33.1% -> +58.1%; NOW
+11.8% -> +20.5%), so the concentration split (79.9% NOW / 20.1% BMNR) is
essentially unchanged from last month — still a function of BMNR's 10-share
size, not a deliberate rebalance.

## Action flags (priority order)

1. **[Mandate — still open, now 1 month unresolved] BMNR's mechanical
   Shariah ratio pre-check still FAILS** (`industry 'Capital Markets' —
   core business fails screen`), against the recorded `compliant` status
   (screened 2026-07-07, unchanged since last report). BMNR's own Sept 2026
   disclosures reinforce the concern: as of Sept 13 it reported **$15.8B**
   in total crypto/cash/"moonshot" holdings (5.96M ETH, ~4.9% of total ETH
   supply, plus stakes in Beast Industries and Eightco Holdings) — a
   scale and structure that looks more like a financial-asset treasury
   vehicle than an operating company, which is exactly the profile a
   business-activity screen is built to catch. Per this repo's Gate 1
   ("Shariah knockout -> AVOID/SELL, absolute"), a confirmed fail would be
   a hard SELL independent of the +58.1% return. `recommend.py`'s "would
   buy today" check still only reads the recorded field and stays silent
   on this. **Re-screen in Zoya/Musaffa on the business-activity question
   specifically — this has now gone unresolved for a full reporting
   cycle.**
2. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH
   holds. Do not add. Note the stock re-rated up ~7.4% on Sept 14 after Q2
   FY2026 results (EPS $0.90 vs. $0.86 consensus, revenue +24% YoY) and
   several analyst price-target raises (Needham to $155 from $115, BTIG to
   $170 from $150), so the rich multiple now sits on top of confirmed
   beat-and-raise fundamentals, not just narrative.
3. **[DCF caveat / BMNR]** The -97.1% DCF "downside" remains not a
   meaningful signal — the cash-flow model doesn't fit a crypto-treasury
   business whose value tracks ETH holdings and staking yield, not
   discounted operating cash flow. Treat as a data gap, not a valuation call.
4. **[Catalyst / NOW — horizon changed]** Next earnings are now confirmed
   for **2026-10-28** (~41 days out) — inside the 60-day catalyst-horizon
   default for the first time since BMNR's position opened. AI governance
   tooling launches and continued subscription-growth acceleration
   commentary are the narrative drivers into that print.
5. **[Discovery] 50 leads this run, 28 clear to LEAD tier** (up from 9 last
   run) — the rest capped at RESEARCH by the asymmetry/catalyst gates.
   **PLTR** carries over again with its still-unresolved government/defense
   business-activity question from prior runs — nothing new to add, still
   open. **CDE, AGI, IAG, EGO** — the recurring precious-metals/mining
   cluster is back at LEAD tier again; same open royalty-financing
   structure question as before.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressively building its ETH
treasury — 5.96M ETH (~4.9% of global supply) plus $549M cash and
marketable securities, per its Sept 14, 2026 disclosure, with projected
annualized ETH staking rewards of $392M at full scale. Stock up +58.1%
since the $15.43 cost basis.
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16/)

**Case to flag (compliance, independent of the price story):** Same
mechanical ratio-precheck disagreement as last run, now a month stale.
Recent reporting also shows the operating business running a net loss
(~$46.5M revenue vs. ~$83.6M net loss last quarter per stockanalysis.com),
with the investment case resting almost entirely on the treasury/staking
model — reinforcing rather than resolving the business-activity question.
The holding file is still missing `thesis_one_liner`, `variant_view`,
`initial_stop`, `target_price`, and `pre_mortem`.

**Verdict: HOLD (no technical rule fired) — the compliance question is
still the thing to resolve first, not the price action, and it has now sat
open for a full month.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 beat (EPS $0.90 vs. $0.86 consensus, revenue
+24% YoY) drove a +7.4% single-day rally on Sept 14; Needham and BTIG both
raised price targets ($155 and $170 respectively); new AI governance tools
launched, extending the AI-agent platform narrative. DCF gap is a modest
-13.3%, not extreme.
[ad-hoc-news (price targets)](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-after-analysts-lift-price-targets/70099918) ·
[ad-hoc-news (7.4% jump)](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-heads-into-the-open-after-a-7-4-percent-jump/70108715)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum turned
positive (+5.1%, vs. -5.3% last run) but the multiple is now pricing in a
confirmed beat, raising the bar for the next one. Next earnings **2026-10-28**
is now inside the 60-day catalyst window — the nearest binary event either
holding has had in several reports.
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: still only reads the
  *recorded* `shariah.status` field (`compliant`), so it stays silent
  despite the ratio-precheck fail persisting a second run. Nothing in the
  pipeline will re-flag this on its own until the recorded status is
  updated — the follow-up is still on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); both prices sit above their chandelier stops regardless.
- **VOL_THROTTLE -> BMNR**: portfolio note fired this run — ATR 7.49% is
  above the 6% threshold; size down if adding.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.40 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $138.50 | -13.3% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** (expected — no card has been reviewed and
flipped to `status: planned`; all 77 cards in `setups/` are still `draft`).
All new-idea surfacing comes from machine discovery below instead.

## Draft & planned setups — 50 leads, 14 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one (14 new: APA, BLSH,
CORZ, DDOG, FSLR, HPE, NTAP, NTNX, NTR, ORCL-PD, PR, TECK, TS, XOM; 36
existing cards left unchanged). **Every DRAFT card is unreviewed and
Shariah UNVERIFIED — proposals to review and edit, never buys.**

28 of the 50 leads clear to LEAD tier this run (up sharply from 9 last
run), the rest capped at RESEARCH by the asymmetry or catalyst-horizon gate:

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| AA | LEAD | existing | 20.0:1 | earnings 2026-10-15 | 28 |
| FSLR | LEAD | new | 20.0:1 | earnings 2026-10-29 | 42 |
| TTMI | LEAD | existing | 19.1:1 | earnings 2026-11-04 | 48 |
| VICR | LEAD | existing | 14.6:1 | earnings 2026-10-20 | 33 |
| IONQ | LEAD | existing | 14.0:1 | earnings 2026-11-04 | 48 |
| FORM | LEAD | existing | 12.5:1 | earnings 2026-10-28 | 41 |
| IAG | LEAD | existing | 8.9:1 | earnings 2026-11-03 | 47 |
| GDDY | LEAD | existing | 9.7:1 | earnings 2026-10-29 | 42 |
| FOX | LEAD | existing | 9.8:1 | earnings 2026-10-29 | 42 |
| PAY | LEAD | existing | 9.5:1 | earnings 2026-11-02 | 46 |

(Full 28-name LEAD list and all 50 rows in `leads.md`; not reproduced in
full here to keep this report readable.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, IAG, AGI, EGO** — the recurring precious-metals/mining cluster,
  all at LEAD tier again this run; mining-royalty financing structures
  raised the same open question in earlier runs. Still worth a real screen
  before spending review time on any of these cards.
- **BLSH, CORZ** — no setup card yet despite clearing to LEAD; still need
  a ~10-min card written before they can move past RESEARCH.
- **22 RESEARCH-tier leads** — full list in `leads.md`, not reproduced here.

## Follow-ups (priority order)

1. **[Urgent — now 1 month open] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has disagreed with the recorded "compliant" status for
   a full reporting cycle now. This is the largest compliance question in
   the book (20.1% weight, +58.1% return) and the pipeline will not
   re-surface it on its own — see the COMPLIANCE_GATE note above.
2. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, unchanged from
   last run.
3. **[Time-boxed — now inside horizon] NOW earnings 2026-10-28** — 41 days
   out and now inside the 60-day catalyst window; the first near-term
   binary event flagged for this book in several reports.
4. **[Housekeeping] 14 new DRAFT setup cards** added this run (77 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades
   to `transactions.csv` (or via `/apply-trade`) to unlock the discipline
   guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [BMNR Stock Slides As BitMine Immersion Momentum Stalls — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16/)
- [Bitmine Immersion Technologies (BMNR) Stock Price & Overview — stockanalysis.com](https://stockanalysis.com/stocks/bmnr/)
- [ServiceNow stock gains after analysts lift price targets — ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-after-analysts-lift-price-targets/70099918)
- [ServiceNow stock heads into the open after a 7.4 percent jump — ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-heads-into-the-open-after-a-7-4-percent-jump/70108715)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
