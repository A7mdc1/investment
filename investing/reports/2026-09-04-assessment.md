# Portfolio Assessment — 2026-09-04

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (14 new DRAFT setup cards auto-filled: AAPL, APA,
ASND, BLSH, FLYW, FRO, HBM, NTNX, PR, SMTC, SNA, TECK, TS, XOM; 36 existing
cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still no `transactions.csv` (discipline guard stays
dormant).

**Since the last report (2026-08-19):** no trades recorded. Both positions
have moved meaningfully: BMNR is up sharply (now +62.5% vs. cost, was
+33.1%), NOW has pulled back from its recent high but is still up +22.8%
(was +11.8% but priced off a different snapshot). The open compliance
question on BMNR flagged last run is **unchanged and still unresolved.**

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.08**, up
**+62.5%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still FAILS — same open question as last run,
now with a larger unrealized gain riding on it.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -9.1:1 (DCF-derived target sits far below the stop; DCF does not fit this business — see caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails screen (unchanged from 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $25.08 price -> -97.1% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $22.3972 — price ~12.0% above it |
| 6m momentum (skip last month) | -3.1% |
| Portfolio note | ATR 6.0% -> vol-throttle flag (size down) |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$141.23**, **+22.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $141.23 price -> -14.9% (price richer to the model than last run's -6.6%) |
| Trailing stop (chandelier) | $130.0182 — price is ~8.6% above it |
| 6m momentum (skip last month) | -5.6% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.08 | 10 | $15.43 | $250.80 | +62.5% | 20.2% |
| NOW | $141.23 | 7 | $114.97 | $988.44 | +22.8% | 79.8% |

**Total value: $1,239.24** | Cost: $959.09 | **Total return: ~+29.2%** (+$280.15 unrealised)

Total value is up from $1,105.51 (2026-08-19) to $1,239.24, entirely from
price appreciation — no new capital or trades logged. NOW's weight edged down
slightly (81.4% -> 79.8%) simply because BMNR's percentage gain outpaced it
this cycle, not from any rebalancing action.

## Action flags (priority order)

1. **[Mandate — still open, unchanged] BMNR's mechanical Shariah ratio
   pre-check FAILS**, same flag as 2026-08-19: `industry 'Capital Markets'
   matches 'capital markets' — core business fails screen`. The recorded
   status is still `compliant` (broker app, screened 2026-07-07 — over two
   months old now, though not yet flagged `stale` by the script's threshold).
   Nothing has changed to resolve this since last run, and the position has
   grown from +33.1% to +62.5% while the question sits open. Per this repo's
   Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL, independent
   of the return. `recommend.py`'s "would buy today" check still only reads
   the recorded field and stays silent on this. **This is now the second
   consecutive run flagging the same unresolved question — recommend
   resolving it in Zoya/Musaffa before the position grows further.**
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still
   holds. DCF gap widened to -14.9% (was -6.6%) as price ran up from $128.63
   to $141.23. Do not add.
3. **[DCF caveat / BMNR]** The -97.1% DCF "downside" remains not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business valued on
   ETH holdings and staking yield, not discounted operating cash flow. Treat
   as a data gap, not a valuation call.
4. **[Catalyst / NOW]** No confirmed earnings date in the holding file; live
   research this run puts the next print at **~2026-11-04** (61 days out —
   just outside the 60-day catalyst horizon). Q2 FY26 results (reported
   2026-07-22) beat estimates (EPS $0.90 vs. $0.76 est.) with subscription
   revenue up 24.5% YoY. Management appears at the Citi Global TMT
   Conference and Goldman Sachs Communacopia Tech Conference on 2026-09-09 —
   a soft catalyst window worth watching for guidance commentary, though
   not a binary event.
5. **[Discovery] 50 leads this run, 20 clear to LEAD tier** (up sharply from
   9 last run) — the strongest discovery pool since the 08-19 run raised
   `discover_top_n` to 50. 14 fresh DRAFT setup cards were auto-filled for
   leads that didn't already have one; 36 existing cards were left as-is.
   PLTR carries over again as a LEAD with its unresolved government/defense
   business-activity question from prior runs — still open, nothing new.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continuing an aggressive ETH accumulation
program — reported total holdings of ~$15.6B as of 2026-08-30, and an
extended 65-week ETH-buying run that added 53,501 ETH in the most recent
week alone. Stock up +62.5% since the $15.43 cost basis, nearly double the
gain reported last cycle (+33.1%); recorded compliance status is still
"compliant."
[CNBC](https://www.cnbc.com/quotes/BMNR) ·
[MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/BMNR/news)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status again this run
— identical flag to 2026-08-19, meaning the question has now persisted
across at least two runs without resolution. The holding file is still
missing `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
and `pre_mortem` — there remains no PM-grade record to weigh the compliance
question against beyond the mechanical LOW-conviction default, seven weeks
after the position was opened.

**Verdict: HOLD (no technical rule fired) — the compliance question is still
the thing to resolve first, and it is now the priority action item two runs
running.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 results beat estimates (EPS $0.90 vs. $0.76 est.,
subscription revenue +24.5% YoY to $3,877M) reported 2026-07-22. Executives
present at two major investor conferences on 2026-09-09 (Citi Global TMT,
Goldman Sachs Communacopia), which could surface incremental guidance
commentary ahead of the Q3 print. DCF still shows the model has not caught
up to the rally.
[ServiceNow Q2 2026 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx) ·
[Nasdaq earnings](https://www.nasdaq.com/market-activity/stocks/now/earnings)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; DCF gap to
intrinsic value widened to -14.9% (from -6.6% last run) as price outran the
model's growth assumptions; 6m momentum still negative (-5.6%) despite the
rally; next earnings not confirmed in-file but estimated ~2026-11-04 (just
outside the 60-day catalyst window as of this report).
[Nasdaq earnings](https://www.nasdaq.com/market-activity/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite this run's ratio-precheck fail — same gap as last run. This
  is now the second run in a row where the automated pipeline will not
  re-flag this on its own; the follow-up remains on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE -> BMNR**: fired this run (`portfolio_notes`) — ATR 6.0% is
  at the `vol_throttle_atr_pct` threshold; a de-risk note, not an action.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.08 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $141.23 | -14.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 78 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 14 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank, unchanged `discover_top_n: 50`). `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
without one (14 new cards: AAPL, APA, ASND, BLSH, FLYW, FRO, HBM, NTNX, PR,
SMTC, SNA, TECK, TS, XOM; 36 existing cards left unchanged). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.**

20 of the 50 leads clear to LEAD tier this run (up sharply from 9 last run —
the rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | R:R | Has card | Catalyst |
|---|---|---|---|
| LRCX | 18.3:1 | existing | earnings 2026-10-21 |
| CLS | 16.9:1 | existing | earnings 2026-10-26 |
| TSLA | 14.6:1 | existing | earnings 2026-10-21 |
| AA | 10.7:1 | existing | earnings 2026-10-15 |
| HAS | 10.2:1 | existing | earnings 2026-10-22 |
| EGO | 7.6:1 | existing | earnings 2026-10-29 |
| ALAB | 7.3:1 | existing | earnings 2026-11-03 |
| AMD | 7.0:1 | existing | earnings 2026-11-03 |
| XOM | 6.9:1 | new | earnings 2026-10-30 |
| AGI | 6.1:1 | existing | earnings 2026-10-28 |
| GDDY | 5.9:1 | existing | earnings 2026-10-29 |
| NET | 5.9:1 | existing | earnings 2026-10-29 |
| FOX | 5.5:1 | existing | earnings 2026-10-29 |
| HBM | 5.3:1 | new | earnings 2026-10-29 |
| AVT | 4.5:1 | existing | earnings 2026-10-28 |
| IAG | 3.9:1 | existing | earnings 2026-11-03 |
| MSFT | 3.6:1 | existing | earnings 2026-10-28 |
| SMCI | 3.3:1 | existing | earnings 2026-11-03 |
| SIMO | 3.0:1 | existing | earnings 2026-10-29 |
| PLTR | 3.0:1 | existing | earnings 2026-11-02 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **AGI, IAG, EGO** — the recurring precious-metals-mining cluster remains
  in the LEAD tier; mining-royalty financing structures raised the same open
  question in earlier runs. Still worth a real screen before spending review
  time on any of these cards.
- **ULTA, ADI, ZS, CIEN, GWRE, SNX, CRDO** — LEAD-tier in the 2026-08-19
  report, now either RESEARCH-tier (ULTA fell to 2.8:1 R:R as its earnings
  catalyst passed and rolled forward to 2026-12-03; ZS, SNX, CRDO still
  present but capped by asymmetry/catalyst gates) or dropped out of this
  run's screened pool entirely (ADI, CIEN, GWRE) — the discovery pool
  resamples its screen source each run, so absence here doesn't mean a
  negative signal, just that they weren't re-pulled today.
- **30 RESEARCH-tier leads** this run — full list in `leads.md`; not
  reproduced here in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now flagged 2 runs in a row] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status on the business-activity question in both the 2026-08-19 and
   2026-09-04 runs. This is the largest compliance question in the book
   (20.2% weight, +62.5% return, up from +33.1% two weeks ago) and the
   automated pipeline will NOT re-surface it on its own.
2. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, seven weeks after
   the position was opened.
3. **[Time-boxed] NOW earnings ~2026-11-04** (estimated, unconfirmed in-file)
   — 61 days out; investor-conference appearances 2026-09-09 are a nearer
   soft catalyst to watch for incremental guidance commentary.
4. **[Housekeeping] 14 new DRAFT setup cards** added this run (78 total in
   `setups/`); none are `planned`. Review at your own pace — the 20 LEAD-tier
   names above are the highest-signal place to start.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BMNR: BitMine Immersion Technologies, Inc. — CNBC](https://www.cnbc.com/quotes/BMNR)
- [BMNR News — MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/BMNR/news)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow, Inc. Common Stock (NOW) Earnings Report Dates & Earnings Forecasts — Nasdaq](https://www.nasdaq.com/market-activity/stocks/now/earnings)
