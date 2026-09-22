# Portfolio Assessment — 2026-09-22

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 by max-benefit kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (16 new DRAFT setup cards
auto-filled; 34 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run separately — still no `transactions.csv`
(discipline guard stays dormant). No trades recorded since the last report
(2026-08-19); still just BMNR + NOW.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$28.49**, up
**+84.6%** vs. the $15.43 cost basis (was +33.1% at the last report five
weeks ago). **Action Flag #1 below is unchanged and still open — the
mechanical Shariah business-activity pre-check still disagrees with the
recorded "compliant" status, on a position that has grown from 18.6% to
23.0% of the book.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.0:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (same flag as 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $28.49 price -> -97.5% (see DCF caveat: model doesn't fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.9355 — price ~24.2% above it |
| 6m momentum (skip last month) | +7.3% |
| Would buy today? | Mechanically yes per recommend.py's gates — it only reads the *recorded* Shariah field, still blind to the ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$136.10**, **+18.4%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah (recorded) | **REVIEW — screen is now >100 days old** (screened 2026-06-09), broker app still shows compliant |
| DCF intrinsic value | $120.12 vs. $136.10 price -> -11.7% (price moderately rich to the model) |
| Trailing stop (chandelier) | $130.6155 — price is ~4.0% above it (tightest gap between price and stop since tracking began) |
| 6m momentum (skip last month) | +15.8% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, the Shariah screen going stale (now true) or flipping, or price closing below the trailing stop |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- Vol throttle: BMNR ATR 6.54% — size down per `vol_throttle_atr_pct`.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $28.49 | 10 | $15.43 | $284.90 | +84.6% | 23.0% |
| NOW | $136.04 | 7 | $114.97 | $952.28 | +18.3% | 77.0% |

**Total value: $1,237.18** | Cost: $959.09 | **Total return: ~+29.0%** (+$278.09 unrealised)

Both positions are up sharply since the last report — BMNR has more than
doubled its gain (+33.1% -> +84.6%) and NOW has extended (+11.8% -> +18.3%).
Weighting has drifted slightly further toward BMNR (18.6% -> 23.0%) purely
from price action, not a sizing decision recorded anywhere.

## Action flags (priority order)

1. **[Mandate — still open, 2nd run in a row] BMNR's mechanical Shariah
   ratio pre-check still FAILS**, same flag as 2026-08-19: `industry
   'Capital Markets' matches 'capital markets' — core business fails
   screen`. This still conflicts with the recorded `compliant` status
   (broker app, screened 2026-07-07, now 77 days old). Fresh reporting this
   run reinforces rather than resolves the question: as of 2026-09-21,
   BitMine's combined crypto/cash/marketable-securities holdings reached
   **$17.1B**, anchored by **5.98M ETH (4.9% of total supply)**, with
   **5.07M ETH staked** generating a projected **$357M in annualized
   staking revenue**. That is a yield-bearing financial-asset treasury at
   even greater scale than the $11.4B/98%-of-revenue picture described last
   run — the profile a business-activity screen is built to catch has only
   gotten more pronounced, not less. Per this repo's own Gate 1 ("Shariah
   knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail would be a hard SELL, independent of the
   now +84.6% return. **`recommend.py`'s "would buy today" check still only
   reads the recorded field and is silent on this.** This is now the
   longest-open compliance question in the book (2 consecutive runs,
   5+ weeks) — re-screen the business-activity question specifically in
   Zoya/Musaffa before treating "compliant" as settled or adding to the
   position. [PR Newswire, 2026-09-21](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884432.html)
2. **[New this run] NOW's recorded Shariah screen just went stale** —
   screened 2026-06-09, now >100 days old (`shariah_status: REVIEW` per
   recommend.py). Not a compliance fail, just a due-for-refresh flag; screen
   again in Zoya/Musaffa to keep the "compliant" record current.
3. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH
   holds. Do not add.
4. **[DCF caveat / BMNR]** The -97.5% DCF "downside" is still not a
   meaningful signal — `dcf.py`'s cash-flow model (5% growth, 10% discount,
   no BMNR-specific override) doesn't fit a crypto-treasury business whose
   value tracks ETH holdings and staking yield, not discounted operating
   cash flow. Treat as a data gap, not a valuation call.
5. **[Catalyst / NOW]** Next earnings land **2026-10-28** (36 days out —
   inside the 60-day catalyst horizon now, unlike last run). No news since
   the last report beyond routine coverage; nothing thesis-breaking found.
6. **[Discovery] 50 leads this run, 27 clearing to LEAD tier** (up from 9
   last run — same `discover_top_n: 50`, but a broader mix cleared the
   asymmetry/catalyst gates this time). **PLTR** carries over again with its
   unresolved government/defense business-activity question from prior
   runs — still open, nothing new. The precious-metals/mining cluster
   (**CDE, AGI, IAG** clear to LEAD this run; EGO stays RESEARCH) still
   carries the same recurring royalty-financing compliance question flagged
   in earlier runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressively growing its core
Ethereum position — 5.98M ETH (4.9% of global supply) and $17.1B in total
crypto/cash/marketable-securities holdings as of 2026-09-21, the world's
largest ETH treasury and second-largest crypto treasury overall behind
Strategy Inc.'s BTC book. Staked ETH (5.07M tokens) is projected to generate
$357M in annualized staking revenue. Chairman Tom Lee is keynoting Korea
Blockchain Week on 2026-09-30, reiterating the push toward 5% of total ETH
supply. Stock up +84.6% since the $15.43 cost basis; recorded compliance
status is still "compliant."
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884432.html) ·
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check has now disagreed with the recorded status for
**two runs in a row** — see Action Flag #1. The scale of the treasury and
staking-yield business has only grown since the flag first appeared. The
holding file is also still missing `thesis_one_liner`, `variant_view`,
`initial_stop`, `target_price`, and `pre_mortem` — nine weeks after the
position was opened, there is still no PM-grade record to weigh the
compliance question against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — the compliance question is
still the thing to resolve first, not the price action, and it is now more
urgent given the larger unrealized gain and larger portfolio weight.**

### NOW — ServiceNow, Inc
**Case to keep:** Up +18.3% since cost basis and +15.8% on 6m momentum;
price sits only ~4.0% above its trailing stop, the tightest cushion since
tracking began, but the trend itself is intact. DCF shows an ~11.7% premium
to intrinsic value — richer than last run's ~6.6% gap but not extreme.
Earnings confirmed for 2026-10-28, now inside the 60-day catalyst horizon.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the recorded
Shariah screen just crossed the staleness threshold (>100 days since
2026-06-09) — a housekeeping item, not a red flag, but due for a refresh
before the position grows further. No thesis-breaking news found this run.
[TipRanks — earnings](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (still `compliant`), so it stays silent
  for a second run despite the ratio-precheck fail. Nothing in the automated
  pipeline will re-flag this on its own until the recorded status is
  updated — the follow-up is still on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); NOW's price is closest it has been to its chandelier stop
  (~4.0% above) — worth watching, not yet triggered.
- **VOL_THROTTLE -> BMNR**: fired — ATR 6.54% above the 6% threshold; size
  down per policy if adding.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $28.49 | -97.5% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $136.10 | -11.7% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** this run (expected — no card has been reviewed and flipped
to `status: planned` yet; all 81 cards in `setups/` are still `draft`).

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (16
new cards: APA, NTNX, ONON, FRO, BLSH, TS, CORZ, TECK, DDOG, AMKR, HPE, XOM,
and others; 34 existing cards left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

27 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run —
same `discover_top_n: 50`, a broader set cleared the asymmetry/catalyst
gates):

| Ticker | R:R | Score | Has card | Catalyst |
|---|---|---|---|---|
| MKSI | 20.0:1 | 26.0 | existing | earnings 2026-11-04 |
| AGI | 20.0:1 | 38.3 | existing | earnings 2026-10-28 |
| PAAS | 19.1:1 | 35.2 | new | earnings 2026-11-16 |
| UTHR | 18.0:1 | 24.9 | existing | earnings 2026-10-28 |
| FSLR | 16.7:1 | 27.2 | new | earnings 2026-10-29 |
| CDE | 11.4:1 | 39.1 | existing | earnings 2026-10-28 |
| IONQ | 10.8:1 | 33.9 | existing | earnings 2026-11-04 |
| XOM | 7.7:1 | 32.6 | new | earnings 2026-10-30 |
| HBM | 7.1:1 | 45.9 | new | earnings 2026-10-29 |
| WDC | 7.1:1 | 32.4 | existing | earnings 2026-11-05 |

(Top 10 by reward:risk shown; the remaining 17 LEAD-tier names — GOOGL,
MSFT, GDDY, LRCX, APA, ASTS, CNQ, ONON, SMCI, TSLA, BLSH, CVE, TTMI, TS,
CORZ, AMKR, IAG — plus all 23 RESEARCH-tier names are in `leads.md`, not
reproduced here to keep this report readable.)

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add; still
  RESEARCH tier this run (reward:risk 1.4:1, below the swing floor).
- **CDE, AGI, IAG** (LEAD) and **EGO** (RESEARCH) — the recurring
  precious-metals/mining cluster; the royalty-financing-structure question
  raised in earlier runs is still open. Worth a real screen before spending
  review time on any of these cards.

## Follow-ups (priority order)

1. **[Urgent — 2nd run in a row] BMNR Shariah re-screen**: the mechanical
   ratio pre-check still disagrees with the recorded "compliant" status on
   the business-activity question. This is the largest and now
   longest-open compliance question in the book (23.0% weight, +84.6%
   return, 5+ weeks open) and the automated pipeline will NOT re-surface it
   on its own — see the COMPLIANCE_GATE note above.
2. **[New — housekeeping] NOW Shariah screen is stale** (>100 days since
   2026-06-09) — re-screen in Zoya/Musaffa to keep the record current.
3. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, nine weeks after
   the position was opened.
4. **[Time-boxed] NOW earnings 2026-10-28** — 36 days out, now inside the
   60-day catalyst horizon; track the AI ACV / Armis integration narrative
   into the print.
5. **[Housekeeping] 16 new DRAFT setup cards** added this run (81 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.
   No trades have occurred since the last report, so nothing is backlogged.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.98 Million Tokens, and Total Crypto and Total Cash Holdings of $17.1 Billion — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884432.html)
- [BitMine Highlights Record Ethereum Treasury and Staking Growth — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2)
- [ServiceNow (NOW) Earnings Dates — TipRanks](https://www.tipranks.com/stocks/now/earnings)
