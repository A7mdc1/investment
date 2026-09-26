# Portfolio Assessment — 2026-09-26

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 160-name raw pool, top 50 kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (15 new DRAFT setup cards
auto-filled; 35 existing cards left unchanged, 63 total in `setups/` before
this run, 78 total after) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run separately — still no `transactions.csv`
(discipline guard stays dormant; no trades recorded since the last report).

**Since the last report (2026-08-19):** no trades recorded. Holdings are
unchanged (BMNR 10 sh, NOW 7 sh); both are up further since last cycle.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.56**, up
**+78.6%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.6:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL again** — industry classified `Capital Markets`; core business fails the screen. Unresolved for a third consecutive report. |
| DCF intrinsic value | $0.72 vs. $27.56 price -> -97.4% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $23.4915 — price ~14.8% above it |
| 6m momentum (skip last month) | +27.9% |
| Would buy today? | Mechanically yes per recommend.py's gates — it only reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 >= pe_rich 50). Live
price **$135.62**, **+17.96%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah (recorded) | REVIEW — recorded compliant, but screen is now **109 days old** (>1 quarter) — stale, re-screen |
| DCF intrinsic value | $120.12 vs. $135.62 price -> -11.4% (price moderately rich to the model) |
| Trailing stop (chandelier) | $130.2991 — price is only ~3.9% above it (tightest cushion of the two holdings) |
| 6m momentum (skip last month) | +21.4% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated variant view |
| What changes verdict | thesis_broken: true, the Shariah screen flipping, or price closing below $130.30 |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- Vol-throttle note (verdict.py): **BMNR ATR 6.49%** — size down per the vol throttle if adding.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.56 | 10 | $15.43 | $275.60 | +78.6% | 22.5% |
| NOW | $135.62 | 7 | $114.97 | $949.34 | +18.0% | 77.5% |

**Total value: $1,224.94** | Cost: $959.09 | **Total return: ~+27.7%** (+$265.85 unrealised)

Both positions gained since the last report (BMNR +34.2 points of return,
NOW +6.2 points). NOW's trailing-stop cushion has compressed from ~17.9% to
~3.9% since last cycle — the tightest margin either holding has carried in
recent reports, worth watching even though `trade_type: core` exempts it
from the technical trailing-stop SELL trigger.

## Action flags (priority order)

1. **[Mandate — unresolved, 3rd consecutive report] BMNR's mechanical
   Shariah ratio pre-check still FAILS**, flagging `industry 'Capital
   Markets' matches 'capital markets' — core business fails screen`. This
   still conflicts with the recorded `compliant` status (broker app,
   screened 2026-07-07). Independent research this run reinforces the
   concern rather than resolving it: BMNR pivoted in June 2025 from a
   bitcoin miner to an Ethereum "digital-asset treasury" company — it now
   holds ~5.98M ETH (~4.9% of ETH supply), 212 BTC, and ~$714M cash
   (~$17.1B total), stakes ETH for an annualized ~2.6% yield, and funds
   further ETH purchases by issuing new equity. Yahoo Finance's
   classification (Financial Services / Capital Markets) tracks the actual
   business model, not a mislabel: this is economically a leveraged,
   equity-wrapped crypto-holding vehicle, which is close to the pattern a
   business-activity screen is designed to catch. Per this repo's Gate 1
   ("Shariah knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail would be a hard SELL, independent of the
   +78.6% return. `recommend.py`'s "would buy today" check still cannot see
   this — it only reads the recorded field. **This took 7 runs to resolve
   for FIG; it has now run 3 cycles unresolved on the position that replaced
   it.**
2. **[Catalyst / NOW — status change this run]** Next earnings now
   identified at **~2026-10-28** (32 days out — provisional, not yet
   confirmed on ServiceNow's own IR site), which is **inside** the 60-day
   catalyst horizon for the first time since BMNR replaced FIG (last report
   had it 72 days out / outside the window). Company's own Q3 guide is
   +20.5% YoY subscription growth — at the low end of / slightly below the
   ~21-22% growth rate the holding's "what would change my mind" note treats
   as the deceleration threshold, even though the FY guide (+22.5%) and
   actual Q2 growth (+23-24.5%) remain above it. Worth watching at the
   print, not yet a broken thesis.
3. **[Governance/valuation — new this run] BMNR** — sell-side and analyst
   commentary in September 2026 has begun openly questioning the
   treasury-company premium (market cap tracking ETH-holdings value closely;
   peer ETHZilla already abandoned the same model in Feb 2026), and BMNR
   carries an unresolved shareholder-rights inquiry tied to a January 2026
   authorized-share increase (500M -> 50B shares) used to fund ongoing ETH
   buys. None of this is a Shariah question, but it bears on the "would you
   buy this here today?" test independent of Action Flag #1.
4. **[Valuation / NOW]** P/E ~119.02 (recorded) — rich; VALUATION_RICH holds.
   Do not add.
5. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business valued on
   ETH holdings and staking yield, not discounted operating cash flow. Treat
   as a data gap, not a valuation call.
6. **[Discovery] 50 leads this run, 24 cleared to LEAD tier** (up from 9
   last run) — the rest capped at RESEARCH by the asymmetry/catalyst gates.
   **PLTR** and **IAG** both carry over again with previously-flagged
   business-activity questions (PLTR: government/defense; IAG/mining names:
   royalty-financing structure) — nothing new to add, still open.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Actively growing its core Ethereum position
(~5.98M ETH, ~4.9% of global supply, as of ~Sept 20-22) with a stated public
goal of crossing 5% of total ETH supply before year-end 2026 — it was ~98%
of the way there as of the most recent disclosure. Staking generates a
reported ~$357M annualized run-rate. Shares surged ~5% on Sept 22 on a
27,562-ETH purchase disclosure; recent analyst target hikes include Cantor
Fitzgerald to $63.60 (from $30.60) and B. Riley to $34 (from $30), both Sept
22, 2026. Stock up +78.6% since the $15.43 cost basis; recorded compliance
status is "compliant."

**Case to flag:** The mechanical ratio pre-check still disagrees with the
recorded status — see Action Flag #1, now unresolved for 3 consecutive
reports. Separately, sell-side commentary this month is questioning whether
the equity wrapper deserves any premium over the underlying ETH (market cap
≈ ETH-holdings value; BMNR reportedly trades ~0.75-0.80x mNAV at various
points, reflecting dilution from repeated share issuance and mark-to-market
losses). The holding file itself remains incomplete: no `thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, or `pre_mortem` filled in,
~11 weeks after the position was opened — there is still no PM-grade record
to weigh the compliance/valuation questions against beyond the mechanical
LOW-conviction default. A fiscal-year-end change (Aug 31 -> Dec 31, board
approved ~July 2026) also means the next scheduled report to investors within
this window is uncertain — likely a transition-period 10-KT rather than a
normal quarterly print; confirm directly with BitMine IR before assuming a
near-term catalyst date.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, not the price action; it has now gone
three reports without action.**

### NOW — ServiceNow, Inc
**Case to keep:** 6m momentum +21.4%, and analyst sentiment has firmed
further this month — Cantor Fitzgerald raised its target from $141 to $174,
BMO from $118 to $150, and BTIG from $150 to $170 (all ~Sept 22, 2026);
consensus remains "Moderate Buy." Company beat and raised full-year
subscription-revenue guidance at the Q2 print (to +22.5% YoY), and the Armis
acquisition (closed April 2026, ~$7.6B) is now integrated into a launched
"Autonomous Security & Risk" product line. DCF shows only a moderate ~11.4%
premium to intrinsic value.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active. Non-GAAP subscription
gross margin compressed 250bps YoY in Q2 (83.0% -> 80.5%) on AI-infrastructure
costs, and Q3 guidance of +20.5% YoY subscription growth is the first
quarter-specific guide to dip toward the deceleration range the holding's own
"what would change my mind" note calls out. Separately, a June 2026
unauthenticated-API security incident (fixed within days; company attributes
the activity to researchers, not attackers who exfiltrated data) is a
reputational item from within the last ~3.5 months worth being aware of, even
with no disclosed financial or contractual impact found. The recorded
Shariah screen is now 109 days old — stale, re-screen. `last_review`
(2026-06-15) is also past the 90-day `review_cadence_days` guard — due for a
fresh "would I buy this here today?" underwrite regardless of any trigger.

**Verdict: HOLD (RULE: VALUATION_RICH) — thesis intact; growth narrative
constructive, but margin compression and the approaching Q3 print (now
inside the catalyst horizon) are the things to track before the next report.**

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (still `compliant`), so it stays silent
  despite three consecutive runs of a ratio-precheck fail. Nothing in the
  automated pipeline will re-flag this on its own until the recorded status
  is updated — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); BMNR sits ~14.8%
  above its chandelier stop, NOW only ~3.9% above (tightest margin yet).
- **VOL_THROTTLE fired -> BMNR** (ATR 6.49%): size down if adding, per
  `portfolio_notes`.
- **review_cadence_days (90) guard -> NOW**: `last_review` is 2026-06-15,
  103 days ago — overdue for re-underwrite independent of any price trigger.

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
and flipped to `status: planned` yet; all 78 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 15 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, 160 raw names)
and rewrote **`leads.md`** (top 50 by max-benefit rank). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
without one: **15 new** (NUE, NTNX, FN, XOM, BLSH, TS, CORZ, TECK, FRO, LLY,
AMKR, DDOG, HPE, NTAP, SMTC) and **35 existing cards left unchanged**. Every
DRAFT card is unreviewed and Shariah **UNVERIFIED** — proposals to review and
edit, never buys.

**24 of the 50 leads clear to LEAD tier this run** (up from 9 last report;
the rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| GOOGL | existing | 13.8:1 | earnings 2026-10-28 | 32 |
| GDDY | existing | 18.1:1 | earnings 2026-10-29 | 33 |
| LIF | existing | 18.9:1 | earnings 2026-11-09 | 44 |
| IAG | existing | 12.4:1 | earnings 2026-11-03 | 38 |
| MKSI | existing | 10.1:1 | earnings 2026-11-04 | 39 |
| FN | new | 10.2:1 | earnings 2026-11-02 | 37 |
| NTNX | new | 9.3:1 | earnings 2026-11-25 | 60 |
| NUE | new | 8.8:1 | earnings 2026-10-26 | 30 |
| CORZ | new | 8.0:1 | earnings 2026-10-23 | 27 |
| TS | new | 8.0:1 | earnings 2026-11-04 | 39 |
| BLSH | new | 7.2:1 | earnings 2026-11-12 | 47 |
| WDC | existing | 7.1:1 | earnings 2026-11-05 | 40 |
| XOM | new | 6.7:1 | earnings 2026-10-30 | 34 |
| ASTS | existing | 6.3:1 | earnings 2026-11-09 | 44 |
| TECK | new | 5.5:1 | earnings 2026-10-29 | 33 |
| TSLA | existing | 5.1:1 | earnings 2026-10-21 | 25 |
| AMKR | new | 4.0:1 | earnings 2026-10-26 | 30 |
| DINO | existing | 4.2:1 | earnings 2026-10-28 | 32 |
| TTMI | existing | 4.2:1 | earnings 2026-11-04 | 39 |
| IONQ | existing | 3.9:1 | earnings 2026-11-04 | 39 |
| LRCX | existing | 3.7:1 | earnings 2026-10-21 | 25 |
| KLIC | existing | 3.6:1 | earnings 2026-11-18 | 53 |
| DOCN | existing | 3.2:1 | earnings 2026-11-04 | 39 |
| LLY | new | 3.0:1 | earnings 2026-10-29 | 33 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **IAG** — recurring precious-metals/mining-royalty name; the same
  mining-royalty-financing question raised for CDE/AR/AGI/KGC/EGO in earlier
  runs applies here too. Still worth a real screen before spending review
  time on the card.
- **26 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now 3 reports open] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has disagreed with the recorded "compliant" status for
   three consecutive cycles now, on the business-activity question
   specifically. This is the largest compliance question in the book (22.5%
   weight, +78.6% return) and the automated pipeline will not re-surface it
   on its own — see the COMPLIANCE_GATE note above. Recommend resolving this
   before the next report.
2. **[Time-boxed — status change] NOW earnings ~2026-10-28** — now 32 days
   out and inside the 60-day catalyst horizon (was 72 days / outside it last
   report). Track the Q3 subscription-growth print against the +20.5% YoY
   guide and the margin-compression trend from Q2.
3. **[Housekeeping — still open] BMNR holding file** — `thesis_one_liner`,
   `variant_view`, `initial_stop`, `target_price`, `pre_mortem` are all still
   null/empty, ~11 weeks after the position was opened.
4. **[Housekeeping] NOW `last_review`** is 103 days old, past the 90-day
   `review_cadence_days` guard — due for a fresh underwrite.
5. **[Housekeeping] 15 new DRAFT setup cards** added this run (78 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — `transactions.csv` is
   still empty, so the discipline guard (performance vs. Shariah benchmark)
   remains dormant. No trades to log since the last report.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Q2 FY2026 results, 8-K — SEC.gov](https://www.sec.gov/)
- [ServiceNow Newsroom — "ServiceNow launches Autonomous Security & Risk" (2026)](https://www.servicenow.com/company/media/press-room.html)
- [BitMine Immersion Technologies treasury update, Sept 22, 2026 — PRNewswire](https://www.prnewswire.com/)
- [Bitmine shares surge on new ETH purchase disclosure, Sept 22, 2026 — The Coin Republic](https://www.thecoinrepublic.com/)
- [BMNR treasury-premium/mNAV scrutiny, Sept 17, 2026 — Foreign Policy Journal](https://foreignpolicyjournal.com/)
- [ServiceNow API security incident, June 2026 — TechCrunch / The Hacker News](https://techcrunch.com/)
- [ServiceNow analyst target updates, Sept 22, 2026 — ad-hoc-news.de](https://www.ad-hoc-news.de/)
