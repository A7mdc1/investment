# Portfolio Assessment — 2026-09-05

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (16 new DRAFT setup cards auto-filled — NTNX, XOM,
HBM, NTAP, AAPL, BLSH, TECK, TS, FLYW, FRO, APA, PR, SMTC, BBY, ASND, SNA;
34 existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run separately — still no `transactions.csv`
(discipline guard stays dormant).

**Since the last report (2026-08-19):** no trades recorded. Both positions
are unchanged in size; this run's focus is the still-unresolved BMNR
compliance question (now checked directly against fresh web research — see
Action Flag #1) and a NOW earnings date that has now rolled inside the
60-day catalyst window.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$24.97**, up
**+61.8%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — see Action Flag #1.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -9.4:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (same flag as last run) |
| DCF intrinsic value | $0.72 vs. $24.97 price -> -97.1% (not a meaningful signal — DCF does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.3972 — price ~10.3% above it |
| 6m momentum (skip last month) | -3.1% |
| Portfolio note | ATR 6.02% -> vol-throttle: size down per rules.md |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads only the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$141.26**, **+22.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $141.26 price -> -15.0% (price richer to the model than last run's -6.6%, tracking the rally) |
| Trailing stop (chandelier) | $130.0182 — price is ~8.0% above it |
| 6m momentum (skip last month) | -5.6% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $24.97 | 10 | $15.43 | $249.70 | +61.8% | 20.2% |
| NOW | $141.26 | 7 | $114.97 | $988.82 | +22.9% | 79.8% |

**Total value: $1,238.52** | Cost: $959.09 | **Total return: ~+29.1%** (+$279.43 unrealised)

Both positions gained since 2026-08-19 (BMNR +21.6%, NOW +9.8% in price
terms over the period); the weight split (20.2% / 79.8%) is essentially
unchanged from last run's 18.6%/81.4%.

## Action flags (priority order)

1. **[Mandate — persists, still unresolved] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`, conflicting with the
   recorded `compliant` status (screened 2026-07-07, now 60 days stale
   against the review, though not yet flagged stale by shariah.py's own
   window). Dedicated web research this run looked specifically for anything
   that would resolve this one way or the other — a Shariah-screening
   provider's classification, an index reclassification, a company statement
   on business-activity characterization — and **found nothing**. Yahoo
   Finance still lists BMNR under "Capital Markets." Meanwhile the
   fundamentals that originally raised the question have deepened: ETH
   holdings grew to **5.9M ETH** (~$15.6B total crypto/cash/marketable
   securities) as of Aug 30, 86% of it now staked via MAVAN with annualized
   staking revenue projected at **~$335M** (scaling toward ~$390M at full
   staking) — Q2 staking revenue alone was $45.7M, ~98% of total revenue.
   The board also declared 17 more BMNP preferred dividends running through
   December. This is now the **third straight run** flagging the same
   conflict with zero resolution, on a position whose weight has grown to
   20.2% (from 18.6%) and return to +61.8% (from +33.1%). Per this repo's
   own Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL regardless
   of the return. **`recommend.py`'s "would buy today" check still only
   reads the recorded field and stays silent on this.** Re-screen in
   Zoya/Musaffa on the business-activity question specifically — this has
   now gone two months without a fresh independent screen.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF caveat / BMNR]** The -97.1% DCF "downside" remains not a meaningful
   signal — the model (5% growth, 10% discount, no BMNR-specific override)
   does not fit a crypto-treasury business valued on ETH holdings and
   staking yield, not discounted operating cash flow.
4. **[Catalyst / NOW — now inside the window]** Next earnings now estimated
   **~2026-10-28** (53 days out — inside the 60-day catalyst horizon for the
   first time this cycle; date is analyst-tracker estimated, not yet
   company-confirmed). Fundamentals reported since last run are strong: Q2
   subscription revenue +24.5% YoY, FY2026 subscription guidance **raised**
   to $15.76-15.78B (~21% CC growth — still at the thesis's own threshold,
   not below it), and the AI ACV target was raised from $1B to $1.5B with
   >$1M/yr Now Assist customers up >130% YoY. Analyst targets have moved up
   accordingly (BofA to $150, Wells Fargo to $175, Bernstein to $248). The
   stock did fall ~4.3% on 2026-09-02, but no company-specific negative
   catalyst was found — reads as broad tech/rate-sensitive weakness, not a
   thesis break.
   [24/7 Wall St.](https://247wallst.com/investing/2026/08/25/servicenow-just-ripped-29-in-a-month-what-would-it-take-to-get-now-stock-up-to-150/) ·
   [TIKR](https://www.tikr.com/blog/servicenow-jumped-7-on-a-150-analyst-target-heres-where-the-stock-could-go)
5. **[Discovery] 50 leads this run, 18 clear to LEAD tier** (up from 9 last
   run). **PLTR** carries over again with its still-unresolved
   government/defense business-activity question — nothing new to add,
   still open. The precious-metals cluster (**AGI, EGO, IAG** all LEAD this
   run) is the same recurring group flagged before on mining-royalty
   financing-structure grounds — still worth a real screen before spending
   review time on any of these cards.
6. **[Housekeeping, unresolved] BMNR holding file** is still missing
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, and
   `pre_mortem` — two months after the position was opened (2026-07-07).

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH holdings keep growing (5.9M ETH, ~86%
staked) with staking revenue now ~98% of total revenue and annualizing
toward ~$335-390M; the $4B buyback remains active; B. Riley raised its price
target to $30 from $25 in early September. Stock up +61.8% since the $15.43
cost basis; recorded compliance status is "compliant."
[Motley Fool](https://www.fool.com/investing/2026/09/03/why-bitmine-immersion-technologies-soared-465-in-a/) ·
[The Block treasury tracker](https://www.theblock.co/treasuries/bmnr)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check has now disagreed with the recorded status for
three consecutive runs with no independent re-screen in between — see
Action Flag #1. The holding file also remains incomplete (no
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, or
`pre_mortem`), so there is still no PM-grade record to weigh the compliance
question against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, and it has now gone unresolved for two
months.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 subscription revenue +24.5% YoY beat guidance; FY2026
guidance raised; AI ACV target raised from $1B to $1.5B with >$1M/yr Now
Assist customers up >130% YoY; multiple analyst price-target raises (BofA
$150, Wells Fargo $175, Bernstein $248). DCF shows a wider but still
moderate ~15% premium to intrinsic value.
[24/7 Wall St.](https://247wallst.com/investing/2026/08/25/servicenow-just-ripped-29-in-a-month-what-would-it-take-to-get-now-stock-up-to-150/) ·
[ServiceNow IR — Q2 2026 results](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum still
negative (-5.6%); the stock fell ~4.3% on 2026-09-02 with no identified
company-specific cause; next earnings (~Oct 28, estimated) now sits inside
the 60-day catalyst window, so this is the first run where a near-term
binary event is in play.
[MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite three straight runs of ratio-precheck fails. Nothing in the
  automated pipeline will re-flag this on its own until you update the
  recorded status — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE fired -> BMNR**: ATR 6.02% above the 6% threshold — size
  down note, per rules.md.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $24.97 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $141.26 | -15.0% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all 79 cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one (16 new cards — NTNX,
XOM, HBM, NTAP, AAPL, BLSH, TECK, TS, FLYW, FRO, APA, PR, SMTC, BBY, ASND,
SNA; 34 existing cards left unchanged). **Every DRAFT card is unreviewed and
Shariah UNVERIFIED — proposals to review and edit, never buys.**

18 of the 50 leads clear to LEAD tier this run (up from 9 last run; the rest
are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| STX | existing | 10.6:1 | earnings 2026-10-27 | 52 |
| ALAB | existing | 9.4:1 | earnings 2026-11-03 | 59 |
| LRCX | existing | 17.8:1 | earnings 2026-10-21 | 46 |
| TSLA | existing | 12.3:1 | earnings 2026-10-21 | 46 |
| HAS | existing | 11.4:1 | earnings 2026-10-22 | 47 |
| AA | existing | 13.6:1 | earnings 2026-10-15 | 40 |
| CLS | existing | 17.0:1 | earnings 2026-10-26 | 51 |
| TTMI | existing | 20.0:1 | earnings 2026-11-04 | 60 |
| XOM | new | 8.7:1 | earnings 2026-10-30 | 55 |
| AMD | existing | 6.4:1 | earnings 2026-11-03 | 59 |
| MSFT | existing | 3.9:1 | earnings 2026-10-28 | 53 |
| PLTR | existing | 3.3:1 | earnings 2026-11-02 | 58 |

(EGO, FOX, HBM, AGI, GDDY, IAG also clear to LEAD this run — full list in `leads.md`.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **AGI, EGO, IAG** (plus **CDE, AR, KGC** in the broader RESEARCH-tier
  pool) — the recurring precious-metals/mining cluster; mining-royalty
  financing structures raised the same open question in earlier runs. Still
  worth a real screen before spending review time on any of these cards.
- **32 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — unresolved for two months] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status for three consecutive runs on the business-activity question
   specifically, and dedicated research this run found no external
   clarification. This is the largest compliance question in the book
   (20.2% weight, +61.8% return) and the automated pipeline will NOT
   re-surface it on its own — see the COMPLIANCE_GATE note above.
2. **[Housekeeping, unresolved] BMNR holding file is still missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, two months after
   the position was opened.
3. **[Time-boxed — now inside the window] NOW earnings ~2026-10-28**
   (estimated, unconfirmed) — 53 days out; track guidance vs. the raised
   AI ACV target between now and then.
4. **[Housekeeping] 16 new DRAFT setup cards** added this run (79 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [The Block – BMNR treasury tracker](https://www.theblock.co/treasuries/bmnr)
- [PRNewswire – BMNR ETH holdings reach 5.90M tokens, $15.6B total](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-90-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-6-billion-302864579.html)
- [KuCoin – Bitmine Q2 2026 ETH staking revenue $45.7M](https://www.kucoin.com/news/flash/bitmine-earns-45-7m-in-ethereum-staking-revenue-for-q2-2026)
- [KuCoin – Bitmine staking >98% of revenue](https://www.kucoin.com/news/flash/bitmine-s-eth-staking-revenue-surpasses-98-of-total-4-9m-eth-staked)
- [TipRanks – BitMine Series A (BMNP) preferred dividends declared](https://www.tipranks.com/news/company-announcements/bitmine-declares-series-a-preferred-stock-dividends)
- [Motley Fool – Why Bitmine soared 46.5% in August](https://www.fool.com/investing/2026/09/03/why-bitmine-immersion-technologies-soared-465-in-a/)
- [Yahoo Finance – BMNR company profile (Capital Markets industry)](https://finance.yahoo.com/quote/BMNR/profile/)
- [ServiceNow Investor Relations – Q2 2026 financial results](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [24/7 Wall St. – ServiceNow ripped 29% in a month](https://247wallst.com/investing/2026/08/25/servicenow-just-ripped-29-in-a-month-what-would-it-take-to-get-now-stock-up-to-150/)
- [TheNextWeb – ServiceNow AI ACV target raised to $1.5B](https://thenextweb.com/news/servicenow-30-billion-2030-now-assist-ai-revenue)
- [TIKR – ServiceNow jumps on $150 BofA target](https://www.tikr.com/blog/servicenow-jumped-7-on-a-150-analyst-target-heres-where-the-stock-could-go)
- [MarketChameleon – NOW earnings dates](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)
