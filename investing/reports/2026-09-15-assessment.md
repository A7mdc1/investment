# Portfolio Assessment — 2026-09-15

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (21 new DRAFT setup cards auto-filled; 42 existing
cards left unchanged — 63 cards total in `setups/` before this run's
auto-fills brought the total to 85) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run separately — still no `transactions.csv` (discipline
guard stays dormant). Web research this run turned up a **material new
compliance signal on BMNR — see Action Flag #1, this is the most important
thing in this report.**

**Since the last report (2026-08-19):** no trades recorded. Both positions
are unchanged in size; BMNR is up further (+56.6% vs. +33.1% last run), NOW
is up further (+27.1% vs. +11.8% last run).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.15/24.17**,
up **+56.6%** vs. the $15.43 cost basis. **See Action Flag #1 — a named
Shariah screener (Musaffa) now shows this holding as NOT HALAL, directly
contradicting the recorded "compliant" status. This is an escalation from
last run's internal ratio-precheck disagreement.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -9.9:1 (DCF-derived target sits below the stop; DCF caveat still applies, see below) |
| Shariah (recorded, holding file) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from last run) |
| Shariah (Musaffa, live, Sep 2026) | **NOT HALAL** — "does not pass Musaffa's business and financial screening criteria" (specific failed criterion not disclosed on the page) |
| Shariah (Zoya, live) | Compliant — cites minimal interest income (~0.02% of revenue); page content looked partly templated/stale |
| Portfolio note (vol throttle, new this run) | BMNR ATR 7.16% — size down per vol throttle |
| Trailing stop (chandelier) | $21.7788 — price ~10.9% above it |
| 6m momentum (skip last month) | -22.7% (deteriorated from -13.1% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field only; it is silent on both the mechanical ratio fail and the Musaffa flip |
| What changes verdict | A resolved Zoya/Musaffa re-screen; right now the two named services **disagree with each other**, not just with the recorded status |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$146.06/146.14**, **+27.1%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.6:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); mechanical ratio pre-check also clean this run (debt ratio 1.6%, liquid ratio 4.2%) |
| DCF intrinsic value | $120.12 vs. $146.05 price -> -17.8% (gap widened from -6.6% last run as price ran ahead) |
| Trailing stop (chandelier) | $129.5736 — price is ~12.7% above it |
| 6m momentum (skip last month) | +7.9% (turned positive from -5.3% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.17 | 10 | $15.43 | $241.70 | +56.6% | 19.1% |
| NOW | $146.14 | 7 | $114.97 | $1,022.98 | +27.1% | 80.9% |

**Total value: $1,264.68** | Cost: $959.09 | **Total return: ~+31.9%** (+$305.59 unrealised)

## Action flags (priority order)

1. **[Mandate — ESCALATED this run] BMNR: Musaffa now shows NOT HALAL,
   directly contradicting the recorded "compliant" broker-app status.**
   Live web research this run found Musaffa's BMNR page (dated "Last Updated:
   September 2026") now states the name "does not pass Musaffa's business and
   financial screening criteria," without disclosing which specific ratio or
   business test failed. Zoya's live page still shows compliant, citing
   minimal interest income — but its content looked partly templated and may
   not be fully current. **The two named screening services now disagree with
   each other**, not just with your recorded status. This sits on top of last
   run's finding, which still stands unchanged: this repo's own mechanical
   ratio pre-check independently fails BMNR on the same `Capital Markets`
   classification (Ethereum-treasury business, ~98% of revenue from ETH
   staking, ~$15.8B total crypto/cash/marketable-securities treasury, a
   buyback plus scheduled preferred dividends — a profile a business-activity
   screen is built to catch). Per this repo's own Gate 1 ("Shariah knockout —
   non-compliant / ratio-or-business flag -> AVOID/SELL, absolute"), a
   confirmed fail would be a hard SELL, independent of the +56.6% return.
   `recommend.py`'s "would buy today" check only reads the recorded field and
   is silent on all three of: the mechanical pre-check fail, the Musaffa
   flip, and the Musaffa/Zoya disagreement. **This is now a two-month-old
   open question (first flagged 2026-08-19) that has gotten materially worse,
   not better — resolve it directly with your own Zoya/Musaffa accounts
   before treating "compliant" as settled, and before adding to this
   position.**
2. **[Housekeeping — unresolved from last run] BMNR holding file is still
   missing PM-grade fields** — `thesis_one_liner`, `variant_view`,
   `initial_stop`, `target_price`, `pre_mortem` are all still null/empty,
   over two months after the position was opened (2026-07-07).
3. **[Technical / BMNR] Vol throttle fired** — ATR 7.16%, above the
   `vol_throttle_atr_pct: 6` knob; `verdict.py` flags this as a size-down note
   (not a verdict change). 6m momentum has also turned more negative (-22.7%,
   from -13.1% last run) even as the price is up big off cost — a volatile,
   round-tripping name.
4. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add. DCF gap widened to -17.8% (from -6.6%) as price outran the model.
5. **[Catalyst / NOW]** Earnings confirmed for **2026-10-28** (43 days out,
   inside the 60-day horizon) — aggregator-sourced (TipRanks), not verified
   against ServiceNow's own IR page directly this run. AI ACV crossed $1B and
   the 2026 target was raised to **$1.5B** (announced 2026-09-09 at Citi's
   TMT conference); Needham raised its target to $155, BTIG to $170, BMO to
   $150 — all post-split-adjusted. No integration-progress KPIs found for
   Armis specifically this window (data gap, not a negative signal).
6. **[Discovery] 50 leads this run, 18 clearing to LEAD tier** (up from 9
   last run) — see the setups table below. **PLTR** carries over again with
   its unresolved government/defense business-activity question. The
   recurring precious-metals/mining names (CDE, AGI, AR among this run's
   leads) still carry the same open mining-royalty-financing question raised
   in prior runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Treasury has grown to **5,956,378 ETH**
(~4.9% of ETH supply) plus 212 BTC, a $180M stake in Beast Industries, a $98M
stake in Eightco Holdings, and $549M cash/marketable securities — total
**$15.8B** as of a 2026-09-14 release, up from ~$11.4B in mid-August. ETH
itself rallied from ~$1,893 (Aug 16) to ~$2,500-2,513 (Sep 13-15), a roughly
one-third move that did much of the heavy lifting on returns this cycle. As
of an Aug 10 CoinDesk report, management is slowing ETH accumulation (nearing
its self-set 5%-of-supply target) and shifting capital toward buybacks
(19.1M shares repurchased since July 1). A Blockworks mNAV dashboard shows
the stock trading close to ~1.0x its treasury NAV recently — down from
historically higher premiums, i.e. not obviously overpriced against its
crypto holdings on that specific measure.
[PR Newswire — $15.8B holdings, Sep 14](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html) ·
[CoinDesk — buyback shift](https://www.coindesk.com/business/2026/08/10/bitmine-s-eth-buying-slows-as-tom-lee-s-firm-shifts-capital-to-share-buybacks) ·
[Blockworks — mNAV dashboard](https://blockworks.com/analytics/BMNR/bitmine-bmnr-treasury-holdings/bitmine-bmnr-basic-mnav)

**Case to flag (compliance, independent of the price/treasury story):** See
Action Flag #1 — Musaffa now shows NOT HALAL; the repo's own mechanical
pre-check independently fails it; only Zoya still shows compliant, on
content that looked partly stale. Separately, a December 2025 governance
episode (a 50B authorized-share increase, a director's board exit, a pending
CFO departure, and a shareholder-rights investigation by Purcell &
Lefkowitz) predates this reporting window and I found no update on its
resolution — noting it so it isn't mistaken for new, but it remains an open,
undated item worth a status check. No thesis-breaking news specific to the
past 30 days was found otherwise.
[Yahoo Finance — governance/dilution episode, Dec 2025](https://finance.yahoo.com/news/bitmine-immersion-technologies-bmnr-down-110945557.html)

**Verdict: HOLD (no technical rule fired) — but the compliance question,
now sharper than last run, is the thing to resolve first, not the price or
treasury story.**

### NOW — ServiceNow, Inc
**Case to keep:** No thesis-breaking news found since the last report; Q2
2026 results (pre-window, ~Jul 22) beat and *raised* full-year subscription
guidance, with cRPO growth steady around 21-21.5% for five straight quarters.
AI ACV crossed $1B with the 2026 target raised to $1.5B (announced Sep 9);
security/risk products (including Armis) separately crossed $1B ACV.
Multiple sell-side targets moved up in September (Needham to $155, BTIG to
$170, BMO to $150), all comfortably above the current price, though these
are analyst opinions, not a promise of returns. DCF gap (-17.8%) is a
model-vs-price gap under stated assumptions, not a verdict.
[diginomica — Q2 2026 AI ACV](https://diginomica.com/servicenow-q2-2026-ai-acv-passes-1-billion-zavery-says-governance-opening-new-doors) ·
[Investing.com — Citi TMT transcript, Sep 9](https://www.investing.com/news/transcripts/servicenow-at-citis-2026-global-tmt-conference-ai-push-deepens-93CH-4894682)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; price has run well
ahead of the DCF model since last run (-6.6% -> -17.8% gap). Earnings land
2026-10-28 (43 days out, inside the catalyst horizon) — a real near-term
event this time, unlike last run's 72-day-out reading. No update found on
Armis integration progress metrics specifically (attach rate, cross-sell
ACV) — a data gap, not a negative.
[TipRanks — earnings date](https://www.tipranks.com/stocks/now/earnings) ·
[ServiceNow Newsroom — Autonomous Security & Risk launch](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-Autonomous-Security--Risk-integrating-Armis-and-Veza-to-govern-every-AI-agent-identity-and-connected-asset/default.aspx)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite the mechanical ratio-precheck fail AND the new Musaffa
  NOT HALAL flag. Nothing in the automated pipeline will re-flag this on its
  own until you update the recorded status — the follow-up is on you, and it
  has now been open two runs / two months.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **New this run: vol-throttle note -> BMNR** (ATR 7.16% > 6% knob):
  size-down signal, not a verdict change.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.17 | -97.0% (not a meaningful signal — cash-flow DCF does not fit a crypto-treasury business; see caveat below) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $146.05 | -17.8% | growth_5y 18%, terminal 3%, discount 10% |

**BMNR DCF caveat (unchanged from last run):** the model discounts operating
cash flow, which does not represent how a crypto-treasury company creates or
loses value (that's driven by ETH holdings, staking yield, and mNAV versus
treasury NAV — see the mNAV note above). Treat the -97.0% figure as a data
gap, not a valuation call.

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs** this run (expected — no card has been reviewed and
flipped to `status: planned` yet; all cards in `setups/` are still `draft`).

## Draft & planned setups — 50 leads, 21 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one (21 new cards this run:
AAPL, APA, BBY, BKR, BLSH, DDOG, DDS, EXPE, FLYW, FRO, HPE, NTAP, NTNX, NTR,
PR, SMCIP, SMTC, SNA, SOLV, TECK, TS — 85 cards now on disk). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.**

18 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| AGI | existing | 20.0:1 | earnings 2026-10-28 | 43 |
| DOCN | existing | 16.9:1 | earnings 2026-11-04 | 50 |
| CDE | existing | 15.3:1 | earnings 2026-10-28 | 43 |
| MU | existing | 14.2:1 | earnings 2026-09-30 | 15 |
| UTHR | existing | 11.8:1 | earnings 2026-10-28 | 43 |
| DDOG | new | 9.2:1 | earnings 2026-11-05 | 51 |
| TSLA | existing | 8.3:1 | earnings 2026-10-21 | 36 |
| CLS | existing | 8.1:1 | earnings 2026-10-26 | 41 |
| DLO | existing | 7.0:1 | earnings 2026-11-11 | 57 |
| BLSH | new | 6.0:1 | earnings 2026-11-12 | 58 |
| FLYW | new | 6.0:1 | earnings 2026-11-03 | 49 |
| GDDY | existing | 3.9:1 | earnings 2026-10-29 | 44 |
| MSFT | existing | 3.8:1 | earnings 2026-10-28 | 43 |
| PLTR | existing | 3.8:1 | earnings 2026-11-02 | 48 |
| GOOGL | existing | 4.7:1 | earnings 2026-10-28 | 43 |
| ARW | existing | 3.5:1 | earnings 2026-10-29 | 44 |
| AR | existing | 3.3:1 | earnings 2026-10-28 | 43 |
| TS | new | 3.1:1 | earnings 2026-11-04 | 50 |

Notably, **ADI, ZS, CRDO, ULTA, SNX** — LEAD tier last run — dropped to
RESEARCH this run (asymmetry compressed as their prices moved, and/or
earnings dates rolled past). **AA, CIEN, GWRE** (LEAD last run) no longer
appear in the top-50 pool at all.

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI** — the recurring precious-metals/mining-adjacent cluster
  flagged in prior runs (mining-royalty financing structures raised the same
  open question). Still worth a real screen before spending review time on
  any of these cards.
- **32 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — escalated this run] BMNR Shariah re-screen.** Musaffa now
   shows NOT HALAL; the repo's own mechanical ratio pre-check independently
   fails it; only Zoya (on possibly-stale content) shows compliant. Three
   sources now disagree with each other on a position worth 19.1% of the
   book with a +56.6% unrealized gain. This is the single highest-priority
   item in this report — resolve it directly, don't let the recorded
   "compliant" field stand by default.
2. **[Housekeeping — still open, 2nd run in a row] BMNR holding file is
   missing PM-grade fields** — `thesis_one_liner`, `variant_view`,
   `initial_stop`, `target_price`, `pre_mortem` are still null/empty, over
   two months after the position was opened.
3. **[Time-boxed] NOW earnings 2026-10-28** — 43 days out; now inside the
   catalyst horizon. Worth deciding ahead of time whether/how you'll react
   given the P/E is already rich and the DCF gap has widened.
4. **[Housekeeping] 21 new DRAFT setup cards** added this run (85 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens and Total Crypto and Total Cash Holdings of $15.8 Billion — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [Bitmine's ETH Buying Slows as Tom Lee's Firm Shifts Capital to Share Buybacks — CoinDesk](https://www.coindesk.com/business/2026/08/10/bitmine-s-eth-buying-slows-as-tom-lee-s-firm-shifts-capital-to-share-buybacks)
- [BMNR mNAV dashboard — Blockworks](https://blockworks.com/analytics/BMNR/bitmine-bmnr-treasury-holdings/bitmine-bmnr-basic-mnav)
- [BMNR — Musaffa](https://musaffa.com/stock/BMNR/)
- [BMNR — Zoya](https://zoya.finance/stocks/bmnr)
- [Bitmine Immersion Technologies (BMNR) Down 10% — governance/dilution episode, Dec 2025 — Yahoo Finance](https://finance.yahoo.com/news/bitmine-immersion-technologies-bmnr-down-110945557.html)
- [Bitmine Immersion Stock Rallies Friday — CLARITY Act sentiment — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/09/61744911/bitmine-immersion-stock-rallies-friday-whats-happening)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow Q2 2026: AI ACV Passes $1 Billion — diginomica](https://diginomica.com/servicenow-q2-2026-ai-acv-passes-1-billion-zavery-says-governance-opening-new-doors)
- [ServiceNow at Citi's 2026 Global TMT Conference transcript — Investing.com](https://www.investing.com/news/transcripts/servicenow-at-citis-2026-global-tmt-conference-ai-push-deepens-93CH-4894682)
- [ServiceNow launches Autonomous Security & Risk, integrating Armis and Veza — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-Autonomous-Security--Risk-integrating-Armis-and-Veza-to-govern-every-AI-agent-identity-and-connected-asset/default.aspx)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [ServiceNow shares rise — price target roundup — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-shares-rise-2-6-110446134.html)
