# Portfolio assessment — 2026-09-16

Decision support only — not financial advice. Every figure here is a
mechanical output of `rules.md` or a broker-recorded/pre-check flag, not a
recommendation. Shariah status shown is a broker-app record or a mechanical
ratio/business-activity pre-check, never a fatwa — verify independently in
Zoya/Musaffa before acting on anything below. Compliance is a gate, not a
tiebreaker.

## 0. Auto-discovery + scaffold (ran first)

`discover.py` and `scaffold.py --all-leads` ran live against Yahoo Finance
(rate-limited but reachable — no DATA_GAP). `leads.md` was rewritten
(top 50 by max-benefit rank, generated 2026-09-16): **18 LEAD / 32
RESEARCH**, none above LEAD tier (discovery output is never more than LEAD
by design). 31 of the 50 already had a setup card; scaffold auto-filled
**19 new DRAFT cards** for the rest (NTNX, ASND, DDOG, PR, TS, HPE, XOM,
NTR, SMCIP, APA, NTAP, AAPL, SMTC, SOLV, DDS, BBY, FRO, SNA, TECK) —
`setups/` now holds **82 cards, still 0 `planned`** (only the unused
`_template.md` carries a `planned` string). Every card remains
machine-filled and unreviewed; none can reach BUY-CANDIDATE until you
review, edit, and flip `status: planned`, and screen it compliant.

## 1. Verdicts (lead with this)

Two holdings — concentration checks are muted until the book has >= 4 names
(`min_names_for_concentration`).

**BMNR -> HOLD** (rule: `DEFAULT` — no rule fired)
- Price $22.665 | weight 18.7% | return **+46.9%** since cost $15.43
- Trailing (chandelier) stop **$21.6642** — price is ~4.4% above it
- 6m momentum (skip last month): **-19.4%**
- R-multiple: n/a (no `initial_stop` recorded on the card)
- Portfolio note: **vol-throttle** — BMNR's ATR is 7.8%, above the 6% throttle
  threshold; size down before adding.
- PM-grade record (recommend.py, mechanical proxy): conviction **LOW**
  ("reward:risk -21.7:1 — skew too thin"); target $0.72 via DCF intrinsic
  value (see caveat under DCF below — this number is not meaningful for a
  crypto-treasury vehicle and should not be read as a real target); stop
  $21.6642; downside 4.5%. `would_buy_today: true` is a placeholder from an
  unset front-matter flag, not a real underwrite — see PM_FRAMEWORK gaps below.

**NOW -> HOLD** (rule: `VALUATION_RICH` — P/E ~119.02, hold, do not add)
- Price $140.95 | weight 81.3% | return **+22.6%** since cost $114.97
- Trailing stop **$129.9691** — price is ~7.8% above it
- 6m momentum: **+0.8%** (roughly flat)
- PM-grade record: conviction **LOW** ("reward:risk -1.9:1 — skew too
  thin" — the DCF target sits below spot, see below); thesis
  "Durable enterprise-workflow subscription grower; AI-agent expansion is
  the forward driver"; catalyst (soft) "Q2 FY2026 earnings + Armis
  integration progress"; downside 7.8% to trailing stop.

## 2. Snapshot

| Ticker | Price | Shares | Cost | Value | Weight | Return |
|---|---|---|---|---|---|---|
| BMNR | $22.665 | 10 | $15.43 | $226.65 | 18.68% | +46.89% |
| NOW | $140.92 | 7 | $114.97 | $986.44 | 81.32% | +22.57% |
| **Total** | | | | **$1,213.09** | 100% | |

Two-name book — NOW alone is 81% of the account, well past the 22%
single-name cap in `rules.md`, but the concentration rule is explicitly
muted below 4 names (small-account carve-out, not an oversight).

## 3. Action flags (priority order)

1. **[Mandate — recurring, unresolved] BMNR Shariah ratio pre-check
   disagrees with the recorded "compliant" status.** `shariah.py`'s
   business-activity pre-check flags BMNR's sector/industry
   (Financial Services / **Capital Markets**) as failing the screen
   ("core business fails screen"), while the holding's front-matter still
   carries `status: compliant` from the 2026-07-07 screen. This is the
   same open flag from the last two reports — the automated pipeline will
   not re-surface it on its own; it needs a fresh, deliberate Zoya/Musaffa
   re-screen given BMNR's business model (crypto-treasury / ETH-staking
   operator) may not map cleanly onto the "Capital Markets" classification
   it inherited from GICS-style sector tagging.
2. **[Valuation]** NOW: P/E ~119 vs `pe_rich` threshold of 50 —
   `VALUATION_RICH` fired -> hold, do not add (already reflected in the
   verdict above).
3. **[Volatility]** BMNR: daily ATR ~7.8%, above the 6% vol-throttle
   threshold — size down before adding to this position.
4. **[Housekeeping — recurring, still open]** BMNR's holding file is still
   missing every PM-grade field (`thesis_one_liner`, `variant_view`,
   `initial_stop`, `target_price`, `pre_mortem`, `conviction`) — 10 weeks
   after the position was opened. Without `initial_stop` there is no
   R-multiple and no real HARD_STOP trigger; the engine is only using the
   ATR-derived chandelier stop as a fallback.
5. **[Infrastructure — still open]** No `transactions.csv` ledger exists
   yet (`journal.py` errors: file not found). The FIG close and BMNR buy
   referenced in earlier reports still aren't logged — until they are, the
   discipline guard (net-of-cost performance vs a Shariah benchmark) can't
   run at all.

## 4. Per-holding read

**BMNR — Bitmine Immersion Technologies**
- *Case to keep*: up 46.9% since entry; ETH treasury continues to scale
  (holdings reported at 5.96M ETH / ~$15.8B total crypto+cash as of
  2026-09-14, per company PR); no confirmed thesis-break in current news.
- *Case to trim/review*: no recorded `initial_stop`, `target_price`, or
  `pre_mortem` — the position has effectively no written exit plan two and
  a half months in; 6m momentum is negative (-19.4%) even as price sits
  above cost; the Shariah compliance question above is unresolved and is
  now the single largest compliance question in the book by weight.
- Recent news (web, 2026-09): ETH/crypto holdings updates continue
  (5.96M ETH, ~$15.8B total crypto+cash+securities as of 2026-09-13/14);
  stock traded $23.76–$24.98 on 2026-09-15 (slightly above the $22.665
  yfinance close used above — normal same-day divergence); a Tom Lee
  keynote is scheduled at KBW on 2026-09-30 (soft, non-earnings catalyst;
  no hard earnings date surfaced). Nothing found that breaks the thesis.

**NOW — ServiceNow**
- *Case to keep*: subscription growth intact, AI-agent (Zurich platform)
  narrative still the forward driver; 6m momentum roughly flat, price is
  still 7.8% above trailing stop; catalyst (Q3 FY2026 earnings) is
  confirmed for **2026-10-28**, 42 days out — inside `catalyst_horizon_days`
  (60), so this is not dead money.
- *Case to trim/review*: P/E ~119 is rich even for the growth rate assumed
  in the card's own DCF (18% 5y growth), and the DCF intrinsic value
  ($120.12) sits below the current price ($140.95, -14.8%) — the position
  is being held at a premium to its own stated model, which is the
  `VALUATION_RICH` rule's point. No `variant_view` is written, so there is
  no articulated reason the market's rich multiple is wrong; the card
  currently just accepts consensus pricing.
- Recent news (web): Q3 FY2026 earnings confirmed for 2026-10-28
  (after close); no thesis-breaking news found; ~$35M FX headwind flagged
  in Q2 guidance for Q3, immaterial to the core subscription thesis.

## 5. Suggested actions (from YOUR pre-set rules in `rules.md`)

- **Rule `VALUATION_RICH` fired -> NOW: HOLD, do not add** (P/E 119.02 >=
  `pe_rich` 50).
- **Vol-throttle note fired -> BMNR: size down** (ATR 7.8% >
  `vol_throttle_atr_pct` 6%) if considering adding.
- No `SELL`, `TRIM`, `REVIEW`, `TAKE_PARTIAL`, `HARD_STOP`, `TRAIL_STOP`,
  `MOMENTUM_STOP`, `EMA_BREAK`, `THESIS_BREAK`, `TARGET_REACHED`, or
  `TIME_STOP` rule fired on either holding this run.
- These are your own pre-committed rules from `rules.md` resolving against
  today's data — not advice generated ad hoc.

If you execute anything based on this report, run `/apply-trade` so the
holdings files and ledger stay in sync.

## 6. DCF

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $22.665 | **-96.8%** | growth_5y 5%, terminal 2.5%, discount 10% — a standard cash-flow DCF is a poor fit for a crypto-treasury holding company whose value is driven by ETH/BTC marked-to-market plus staking yield, not operating cash flow. Treat this number as a model-mismatch artifact, not a real valuation signal. |
| NOW | $120.12 | $140.95 | **-14.8%** | growth_5y 18%, terminal 3%, discount 10% — a more standard SaaS DCF; still shows the stock trading above its own model's fair value at the current multiple. |

## 7. New ideas (from discovery + watchlist)

`watchlist.md` has **no hand-curated tickers** right now (it's still the
blank template) — so `recommend.py`'s `ideas` array (which reads only from
watchlist.md) came back empty. There is nothing to promote to BUY-CANDIDATE
this run; every candidate name in the system today lives in the raw
`leads.md` discovery pool below, and every one of them is capped at LEAD or
RESEARCH by construction (EDGE unsupplied, Shariah UNVERIFIED).

Top of today's 50-name discovery pool by max-benefit rank (full list in
`leads.md`; not reproduced in full here):

| Ticker | Verb | R:R | Score | Setup card | Earnings |
|---|---|---|---|---|---|
| MU | LEAD | 13.1:1 | 48.9 | has card | 2026-09-30 |
| MSFT | LEAD | 10.6:1 | 43.4 | has card | 2026-10-28 |
| NTNX | RESEARCH | 9.6:1 | 61.3 | new DRAFT this run | 2026-11-25 |
| SIMO | LEAD | 13.2:1 | 39.5 | has card | 2026-10-29 |
| AR | LEAD | 16.0:1 | 32.5 | has card | 2026-10-28 |
| CDE | LEAD | 15.6:1 | 30.3 | has card | 2026-10-28 |
| TSLA | LEAD | 7.4:1 | 35.3 | has card | 2026-10-21 |
| PLTR | LEAD | 7.1:1 | 40.1 | has card | 2026-11-02 |
| GOOGL | LEAD | 4.2:1 | 38.0 | has card | 2026-10-28 |
| DDOG | LEAD | 4.6:1 | 48.3 | new DRAFT this run | 2026-11-05 |

Flags worth noting before spending review time on any of these:
- **PLTR** carries the same unresolved government/defense business-activity
  question flagged in prior runs — nothing new to add this run.
- **CDE, AR, AGI, IAG** — the recurring precious-metals/mining cluster is
  back at the top of the LEAD tier again; the mining-royalty financing
  structure question from earlier runs is still open and unresolved.
- **AMD, DELL, DINO, NET, CVE, APA, FRO, BBY** all show sub-3:1 or near-zero
  reward:risk and land in RESEARCH purely on the asymmetry gate — high
  mechanical score, thin skew.
- 19 of the 50 leads (NTNX, ASND, DDOG, PR, TS, HPE, XOM, NTR, SMCIP, APA,
  NTAP, AAPL, SMTC, SOLV, DDS, BBY, FRO, SNA, TECK) had no setup card before
  this run; scaffold.py wrote DRAFT proposals for all of them this run —
  see `setups/` (all `status: draft`, none `planned`).

## 8. Draft & planned setups

All **82** cards in `setups/` are `status: draft` (machine-filled by
`scaffold.py`, unreviewed) — verdict `RESEARCH — DRAFT awaiting your review
(set status: planned to approve)`. None are `planned` or `live`, so there
is currently **no card in the system that can reach BUY-CANDIDATE** — every
one needs your review, edits to entry/stop/target/invalidation logic where
you disagree, a flip to `status: planned`, and a human Zoya/Musaffa
compliance screen before `recommend.py` can re-gate it. 19 of the 82 are
brand-new this run (listed in section 7); the remaining 63 carry over
unreviewed from prior runs. Given the volume, there is no ranking here
beyond what's already in `leads.md` — review at your own pace.

## 9. Follow-ups (priority order)

1. **[Recurring, unresolved] BMNR Shariah re-screen** — the ratio pre-check
   vs. recorded "compliant" status conflict is now three reports old.
   Largest compliance question in the book by weight (18.7%).
2. **[Housekeeping, recurring] BMNR holding file PM fields** — still all
   null (`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem`) 10 weeks after entry; no R-multiple can be computed without
   `initial_stop`.
3. **[Time-boxed] NOW earnings 2026-10-28** — 42 days out; confirmed via
   web search this run. No action needed yet; track the AI-agent /
   Armis-integration narrative into the print.
4. **[Housekeeping] 19 new DRAFT setup cards** added this run (82 total in
   `setups/`); none `planned`. Review at your own pace — no urgency implied
   by volume alone.
5. **[Infrastructure, still open] No ledger** — `transactions.csv` still
   doesn't exist; start logging via `/apply-trade` to unlock the discipline
   guard (net-of-cost performance vs. Shariah benchmark).

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.96 Million Tokens, and Total Crypto and Total Cash Holdings of $15.8 Billion — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-96-million-tokens-and-total-crypto-and-total-cash-holdings-of-15-8-billion-302877149.html)
- [BitMine Immersion Stock Rallies Friday: What's Happening? — Benzinga](https://www.benzinga.com/trading-ideas/movers/26/09/61744911/bitmine-immersion-stock-rallies-friday-whats-happening)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings — Morningstar / PR Newswire](https://www.morningstar.com/news/pr-newswire/20260908ny42129/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-593-million-tokens-and-total-crypto-and-total-cash-holdings-of-157-billion)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [NOW Earnings Dates, Upcoming and Historical — MarketChameleon](https://marketchameleon.com/Overview/NOW/Earnings/Earnings-Dates/)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
