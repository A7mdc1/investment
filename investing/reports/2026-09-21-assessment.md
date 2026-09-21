# Portfolio Assessment — 2026-09-21

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (12 new DRAFT setup cards auto-filled — NUE, FSLR,
ORCL-PD, FN, TECK, TS, CORZ, BLSH, APA, NTNX, AMKR, DDOG; 38 existing cards
left unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still no `transactions.csv` (discipline guard stays
dormant). This is the first assessment since 2026-08-19 (a 33-day gap vs. the
usual ~2-5 week cadence).

**Since the last report:** no trades recorded. Same two holdings (BMNR, NOW).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.83**, up
**+80.3%** vs. the $15.43 cost basis. **See Action Flag #1 — this is the
THIRD consecutive run (2026-07-06 as a pre-buy idea, 2026-08-19, now
2026-09-21) where the mechanical Shariah business-activity pre-check
disagrees with the recorded "compliant" status, and it is still unresolved.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.0:1 (DCF-derived target sits below the stop; DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL (unchanged)** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $27.83 price -> -97.4% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $22.4001 — price ~19.5% above it |
| 6m momentum (skip last month) | +3.0% |
| Portfolio note | ATR 6.77% — vol-throttle note fired (size down) |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$137.20**, **+19.3%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.7:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | REVIEW — recorded compliant but screen is **>100 days old** (screened 2026-06-09) — re-screen due |
| DCF intrinsic value | $120.12 vs. $137.20 price -> -12.5% (richer to the model than last run's -6.6%) |
| Trailing stop (chandelier) | $130.9973 — price ~4.7% above it (tighter cushion than last run's ~18%) |
| 6m momentum (skip last month) | +17.5% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules still muted until
  ≥4 names (`min_names_for_concentration: 4`), but see Action Flag #2 below —
  BMNR's raw weight has now crossed the 22% cap number itself.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.82 | 10 | $15.43 | $278.15 | +80.3% | 22.5% |
| NOW | $137.20 | 7 | $114.97 | $960.37 | +19.3% | 77.5% |

**Total value: $1,238.52** | Cost: $959.09 | **Total return: ~+29.1%** (+$279.43 unrealised)

BMNR's outsized gain (+80.3% since 2026-07-07, vs. +33.1% as of the last
report) has pulled its weight from 18.6% to 22.5% — purely from price
appreciation on an unchanged 10-share position, not a deliberate add.

## Action flags (priority order)

1. **[Mandate — unresolved for the 3rd run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, same flag as 2026-08-19 and 2026-07-06:
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. This has now sat open for ~2.5 months while the position
   grew from +33% to +80% and from 18.6% to 22.5% of the book. Recent
   independent coverage (Sep 17-19) sharpens the same question the pre-check
   is built to catch: analysts are explicitly debating what premium, if any,
   BMNR shareholders pay over its ETH holdings, note a recurring
   equity-dilution pipeline funding further ETH purchases, and one outlet
   flags the stock trading near/below book-value benchmarks — all describing
   a financial/treasury-vehicle profile (staking yield off a large
   crypto/cash balance sheet, capital raises, no operating product line),
   not an operating technology business.
   [Foreign Policy Journal (Sep 17)](https://www.foreignpolicyjournal.com/2026/09/17/bitmine-immersion-technologies-nasdaq-bmnr-approaches-5-of-all-ethereum-in-circulation-as-analysts-question-investment-case/) ·
   [Foreign Policy Journal (Sep 19)](https://www.foreignpolicyjournal.com/2026/09/19/bitmine-immersion-technologies-nasdaq-bmnr-appears-to-trade-below-industry-book-value-benchmarks/).
   Per this repo's own Gate 1 ("Shariah knockout — non-compliant /
   ratio-or-business flag -> AVOID/SELL, absolute"), a confirmed fail would
   be a hard SELL, independent of the return. **`recommend.py`'s "would buy
   today" check still only reads the recorded field and stays silent on
   this.** Re-screen the business-activity question specifically in
   Zoya/Musaffa before this compounds further — this is the same open
   category that took 7 runs to resolve with FIG.
2. **[New this run] BMNR weight (22.5%) has crossed `max_position_pct` (22%)
   in raw terms.** The CONCENTRATION rule does not fire mechanically
   (`min_names_for_concentration: 4`, and only 2 names are held), but the
   number itself is now past the cap you set — worth a conscious decision
   (trim / accept / add names) rather than letting the mute-rule hide it.
3. **[Shariah / NOW] Recorded screen is now stale** (>100 days since
   2026-06-09) — `shariah_status: REVIEW` per recommend.py. Not a compliance
   fail, just due for a refresh.
4. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
5. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is still not a
   meaningful signal — the model (5% growth, 10% discount, no BMNR-specific
   override) does not fit a crypto-treasury business valued on ETH holdings
   and staking yield, not discounted operating cash flow.
6. **[Catalyst / NOW]** Next earnings now land **~2026-10-28 (37 days out —
   inside the 60-day catalyst-horizon for the first time this cycle)**. AI
   ACV momentum continues (agentic revenue est. $19.1M in 2026 -> $343.9M by
   2030, still early-stage) and ServiceNow shipped new AI-governance products
   (AI Control Tower, Context Engine, Shift Zero) aimed at securing agentic
   workflows — but the stock is also described as "down 20.2% YTD" against a
   ~28% one-month rally, i.e. choppy, and one analyst-target read puts fair
   value only modestly above spot (~$145.71 avg target vs. $137.20 spot).
   [24/7 Wall St.](https://247wallst.com/investing/2026/09/03/servicenow-just-rallied-28-in-a-month-take-profits-or-buy-more/) ·
   [Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/how-ai-governance-launches-at-servicenow-now-have-changed-it) ·
   [TipRanks](https://www.tipranks.com/stocks/now/earnings)
7. **[Discovery] 50 leads this run, 29 clear to LEAD tier — up sharply from
   9/50 last run.** This jump is mechanical, not a quality signal: most of
   the pool's earnings dates (late Oct / early Nov) simply moved inside the
   60-day catalyst horizon as the calendar advanced, pulling many
   previously-RESEARCH names up a tier without any change in their
   asymmetry or edge. **PLTR** stayed at RESEARCH (reward:risk 1.7:1 <
   3.0 floor) — no new government/defense compliance question to add this
   run since it doesn't clear the asymmetry gate regardless. The
   precious-metals/mining cluster shifted composition (CDE, EGO, IAG this
   run vs. CDE/AR/AGI/IAG/KGC/EGO last run) — same open
   mining-royalty-financing compliance question as before applies to any of
   these before spending review time on their cards.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH treasury now $16.1B (5.98M ETH, ~4.9% of
global supply) plus other crypto/cash of $17.1B combined; staking yield
2.62% annualized (~$357M projected annual revenue); launched MAVAN, an
institutional-grade staking platform now serving outside clients. Analyst
panel (3 covering) is uniformly bullish with a $37.33 average target, above
the current $27.83 price.
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2) ·
[Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/09/17/bitmine-immersion-technologies-nasdaq-bmnr-approaches-5-of-all-ethereum-in-circulation-as-analysts-question-investment-case/)

**Case to flag (compliance, independent of the price story):** Same
unresolved ratio-precheck fail as the last two runs (see Action Flag #1),
now reinforced by independent coverage describing the same
financial-treasury profile the screen is built to catch. The holding file
is still missing `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, `pre_mortem` — over two months since the position was
opened, so there's still no PM-grade record to weigh the compliance
question against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — the compliance question is now
three runs old and the position is both bigger (+80.3%) and heavier (22.5%
weight) than when first flagged. This is the thing to resolve, not the
price action.**

### NOW — ServiceNow, Inc
**Case to keep:** AI ACV momentum continues; new AI-governance suite (AI
Control Tower, Context Engine, Shift Zero) targets a real emerging need
(securing agentic workflows) and reinforces the platform moat; DCF gap is
modest (-12.5%) relative to a durable ~18-21% growth profile. Earnings now
fall inside the 60-day catalyst window for the first time this cycle
(~2026-10-28).
[Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/how-ai-governance-launches-at-servicenow-now-have-changed-it) ·
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-brings-Autonomous-Workforce-to-every-major-business-function/default.aspx)

**Case to watch:** P/E ~119 (recorded) keeps VALUATION_RICH active; stock
described as choppy (down 20.2% YTD vs. a recent 28% one-month rally); the
Shariah screen is now stale (>100 days) and due for refresh; average analyst
target (~$145.71) implies only modest (~6%) upside from spot, a thinner
margin of safety than a rich multiple usually wants.
[24/7 Wall St.](https://247wallst.com/investing/2026/09/03/servicenow-just-rallied-28-in-a-month-take-profits-or-buy-more/) ·
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite three straight runs of a ratio-precheck fail. Nothing in
  the automated pipeline will re-flag this on its own until the recorded
  status is updated — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **CONCENTRATION does NOT fire -> BMNR**: muted by `min_names_for_concentration: 4`
  even though raw weight (22.5%) now exceeds `max_position_pct` (22%) — see
  Action Flag #2.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE -> BMNR**: fired — ATR 6.77% above the 6% threshold; size
  down per policy if adding.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $27.83 | -97.4% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $137.20 | -12.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 73 real cards in `setups/` are
still `draft`).

## Draft & planned setups — 50 leads, 12 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank, `discover_top_n` unchanged at 50). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
without one (12 new: NUE, FSLR, ORCL-PD, FN, TECK, TS, CORZ, BLSH, APA,
NTNX, AMKR, DDOG; 38 existing cards left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

29 of the 50 leads clear to LEAD tier this run — up sharply from 9/50 last
run (see Action Flag #7 on why: mostly earnings-calendar drift into the
60-day window, not a quality change). Top 15 by max-benefit rank:

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| IAG | LEAD | existing | 11.3:1 | earnings 2026-11-03 | 43 |
| FOX | LEAD | existing | 12.1:1 | earnings 2026-10-29 | 38 |
| CDE | LEAD | existing | 16.2:1 | earnings 2026-10-28 | 37 |
| UTHR | LEAD | existing | 18.0:1 | earnings 2026-10-28 | 37 |
| WDC | LEAD | existing | 12.3:1 | earnings 2026-11-05 | 45 |
| NUE | LEAD | new | 8.6:1 | earnings 2026-10-26 | 35 |
| IONQ | LEAD | existing | 9.9:1 | earnings 2026-11-04 | 44 |
| FSLR | LEAD | new | 20.0:1 | earnings 2026-10-29 | 38 |
| EGO | LEAD | existing | 8.3:1 | earnings 2026-10-29 | 38 |
| MKSI | LEAD | existing | 20.0:1 | earnings 2026-11-04 | 44 |
| ASTS | LEAD | existing | 11.8:1 | earnings 2026-11-09 | 49 |
| MSFT | LEAD | existing | 7.0:1 | earnings 2026-10-28 | 37 |
| FN | LEAD | new | 20.0:1 | earnings 2026-11-02 | 42 |
| LRCX | LEAD | existing | 7.0:1 | earnings 2026-10-21 | 30 |
| TECK | LEAD | new | 5.3:1 | earnings 2026-10-22 | 31 |

(14 more LEAD-tier names not shown — full list in `leads.md`; not reproduced
here in full to keep this report readable.)

All 50 cleared the liquidity floor and a clean ratio pre-check this run
(no discovery-pool AVOID this time — unlike BMNR's holding-level fail).
Shariah status on every card is `unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — stays at RESEARCH (reward:risk 1.7:1, below the 3.0 floor);
  no compliance question resurfaced this run since it doesn't clear
  asymmetry regardless.
- **CDE, EGO, IAG** — the precious-metals/mining cluster is back (composition
  shifted vs. last run's CDE/AR/AGI/IAG/KGC/EGO); the same open
  mining-royalty-financing compliance question from earlier runs applies.
- **21 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here.

## Follow-ups (priority order)

1. **[Urgent — 3rd run unresolved] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has disagreed with the recorded "compliant" status for
   three consecutive runs (2026-07-06, 2026-08-19, 2026-09-21) on the
   business-activity question specifically, while the position grew from
   +33%/18.6% weight to +80%/22.5% weight. The automated pipeline will NOT
   re-surface this on its own — see the COMPLIANCE_GATE note above.
2. **[New] BMNR weight (22.5%) vs. your own `max_position_pct` (22%)** —
   a conscious call is due (trim / accept / add names), since the mute-rule
   for <4 names is hiding this from the mechanical verdict.
3. **[Housekeeping] BMNR holding file is missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, over two months after the
   position was opened.
4. **[Housekeeping] NOW Shariah screen is stale** (>100 days,
   screened 2026-06-09) — re-screen in Zoya/Musaffa.
5. **[Time-boxed] NOW earnings ~2026-10-28** — 37 days out, now inside the
   catalyst horizon; track the AI ACV / AI-governance-suite narrative into
   the print.
6. **[Housekeeping] 12 new DRAFT setup cards** added this run (73 real
   cards total in `setups/`); none are `planned`. Review at your own pace.
7. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Immersion Technologies (NASDAQ: BMNR) Approaches 5% Of All Ethereum In Circulation As Analysts Question Investment Case — Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/09/17/bitmine-immersion-technologies-nasdaq-bmnr-approaches-5-of-all-ethereum-in-circulation-as-analysts-question-investment-case/)
- [Bitmine Immersion Technologies (NASDAQ: BMNR) Appears To Trade Below Industry Book Value Benchmarks — Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/09/19/bitmine-immersion-technologies-nasdaq-bmnr-appears-to-trade-below-industry-book-value-benchmarks/)
- [BitMine Highlights Record Ethereum Treasury and Staking Growth — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2)
- [ServiceNow Just Rallied 28% in a Month: Take Profits, or Buy More? — 24/7 Wall St.](https://247wallst.com/investing/2026/09/03/servicenow-just-rallied-28-in-a-month-take-profits-or-buy-more/)
- [How AI Governance Launches At ServiceNow (NOW) Have Changed Its Investment Story — Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/how-ai-governance-launches-at-servicenow-now-have-changed-it)
- [ServiceNow brings Autonomous Workforce to every major business function — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-brings-Autonomous-Workforce-to-every-major-business-function/default.aspx)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
