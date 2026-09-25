# Portfolio Assessment — 2026-09-25

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, fresh pool, top 50 kept per `discover_top_n:
50`) → `scaffold.py --all-leads` (15 new DRAFT setup cards auto-filled — FN,
LLY, NTNX, NUE, TS, XOM, BLSH, TECK, FRO, CORZ, AMKR, DDOG, HPE, NTAP, AAPL;
the remaining ~35 leads already had cards and were left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` not run
separately — still no `transactions.csv` (discipline guard stays dormant; no
trades logged since the FIG sale / BMNR buy in July).

**Since the last report (2026-08-19):** no trades. Same two holdings (BMNR,
NOW). BMNR's weight has now crossed `max_position_pct` (22.4% vs. the 22%
knob) purely from price appreciation, not a deliberate add.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.48**, up
**+78.1%** vs. the $15.43 cost basis. **See Action Flag #1 — the mechanical
Shariah business-activity pre-check still disagrees with the recorded
"compliant" status, for the second consecutive report.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.7:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from last run) |
| DCF intrinsic value | $0.72 vs. $27.48 price -> -97.4% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $23.4929 — price ~17.0% above it |
| 6m momentum (skip last month) | +27.9% |
| Weight | **22.4%** — now above the `max_position_pct: 22` knob, though the CONCENTRATION rule stays muted (only 2 holdings, floor is 4) |
| Would buy today? | Mechanically yes per `recommend.py`'s gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$136.19**, **+18.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.7:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | **REVIEW** — recorded compliant but screen is now >100 days old (screened 2026-06-09); re-screen |
| DCF intrinsic value | $120.12 vs. $136.19 price -> -11.9% (price moderately rich to the model) |
| Trailing stop (chandelier) | $130.3448 — price ~4.5% above it (tightened vs. last run's ~18%) |
| 6m momentum (skip last month) | +21.4% |
| Would buy today? | Mechanically yes per `recommend.py`'s gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules stay muted until >= 4 names, per verdict.py's own note.
- Portfolio note: BMNR ATR 6.51% — vol throttle flagged (`portfolio_notes`), size down accordingly if adding.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.48 | 10 | $15.43 | $274.75 | +78.1% | 22.4% |
| NOW | $136.19 | 7 | $114.97 | $953.33 | +18.5% | 77.6% |

**Total value: $1,228.08** | Cost: $959.09 | **Total return: ~+28.0%** (+$268.99 unrealised)

Both positions are up since the last report; BMNR's gain has pulled it above
the 22% single-name cap for the first time, purely on price action.

## Action flags (priority order)

1. **[Mandate — unresolved, 2nd consecutive run] BMNR's mechanical Shariah
   ratio pre-check still FAILS**, flagging `industry 'Capital Markets'
   matches 'capital markets' — core business fails screen`. This still
   conflicts with the recorded `compliant` status (broker app, screened
   2026-07-07 — now 80 days old). Fresh web research this run reinforces the
   same picture as last time: BMNR now holds ~5.98M ETH (4.9% of total
   supply) plus cash/securities/"moonshot" holdings totaling **$17.1B**, runs
   a staking program (MAVAN) projecting **$357M** in annualized staking
   revenue, and is actively expanding that staking infrastructure to
   institutional clients — i.e., an asset-management/yield business on a
   large financial-asset treasury, which is exactly the profile a
   business-activity screen is built to catch. Per this repo's own Gate 1
   ("Shariah knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail here would be a hard SELL, independent of the
   +78.1% return. **`recommend.py`'s "would buy today" check only reads the
   recorded field and is silent on this.** This is now the position's second
   full reporting cycle unresolved, and the position has grown from 18.6% to
   22.4% of the book in that time — re-screen the business-activity question
   specifically in Zoya/Musaffa before this compounds further.
2. **[Mandate / NOW] Shariah screen is stale** — recorded 2026-06-09, now
   >100 days old (COMPLIANCE_SCREEN convention is "review before any add" past
   ~1 quarter). Ratio pre-check itself is still clean (debt 1.7%, liquid
   4.5%), so this is a staleness flag, not a fail — but NOW is 77.6% of the
   book and hasn't been re-screened since June.
3. **[Concentration / BMNR]** Weight crossed the 22% `max_position_pct` knob
   this run (22.4%). The CONCENTRATION rule doesn't mechanically fire yet
   (verdict.py requires >= 4 names before it activates), but the cap itself
   is already breached in substance.
4. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business valued on
   ETH holdings and staking yield, not discounted operating cash flow. Treat
   as a data gap, not a valuation call.
5. **[Catalyst / NOW]** Next earnings estimated **~2026-10-27/28** (32-33
   days out — inside the 60-day catalyst horizon for the first time this
   cycle). Analyst sentiment has firmed since last run: Cantor Fitzgerald
   raised its price target to $174 (from $141, Overweight) on 2026-09-21;
   ServiceNow also closed a ~5% stake / $40M Series C investment in Indian
   banking-software provider BusinessNext, extending into India/Southeast
   Asia. IR has not posted an official date yet — front-matter `catalyst.date`
   is left `null` per the file's own note until confirmed.
6. **[Discovery] 50 leads this run**, 21 clearing to LEAD tier (up from 9 last
   run). **PLTR** and **IAG** carry forward with open business-activity
   questions from prior runs (PLTR: government/defense; IAG/mining-royalty
   cluster generally) — nothing new to add, still open before spending review
   time on either.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH treasury and staking program continue to
scale — 5.98M ETH (4.9% of total supply), $17.1B combined crypto/cash/
securities holdings as of 2026-09-21, and a staking platform (MAVAN)
projecting $357M annualized revenue at a 2.62% yield. Stock up +78.1% since
the $15.43 cost basis; recorded compliance status is still "compliant."
Chairman Tom Lee is keynoting Korea Blockchain Week on 2026-09-30, continuing
the public push toward 5% of total ETH supply.
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884434.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status for a second
straight run — see Action Flag #1. The holding file is still missing
PM-grade fields (`thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, `pre_mortem` all null), so there's no recorded conviction
case to weigh the compliance question against beyond the mechanical
LOW-conviction default. Weight has also grown past the 22% cap.

**Verdict: HOLD (no technical rule fired) — the compliance question, now
unresolved for two cycles on a growing position, is the thing to resolve
first, not the price action.**

### NOW — ServiceNow, Inc
**Case to keep:** Cantor Fitzgerald raised its price target to $174
(Overweight) on 2026-09-21; consensus is Buy across 32 analysts as of the
same date. New EmployeeWorks deployment (INRY, 2026-09-23) and the BusinessNext
investment extend the platform story into new geographies. DCF shows an
~11.9% premium to intrinsic value — richer than last run (-6.6%) but not
extreme.
[CNBC](https://www.cnbc.com/quotes/NOW) ·
[Stockanalysis.com](https://stockanalysis.com/stocks/now/)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; Shariah screen is
now stale (>100 days); earnings now sit inside the 60-day catalyst window
(~Oct 27/28) without a confirmed IR date yet.
[SEC 8-K FY2026 Q2](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite the ratio-precheck fail persisting for a second run. Nothing
  in the automated pipeline will re-flag this on its own until the recorded
  status changes — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **COMPLIANCE_SCREEN (staleness) -> NOW**: screen is >1 quarter old; review
  before any add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit above
  their computed chandelier levels regardless.
- **VOL_THROTTLE -> BMNR**: ATR 6.51% flagged in `portfolio_notes` — size
  down if adding to this name.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $27.48 | -97.4% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $136.19 | -11.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs** this run (expected — no card has been reviewed and
flipped to `status: planned` yet; all 78 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 15 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one — 15
new: FN, LLY, NTNX, NUE, TS, XOM, BLSH, TECK, FRO, CORZ, AMKR, DDOG, HPE,
NTAP, AAPL. The remaining ~35 leads already had cards from prior runs and
were left unchanged. **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

21 of the 50 leads clear to LEAD tier this run (up from 9 last run):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| GOOGL | existing | 14.6:1 | earnings 2026-10-28 | 33 |
| IAG | existing | 12.7:1 | earnings 2026-11-03 | 39 |
| GDDY | existing | 18.6:1 | earnings 2026-10-29 | 34 |
| NUE | new | 8.7:1 | earnings 2026-10-26 | 31 |
| MKSI | existing | 9.7:1 | earnings 2026-11-04 | 40 |
| FN | new | 16.2:1 | earnings 2026-11-02 | 38 |
| XOM | new | 7.5:1 | earnings 2026-10-30 | 35 |
| LIF | existing | 13.0:1 | earnings 2026-11-09 | 45 |
| TS | new | 8.7:1 | earnings 2026-11-04 | 40 |
| LLY | new | 6.3:1 | earnings 2026-10-29 | 34 |
| WDC | existing | 7.4:1 | earnings 2026-11-05 | 41 |
| BLSH | new | 6.9:1 | earnings 2026-11-12 | 48 |
| TSLA | existing | 5.1:1 | earnings 2026-10-21 | 26 |
| TECK | new | 5.5:1 | earnings 2026-10-29 | 34 |
| CORZ | new | 6.9:1 | earnings 2026-10-23 | 28 |
| LRCX | existing | 3.8:1 | earnings 2026-10-21 | 26 |
| IONQ | existing | 3.5:1 | earnings 2026-11-04 | 40 |
| AMKR | new | 4.0:1 | earnings 2026-10-26 | 31 |
| ASTS | existing | 6.4:1 | earnings 2026-11-09 | 45 |
| TTMI | existing | 4.0:1 | earnings 2026-11-04 | 40 |
| KLIC | existing | 3.5:1 | earnings 2026-11-18 | 54 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — still carries its unresolved government/defense business-activity
  question from prior runs (RESEARCH tier this run, R:R 0.9:1 — also fails
  the asymmetry gate outright). Nothing new to add, still open.
- **IAG** — mining-royalty financing structure flagged in prior runs; the
  rest of the precious-metals cluster (CDE, AR, AGI, KGC, EGO) dropped out of
  this run's top 50, but the open question on the category stands.
- **29 RESEARCH-tier leads** this run — full list in `leads.md`; not
  reproduced here in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — 2nd consecutive run] BMNR Shariah re-screen**: the mechanical
   ratio pre-check disagrees with the recorded "compliant" status on the
   business-activity question specifically, and the position has grown from
   18.6% to 22.4% of the book while unresolved. This is the largest open
   compliance question in the book and the automated pipeline will not
   re-surface it on its own.
2. **[Mandate] NOW Shariah re-screen** — recorded status is now >100 days
   old; re-screen before any add and to keep the record current on 77.6% of
   the book.
3. **[Housekeeping] BMNR holding file is missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, ~11 weeks after the position was
   opened.
4. **[Time-boxed] NOW earnings ~2026-10-27/28** — now inside the 60-day
   catalyst horizon; confirm the official IR date once posted and update the
   holding's `catalyst.date` field.
5. **[Housekeeping] 15 new DRAFT setup cards** added this run (78 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Highlights Record Ethereum Treasury and Staking Growth — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.98 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884434.html)
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [NOW: ServiceNow, Inc. Stock Price, Quote and News — CNBC](https://www.cnbc.com/quotes/NOW)
- [ServiceNow (NOW) Stock Price & Overview — Stockanalysis.com](https://stockanalysis.com/stocks/now/)
- [ServiceNow, Inc. Form 8-K FY2026 Q2 — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)
