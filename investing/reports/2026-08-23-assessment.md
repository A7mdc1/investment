# Portfolio Assessment — 2026-08-23

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (5 new DRAFT setup cards auto-filled — ASND, EXPE,
SMCIP, XOM, JAZZ; 45 existing cards left unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` not run separately — still no
`transactions.csv` (discipline guard stays dormant).

**Since the last report (2026-08-19):** no trades recorded. Both holdings
gained: BMNR $20.54 → $22.83, NOW roughly flat at $128.63 → $128.48.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$22.83**, up
**+48.0%** vs. the $15.43 cost basis. **Action Flag #1 is unchanged from last
run: the mechanical Shariah business-activity pre-check still disagrees with
the recorded "compliant" status — this is now the second consecutive report
flagging it.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.8:1 (DCF-derived target sits far below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL, again** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $22.83 price -> -96.9% (not a meaningful signal — see caveat) |
| Trailing stop (chandelier) | $19.5901 — price ~14.2% above it |
| 6m momentum (skip last month) | -17.6% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not the ratio-precheck fail (unchanged limitation) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$128.48**, **+11.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.5:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $128.48 price -> -6.5% (price modestly rich to the model) |
| Trailing stop (chandelier) | $111.0091 — price ~13.6% above it |
| 6m momentum (skip last month) | -11.8% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $22.83 | 10 | $15.43 | $228.30 | +48.0% | 20.2% |
| NOW | $128.48 | 7 | $114.97 | $899.36 | +11.8% | 79.8% |

**Total value: $1,127.66** | Cost: $959.09 | **Total return: ~+17.6%** (+$168.57 unrealised)

Weights are essentially unchanged from last run (BMNR 18.6% -> 20.2%, NOW
81.4% -> 79.8%) — BMNR's outsized move (+9.9pp move since 08-19) closed some
of the gap but the book is still dominated by NOW.

## Action flags (priority order)

1. **[Mandate — STILL OPEN, 2nd run] BMNR's mechanical Shariah ratio
   pre-check FAILS again**, same flag as 08-19:
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. Recorded status is still `compliant` (broker app,
   2026-07-07) and nothing has changed on the card since last report — no
   re-screen has been logged. Fresh reporting this run reinforces the same
   picture as before: BitMine describes itself as an Ethereum treasury
   company holding **$11.4B** in crypto/cash/strategic stakes (5.82M ETH,
   ~4.8% of supply, target 5%), funding buybacks (20.8M+ shares repurchased
   since July) and **17 scheduled BMNP preferred dividends** off staking
   yield (~$254-299M annualized). That combination — a large financial-asset
   treasury generating yield income, financed partly through preferred
   dividends — is exactly the profile a business-activity screen is meant to
   flag, and it is unchanged from last run's read. Per this repo's Gate 1
   ("Shariah knockout ... -> AVOID/SELL, absolute"), a confirmed fail here
   would be a hard SELL regardless of the now +48.0% return. `recommend.py`
   still only reads the recorded field and stays silent on this. **This has
   now sat open across two consecutive reports on the single largest
   position-return item in the book — worth resolving in Zoya/Musaffa before
   the next report, not deferring again.**
   [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-bmnr-151249411.html) ·
   [PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html) ·
   [StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still holds. Do not add.
3. **[DCF caveat / BMNR]** The -96.9% DCF "downside" is still not a
   meaningful signal — the cash-flow model does not fit a crypto-treasury
   business valued on ETH holdings/staking yield, not discounted operating
   cash flow. Same caveat as last run; treat as a data gap.
4. **[Catalyst / NOW]** Q2 FY2026 results are in and were strong (revenue
   $3.99B, +24% YoY; EPS $0.90, +11.1% YoY); Q3 subscription guidance
   $3.975-3.980B. Bank of America raised its price target to $150 from $130
   on 2026-08-19 (Buy). Next earnings still ~2026-10-28 (~66 days out —
   outside the 60-day catalyst horizon, so still no near-term binary event).
   [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-holds-above-128-as-ai-deals-and-strong-q2-earnings/69986376)
5. **[Discovery] 50 leads this run**, only 13 clearing to LEAD tier (up from
   9 last run) — the rest capped at RESEARCH by asymmetry/catalyst gates.
   **PLTR dropped out of the top-50 pool this run** (was carried over with an
   unresolved defense/government business-activity question in prior runs;
   its absence here is a pool-ranking effect, not a resolution — nothing to
   conclude from it). The precious-metals cluster (CDE, AR, AGI, KGC, EGO)
   is still present at RESEARCH tier; same open mining-royalty-financing
   question as before, still unscreened.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH holdings now 5.82M tokens (~4.8% of
global supply, targeting 5%), total crypto/cash/strategic holdings $11.4B.
Buyback program continues (20.8M+ shares repurchased since July under the
$4B plan); management projects $254-299M annualized ETH staking revenue via
MAVAN; the board has locked in 17 upcoming BMNP preferred dividends. BMNR was
also added to the Russell 1000 this run, which should broaden
institutional/index-fund ownership. Stock up +48.0% since the $15.43 cost
basis; recorded compliance status is still "compliant."
[Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-bmnr-151249411.html) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status for a second
straight run — see Action Flag #1. The holding file is still missing
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, and
`pre_mortem` — six weeks after the position was opened, there is still no
PM-grade record to weigh the compliance question against.

**Verdict: HOLD (no technical rule fired) — the compliance question is now
two reports old and unresolved; it is the thing to resolve, not the price
action, which keeps getting better while the open question sits untouched.**

### NOW — ServiceNow, Inc
**Case to keep:** Q2 FY2026 beat with 24% YoY revenue growth and 11.1% YoY
EPS growth; Q3 subscription guidance implies continued mid-20s growth. Bank
of America raised its price target to $150 (from $130, Buy) on 2026-08-19;
consensus target ~$144. DCF shows only a modest ~6.5% premium to intrinsic
value — not an extreme gap.
[ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-holds-above-128-as-ai-deals-and-strong-q2-earnings/69986376)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; 6m momentum still
negative (-11.8%, more negative than last run's -5.3%) despite the earnings
beat; next earnings not until ~2026-10-28, so still no near-term binary
catalyst.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two runs of ratio-precheck fails now. Nothing in the
  automated pipeline will re-flag this on its own — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); both prices sit well above their computed chandelier levels.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $22.83 | -96.9% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $128.48 | -6.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** this run (expected — no card has been reviewed and flipped
to `status: planned` yet; all 69 cards in `setups/` are still `draft`).

## Draft & planned setups — 50 leads, 5 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (top 50
by max-benefit rank). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for the 5 leads without one (ASND, EXPE, SMCIP,
XOM, JAZZ; 45 existing cards left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

13 of the 50 leads clear to LEAD tier this run (up from 9 last run):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| ULTA | LEAD | existing | 20.0:1 | earnings 2026-08-27 | 4 |
| VICR | LEAD | existing | 19.4:1 | earnings 2026-10-20 | 58 |
| CIEN | LEAD | existing | 9.4:1 | earnings 2026-09-03 | 11 |
| SNX | LEAD | existing | 8.4:1 | earnings 2026-09-24 | 32 |
| AA | LEAD | existing | 7.0:1 | earnings 2026-10-15 | 53 |
| CRDO | LEAD | existing | 7.1:1 | earnings 2026-09-01 | 9 |
| TER | LEAD | existing | 5.7:1 | earnings 2026-10-21 | 59 |
| ZS | LEAD | existing | 5.5:1 | earnings 2026-09-03 | 11 |
| LRCX | LEAD | existing | 3.8:1 | earnings 2026-10-21 | 59 |
| TSLA | LEAD | existing | 3.5:1 | earnings 2026-10-21 | 59 |
| GWRE | LEAD | existing | 3.3:1 | earnings 2026-09-03 | 11 |
| HAS | LEAD | existing | 3.3:1 | earnings 2026-10-22 | 60 |
| NVDA | LEAD | existing | 3.2:1 | earnings 2026-08-26 | 3 |

(ULTA and NVDA have earnings inside the next week — if still accurate,
verify before treating either lead as forward-looking rather than
already-priced.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR dropped out of the top-50 pool this run** — was flagged in prior
  runs for an unresolved government/defense business-activity question.
  Absence from this run's ranking is not a resolution of that question,
  just a ranking effect; nothing to act on.
- **CDE, AR, AGI, KGC, EGO** — the recurring precious-metals/mining cluster
  (still at RESEARCH tier); mining-royalty financing structures raised the
  same open question in earlier runs. Still worth a real screen before
  spending review time on any of these cards.
- **37 RESEARCH-tier leads** total — full list in `leads.md`; not
  reproduced here in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — now 2 runs old] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has disagreed with the recorded "compliant" status for
   two consecutive reports now on the business-activity question
   specifically. This is the single most-flagged open item in the book
   (20.2% weight, +48.0% return) and the automated pipeline will NOT
   re-surface it beyond this report format — see the COMPLIANCE_GATE note.
2. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, six weeks after
   the position was opened.
3. **[Time-boxed] NOW earnings ~2026-10-28** — ~66 days out; no action
   needed yet, but the Q2 beat and BofA target raise are constructive
   context to carry forward.
4. **[Housekeeping] 5 new DRAFT setup cards** added this run (69 total in
   `setups/`); none are `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Why BitMine Immersion Technologies (BMNR) Is Up 13.1% After Targeting 5% of All Ethereum — Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-technologies-bmnr-151249411.html)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.82 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)
- [BMNR Stock Rides Ethereum Staking Wave And Aggressive Buybacks — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)
- [ServiceNow stock holds above $128 as AI deals and strong Q2 earnings support outlook — ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-holds-above-128-as-ai-deals-and-strong-q2-earnings/69986376)
