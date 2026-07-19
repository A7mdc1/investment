# Portfolio Assessment — 2026-07-19

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 140-name pool, top 50 by max-benefit rank —
first attempt timed out at 90s on the Yahoo fetch, re-ran in the background
and completed) → `scaffold.py --all-leads` (6 new DRAFT setup cards for leads
without one: UTHR, SFD, AMKR, NEM, ESE, FORM; 44 existing cards left
unchanged, including 25 scaffolded earlier this same cycle for last week's
leads that hadn't been reviewed yet) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps.
`journal.py` not run separately — still 0 closed trades logged
(`transactions.csv` doesn't exist yet — discipline guard stays dormant until
you log via `/apply-trade`).

**Portfolio composition changed since 2026-07-13**: FIG was sold (closed
2026-07-13, realized P/L +$54.95, exited on the compliance gate) and BMNR was
bought. The book is now BMNR + NOW, 2 holdings.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$15.69**,
**+1.7%** vs. $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-9.1:1** (DCF-based skew argues against holding, not for adding — see caveat below) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see flag below** |
| DCF intrinsic value | **$0.72** vs. $15.69 price -> **-95.4%** ("upside") — **the DCF model is not a sane fit for this business (see note)** |
| Trailing stop (chandelier) | $14.0499 — price is $1.64 above it |
| 6m momentum (skip last month) | -50.4% |
| Portfolio note | ATR **6.82%** — flagged for the vol-throttle (size down) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction is LOW and the DCF read is not usable here |
| What changes verdict | thesis_broken: true, a SELL technical trigger, or the Shariah screen flipping |

**⚠ Flag (not from verdict.py, from shariah.py's ratio pre-check):** BMNR's
Yahoo sector/industry metadata is **Financial Services / Capital Markets**,
which trips the ratio pre-check's core-business knockout ("industry 'Capital
Markets' matches 'capital markets' — core business fails screen") even though
the position is recorded **compliant** via the broker app (screened
2026-07-07). BMNR's actual business — an Ethereum treasury/staking vehicle
(holds ~4.9M ETH, ~$11.3B in crypto + cash per its July 2026 investor
updates) — is exactly the kind of holding-company structure the "Capital
Markets" classification is meant to catch, and it's also why the standard DCF
(cash-flow-from-operations model) produces a nonsensical $0.72 intrinsic value
against a $15.69 price: BMNR isn't valued on discounted operating cash flows,
it trades on its ETH NAV plus a staking-yield/treasury-strategy premium. This
is a genuine conflict between the recorded compliant status and the
mechanical pre-check that's worth re-verifying in Zoya/Musaffa specifically
on the business-activity test (not just the ratio test) — a broker-app label
from 2 weeks ago doesn't resolve a structural question like this.

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$103.24**, **-10.2%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | MEDIUM — reward:risk 2.7:1 (moderate skew) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $103.24 price -> **+16.6% upside** to the model |
| Trailing stop (chandelier) | $96.9859 — price is $6.25 above it |
| 6m momentum (skip last month) | -24.7% |
| Would buy today? | Mechanically yes per recommend.py's gates |
| What changes verdict | thesis_broken: true, a SELL technical trigger, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names
  (`min_names_for_concentration: 4`).
- **`last_review` on NOW's card is 2026-06-15 — 34 days stale** as of this
  run. `review_cadence_days` is 90, so this doesn't trigger a rule yet, but
  it's the older of the two records and worth a fresh "would I buy this here
  today?" pass, especially with earnings 3 days out.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.69 | 10 | $15.43 | $156.90 | +1.7% | 17.8% |
| NOW | $103.24 | 7 | $114.97 | $722.68 | -10.2% | 82.2% |

**Total value: $879.58** | Cost: $958.09 | **Total return: ~-8.2%** (-$78.51 unrealised)

NOW has dropped further since the 2026-07-13 run (was $112.72, now $103.24,
-8.4% in 6 days) ahead of its earnings print. BMNR is a new position (bought
after the 2026-07-13 FIG sale) and sits modestly positive. The book overall
swung from +3.6% (2026-07-13, when FIG's rally was carrying it) to -8.2% now
— driven almost entirely by NOW's slide, and NOW is 82% of the book.

## Action flags (priority order)

1. **[Compliance — needs re-verification] BMNR business-activity flag** — the
   mechanical ratio pre-check fails BMNR on the "Capital Markets" industry
   knockout even though the broker app records it compliant. This is the
   single most important open question in the book right now: it's your
   second-largest position (17.8%) and the question is structural (what kind
   of company is this), not a ratio that will refresh itself. Re-screen
   specifically the business-activity test in Zoya/Musaffa — don't rely on
   the 2026-07-07 broker label alone.
2. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22 — 3 days out.**
   Consensus revenue ~$3.92B (+22% y/y). The July 22 print will be read less
   on headline subscription revenue than on whether cRPO growth clears
   ~19.5%, whether ex-Armis growth holds near 20%, and management's tone on
   late-June deal timing — Armis is modeled to cost ~0.75pp of operating
   margin and ~2pp of FCF margin as the integration proceeds.
   [ts2.tech](https://ts2.tech/en/servicenow-stock-slides-as-ibm-budget-warning-turns-july-earnings-into-a-core-growth-test/) ·
   [TradingView/Zacks](https://www.tradingview.com/news/zacks:af814e0e1094b:0-servicenow-set-to-report-q2-earnings-buy-sell-or-hold-the-stock/)
3. **[Price action / NOW] IBM's budget-warning read-through** — coverage
   this cycle frames the print as "a core-growth test" after a peer
   (IBM) flagged enterprise software budget softness; NOW's 6m momentum is
   already the weaker of the two holdings at -24.7% (vs. BMNR's -50.4%, which
   is a shorter-history, higher-vol name so less comparable).
   [ts2.tech](https://ts2.tech/en/servicenow-stock-slides-as-ibm-budget-warning-turns-july-earnings-into-a-core-growth-test/)
4. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add.
5. **[Vol throttle / BMNR] ATR 6.82%** — flagged for size-down per
   `vol_throttle_atr_pct: 6`; informational given no rule forces action.
6. **[New leads this run]** Top of the refreshed pool by max-benefit rank:
   **GOOGL** and **TSLA** (both LEAD, both SPUS holdings, both share NOW's
   2026-07-22 earnings date) at reward:risk 10.1:1 and 13.4:1 respectively —
   the widest R:R at the top of the list this run. All 20 top leads are
   UNVERIFIED Shariah (ratio pre-check only); none has been reviewed or
   screened.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** Ethereum treasury holdings keep scaling — ~4.9M ETH staked
(~4.8% of total ETH supply) and ~$11.3B in total crypto + cash per the July
2026 investor updates, with the "Alchemy of 5%" target (5% of ETH supply in
12 months) 96% reached. Projected annualized ETH staking yield ~$284M at
scale (2.70% 7-day yield). Position is small (+1.7%) and recorded Shariah
compliant.
[PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html) ·
[TimothySykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_14/)

**Case to trim/exit (compliance question, independent of price):** the ratio
pre-check's business-activity knockout (Financial Services / Capital Markets)
directly conflicts with the broker app's compliant label. A crypto-treasury
company that raises capital (it closed a $273.8M preferred-stock offering on
June 10) to accumulate and stake an interest-bearing digital asset is a
structure Zoya/Musaffa screens are specifically built to catch or clear —
this needs the actual screen, not the pre-check or the broker label alone.
The standard DCF is not usable here (see verdict table) — don't read the
-95.4% number as a valuation call; it's a model mismatch, not a signal.
6m momentum -50.4% reflects this being a young, thin-history, high-vol name,
not necessarily thesis decay.

**HOLD — but the compliance question is the thing to resolve, not the
price.** This is a new, small position; the two independent flags (business-
activity pre-check conflict + DCF-model mismatch) both point the same
direction: verify the fundamentals of what this company actually is before
treating "recorded compliant" as settled.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (3 days out);
consensus ~22% revenue growth; Now Assist net-new ACV is outperforming
forecasts (customers spending $1M+ growing >130% y/y per management
commentary); DCF shows +16.6% upside to intrinsic value ($120.42) at recorded
assumptions; price is still above its chandelier trailing stop ($103.24 vs.
$96.99).
[TradingView/Zacks](https://www.tradingview.com/news/zacks:af814e0e1094b:0-servicenow-set-to-report-q2-earnings-buy-sell-or-hold-the-stock/) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-set-report-q2-earnings-151900170.html)

**Case to trim/watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
worsened to -24.7% (peer softness read-through from IBM's budget commentary,
per this cycle's coverage); Armis is modeled to be a near-term margin drag
(~0.75pp operating, ~2pp FCF) as it's integrated; price down another 8.4%
since last run ahead of the print — the market appears to be pricing in some
risk to Thursday's numbers already.
[ts2.tech](https://ts2.tech/en/servicenow-stock-slides-as-ibm-budget-warning-turns-july-earnings-into-a-core-growth-test/) ·
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add. Unchanged from last run.
- **No rule fired -> BMNR**: DEFAULT/HOLD per verdict.py — but see the
  compliance flag above, which verdict.py's mechanical rules don't (and
  can't) evaluate; it's not encoded as a rule.
- **VOL_THROTTLE note -> BMNR**: ATR 6.82% >= `vol_throttle_atr_pct: 6` —
  size-down note, informational only (not a trim trigger by itself).
- **DRAWDOWN_REVIEW not firing -> NOW**: -10.2% vs. the 20% threshold — not
  yet, but this is worse than last run's -2.0% and worth watching into
  earnings.
- **TRAIL_STOP -> both**: does NOT fire (`trade_type: core` exempts both from
  the technical trailing-stop rule); both remain above their computed levels.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $15.69 | -95.4% (model mismatch — see note above) | growth_5y 5%, terminal 2.5%, discount 10% |
| NOW | $120.42 | $103.24 | +16.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — it only evaluates
watchlist entries, and no card has been reviewed and flipped to
`status: planned` yet). All new-idea surfacing this cycle comes from machine
discovery below instead.

## Draft & planned setups — 50 leads, 6 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (140 names from SPUS holdings +
the `growth_technology_stocks` / `undervalued_large_caps` screens) and
rewrote **`leads.md`** (top 50 by max-benefit rank). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead that didn't
already have one — 6 new this run (**UTHR, SFD, AMKR, NEM, ESE, FORM**); the
other 44, including 25 scaffolded earlier in this same cycle for last week's
leads, were left unchanged. **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.** None can reach
BUY-CANDIDATE until you review the card, edit anything you disagree with, set
`status: planned`, and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| GOOGL | LEAD | existing | 10.1:1 | earnings 2026-07-22 | 3 |
| TSLA | LEAD | existing | 13.4:1 | earnings 2026-07-22 | 3 |
| ALKT | LEAD | existing | 9.0:1 | earnings 2026-07-29 | 10 |
| FICO | LEAD | existing | 7.0:1 | earnings 2026-07-29 | 10 |
| P | LEAD | existing | 13.9:1 | earnings 2026-08-26 | 38 |
| AVGO | LEAD | existing | 15.0:1 | earnings 2026-09-03 | 46 |
| LIF | LEAD | existing | 8.1:1 | earnings 2026-08-10 | 22 |
| UTHR | LEAD | new | 6.3:1 | earnings 2026-07-29 | 10 |
| MSFT | LEAD | existing | 5.0:1 | earnings 2026-07-29 | 10 |
| AMD | LEAD | existing | 3.6:1 | earnings 2026-08-04 | 16 |
| DUOL | LEAD | existing | 4.0:1 | earnings 2026-08-05 | 17 |
| GDDY | LEAD | existing | 4.3:1 | earnings 2026-07-30 | 11 |
| VRNS | RESEARCH | existing | 2.8:1 | earnings 2026-07-28 | 9 |
| DELL | RESEARCH | existing | 2.4:1 | earnings 2026-09-03 | 46 |
| PLTR | LEAD | existing | 4.9:1 | earnings 2026-08-03 | 15 |
| SFD | RESEARCH | new | 2.7:1 | earnings 2026-07-28 | 9 |
| MT | RESEARCH | existing | 1.7:1 | earnings 2026-07-30 | 11 |
| ZS | LEAD | existing | 4.8:1 | earnings 2026-09-02 | 45 |
| NVDA | LEAD | existing | 3.4:1 | earnings 2026-08-26 | 38 |
| STX | RESEARCH | existing | n/a | earnings 2026-07-28 | 9 |

All 20 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **GOOGL / TSLA (top of this run's ranking, both SPUS holdings, both share
  NOW's 2026-07-22 earnings date)** — widest reward:risk in the top 20, but a
  mega-cap ratio pre-check being clean is not the same as a business-activity
  screen: Tesla's financing-arm interest income and Alphabet's ad/interest-
  bearing cash mix both need the actual Zoya/Musaffa screen. Same nuance
  flagged last run.
- **MT, PLTR** — carried over from prior runs' flags (MT's implausibly tight
  engineered entry/stop/target band; PLTR's government/defense
  business-activity question). Nothing new to add.
- **NEM (new lead, no card yet — precious-metals miner)** — same
  mining/royalty-financing-structure question flagged for AU/CDE in prior
  runs; worth the same scrutiny before scaffolding a card, given the pattern.
- **STX (n/a reward:risk, RESEARCH not LEAD)** — no computable R:R from the
  discovery-stage formula; needs an actual look before treating the score
  alone as a signal.

## Follow-ups (priority order)

1. **[New, most important] BMNR business-activity re-screen** — verify in
   Zoya/Musaffa specifically whether an ETH-treasury/staking vehicle passes
   the core-business test; don't rely on the 2026-07-07 broker-app label
   given the ratio pre-check's direct conflict.
2. **[Time-boxed] NOW earnings 2026-07-22** — 3 days out; watch cRPO growth
   vs. ~19.5%, ex-Armis growth vs. ~20%, and any read-through from IBM's
   enterprise-budget commentary.
3. **[Housekeeping] NOW's `last_review` is 34 days stale (2026-06-15)** — a
   fresh "would I buy this here today?" pass would be timely with earnings
   imminent, even though the 90-day cadence rule hasn't fired yet.
4. **[Housekeeping] 6 new DRAFT setup cards** added this run (UTHR, SFD,
   AMKR, NEM, ESE, FORM); 31 DRAFT cards now sit unreviewed across two
   cycles. None are `planned`, none can reach BUY-CANDIDATE.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Set to Report Q2 Earnings: Buy, Sell or Hold the Stock? — TradingView/Zacks](https://www.tradingview.com/news/zacks:af814e0e1094b:0-servicenow-set-to-report-q2-earnings-buy-sell-or-hold-the-stock/)
- [ServiceNow Set to Report Q2 Earnings: Buy, Sell or Hold the Stock? — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-set-report-q2-earnings-151900170.html)
- [ServiceNow stock slides as IBM budget warning turns July earnings into a core-growth test — ts2.tech](https://ts2.tech/en/servicenow-stock-slides-as-ibm-budget-warning-turns-july-earnings-into-a-core-growth-test/)
- [ServiceNow Inc (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [BMNR Stock Climbs As Ethereum Treasury Bet Scales To $11.3B — TimothySykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_14/)
