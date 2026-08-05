# Portfolio assessment — 2026-08-05

Decision support, not advice. Every figure below is mechanical output from
`rules.md`'s pre-set knobs or a live data pull — verify all Shariah status in
Zoya/Musaffa before acting on anything here.

## Verdicts (lead with this)

`verdict.py`: **BMNR -> HOLD** (DEFAULT — no rule fired) · **NOW -> HOLD**
(VALUATION_RICH — P/E ~119.02, hold, do not add). Only 2 holdings — the
concentration rule stays muted until >= 4 names. Portfolio note: **BMNR ATR
6.35% — size down per vol throttle** if adding.

| Ticker | Verdict | Price | Weight | Return | Trailing stop | Dist. to stop | 6m momentum |
|---|---|---|---|---|---|---|---|
| BMNR | HOLD | $18.14 | 18.2% | +17.6% | $14.86 | -18.1% | -33.8% |
| NOW | HOLD | $116.45 | 81.8% | +1.3% | $100.07 | -14.1% | +0.9% |

PM-grade record (`recommend.py` — mechanical proxies, not a real conviction call):

- **BMNR** — conviction LOW ("reward:risk -5.3:1 — skew too thin", driven by a
  DCF target that is not a meaningful methodology for this business, see below).
  Shariah PASS *on the recorded broker flag only* — see the flag below.
  `thesis_one_liner`: "NEW position — screen compliance in Zoya/Musaffa before
  adding more." Nothing else in the PM record is filled in (no variant view,
  catalyst, invalidation, pre-mortem) — this card is effectively empty past the
  entry note.
- **NOW** — conviction LOW ("reward:risk 0.2:1 — skew too thin" on the DCF-based
  target/stop the engine computes; this is a mechanical artifact of `verdict.py`'s
  chandelier stop vs. a DCF target, not a real asymmetry read for a core holding).
  Shariah PASS (recorded compliant, screened 2026-06-09, not stale).
  `conviction`, `variant_view`, `initial_stop`, `target_price`, `invalidation`,
  `pre_mortem` are all still `null` in the card's front-matter — same TODOs open
  since `last_review: 2026-06-15`. Not yet overdue against the 90-day
  `review_cadence_days`, but worth closing before the Q3 print.

## Snapshot

Total value: **$996.19** (2 open positions).

| Ticker | Shares | Cost basis | Price | Value | Weight | Return |
|---|---|---|---|---|---|---|
| BMNR | 10 | $15.43 | $18.14 | $181.11 | 18.2% | +17.4% |
| NOW | 7 | $114.97 | $116.45 | $815.08 | 81.8% | +1.3% |

## Action flags (priority order)

1. **[Mandate flag, not a price call] BMNR fails the automated Shariah ratio
   pre-check** — `shariah.py` flags industry `Capital Markets` as failing the
   business-activity screen, even though the broker app recorded the position
   `compliant` on 2026-07-07. This is worth a real re-screen, not a rubber
   stamp: BitMine's core business is now an Ethereum treasury/staking company
   (~5.8M ETH held, ~4.8% of total supply, plus a new institutional staking
   platform, "MAVAN") rather than a conventional operating business — that
   profile (large interest/yield-bearing crypto treasury, staking-fee income)
   is exactly the kind of thing a generic broker-app compliance flag can miss.
   The holding's own thesis note already says "screen compliance in Zoya/Musaffa
   before adding more" — this flag says: do that screen now, on the current
   business, not the original listing.
2. **[Valuation, recurring] NOW P/E ~119** — `VALUATION_RICH` rule fires again
   (hold, do not add); priced for continued high growth.
3. **[Stale field] NOW catalyst date needs updating** — the card still lists
   "Q2 FY2026 earnings" with `date: null` as the forward catalyst. That
   earnings report already happened on 2026-07-22 (beat: EPS $0.90 vs. $0.76
   est.; revenue $3.99B, +1.65% vs. consensus). The next scheduled catalyst is
   **Q3 2026 earnings, 2026-10-28** (guided ~20.5% YoY subscription growth,
   31% non-GAAP operating margin, per the Q2 call).
4. **[Infrastructure, still open]** No `transactions.csv`/`journal.csv` exist
   yet — the FIG sale and BMNR buy were recorded by hand-editing the holding
   `.md` files, not via `/apply-trade`. The discipline guard (net-of-benchmark
   performance tracking) stays unavailable until trades are logged through the
   script.

## Per-holding read

### BMNR — Bitmine Immersion Technologies
- **Case to keep**: up +17.4% since cost basis; broker app has it recorded
  compliant; small, deliberately-sized position (18.2% of a two-name, $996
  book).
- **Case to trim/re-underwrite**: (a) the compliance pre-check flag above is
  a real open question, not a technicality — the company's revenue mix is now
  dominated by holding and staking Ethereum, which raises the standard
  interest/riba-adjacent questions around staking yield that a screen should
  resolve explicitly, not infer from a generic "Capital Markets" SIC code;
  (b) 6-month momentum is **-33.8%** even though the position itself is
  green, meaning the cost basis was set near a local low, not on an uptrend —
  worth being honest that this is a bounce inside a longer downtrend; (c) the
  DCF intrinsic value ($0.72 vs. $18.14 price, -96%) is **not a meaningful
  number for this security** — a standard FCF-growth DCF doesn't model a
  company whose value is ~its ETH holdings times ETH's price, so don't read
  that -96% as a real downside estimate; it's a methodology mismatch, and
  `dcf.py` has no NAV-based mode for treasury companies. (d) BMNR also
  disclosed a fiscal year-end change (Aug 31 -> Dec 31) and a $4B buyback
  program (4.5M shares repurchased) — both corporate-structure items worth
  reading the filing on, not swing catalysts.
- I could not verify one figure surfaced in web search (a claimed one-day
  +14% move "on August 6") — that date is tomorrow relative to today
  (2026-08-05), so it's either a forward-dated/aggregator artifact or wrong;
  I'm flagging it as unverified rather than including it as fact.

### NOW — ServiceNow
- **Case to keep**: Q2 beat on both lines; guided Q3 subscription growth
  ~20.5% YoY with a still-strong 31% non-GAAP operating margin; durable
  enterprise-workflow subscription model; Shariah recorded compliant with a
  low purification % (3.35%), not stale.
- **Case to trim/re-underwrite**: P/E ~119 continues to price in sustained
  high growth — any deceleration (subscription growth, Armis integration
  hiccups, the FX headwind flagged for Q3 cRPO) would compress the multiple
  hard. DCF (18% 5y growth, 3% terminal, 10% discount) puts intrinsic value at
  $120.12 vs. $116.45 — only +3.2% upside on the base case, i.e., close to
  fairly valued rather than cheap. The PM record's qualitative fields
  (conviction, variant view, initial stop, target, invalidation, pre-mortem)
  are still all blank — there's no written variant view distinguishing this
  from "holding at consensus," which itself caps how much conviction the
  position should carry per the framework.

## Suggested actions (from your rules)

- **Rule VALUATION_RICH fired on NOW** (P/E ~119.02 >= `pe_rich: 50`) ->
  pre-set action: hold, do not add. Fact: trailing P/E 119.02.
- **Vol-throttle note fired on BMNR** (daily ATR% 6.35% >= `vol_throttle_atr_pct:
  6`) -> pre-set action: size down any addition. Fact: 22-period ATR% 6.35%.
- No SELL/TRIM/COMPLIANCE_GATE rule fired on either holding this run.

If you execute anything from this report, run `/apply-trade` so holdings and
the ledger update.

## DCF

| Ticker | Price | Intrinsic value | Upside | Assumptions (5y growth / terminal / discount) |
|---|---|---|---|---|
| BMNR | $18.14 | $0.72 | -96.0% | 5% / 2.5% / 10% — **not a meaningful model for a crypto-treasury company; see flag above** |
| NOW | $116.45 | $120.12 | +3.2% | 18% / 3% / 10% |

## New ideas (from `leads.md`, machine-discovered — none are buys)

`discover.py` refreshed the pool today (2026-08-05, top 50 by max-benefit
rank) and `scaffold.py --all-leads` filled 24 new DRAFT setup cards for names
that didn't already have one. **Every DRAFT card is unreviewed and Shariah
UNVERIFIED** — none can reach BUY-CANDIDATE until you review it, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa. `recommend.py`'s `ideas` array is empty because
`watchlist.md` has no hand-curated tickers yet — the table below is
discovery's own LEAD/RESEARCH verdict, not a re-gated recommendation.

Top names with a catalyst inside ~2 weeks:

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| KLIC | LEAD | existing | 8.4:1 | earnings 2026-08-05 | 0 |
| DUOL | LEAD | existing | 5.7:1 | earnings 2026-08-05 | 0 |
| TS | LEAD | new | 3.7:1 | earnings 2026-08-05 | 0 |
| CDE | LEAD | existing | 3.6:1 | earnings 2026-08-05 | 0 |
| WDC | RESEARCH | new | 2.6:1 | earnings 2026-08-05 | 0 |
| HST | RESEARCH | new | 0.4:1 | earnings 2026-08-05 | 0 |
| UTHR | RESEARCH | new | n/a | earnings 2026-08-05 | 0 |
| CF | RESEARCH | existing | n/a | earnings 2026-08-05 | 0 |
| PDFS | LEAD | new | 4.6:1 | earnings 2026-08-06 | 1 |
| CNQ | LEAD | existing | 3.6:1 | earnings 2026-08-06 | 1 |
| ESE | RESEARCH | new | 1.4:1 | earnings 2026-08-06 | 1 |
| ARW | RESEARCH | new | 0.7:1 | earnings 2026-08-06 | 1 |
| LIF | LEAD | existing | 5.5:1 | earnings 2026-08-10 | 5 |
| SMCI | LEAD | new | 4.2:1 | earnings 2026-08-11 | 6 |

Full pool is in `leads.md` (50 rows, includes ADI, ZS, CRDO, ULTA, MU, GOOGL,
MSFT, AMD, PLTR, AU and more, all still `unverified`/`draft`).

**Flags worth your attention before reviewing any of these:**
- **DELL** — score 75.9 (highest in the pool) but reward:risk is only 0.1:1;
  the asymmetry gate correctly caps it at RESEARCH despite the high score —
  a reminder the composite score is a ranking signal, not a gate pass.
- **PLTR, AU, CDE, MT** — carried over from prior runs: PLTR's government/
  defense-adjacent revenue line, AU/CDE's mining/royalty financing structure,
  and MT's historically tight engineered entry/stop/target band are all
  still open business-activity or data-quality questions worth resolving
  before spending review time on those cards. Nothing new to add this run.
- **TS, WDC, UTHR, HST, CF, KGC, HAS, DINO, FSLR** and other newly-scaffolded
  names are conventional-industry businesses with a clean ratio pre-check —
  still need the actual Zoya/Musaffa business screen, not an assumption.

## Follow-ups (priority order)

1. **[This run's standout] BMNR business-activity re-screen** — the recorded
   `compliant` flag predates (or doesn't reflect) BitMine's pivot to an
   Ethereum-treasury/staking business; get an explicit Zoya/Musaffa answer on
   the staking-yield and treasury-holding structure before adding to the
   position.
2. **[Housekeeping] NOW catalyst date** — update `holdings/now-servicenow.md`'s
   `catalyst` block to the confirmed Q3 2026 print (2026-10-28) now that Q2 has
   reported; the current `date: null` is stale.
3. **[Ongoing, low urgency] NOW PM-record TODOs** — conviction, variant view,
   initial stop, target price, invalidation, and pre-mortem are all still
   blank; due for a real re-underwrite before `last_review` hits the 90-day
   mark (~2026-09-13).
4. **[Housekeeping] 24 new DRAFT setup cards** added this run (60+ total in
   `setups/`); none are `planned`. Review at your own pace — several near-term
   earnings dates (today through mid-August) don't wait.
5. **[Infrastructure, still open]** No ledger yet — start logging trades via
   `/apply-trade` so `journal.py`'s per-setup expectancy report and the
   discipline guard have data to work with.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow (NOW) Q2 Earnings and Revenues Top Estimates — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html)
- [ServiceNow, Inc. - Form 8-K - FY2026 (Q2 results)](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000072/erq2fy26.htm)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.8 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-8-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302840749.html)
- [BitMine Immersion Technologies (BMNR) – Ethereum's Largest Treasury Company — CoinGecko](https://www.coingecko.com/learn/what-is-bmnr-bitmine-ethereum-treasury-tom-lee)
- [Bitmine Immersion Technologies Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
