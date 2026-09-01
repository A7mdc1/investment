# Portfolio Assessment — 2026-09-01

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (15 new DRAFT setup cards auto-filled — BBY, EXPE,
SMTC, SMCIP, TECK, TS, BLSH, FLYW, XOM, BKR, ASND, AAPL, PSX, APA, NTNX; the
rest of the 50 leads already had cards, unchanged) → `prices.py` / `shariah.py`
/ `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` still returns 0 closed trades — no
`transactions.csv` yet (discipline guard stays dormant).

**Since the last report (2026-08-19):** no trades logged. Same two holdings —
BMNR and NOW. The BMNR Shariah ratio pre-check flag from last run is **still
open and still failing** — see Action Flag #1.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$23.59**, up
**+52.9%** vs. the $15.43 cost basis. **Action Flag #1 carries over unresolved:
the mechanical Shariah business-activity pre-check still disagrees with the
recorded "compliant" status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -34.5:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL — unchanged from last run** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $23.59 price -> -97.0% (not a meaningful signal — see caveat below) |
| Trailing stop (chandelier) | $22.9288 — price ~2.8% above it (much tighter cushion than last run's ~18%) |
| 6m momentum (skip last month) | -11.0% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction), or a HARD_STOP/TRAIL_STOP trigger at $22.93 |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$143.05**, **+24.4%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $143.05 price -> -16.0% (gap to intrinsic value widened from -6.6% last run) |
| Trailing stop (chandelier) | $130.6373 — price is ~9.9% above it |
| 6m momentum (skip last month) | +0.9% (turned positive since last run's -5.3%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $23.59 | 10 | $15.43 | $235.90 | +52.9% | 19.1% |
| NOW | $143.08 | 7 | $114.97 | $1,001.56 | +24.4% | 80.9% |

**Total value: $1,237.46** | Cost: $959.09 | **Total return: ~+29.0%** (+$278.37 unrealised)

Both positions are up sharply since the last report — BMNR +$30.45 in value,
NOW +$101.50 — and the book stays as concentrated in NOW (80.9%) as before;
still a function of BMNR's small share count, not a deliberate sizing call
recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — still open, 2nd run in a row] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, same flag as 2026-08-19: `industry 'Capital
   Markets' matches 'capital markets' — core business fails screen`. This
   still conflicts with the recorded `compliant` status (broker app, screened
   2026-07-07 — now stale-adjacent at 56 days old). Current reporting
   confirms the profile that raised the question last run hasn't changed:
   BMNR now holds ~5.9M ETH (~4.9% of global supply, ~$14.8-15.6B in total
   crypto/cash holdings), runs its own staking operation (MAVAN) projecting
   $330-381M in annualized staking revenue, and continues an aggressive
   buyback (19M+ shares repurchased since July). That is a yield-generating
   financial-asset treasury — the same category a business-activity screen
   is built to flag. Per this repo's own Gate 1 ("Shariah knockout —
   non-compliant / ratio-or-business flag -> AVOID/SELL, absolute"), a
   confirmed fail would be a hard SELL, independent of the +52.9% return.
   **`recommend.py`'s "would buy today" check still only reads the recorded
   field and stays silent on this.** This is now two runs unresolved on the
   position with the second-largest weight in the book (19.1%) — the
   re-screen in Zoya/Musaffa is overdue.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still
   holds. Do not add.
3. **[DCF caveat / BMNR]** The -97.0% DCF "downside" is still not a
   meaningful signal — `dcf.py`'s cash-flow model (5% growth, 10% discount,
   no BMNR-specific override) doesn't fit a crypto-treasury business valued
   on ETH holdings and staking yield, not discounted operating cash flow.
   Treat as a data gap, not a valuation call.
4. **[Catalyst / NOW] Next earnings now ~2026-10-28 — 57 days out, just
   inside the 60-day catalyst-horizon default** (was 72 days out and outside
   the window last run). The holding file's `catalyst.date` is still `null`
   though, so `recommend.py` can't see this itself — worth setting the date
   on the card. Growth narrative continues constructive (AI ACV past $1B
   last run; no contradicting news this run).
5. **[Catalyst / BMNR] Mid-September CLARITY Act vote** flagged in current
   coverage as a crypto-policy catalyst that could move ETH-treasury names —
   not in the holding file, not gated by this system, purely FYI.
6. **[Discovery] 50 leads this run, 19 clearing to LEAD tier** — up sharply
   from 9/50 last run (more names now have catalysts inside the 60-day
   window as September earnings season approaches). **PLTR** carries over
   again, still capped at RESEARCH (reward:risk 1.2:1, below floor) — its
   unresolved government/defense business-activity question from prior runs
   remains untouched either way. The precious-metals/mining cluster (AGI,
   CDE, EGO) moved INTO LEAD tier this run; KGC, IAG, AR stayed at RESEARCH —
   same open business-activity question as prior runs on this cluster,
   nothing new to add.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH position grew to ~5.9M tokens (~4.9% of
global supply) with total crypto/cash holdings reported between $14.8B and
$15.6B depending on the snapshot date. Buyback continues (3M shares
repurchased in the past week alone per latest coverage, 19M+ since July).
Staking revenue run-rate projected at $330-381M annualized via its own MAVAN
validator network. Stock up +52.9% since the $15.43 cost basis; recorded
compliance status is still "compliant."
[BitMine ETH holdings announcement — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-81-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-6-billion-302846858.html) ·
[Timothy Sykes — BMNR Ethereum treasury coverage](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_25/)

**Case to flag (compliance, independent of the price story):** The mechanical
ratio pre-check still disagrees with the recorded status — see Action Flag
#1, now open for a second consecutive run. The holding file is still missing
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, and
`pre_mortem` — over 7 weeks after the position was opened, there is still no
PM-grade record to weigh the compliance question against beyond the
mechanical LOW-conviction default. The trailing stop has also tightened
considerably in dollar terms relative to price (chandelier $22.93 vs. price
$23.59, ~2.8% cushion) even though the position is up over 50% — worth
knowing if volatility picks up.

**Verdict: HOLD (no technical rule fired) — the compliance question is still
the thing to resolve first, not the price action, and it has now gone two
runs without action.**

### NOW — ServiceNow, Inc
**Case to keep:** No news this run contradicts the growth thesis (AI ACV
past $1B, Armis integration ongoing per last run's research — nothing
new surfaced to revisit it this cycle). Q3 2026 consensus EPS estimate is
$1.03 vs. $0.96 a year ago. Stock has drifted markedly higher since its last
earnings print (July 22, 2026).
[TipRanks — NOW earnings](https://www.tipranks.com/stocks/now/earnings)

**Case to watch:** P/E ~119 (recorded) keeps VALUATION_RICH active. DCF gap
to intrinsic value widened to -16.0% from -6.6% last run — price has run
further ahead of the model's estimate even as the model's inputs (18%
growth, 3% terminal, 10% discount) haven't changed. Next earnings ~2026-10-28
now sits just inside the 60-day catalyst window (57 days out) — the first
time in recent runs this holding has had a near-term binary event to react
to.
[MarketChameleon — NOW earnings dates](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: still only reads the *recorded*
  `shariah.status` field (currently `compliant`), so it stays silent despite
  two straight runs of ratio-precheck failure. Nothing in the automated
  pipeline will re-flag this on its own until the recorded status is
  updated — the follow-up remains on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); BMNR's price sits
  only ~2.8% above its chandelier level now, worth a closer watch even
  though the rule is exempted.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $23.59 | -97.0% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $143.05 | -16.0% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs** this run — expected, since no card has been reviewed and
flipped to `status: planned` yet; all 79 cards in `setups/` are still `draft`.

## Draft & planned setups — 50 leads, 15 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank, unchanged `discover_top_n: 50`). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for the 15 leads
without one (BBY, EXPE, SMTC, SMCIP, TECK, TS, BLSH, FLYW, XOM, BKR, ASND,
AAPL, PSX, APA, NTNX); the remaining 35 leads already had cards from prior
runs, left unchanged. **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

19 of the 50 leads clear to LEAD tier this run (up from 9/50 last run) — the
rest capped at RESEARCH by the asymmetry or catalyst-horizon gate:

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| DELL | LEAD | existing | 5.5:1 | earnings 2026-09-01 | 0 (today) |
| ZS | LEAD | existing | 6.8:1 | earnings 2026-09-03 | 2 |
| GWRE | LEAD | existing | 4.2:1 | earnings 2026-09-03 | 2 |
| SNX | LEAD | existing | 10.6:1 | earnings 2026-09-24 | 23 |
| MU | LEAD | existing | 4.8:1 | earnings 2026-09-30 | 29 |
| AA | LEAD | existing | 7.3:1 | earnings 2026-10-15 | 44 |
| TSLA | LEAD | existing | 5.1:1 | earnings 2026-10-21 | 50 |
| HAS | LEAD | existing | 4.9:1 | earnings 2026-10-22 | 51 |
| AGI | LEAD | existing | 16.5:1 | earnings 2026-10-28 | 57 |
| APH | LEAD | existing | 6.2:1 | earnings 2026-10-28 | 57 |
| AVT | LEAD | existing | 5.8:1 | earnings 2026-10-28 | 57 |
| CDE | LEAD | existing | 4.4:1 | earnings 2026-10-28 | 57 |
| UTHR | LEAD | existing | 5.8:1 | earnings 2026-10-28 | 57 |
| FOX | LEAD | existing | 6.3:1 | earnings 2026-10-29 | 58 |
| SIMO | LEAD | existing | 6.1:1 | earnings 2026-10-29 | 58 |
| HBM | LEAD | no card | 7.1:1 | earnings 2026-10-29 | 58 |
| NET | LEAD | existing | 5.1:1 | earnings 2026-10-29 | 58 |
| EGO | LEAD | existing | 3.5:1 | earnings 2026-10-29 | 58 |
| GDDY | LEAD | existing | 3.5:1 | earnings 2026-10-29 | 58 |

(DELL's earnings date is today per the discovery snapshot — if still
accurate, that catalyst has effectively already arrived; verify before
treating the lead as forward-looking.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — still capped at RESEARCH (reward:risk 1.2:1, below floor);
  carries the same unresolved government/defense business-activity question
  from prior runs. Nothing new to add.
- **AGI, CDE, EGO** moved into LEAD tier this run (were RESEARCH-tier or
  absent before); **KGC, IAG, AR** stayed at RESEARCH. This whole
  precious-metals/mining cluster carries the same recurring
  mining-royalty-financing business-activity question raised in earlier
  runs — worth a real Zoya/Musaffa screen before spending review time on
  any of these cards, LEAD tier or not.
- **31 RESEARCH-tier leads** not reproduced here in full — see `leads.md`.

## Follow-ups (priority order)

1. **[Urgent — now 2 runs unresolved] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status for two consecutive runs (2026-08-19 and 2026-09-01) on the same
   business-activity question. This is the largest open compliance question
   in the book (19.1% weight, +52.9% return) and the automated pipeline will
   NOT re-surface it on its own — see the COMPLIANCE_GATE note above. This
   should not carry to a third run without action.
2. **[Housekeeping] BMNR holding file still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, now 7+ weeks after the position
   was opened.
3. **[Housekeeping] NOW's `catalyst.date` is null** despite a known estimated
   earnings date (~2026-10-28, now inside the 60-day gate window) —
   setting it would let `recommend.py` see the catalyst itself instead of
   relying on this report's manual research each run.
4. **[Time-boxed] NOW earnings ~2026-10-28** — 57 days out, now inside the
   catalyst-horizon window; track the AI ACV / Armis narrative into the
   print.
5. **[Housekeeping] 15 new DRAFT setup cards** added this run (79 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — `transactions.csv` is
   still empty and the discipline guard stays dormant. Log any executed
   trade via `/apply-trade`.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Immersion Technologies (BMNR) Announces ETH Holdings — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-81-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-6-billion-302846858.html)
- [BMNR Stock Jumps As Massive Ethereum Treasury Draws Traders — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_25/)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [NOW Earnings Dates, Upcoming and Historical — MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)
