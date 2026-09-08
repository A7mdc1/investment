# Portfolio Assessment — 2026-09-08

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (14 new DRAFT setup cards auto-filled — NTNX, CORZ,
XOM, HPE, NTAP, AAPL, FLYW, BLSH, HBM, SOLV, TS, TECK, SMTC, FRO; the rest of
the pool already had cards from prior runs) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run separately — still no `transactions.csv`
(discipline guard stays dormant). No trades recorded since the last report
(2026-08-19); holdings are unchanged (BMNR 10 sh, NOW 7 sh).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.00**, up
**+62.0%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — unresolved for a third run in a row.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -9.3:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $25.00 price -> -97.1% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.3795 — price ~10.5% above it (was ~18.4% above last run — the buffer has compressed) |
| 6m momentum (skip last month) | -9.1% |
| Vol throttle | ATR 6.04% > 6% threshold — portfolio note: size down |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail (see below) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$134.22**, **+16.7%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.1:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $134.17 price -> -10.5% (price more rich to the model than last run's -6.6%) |
| Trailing stop (chandelier) | $129.7059 — price is only ~3.3% above it (was ~17.9% last run — much closer to triggering) |
| 6m momentum (skip last month) | +2.4% (flipped positive from -5.3% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
  BMNR is now 21.0% of the book, just under the 22% `max_position_pct` cap.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.00 | 10 | $15.43 | $249.90 | +62.0% | 21.0% |
| NOW | $134.22 | 7 | $114.97 | $939.54 | +16.7% | 79.0% |

**Total value: $1,189.44** | Cost: $958.09 | **Total return: ~+24.1%** (+$231.35 unrealised)

Both positions gained since 2026-08-19 ($1,105.51 -> $1,189.44, +7.6%), with
BMNR doing most of the work (+62.0% now vs. +33.1% then). NOW's rally has
also pulled its price much closer to its trailing stop (~3.3% buffer, down
from ~17.9%) — worth watching even though no SELL/TRIM rule fired yet.

## Action flags (priority order)

1. **[Mandate — still open, 3rd run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`. This still conflicts
   with the recorded `compliant` status (broker app, screened 2026-07-07,
   now stale by that measure regardless of the `stale: false` flag on
   staleness-by-date). Independent web research this run confirms BMNR
   continues to operate as an Ethereum treasury company: as of 2026-09-08 it
   holds 5.93M ETH plus BTC, Beast Industries and Eightco Holdings stakes,
   totaling **$15.7B** in crypto + cash + marketable securities, and it has
   staked more ETH than any other entity, projecting ~$386M in annualized
   staking rewards at scale. That is a larger treasury and a more
   yield-driven profile than at the last two check-ins, not a smaller one —
   the compliance question has gotten *more* relevant as the position has
   compounded, not less. Per this repo's own Gate 1 ("Shariah knockout —
   non-compliant / ratio-or-business flag -> AVOID/SELL, absolute"), a
   confirmed fail here would be a hard SELL, independent of the now +62.0%
   return. **`recommend.py`'s "would buy today" check only reads the
   recorded field and cannot see this — it is silent on the flag, same as
   every prior run.** Re-screen in Zoya/Musaffa on the business-activity
   question specifically before adding to this position, or before treating
   "compliant" as settled. Deferring this now costs more (in dollar terms)
   than it did in August or July.
2. **[Technical / NOW] Trailing-stop buffer has compressed sharply** — price
   is now only ~3.3% above the $129.71 chandelier stop (`trade_type: core`
   still exempts NOW from the automatic TRAIL_STOP rule, so nothing fires
   mechanically, but it's close enough to be worth a manual check before the
   next report).
3. **[Valuation / NOW] P/E ~119 (recorded, static field — not re-fetched live
   by signals.py)** — VALUATION_RICH still holds. Do not add.
4. **[DCF caveat / BMNR]** The -97.1% DCF "downside" is still not a
   meaningful signal — `dcf.py`'s cash-flow model (5% growth, 10% discount,
   no BMNR-specific override in the holding file) does not fit a
   crypto-treasury business whose value is driven by ETH holdings and
   staking yield, not discounted operating cash flow. Treat this number as a
   data gap, not a valuation call.
5. **[Catalyst / NOW]** Next earnings estimated **~2026-10-28** (50 days out
   — inside the 60-day catalyst-horizon window this time). Q2 FY26
   subscription revenue beat guidance by 150bp on U.S. federal demand
   strength; management flagged an ~$35M FX headwind for Q3.
   [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm) ·
   [TipRanks](https://www.tipranks.com/stocks/now/earnings)
6. **[Discovery] 50 leads this run, 26 clearing to LEAD tier** (up from 9
   last run — a materially wider clearing pool this cycle; the rest capped
   at RESEARCH by the asymmetry/catalyst gates). **PLTR, CDE, AGI, IAG, EGO**
   all carry over again with the same open business-activity questions
   flagged in prior runs (defense/government exposure for PLTR;
   mining-royalty financing structures for the metals cluster) — nothing new
   to add, still open.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressively growing its core
Ethereum position (5.93M ETH as of 2026-09-08, plus 211 BTC and equity stakes
in Beast Industries and Eightco Holdings) with $15.7B in total crypto/cash/
marketable-securities holdings and the largest ETH staking book of any
entity, projecting ~$386M in annualized staking revenue at scale. Stock up
+62.0% since the $15.43 cost basis; recorded compliance status is still
"compliant."
[Chainwire](https://chainwire.org/2026/09/08/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion/) ·
[PR Newswire](https://www.prnewswire.com/in/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion-302871981.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check still disagrees with the recorded status — see
Action Flag #1, now in its third consecutive run unresolved. The holding
file is also still missing PM-grade fields (`thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, `pre_mortem` all null), so
there is still no real conviction record to weigh the compliance question
against — two months after the position was opened.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
now the most urgent open item in the whole book, and it is getting more
expensive to leave unresolved as the position compounds.**

### NOW — ServiceNow, Inc
**Case to keep:** Subscription revenue keeps beating guidance (Q2 FY26 beat
by 150bp on U.S. federal demand); 6m momentum has flipped positive (+2.4%
vs. -5.3% last run); DCF gap to intrinsic value is a modest -10.5%, not an
extreme one.
[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm) ·
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the trailing-stop
buffer has compressed to ~3.3% from ~17.9% last run — the position has less
room to give back before a technical trigger would matter if `trade_type`
weren't exempting it; next earnings ~2026-10-28 is now inside the 60-day
catalyst window, so an FX-headwind-driven guidance surprise is a real
near-term risk to watch for.
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite three straight runs of ratio-precheck failure. That gap is
  worth naming explicitly again: nothing in the automated pipeline will
  re-flag this on its own until you update the recorded status — the
  follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit above
  their computed chandelier levels, though NOW's buffer is now thin (~3.3%).
- **VOL_THROTTLE fired -> BMNR**: ATR 6.04% > 6% threshold — size down per
  the portfolio note.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.00 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $134.17 | -10.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs** this run (expected — no card has been reviewed and
flipped to `status: planned` yet; all 77 non-template cards in `setups/` are
still `draft`).

## Draft & planned setups — 50 leads, 14 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one (14 new this run: NTNX,
CORZ, XOM, HPE, NTAP, AAPL, FLYW, BLSH, HBM, SOLV, TS, TECK, SMTC, FRO — 41
existing cards left unchanged). **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

26 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run;
the rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| MSFT | LEAD | existing | 11.3:1 | earnings 2026-10-28 | 50 |
| ALAB | LEAD | existing | 20.0:1 | earnings 2026-11-03 | 56 |
| CORZ | LEAD | new | 17.7:1 | earnings 2026-10-23 | 45 |
| GOOGL | LEAD | existing | 20.0:1 | earnings 2026-10-28 | 50 |
| GDDY | LEAD | existing | 20.0:1 | earnings 2026-10-29 | 51 |
| FOX | LEAD | existing | 11.7:1 | earnings 2026-10-29 | 51 |
| WDC | LEAD | existing | 14.4:1 | earnings 2026-11-05 | 58 |
| UTHR | LEAD | existing | 14.9:1 | earnings 2026-10-28 | 50 |
| IONQ | LEAD | existing | 9.7:1 | earnings 2026-11-04 | 57 |
| XOM | LEAD | new | 8.9:1 | earnings 2026-10-30 | 52 |
| AGI | LEAD | existing | 8.0:1 | earnings 2026-10-28 | 50 |
| CLS | LEAD | existing | 7.5:1 | earnings 2026-10-26 | 48 |
| TTMI | LEAD | existing | 7.6:1 | earnings 2026-11-04 | 57 |
| LRCX | LEAD | existing | 6.5:1 | earnings 2026-10-21 | 43 |
| STX | LEAD | existing | 4.8:1 | earnings 2026-10-27 | 49 |
| AA | LEAD | existing | 5.9:1 | earnings 2026-10-15 | 37 |
| NET | LEAD | existing | 5.7:1 | earnings 2026-10-29 | 51 |
| AAPL | LEAD | new | 5.1:1 | earnings 2026-10-29 | 51 |
| IAG | LEAD | existing | 5.2:1 | earnings 2026-11-03 | 56 |
| DOCN | LEAD | existing | 5.2:1 | earnings 2026-11-04 | 57 |
| TSLA | LEAD | existing | 4.7:1 | earnings 2026-10-21 | 43 |
| EGO | LEAD | existing | 4.1:1 | earnings 2026-10-29 | 51 |
| FLYW | LEAD | new | 5.0:1 | earnings 2026-11-03 | 56 |
| PLTR | LEAD | existing | 4.7:1 | earnings 2026-11-02 | 55 |
| CDE | LEAD | existing | 4.1:1 | earnings 2026-10-28 | 50 |
| SMCI | LEAD | existing | 3.2:1 | earnings 2026-11-03 | 56 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI, IAG, KGC, EGO** — the recurring precious-metals/mining
  cluster; mining-royalty financing structures raised the same open question
  in earlier runs. Still worth a real screen before spending review time on
  any of these cards.
- **24 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — 3rd run open] BMNR Shariah re-screen**: the mechanical ratio
   pre-check still disagrees with the recorded "compliant" status on the
   business-activity question specifically. This is now the largest
   compliance question in the book (21.0% weight, +62.0% return) and the
   automated pipeline will NOT re-surface it on its own — see the
   COMPLIANCE_GATE note above. Escalating priority: this is the same
   category of issue that took 7 runs to resolve with FIG.
2. **[Time-sensitive] NOW trailing-stop buffer is thin (~3.3%)** — no rule
   fires automatically (`trade_type: core` exemption) but worth a manual
   check before the next scheduled report given how fast the buffer
   compressed this cycle.
3. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, nearly two months after the
   position was opened.
4. **[Time-boxed] NOW earnings ~2026-10-28** — now inside the 60-day
   catalyst window; track the FX-headwind and federal-demand narrative
   between now and then.
5. **[Housekeeping] 14 new DRAFT setup cards** added this run (79 total
   files in `setups/`, 77 non-template); none are `planned`. Review at your
   own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline
   guard. No trades occurred this cycle to backfill.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.93 Million Tokens — Chainwire](https://chainwire.org/2026/09/08/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings — PR Newswire](https://www.prnewswire.com/in/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion-302871981.html)
- [ServiceNow, Inc. - Form 10-Q - FY2026 — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [NOW Earnings Dates, Upcoming and Historical — MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)
