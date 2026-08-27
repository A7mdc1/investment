# Portfolio Assessment — 2026-08-27

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50 leads kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (9 new DRAFT setup cards auto-filled for leads with
no card — BKR, AMKR, LLY, APA, BLSH, ASND, FLYW, PR, DDOG; 41 existing cards
left unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still no `transactions.csv` (discipline guard stays
dormant).

**Since the last report (2026-08-19):** no trades recorded. Same two
holdings, no `/apply-trade` entries in between.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$26.51**, up
**+71.8%** vs. the $15.43 cost basis. **Action Flag #1 below is unchanged
from last run and now open for a second consecutive assessment — the
mechanical Shariah business-activity pre-check still disagrees with the
recorded "compliant" status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -7.5:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged since 2026-08-19) |
| DCF intrinsic value | $0.72 vs. $26.51 price -> -97.3% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $23.072 — price ~14.9% above it |
| 6m momentum (skip last month) | -18.8% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$137.42**, **+19.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -1.0:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $137.42 price -> -12.6% (price moderately rich to the model) |
| Trailing stop (chandelier) | $119.9727 — price is ~14.6% above it |
| 6m momentum (skip last month) | +5.9% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.51 | 10 | $15.43 | $265.10 | +71.8% | 21.6% |
| NOW | $137.42 | 7 | $114.97 | $961.80 | +19.5% | 78.4% |

**Total value: $1,226.90** | Cost: $959.09 | **Total return: ~+27.9%** (+$267.81 unrealised)

Concentration is essentially unchanged from last run (BMNR 21.6% vs 18.6%,
NOW 78.4% vs 81.4%) — the gap closed slightly because BMNR's return (+71.8%
now vs +33.1% then) outran NOW's, not from any sizing action.

## Action flags (priority order)

1. **[Mandate — open 2nd consecutive run] BMNR's mechanical Shariah ratio
   pre-check still FAILS**, flagging `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`, unchanged from
   2026-08-19. This continues to conflict with the recorded `compliant`
   status (broker app, screened 2026-07-07 — now 51 days old). Recent
   reporting reinforces the same profile as last run: BitMine's holdings
   plus cash/marketable securities reached **$14.9B** as of August 23
   (5.85M ETH, ~4.8% of supply), with management projecting **$254–299M in
   annualized ETH staking revenue** and an active **$4B buyback** (1.7M
   shares repurchased in the past week alone, 20.8M+ cumulative since July).
   That is a financial-asset-treasury / staking-yield business model, which
   is exactly the kind of activity a business-activity screen is built to
   catch. Per this repo's own Gate 1 ("Shariah knockout — non-compliant /
   ratio-or-business flag -> AVOID/SELL, absolute"), a confirmed fail would
   be a hard SELL regardless of the +71.8% return. `recommend.py`'s "would
   buy today" check only reads the recorded field and is still silent on
   this. **This is now two runs open with no re-screen — treat it as
   overdue**, the same pattern that took 7 runs to resolve with FIG.
   [StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/) ·
   [PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-85-million-tokens-and-total-crypto-and-total-cash-holdings-of-14-9-billion-302857967.html)
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH still
   holds. Do not add.
3. **[DCF caveat / BMNR]** The -97.3% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business whose
   value tracks ETH holdings and staking yield, not discounted operating
   cash flow. Treat this as a data-model gap, not a valuation call.
4. **[Catalyst / NOW]** Next earnings **confirmed for 2026-10-28, after
   close** (62 days out — just outside the 60-day catalyst-horizon default).
   Q3 guidance calls for subscription revenue of $3.975–3.980B (+20.5% YoY)
   and ~20% cRPO growth, with a stated $35M FX headwind to cRPO.
   [TipRanks](https://www.tipranks.com/stocks/now/earnings)
5. **[Catalyst / BMNR]** No confirmed next-earnings date found this run
   (crypto-treasury companies typically report on a different cadence than
   operating earnings calendars) — flagging as a data gap rather than
   fabricating a date.
6. **[Discovery] 50 leads this run**, 12 clearing to LEAD tier (up from 9
   last run) — the rest capped at RESEARCH by the asymmetry/catalyst gates.
   **PLTR** carries over again with its still-unresolved government/defense
   business-activity question flagged in prior runs — nothing new to add.
   The recurring precious-metals/mining names (**AGI, KGC, IAG**) are back
   in this run's pool too, same open compliance question as before.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Total crypto + cash/marketable-securities
holdings reached $14.9B as of Aug 23 (5.85M ETH), management projects
$254–299M in annualized ETH staking revenue via the MAVAN platform, and the
$4B buyback continues (1.7M shares repurchased in the past week, 20.8M+
cumulative since July). Stock up +71.8% since the $15.43 cost basis; recorded
compliance status is "compliant."
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-85-million-tokens-and-total-crypto-and-total-cash-holdings-of-14-9-billion-302857967.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check still disagrees with the recorded status — see
Action Flag #1, now open two runs running. The holding file itself is still
incomplete: no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` filled in, six weeks after the position was
opened — there is still no PM-grade record to weigh the compliance question
against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
now overdue to resolve, not the price action.**

### NOW — ServiceNow, Inc
**Case to keep:** Subscription revenue guided to +20.5% YoY for Q3, cRPO
guided to ~20% growth; AI-agent (Zurich platform) and Armis
security-workflow integration remain the forward drivers cited in the
holding thesis. DCF shows a moderate ~12.6% premium to intrinsic value — not
an extreme gap, and less stretched in percentage terms than the raw P/E
suggests.
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; earnings land
2026-10-28 after close (62 days out, just past the 60-day catalyst-horizon
default) with a stated $35M FX headwind to cRPO already baked into guidance
— worth watching whether that headwind widens.

**Verdict: HOLD (VALUATION_RICH) — no new information changes the thesis
this run.**

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two consecutive runs of ratio-precheck fails. Nothing in
  the automated pipeline will re-flag this on its own until the recorded
  status is updated — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $26.51 | -97.3% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $137.42 | -12.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 9 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and rewrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead that didn't
already have one: **BKR, AMKR, LLY, APA, BLSH, ASND, FLYW, PR, DDOG** (9
new cards; 41 existing cards left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

12 of the 50 leads clear to LEAD tier this run (up from 9 last run):

| Ticker | R:R | Catalyst | Days out |
|---|---|---|---|
| AMKR | 20.0:1 | earnings 2026-10-26 | 60 |
| CLS | 13.3:1 | earnings 2026-10-26 | 60 |
| BKR | 10.9:1 | earnings 2026-10-22 | 56 |
| CIEN | 8.9:1 | earnings 2026-09-03 | 7 |
| TER | 8.9:1 | earnings 2026-10-21 | 55 |
| AA | 7.9:1 | earnings 2026-10-15 | 49 |
| CRDO | 6.6:1 | earnings 2026-09-01 | 5 |
| MU | 5.1:1 | earnings 2026-09-30 | 34 |
| TSLA | 5.0:1 | earnings 2026-10-21 | 55 |
| LRCX | 4.2:1 | earnings 2026-10-21 | 55 |
| ZS | 3.7:1 | earnings 2026-09-03 | 7 |
| HAS | 3.6:1 | earnings 2026-10-22 | 56 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **AGI, KGC, IAG** — the recurring precious-metals/mining cluster;
  mining-royalty financing structures raised the same open question in
  earlier runs. Still worth a real screen before spending review time on
  any of these cards.
- **38 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Overdue — 2nd run open] BMNR Shariah re-screen**: the mechanical
   ratio pre-check has now disagreed with the recorded "compliant" status
   for two consecutive assessments (08-19 and 08-27). This is the largest
   compliance question in the book (21.6% weight, +71.8% return) and the
   automated pipeline will NOT re-surface it on its own — see the
   COMPLIANCE_GATE note above.
2. **[Housekeeping — 6 weeks open] BMNR holding file is still missing
   PM-grade fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` remain null/empty.
3. **[Time-boxed] NOW earnings 2026-10-28 after close** — 62 days out; no
   action needed yet, track the AI ACV / Armis integration narrative and the
   stated FX headwind to cRPO between now and then.
4. **[Housekeeping] 9 new DRAFT setup cards** added this run; none are
   `planned`. Review at your own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Rides Ethereum Staking Wave And Aggressive Buybacks — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_20/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.85 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-85-million-tokens-and-total-crypto-and-total-cash-holdings-of-14-9-billion-302857967.html)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
