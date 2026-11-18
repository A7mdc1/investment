# Portfolio Assessment — 2026-11-18

Not financial advice. This is decision support only. Every buy, sell and hold
decision is yours. The Shariah status below comes from the broker app's
recorded screen or a mechanical ratio pre-check. Neither is a fatwa, so verify
in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept) → `scaffold.py --all-leads` (27
new DRAFT cards; 23 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py`, all on live data with no
gaps. There is still no `transactions.csv`, so the discipline guard stays
dormant.

**Since the last report (2026-08-19, 91 days ago):** no trades were recorded.
The book fell from **$1,105.51 to $787.45 (−28.8%)**. NOW gave back its whole
gain after Q3 earnings, and BMNR dropped from $20.54 to $15.50 as ETH fell.

## Verdicts (lead with this)

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW, down −21.4% vs cost; VALUATION_RICH
also fired: hold, don't add). Live price is **$90.40** against a $114.97 cost.

| PM-grade record (recommend.py, mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW: no reward:risk or stated edge on file, so it can't self-assess |
| Shariah | **REVIEW**: recorded compliant, but the screen dates from 2026-06-09 (>100 days, now stale) |
| Target / method | $119.65 / DCF intrinsic value (+32.4%) |
| Trailing stop (chandelier) | $139.89, so **price is 35% below it**. `trade_type: core` exempts NOW from TRAIL_STOP, so the rule doesn't fire |
| R-multiple | n/a (no `initial_stop` recorded) |
| 6m momentum (skip last month) | +44.8%. This lookback ends before the October collapse, so it's misleading here |
| Would buy today? | **No** (recommend.py) |
| What changes verdict | `thesis_broken: true`, a SELL trigger, or the Shariah screen flipping |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Live price is **$15.50**,
+0.5% vs the $15.43 cost (it was +33.1% at the last run).

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW: holding file has no thesis, stop, target or pre-mortem |
| Shariah | **REVIEW**: recorded compliant on 2026-07-07, now >100 days and stale. The business-activity question from last run is still open (see Flag #1) |
| Target / method | −$6.53 / DCF. Not meaningful: a DCF doesn't fit an ETH-treasury business |
| Trailing stop (chandelier) | $20.17, so **price is 23% below it**. Core is exempt, so it doesn't fire |
| 6m momentum | +17.7% (lookback ends before the November ETH slide) |
| Would buy today? | Mechanically yes, but that check reads only the recorded Shariah field |
| What changes verdict | A Zoya/Musaffa business-activity re-screen, or a `thesis_broken` flag |

**Portfolio notes (verdict.py):** with only 2 holdings, the concentration rules
are muted until there are at least 4 names. **VOL_THROTTLE fired for both
names:** BMNR ATR is 9.38% and NOW ATR is 7.23%, so the rule says size down.

These are your own rules in `rules.md` resolving mechanically. They are not
advice.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| NOW | $90.35 | 7 | $114.97 | $632.45 | −21.4% | 80.3% |
| BMNR | $15.50 | 10 | $15.43 | $155.00 | +0.5% | 19.7% |

**Total value: $787.45** | Cost: $959.09 | **Total return: −17.9%** (−$171.64
unrealised)

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale.** NOW was screened 2026-06-09
   and BMNR 2026-07-07; both are now past the ~100-day freshness window, and
   recommend.py marks both as `REVIEW`. For BMNR, last run's business-activity
   concern still stands. Its own releases describe it as an ETH treasury
   company holding about 6.07M ETH (about 4.97% of supply) and funded by heavy
   share issuance. This run's ratio pre-check returned `business_ok: null`:
   it neither confirmed nor cleared the industry, unlike last run's
   `Capital Markets` fail. Treat that as unresolved, not as cleared. Re-screen
   both names in Zoya/Musaffa.
2. **[Drawdown / NOW] DRAWDOWN_REVIEW fired, at −21.4% vs cost.** Q3 FY26
   was reported on 2026-10-28. Revenue grew +20.5% to $4.11B, but adjusted EPS
   was $1.00, below most estimates, and the Q4 cRPO growth guide of 18.5% came
   in below the ~19% consensus. Shares fell as much as 25% the next day, the
   biggest intraday drop since the 2012 IPO, and drifted lower into November.
   [The Next Web](https://thenextweb.com/news/servicenow-results-shares-record-drop-crpo-outlook) ·
   [Stocktwits](https://stocktwits.com/news-articles/markets/equity/now-stock-declines-double-digits-after-hours-on-earnings-miss-and-ai-concerns/cZUQ2ikR9GA) ·
   [AI Weekly](https://aiweekly.co/alerts/servicenow-shares-sink-15-after-hours-as-q4-crpo-guide-lands-below-street)
3. **[Catalyst / BMNR] Earnings are expected on ~2026-11-20, 2 days out.**
   The holding has no `earnings_plan` and no stop. ETH fell from ~$2,234
   (Nov 8) to ~$1,823 (Nov 15), and coverage cites ~$6.2B of unrealised crypto
   losses over the fiscal year. Shares outstanding have also risen sharply
   (~613M) to fund ETH buying.
   [Finviz / company PR](https://finviz.com/news/423162/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-608-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-118-billion) ·
   [Stocktwits](https://stocktwits.com/news-articles/markets/equity/tom-lee-s-ethereum-bet-is-costing-bitmine-billions-on-paper-and-he-s-still-buying/cNGDkxfR9Be) ·
   [StockAnalysis](https://stockanalysis.com/quote/otc/BMNRD/)
4. **[Risk discipline] Both prices sit far below their chandelier stops**
   (NOW 35%, BMNR 23%). The core label exempts them from TRAIL_STOP, so no rule
   fires. Neither holding records an `initial_stop`, so nothing pre-committed
   caps further downside. That is a gap in the framework, not a price call.
5. **[Valuation / NOW] Recorded P/E is ~119.** That figure is a stale
   front-matter value from June. VALUATION_RICH still fires on it (hold, don't
   add). Refresh it.

## Per-holding read

### NOW (ServiceNow)
**Case to keep:** Revenue still grows ~20%, and management raised its AI sales
target to ~$1.7B. The DCF (18% growth, 10% discount) now shows **+32.4%** to
intrinsic value; last run it showed −6.6%. Some analysts point to early
contract renewals pulled into Q3 as a timing distortion in cRPO.
[nowben](https://nowben.com/servicenows-stock-plunges-after-q3-2026-earnings/)

**Case to trim or exit:** The holding's own "what would change my mind" text
says *"subscription growth decelerating meaningfully below current ~21-22% YoY,
or a guidance cut tied to AI-agent or Armis traction."* The cRPO guide of 18.5%
and the ~20.5% revenue print are moving toward that line, and coverage partly
tied the reaction to Armis. Whether this counts as "meaningfully below" is your
call to make and record (`invalidation` / `thesis_broken`). The position is
also 80% of the book.

### BMNR (Bitmine Immersion)
**Case to keep:** It's near its stated "5% of ETH" goal and is still
accumulating. The analyst average target is ~$33.5 according to one
aggregator. The stock is about flat vs cost.

**Case to flag:** Price is a levered proxy on ETH, which is down ~44% over the
year. It funds itself through dilutive share sales. Earnings land in 2 days
with no gap plan. The compliance question (Flag #1) comes before any
price-based decision. The file still has no thesis, stop, target or pre-mortem,
four months after entry.

## Suggested actions (from YOUR rules, rules.md)

- **DRAWDOWN_REVIEW fired -> NOW:** re-underwrite. Ask "would I buy it here
  today?" and update `last_review`.
- **VALUATION_RICH fired -> NOW:** hold, do not add.
- **VOL_THROTTLE fired -> NOW, BMNR:** size down per the throttle (ATR 7.2% / 9.4%).
- **Shariah staleness (COMPLIANCE gate) -> NOW, BMNR:** re-screen. A failed
  screen is an absolute SELL under Gate 1.
- **TRAIL_STOP -> not fired** (core exemption), even though both prices are
  below their chandelier levels.

*If you execute anything, run `/apply-trade` so the holdings files and ledger update.*

## DCF (live)

| Ticker | Intrinsic | Price | Up/(down) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $90.40 | +32.4% | growth_5y 18%, terminal 3%, discount 10% (holding override) |
| BMNR | −$6.53 | $15.51 | n/m | default 5% / 2.5% / 10%. The model doesn't fit a crypto-treasury business |

## New ideas

`watchlist.md` doesn't exist or is empty, so recommend.py's `ideas` array is
empty and there are **0 BUY-CANDIDATEs**. All 90 setup cards are still
`status: draft`. Nothing can reach BUY-CANDIDATE until you review a card and
set it to `planned`.

## Draft setups — 50 leads, 27 new DRAFT cards

Only **3 leads clear to LEAD tier** (asymmetry and catalyst gates passed). All
three are Shariah UNVERIFIED and have no edge stated. Levels are formula
outputs to review, not buys:

| Ticker | R:R | Entry / target / stop | Catalyst |
|---|---|---|---|
| SNX | 12.6:1 | ~233.85 / 298.28 / 229.87 | earnings 2027-01-07 (50d) |
| ADI | 6.8:1 | ~378.13 / 444.34 / 375.31 | earnings 2026-11-24 (6d), so a gap plan is needed if held through it |
| AVGO | 4.5:1 | ~349.49 / 493.63 / 317.52 | earnings 2026-12-09 (21d) |

The other 47 leads are capped at RESEARCH, mostly for having no catalyst
inside the horizon. New DRAFT cards this run: AAPL, ANET, APA, ASND, BBY, COHR,
CRH, DIOD, FN, FRO, HST, HSY, JBL, KEYS, KLAC, LLY, LSCC, NTAP, NTNX, PSX, SANM,
SMTC, TS, TXN, UI, VIAV, VLO. Several of the new names deserve a
business-activity screen before you spend review time on them:
- **HST** is a REIT.
- **FRO** is shipping, so check its financing.
- **PLTR** still carries its defense question.

The full list is in `leads.md`.

## Follow-ups (priority order)

1. **[Mandate] Re-screen NOW and BMNR in Zoya/Musaffa.** Both are stale, and
   BMNR's business-activity question is still open.
2. **[Time-critical] BMNR earnings ~Nov 20.** Decide whether to hold through
   the print, and record an `initial_stop` / earnings plan.
3. **[Re-underwrite] NOW after the Q3 guide.** Decide whether the 18.5% cRPO
   guide breaches your written invalidation, then record `invalidation`,
   `initial_stop` and `target_price`.
4. **[Housekeeping]** Refresh NOW's stale `pe` / `last_price` front-matter, and
   complete BMNR's PM fields.
5. **[Infrastructure]** Start `transactions.csv` (via `/apply-trade`) to unlock
   the discipline guard.

---

Not a financial advisor. Shariah status here is a recorded broker-app flag or a
mechanical pre-check, not a fatwa. Verify in Zoya/Musaffa before acting.

Sources:
- [ServiceNow shares fall a record 25% after its bookings outlook misses — The Next Web](https://thenextweb.com/news/servicenow-results-shares-record-drop-crpo-outlook)
- [NOW Stock Declines Double Digits After Hours — Stocktwits](https://stocktwits.com/news-articles/markets/equity/now-stock-declines-double-digits-after-hours-on-earnings-miss-and-ai-concerns/cZUQ2ikR9GA)
- [ServiceNow Shares Sink 15%+ After Hours as Q4 cRPO Guide Lands Below Street — AI Weekly](https://aiweekly.co/alerts/servicenow-shares-sink-15-after-hours-as-q4-crpo-guide-lands-below-street)
- [ServiceNow's stock plunges after Q3 2026 earnings — nowben](https://nowben.com/servicenows-stock-plunges-after-q3-2026-earnings/)
- [ServiceNow Q3 2026 in line but stock drops — StockStory](https://stockstory.org/us/stocks/nyse/now/news/earnings/servicenow-nysenow-reports-q3-2026-in-line-with-expectations-but-stock-drops-171percent)
- [BitMine ETH holdings reach 6.08M tokens — Finviz / company PR](https://finviz.com/news/423162/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-608-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-118-billion)
- [Tom Lee's Ethereum Bet Is Costing Bitmine Billions On Paper — Stocktwits](https://stocktwits.com/news-articles/markets/equity/tom-lee-s-ethereum-bet-is-costing-bitmine-billions-on-paper-and-he-s-still-buying/cNGDkxfR9Be)
- [Bitmine Immersion Technologies (BMNR) — StockAnalysis](https://stockanalysis.com/quote/otc/BMNRD/)
