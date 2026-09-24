# Portfolio Assessment — 2026-09-24

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (16 new DRAFT setup cards auto-filled for leads
that had none; 34 existing/matching cards left unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
ran against live Yahoo data, but Yahoo's crumb endpoint was rate-limited
(HTTP 429) for parts of this run, which blanked out some metadata fetches —
see Action Flag #1 below, this is a real data gap, not a resolved issue.
`journal.py` not run — still no `transactions.csv` (discipline guard stays
dormant). **Since the last report (2026-08-19): no trades recorded** —
BMNR (10 sh @ $15.43) and NOW (7 sh @ $114.97) are unchanged.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.78**, up
**+80.0%** vs. the $15.43 cost basis. **Action Flag #1 below: this run could
not re-verify the business-activity precheck that failed last run — treat
the compliance question as still open, not cleared.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.2:1 (DCF-derived target sits below the stop; DCF doesn't fit this business — see caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale (79 days old) |
| Shariah (mechanical ratio pre-check, this run) | **UNKNOWN — data gap.** Yahoo crumb was rate-limited, so sector/industry metadata could not be fetched (`business_ok: null`). Last run (2026-08-19) this same check FAILED — industry `Capital Markets`. That flag has not been resolved, only un-checkable this run. |
| DCF intrinsic value | $0.72 vs. $27.78 price -> -97.4% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $23.3939 — price ~18.8% above it |
| 6m momentum (skip last month) | +16.9% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check only reads the *recorded* Shariah field, which cannot see the unresolved business-activity question |
| What changes verdict | A completed Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$138.90**, **+20.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.2:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | **REVIEW — recorded compliant but screen is stale** (screened 2026-06-09, 107 days old, > 100-day threshold) |
| DCF intrinsic value | $120.12 vs. $138.90 price -> -13.5% (price moderately rich to the model) |
| Trailing stop (chandelier) | $130.2538 — price is ~6.6% above it |
| 6m momentum (skip last month) | +23.2% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going further stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- **Vol-throttle note (new this run):** BMNR daily ATR ~6.56% — `verdict.py`
  flags this as a size-down signal (`vol_throttle_atr_pct: 6` in rules.md).

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.78 | 10 | $15.43 | $277.80 | +80.0% | 22.2% |
| NOW | $138.90 | 7 | $114.97 | $972.30 | +20.8% | 77.8% |

**Total value: $1,250.10** | Cost: $959.09 | **Total return: ~+30.3%** (+$291.01 unrealised)

Weighting is essentially unchanged from last report (BMNR ~22% / NOW ~78%
then too) — both positions rallied roughly in tandem since 2026-08-19.

## Action flags (priority order)

1. **[Mandate — carried over, now a data gap] BMNR's mechanical Shariah
   business-activity precheck is UNKNOWN this run**, not clean. Yahoo's
   crumb endpoint was rate-limited (HTTP 429) throughout this run, so the
   sector/industry metadata `business_precheck()` needs could not be
   fetched (`business_ok: null`). The **2026-08-19 report's FAIL is the
   most recent real read**: industry classified `Capital Markets`, which
   this repo's own knockout list treats as a core-business fail. Current
   independent reporting still describes BMNR as an Ethereum treasury
   company earning staking yield off a ~$17.1B crypto/cash balance sheet
   (5.98M ETH as of 2026-09-20) — the same profile that triggered the flag
   last time. Per Gate 1 ("Shariah knockout... -> AVOID/SELL, absolute"),
   an eventual confirmed fail would be a hard SELL independent of the
   +80.0% return. **Re-screen this specific business-activity question in
   Zoya/Musaffa — do not treat this run's silence as a clearance.** This is
   now two runs (07-13→08-19 resolved FIG this way over 7 runs; this is a
   fresh open question on the position that replaced it) without
   resolution.
2. **[Mandate] NOW's recorded Shariah screen is now stale** (107 days since
   2026-06-09, over the 100-day threshold) — re-screen in Zoya/Musaffa and
   update `screened:` in the holding file regardless of outcome.
3. **[Valuation / NOW]** P/E ~119 (recorded) — rich; VALUATION_RICH holds. Do not add.
4. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is still not a
   meaningful signal — the model (5% growth, 10% discount, no BMNR-specific
   override) doesn't fit a crypto-treasury business valued on ETH holdings
   and staking yield, not discounted operating cash flow.
5. **[Catalyst / NOW]** Next earnings now land **~2026-10-27 (33 days out —
   inside the 60-day catalyst-horizon window)**, materially closer than the
   72 days reported last run. ServiceNow raised FY2026 subscription revenue
   guidance to $15.755–$15.770B on 2026-09-17, and Cantor Fitzgerald raised
   its price target to $174 (from $141) and Needham to $155 (from $115) this
   month. The holding file's `catalyst.date` field is still `null` — worth
   updating to the confirmed date.
6. **[Discovery] 50 leads this run, 21 clear to LEAD tier** (up from 9 last
   run), 16 of which still have no setup card. GDDY, MKSI, LIF, LRCX, WDC,
   SMCI, CVE, CNQ, IONQ, TTMI, ASTS, KLIC already have cards (all DRAFT,
   unreviewed). **PLTR** carries over again with its unresolved
   government/defense business-activity question — nothing new. **EGO**
   (precious-metals cluster, flagged in prior runs) also recurs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH holdings grew to 5.98M tokens (~4.9% of
global supply) with total crypto/cash/marketable-securities holdings of
$17.1B as of 2026-09-20, up from $15.8B a week earlier. Annualized ETH
staking rewards are projected at ~$392M. B. Riley and Cantor Fitzgerald both
raised price targets this month (to $30 and $63.60) on improving crypto
momentum; the stock is up ~99% quarter-to-date. Recorded compliance status
is "compliant."
[PR Newswire (9/21)](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html) ·
[Timothy Sykes (9/17)](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_17-2/) ·
[StocksToTrade (9/16)](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16-2/)

**Case to flag (compliance, independent of the price story):** The
mechanical business-activity precheck could not run this cycle (data gap),
and the last time it *did* run (2026-08-19) it failed on the same industry
classification. The holding file is still missing `thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, and `pre_mortem` — over ten
weeks after the position was opened, there is still no PM-grade record to
weigh the compliance question against beyond the mechanical LOW-conviction
default.

**Verdict: HOLD (no technical rule fired) — the compliance question (Action
Flag #1) is still the thing to resolve, not the price action.**

### NOW — ServiceNow, Inc
**Case to keep:** FY2026 subscription revenue guidance raised to
$15.755–$15.770B (2026-09-17); Q3 subscription guidance $3.975–$3.980B at a
31% operating margin. Two analyst target hikes this month (Cantor to $174,
Needham to $155). DCF shows a moderate ~13.5% premium to intrinsic value —
wider than last run's ~6.6% gap but not extreme.
[Ad-Hoc News — Needham target](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-on-a-fresh-needham-target/70124578) ·
[Ad-Hoc News — valuation](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-falls-as-investors-weigh-ai-growth-against-rich-valuation/70136701)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the Shariah screen
is now stale (107 days); earnings land 2026-10-27 — inside the 60-day
catalyst window for the first time since this position was opened, so the
next print is a real near-term event to plan around, not a distant one.
[SEC 8-K (Q2 FY26 results)](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: it only reads the *recorded*
  `shariah.status` (`compliant`), so it stays silent despite the open
  business-activity question. Nothing in the pipeline will re-flag this on
  its own — the re-screen is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire (`trade_type: core` exempts
  both); both prices sit well above their chandelier stops regardless.
- **VOL_THROTTLE fired -> BMNR**: ATR ~6.56% > `vol_throttle_atr_pct: 6` —
  size-down note only, not a trim/sell signal.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $27.78 | -97.4% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $138.90 | -13.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** (expected — every one of the 80 cards in
`setups/` is still `status: draft`, none reviewed/flipped to `planned`).

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead that lacked one (16 new: AMKR, APA,
BBY, BLSH, CORZ, DDOG, DDS, FN, FRO, HPE, NTAP, NTNX, NUE, ONON, TECK, TS;
34 existing cards left unchanged). **Every DRAFT card is unreviewed and
Shariah UNVERIFIED — proposals to review and edit, never buys.**

21 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
asymmetry/catalyst gates capped the rest at RESEARCH):

| Ticker | R:R | Has card | Catalyst | Days out |
|---|---|---|---|---|
| GDDY | 8.9:1 | existing | earnings 2026-10-29 | 35 |
| MKSI | 10.7:1 | existing | earnings 2026-11-04 | 41 |
| NUE | 7.7:1 | new | earnings 2026-10-26 | 32 |
| LIF | 16.1:1 | existing | earnings 2026-11-09 | 46 |
| FN | 20.0:1 | new | earnings 2026-11-02 | 39 |
| TECK | 6.0:1 | new | earnings 2026-10-29 | 35 |
| LRCX | 5.6:1 | existing | earnings 2026-10-21 | 27 |
| WDC | 6.4:1 | existing | earnings 2026-11-05 | 42 |
| SMCI | 3.3:1 | existing | earnings 2026-11-03 | 40 |
| CVE | 4.9:1 | existing | earnings 2026-10-29 | 35 |
| CNQ | 5.7:1 | existing | earnings 2026-11-05 | 42 |
| IONQ | 4.5:1 | existing | earnings 2026-11-04 | 41 |
| BLSH | 4.2:1 | new | earnings 2026-11-12 | 49 |
| CORZ | 4.7:1 | new | earnings 2026-10-23 | 29 |
| AMKR | 4.5:1 | new | earnings 2026-10-26 | 32 |
| TS | 4.1:1 | new | earnings 2026-11-04 | 41 |
| APA | 3.5:1 | new | earnings 2026-11-04 | 41 |
| ONON | 5.0:1 | new | earnings 2026-11-11 | 48 |
| TTMI | 4.6:1 | existing | earnings 2026-11-04 | 41 |
| ASTS | 5.8:1 | existing | earnings 2026-11-09 | 46 |
| KLIC | 4.1:1 | existing | earnings 2026-11-18 | 55 |

All 50 cleared the liquidity floor and a clean ratio pre-check (where data
was available) — not a business-activity screen. Shariah status on every
card is `unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** (RESEARCH tier this run) — carried over again with its
  unresolved government/defense business-activity question. Nothing new.
- **CVE, CNQ, TECK** — energy/mining names; worth the same scrutiny prior
  runs gave the precious-metals cluster (CDE/AR/AGI/IAG/KGC/EGO — EGO also
  recurs this run at RESEARCH tier) before spending review time on cards.
- **29 RESEARCH-tier leads** — full list in `leads.md`, not reproduced here.

## Follow-ups (priority order)

1. **[Urgent, still open] BMNR Shariah business-activity re-screen** — this
   run's mechanical check couldn't even run (Yahoo rate-limited); the last
   real read (08-19) failed. Largest single open compliance question in the
   book (22.2% weight, +80.0% return).
2. **[Urgent, new] NOW Shariah screen is stale (107 days)** — re-screen in
   Zoya/Musaffa and update `screened:` either way.
3. **[Housekeeping, aging] BMNR holding file still missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` all still null/empty, 11 weeks after entry.
4. **[Time-boxed, escalated] NOW earnings ~2026-10-27** — now inside the
   60-day catalyst window (33 days out); worth a plan before the print,
   unlike last run's 72-day distant view.
5. **[Housekeeping] 16 new DRAFT setup cards** added this run (80 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96M Tokens, $15.8B Total — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [Bitmine ETH Holdings Reach 5.98M Tokens, $17.1B Total — Business News This Week](https://businessnewsthisweek.com/news/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-598-million-tokens-and-total-crypto-and-total-cash-holdings-of-171-billion/)
- [BMNR Stock Rallies As Massive Ethereum Bet Draws Wall Street — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_17-2/)
- [BMNR Stock Pulls Back As Traders Weigh Deep Losses And Cash Cushion — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16-2/)
- [ServiceNow stock gains on a fresh Needham target — Ad-Hoc News](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-on-a-fresh-needham-target/70124578)
- [ServiceNow stock falls as investors weigh AI growth against rich valuation — Ad-Hoc News](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-falls-as-investors-weigh-ai-growth-against-rich-valuation/70136701)
- [ServiceNow, Inc. — Form 8-K, Q2 FY2026 results — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)
