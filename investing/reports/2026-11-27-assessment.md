# Portfolio Assessment — 2026-11-27

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status below is the broker app's recorded screen or a
mechanical ratio/business-activity pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 169-name raw pool, top 50 kept) →
`scaffold.py --all-leads` (29 new DRAFT cards; 21 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py`, all live. Yahoo rate-limited the crumb fetch
(HTTP 429) but every script returned data, so there are no data gaps.
`journal.py` was not run because there is still no `transactions.csv`.

**Since the last report (2026-08-19), about 14 weeks ago:** the book fell from
$1,105.51 to **$787.09** (−28.8%). Both positions are now below cost. No trades
are recorded since then.

## Verdicts (lead with this)

These are YOUR rules from `rules.md`, resolved mechanically. They are not advice.

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Price **$13.81**, **−10.5%**
vs. $15.43 cost. Chandelier trailing stop $17.85: price is **~23% below it**,
but `trade_type: core` (defaulted, since the file doesn't set it) exempts the
position from TRAIL_STOP. 6m momentum (skip-month) +14.4%. R-multiple n/a (no
`initial_stop`).

| PM-grade record (recommend.py; mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW: no thesis or reward:risk recorded |
| Shariah (recorded) | compliant (broker_app, 2026-07-07). **STALE** (>100 days); recommend.py marks it **REVIEW** |
| Shariah (mechanical pre-check) | **FAIL**: industry `Capital Markets`, core business fails the screen (2nd consecutive run) |
| Target / method | DCF −$6.53 (meaningless for an ETH treasury; see DCF section) |
| Stop | chandelier $17.85 (already breached) |
| Would buy today? | recommend.py says yes, but that ignores both the stale screen and the pre-check fail |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 ≥ 50). Price
**$92.72**, **−19.4%** vs. $114.97 cost. That is **0.6 pts from
DRAWDOWN_REVIEW** (−20%). Chandelier stop $135.65: price is **~32% below it**
(core is exempt). The position sits at 7% of its 52-week range. 6m momentum
(skip-month) +20.7%. That figure is stale: it skips the last month, so it
misses most of the post-earnings collapse.

| PM-grade record (recommend.py; mechanical proxy) | |
|---|---|
| Conviction | LOW: no variant view, stop, or target recorded |
| Shariah (recorded) | compliant (broker_app, 2026-06-09). **STALE** (~5.5 months); recommend.py marks it **REVIEW** |
| Shariah (mechanical pre-check) | PASS (debt 2.5%, liquid 6.5%) |
| Target / method | DCF $119.65 (+29%, assumptions below) |
| Would buy today? | recommend.py says yes; your own re-underwrite is overdue (`last_review` 2026-06-15, past the 90-day cadence) |

**Portfolio notes (verdict.py):**
- Only 2 holdings, so concentration rules stay muted (NOW = 82.5% of the book).
- **Vol throttle fired for both names:** BMNR ATR 10.96%, NOW ATR 7.01% (limit 6%). Size down per your rule.

## Snapshot (live)

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $13.81 | 10 | $15.43 | $138.05 | −10.5% | 17.5% |
| NOW | $92.72 | 7 | $114.97 | $649.04 | −19.4% | 82.5% |

**Total $787.09** | Cost $959.09 | **Unrealised −$172.00 (−17.9%)**

Benchmark context: SPUS fell from ~$59.2 (late Aug) to $54.39 (−8%). Both
holdings did materially worse than the halal benchmark over the window.

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale.** NOW was last screened
   2026-06-09 and BMNR 2026-07-07. `rules.md` COMPLIANCE_SCREEN says
   "screen > 1 quarter old → REVIEW before any add". **Engine gap:**
   `verdict.py` only fires COMPLIANCE_SCREEN for `unknown`/`doubtful` status,
   never for staleness. That is why both verdicts still read HOLD even though
   `shariah.py` and `recommend.py` both report the screens as stale. Also,
   NOW reported Q3 results on Oct 28, and your rules say to re-test each
   audited statement.
2. **[Mandate] BMNR business-activity pre-check FAILS again** (`Capital
   Markets`). This is the second run in a row, and it is still not reconciled
   with the recorded `compliant`. Its revenue is still dominated by ETH
   staking yield on a ~$11B treasury. A confirmed fail = COMPLIANCE_GATE →
   SELL (absolute, independent of P/L).
3. **[Drawdown] NOW −19.4%**, right at the 20% DRAWDOWN_REVIEW line. One more
   soft session fires REVIEW. The thesis needs a real re-check now, not after
   the rule trips (see the per-holding read).
4. **[Valuation / NOW]** VALUATION_RICH uses the *recorded* `pe: 119.02` and
   `last_price: 106.40` in the holding file. Both are stale after the 40% fall
   and should be refreshed.
5. **[Volatility]** Both names exceed the 6% ATR vol-throttle.
6. **[Housekeeping]** BMNR's holding file still has no thesis, stop, target,
   invalidation, or pre-mortem, about 20 weeks after entry. NOW's PM fields
   (conviction, stop, target, invalidation, pre-mortem) are still `null`.

## Per-holding read

### NOW — ServiceNow
**What happened:** Q3 FY26 was reported Oct 28. Revenue was $4.11B (+20.5%
YoY), a beat. Adjusted EPS was $1.00 vs. $1.02 expected, a slight miss. The
full-year subscription-revenue guide was nudged *up* to $15.78–15.79B. The
stock still had its **worst day on record (−27%) on Oct 29**. The selling was
driven by weaker forward subscription-growth expectations and AI-disruption
worries across software, then continued to ~$88 by Nov 20.
[CNBC](https://www.cnbc.com/2026/10/29/servicenow-now-earnings-q3-2026.html) ·
[Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-4981127) ·
[Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/servicenow-now-stock-price-sinks-as-q3-results-expose-profit) ·
[SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm)

**Case to keep:** Revenue growth (~20.5%) is still close to the ~21–22% your
"what would change my mind" line set as the bar, and guidance was raised, not
cut. The DCF (18% growth) now shows +29% to intrinsic value, where August
showed −6.6%. That is a multiple reset, not (yet) a broken business.

**Case to trim/exit:** Your own "change my mind" trigger is *subscription
growth decelerating meaningfully* or a guidance cut tied to AI/Armis. The
market is pricing exactly that deceleration risk forward. The position is 82%
of the book, with no stop, target, or invalidation written down, so there is
no pre-committed exit, and the rule set exempts it from the trailing stop.
The price is near its 52-week low.

**Your decision to make:** re-underwrite against your written trigger (the
next forward sub-growth guide is the evidence). Then either fill in
`initial_stop` / `invalidation`, or decide you no longer hold the thesis. Do
not average down on an unexamined thesis (your discipline guard).

### BMNR — Bitmine Immersion Technologies
**What happened:** ETH fell from ~$2,261 (Nov 1) to ~$1,713 (Nov 22), and
BMNR's reported total holdings fell from $14.5B to $11.1B over November.
Bitmine says it caps ETH buying at 5% of supply. It declared a $0.01 common
dividend (record date Dec 8, paid Dec 29). The stock is down ~50% from its
late-September ~$27.5.
[Nasdaq / company PR](https://www.nasdaq.com/press-release/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens) ·
[SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm) ·
[CNN Markets](https://www.cnn.com/markets/stocks/BMNR)

**Case to keep:** It is the largest ETH treasury, still accumulating and
staking, and the price is a levered proxy for an ETH rebound. It is a small
weight (17.5%).

**Case to exit:** The compliance question (Flag #2) is unresolved and now
stale. The price is a direct function of ETH, with no operating-business
cushion. There is no written thesis or exit plan.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired → NOW:** HOLD, do not add (based on the stale recorded P/E).
- **VOL_THROTTLE fired → BMNR, NOW:** size down / de-risk note.
- **COMPLIANCE_SCREEN *should* fire → BMNR, NOW** (screen > 1 quarter old →
  REVIEW before any add), per the rules.md prose. verdict.py doesn't encode
  staleness, so it is listed here manually.
- **DRAWDOWN_REVIEW → NOW:** not fired, at −19.4% vs the −20% threshold.
- **Re-underwrite cadence (90 days) exceeded → NOW** (`last_review` 2026-06-15)
  and BMNR (never reviewed).
- **TRAIL_STOP:** price is below the chandelier for both, but `trade_type: core`
  exempts them. If either was meant as a swing/momentum trade, this would be a
  SELL. Set `trade_type` deliberately on BMNR (currently defaulted).

*If you execute anything, run `/apply-trade` so holdings + ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Up/(down) | Assumptions |
|---|---|---|---|---|
| BMNR | −$6.53 | $13.81 | n/m | default 5% growth / 2.5% terminal / 10% discount. A cash-flow DCF does not fit an ETH-treasury company; treat as a data gap |
| NOW | $119.65 | $92.72 | +29.1% | growth_5y 18%, terminal 3%, discount 10% (from holding file). Upside depends on 18% growth holding for 5 years, which is exactly what the market doubts |

## New ideas (watchlist.md)

`watchlist.md` is still empty, so `recommend.py`'s `ideas` array returned
**0** entries and there are **0 BUY-CANDIDATEs**. No card in `setups/` has
been flipped to `status: planned`.

## Draft & planned setups — 50 leads, 29 fresh DRAFT cards

Discovery used SPUS holdings plus the growth-tech and undervalued-large-cap
screens (169 names) and kept the top 50 in `leads.md`. Only **4 clear to LEAD
tier**. The other 46 are capped at RESEARCH by the asymmetry or
catalyst-horizon gate. Most earnings dates are now Jan–Feb 2027, outside the
60-day window.

| Ticker | Tier | R:R (discovery) | Entry / target / stop (discovery est.) | Catalyst | Card |
|---|---|---|---|---|---|
| AVGO | LEAD | 17.6:1 | ~310.96 / 493.59 / 307.38 | earnings 2026-12-09 | existing, **stale** |
| SNX | LEAD | 12.1:1 | ~225.60 / 298.02 / 224.82 | earnings 2027-01-07 | existing, **stale** |
| TXN | LEAD | 3.4:1 | ~280.78 / 330.72 / 265.98 | earnings 2027-01-26 | **new** |
| RCL | LEAD | 3.5:1 | ~314.34 / 350.43 / 304.16 | earnings 2027-01-26 | existing, **stale** |

**Stale-card warning:** AVGO, SNX and RCL cards were scaffolded in earlier
runs and are skipped without `--force`. Their levels and catalysts are already
in the past: AVGO's card targets the 2026-09-02 print with entry $364.41, and
its stop sits *above* entry; SNX's card targets 2026-09-24; RCL's targets
2026-07-28. Re-scaffold with `scaffold.py --force` or edit by hand before
reviewing. The very tight discovery stops on AVGO (−1.2%) and SNX (−0.3%)
are what inflate their R:R. The `0.5×ATR` floor applies inside `reward_risk()`,
but read those ratios sceptically.

**TXN (new DRAFT): RESEARCH, awaiting your review (set `status: planned` to approve)**
- setup_type: earnings_run; entry ~$281.28 ahead of the 2027-01-26 print
- stop $265.94: chandelier (HH22 $317.20 − 3×ATR $17.09)
- target T1 $304.29 (+1.5R), T2 $327.30 (+3R); structure ceiling = 52-week high $330.53. Card R:R at T1 = 1.5:1, **below the 2.0 swing floor**; at T2 it is 3:1
- invalidation: no positive drift 5 sessions pre-print / gives back > 1 ATR
- gap plan: `no_earnings_in_window` (21-day window ends before the print)
- Shariah: pre-check business OK, ratios OK. UNVERIFIED; screen in Zoya/Musaffa

Every level is a formula output. Approval means editing what you disagree with
and flipping `status: planned`. Shariah stays `unverified` on every card by
construction.

**Flags across the lead list:** there is a large energy/refiner cluster this
run (XOM, VLO, PSX, APA, PR, DINO, CVE, CNQ, FRO) and steel/metals (NUE,
STLD, TS). **PLTR** carries over again with its open government/defense
business-activity question. **HST** is a REIT (lodging), and **FOX** is media.
Both are worth a careful business screen before spending review time.

## Follow-ups (priority order)

1. **Re-screen NOW and BMNR in Zoya/Musaffa.** Both are stale. For BMNR,
   specifically settle the business-activity question.
2. **Re-underwrite NOW** against your written "change my mind" trigger, post
   Q3. Write `initial_stop` + `invalidation` + `pre_mortem`, or decide the
   thesis no longer holds. It is 82% of the book with no pre-committed exit.
3. **Decide BMNR's role.** Set `trade_type`, a thesis, and an exit. As core it
   is exempt from a stop it already broke by 23%.
4. **Refresh NOW's recorded `pe` / `last_price` / 52-week fields**, which are
   stale after the drop.
5. **[Engine]** Consider making `verdict.py` fire COMPLIANCE_SCREEN when the
   screen is > 1 quarter old, to match `rules.md` (shariah.py already computes
   `stale`).
6. **[Housekeeping]** 29 new DRAFT cards (92 cards total, none planned). Run
   `--force` to refresh the stale AVGO/SNX/RCL cards if you want to review them.
7. **[Infrastructure]** There is still no `transactions.csv`, so the
   discipline guard stays dormant. Log the FIG sale and BMNR buy via
   `/apply-trade`.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow (NOW) earnings Q3 2026 — CNBC](https://www.cnbc.com/2026/10/29/servicenow-now-earnings-q3-2026.html)
- [Earnings call transcript: ServiceNow Q3 2026 — Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-4981127)
- [ServiceNow Stock Price Sinks As Q3 Results Expose Profit Strain — Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/servicenow-now-stock-price-sinks-as-q3-results-expose-profit)
- [ServiceNow Stock Falls 18%: Q3 2026 Earnings & Outlook — INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook)
- [ServiceNow Q3 FY2026 8-K — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm)
- [Bitmine ETH holdings press release — Nasdaq](https://www.nasdaq.com/press-release/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens)
- [Bitmine 8-K (Nov 2026) — SEC](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm)
- [BMNR quote & headlines — CNN Markets](https://www.cnn.com/markets/stocks/BMNR)
