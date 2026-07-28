# Portfolio Assessment — 2026-07-28

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, pool widened to top **50** by max-benefit rank
per `discover_top_n: 50`) → `scaffold.py --all-leads` (28 new DRAFT setup
cards auto-filled for leads without one; 22 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` not run
separately — still 0 closed trades (`transactions.csv` doesn't exist yet —
discipline guard stays dormant until you start logging via `/apply-trade`).

Since the last report (2026-07-13): FIG was sold and BMNR was bought
(2026-07-13, recorded in a separate commit) — the book is now BMNR + NOW,
two names, down from FIG + NOW.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.795000076293945**,
up **+15.3%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.8:1 (skew argues against adding, not for it) |
| Shariah | recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see Action flag #1: the mechanical ratio pre-check now fails** |
| DCF intrinsic value | $0.72 vs. $17.80 price -> -96.0% (see caveat below — this model likely doesn't fit BMNR's business) |
| Trailing stop (chandelier) | $14.8381 — price ~16.6% above it |
| 6m momentum (skip last month) | -51.2% |
| Portfolio note | ATR 6.52% — vol-throttle note (size down) |
| Would buy today? | Mechanically "yes" per recommend.py's gates — but no thesis, stop, target, or invalidation is written on the card yet, so treat this as noise, not a signal |
| What changes verdict | thesis_broken: true, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$111.80999755859375**, **-2.75%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.12** vs. $111.81 price -> **+7.4% upside** to the model (assumptions below likely stale given the Q2 beat — see flags) |
| Trailing stop (chandelier) | $94.9691 — price is $16.84 above it |
| 6m momentum (skip last month) | -27.9% (worse than last run's -27.5%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names
  (`min_names_for_concentration: 4`). Worth naming anyway: **NOW is 81.5% of
  the book** — the concentration *rule* is off, the concentration *fact* isn't.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.80 | 10 | $15.43 | $177.95 | +15.3% | 18.5% |
| NOW | $111.81 | 7 | $114.97 | $782.67 | -2.75% | 81.5% |

**Total value: $960.62** | Cost: $959.09 | **Total return: ~+0.2%** (+$1.61 unrealised)

Book value dropped from $1,610.49 (2026-07-13, when it held FIG+NOW) to
$960.62 now — expected, since the FIG position (51% of the prior book) was
sold and replaced by a much smaller BMNR position. NOW itself gained since
last run: $112.72 -> $111.81 is roughly flat net, but the path in between was
a sharp post-earnings rally (see flag #2) that has partly faded from its
peak by today.

## Action flags (priority order)

1. **[Mandate — new this run] BMNR's mechanical Shariah ratio pre-check now
   FAILS**: `shariah.py` flags `industry 'Capital Markets' matches 'capital
   markets' — core business fails screen`. This is independent of the
   recorded broker-app "compliant" status (screened 2026-07-07, three weeks
   ago) and is a real signal, not noise: BitMine's business has visibly
   shifted since that screen — as of 2026-07-27 it holds **$11.8B in
   combined crypto/cash**, anchored by **5.79M ETH (4.8% of total supply)**,
   with **~$9.6B actively staked** generating a projected **$299M/yr in
   staking rewards** ([ForeignPolicyJournal](https://www.foreignpolicyjournal.com/2026/07/27/bitmine-immersion-technologies-nyse-bmnr-closes-in-on-5-ethereum-supply-target-with-11-8-billion-treasury/)).
   That's a large-scale digital-asset treasury/staking vehicle, not the
   immersion-cooling/hosting business the name suggests — exactly the kind
   of "Capital Markets" reclassification the pre-check is designed to catch.
   Musaffa's public halal verdict for BMNR is dated to Q3 2025
   ([musaffa.com/stock/BMNR](https://musaffa.com/stock/BMNR/)) — **before**
   this treasury strategy scaled to its current size, so it should not be
   treated as current. **Recommend re-screening BMNR in Zoya/Musaffa now**,
   with the staking-income and treasury-concentration structure specifically
   in view, rather than resting on the 2026-07-07 broker-app screen.
2. **[Catalyst / NOW] Q2 FY2026 earnings landed 2026-07-22 and beat**: EPS
   $0.90 vs. $0.76 expected (+18.4%); subscription revenue $3.877B, +24.5%
   y/y (above the $3.815-3.820B modeled last run); cRPO +21.5% y/y. Stock
   popped ~5.5% in pre-market the same day and has continued higher since;
   multiple analysts raised targets — Jefferies to $140, Evercore ISI to
   $160, JPMorgan to $150, Bernstein to $248 — consensus average ~$140 per
   S&P Global data ([Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60637159/servicenow-analysts-increase-their-forecasts-after-better-than-expected-q2-earnings)).
   The recorded DCF assumption (`growth_5y: 0.18`) is now conservative
   against a 24.5% actual print — worth revisiting if you want the DCF
   upside number to reflect the new information, though that's your call to
   make, not something auto-updated here.
3. **[Housekeeping / BMNR] Zero PM fields filled in on a 3-week-old
   position** — `conviction`, `catalyst`, `initial_stop`, `target_price`,
   `invalidation`, and `pre_mortem` are all still `null` on
   `holdings/bmnr.md`. This is why recommend.py can't compute a real
   conviction call and is falling back to the DCF-derived $0.72 target
   (see caveat below). Worth at least a stop and an invalidation trigger
   given the position is +15.3% and sits on a name with -51.2% six-month
   momentum underneath the recent bounce.
4. **[Data caveat] BMNR's DCF ($0.72 vs. $17.80, -96%) is very likely not a
   meaningful signal.** `dcf.py`'s standard cash-flow model assumes an
   operating business with modelable growth/margins; BMNR's value today is
   overwhelmingly its ETH/cash treasury, not discounted operating cash
   flows. Flagging so this number isn't read as "96% overvalued" — it's a
   model-mismatch artifact, not a valuation call.
5. **[Valuation / NOW] P/E ~119 (recorded) still >= pe_rich (50)** —
   VALUATION_RICH holds; do not add, per your own rule.
6. **[Concentration, informational — rule muted at n=2]** NOW is 81.5% of
   the book. `min_names_for_concentration: 4` keeps the mechanical
   CONCENTRATION rule from firing, but the raw fact is worth having in view
   given how thin the book still is.
7. **[Discovery pool widened]** `discover_top_n` is now 50 (was 20 as of
   the last two runs) — `leads.md` is proportionally longer this run; see
   the table below.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** +15.3% since the 2026-07-13 entry; price is comfortably
($2.96, ~16.6%) above the chandelier trailing stop; the underlying ETH
treasury strategy has scaled rapidly (5.79M ETH, ~4.8% of total supply,
$11.8B combined crypto/cash/marketable securities as of 2026-07-27) and the
stock was recently added to the Russell 1000
([TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-in-operational-update)) —
real, dated developments, not speculation.

**Case to trim/watch closely:** the mechanical Shariah ratio pre-check now
fails on business-activity grounds (flag #1) — a materially different
picture than the "compliant" screen this position was opened on three weeks
ago. Six-month momentum is deeply negative (-51.2%) even with the recent
bounce, meaning the current gain sits on top of a much larger prior
drawdown, not a clean uptrend. No stop, target, thesis, or invalidation is
written down for this position — the file still reads "NEW position" from
entry day.

**Nothing here is a compliance verdict** — the ratio pre-check is a
heads-up, not a fatwa. But given how much BitMine's business has visibly
shifted (treasury/staking scale, not immersion-cooling/hosting), re-running
the Zoya/Musaffa screen now — rather than relying on the 2026-07-07 date —
is the concrete next step, same shape as FIG's compliance flag from prior
runs, just one cycle old instead of seven.

### NOW — ServiceNow, Inc.
**Case to keep:** clean Q2 FY2026 beat on both lines (EPS +18.4% vs.
consensus, subscription revenue +24.5% y/y), raised guidance, cRPO +21.5%
y/y, and a wave of analyst target increases since the print (flag #2). DCF
still shows a modest +7.4% upside at the recorded (now conservative)
assumptions. Consensus rating remains "Strong Buy."

**Case to trim/watch closely:** P/E ~119 still VALUATION_RICH per your own
rule — rich multiples need growth to keep delivering, and this quarter did
deliver, but the bar stays high. 6m momentum is still negative (-27.9%,
slightly worse than last run) — the stock's own 12-month range has been
volatile even though this specific quarter beat. Position is 81.5% of a
two-name book; a single-name miss next quarter would land hard.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -2.75% vs. the 20% threshold.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire (`trade_type: core` on NOW
  exempts it from the technical trailing-stop rule; BMNR has no
  `trade_type` set and is currently well clear of its computed level
  regardless: $17.80 vs. $14.84).
- **VOL_THROTTLE note -> BMNR**: ATR 6.52% — informational; size down if
  adding, this is not a sell signal on its own.
- **No rule in `rules.md` currently checks a *business-activity*
  reclassification mid-hold** — flag #1 above is outside the mechanical
  rule set entirely, which is exactly why it needs your own action rather
  than waiting for a script to surface it as a SELL.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $17.80 | -96.0% | growth_5y 5%, terminal 2.5%, discount 10% — **model mismatch, see flag #4** |
| NOW | $120.12 | $111.81 | +7.4% | growth_5y 18%, terminal 3%, discount 10% — **likely conservative post-beat, see flag #2** |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run — expected, since no card has
been reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 50 leads, 28 fresh DRAFT cards this run

`discover.py`'s pool widened from 20 to 50 (`discover_top_n: 50`, changed
since last run) and wrote **`leads.md`** (top 50 by max-benefit rank).
`scaffold.py --all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for
every lead that didn't already have one — **22 cards left unchanged**
(CVE, CNQ, PLTR, VRNS, AU, ALKT, FICO, LIF, CF, ADI, DUOL, GDDY, MSFT, RCL,
ZS, SIMO, MT, PAY, AMD, ALAB, KLIC, ULTA), **28 new DRAFT cards written**
(STX, TS, UTHR, SMCI, AGI, PAAS, KGC, ARW, DELL, NEM, P, NVDA, DINO, AVGO,
GWRE, SFD, AAPL, LLY, DLO, CLS, WDC, CRH, ESE, APH, PDFS, BBY, MU, FLYW).
Compared to the 2026-07-13 pool: **TSLA, GOOGL, JNJ, CIEN, FSLR, PSX, BKR,
DG, TTMI, AA, CRDO dropped off**; **ADI, AGI, AU, CRH, ESE, KGC, NEM, PAAS,
SFD, SMCI, UTHR are new** — notably a cluster of gold/silver miners (AGI,
AU, KGC, NEM, PAAS) and materials/oil names (CRH, ESE, SFD) entering as the
screens rotate. **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.** None can reach BUY-CANDIDATE
until you review the card, edit anything you disagree with, set
`status: planned`, and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| CVE | LEAD | existing | 10.8:1 | earnings 2026-07-29 | 1 |
| CNQ | LEAD | existing | 11.7:1 | earnings 2026-08-06 | 9 |
| STX | LEAD | new | 9.5:1 | earnings 2026-07-28 | 0 |
| TS | LEAD | new | 14.7:1 | earnings 2026-08-05 | 8 |
| UTHR | LEAD | new | 12.5:1 | earnings 2026-08-05 | 8 |
| SMCI | LEAD | new | 9.7:1 | earnings 2026-08-11 | 14 |
| AGI | LEAD | new | 20.0:1 | earnings 2026-07-29 | 1 |
| PAAS | LEAD | new | 11.7:1 | earnings 2026-08-12 | 15 |
| PLTR | LEAD | existing | 10.3:1 | earnings 2026-08-03 | 6 |
| VRNS | LEAD | existing | 4.9:1 | earnings 2026-07-28 | 0 |
| AU | LEAD | existing | 8.2:1 | earnings 2026-07-31 | 3 |
| ALKT | LEAD | existing | 6.4:1 | earnings 2026-07-29 | 1 |
| KGC | LEAD | new | 7.0:1 | earnings 2026-07-29 | 1 |
| FICO | LEAD | existing | 3.7:1 | earnings 2026-07-29 | 1 |
| ARW | LEAD | new | 3.7:1 | earnings 2026-08-06 | 9 |
| LIF | LEAD | existing | 5.4:1 | earnings 2026-08-10 | 13 |
| CF | LEAD | existing | 4.6:1 | earnings 2026-08-05 | 8 |
| DELL | LEAD | new | 3.6:1 | earnings 2026-09-03 | 37 |
| ADI | LEAD | existing | 7.1:1 | earnings 2026-08-19 | 22 |
| NEM | RESEARCH | new | 10.8:1 | earnings 2026-10-22 | 86 |
| DUOL | LEAD | existing | 3.6:1 | earnings 2026-08-05 | 8 |
| GDDY | LEAD | existing | 4.2:1 | earnings 2026-07-30 | 2 |
| MSFT | LEAD | existing | 4.2:1 | earnings 2026-07-29 | 1 |
| P | LEAD | new | 8.0:1 | earnings 2026-08-26 | 29 |
| NVDA | LEAD | new | 6.9:1 | earnings 2026-08-26 | 29 |
| DINO | RESEARCH | new | 1.0:1 | earnings 2026-07-28 | 0 |
| RCL | RESEARCH | existing | 1.4:1 | earnings 2026-07-28 | 0 |
| AVGO | LEAD | new | 5.1:1 | earnings 2026-09-03 | 37 |
| ZS | LEAD | existing | 4.0:1 | earnings 2026-09-02 | 36 |
| SIMO | RESEARCH | existing | n/a | earnings 2026-07-29 | 1 |
| MT | RESEARCH | existing | 0.8:1 | earnings 2026-07-30 | 2 |
| GWRE | LEAD | new | 3.5:1 | earnings 2026-09-03 | 37 |
| PAY | RESEARCH | existing | 1.4:1 | earnings 2026-08-03 | 6 |
| SFD | RESEARCH | new | 2.5:1 | earnings 2026-08-11 | 14 |
| AAPL | RESEARCH | new | 0.1:1 | earnings 2026-07-30 | 2 |
| LLY | RESEARCH | new | 0.3:1 | earnings 2026-08-05 | 8 |
| ULTA | LEAD | existing | 3.5:1 | earnings 2026-08-27 | 30 |
| DLO | RESEARCH | new | 0.9:1 | earnings 2026-08-13 | 16 |
| CLS | RESEARCH | new | 5.0:1 | earnings 2026-10-26 | 90 |
| WDC | RESEARCH | new | n/a | earnings 2026-08-05 | 8 |
| AMD | RESEARCH | existing | n/a | earnings 2026-08-04 | 7 |
| ALAB | RESEARCH | existing | n/a | earnings 2026-08-04 | 7 |
| KLIC | RESEARCH | existing | n/a | earnings 2026-08-05 | 8 |
| CRH | RESEARCH | new | n/a | earnings 2026-07-30 | 2 |
| ESE | RESEARCH | new | n/a | earnings 2026-08-06 | 9 |
| APH | RESEARCH | new | n/a | earnings 2026-07-29 | 1 |
| PDFS | RESEARCH | new | n/a | earnings 2026-08-06 | 9 |
| BBY | RESEARCH | new | 0.2:1 | earnings 2026-08-27 | 30 |
| MU | RESEARCH | existing | n/a | earnings 2026-09-23 | 57 |
| FLYW | RESEARCH | new | n/a | earnings 2026-08-04 | 7 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, MT** — carried over from prior runs' flags (government/defense
  business-activity question for PLTR; mining/royalty financing structure
  questions for precious-metals names; MT's implausibly tight engineered
  entry/stop/target band). Nothing new to add — still open.
- **New gold/silver-mining cluster this run (AGI, AU, KGC, NEM, PAAS)** —
  five precious-metals names now in the pool at once (up from AU alone last
  run). Mining/royalty companies often carry the same financing-structure
  and non-core-revenue questions flagged on AU before; worth screening as a
  cluster, not five independent names, if you're going to look at any of
  them.
- **TSLA / GOOGL dropped off this run** (were flagged last time as
  SPUS-holding mega-caps needing a real business-activity screen). They're
  simply outside this run's top-50 by max-benefit rank, not resolved either
  way — re-check if you're still interested in either.
- **MSFT / NVDA / AVGO (SPUS holdings, in pool again/new)** — same standing
  note as before: SPUS holding the name is not a substitute for the actual
  Zoya/Musaffa business-activity screen.

## Follow-ups (priority order)

1. **[New — Shariah] BMNR ratio pre-check now fails** — re-screen in
   Zoya/Musaffa given the scaled-up ETH treasury/staking business, rather
   than resting on the 2026-07-07 broker-app screen. See Action flag #1.
2. **[Housekeeping] BMNR position has no stop, target, thesis, or
   invalidation written** three weeks after entry — worth at least a
   defensive stop given -51.2% six-month momentum underneath the current
   bounce. See Action flag #3.
3. **[Time-relevant] NOW's Q2 beat + raised guidance** — if you want the
   DCF's growth assumption to reflect the new information (24.5% actual vs.
   18% modeled), that's a `holdings/now-servicenow.md` edit, not something
   this run changes for you.
4. **[Housekeeping] 28 new DRAFT setup cards** added this run (59 total in
   `setups/` now); none are `planned`, none can reach BUY-CANDIDATE. Review
   at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades
   to `transactions.csv` (or via `/apply-trade`) to unlock the discipline
   guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Immersion Technologies (NYSE: BMNR) Closes In On 5% Ethereum Supply Target With $11.8 Billion Treasury — Foreign Policy Journal](https://www.foreignpolicyjournal.com/2026/07/27/bitmine-immersion-technologies-nyse-bmnr-closes-in-on-5-ethereum-supply-target-with-11-8-billion-treasury/)
- [BitMine Highlights Massive Ethereum Treasury in Operational Update — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-in-operational-update)
- [Is Bitmine Immersion Technologies Inc - BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [BitMine Immersion Technologies Inc Stock Price Today — Investing.com](https://www.investing.com/equities/bitmine-immersion-tech)
- [ServiceNow Analysts Increase Their Forecasts After Better-Than-Expected Q2 Earnings — Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60637159/servicenow-analysts-increase-their-forecasts-after-better-than-expected-q2-earnings)
- [ServiceNow (NOW) Reports Strong Q2 Earnings, Boosts Revenue Outlook — GuruFocus](https://www.gurufocus.com/news/8973045/servicenow-now-reports-strong-q2-earnings-boosts-revenue-outlook)
