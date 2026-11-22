# Portfolio Assessment — 2026-11-22

Not financial advice. This is decision support only: every buy, sell and hold call
is yours. The Shariah status below is either the broker app's recorded screen or a
mechanical ratio/business-activity pre-check. Neither is a fatwa. Verify in
Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 169-name raw pool, 74 dropped by the Shariah
ratio/business knockout, 4 dropped by the liquidity floor, top 50 kept) →
`scaffold.py --all-leads` (**27 new DRAFT setup cards**, 23 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py`. All of these ran on live data with no gaps. There is still no
`transactions.csv`, so the discipline guard stays dormant.

**Since the last report (2026-08-19), about 3 months ago:** no trades were
recorded. The book fell from **$1,105.51 to $743.07 (−32.8%)**. Both holdings
dropped sharply. NOW lost about 32% and BMNR about 37%.

## Verdicts (lead with this)

These are YOUR rules resolving mechanically, not advice.

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW, −23.8% vs. cost. VALUATION_RICH also
fired: hold, do not add). Live price **$87.61** against a cost of $114.97. The
price sits at **4% of its 52-week range** ($81.24–$239.62).

| PM-grade record (recommend.py — mechanical proxies, not a conviction call) | |
|---|---|
| Conviction | LOW: no reward:risk or stated edge to self-assess |
| Shariah | **REVIEW**: recorded compliant, but the screen dated 2026-06-09 is now stale (>100d) |
| DCF intrinsic value | $119.65 vs. $87.61 → +36.6% (assumes 18% 5y growth, 3% terminal, 10% discount) |
| Chandelier trailing stop | $139.70. Price is ~37% **below** it. TRAIL_STOP fires only for swing, momentum or catalyst trades, and NOW is `core`, so no SELL is triggered |
| 6m momentum (skip last month) | +53.7% (the lookback window still includes the summer rally) |
| Would buy today? | **No** (recommend.py) |
| R-multiple | n/a: no `initial_stop` set |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Live price **$12.98** against a
cost of $15.43 (−15.9%). The verdict ignores this run's Shariah pre-check fail
(see Flag #1).

| PM-grade record (recommend.py — mechanical proxies) | |
|---|---|
| Conviction | LOW: the holding file has no thesis, target, stop or pre-mortem |
| Shariah (recorded) | **REVIEW**: broker_app compliant, screened 2026-07-07, now stale |
| Shariah (ratio pre-check, this run) | **FAIL**: industry `Capital Markets`, so the core business fails the screen (2nd consecutive run) |
| DCF intrinsic value | −$6.53. Not meaningful: a cash-flow DCF doesn't fit an ETH-treasury company |
| Chandelier trailing stop | $18.82. Price is ~31% below it. No rule fires because BMNR is `core` |
| 6m momentum | +19.2% |
| Would buy today? | Mechanically yes, but that only reads the recorded Shariah field and cannot see the pre-check fail |

Portfolio notes: there are only 2 holdings, so concentration rules stay muted until
there are at least 4. The vol throttle fired on both names (ATR: BMNR 11.1%, NOW 7.5%).

## Snapshot (live)

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $12.98 | 10 | $15.43 | $129.80 | −15.9% | 17.5% |
| NOW | $87.61 | 7 | $114.97 | $613.27 | −23.8% | 82.5% |

**Total value: $743.07** | Cost: $959.09 | **Total return: −22.5% (−$216.02 unrealised)**

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are now stale.** NOW was screened 2026-06-09 and
   BMNR 2026-07-07. Re-screen both in Zoya/Musaffa.
2. **[Mandate — carried over, still open] BMNR fails the business-activity
   pre-check** (`Capital Markets`). Last run's research found an ETH-treasury model:
   staking-yield revenue, a large crypto treasury, and preferred dividends. Gate 1
   treats a confirmed fail as an absolute SELL, whatever the P/L. This flag has now
   come up on 2 runs. FIG's flag stayed open for 7 runs before it was settled.
3. **[Drawdown / NOW] DRAWDOWN_REVIEW fired at −23.8%.** NOW reported FQ3 on
   2026-10-28. Adjusted EPS was $1.00 vs. ~$1.02 consensus, its first miss in six
   quarters. Revenue was $4.106B (+20.5% YoY), slightly above estimates. Q4 cRPO
   guidance was 18.5% vs. ~19% expected. The full-year AI ACV target was *raised* to
   $1.7B. The CFO cited Armis acquisition debt costs and lower interest income. Shares
   fell ~18.7% to ~$122 the next morning. They now trade at $87.61, so the slide has
   continued for about another 28%. I could not confirm a specific cause for the
   November leg.
   [Stocktwits](https://stocktwits.com/news-articles/markets/equity/now-stock-declines-double-digits-after-hours-on-earnings-miss-and-ai-concerns/cZUQ2ikR9GA) ·
   [Finviz](https://finviz.com/news/411446/why-is-servicenow-stock-falling-187-in-premarket-trading) ·
   [Tiger](https://www.itiger.com/news/2679241731)
4. **[Holding files incomplete]** Neither holding has an `initial_stop`,
   `target_price`, `invalidation` or `pre_mortem`. NOW's `catalyst.date` still points
   at Q2 earnings. Because both are `core`, no stop-based rule can ever fire on them.
   That is why −24% and −16% drawdowns still read HOLD/REVIEW, not SELL.
5. **[DCF caveat / BMNR]** Treat the negative DCF as a data gap, not a valuation call.
6. **[Discovery] 50 leads, 0 at LEAD tier.** 39 are capped by ASYMMETRY_GATE and 11
   by CATALYST_GATE. Most earnings dates fall in late Jan/Feb 2027, outside the
   60-day window. Many rows show "reward-risk n/a" because price sits *below* its
   chandelier stop (stop > entry). This is a broad pullback signature across the
   pool, not a set of clean setups.

## Per-holding read

### NOW — ServiceNow
**Case to keep:** Revenue growth held at ~20.5%. The AI ACV target was raised to
$1.7B. The DCF (stated assumptions above) puts intrinsic value ~37% above price. The
price is near the 52-week low, which is where your note says "value or falling knife
— check why."
**Case to cut or trim:** Two of the risks your holding file lists have started to
show up. Your "what would change my mind" names a guidance cut tied to AI-agent or
Armis traction. cRPO guidance decelerated to 18.5%, and management tied part of the
EPS shortfall to Armis financing. P/E is still ~119 (recorded value). The position is
82.5% of the book, and the price has kept falling after earnings.
**Open question for you:** does 18.5% cRPO count as "decelerating meaningfully below
~21–22%"? Your file does not set a number. Writing one into `invalidation` would let
THESIS_BREAK resolve this mechanically next time.

### BMNR — Bitmine Immersion
**Case to keep:** The latest dated update I found (Sept 2026) shows ~5.96M ETH held
and the largest ETH treasury globally. It remains a leveraged ETH proxy.
[Finviz](https://finviz.com/news/391579/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-596-million-tokens-and-total-crypto-and-total-cash-holdings-of-158-billion)
**Case to flag:** The compliance question is unresolved (Flag #2). There is no
written thesis, stop or target. ATR is 11%, so this is very volatile. I could not
find November 2026 news, so the current ETH and treasury figures are unconfirmed.

## Suggested actions (from YOUR rules, rules.md)

- Rule **DRAWDOWN_REVIEW** fired on NOW → your pre-set action is REVIEW: re-underwrite
  the position ("would I buy here today?"). recommend.py says no.
- Rule **VALUATION_RICH** fired on NOW → hold, do not add.
- **No averaging down on a broken thesis** (discipline guard). This matters if you are
  considering adding to NOW at the lows. Decide first whether the thesis is intact.
- **Vol throttle** fired on both names → size down any adds.
- No SELL rule fired. TRAIL_STOP/EMA_BREAK apply only to swing or momentum trade types,
  and no `initial_stop` is set.

If you execute anything, run `/apply-trade` so holdings and the ledger update.

## DCF

| Ticker | Intrinsic | Price | Gap | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $87.61 | +36.6% | growth 18% 5y, terminal 3%, discount 10% (holding-file override) |
| BMNR | −$6.53 | $12.98 | n/m | growth 5%, terminal 2.5%, discount 10% (defaults; model doesn't fit) |

## New ideas

`recommend.py`'s `ideas` array is empty: `watchlist.md` has no curated names. From
discovery, **no name reaches LEAD**, and none can be BUY-CANDIDATE. Every row is
Shariah UNVERIFIED with EDGE not supplied. Near-term earnings inside the window:
SMTC (11-23), BBY / NTNX / DELL / ADI (11-24), NTAP / CRDO (12-01), AVGO (12-09),
CIEN (12-10), JBL (12-16), MU (12-17). Most of these show stop > entry, so the
asymmetry gate fails. Of the near-term names, only BBY has a computable R:R (2.8:1).
The full table is in `leads.md`.

## Draft & planned setups

- **27 new DRAFT cards** this run: AAPL, ANET, APA, ASND, BBY, COHR, EXPE, FN, FRO,
  HSY, JBL, LLY, LSCC, NTAP, NTNX, NUE, PR, PSX, SANM, SMTC, SNA, STLD, TXN, UI, VIAV,
  VLO, XOM. Each one reads: `RESEARCH — DRAFT awaiting your review (set status:
  planned to approve)`. Every level is a Yahoo formula output (EMA20 entry, 3×ATR
  chandelier stop, 1.5R/3R targets). Shariah is `unverified` on every card.
- Business-screen heads-up: some new drafts are energy or refining names (APA, PR,
  XOM, PSX, VLO, FRO). Confirm their ratio and debt profiles in Zoya/Musaffa. The
  pre-check is not a business screen.
- **PLANNED/LIVE cards: none.** No BUY-CANDIDATE is possible this run.
- `setups/` now holds ~77 draft cards and none have been promoted. Consider deleting
  drafts you will never review so the folder stays usable.

## Follow-ups

1. Re-screen **BMNR** in Zoya/Musaffa on the business-activity question
   (open for 2 runs).
2. Re-screen **NOW** (stale).
3. Re-underwrite NOW (DRAWDOWN_REVIEW). Set a numeric `invalidation` (e.g. a cRPO
   floor), an `initial_stop`, and update `catalyst` (next earnings ~late Jan 2027).
4. Fill in BMNR's holding file: thesis, stop, target, pre-mortem.
5. If you trade, run `/apply-trade`.

*Not financial advice. Shariah status must be verified in Zoya/Musaffa.*
