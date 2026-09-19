# Portfolio Assessment — 2026-09-19

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (13 new DRAFT setup cards auto-filled; 63 existing
cards left unchanged, 76 ticker cards total in `setups/`) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` not run separately — still no
`transactions.csv` (discipline guard stays dormant, no trades logged since
the last report).

**Since the last report (2026-08-19):** no trades recorded. Holdings are
unchanged (BMNR, NOW). One month has elapsed with no `/apply-trade` entries.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.99**, up
**+68.4%** vs. the $15.43 cost basis. **The mechanical Shariah business-activity
pre-check still disagrees with the recorded "compliant" status — this is the
third consecutive run carrying this open flag.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.3:1 (DCF-derived target sits below the stop) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from last run) |
| DCF intrinsic value | $0.72 vs. $25.99 price -> -97.2% (see DCF caveat below — model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $21.2401 — price ~22.4% above it |
| 6m momentum (skip last month) | -4.3% |
| Vol throttle | **NEW this run** — ATR 7.35% > `vol_throttle_atr_pct` (6%): portfolio note says size down |
| Would buy today? | Mechanically yes per recommend.py's gates — reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$135.47**, **+17.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah (recorded) | **REVIEW — NEW this run.** Recorded compliant (screened 2026-06-09) but the screen is now >100 days old — `shariah.py` flags it stale for the first time |
| DCF intrinsic value | $120.12 vs. $135.47 price -> -11.3% (rich to the model; wider gap than last run's -6.6% as price ran ahead of the DCF's unchanged assumptions) |
| Trailing stop (chandelier) | $130.1246 — price is ~4.1% above it (tighter buffer than last run's ~17.9%) |
| 6m momentum (skip last month) | +12.3% (reversed from -5.3% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, the Shariah screen going stale (now true) or flipping, or a close below the trailing stop |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.99 | 10 | $15.43 | $259.90 | +68.4% | 21.5% |
| NOW | $135.47 | 7 | $114.97 | $948.29 | +17.8% | 78.5% |

**Total value: $1,208.19** | Cost: $959.09 | **Total return: ~+26.0%** (+$249.10 unrealised)

Both positions gained since the last report; BMNR's weight edged up (18.6% ->
21.5%, now just under the 22% `max_position_pct` cap) purely from price
appreciation, not a sizing decision recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — recurring, 3rd run] BMNR's mechanical Shariah ratio pre-check
   still FAILS**, same flag as 2026-08-19 and 2026-07-13:
   `industry 'Capital Markets' matches 'capital markets' — core business fails
   screen`. Independent web research this run found a directly relevant data
   point not surfaced before: **Musaffa's own screener page for BMNR states
   it is Halal & Shariah compliant per its AAOIFI-based methodology, as of a
   Q3 2025 report** ([musaffa.com/stock/BMNR](https://musaffa.com/stock/BMNR/)).
   That is real evidence the recorded "compliant" status has independent
   third-party support, not just a broker-app label — but it is also dated
   (Q3 2025), predates BMNR's Ethereum-treasury pivot scaling up through
   2026, and is not the same as a fresh re-screen. Separately, analysts are
   now publicly debating BMNR's investment case on valuation grounds — NAV
   premium/discount to its ETH holdings, dilution from capital raises, and
   structural risk if ETH falls — which is a business-model question
   (yield/appreciation off a large financial-asset treasury) adjacent to,
   but distinct from, the Shariah business-activity question
   ([Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/09/17/bitmine-immersion-technologies-nasdaq-bmnr-approaches-5-of-all-ethereum-in-circulation-as-analysts-question-investment-case/)).
   **Net: this is still an open question, not resolved either direction.**
   Per Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL regardless
   of the +68.4% return; a confirmed pass (fresh Musaffa/Zoya re-screen)
   would close this out. `recommend.py`'s "would buy today" check still only
   reads the recorded field and stays silent on the ratio-precheck fail.
2. **[Mandate — NEW this run] NOW's recorded Shariah screen is now stale**
   (screened 2026-06-09, >100 days old) — `shariah.py` flipped its status
   from PASS to REVIEW this run. This is the larger position (78.5% of the
   book) and has never been re-screened since June. COMPLIANCE_SCREEN
   (rules.md Stage 1) calls for REVIEW before any add until re-screened.
3. **[NEW this run] BMNR vol-throttle note fired** — ATR 7.35% exceeds the
   6% `vol_throttle_atr_pct` threshold; `verdict.py`'s portfolio note flags
   sizing down. Not a SELL/TRIM trigger by itself, but a real signal this
   position's volatility has picked up since last run (no such note fired
   2026-08-19).
4. **[Housekeeping — recurring] BMNR review overdue in substance.** No
   `last_review` has ever been recorded (front-matter field still empty),
   74 days after the position was opened (2026-07-07). `thesis_one_liner`,
   `variant_view`, `initial_stop`, `target_price`, `pre_mortem` remain
   unfilled — unchanged from the 2026-08-19 flag.
5. **[Housekeeping — NEW this run] NOW's `review_cadence_days` (90) has been
   exceeded.** `last_review: 2026-06-15` -> 96 days ago as of this report.
   rules.md's discipline guard calls for re-underwriting at least this often
   "even with no trigger."
6. **[DCF caveat / BMNR]** The -97.2% DCF "downside" is not a meaningful
   signal — the model's 5% growth / 10% discount cash-flow framework does
   not fit a crypto-treasury business valued on ETH holdings and staking
   yield. Independent sources this run show the same divergence (a
   Simply Wall St DCF near $0.01) alongside NAV-based estimates in the
   $38-46/share range — a completely different valuation lens. Treat the
   formula output as a data gap, not a valuation call.
7. **[Catalyst / NOW — changed this run]** Next earnings now falls **inside**
   the 60-day catalyst horizon for the first time in several runs: sources
   point to an earnings call around **2026-10-28** (39 days out) with the
   formal Q3 report expected **~2026-11-04** (46 days out) — treat the exact
   date as unconfirmed until ServiceNow IR posts it.
   [Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings) ·
   [AlphaQuery](https://www.alphaquery.com/stock/NOW/earnings-history)
8. **[Discovery] 50 leads this run, 32 clearing to LEAD tier** (up from 9
   last run) — 13 new DRAFT cards scaffolded. **PLTR** carries over again
   with its unresolved government/defense business-activity question.
   **CDE, AGI, IAG, EGO, TECK** — the recurring precious-metals/mining
   cluster (TECK — coal/base-metals miner — is new to the pool this run,
   joining the same open financing-structure question raised on the others
   in prior runs).

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH holdings reached ~5.96M tokens
(~$15.4-15.8B), approaching BitMine's own public target of >5% of all
circulating ETH; ~5.07M ETH now staked via its MAVAN platform, with
annualized staking revenue now projected around $334-392M (up from the
~$287M cited last run). MAVAN has also expanded to serve outside
institutional clients, a second potential revenue line beyond the treasury
itself.
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-announces-record-ethereum-holdings-and-investment) ·
[The Block](https://www.theblock.co/treasuries/bmnr) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)

**Case to flag:** Two independent question marks, not one. (1) Compliance —
see Action Flag #1; Musaffa's own page calls it compliant, but on a dated
screen, while the mechanical ratio pre-check keeps failing on the same
industry classification. (2) Valuation debate is now public and two-sided —
some analysts model BMNR near or below NAV (a discount), others flag
dilution from repeated capital raises (including BMNP preferred shares) and
the risk of the whole structure re-rating hard if ETH itself falls, given no
operating-business cash flow to fall back on.
[Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/09/17/bitmine-immersion-technologies-nasdaq-bmnr-approaches-5-of-all-ethereum-in-circulation-as-analysts-question-investment-case/) ·
[Seeking Alpha — BMNP preferred](https://seekingalpha.com/article/4915591-bitmine-immersion-bmnp-preferred-capital-and-the-cost-of-ethereum-treasury-expansion)

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, and the new vol-throttle note says size
discipline matters more than it did last run.**

### NOW — ServiceNow, Inc
**Case to keep:** 6-month momentum turned positive (+12.3%, vs. -5.3% last
run) and price sits comfortably above its trailing stop, though the buffer
has narrowed to ~4.1% (was ~17.9%). DCF still shows a real but modest premium
(-11.3%), not an extreme gap.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the Shariah screen
is now stale (Action Flag #2) on the single largest position in the book;
and the trailing-stop buffer has compressed meaningfully month-over-month —
worth confirming that's the calmer walk-up to earnings and not the position
losing altitude. Next earnings now sits inside the 60-day catalyst window
(Action Flag #7) for the first time since this book tracked NOW.
[Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings) ·
[ServiceNow Q2 2026 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: reads only the *recorded*
  `shariah.status` (still `compliant`), so it stays silent despite the
  ratio-precheck fail persisting a third run. Nothing in the automated
  pipeline re-flags this on its own.
- **COMPLIANCE_SCREEN fires -> NOW**: screen is now >1 quarter old (stale)
  -> REVIEW before any add, per Stage 1 of rules.md.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit above
  their computed chandelier levels regardless, though NOW's buffer is thin.
- **VOL_THROTTLE -> BMNR**: portfolio note fired this run (ATR 7.35% > 6%) —
  a size-down signal, not an automated trim.
- **review_cadence_days (90) exceeded -> NOW** (96 days since last_review):
  re-underwrite per the discipline guard.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.99 | -97.2% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $135.47 | -11.3% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** again this run — expected, since no card has been reviewed
and flipped to `status: planned` yet; all 76 ticker cards in `setups/` are
still `draft`.

## Draft & planned setups — 50 leads, 13 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one (13 new cards: AMKR,
APA, BLSH, CORZ, DDOG, HBM, NTNX, NTR, ORCL-PD, PR, TECK, TS, XOM; 63
existing cards left unchanged). **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

32 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run —
mostly wider reward:risk on this run's price levels), 18 capped at RESEARCH:

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| MSFT | LEAD | existing | 10.0:1 | earnings 2026-10-28 | 39 |
| GDDY | LEAD | existing | 13.0:1 | earnings 2026-10-29 | 40 |
| LRCX | LEAD | existing | 20.0:1 | earnings 2026-10-21 | 32 |
| CDE | LEAD | existing | 11.8:1 | earnings 2026-10-28 | 39 |
| AGI | LEAD | existing | 13.2:1 | earnings 2026-10-28 | 39 |
| APH | LEAD | existing | 9.1:1 | earnings 2026-10-28 | 39 |
| IONQ | LEAD | existing | 18.5:1 | earnings 2026-11-04 | 46 |
| AMKR | LEAD | new | 9.6:1 | earnings 2026-10-26 | 37 |
| WDC | LEAD | existing | 14.9:1 | earnings 2026-11-05 | 47 |
| KLIC | LEAD | existing | 20.0:1 | earnings 2026-11-18 | 60 |

(Full 50-name pool, including the remaining 22 LEAD-tier and 18 RESEARCH-tier
rows, is in `leads.md` — not reproduced in full here to keep this report
readable.)

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AGI, IAG, EGO, TECK** — the recurring precious-metals/mining
  cluster; mining-royalty and metals-financing structures raised the same
  open Shariah question in earlier runs (TECK is a new addition to the pool
  this run, same open question).
- **18 RESEARCH-tier leads** capped by the asymmetry or catalyst-horizon
  gate — full list in `leads.md`.

## Follow-ups (priority order)

1. **[Urgent — recurring, 3rd run] BMNR Shariah re-screen.** The ratio
   pre-check keeps failing on the business-activity question while the
   recorded status stays "compliant"; this run adds a data point (Musaffa's
   page calling it compliant, but on a dated Q3-2025 screen) that cuts both
   ways rather than resolving it. Get a fresh Zoya/Musaffa screen dated to
   BMNR's current (2026) treasury/staking scale specifically.
2. **[Urgent — NEW this run] NOW Shariah re-screen.** Recorded screen is now
   stale (>100 days); this is the 78.5%-weight position in the book.
3. **[Housekeeping — recurring] BMNR holding file still missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` all remain null/empty, 74 days after entry.
4. **[Housekeeping — NEW this run] NOW re-underwrite is due** —
   `review_cadence_days` (90) exceeded; `last_review` still reads 2026-06-15.
5. **[Time-boxed — NEW this run] NOW earnings ~2026-10-28/11-04** — now
   inside the 60-day catalyst window; track the guidance/AI-ACV narrative
   into that print given the position's compressed trailing-stop buffer.
6. **[Housekeeping] 13 new DRAFT setup cards** added this run (76 ticker
   cards total in `setups/`); none are `planned`. Review at your own pace.
7. **[Infrastructure — still open]** No ledger yet — `transactions.csv` is
   still absent; the discipline guard (net-of-cost vs. benchmark) can't run
   without logged trades.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [Bitmine announces record Ethereum holdings and investment — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-announces-record-ethereum-holdings-and-investment)
- [BitMine Immersion Technologies (NASDAQ: BMNR) Approaches 5% Of All Ethereum In Circulation As Analysts Question Investment Case — Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/09/17/bitmine-immersion-technologies-nasdaq-bmnr-approaches-5-of-all-ethereum-in-circulation-as-analysts-question-investment-case/)
- [Bitmine Immersion: BMNP Preferred Capital And The Cost Of Ethereum Treasury Expansion — Seeking Alpha](https://seekingalpha.com/article/4915591-bitmine-immersion-bmnp-preferred-capital-and-the-cost-of-ethereum-treasury-expansion)
- [Is Bitmine Immersion Technologies Inc - BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [ServiceNow, Inc. (NOW) - Earnings History — AlphaQuery](https://www.alphaquery.com/stock/NOW/earnings-history)
- [ServiceNow, Inc. Earnings Report Dates & Earnings Forecasts — Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
