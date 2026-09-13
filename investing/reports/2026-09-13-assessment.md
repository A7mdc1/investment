# Portfolio Assessment — 2026-09-13

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (15 new DRAFT setup cards auto-filled: ORCL-PD,
KEYS, TECK, FLYW, HPE, NTR, TS, NTAP, XOM, AAPL, ASND, APA, DDS, FRO, SNA;
35 existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run — `transactions.csv` still doesn't exist
(gitignored/never created), so the discipline guard stays dormant. No trades
recorded since the last report (2026-08-19) — same two holdings, same share
counts.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.03**, up
**+62.2%** vs. the $15.43 cost basis. **See Action Flag #1 — the Shariah
business-activity pre-check has now failed for a second consecutive run.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -8.2:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL, 2nd run running** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $25.03 price -> -97.1% (see caveat: DCF does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.0645 — price ~11.8% above it |
| 6m momentum (skip last month) | -12.9% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check only reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 >= pe_rich 50).
Live price **$132.53**, **+15.3%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $132.53 price -> -9.4% |
| Trailing stop (chandelier) | $130.3141 — price is only **~1.7% above it** (was ~17.9% above last run) |
| 6m momentum (skip last month) | +10.6% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- Vol-throttle note: BMNR ATR ~6.53% — de-risk note per `vol_throttle_atr_pct: 6`.
- `trade_type: core` on both positions exempts them from the automated
  `TRAIL_STOP` SELL trigger — the NOW cushion below is informational, not a
  live signal, but it moved from ~17.9% to ~1.7% in under a month and is
  worth your own attention.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.03 | 10 | $15.43 | $250.30 | +62.2% | 21.2% |
| NOW | $132.53 | 7 | $114.97 | $927.71 | +15.3% | 78.8% |

**Total value: $1,178.01** | Cost: $959.09 | **Total return: ~+22.8%** (+$218.92 unrealised)

## Action flags (priority order)

1. **[Mandate — escalating] BMNR's mechanical Shariah ratio pre-check FAILS
   for the second run in a row**, flagging `industry 'Capital Markets'
   matches 'capital markets' — core business fails screen`. This still
   conflicts with the recorded `compliant` status (broker app, screened
   2026-07-07, now over two months old). Fresh web research this run
   reinforces the concern rather than resolving it: as of Sept 8, 2026,
   BMNR reports **5.93M ETH + 211 BTC + equity stakes in Beast Industries
   and Eightco Holdings**, totaling **$15.7B** in crypto/cash/marketable
   securities, with **~5.07M ETH staked** for a projected **$330-386M/yr**
   in staking revenue. That is a larger treasury and a larger staking-income
   share than at the last screen — the business has moved further toward an
   investment/treasury vehicle, not back toward an operating tech company.
   Per this repo's own Gate 1 ("Shariah knockout — non-compliant /
   ratio-or-business flag -> AVOID/SELL, absolute"), a confirmed fail would
   be a hard SELL regardless of the +62.2% return. `recommend.py`'s "would
   buy today" check still only reads the recorded field and is silent on
   this. **This is the same unresolved-flag pattern that took 7 runs to
   close out with FIG** — recommend re-screening the business-activity
   question in Zoya/Musaffa now rather than letting it run another cycle.
   [PR Newswire, Sept 8](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion-302871960.html)
2. **[Technical / NOW] Trailing-stop cushion compressed sharply** — from
   ~17.9% above the chandelier stop last run to ~1.7% now ($132.53 vs.
   $130.3141). `trade_type: core` means this doesn't auto-fire SELL, but a
   further pullback would put price through the computed technical stop.
3. **[Valuation / NOW] P/E ~119.02 (recorded)** — rich; VALUATION_RICH holds. Do not add.
4. **[DCF caveat / BMNR]** The -97.1% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business whose
   value is driven by ETH/BTC holdings and staking yield, not discounted
   operating cash flow. Treat this as a data-gap, not a valuation call.
5. **[Catalyst / NOW]** Next earnings confirmed for **2026-10-28** (45 days
   out — inside the 60-day catalyst horizon). NOW last reported 2026-07-22.
   [TipRanks](https://www.tipranks.com/stocks/now/earnings)
6. **[Discovery] 50 leads this run, 20 clear to LEAD tier** (up from 9 last
   run) — see the Draft & planned setups section. **PLTR** carries over
   again with its still-unresolved government/defense business-activity
   question. The recurring precious-metals cluster (**CDE, AR, AGI, IAG,
   EGO**) also reappears, unresolved from prior runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH treasury has kept growing (5.93M ETH,
211 BTC, $15.7B total crypto/cash/securities as of Sept 8) with staking
revenue now projected at $330-386M/yr annualized; stock up +62.2% since the
$15.43 cost basis. Shares also rallied Sept 11 on crypto-regulation
optimism. Recorded compliance status is still "compliant."
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion-302871960.html) ·
[Benzinga](https://www.benzinga.com/trading-ideas/movers/26/09/61744911/bitmine-immersion-stock-rallies-friday-whats-happening)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check has now failed two runs running, and the
business (large staking-income treasury, equity stakes in other companies)
looks more like an investment vehicle each report, not less. The holding
file is still missing `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, and `pre_mortem` — two months after the position was
opened, there is still no PM-grade record to weigh the compliance question against.

**Verdict: HOLD (no technical rule fired) — the compliance question is the
thing to resolve, and it's now overdue.**

### NOW — ServiceNow, Inc
**Case to keep:** 6m momentum turned positive (+10.6%, vs. -5.3% last run);
DCF shows only a modest ~9.4% premium to intrinsic value. Compliance
recorded clean with a fresh, passing ratio pre-check.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active. The chandelier
trailing-stop cushion compressed from ~17.9% to ~1.7% since last run —
informational only given `trade_type: core`, but a real change worth
tracking into the Oct 28 print. No new company-specific news surfaced this
run beyond the confirmed earnings date.
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two consecutive ratio-precheck fails. Nothing in the
  automated pipeline will re-flag this further until you update the
  recorded status — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); NOW's cushion is thin (~1.7%) but this rule stays
  informational for core positions.
- **VOL_THROTTLE -> BMNR**: fired — ATR ~6.53% above the 6% throttle
  threshold; size-down note only, not an auto-trim.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.03 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $132.53 | -9.4% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** (expected — no card has been reviewed and
flipped to `status: planned`; every card in `setups/` is still `draft`).
All new-idea surfacing this run comes from machine discovery below instead.

## Draft & planned setups — 50 leads, 15 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings +
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one
(ORCL-PD, KEYS, TECK, FLYW, HPE, NTR, TS, NTAP, XOM, AAPL, ASND, APA, DDS,
FRO, SNA — 15 new; 35 existing cards left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never buys.**

20 of the 50 leads clear to LEAD tier this run (up from 9 last run; the rest
capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Has card | R:R | Score | Catalyst | Days out |
|---|---|---|---|---|---|
| TTMI | existing | 16.6:1 | 38.8 | earnings 2026-11-04 | 52 |
| UTHR | existing | 16.0:1 | 26.9 | earnings 2026-10-28 | 45 |
| AGI | existing | 12.7:1 | 25.3 | earnings 2026-10-28 | 45 |
| PLTR | existing | 11.2:1 | 34.2 | earnings 2026-11-02 | 50 |
| FOX | existing | 11.0:1 | 30.8 | earnings 2026-10-29 | 46 |
| GOOGL | existing | 9.4:1 | 33.5 | earnings 2026-10-28 | 45 |
| GDDY | existing | 8.9:1 | 41.5 | earnings 2026-10-29 | 46 |
| MSFT | existing | 7.6:1 | 50.6 | earnings 2026-10-28 | 45 |
| IAG | existing | 6.7:1 | 33.4 | earnings 2026-11-03 | 51 |
| DOCN | existing | 6.1:1 | 45.0 | earnings 2026-11-04 | 51 |
| AR | existing | 6.0:1 | 41.9 | earnings 2026-10-28 | 45 |
| CDE | existing | 5.9:1 | 34.3 | earnings 2026-10-28 | 45 |
| TSLA | existing | 5.6:1 | 30.6 | earnings 2026-10-21 | 38 |
| FLYW | new | 5.6:1 | 39.2 | earnings 2026-11-03 | 51 |
| TECK | new | 5.4:1 | 34.4 | earnings 2026-10-22 | 39 |
| EGO | existing | 5.1:1 | 38.2 | earnings 2026-10-29 | 46 |
| BLSH | new | 4.9:1 | 40.1 | earnings 2026-11-12 | 60 |
| MU | existing | 3.6:1 | 51.8 | earnings 2026-09-30 | 17 |
| CLS | existing | 3.5:1 | 44.0 | earnings 2026-10-26 | 43 |
| DLO | existing | 4.4:1 | 36.5 | earnings 2026-11-11 | 59 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI, IAG, EGO** — the recurring precious-metals/mining
  cluster; the same royalty-financing business-activity question raised in
  earlier runs is still open. Also worth sizing as one correlated bet, not
  five, if any are ever promoted.
- **30 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — escalating] BMNR Shariah re-screen** — the mechanical
   ratio pre-check has now disagreed with the recorded "compliant" status
   for two consecutive runs, and this run's research points the same
   direction (larger treasury, larger staking-income share). This is the
   largest compliance question in the book (21.2% weight, +62.2% return)
   and the pipeline will not re-surface it further on its own.
2. **[Housekeeping — overdue] BMNR holding file is still missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, two months after
   the position opened.
3. **[Watch] NOW trailing-stop cushion** — compressed from ~17.9% to ~1.7%
   in under a month; no action required (`trade_type: core`), but worth
   tracking into the Oct 28 earnings print.
4. **[Housekeeping] 15 new DRAFT setup cards** added this run; none are
   `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Decision support only, not financial advice. Every Shariah status above —
recorded or mechanically pre-checked — must be independently verified in
Zoya/Musaffa before you act on it.
