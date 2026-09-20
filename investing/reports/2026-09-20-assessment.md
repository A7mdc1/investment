# Portfolio Assessment — 2026-09-20

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (14 new DRAFT setup cards auto-filled — AMKR,
ORCL-PD, HBM, TECK, NUE, CORZ, DDOG, PR, NTR, NTNX, TS, BLSH, XOM, APA; 36
existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` run for completeness — still no `transactions.csv` (0
closed trades; discipline guard stays dormant).

**Since the last report (2026-08-19), 32 days ago:** no trades were logged.
Both holdings are unchanged in size; both have moved meaningfully in price.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.99**, up
**+68.4%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.3:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL, unchanged from last run** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $25.99 price -> -97.2% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $21.2401 — price ~18.3% above it |
| 6m momentum (skip last month) | -4.3% |
| Portfolio note | ATR 7.35% — above the 6% vol-throttle threshold; size down |
| Would buy today? | Mechanically yes per recommend.py's gates — this check only reads the *recorded* Shariah field, not the ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$135.47**, **+17.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | **REVIEW, NEW this run** — recorded compliant (screened 2026-06-09) but the screen is now >100 days old; re-screen |
| DCF intrinsic value | $120.12 vs. $135.47 price -> -11.3% (price modestly rich to the model) |
| Trailing stop (chandelier) | $130.1246 — price only ~3.9% above it (tightest buffer of the two holdings) |
| 6m momentum (skip last month) | +12.3% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, the Shariah screen flipping, or a technical break below $130.12 |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.99 | 10 | $15.43 | $259.90 | +68.4% | 21.5% |
| NOW | $135.47 | 7 | $114.97 | $948.29 | +17.8% | 78.5% |

**Total value: $1,208.19** | Cost: $959.09 | **Total return: ~+26.0%** (+$249.10 unrealised)

Concentration in NOW eased slightly from 81.4% (last run) to 78.5%, purely
because BMNR's price gain outpaced NOW's — not a rebalancing decision
recorded anywhere in the files.

## Action flags (priority order)

1. **[Mandate — carried over, still open] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, same `Capital Markets` business-activity flag as
   last run, still unresolved five weeks later. The position is now up
   **+68.4%** (vs. +33.1% last run) and its weight has grown to 21.5% — the
   gain makes this flag more consequential, not less. Per this repo's own
   Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL regardless
   of return. Re-screen in Zoya/Musaffa on the business-activity question
   specifically before treating "compliant" as settled.
2. **[Mandate — NEW this run] NOW's Shariah screen is now stale** —
   screened 2026-06-09, which is >100 days old (past the ~1-quarter
   freshness bar `recommend.py` checks). `recommend.py` now reports
   `shariah_status: REVIEW` instead of PASS. This is a policy issue
   independent of price: re-screen before treating compliance as current,
   especially on the account's largest position (78.5% of the book).
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
4. **[DCF caveat / BMNR]** The -97.2% DCF "downside" remains not a
   meaningful signal — the model's growth/discount assumptions don't fit a
   crypto-treasury business valued on ETH holdings and staking yield, not
   discounted operating cash flow.
5. **[Catalyst / NOW]** Next earnings land **2026-10-28** (38 days out —
   now *inside* the 60-day catalyst-horizon default, unlike last run's
   72-day gap). Guidance already points to Q3 subscription revenue of
   $3.975–$3.980B (+20.5% YoY) and FY2026 subscription revenue raised to
   $15.76–$15.78B (+22.5% YoY); AI ACV is tracking toward a 30%-by-2030
   target. The holding file's `catalyst.date` is still `null` — worth
   updating to 2026-10-28 now that it's confirmed.
6. **[BMNR] Vol-throttle note fired**: daily ATR ~7.35%, above the 6%
   threshold — `verdict.py` flags this for position-sizing awareness, not
   a sell signal.
7. **[Discovery] 50 leads this run** (unchanged `discover_top_n: 50`), 33
   clearing to LEAD tier (up from 9 last run — reward:risk profiles across
   the pool improved broadly), 17 capped at RESEARCH by the asymmetry or
   catalyst gates. **PLTR** carries over again, still RESEARCH tier
   (reward:risk 2.7:1), with its unresolved government/defense
   business-activity question from prior runs unchanged.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continuing to build the ETH treasury —
5.96M ETH held as of Sept 13 (~$15.8B combined crypto/cash/securities), plus
staked ETH leadership (5.07M ETH staked, ~$334M annualized staking revenue
projected). Cantor Fitzgerald raised its price target to $63.60 from $30.60
on Sept 10. Stock up +68.4% since the $15.43 cost basis.
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16/)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check still disagrees with the recorded status — see
Action Flag #1, now five weeks unresolved. The holding file is still
missing PM-grade fields (`thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, `pre_mortem` all null/empty), so there is still no written
thesis to weigh the compliance question against. Financial profile shows a
~$83.6M quarterly net loss against ~$46.5M revenue — the business runs on
treasury/staking economics, not operating profit, reinforcing the
"financial vehicle" question the ratio pre-check is raising.

**Verdict: HOLD (no technical rule fired) — the compliance question is
still the thing to resolve first, and it's now the oldest open item in the book.**

### NOW — ServiceNow, Inc
**Case to keep:** Guidance reaffirmed/raised into the Oct 28 print — Q3
subscription revenue guided to +20.5% YoY, FY2026 subscription revenue
raised to +22.5% YoY growth, AI ACV tracking toward 30% of ACV by 2030.
Momentum has turned positive (6m momentum +12.3%, vs. -5.3% last run). DCF
gap to price is modest (-11.3%).
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the Shariah screen
is now stale (Action Flag #2); the trailing stop is the tightest it's been —
price sits only ~3.9% above the $130.12 chandelier level, vs. ~18% buffer
last run, so a moderate pullback would put the technical SELL trigger in
play.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (still `compliant`), so it stays silent
  despite the ratio-precheck fail persisting for a second run. Nothing in
  the automated pipeline will re-flag this on its own.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); NOW's price buffer
  above its chandelier level has compressed sharply this run (~3.9%), worth
  watching even though the rule is exempted.
- **VOL_THROTTLE -> BMNR**: fired this run (ATR 7.35% > 6% threshold) — a
  new portfolio note vs. last run, where none surfaced.

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
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 79 files in `setups/` are still
`draft` or reference material).

## Draft & planned setups — 50 leads, 14 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank, `discover_top_n` unchanged at 50). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
without one (14 new: AMKR, ORCL-PD, HBM, TECK, NUE, CORZ, DDOG, PR, NTR,
NTNX, TS, BLSH, XOM, APA; 36 existing cards left unchanged). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.**

33 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| MSFT | LEAD | existing | 10.0:1 | earnings 2026-10-28 | 38 |
| GDDY | LEAD | existing | 13.0:1 | earnings 2026-10-29 | 39 |
| LRCX | LEAD | existing | 20.0:1 | earnings 2026-10-21 | 31 |
| CDE | LEAD | existing | 11.8:1 | earnings 2026-10-28 | 38 |
| AGI | LEAD | existing | 13.2:1 | earnings 2026-10-28 | 38 |
| APH | LEAD | existing | 9.1:1 | earnings 2026-10-28 | 38 |
| IONQ | LEAD | existing | 18.5:1 | earnings 2026-11-04 | 45 |
| AMKR | LEAD | new | 9.6:1 | earnings 2026-10-26 | 36 |
| WDC | LEAD | existing | 14.9:1 | earnings 2026-11-05 | 46 |
| KLIC | LEAD | existing | 20.0:1 | earnings 2026-11-18 | 59 |

(Full 50-row pool, including the remaining 23 LEAD-tier and 17 RESEARCH-tier
rows, is in `leads.md` — not reproduced in full here to keep this report
readable.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again, still RESEARCH tier, with its unresolved
  government/defense business-activity question from prior runs. Nothing
  new to add.
- **CDE, AGI, EGO, IAG** — the recurring precious-metals/mining cluster,
  all LEAD tier again this run; mining-royalty financing structures raised
  the same open question in earlier runs. Still worth a real screen before
  spending review time on any of these cards. (NUE, TECK — steel/base-metals
  mining — are new entrants to the same broad sector this run.)
- **17 RESEARCH-tier leads** capped mainly by the asymmetry gate (several,
  like AMD, DINO, DELL, sit at reward:risk well under 1:1 on the discovery-
  stage entry/target/stop) — full list in `leads.md`.

## Follow-ups (priority order)

1. **[Urgent — carried over, now 2 runs open] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has now disagreed with the recorded
   "compliant" status for two consecutive runs, on a position that has
   grown from +33.1% to +68.4% and from 18.6% to 21.5% of the book in that
   time. The automated pipeline will NOT re-surface this on its own.
2. **[Urgent — NEW this run] NOW Shariah re-screen**: recorded screen is
   now >100 days old (screened 2026-06-09); `recommend.py` flips to REVIEW.
   This is the account's largest position (78.5%) — re-screen before the
   next report.
3. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, nine weeks after the position was
   opened.
4. **[Time-boxed] NOW earnings 2026-10-28** — 38 days out, now inside the
   catalyst horizon; update the holding file's `catalyst.date` from `null`
   to `2026-10-28` and watch the trailing-stop buffer (currently only ~3.9%).
5. **[Housekeeping] 14 new DRAFT setup cards** added this run (79 files
   total in `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [BMNR Stock Slides As BitMine Immersion Momentum Stalls — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_16/)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [NOW Earnings Dates, Upcoming and Historical — MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)
