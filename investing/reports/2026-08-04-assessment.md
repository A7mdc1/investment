# Portfolio Assessment — 2026-08-04

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data; pool widened to top-50 by max-benefit rank per
the current `rules.md` knob, up from 20 last run) → `scaffold.py --all-leads`
(31 new DRAFT setup cards auto-filled for names without one; 19 existing cards
left unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still 0 closed trades (no `transactions.csv` yet — the
discipline guard stays dormant until you start logging via `/apply-trade`).
**22 days since the last assessment (2026-07-13)** — longer than the usual
weekly cadence; both holdings changed in that gap (FIG sold, BMNR bought,
same day as the last report).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.74**, up
**+15.0%** vs. the $15.43 cost basis (opened 2026-07-13).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-5.66:1** (DCF-implied downside dominates; skew argues against adding) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but the mechanical ratio pre-check flags a conflict** (see below) |
| DCF intrinsic value | $0.72 vs. $17.74 price -> **-96% "upside"** — see caveat below, this number is not meaningful for this business |
| Trailing stop (chandelier) | $14.735 — price ~20.4% above it |
| 6m momentum (skip last month) | -31.8% |
| Portfolio note | ATR 6.74% — vol-throttle note; ATR-based sizing already reflects this if you add |
| Would buy today? | Mechanically "yes" per recommend.py's technical gate — but conviction is flagged LOW and the DCF/reward:risk numbers argue the opposite; read this as the tool's gates disagreeing, not a signal to add |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$116.06**, **+0.95%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.24:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.12** vs. $116.06 price -> **+3.5% upside** to the model |
| Trailing stop (chandelier) | $99.5523 — price is $16.51 above it |
| 6m momentum (skip last month) | -8.5% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.74 | 10 | $15.43 | $177.40 | +15.0% | 17.9% |
| NOW | $116.06 | 7 | $114.97 | $812.42 | +0.9% | 82.1% |

**Total value: $989.82** | Cost: $959.09 | **Total return: ~+3.2%** (+$30.73 unrealised)

NOW is now 82% of the book — BMNR's small share size (10 shares, ~$154 cost)
keeps it a minority position even after a 15% gain. This is a concentrated
2-name portfolio; the 4-name concentration-rule floor stays muted.

## Action flags (priority order)

1. **[Mandate — new, needs your attention] BMNR Shariah pre-check conflict.**
   The broker app records BMNR as `compliant` (screened 2026-07-07), but
   `shariah.py`'s mechanical ratio pre-check flags it: *"industry 'Capital
   Markets' matches 'capital markets' — core business fails screen."*
   Independent of that industry-keyword match, BMNR's actual business is an
   **Ethereum treasury + staking operation**: as of 2026-08-02 it holds
   ~5.80M ETH (~$10.75B) and has **~4.92M ETH actively staked (~$9.2B)**,
   earning an ongoing yield (~$291M/yr projected) through its MAVAN staking
   platform. Staking-derived yield on a crypto asset is a substantively
   different compliance question than a simple business-activity screen, and
   it's one the broker app's "compliant" tag may not have evaluated. **This
   is worth a real Zoya/Musaffa re-screen before adding to the position** —
   the pre-check disagreeing with the recorded status is exactly the case
   `shariah.py` exists to surface. [The Block](https://www.theblock.co/treasuries/bmnr) ·
   [PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-8-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302840749.html)
2. **[Risk / BMNR] Heavy shareholder dilution.** Diluted shares outstanding
   went from ~24.5M (FY2025) to ~454.6M in Q1 2026 — the ETH-holdings growth
   is being funded largely through equity issuance (ATM-style raises), the
   same playbook as other crypto-treasury vehicles. Per-share NAV growth is
   what matters here, not headline ETH-holdings growth; worth tracking
   whether ETH-per-share is actually compounding or just gross ETH.
3. **[DCF / BMNR — caveat, not a sell signal] The -96% DCF read is not a
   meaningful number for this business.** `dcf.py` used generic default
   assumptions (5% growth, 2.5% terminal, 10% discount) because BMNR's
   holding file has no `dcf:` block — a discounted-cash-flow model doesn't
   fit a company whose value is mark-to-market crypto holdings plus staking
   yield, not operating cash flow. Treat this line as a data gap, not a
   valuation call; if you want a real read on BMNR, an ETH-holdings-per-share
   vs. market-cap (mNAV) comparison would be the honest framework, not DCF.
4. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
5. **[Catalyst / NOW — stale field] Q2 FY2026 earnings already happened
   (2026-07-22)** — the holding's `catalyst.date` front-matter is still
   `null`; it should be updated. Results: EPS $0.90 vs. $0.76 est. (+18.4%),
   subscription revenue $3.877B (+24.5% y/y), ServiceNow AI crossed $1B ACV,
   cRPO $13.20B (+21%), and FY2026 subscription guidance was **raised** to
   $15.76-15.78B (~22.5% growth). Next catalyst: **Q3 FY2026 earnings, 2026-10-28**
   (85 days out — past `catalyst_horizon_days`; not dead money yet, the just-passed
   print was itself the catalyst and results were strong).
   [ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx) ·
   [GuruFocus](https://www.gurufocus.com/news/8973045/servicenow-now-reports-strong-q2-earnings-boosts-revenue-outlook)
6. **[Housekeeping] Discovery pool widened 20 -> 50 leads** this run (per an
   updated `rules.md` knob) — the leads.md ticker overlap with last run is
   low mostly because of pool size, not a change in what's attractive; see
   the leads table below.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** Up 15% since the 2026-07-13 entry; the underlying ETH
treasury has grown from 5.62M to 5.80M ETH and total crypto/cash holdings
from ~$10.4B to ~$11.3B+ over the past month; the new MAVAN staking platform
adds a yield stream (~$291M/yr projected) on top of the price-appreciation
bet, and Bitmine remains the #1 Ethereum treasury / #2 global crypto
treasury by holdings. [PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-8-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302840749.html)

**Case to review closely (independent of price):** the Shariah pre-check
conflict above is the real open question, not the chart — a broker-app
"compliant" tag on a business whose core activity is holding + staking a
cryptoasset for yield deserves the actual Zoya/Musaffa screen the holding's
own thesis note says is still outstanding ("NEW position — screen compliance
... before adding more"). Separately, the ~19x dilution in diluted shares
outstanding over the past year means gross ETH-holdings growth overstates
per-share value creation — the number to actually track is ETH-per-share,
not ETH-total. DCF is not a usable framework here (see flag #3); if you want
a real valuation anchor, compare price to an mNAV (market cap ÷ ETH holdings
value) instead.

**Verdict: HOLD** (no rule fired) — the position is small (17.9% of a
2-name book) and nothing here is a SELL trigger, but the compliance question
is the one thing worth resolving before it grows larger as a share of the book.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 print (2026-07-22) beat cleanly on both lines —
EPS $0.90 vs. $0.76 est., subscription revenue +24.5% y/y — and management
raised full-year subscription guidance to ~22.5% growth. ServiceNow AI
crossed $1B in annual contract value, and cRPO (a forward-revenue proxy)
grew 21% to $13.20B. DCF still shows a modest (+3.5%) upside to intrinsic
value at the recorded assumptions. Price is comfortably above the chandelier
trailing stop ($116.06 vs. $99.55).
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to trim / watch closely:** P/E ~119 (recorded) still triggers
VALUATION_RICH — priced for continued high growth, so any deceleration would
hit hard. 6m momentum is -8.5% (mildly negative but improved vs. the -27.5%
seen last run — the post-earnings pop helped). Next hard catalyst is 85 days
out (Q3 earnings, 2026-10-28); nothing thesis-breaking surfaced in this
round's research.

**Verdict: HOLD** (VALUATION_RICH — hold, don't add).

## Suggested actions (from YOUR rules, rules.md)

- **DEFAULT (no rule fired) -> BMNR**: HOLD. No mechanical trigger, but see
  Action flags #1-#3 — this is a policy/data-quality question, not a price rule.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **VOL_THROTTLE note -> BMNR**: ATR 6.74% — informational; size any add
  down accordingly per `risk_per_trade_pct`.
- **TRAIL_STOP -> both**: does NOT fire; both positions sit well above their
  computed chandelier stops (BMNR $17.74 vs. $14.735; NOW $116.06 vs. $99.5523).
- **DRAWDOWN_REVIEW not firing -> either**: both holdings are in gains, well
  inside the 20% threshold.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $17.74 | -96.0% | growth_5y 5%, terminal 2.5%, discount 10% (**generic defaults — no `dcf:` block on the holding; not a meaningful model for a crypto-treasury balance sheet, see flag #3**) |
| NOW | $120.12 | $116.06 | +3.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** — expected, since no setup card has been
reviewed and flipped to `status: planned` yet (all 63 cards in `setups/` are
still machine-filled `draft`).

## Draft & planned setups — 50 leads, 31 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens); the pool size
knob (`discover_top_n`) was widened from 20 to 50 since the last run, so most
of the ticker turnover below reflects that widening, not a shift in what
looks attractive. `scaffold.py --all-leads` filled **31 new DRAFT cards**
(19 already existed and were left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| ALAB | LEAD | existing | 7.8:1 | earnings 2026-08-04 | 0 |
| CF | LEAD | existing | 10.4:1 | earnings 2026-08-05 | 1 |
| DUOL | LEAD | existing | 8.1:1 | earnings 2026-08-05 | 1 |
| TTMI | LEAD | new | 8.8:1 | earnings 2026-08-05 | 1 |
| PDFS | LEAD | new | 7.1:1 | earnings 2026-08-06 | 2 |
| CIEN | LEAD | new | 9.6:1 | earnings 2026-09-09 | 36 |
| FLYW | LEAD | new | 5.8:1 | earnings 2026-08-04 | 0 |
| CDE | LEAD | existing | 6.1:1 | earnings 2026-08-05 | 1 |
| LIF | LEAD | existing | 3.6:1 | earnings 2026-08-10 | 6 |
| PAAS | LEAD | new | 5.3:1 | earnings 2026-08-12 | 8 |
| GWRE | LEAD | new | 5.4:1 | earnings 2026-09-03 | 30 |
| SMCI | LEAD | new | 4.1:1 | earnings 2026-08-11 | 7 |
| ZS | LEAD | existing | 3.3:1 | earnings 2026-09-02 | 29 |
| ADI | LEAD | existing | 3.4:1 | earnings 2026-08-19 | 15 |
| MU | LEAD | existing | 3.5:1 | earnings 2026-09-23 | 50 |
| ULTA | LEAD | existing | 3.4:1 | earnings 2026-08-27 | 23 |

*(20 of 50 leads clear to LEAD; the remaining 30 are RESEARCH — capped mostly
by the asymmetry or catalyst-horizon gates. Full detail in `leads.md`.)*

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, CDE** — carried over from prior runs' flags (government/defense
  business-activity question for PLTR; mining/royalty financing structure
  questions for precious-metals names AU/CDE). Still open, still worth
  checking before spending review time on the cards.
- **AA, AGI (RESEARCH but reward:risk 12-20:1)** — very wide R:R usually
  means the stop is implausibly tight relative to the stock's actual
  volatility, an engineered-band artifact rather than a real edge; sanity-
  check the entry/stop math before trusting the ratio.
- **Gold/silver miner cluster (AEM, AU, CDE, KGC, PAAS, HBM)** — six names
  from the same commodity/business-activity family showed up this run; if
  more than one clears to planned, size the cluster as one correlated bet,
  not N independent ones (same correlation-note logic as the semiconductor
  cluster in `watchlist.md`).
- **New setup cards without earnings dates checked against BMNR/NOW** — none
  of this run's leads overlap the existing holdings' sectors closely enough
  to change the concentration read.

## Follow-ups (priority order)

1. **[New, top priority] BMNR Shariah re-screen** — the ratio pre-check
   flagged a conflict against the recorded "compliant" status; get the
   actual Zoya/Musaffa screen done, specifically evaluating the ETH-staking
   yield mechanism, not just the equity itself.
2. **[Housekeeping] NOW holding front-matter is stale** — `catalyst.date`
   still `null` despite the Q2 print having happened; update to reflect the
   2026-10-28 Q3 date, and consider filling in the still-empty
   `conviction` / `variant_view` / `initial_stop` / `target_price` /
   `invalidation` / `pre_mortem` fields per the PM schema (all `null` today).
3. **[Ongoing] BMNR dilution tracking** — check ETH-per-share (not just
   total ETH holdings) each cycle; heavy share issuance can make gross
   treasury growth look better than it is per-share.
4. **[Housekeeping] 31 new DRAFT setup cards** added this run (63 total in
   `setups/`); none are `planned`, none can reach BUY-CANDIDATE. Review at
   your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [BMNR Announces ETH Holdings Reach 5.8 Million Tokens, $11.3B Total — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-8-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302840749.html)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow (NOW) Reports Strong Q2 Earnings, Boosts Revenue Outlook — GuruFocus](https://www.gurufocus.com/news/8973045/servicenow-now-reports-strong-q2-earnings-boosts-revenue-outlook)
- [Bitmine Immersion Technologies (BMNR) Shares Outstanding (Diluted Average) — Business Quant](https://businessquant.com/metrics/bmnr/shares-outstanding-diluted-average)
