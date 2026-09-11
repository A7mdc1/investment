# Portfolio Assessment — 2026-09-11

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data via the curl_cffi impersonation workaround —
no data gaps this run) built a fresh 50-name pool (SPUS holdings +
`growth_technology_stocks` / `undervalued_large_caps` screens, `discover_top_n:
50`) and overwrote `leads.md` → `scaffold.py --all-leads` (15 new DRAFT setup
cards auto-filled; 63 existing cards left unchanged — 78 total in `setups/`)
→ `prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live. `journal.py` not run — `transactions.csv` still
doesn't exist in this workspace (it's git-ignored on purpose; personal ledger
data is never committed), so the discipline guard stays dormant.

**Since the last report (2026-08-19):** no new transactions recorded (holdings
unchanged: BMNR 10 sh, NOW 7 sh). BMNR's price kept climbing (+33.1% → +65.75%
vs. cost) and **the BMNR Shariah ratio-pre-check conflict flagged "urgent" last
cycle is still open** — same recorded `compliant` status, same screen date
(2026-07-07), no re-screen recorded. That's the top item below.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$25.58**, up
**+65.75%** vs. the $15.43 cost basis. **Action Flag #1 — the mechanical
Shariah business-activity pre-check still disagrees with the recorded
"compliant" status, unresolved since last run.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -7.1:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $25.60 price -> -97.2% (see DCF caveat: model doesn't fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.0645 — price ~13.7% above it |
| 6m momentum (skip last month) | -12.9% |
| Portfolio note | ATR 6.39% (> `vol_throttle_atr_pct` 6) — size down per vol throttle |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail (see below) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 >= pe_rich 50).
Live price **$132.35**, up **+15.16%** vs. the $114.97 cost basis. Price is
now only **~1.5% above its trailing stop ($130.31)** — the tightest cushion
either holding has shown in recent reports.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -3.8:1 (DCF target below stop) |
| Shariah (recorded) | PASS — broker_app compliant, purification 3.35%, screened 2026-06-09 |
| Shariah (mechanical ratio pre-check, this run) | PASS — clean (debt_ratio 0.018, liquid_ratio 0.046, business_ok) |
| DCF intrinsic value | $120.12 vs. $132.37 price -> -9.3% |
| Trailing stop (chandelier) | $130.3141 — price ~1.5% above it |
| 6m momentum (skip last month) | +10.6% |
| Would buy today? | Mechanically yes per recommend.py's gates |
| What changes verdict | A close below $130.31 (TRAIL_STOP), or subscription growth decelerating well below ~20% YoY |

`verdict.py` note: only 2 holdings — concentration rule stays muted until
>= 4 names (`min_names_for_concentration`). Worth saying plainly anyway: NOW
alone is **78.4%** of this book.

## Snapshot (live)

| Ticker | Shares | Cost | Price | Value | Weight | Return |
|---|---|---|---|---|---|---|
| BMNR | 10 | $15.43 | $25.58 | $255.75 | 21.63% | +65.75% |
| NOW | 7 | $114.97 | $132.41 | $926.83 | 78.37% | +15.16% |
| **Total** | | | | **$1,182.58** | | |

## Action flags (priority order)

1. **[Mandate — carried over, still unresolved] BMNR's mechanical Shariah
   ratio pre-check still FAILS** (`industry 'Capital Markets' matches
   'capital markets' — core business fails screen`), against the recorded
   `compliant` status (broker app, screened 2026-07-07 — same date as last
   run, so no re-screen has happened). Current web reporting reinforces why
   this is a real question, not noise: as of 2026-09-08 BitMine holds
   5.93M ETH + 211 BTC + stakes in Beast Industries and Eightco, totaling
   **$15.7B** in crypto/cash/marketable securities, with ~4.9% of the entire
   ETH supply staked. That is a financial-treasury/yield profile, not an
   operating-tech one — the same category of business-activity question a
   Shariah screen is built to catch. Per this repo's Gate 1 ("Shariah
   knockout — non-compliant / ratio-or-business flag -> AVOID/SELL,
   absolute"), a confirmed fail here would be a hard SELL independent of the
   now much larger +65.75% return. **`recommend.py`'s "would buy today"
   check only reads the recorded field and stays silent on this flag** —
   the automated pipeline will not resolve this on its own; it needs an
   actual Zoya/Musaffa business-activity re-screen. This is the second
   consecutive run carrying this flag with no action taken.
2. **[Risk / BMNR]** Cantor Fitzgerald raised its price target to **$63.60**
   from $30.60 on 2026-09-10 — a large jump in analyst sentiment on the ETH
   treasury/staking narrative. Not a compliance signal either way, but a
   reminder the position's size and momentum are both increasing while the
   mandate question above stays open.
3. **[Technical / NOW]** Price is **~1.5% above its trailing stop** ($132.35
   vs. $130.3141) — the closest either holding has sat to a TRAIL_STOP
   trigger in recent cycles. No rule has fired yet; flagging the proximity.
4. **[Valuation / NOW]** P/E ~119 (recorded) — rich; VALUATION_RICH holds. Do not add.
5. **[DCF caveat / BMNR]** The -97.2% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override) does not fit a crypto-treasury business whose
   value tracks ETH holdings and staking yield, not discounted operating
   cash flow. Treat this as a data-model gap, not a valuation call.
6. **[Catalyst / NOW]** ServiceNow has not yet announced its Q3 2026
   earnings date; historical pattern (late Oct in 2021-2025) points to
   roughly **2026-10-23 to 2026-10-29** — outside the 60-day catalyst
   horizon for now. Guidance already points to subscription revenue growth
   of ~20.5% YoY and cRPO growth of ~20% for the quarter.
7. **[Discovery] 50 leads this run**, 22 clearing to LEAD tier (up from 9
   last run — see table below); the rest capped at RESEARCH by the
   asymmetry/catalyst gates. The recurring precious-metals/mining cluster
   (**CDE, AR, EGO, IAG, AGI**) is back in the LEAD list again with the same
   open royalty-financing business-activity question raised in prior runs —
   nothing new to add. PLTR dropped out of the top-50 pool this run (was
   flagged in prior reports; not in today's leads.md at all).

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc

**Case to keep:** momentum and headline fundamentals (ETH holdings, staking
yield, buyback program) keep improving, and the recorded compliance status
has not changed. Price sits comfortably above its trailing stop.

**Case to trim/exit:** the mechanical Shariah signal is now flagging for a
second straight cycle and the position has grown to 21.6% of the book while
that question sits open. FIG (the position BMNR effectively replaced) took 7
runs to resolve a similar conflict, holding through the entire time at a
loss it didn't need to take. The PM-grade fields that would normally justify
holding through this kind of flag — `conviction`, `thesis_one_liner`,
`variant_view`, `initial_stop`, `target_price`, `pre_mortem` — are still all
null/empty on `holdings/bmnr.md`, two months after the position was opened.

### NOW — ServiceNow, Inc

**Case to keep:** durable subscription growth (~20%+ guided), AI-agent
expansion, Armis integration progressing; price is up modestly since the last
report and momentum remains positive (+10.6% 6m skip-month).

**Case to trim/watch:** P/E ~119 is priced for continued high growth with no
room for a stumble; price is now only ~1.5% above its trailing stop, tighter
than in prior reports. No hard catalyst date is confirmed yet for the ~Oct
28 earnings window.

## Suggested actions (from YOUR rules, rules.md)

- **Rule VALUATION_RICH fired -> HOLD, do not add** (NOW P/E ~119.02 >=
  `pe_rich` 50). This is your own pre-committed rule, not advice from the tool.
- **Vol-throttle note fired -> size down** (BMNR daily ATR 6.39% >
  `vol_throttle_atr_pct` 6). Informational; the routine never auto-trades.
- No HARD_STOP, TRAIL_STOP, MOMENTUM_STOP, or EMA_BREAK rule fired for either
  holding this run.
- If you execute anything from this report, run `/apply-trade` so holdings +
  the ledger update.

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/downside | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $25.60 | -97.2% | growth 5% / terminal 2.5% / discount 10% — **doesn't fit a crypto-treasury model, see caveat above** |
| NOW | $120.12 | $132.37 | -9.3% | growth 18% / terminal 3% / discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs** this run (expected — no card has been reviewed and
flipped to `status: planned` yet; all 78 cards in `setups/` are still `draft`).

## Draft & planned setups — 50 leads, 15 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank, unchanged `discover_top_n: 50`).
`scaffold.py --all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for
every lead without one (15 new: AAPL, APA, ASND, BLSH, FLYW, FRO, HBM, HPE,
KEYS, NTAP, NTR, SMCIP, TECK, TS, XOM; 63 existing cards left unchanged — 78
total). **Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals
to review and edit, never buys.**

22 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
rest are capped at RESEARCH by the asymmetry or catalyst-horizon gate):

| Ticker | R:R | Has card | Catalyst | Days out |
|---|---|---|---|---|
| AA | 20.0:1 | existing | earnings 2026-10-15 | 34 |
| LRCX | 18.8:1 | existing | earnings 2026-10-21 | 40 |
| TTMI | 17.5:1 | existing | earnings 2026-11-04 | 54 |
| UTHR | 15.9:1 | existing | earnings 2026-10-28 | 47 |
| AGI | 13.6:1 | existing | earnings 2026-10-28 | 47 |
| HAS | 11.7:1 | existing | earnings 2026-10-22 | 41 |
| FOX | 11.1:1 | existing | earnings 2026-10-29 | 48 |
| GDDY | 10.6:1 | existing | earnings 2026-10-29 | 48 |
| TER | 10.0:1 | existing | earnings 2026-10-21 | 40 |
| MSFT | 8.9:1 | existing | earnings 2026-10-28 | 47 |
| HBM | 7.8:1 | **new** | earnings 2026-10-29 | 48 |
| GOOGL | 7.0:1 | existing | earnings 2026-10-28 | 47 |
| IAG | 6.1:1 | existing | earnings 2026-11-03 | 53 |
| CDE | 6.0:1 | existing | earnings 2026-10-28 | 47 |
| TSLA | 5.8:1 | existing | earnings 2026-10-21 | 40 |
| EGO | 5.7:1 | existing | earnings 2026-10-29 | 48 |
| TECK | 5.4:1 | **new** | earnings 2026-10-22 | 41 |
| FLYW | 5.4:1 | **new** | earnings 2026-11-03 | 53 |
| AR | 5.2:1 | existing | earnings 2026-10-28 | 47 |
| CLS | 4.2:1 | existing | earnings 2026-10-26 | 45 |
| DOCN | 4.0:1 | existing | earnings 2026-11-04 | 54 |
| MU | 3.5:1 | existing | earnings 2026-09-30 | 19 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **CDE, AR, EGO, IAG, AGI** — the recurring precious-metals/mining cluster;
  mining-royalty financing structures raised the same open question in
  earlier runs (KGC was in that cluster before too, not in today's LEAD
  list). Still worth a real screen before spending review time on any of
  these cards.
- **MU** — earnings in just 19 days, the closest catalyst of the LEAD tier.
- **28 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — carried over from last run, still open] BMNR Shariah
   re-screen.** The mechanical ratio pre-check has now disagreed with the
   recorded "compliant" status for two consecutive runs with no re-screen
   recorded. The position has grown from +33.1% to +65.75% and 21.6% weight
   while this sits open. The automated pipeline will not re-surface this on
   its own beyond flagging it here — see Action Flag #1.
2. **[Time-boxed] NOW is ~1.5% above its trailing stop ($130.31)** — the
   tightest cushion either holding has shown recently; worth watching more
   closely than a routine HOLD would suggest.
3. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, two months after the position was
   opened.
4. **[Time-boxed] NOW earnings ~2026-10-23 to 2026-10-29** (not yet
   officially confirmed) — 42-48 days out; no action needed yet.
5. **[Housekeeping] 15 new DRAFT setup cards** added this run (78 total in
   `setups/`); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.93 Million Tokens, Total Crypto/Cash of $15.7 Billion — Morningstar/PR Newswire](https://www.morningstar.com/news/pr-newswire/20260908ny42129/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-593-million-tokens-and-total-crypto-and-total-cash-holdings-of-157-billion)
- [BMNR quote, Cantor Fitzgerald price target raise to $63.60 — CNBC](https://www.cnbc.com/quotes/BMNR)
- [ServiceNow, Inc. Form 10-Q FY2026 — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000076/now-20260630.htm)
- [ServiceNow (NOW) Earnings Date and Reports 2026 — MarketBeat](https://www.marketbeat.com/stocks/NYSE/NOW/earnings/)
