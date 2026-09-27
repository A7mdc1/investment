# Portfolio Assessment — 2026-09-27

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (14 new DRAFT setup cards auto-filled — AMKR, BLSH,
CORZ, DDOG, FN, FRO, HPE, LLY, NTAP, NTNX, NUE, SMTC, TECK, TS, XOM; the rest
of the 50 leads already had cards, left unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` run but still nothing to report —
no `transactions.csv` (discipline guard stays dormant).

**Since the last report (2026-08-19):** no trades recorded — still just BMNR
and NOW. Both positions are up further; BMNR's compliance question from last
run is still open and unresolved.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.56**, up
**+78.6%** vs. the $15.43 cost basis. **The mechanical Shariah business-
activity pre-check still disagrees with the recorded "compliant" status —
same open flag as last report, now on a materially larger gain.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.6:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $27.56 price -> -97.4% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $23.4915 — price ~17.3% above it |
| 6m momentum (skip last month) | +27.9% |
| Vol throttle | ATR 6.49% > 6% threshold — portfolio note flags sizing down (new this run) |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$135.62**, **+18.0%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | **REVIEW — recorded compliant but screen is now >100 days old (screened 2026-06-09) — re-screen** (new this run; was "not stale" last report) |
| DCF intrinsic value | $120.12 vs. $135.62 price -> -11.4% (more rich to the model than last report's -6.6%) |
| Trailing stop (chandelier) | $130.2991 — price is ~4.1% above it (tighter cushion than last report's ~17.9%) |
| 6m momentum (skip last month) | +21.4% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, the Shariah screen flipping, or price closing below the trailing stop |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names
  (NOW alone is 77.5% of the book, well above the 22% `max_position_pct` cap
  that would otherwise apply).

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.56 | 10 | $15.43 | $275.60 | +78.6% | 22.5% |
| NOW | $135.62 | 7 | $114.97 | $949.34 | +18.0% | 77.5% |

**Total value: $1,224.94** | Cost: $959.09 | **Total return: ~+27.7%** (+$265.85 unrealised)

Both positions gained since 2026-08-19 (BMNR +34.2 points of return, NOW
+6.2 points), and the book's total value rose from $1,105.51 to $1,224.94.
Weights are effectively unchanged (BMNR ~22.5% vs ~18.6%, NOW ~77.5% vs
~81.4%) — still a function of BMNR's small share count, not a deliberate
rebalance.

## Action flags (priority order)

1. **[Mandate — still open, unresolved since 2026-08-19] BMNR's mechanical
   Shariah ratio pre-check still FAILS**, flagging `industry 'Capital
   Markets' matches 'capital markets' — core business fails screen`. This
   still conflicts with the recorded `compliant` status (broker app,
   screened 2026-07-07 — six weeks stale relative to this run but not yet
   flagged `stale` by the staleness window). Fresh reporting this run
   reinforces the treasury-company read: as of 2026-09-21 Bitmine held 5.98M
   ETH (~4.9% of ETH supply) plus BTC and equity stakes, for **$17.1B** in
   total crypto + cash + "moonshot" holdings, with projected annualized ETH
   staking rewards of **$421M**. That is a larger, more concentrated
   financial-asset/staking-income profile than when this flag first fired
   last run — if anything, the business-activity question has gotten more
   pointed, not less, even as the position's paper gain has grown to
   **+78.6%**. Per this repo's own Gate 1 ("Shariah knockout —
   non-compliant / ratio-or-business flag -> AVOID/SELL, absolute"), a
   confirmed fail here would be a hard SELL regardless of the return.
   **`recommend.py`'s "would buy today" check only reads the recorded field
   and remains silent on this.** Re-screen in Zoya/Musaffa on the
   business-activity question specifically — this is now two consecutive
   monthly runs with the same unresolved flag on the position's largest
   percentage gainer.
2. **[Mandate — new this run] NOW's Shariah screen is now stale** (screened
   2026-06-09, >100 days old vs. the ~1-quarter freshness window) —
   `shariah.py` returns `"stale": true` for the first time on this holding.
   Recorded status is still `compliant`; this just needs a refresh, not a
   red flag, but it is now overdue.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add. DCF gap to intrinsic value also widened (-6.6% -> -11.4%).
4. **[Risk / BMNR — new this run] Vol throttle note fired**: BMNR's ATR is
   6.49%, above the `vol_throttle_atr_pct: 6` de-risk threshold —
   `verdict.py`'s portfolio_notes flags this as a sizing-down consideration,
   not an exit signal.
5. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is still not a
   meaningful signal — `dcf.py`'s cash-flow model (5% growth, 10% discount,
   no BMNR-specific override in the holding file) does not fit a
   crypto-treasury business whose value tracks ETH holdings and staking
   yield, not discounted operating cash flow. Treat this as a data gap, not
   a valuation call.
6. **[Catalyst / NOW]** Next earnings confirmed **2026-10-28** (31 days out
   — now inside the 60-day catalyst-horizon window, unlike last report's
   72-day-out reading). The holding file's own `catalyst.date` front-matter
   is still `null` despite this being public — worth updating so
   `recommend.py` picks it up directly next run.
7. **[Discovery] 50 leads this run**, 24 clearing to LEAD tier (up from 9
   last run) — 14 fresh DRAFT setup cards auto-filled. **PLTR** carries over
   again at RESEARCH tier with its still-unresolved government/defense
   business-activity question from prior runs — nothing new to add, still
   open.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continuing to grow its Ethereum treasury —
5.98M ETH (~4.9% of global ETH supply) as of 2026-09-21, plus 212 BTC, a
$180M stake in Beast Industries, a $105M stake in Eightco Holdings, and $714M
cash/marketable securities, for $17.1B in total holdings (up from $15.8B a
week earlier on 2026-09-14). Projected annualized ETH staking revenue of
$421M. Stock up +78.6% since the $15.43 cost basis; recorded compliance
status is still "compliant."
[PR Newswire (9/21)](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884434.html) ·
[PR Newswire (9/14)](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html) ·
[StocksToTrade (9/16)](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16-2/)

**Case to flag (compliance, independent of the price story):** The mechanical
ratio pre-check still disagrees with the recorded status — see Action Flag
#1, now two runs running. Separately, the holding file itself remains
incomplete: no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` have been filled in, six weeks after last
report flagged the same gap and now ten weeks after the position was opened.
The new vol-throttle note (ATR 6.49%) is a second, independent reason to
think about sizing here regardless of the compliance question.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, not the price action, and it has now been
open across two monthly assessment runs.**

### NOW — ServiceNow, Inc
**Case to keep:** Earnings confirmed for 2026-10-28, with $29B in remaining
performance obligations and agentic AI deployments up ninefold in nine
months; the company has a track record of beating estimates (Q2 beat: $0.90
vs. $0.76 consensus). DCF still shows only a moderate premium to intrinsic
value (-11.4%), not an extreme gap.
[TipRanks](https://www.tipranks.com/stocks/now/earnings) ·
[ServiceNow Newsroom — Q2 2026 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active and the DCF gap
widened month-over-month; the Shariah screen is now stale and due for
re-verification; the ~$35M FX headwind flagged ahead of Q3 cRPO is a real,
if modest, drag to watch in the print. Price cushion above the trailing stop
has also compressed to ~4.1% (from ~17.9% last report) even though momentum
is still positive — worth knowing the technical margin for error is thinner
than it was.
[SEC 8-K — Q2 FY2026 results](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm) ·
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

**Verdict: HOLD (VALUATION_RICH) — no action, but re-screen Shariah and
watch the trailing-stop cushion into the Oct 28 print.**

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two consecutive runs of a ratio-precheck fail. Nothing in
  the automated pipeline will re-flag this on its own until you update the
  recorded status — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit above
  their computed chandelier levels regardless — BMNR comfortably (~17.3%),
  NOW more tightly (~4.1%).
- **VOL_THROTTLE -> BMNR**: portfolio_notes fired this run (ATR 6.49% >
  6% threshold) — a sizing-down consideration, not a rule-forced exit.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $27.56 | -97.4% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $135.62 | -11.4% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; every card in `setups/` is still
`draft`).

## Draft & planned setups — 50 leads, 14 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and rewrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (14
new: AMKR, BLSH, CORZ, DDOG, FN, FRO, HPE, LLY, NTAP, NTNX, NUE, SMTC, TECK,
TS, XOM). **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.**

24 of the 50 leads clear to LEAD tier this run (up from 9 last run):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| GOOGL | LEAD | existing | 13.8:1 | earnings 2026-10-28 | 31 |
| IAG | LEAD | existing | 12.4:1 | earnings 2026-11-03 | 37 |
| GDDY | LEAD | existing | 18.1:1 | earnings 2026-10-29 | 32 |
| NUE | LEAD | new | 8.8:1 | earnings 2026-10-26 | 29 |
| NTNX | LEAD | new | 9.3:1 | earnings 2026-11-25 | 59 |
| FN | LEAD | new | 10.2:1 | earnings 2026-11-02 | 36 |
| MKSI | LEAD | existing | 10.1:1 | earnings 2026-11-04 | 38 |
| LIF | LEAD | existing | 18.9:1 | earnings 2026-11-09 | 43 |
| XOM | LEAD | new | 6.7:1 | earnings 2026-10-30 | 33 |
| BLSH | LEAD | new | 7.2:1 | earnings 2026-11-12 | 46 |
| TS | LEAD | new | 8.0:1 | earnings 2026-11-04 | 38 |
| WDC | LEAD | existing | 7.1:1 | earnings 2026-11-05 | 39 |
| CORZ | LEAD | new | 8.0:1 | earnings 2026-10-23 | 26 |
| DINO | LEAD | existing | 4.2:1 | earnings 2026-10-28 | 31 |
| TSLA | LEAD | existing | 5.1:1 | earnings 2026-10-21 | 24 |
| TECK | LEAD | new | 5.5:1 | earnings 2026-10-29 | 32 |
| LRCX | LEAD | existing | 3.7:1 | earnings 2026-10-21 | 24 |
| LLY | LEAD | new | 3.0:1 | earnings 2026-10-29 | 32 |
| IONQ | LEAD | existing | 3.9:1 | earnings 2026-11-04 | 38 |
| AMKR | LEAD | new | 4.0:1 | earnings 2026-10-26 | 29 |
| ASTS | LEAD | existing | 6.3:1 | earnings 2026-11-09 | 43 |
| TTMI | LEAD | existing | 4.2:1 | earnings 2026-11-04 | 38 |
| DOCN | LEAD | existing | 3.2:1 | earnings 2026-11-04 | 38 |
| KLIC | LEAD | existing | 3.6:1 | earnings 2026-11-18 | 52 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again at RESEARCH tier with its unresolved
  government/defense business-activity question from prior runs. Nothing new
  to add.
- **IAG** — precious-metals miner; the mining/royalty-financing business-
  activity question raised in prior runs for this cluster (CDE, AR, AGI,
  IAG, KGC, EGO) applies here too. Worth a real Zoya/Musaffa screen before
  spending review time on the card.
- **XOM, TS (Tenaris), DINO, TECK** — energy/materials names; conventional
  debt/financing structures at large integrated energy and mining companies
  are exactly what the ratio pre-check is built to catch even when it
  reports clean — verify, don't assume, given BMNR's experience this run.
- **26 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now two runs open] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has disagreed with the recorded "compliant" status for
   two consecutive monthly runs, on a position that has grown from +33.1%
   to +78.6% in that time. This is the largest open compliance question in
   the book — the automated pipeline will NOT re-surface it on its own; see
   the COMPLIANCE_GATE note above.
2. **[New] NOW Shariah re-screen**: screen is now >100 days old
   (2026-06-09) — refresh in Zoya/Musaffa and update the holding's
   `shariah.screened` date.
3. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, ten weeks after
   the position was opened and one full report cycle after this gap was
   first flagged.
4. **[Time-boxed] NOW earnings 2026-10-28** — 31 days out, now inside the
   catalyst horizon; update the holding file's `catalyst.date` field
   (currently `null`) to match, and watch the trailing-stop cushion (now
   ~4.1%, down from ~17.9%) into the print.
5. **[Housekeeping] 14 new DRAFT setup cards** added this run (AMKR, BLSH,
   CORZ, DDOG, FN, FRO, HPE, LLY, NTAP, NTNX, NUE, SMTC, TECK, TS, XOM).
   None are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.98 Million Tokens, Total Holdings $17.1B — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884434.html)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens, Total Holdings $15.8B — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [BMNR Stock Pulls Back As Traders Weigh Deep Losses And Cash Cushion — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16-2/)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow, Inc. — Form 8-K — Q2 FY2026 — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)
