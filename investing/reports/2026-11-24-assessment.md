# Portfolio Assessment — 2026-11-24

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check, neither a fatwa — verify independently
in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 170-name raw pool; 4 dropped on liquidity,
76 dropped on the Shariah ratio knockout; top 50 kept) → `scaffold.py
--all-leads` (**26 new DRAFT cards**, 24 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps. Still no `transactions.csv`, so
`journal.py` and the discipline guard stay dormant.

**Since the last report (2026-08-19), about 3 months ago:** no trades were recorded. Both
holdings have fallen sharply. The book is down from $1,105.51 to **$777.99**
(−29.6%), and is now **−18.9% vs. cost**.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically, not advice.

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW — down −20.1% vs. cost; also
VALUATION_RICH — recorded P/E ~119, "hold, do not add").

| PM-grade record (recommend.py — mechanical proxy, not a conviction call) | |
|---|---|
| Price / cost | $91.90 vs. $114.97 → **−20.1%** |
| Conviction | LOW — "missing reward:risk or a stated thesis" (variant_view, stop, target, invalidation, pre-mortem all still `null`) |
| Shariah | **REVIEW — recorded compliant but screen is from 2026-06-09 (>100d, stale)** |
| DCF intrinsic value | $119.65 → +30.2% vs. price (assumptions: 18% 5y growth, 3% terminal, 10% discount) |
| Chandelier trail | $139.64 — **price is ~34% below it** (informational: trade_type `core` is exempt from TRAIL_STOP by design) |
| EMA fast | $103.93 — price below it |
| 6m momentum (skip last month) | +54.9% (the 6m-1 window excludes the recent slide; see the 1-month drop below) |
| 52w position | 7% of range (52w low $81.24) |
| Would buy today? | **false** per recommend.py |
| Review cadence | last_review 2026-06-15 → **162 days ago**, overdue vs. `review_cadence_days: 90` |

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired).

| PM-grade record (recommend.py — mechanical proxy) | |
|---|---|
| Price / cost | $13.40 vs. $15.43 → **−13.1%** (was +33.1% at last report) |
| Conviction | LOW — no thesis, stop, target or catalyst written in `holdings/bmnr.md` |
| Shariah | **REVIEW — recorded compliant 2026-07-07, now flagged stale by shariah.py** |
| DCF intrinsic value | −$6.53 (model does not fit a crypto-treasury business; ignore as a target) |
| Chandelier trail | $17.91 — price ~25% below it (core → exempt) |
| EMA fast | $17.44 — price below it |
| 6m momentum | +11.3% |
| Would buy today? | true per recommend.py (reads only the recorded Shariah field and gates; no thesis) |

Portfolio notes (verdict.py): only 2 holdings → concentration rules muted;
**vol throttle: BMNR ATR 11.1%, NOW ATR 7.1% — "size down"**.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| NOW | $91.96 | 7 | $114.97 | $643.69 | −20.0% | 82.7% |
| BMNR | $13.43 | 10 | $15.43 | $134.30 | −13.0% | 17.3% |

**Total value: $777.99** | Cost: $959.09 | **Total return −$181.10 (−18.9%)**

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale.** NOW was screened 2026-06-09
   and BMNR 2026-07-07; shariah.py marks both stale. The ratio pre-check passes
   on both this run (NOW debt 2.5% / liquid 6.6%; BMNR debt 0% / liquid 6.5%).
   But BMNR's business-activity check returned `null` this run, so it was not
   assessed. The **2026-08-19 report flagged a business-activity FAIL** for BMNR
   (`Capital Markets`, ETH-treasury/staking income). That question is still
   open. Re-screen both in Zoya/Musaffa. Do this before any add.
2. **[Rule] NOW DRAWDOWN_REVIEW fired** (−20% vs. cost). Your pre-set action
   is REVIEW: re-run "would I buy this here today?" recommend.py says false.
3. **[Hygiene] NOW re-underwrite is overdue** (162 days vs. a 90-day cadence).
   Stop, target, invalidation, variant view and pre-mortem are still `null`.
   Without them the engine can't size risk or tell you when you're wrong.
4. **[Hygiene] BMNR has no written thesis, stop or catalyst.** The card still says
   "NEW position — screen compliance before adding more."
5. **[Valuation] NOW P/E ~119** (recorded) — VALUATION_RICH: hold, do not add.

## Per-holding read (catalysts and news, web research, this run)

**NOW** — The stock is near the bottom of its 52-week range ($81.24–$175.00 per
MarketBeat).
- *Case to keep:* Q3 (reported Oct 28) revenue of $4.11B beat by about $20M. The full-year
  AI ACV target was raised to $1.7B+. Sell-side remains mostly Buy (36 Buy, 4 Hold,
  2 Sell). RBC kept Outperform with a $165 target. The DCF shows +30% under your
  stated assumptions. A Nov 17 Azure → ServiceNow AIOps integration demo was
  shown.
- *Case to trim or exit:* Adjusted EPS of $1.00 missed by $0.02. Expected
  cRPO/backlog growth is slowing, and that is exactly the deceleration your "What would
  change my mind" section names. UBS cut its target from $140 to $100 (Neutral) today,
  and RBC cut to $165. The drop is also tied to a broader AI-software selloff.
  An insider sold 474 shares at $93 on Nov 18. The price is ~34% below the
  chandelier trail. The position is 83% of the book.
- *Catalyst:* the next earnings date is not confirmed. Late January 2027 is
  typical, which is likely just outside the 60-day horizon.
- Your recorded invalidation is "subscription growth decelerating meaningfully
  below ~21–22% YoY." Check the Q3 subscription growth figure against it. I did
  not retrieve it this run.

**BMNR** — The stock fell 13.9% on Nov 20, which was the listed earnings date. The
cause was not confirmed in my search. It closed at $19.00 on Nov 5 and now sits near
the bottom of its 52-week range ($12.80–$42.09 per Investing.com). Bitmine posted a
crypto/cash holdings update on Nov 23 (details truncated in search). Your
outcome depends on ETH price and treasury/financing decisions, not on operations.
The Shariah business-activity question (flag 1) is the gating issue.

## Suggested actions (from YOUR rules)

- **Rule DRAWDOWN_REVIEW fired → REVIEW** (NOW, −20.1% vs. cost).
- **Rule VALUATION_RICH fired → hold, do not add** (NOW, P/E ~119).
- **Shariah staleness → re-screen** (NOW, BMNR).
- **review_cadence_days exceeded → re-underwrite** (NOW).
- **Vol throttle → size down** on any adds (both names).

The routine never auto-trades. If you execute anything, run `/apply-trade` so
holdings, the ledger and the journal update.

## DCF

| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $91.93 | +30.2% | g5y 18%, terminal 3%, r 10% |
| BMNR | −$6.53 | $13.42 | n/m | g5y 5%, terminal 2.5%, r 10% — model doesn't fit an ETH treasury |

## New ideas — discovery (leads.md refreshed, top 50)

**0 LEAD / 50 RESEARCH.** Nothing cleared every discovery gate this run. The
binding gate is mostly CATALYST: most earnings dates land in late Jan–Mar 2027,
after the 60-day horizon (2027-01-23). Several names have stops above
entry ("n/a" R:R) because price is already below its chandelier level. All rows
are **Shariah UNVERIFIED** with **EDGE NOT SUPPLIED**. `recommend.py`'s
`ideas` array is empty because `watchlist.md` has no gated names. **No
BUY-CANDIDATE this run.**

Top-ranked by the max-benefit composite (see `leads.md` for all 50):

| Ticker | R:R (discovery) | Catalyst | Card |
|---|---|---|---|
| UI | 11.2 | earnings 2027-02-05 | new draft |
| LSCC | 10.7 | 2027-02-08 | new draft |
| SANM | 20.0 | 2027-02-01 | new draft |
| COHR | 10.3 | 2027-02-03 | new draft |
| VIAV | 20.0 | 2027-02-03 | new draft |
| SNA | 8.7 | 2027-02-04 | new draft |
| APH | 6.8 | 2027-01-27 | existing |
| NET | 4.2 | 2027-02-09 | existing |
| TSLA | 4.7 | 2027-01-27 | existing |
| CF | 3.9 | 2027-02-17 | existing |

The discovery R:R values of 10–20:1 use a 52w-high structure target. Paired risk:
these targets need a full retrace of a prior high, and every stop is a
formula level. Read them as "room to run, if the setup works," never as an
expected outcome.

## Draft setups (26 new, machine-filled)

**RESEARCH — DRAFT awaiting your review (set status: planned to approve).**
Every level is a Yahoo formula output: pullback entry = EMA20, stop = chandelier
(HH22 − 3×ATR), T1 = entry + 1.5R. Approving one means editing what you disagree
with, setting `status: planned`, and recording a Zoya/Musaffa screen. Shariah is
`unverified` on all 26. The scaffold pre-check comments are on each card.

| Ticker | Setup | Entry | Stop | T1 | R:R | Catalyst | Gap plan |
|---|---|---|---|---|---|---|---|
| UI | pullback | 630.02 | 583.17 | 700.29 | 1.5 | 2027-02-05 earnings | no earnings in window |
| LSCC | pullback | 108.50 | 95.91 | 127.39 | 1.5 | 2027-02-08 | none in window |
| SANM | pullback | 156.68 | 136.75 | 186.57 | 1.5 | 2027-02-01 | none in window |
| COHR | pullback | 215.77 | 172.75 | 280.30 | 1.5 | 2027-02-03 | none in window |
| VIAV | pullback | 30.47 | 25.62 | 37.75 | 1.5 | 2027-02-03 | none in window |
| SNA | pullback | 360.21 | 351.17 | 373.79 | 1.5 | 2027-02-04 | none in window |
| FN | pullback | 330.82 | 279.18 | 408.29 | 1.5 | 2027-02-01 | none in window |
| TXN | pullback | 289.43 | 267.79 | 321.89 | 1.5 | 2027-01-26 | none in window |
| HSY | pullback | 172.57 | 164.03 | 185.40 | 1.5 | 2027-02-04 | none in window |
| TS | pullback | 57.79 | 56.88 | 59.15 | 1.5 | 2027-02-17 | none in window |
| AAPL | breakout | 360.68 | 334.09 | 400.56 | 1.5 | 2027-01-28 | none in window |
| LLY | breakout | 1474.59 | 1336.99 | 1680.99 | 1.5 | 2027-02-03 | none in window |
| ASND | breakout | 282.26 | 255.61 | 322.23 | 1.5 | none dated | none in window |
| BBY | earnings_run | 100.10 | 94.77 | 108.10 | 1.5 | 2026-11-24 (today) | exit_before — already moot |

**12 drafts are unusable as written (stop ≥ entry, no target):** APA, DDOG,
FRO, FTI, JBL, NTAP, NTNX, NUE, PR, PSX, VLO, XOM. For these names, price has
already fallen below the chandelier stop, so the formula can't produce a long
plan. Treat them as "no setup right now." This is a scaffold limitation and
worth a code fix (see follow-ups).

**No PLANNED/LIVE cards exist**, so no BUY-CANDIDATE can appear. The 24 older
draft cards are unchanged and their levels date from earlier runs, so
re-scaffold with `--force` before using any of them.

## Follow-ups (prioritized)

1. Re-screen **NOW** and **BMNR** in Zoya/Musaffa and record the dates. For
   BMNR, specifically resolve the business-activity question from the
   2026-08-19 report.
2. NOW REVIEW: decide whether the thesis survives slowing cRPO. Fill in
   `initial_stop`, `target_price`, `invalidation`, `pre_mortem`, and update `last_review`.
3. BMNR: write a thesis, stop and catalyst, or decide it doesn't belong in
   the book.
4. Optional code fixes: make `scaffold.py` skip or flag names with price below
   the chandelier stop instead of writing stop ≥ entry drafts. Also have
   `shariah.py` surface a `business_ok: null` result as a warning.
5. If you trade, run `/apply-trade`. A `transactions.csv` would let the
   discipline guard compare your results to a Shariah benchmark.

Short-term trading usually trails buy-and-hold after costs.

Sources: [MarketBeat — NOW up 4.8% (Nov 23)](https://marketbeat.com/instant-alerts/price-servicenow-nyse-now-stock-price-up-48-heres-what-happened-2026-11-23) ·
[MarketBeat — UBS cuts NOW PT to $100](https://marketbeat.com/instant-alerts/analyst-servicenow-nyse-now-price-target-cut-to-10000-by-analysts-at-ubs-group-2026-11-24) ·
[ad-hoc-news — RBC cuts NOW PT to $165](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-rbc-cuts-price-target-to-165-dollars/70549841) ·
[ad-hoc-news — NOW × Azure AIOps](https://ad-hoc-news.de/boerse/news/unternehmensnachrichten/servicenow-taps-microsoft-s-azure-to-route-cloud-alerts-straight-into-its-aiops-platform/70546793) ·
[Investing.com — NOW](https://www.investing.com/equities/servicenow-inc) ·
[Yahoo — BMNR history](https://uk.finance.yahoo.com/quote/BMNR/history/) ·
[Investing.com — BMNR](https://www.investing.com/equities/bitmine-immersion-tech) ·
[Robinhood — BMNR](https://robinhood.com/us/en/stocks/BMNR/)

---
*Not financial advice. I'm not a financial advisor. Verify every Shariah status
in Zoya/Musaffa before acting.*
