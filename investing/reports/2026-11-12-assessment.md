# Portfolio Assessment — 2026-11-12

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check, neither a fatwa — verify independently
in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo, top 50 kept) → `scaffold.py --all-leads` (**25 new
DRAFT cards**; existing cards left unchanged; 88 cards now in `setups/`, all
`draft`) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all returned live data. **Data gap:** Yahoo returned HTTP 401
("Invalid Crumb") on the quote-summary endpoint during `shariah.py`, so the
**business-activity** half of the ratio pre-check returned `business_ok: null`
for both names — only the debt/liquid ratio math ran. Still no
`transactions.csv`; the discipline guard stays dormant.

**Since the last report (2026-08-19):** no trades recorded. NOW reported Q3 on
2026-10-28 and fell sharply (see below). It has been ~12 weeks since the last
assessment.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically — not advice.

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Price **$18.69**, **+21.1%**
vs. $15.43 cost.

| PM-grade record (recommend.py — mechanical proxy) | |
|---|---|
| Conviction | LOW — no thesis / reward:risk recorded in the holding file |
| Shariah | **REVIEW** — recorded compliant (broker_app, 2026-07-07) but now **stale (>100d)** |
| Shariah ratio pre-check | debt 0.0 / liquid 0.047 → ratios clean; **business screen did not run (Yahoo 401)** — last run's `Capital Markets` business-activity FAIL is unresolved, not cleared |
| DCF | $-6.53 vs $18.69 — not meaningful (cash-flow DCF does not fit an ETH-treasury company) |
| Trailing stop (chandelier) | $19.80 — **price is ~5.6% BELOW it**; rule exempt because `trade_type` defaults to core |
| Fast EMA | $20.65 — price below |
| 6m momentum | +1.1% |
| Would buy today? | recommend.py says yes, but that check cannot see the stale screen or the open business-activity question |

**NOW -> HOLD** (RULE: VALUATION_RICH — recorded P/E ~119 >= pe_rich 50; HOLD, do not add).
Price **$101.72**, **-11.5%** vs. $114.97 cost.

| PM-grade record (recommend.py — mechanical proxy) | |
|---|---|
| Conviction | LOW — `conviction`, `variant_view`, `initial_stop`, `target_price`, `invalidation`, `pre_mortem` all still null |
| Shariah | **REVIEW** — recorded compliant (broker_app, 2026-06-09) but now **stale (>100d)**; ratio pre-check clean (debt 0.023 / liquid 0.06) |
| DCF | $119.65 vs $101.68 → +17.7% (growth 18%, terminal 3%, discount 10% — the 18% growth input predates the Q3 guide-down and is probably optimistic now) |
| Trailing stop (chandelier) | $137.83 — **price is ~26% BELOW it**; core-exempt so TRAIL_STOP does not fire |
| Fast EMA | $118.15 — price well below |
| 52-week range position | 13% (near the low end) |
| 6m momentum (skip last month) | +54.7% — this lookback excludes the post-earnings month, so it overstates current trend |
| Catalyst on file | "Q2 FY2026 earnings…" — **out of date**; Q3 has already printed |
| Last review | 2026-06-15 (5 months ago) |

- Portfolio notes: only 2 holdings, so concentration rules stay muted until 4 or more names. **VOL_THROTTLE:** BMNR ATR 8.44%, NOW ATR 7.1% — size down per your throttle.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $18.69 | 10 | $15.43 | $186.90 | +21.1% | 20.8% |
| NOW | $101.72 | 7 | $114.97 | $712.04 | -11.5% | 79.2% |

**Total value: $898.94** | Cost: $959.09 | **Total return: ~-6.3%** (-$60.15 unrealised).
Last report: $1,105.51 / +15.3%. The ~$207 swing is almost all NOW's post-earnings drop.

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale (>100 days).** recommend.py
   downgrades both to `REVIEW`. Re-screen BMNR and NOW in Zoya/Musaffa and
   update `shariah.screened` in each holding file.
2. **[Mandate / BMNR] The business-activity question from 2026-08-19 is still
   open.** Last run's mechanical screen flagged BMNR's industry as `Capital
   Markets`. This run could not re-check it (Yahoo 401), so the question is
   unresolved, not cleared. The company's own November filings still describe
   an ETH treasury: ~6.07M ETH, ~5.23M ETH staked, ~$14.3–14.5B in total
   holdings. Under your Gate 1, a confirmed business-activity fail is an
   absolute SELL. When you re-screen, check the business activity, not just
   the ratios.
   [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226050647/ex99-1.htm) ·
   [Seeking Alpha](https://seekingalpha.com/news/4662175-bitmine-says-crypto-holdings-reach-145b)
3. **[Thesis / NOW] Q3 FY2026 (2026-10-28) broke the price trend.** Revenue
   ~$4.11B came in about in line; adjusted EPS of $1.00 missed the $1.02
   consensus (the first miss after six beats). Guidance was soft, and margins
   fell as AI investment rose. Coverage reports a ~27% one-day drop (CNBC: its
   worst day ever) and ~30–32% total post-earnings. Your holding file's
   "what would change my mind" names "a guidance cut tied to AI-agent or Armis
   traction" — that is worth checking against the call transcript now. The
   offsetting fact: management raised its AI net-new-ACV target to $1.7B.
   [CNBC](https://www.cnbc.com/2026/10/29/servicenow-now-earnings-q3-2026.html) ·
   [Benzinga](https://www.benzinga.com/markets/earnings/26/10/62677656/servicenow-reports-mixed-q3-results-shares-sink) ·
   [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-4981127) ·
   [Chartmill](https://www.chartmill.com/news/NOW/Chartmill-57112-ServiceNow-NYSENOW-Stock-Tumbles-After-Q3-Earnings-Miss-and-Soft-Guidance)
4. **[Catalyst / BMNR] Next earnings ~2026-11-20** (8 days out). BMNR tracks
   ETH closely; spot-ETH ETFs saw ~$184M of net outflows on Nov 9.
   [Investing.com](https://www.investing.com/equities/bitmine-immersion-tech)
5. **[Rule gap] Both holdings sit below their chandelier stops, but no rule
   fires** because neither file sets `trade_type` beyond the core default.
   NOW is -11.5% vs cost, which does not reach `drawdown_review_pct: 20`. If
   you hold NOW as a swing rather than a core position, TRAIL_STOP would be
   firing.
6. **[Valuation / NOW]** The recorded P/E of ~119 (`signals.py` reads the
   holding file's `pe` field, which has not been refreshed) keeps
   VALUATION_RICH active: do not add.

## Per-holding read

### NOW — ServiceNow
**Case to keep:** In the cash-flow DCF, intrinsic value is now *above* the
price (+17.7%), the first time in recent runs. Revenue still met
expectations. The AI ACV target was raised to $1.7B, and management called
Q3 an "inflection point". The stock sits in the bottom 13% of its 52-week
range. Some coverage frames the drop as an overreaction.
[Seeking Alpha](https://seekingalpha.com/article/4964887-servicenow-capitalizing-on-a-32-percent-post-earnings-collapse) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-just-dropped-30-month-200208794.html)

**Case to trim/review:** This was the first EPS miss in six quarters, with
soft guidance, margin compression and higher interest expense after Armis.
The market is re-pricing "AI disruption" risk to seat-based SaaS, which goes
to the core of the thesis. The price is far below both the fast EMA and the
chandelier stop. The position is 79% of the book, with no recorded stop,
target, invalidation or pre-mortem to anchor a decision. The DCF's 18%
growth input likely needs lowering after the guide.

Neither side is picked here. The file's own "would I buy here today?"
re-underwrite (`last_review` 2026-06-15) is overdue.

### BMNR — Bitmine Immersion
**Case to keep:** Still +21% vs cost. ETH holdings keep growing (~6.07M ETH).
Most of it is staked, and the buyback has resumed.
**Case to flag:** The compliance question comes before any price question
(flags 1–2). Price is below its trailing stop and fast EMA, earnings are on
Nov 20, and ETH sentiment is weak. The holding file has no thesis, stop or
target at all.
[GuruFocus](https://www.gurufocus.com/news/9193641/a-look-at-bitmine-immersion-technologies-inc-bmnr-after-64-gain-gf-value-302-vs-price-1924)

## Suggested actions (from YOUR rules)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add (from the recorded P/E).
- **COMPLIANCE staleness -> BMNR, NOW**: recommend.py's Shariah status is `REVIEW` for both: re-screen.
- **VOL_THROTTLE fired -> BMNR, NOW**: size down any adds.
- **DRAWDOWN_REVIEW**: not firing (NOW -11.5% < 20%).
- **TRAIL_STOP**: not firing (core-exempt), even though both prices are below their chandelier levels.

*If you execute anything, run `/apply-trade` so the holdings files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Up/(down) | Assumptions |
|---|---|---|---|---|
| BMNR | $-6.53 | $18.69 | n/m | growth 5% (default), terminal 2.5%, discount 10%. The model does not fit a crypto treasury |
| NOW | $119.65 | $101.68 | +17.7% | growth 18%, terminal 3%, discount 10%. The growth input predates the Q3 guide-down |

## New ideas

`watchlist.md` is still empty. `recommend.py` `ideas` → **0 BUY-CANDIDATEs**:
all 88 setup cards are `status: draft`, so none can pass the edge gate.

## Draft & planned setups — 50 leads, 3 at LEAD tier, 25 new DRAFT cards

Every card below is a **formula output, unreviewed, Shariah UNVERIFIED**. To
approve one, edit the levels you disagree with, set `status: planned`, and
screen the name in Zoya/Musaffa.

| Ticker | Tier | R:R | Entry / Target / Stop | Catalyst | Card note |
|---|---|---|---|---|---|
| DLO | LEAD | 7.7:1 | ~13.77 / 16.14 / 13.54 | earnings 2026-11-12 (today) | Existing card's catalyst is stale (2026-11-11) and says `no_earnings_in_window`. Re-check after the print |
| SNX | LEAD | 9.9:1 | ~245.32 / 298.09 / 240.71 | earnings 2027-01-07 | Existing card's catalyst is stale (2026-09-24). Refresh before review |
| AVGO | LEAD | 3.0:1 | ~363.65 / 493.42 / 320.45 | earnings 2026-12-09 | Existing card's catalyst is stale (2026-09-02); `earnings_plan: exit_before` |

The other 47 leads are capped at RESEARCH by the catalyst-horizon gate. Most
show very high formula R:R (10–20:1) on tight stops, which mostly reflects
how close the stop sits to entry, not real asymmetry. New DRAFT cards this run:
AEM, ANET, APA, ASND, BBY, COHR, DIOD, FN, FRO, HST, HSY, KEYS, KLAC, LSCC,
NTAP, NTNX, NUE, ORCL-PD, SMTC, SNA, STLD, TECK, TS, UI, VIAV. **ORCL-PD is a
preferred-type listing:** a fixed-income instrument fails Shariah screens
regardless of the issuer. Treat it as AVOID-pending-verification.

## Follow-ups (prioritized)

1. Re-screen **BMNR** in Zoya/Musaffa, specifically the business-activity test, and update `shariah.screened`.
2. Re-screen **NOW** and update `shariah.screened`.
3. Re-underwrite **NOW** against the Q3 call. Fill in `initial_stop`, `invalidation`, `pre_mortem` and a current `catalyst`. Refresh `pe` and the DCF `growth_5y`. Set `last_review`.
4. Decide `trade_type` for BMNR (earnings Nov 20) and give it at least a stop and a thesis line.
5. Refresh the stale catalyst dates on the DLO, SNX and AVGO cards before reviewing them.

*Not financial advice. Verify every Shariah status in Zoya/Musaffa.*
