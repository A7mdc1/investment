# Portfolio Assessment — 2026-09-12

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (16 new DRAFT setup cards auto-filled — AAPL, APA,
ASND, BLSH, DDS, FLYW, FRO, HPE, KEYS, NTAP, NTR, SMCIP, SNA, TECK, TS, XOM;
34 existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run separately — still no `transactions.csv` (discipline
guard stays dormant).

**Since the last report (2026-08-19):** no trades logged. Both positions have
run higher; the BMNR Shariah ratio-precheck flag from last run is still open
and unresolved — see Action Flag #1.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.03**, up
**+62.2%** vs. the $15.43 cost basis. **Action Flag #1 persists: the
mechanical Shariah business-activity pre-check still disagrees with the
recorded "compliant" status — now two consecutive runs.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -8.2:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen (unchanged from last run) |
| DCF intrinsic value | $0.72 vs. $25.03 price -> -97.1% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.0645 — price ~13.5% above it |
| 6m momentum (skip last month) | -12.9% |
| Vol throttle | ATR 6.53% — portfolio note fired this run: size down |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 >= pe_rich 50).
Live price **$132.53**, **+15.3%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.9:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $132.53 price -> -9.4% (price modestly rich to the model) |
| Trailing stop (chandelier) | $130.3141 — price is only ~1.7% above it (tightest margin recorded yet; was ~17.9% last run) |
| 6m momentum (skip last month) | +10.6% (back to positive; was -5.3% last run) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- `trade_type: core` on both positions exempts them from the mechanical
  TRAIL_STOP sell rule — but NOW's price is now close enough to its computed
  chandelier stop ($130.31 vs. $132.53) that it's worth watching without
  relying on the automated gate to catch it.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $25.03 | 10 | $15.43 | $250.30 | +62.2% | 21.2% |
| NOW | $132.53 | 7 | $114.97 | $927.71 | +15.3% | 78.8% |

**Total value: $1,178.01** | Cost: $959.09 | **Total return: ~+22.8%** (+$218.92 unrealised)

## Action flags (priority order)

1. **[Mandate — still open, 2nd consecutive run] BMNR's mechanical Shariah
   ratio pre-check still FAILS**: `industry 'Capital Markets' matches
   'capital markets' — core business fails screen`. This still conflicts
   with the recorded `compliant` status (broker app, screened 2026-07-07 —
   now over two months old). Nothing changed on this question since last
   run's flag. Per this repo's own Gate 1 ("Shariah knockout —
   non-compliant / ratio-or-business flag -> AVOID/SELL, absolute"), a
   confirmed fail here would be a hard SELL, independent of the +62.2%
   return. **`recommend.py`'s "would buy today" check only reads the
   recorded field and stays silent on this** — the automated pipeline will
   not resolve this on its own. This is now the largest open compliance
   question in the book at 21.2% weight and the position's best return to
   date.
2. **[Valuation / NOW] P/E ~119.02 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Technical / NOW] Trailing-stop margin has compressed sharply** — price
   is only ~1.7% above the computed chandelier stop ($130.31), versus ~17.9%
   at the last assessment. `trade_type: core` means this doesn't auto-fire a
   sell rule, but the cushion that made that exemption low-stakes last run
   has largely closed.
4. **[DCF caveat / BMNR]** The -97.1% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override in the holding file) does not fit a
   crypto-treasury business whose value is driven by ETH holdings and
   staking yield, not discounted operating cash flow. Treat this number as
   a data gap, not a valuation call.
5. **[Catalyst / NOW]** Next earnings confirmed **2026-10-28** (46 days out —
   now inside the 60-day `catalyst_horizon_days` window, unlike last run's
   72-days-out reading). ServiceNow's Autonomous Security & Risk launch
   (Armis + Veza integration, announced May 2026) continues to extend the
   AI-agent-governance story.
6. **[Discovery] 50 leads this run**, 19 clearing to LEAD tier (up from 9
   last run), the rest capped at RESEARCH by the asymmetry/catalyst gates.
   **PLTR** carries over again with its still-unresolved government/defense
   business-activity question flagged in prior runs — nothing new to add.
   The recurring precious-metals/mining cluster (**CDE, AR, AGI, IAG, EGO**)
   also carries over with the same open financing-structure question from
   earlier runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** ETH treasury continues to grow — ~5.93M ETH
(~4.86% of global supply) and ~$15.7B total crypto/cash holdings as of early
September, per company disclosures. The MAVAN institutional staking platform
has expanded to serve institutional custodians. Stock up +62.2% since the
$15.43 cost basis; recorded compliance status is still "compliant."
[The Block](https://www.theblock.co/treasuries/bmnr) ·
[PR Newswire](https://www.prnewswire.com/in/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion-302871981.html)

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status again this
run — see Action Flag #1. Separately, dilution risk is real and growing:
shares outstanding have expanded substantially over the past year, and the
company has layered in a 9.50% coupon preferred (BMNP) that sits ahead of
common in a liquidation and is a permanent drag on common holders if ETH
weakens. The holding file itself is still incomplete — no
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, or
`pre_mortem` filled in, two months after the position was opened.
[Seeking Alpha](https://seekingalpha.com/article/4921130-the-bitmine-immersion-discount-is-dangerous-upgrade)

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, not the price action.**

### NOW — ServiceNow, Inc
**Case to keep:** Momentum has turned positive (6m momentum +10.6%, versus
-5.3% last run). The Armis acquisition (closed April 2026) is now embedded
in a broader "Autonomous Security & Risk" launch (with Veza) governing AI
agent identity and access, reinforcing the AI-agent-expansion thesis. DCF
shows only a modest ~9.4% premium to intrinsic value — not an extreme gap.
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-Autonomous-Security--Risk-integrating-Armis-and-Veza-to-govern-every-AI-agent-identity-and-connected-asset/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the trailing-stop
cushion has compressed to ~1.7% (was ~17.9% last run) even though momentum
and price are both up — a sign the chandelier stop is tightening under
recent volatility, not that the position is breaking down. Next earnings
confirmed for **2026-10-28**.
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite this run's (second consecutive) ratio-precheck fail. That
  gap is worth naming explicitly again: nothing in the automated pipeline
  will re-flag this on its own until you update the recorded status.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both); BMNR still sits well above its chandelier ($22.06 vs.
  $25.03), NOW's cushion has compressed to ~1.7% (see Action Flag #3).
- **VOL_THROTTLE fired -> BMNR**: ATR 6.53% — size down per the vol
  throttle note (new this run; did not fire last time).

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.03 | -97.1% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $132.53 | -9.4% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all cards in `setups/` are still
`draft`).

## Draft & planned setups — 50 leads, 16 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (16
new cards: AAPL, APA, ASND, BLSH, DDS, FLYW, FRO, HPE, KEYS, NTAP, NTR,
SMCIP, SNA, TECK, TS, XOM; 34 existing cards left unchanged). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.**

19 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
mix of names in the pool has changed, not a policy change):

| Ticker | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|
| TTMI | existing | 16.6:1 | earnings 2026-11-04 | 53 |
| UTHR | existing | 16.0:1 | earnings 2026-10-28 | 46 |
| AGI | existing | 12.7:1 | earnings 2026-10-28 | 46 |
| PLTR | existing | 11.2:1 | earnings 2026-11-02 | 51 |
| FOX | existing | 11.0:1 | earnings 2026-10-29 | 47 |
| GOOGL | existing | 9.4:1 | earnings 2026-10-28 | 46 |
| GDDY | existing | 8.9:1 | earnings 2026-10-29 | 47 |
| MSFT | existing | 7.6:1 | earnings 2026-10-28 | 46 |
| IAG | existing | 6.7:1 | earnings 2026-11-03 | 52 |
| DOCN | existing | 6.1:1 | earnings 2026-11-04 | 53 |
| AR | existing | 6.0:1 | earnings 2026-10-28 | 46 |
| TSLA | existing | 5.6:1 | earnings 2026-10-21 | 39 |
| FLYW | new | 5.6:1 | earnings 2026-11-03 | 52 |
| TECK | new | 5.4:1 | earnings 2026-10-22 | 40 |
| CDE | existing | 5.9:1 | earnings 2026-10-28 | 46 |
| EGO | existing | 5.1:1 | earnings 2026-10-29 | 47 |
| DLO | existing | 4.4:1 | earnings 2026-11-11 | 60 |
| CLS | existing | 3.5:1 | earnings 2026-10-26 | 44 |
| MU | existing | 3.6:1 | earnings 2026-09-30 | 18 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI, IAG, EGO** — the recurring precious-metals/mining cluster;
  mining-royalty financing structures raised the same open question in
  earlier runs. Still worth a real screen before spending review time on
  any of these cards.
- **31 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  in full to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — still open, 2nd run] BMNR Shariah re-screen**: the mechanical
   ratio pre-check still disagrees with the recorded "compliant" status on
   the business-activity question specifically. This is the largest open
   compliance question in the book (21.2% weight, +62.2% return) and the
   automated pipeline will NOT re-surface it on its own.
2. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, two months after the position was
   opened.
3. **[Watch] NOW's trailing-stop cushion has compressed to ~1.7%** — not a
   rule trigger (core exemption), but worth a real "would I buy this here
   today?" re-underwrite before the next earnings print on 2026-10-28.
4. **[Housekeeping] 16 new DRAFT setup cards** added this run (50 total
   leads, most already carrying cards); none are `planned`. Review at your
   own pace.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [Bitmine's Ethereum holdings near 6M as crypto treasury hits $15.7B — Seeking Alpha](https://seekingalpha.com/news/4640764-bitmines-ethereum-holdings-near-6m-as-crypto-treasury-hits-157b?feed_item_type=news)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.93 Million Tokens — PR Newswire](https://www.prnewswire.com/in/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-93-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-7-billion-302871981.html)
- [The Bitmine Immersion Discount Is Dangerous (Upgrade) — Seeking Alpha](https://seekingalpha.com/article/4921130-the-bitmine-immersion-discount-is-dangerous-upgrade)
- [ServiceNow launches Autonomous Security & Risk, integrating Armis and Veza — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-launches-Autonomous-Security--Risk-integrating-Armis-and-Veza-to-govern-every-AI-agent-identity-and-connected-asset/default.aspx)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
