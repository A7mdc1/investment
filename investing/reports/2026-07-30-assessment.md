# Portfolio Assessment — 2026-07-30

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (48 new DRAFT setup cards auto-filled for leads
without one; 14 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` ran clean: still 0 closed trades logged to a
ledger (FIG's realized P/L lives only in its closed holding file — see
Follow-ups). This is the first assessment since **2026-07-13** (17 days —
longer than the prior weekly cadence); in the gap, FIG was sold and BMNR
bought (recorded 2026-07-13, closing that run's 7-cycle-unresolved
compliance flag).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.74**, up
**+15.0%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.7:1 (DCF-based target is *below* the current price — see caveat below) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but the mechanical ratio pre-check flags the business**: industry "Capital Markets" matches the capital-markets exclusion list. See Action flag #1. |
| DCF intrinsic value | $0.72 vs. $17.74 price -> **-96.0%** — a standard discounted-cash-flow model is a poor fit for an ETH-treasury holding company (value tracks crypto NAV + staking yield, not operating cash flow); flagged, not literal |
| Trailing stop (chandelier) | $14.7439 — price ~20.3% above it |
| 6m momentum (skip last month) | -55.1% |
| Portfolio note | ATR 6.72% — vol-throttle note (size down) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW pending your own variant view |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah ratio flag being confirmed as a real knockout in Zoya/Musaffa |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$109.51**, **-4.75%** vs. the $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 1.0:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale), clean ratio pre-check (debt 2.1%, liquid 5.5%) |
| DCF intrinsic value | $120.12 vs. $109.57 price -> **+9.6% upside** to the model |
| Trailing stop (chandelier) | $98.9432 — price is $10.57 above it |
| 6m momentum (skip last month) | -23.4% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
  BMNR's 6.72% daily ATR triggers the vol-throttle note; size down if adding.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.74 | 10 | $15.43 | $177.40 | +15.0% | 18.8% |
| NOW | $109.51 | 7 | $114.97 | $766.57 | -4.7% | 81.2% |

**Total value: $943.97** | Cost: $959.09 | **Total return: ~-1.6%** (-$15.12
unrealised). The book is smaller and more concentrated than last run
($1,610.49 with FIG+NOW) — the FIG exit realized +$54.95, and the new BMNR
position (10 sh, $154.30 cost) is roughly a fifth the dollar size of the FIG
position it replaced, so NOW now carries 81% of the book versus 49% before.

## Action flags (priority order)

1. **[Mandate / BMNR] Ratio pre-check disagrees with the recorded compliance
   status.** The broker app has BMNR recorded `compliant` (screened
   2026-07-07), but the mechanical business-activity pre-check flags its
   Yahoo-classified industry as **"Capital Markets"** — a core-business
   exclusion category, not a borderline ratio. BMNR's actual business is an
   Ethereum treasury/staking vehicle (not a bank or broker-dealer), so this
   may well be a sector-classification artifact rather than a real
   knockout — but that's exactly the kind of thing only a real Zoya/Musaffa
   screen resolves, not an assumption either way. This is the single
   largest open question on the book right now.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[DCF / BMNR] Standard DCF model is a poor fit for this business type** —
   it produces a nonsensical -96% "downside" because BMNR's value is
   crypto-NAV-driven, not FCF-driven. Treat the DCF row on BMNR as
   not applicable rather than as a sell signal; NAV-per-share vs. ETH
   holdings would be the more relevant model if you want a real intrinsic
   check on this name.
4. **[Catalyst / NOW] Q2 FY2026 earnings already reported 2026-07-23** (a
   week before this run) — beat on both lines: revenue $3.99B (vs. $3.93B
   est.), EPS $0.90 (vs. $0.86 est.), subscription growth re-accelerated to
   ~23% cc from ~19%, AI ACV crossed $1B with >40% sequential acceleration,
   and full-year subscription guidance was raised for the second time this
   year to $15.755-15.770B. The one soft spot: Q3 subscription guide
   ($3.975-3.980B) landed just under the ~$4B street consensus, capping the
   post-earnings pop. [Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/is-surging-ai-contract-value-and-mixed-earnings-altering-the) ·
   [TradingKey](https://www.tradingkey.com/news/market-movers/262053323-market-movers-now-20260724)
5. **[New this run] Two same-day earnings catalysts land 2026-07-30 (today)**
   among the fresh leads: **AU** (AngloGold, LEAD, R:R 6.4:1) reports
   2026-07-31, and both **MT** (ArcelorMittal) and **FSLR** (First Solar,
   RESEARCH) report today, 2026-07-30 — informational, none are cards you
   hold or have promoted.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** ETH treasury continues to scale — $11.1B total crypto +
cash as of early July, 5.74M ETH held (4.8% of total supply), 4.88M ETH
staked (~$8.8B), and management has been actively buying back shares
(11.6M shares repurchased in July, 6.1M in the most recent week) — a signal
of confidence in the discount to NAV. Stock is up ~15% vs. cost and climbed
from the mid-$14s to high-$17s through late July.
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_27/) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-74-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-1-billion-302818093.html)

**Case to trim / watch:** the holding's own front-matter is nearly empty —
no `conviction`, `catalyst`, `initial_stop`, `target_price`, `invalidation`,
or `pre_mortem` filled in (see Follow-ups #1). 6m momentum is deeply
negative (-55.1%) reflecting ETH's own volatility, daily ATR of 6.72% is
well above the vol-throttle threshold (6%), and — the open item that
matters most — the ratio pre-check's "Capital Markets" flag hasn't been
independently resolved against the recorded compliant status. This is a
NEW, small (18.8% weight) position; the thesis has had one screening date
(2026-07-07) and no re-underwrite since.

**No verdict rule fired — HOLD by default, not by conviction.** The
compliance question (Action flag #1) is the one item that could move this,
and it's unresolved.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 print (reported 2026-07-23, since last assessment) beat
on revenue and EPS, subscription growth re-accelerated to ~23% cc, AI ACV
crossed the $1B mark with accelerating sequential adds, and full-year
subscription guidance was raised for the second time in 2026. DCF shows
+9.6% upside to intrinsic value at recorded assumptions (18% 5y growth, 10%
discount). Shariah ratio pre-check is clean (debt 2.1%, liquid assets 5.5%
of market cap) alongside the recorded compliant status.

**Case to trim / watch:** P/E ~119 keeps VALUATION_RICH firing — priced for
continued high growth; Q3 subscription guide landed just under street
consensus, the one number tempering enthusiasm post-print. 6m momentum is
still negative (-23.4%) despite the earnings pop, and the position is now
81% of a 2-name book — well above where concentration rules would normally
cap a single name once the account has >= 4 positions.

**VALUATION_RICH verdict: HOLD, do not add.** Nothing here breaks the
thesis; the earnings beat is a positive, near-term data point in its favor.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add. P/E ~119 vs. the 50 threshold.
- **No rule fired -> BMNR**: HOLD by default — no SELL/TRIM/REVIEW trigger hit.
- **DRAWDOWN_REVIEW not firing** on either name (BMNR +15.0%, NOW -4.7%,
  both well inside the 20% threshold).
- **TRAIL_STOP** does not fire on either (`trade_type: core` on NOW exempts
  it; BMNR has no `trade_type` set in its front matter — worth adding, see
  Follow-ups).
- **VOL_THROTTLE note -> BMNR**: ATR 6.72% > 6% threshold — size down if
  you add to this name.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $17.74 | -96.0% | growth_5y 5%, terminal 2.5%, discount 10% — **not a good model fit for a crypto-treasury company**; treat as informational, not a sell signal |
| NOW | $120.12 | $109.57 | +9.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run (empty — no watchlist input,
and no card has been reviewed and flipped to `status: planned` yet).

## Draft & planned setups — 50 leads, 48 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank — up from 20 last run per an
unrelated widen to the discovery pool size). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (48
new cards; 14 — ADI, GDDY, PLTR, DUOL, LIF, ALKT, AU, AMD, ZS, PAY, CF,
JNJ, MT, ALAB — already existed and were left unchanged). **Every DRAFT card
is unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.** None can reach BUY-CANDIDATE until you review the card, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa. All 63 files in `setups/` are still `draft` — no
card has ever been promoted to `planned` or `live` across any run so far.

Top 20 by max-benefit rank:

| Ticker | Verdict (leads.md) | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| WDC | LEAD | new | 10.4:1 | earnings 2026-08-05 | 6 |
| UTHR | LEAD | new | 13.2:1 | earnings 2026-08-05 | 6 |
| GWRE | LEAD | new | 11.0:1 | earnings 2026-09-03 | 35 |
| SMCI | LEAD | new | 15.5:1 | earnings 2026-08-11 | 12 |
| ADI | LEAD | existing | 11.2:1 | earnings 2026-08-19 | 20 |
| GDDY | LEAD | existing | 7.0:1 | earnings 2026-07-30 | 0 |
| PAAS | LEAD | new | 10.2:1 | earnings 2026-08-12 | 13 |
| PLTR | LEAD | existing | 19.2:1 | earnings 2026-08-03 | 4 |
| KEYS | LEAD | new | 8.9:1 | earnings 2026-08-18 | 19 |
| DUOL | LEAD | existing | 7.7:1 | earnings 2026-08-05 | 6 |
| NVDA | LEAD | new | 11.4:1 | earnings 2026-08-26 | 27 |
| TS | LEAD | new | 6.8:1 | earnings 2026-08-05 | 6 |
| LIF | LEAD | existing | 6.7:1 | earnings 2026-08-10 | 11 |
| ALKT | RESEARCH | existing | 9.4:1 | earnings 2026-10-28 | 90 |
| AEM | RESEARCH | new | 11.5:1 | earnings 2026-10-28 | 90 |
| SFD | LEAD | new | 5.6:1 | earnings 2026-08-11 | 12 |
| AU | LEAD | existing | 6.4:1 | earnings 2026-07-31 | 1 |
| AMD | LEAD | existing | 4.1:1 | earnings 2026-08-04 | 5 |
| ZS | LEAD | existing | 6.4:1 | earnings 2026-09-02 | 34 |
| KGC | RESEARCH | new | 11.4:1 | earnings 2026-11-10 | 103 |

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over from prior runs' flags: government/defense
  business-activity question, unresolved, still worth a real Zoya/Musaffa
  screen before spending review time on the card despite its 19.2:1 R:R.
- **AU / AEM / KGC / PAAS / SMCI (mining/metals names, several new this
  run)** — royalty-financing and interest-income structure questions common
  to miners are still open; ratio pre-check alone doesn't clear the
  business-activity screen for these.
- **AU reports tomorrow (2026-07-31)** — if you're inclined to look at it,
  the window to do real diligence before the print is basically closed.
- **NVDA / AVGO / LLY / AAPL / MSFT / JNJ (SPUS-holding leads)** — same
  standing note as prior runs: SPUS holding it is not the same as a
  business-activity screen for each name individually.

## Follow-ups (priority order)

1. **[New, high-priority] BMNR ratio pre-check flag** — resolve whether the
   "Capital Markets" classification is a Yahoo sector-mapping artifact or a
   real business-activity concern, in Zoya/Musaffa. This is the most
   consequential open item on the book: BMNR is a new position and the
   recorded-compliant / ratio-flagged status disagree.
2. **[Housekeeping] BMNR's holding file is missing the PM decision-record
   fields** that NOW's file has (conviction, catalyst, initial_stop,
   target_price, invalidation, pre_mortem, trade_type, last_review — all
   blank/absent). Filling these in is what lets verdict.py/recommend.py do
   more than default to HOLD.
3. **[Ongoing] PLTR business-activity screen** — repeatedly the
   highest-R:R lead across runs; still not screened.
4. **[Housekeeping] 48 new DRAFT setup cards** added this run (63 files
   total in `setups/`, all still `draft`); none are `planned`, none can
   reach BUY-CANDIDATE. Several near-term catalysts (WDC/UTHR/SMCI/DUOL/TS
   all report within the next ~2 weeks) if you want to prioritize review.
5. **[Infrastructure — still open]** No `transactions.csv`/`journal.csv`
   ledger exists yet — FIG's +$54.95 realized P/L is recorded only in its
   closed holding file. Start logging trades via `/apply-trade` to unlock
   the discipline guard (journal.py: 0/20 closed trades, sample too small).

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Trader Focus — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_27/)
- [Bitmine Immersion Technologies (BMNR) ETH/cash holdings update — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-74-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-1-billion-302818093.html)
- [Is Surging AI Contract Value And Mixed Earnings Altering The Investment Case For ServiceNow (NOW)? — Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/is-surging-ai-contract-value-and-mixed-earnings-altering-the)
- [ServiceNow Inc Stock (NOW) Moved Up by 6.85% on Jul 24 — TradingKey](https://www.tradingkey.com/news/market-movers/262053323-market-movers-now-20260724)
