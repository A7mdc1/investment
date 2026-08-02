# Portfolio Assessment — 2026-08-02

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check, neither a fatwa — verify independently
in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank, per the
widened `discover_top_n: 50` knob) → `scaffold.py --all-leads` (31 new DRAFT
setup cards auto-filled; 19 existing cards left unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` run: still 0 closed trades logged
(`transactions.csv` doesn't exist yet — discipline guard stays dormant).
Since the last run (2026-07-13) the book changed: **FIG was sold** (closed
2026-07-13, +$54.95 realized, exiting the 7-run compliance flag) and **BMNR
was bought** (10 sh @ $15.43) — both recorded via `/apply-trade` per
`holdings/closed/fig-figma.md` and `holdings/bmnr.md`.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.28**, up
**+12.0%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.2:1 (DCF-implied skew argues against, not for, adding) |
| Shariah (recorded) | PASS — broker-app compliant, screened 2026-07-07, not stale |
| **Shariah (mechanical ratio pre-check)** | **FAIL — industry "Capital Markets" is on the hard business-activity knockout list** (see Action flag #1 below — this is new and needs your attention) |
| DCF intrinsic value | $0.72 vs. $17.28 price -> -95.8% *(caveat: a discounted-cash-flow model is a poor fit for a crypto-treasury balance-sheet play — BMNR's value is mark-to-market ETH holdings + staking yield, not a traditional FCF stream; treat this number as noise, not a real overvaluation signal)* |
| Trailing stop (chandelier) | $14.6136 — price ~15.4% above it |
| 6m momentum (skip last month) | -47.0% |
| Portfolio note | ATR 7.15% — above the 6% vol-throttle threshold; size down on any add |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW, and the compliance question below should be resolved before adding another share |
| What changes verdict | Shariah re-screen (either direction), or a thesis_broken flag |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$111.23**, **-3.25%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.7:1 (recommend.py can't self-assess without a stated variant view) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $111.23 price -> +8.0% upside to the model |
| Trailing stop (chandelier) | $98.4905 — price is $12.74 above it |
| 6m momentum (skip last month) | -9.4% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.28 | 10 | $15.43 | $172.80 | +12.0% | 18.2% |
| NOW | $111.23 | 7 | $114.97 | $778.61 | -3.3% | 81.8% |

**Total value: $951.41** | Cost: $959.09 | **Total return: ~-0.8%** (-$7.68 unrealised)

NOW beat Q2 FY2026 estimates on 2026-07-22 (subscription revenue +24.5%
y/y, non-GAAP operating margin ~29.5%, FY guidance raised) and popped
+6.1% on the print, but has since drifted back down near pre-earnings
levels — the stock traded $106.67-$112.39 on 2026-08-01, still ~42% below
its 52-week high, with the broader multiple-compression story (P/E ~119,
down ~42% over the past year) still the dominant driver over the earnings
beat itself.
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html) ·
[24/7 Wall St.](https://247wallst.com/investing/2026/07/30/servicenow-showing-signs-of-life-but-still-down-25-ytd-115-returns-coming-if-this-analyst-is-correct/)

BMNR disclosed combined crypto/cash/marketable-securities/"moonshot"
holdings of **$11.3B**, including **5.77M ETH** (one of the largest
corporate ETH treasuries), plus a $180M stake in Beast Industries and $69M
in Eightco; shares rose on a buyback and bullish ETH sentiment.
[Simply Wall St](https://simplywall.st/stocks/us/software/nyse-bmnr/bitmine-immersion-technologies/news/bitmine-immersion-technologies-bmnr-is-down-60-after-reveali) ·
[CoinGecko](https://www.coingecko.com/learn/what-is-bmnr-bitmine-ethereum-treasury-tom-lee)

## Action flags (priority order)

1. **[Mandate — NEW this run] BMNR mechanical Shariah ratio pre-check FAILS.**
   `shariah.py`'s business-activity knockout classifies BMNR's Yahoo industry
   as **"Capital Markets"** — on the same hard-fail list as banks, insurers,
   and asset managers — which directly contradicts the recorded broker-app
   "compliant" screen from 2026-07-07. This is *not* automatically a SELL
   (the recorded human screen still governs `compliance_gate` in `verdict.py`
   until you change it), but it's the same category of open question that
   sat unresolved on FIG for seven runs last cycle: BMNR's business model has
   shifted from immersion-cooling infrastructure toward an ETH treasury +
   staking strategy (staking yield is a form of return that Yahoo's
   classifier is reading as "capital markets" activity), which is exactly the
   kind of interest/investment-income structure a real Zoya/Musaffa screen
   needs to re-examine given the pivot. **Re-screen BMNR before adding to it
   or letting the position grow further as a share of the book.**
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Volatility / BMNR] ATR 7.15%** — above the 6% vol-throttle threshold;
   size down on any future add, independent of the compliance question above.
4. **[New leads this run, near-term catalysts]** Two SPUS-holding LEADs have
   earnings in the next 1-2 days: **PLTR** (2026-08-03, tomorrow) and
   **AMD** (2026-08-04) — both UNVERIFIED Shariah (ratio pre-check only,
   clean on the business-activity knockout for both). If either is on your
   radar, the window to research before the print is essentially gone.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** +12.0% since entry two weeks ago; the ETH-treasury pivot
is well-funded ($11.3B combined holdings, $482M cash/marketable securities
buffer) and the company just announced a share buyback plus a fiscal-year-end
change to align to calendar year, both read as a maturing capital-allocation
story rather than a distressed one. Recorded Shariah status is still
"compliant" per the broker app and not stale.

**Case to trim / re-underwrite:** the mechanical ratio pre-check disagrees
with the recorded screen on business-activity grounds (see Action flag #1) —
this is the same category of open question that made FIG a 7-run flag last
cycle, just caught one screen earlier this time. Momentum is deeply negative
(6m -47%, skipping the last month) even as the near-term price is up, and the
DCF model (built for a traditional operating business) is not a meaningful
signal here either way. `holdings/bmnr.md`'s thesis/risks/notes fields are
still blank — worth filling in now while the position is small.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 beat on both revenue and margin (subscription
revenue +24.5% y/y, non-GAAP operating margin ~29.5%, FY2026 subscription
guidance raised to $15.76-15.78B), AI ACV surpassed $1B, and DCF shows +8.0%
upside to intrinsic value ($120.12) at the recorded assumptions. Consensus
stays constructive — Bernstein reportedly lifted its target to $248 in late
July (~114% implied upside from then-current levels), and the average target
sits around $137.
[24/7 Wall St.](https://247wallst.com/investing/2026/07/30/servicenow-showing-signs-of-life-but-still-down-25-ytd-115-returns-coming-if-this-analyst-is-correct/)

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; despite the
earnings beat and the initial +6.1% pop, the stock has round-tripped back to
roughly pre-earnings levels (down -3.3% from cost, worse than last run's
-2.0%), and sits ~42% below its 52-week high with the stock down ~42% over
the trailing year — the multiple-compression story is still overwhelming the
fundamental beat. 6m momentum is -9.4% (improved from -27.5% last run, but
still negative).
[Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60398250/servicenow-stock-falls-friday-whats-going-on) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html)

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **VOL_THROTTLE fired -> BMNR**: ATR 7.15% > 6% threshold — size down on any add; informational, not a sell signal.
- **DRAWDOWN_REVIEW not firing -> NOW**: -3.3% vs. the 20% threshold.
- **DRAWDOWN_REVIEW not firing -> BMNR**: +12.0% (a gain, not a drawdown).
- **TRAIL_STOP -> both**: does NOT fire (`trade_type: core` on NOW exempts
  it; BMNR has no `trade_type` set — worth adding one so this rule actually
  applies going forward).
- **COMPLIANCE_GATE**: does not mechanically fire on BMNR (recorded status is
  still "compliant") — but see Action flag #1; this is a manual re-screen
  item, not something the tool will catch until you update the recorded
  status.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $17.28 | -95.8% *(model mismatch — see note above)* | growth_5y 5%, terminal 2.5%, discount 10% |
| NOW | $120.12 | $111.23 | +8.0% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — it only reads
`watchlist.md`, and no card has been reviewed and flipped to
`status: planned` yet). All new-idea surfacing this cycle comes from machine
discovery below instead.

## Draft & planned setups — 50 leads this run (widened pool), 31 fresh DRAFT cards

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, now
`discover_top_n: 50`) and wrote **`leads.md`**. `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (31
new: SFD, SMCI, GWRE, LLY, AEM, KGC, TS, AA, WDC, DELL, KEYS, BBY, ARW, NVDA,
NEM, P, AVGO, HST, DLO, FLYW, SNX, ESE, PDFS, CORZ, CLS, UTHR, HBM, BKR, APH,
STX, VLO; 19 existing left unchanged: LIF, PLTR, ADI, DUOL, AMD, PAY, SIMO,
TER, AU, ZS, ULTA, JNJ, ALAB, CNQ, GOOGL, MSFT, KLIC, AR, CF). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.** None can reach BUY-CANDIDATE until you review the card, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa.

The table below shows the **15 names that cleared LEAD status** (asymmetry +
catalyst-within-60-days gates both passed) this run, sorted by days to
catalyst — the other 35 are capped at RESEARCH (mostly the asymmetry gate:
reward:risk < 3.0, since the discovery-stage floor is stricter than the
swing floor) and are in `leads.md` in full if you want the complete pool.

| Ticker | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|
| PLTR | existing | 14.2:1 | earnings 2026-08-03 | 1 |
| AMD | existing | 4.6:1 | earnings 2026-08-04 | 2 |
| DUOL | existing | 5.5:1 | earnings 2026-08-05 | 3 |
| LLY | new | 5.5:1 | earnings 2026-08-05 | 3 |
| TS | new | 3.5:1 | earnings 2026-08-05 | 3 |
| LIF | existing | 8.7:1 | earnings 2026-08-10 | 8 |
| SFD | new | 11.9:1 | earnings 2026-08-11 | 9 |
| SMCI | new | 10.2:1 | earnings 2026-08-11 | 9 |
| KEYS | new | 3.7:1 | earnings 2026-08-18 | 16 |
| ADI | existing | 7.8:1 | earnings 2026-08-19 | 17 |
| NVDA | new | 4.0:1 | earnings 2026-08-26 | 24 |
| ULTA | existing | 3.8:1 | earnings 2026-08-27 | 25 |
| ZS | existing | 4.4:1 | earnings 2026-09-02 | 31 |
| GWRE | new | 11.9:1 | earnings 2026-09-03 | 32 |
| AVGO | new | 3.5:1 | earnings 2026-09-03 | 32 |

All 50 cleared the liquidity floor and a clean ratio pre-check (business
activity + debt/liquid ratios) — not a business-activity screen. Shariah
status on every card is `unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR (carried over)** — still has the open government/defense
  business-activity question flagged in prior runs; nothing new, still worth
  checking before spending review time on the card, especially with earnings
  tomorrow.
- **AU, AEM, KGC, NEM, HBM (precious-metals cluster, all RESEARCH this run)**
  — same mining/royalty financing-structure question as before; several
  showed up again this cycle (AU, AEM, KGC, NEM, HBM) — if you're
  considering any, they're correlated as one bet, same as the semiconductor
  cluster note already in `watchlist.md`.
- **PAY, ALAB, FLYW, HST, KLIC, UTHR, CF, ESE, PDFS, CNQ (RESEARCH, catalysts
  1-4 days out)** — capped by the asymmetry gate despite very near-term
  catalysts; not a business problem, just doesn't clear the discovery-stage
  R:R bar today. Worth a manual look if the mechanical R:R undersells a case
  you'd make yourself, since the window before the print is short.

## Follow-ups (priority order)

1. **[Mandate — new] BMNR Shariah re-screen** — the mechanical business-
   activity pre-check now disagrees with the recorded "compliant" status;
   re-verify in Zoya/Musaffa given the treasury/staking pivot before adding
   to the position.
2. **[Housekeeping] BMNR holding file** — `thesis`, `risks`, `notes`, and
   `trade_type` are all still blank in `holdings/bmnr.md`; filling these in
   also lets the TRAIL_STOP rule apply if `trade_type` is set to something
   other than `core`.
3. **[Time-boxed] PLTR / AMD earnings** — 2026-08-03 and 2026-08-04,
   respectively; both are LEADs (not holdings), but the research window is
   essentially closed.
4. **[Housekeeping] 31 new DRAFT setup cards** added this run (50 total
   candidates in `leads.md`); none are `planned`, none can reach
   BUY-CANDIDATE. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Is Down 6.0% After Revealing Massive ETH Treasury And Index Inclusion — Simply Wall St News](https://simplywall.st/stocks/us/software/nyse-bmnr/bitmine-immersion-technologies/news/bitmine-immersion-technologies-bmnr-is-down-60-after-reveali)
- [BitMine Immersion Technologies (BMNR) – Ethereum's Largest Treasury Company — CoinGecko](https://www.coingecko.com/learn/what-is-bmnr-bitmine-ethereum-treasury-tom-lee)
- [ServiceNow (NOW) Q2 Earnings and Revenues Top Estimates — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html)
- [ServiceNow Showing Signs of Life But Still Down 25% YTD — 24/7 Wall St.](https://247wallst.com/investing/2026/07/30/servicenow-showing-signs-of-life-but-still-down-25-ytd-115-returns-coming-if-this-analyst-is-correct/)
- [ServiceNow Stock Falls Friday: What's Going On? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/07/60398250/servicenow-stock-falls-friday-whats-going-on)
