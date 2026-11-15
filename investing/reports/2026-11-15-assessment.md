# Portfolio Assessment — 2026-11-15

Not financial advice. This is decision support only. Every buy, sell and hold
call is yours. Shariah status below is either the broker app's recorded screen
or a mechanical ratio/business-activity pre-check, and neither one is a fatwa.
Verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

All of these ran on live Yahoo data with no data gaps:
- `discover.py` (top 50 kept per `discover_top_n: 50`)
- `scaffold.py --all-leads`: **26 new DRAFT cards**; the 24 leads that already
  had cards were left unchanged. `setups/` now holds 89 cards, and **none** are
  `planned`.
- `prices.py`, `shariah.py`, `dcf.py`, `signals.py`, `verdict.py`, `recommend.py`

`journal.py` was not run because there is still no `transactions.csv` or
`journal.csv`.

**Since the last report (2026-08-19, about 3 months ago):** no trades were
recorded. The book fell from **$1,105.51 to $891.55 (-19.4%)**. Most of that
came from NOW's sharp drop after its Q3 earnings. Both recorded Shariah
screens have now gone **stale** (>100 days), and the BMNR business-activity
question flagged last run is **still unresolved**.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically. They are not advice.

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Price **$17.58**, +13.9% vs
the $15.43 cost basis (it was +33.1% last run).

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW: no thesis or reward:risk in the holding file |
| Shariah (recorded) | **REVIEW**: broker_app "compliant", screened 2026-07-07, **now stale** |
| Shariah (mechanical pre-check, this run) | **FAIL**: industry `Capital Markets`, so the core business fails the screen (2nd consecutive run) |
| DCF intrinsic value | -$6.53 vs $17.58. Not meaningful for a crypto-treasury company (see DCF caveat) |
| Trailing stop (chandelier) | $19.85, which is **above** the current price (-12.9% on recommend.py's basis). `trade_type: core` exempts it from TRAIL_STOP |
| EMA20 | $20.33 (price below it) |
| 6m momentum (skip last month) | +17.6% |
| Would buy today? | recommend.py says "yes", but that check reads only the recorded Shariah field and not the pre-check FAIL |
| Vol throttle | ATR 8.9% > 6% threshold, so size down |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= `pe_rich` 50, so
hold and do not add). Price **$102.25**, **-11.1%** vs the $114.97 cost basis
(it was +11.8% last run).

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW: no stop, target or variant view in the holding file |
| Shariah | **REVIEW**: broker_app "compliant", screened 2026-06-09, **stale** (>5 months). The mechanical ratio pre-check is clean (debt 2.3%, liquid 5.9%) |
| DCF intrinsic value | $119.65 vs $102.25, **+17.0%** (growth 18% / terminal 3% / discount 10%, now at risk given guidance, see below) |
| Trailing stop (chandelier) | $138.00, **35% above** the price. `core` exempts it, but this shows the size of the move |
| EMA20 | $116.55 (price well below it) |
| 52w range position | 13% (near the low end, 52w low $81.24) |
| 6m momentum (skip last month) | +56.3%. This is stale: it reflects the summer rally, not the post-earnings collapse |
| Vol throttle | ATR 7.0% > 6% threshold, so size down |

- Portfolio note: only 2 holdings, so concentration rules stay muted until there
  are 4 or more names. NOW is **80.3%** of the book.
- The recorded P/E of 119 in `holdings/now-servicenow.md` is a hand-entered
  June figure. It still drives VALUATION_RICH even though the price has moved
  a lot. Refresh it if you want that rule to reflect today.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.58 | 10 | $15.43 | $175.80 | +13.9% | 19.7% |
| NOW | $102.25 | 7 | $114.97 | $715.75 | -11.1% | 80.3% |

**Total value: $891.55** | Cost: $959.09 | **Total: -$67.54 (-7.0%) unrealised**

## Action flags (priority order)

1. **[Mandate, carried over and now worse] BMNR business-activity pre-check FAILS
   (2nd run), and the recorded screen is now stale too.** Last run's research
   still applies. BMNR operates as an Ethereum treasury: about 6.07M ETH, of
   which about 5.23M is staked (about $11.7B), plus 216 BTC and about $475M in
   cash and marketable securities as of Nov 8. That profile is what a
   business-activity screen is built to catch. Under the repo's Gate 1, a
   confirmed fail would be a hard SELL. Because the recorded status still says
   `compliant`, COMPLIANCE_GATE stays silent. **Only your Zoya/Musaffa re-screen
   can resolve this, and BMNR reports earnings around Nov 20.**
   [Bitmine 8-K](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226050647/ex99-1.htm) ·
   [Seeking Alpha](https://seekingalpha.com/news/4662175-bitmine-says-crypto-holdings-reach-145b)
2. **[Mandate] NOW recorded screen is stale** (screened 2026-06-09, over 5
   months ago). COMPLIANCE_SCREEN applies: REVIEW before any add. The ratio
   pre-check is clean, so this is a staleness issue, not a red flag.
3. **[Price / NOW] Post-earnings collapse.** Q3 2026 was reported on Oct 28.
   Revenue beat, but adjusted EPS of $1.00 missed the ~$1.02 consensus, ending
   its streak of beats. Q4 guidance calls for cRPO growth to slow to about
   18.5%, and heavier AI investment pushed operating margins down. The stock
   fell about 27% the next day and about 30% over the month, from about $150
   before the print to about $102. Coverage also mentions pressure from news
   about competing AI workplace agents.
   [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-4981127) ·
   [24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/) ·
   [FX Leaders](https://www.fxleaders.com/news/2026/11/10/now-stock-faces-the-last-support-on-anthropic-workplace-news-as-servicenow-shares-decline-following-third-quarter-earnings-report/) ·
   [Seeking Alpha](https://seekingalpha.com/article/4964887-servicenow-capitalizing-on-a-32-percent-post-earnings-collapse)
4. **[Thesis check / NOW]** The holding file's "what would change my mind" says
   *"Subscription growth decelerating meaningfully below current ~21-22% YoY, or
   a guidance cut tied to AI-agent or Armis traction."* Guided cRPO growth of
   18.5% is close to that line. Whether it **crosses** it is your judgement, but
   this is the exact condition you wrote down in advance. `invalidation_hit` is
   still `false` in the file.
5. **[Catalyst / BMNR]** Earnings around **2026-11-20** (5 days out; dates vary
   by source). Buybacks resumed after a 10-week pause. The stock sits near the
   bottom of its 52-week range and below its 200-day SMA.
   [Investing.com](https://www.investing.com/equities/bitmine-immersion-tech) ·
   [StockAnalysis](https://stockanalysis.com/stocks/bmnr/)
6. **[Discovery hygiene] ORCL-PD** appears in the leads with a scaffolded card
   (`setups/orcl-pd.md`). This is an Oracle **preferred share**. Preferred
   stock with a fixed dividend generally fails Shariah screens on structure, no
   matter how the issuer screens. The pre-check does not catch this, so treat
   it as a likely AVOID and consider deleting the card. A discovery filter for
   preferreds (`-P*` suffixes) would stop this from recurring.

## Per-holding read

### NOW — ServiceNow
**Case to keep:** Revenue still beat. The miss was small (about $0.02 on EPS),
and management attributes the margin hit to deliberate AI investment. At $102,
the price sits **17% below** the DCF value even at the file's 18% growth input,
and the shares trade near the low end of their 52-week range. Some analysts
read the margin pressure as temporary.

**Case to reduce:** Guidance says growth is slowing toward or below the line you
wrote down in advance. The multiple was "priced for continued high growth"
(your own Risks note), and the market has just repriced it. Price is far below
both EMA20 and the chandelier level. The position is 80% of the book with no
`initial_stop`, `target_price` or `pre_mortem` recorded, so there is no
pre-committed exit to fall back on. DRAWDOWN_REVIEW (-20%) has not fired yet at
-11.1%. It would fire around $91.98.

**Verdict: HOLD (VALUATION_RICH).** The decision that matters is whether flag 4
counts as your invalidation. The rules can't make that call.

### BMNR — Bitmine Immersion
**Case to keep:** Still +13.9% vs cost. ETH holdings keep growing, the buyback
has resumed, and earnings are imminent.

**Case to flag:** Two runs in a row, the business-activity pre-check has
disagreed with a recorded status that is now stale. The holding file is still
missing every PM field (thesis, stop, target, pre-mortem) four months after
entry. ATR is 8.9%, so it is highly volatile.

**Verdict: HOLD (no rule fired). Resolve the compliance question first.**

## Suggested actions (from YOUR rules)

- **COMPLIANCE_SCREEN fired -> BMNR, NOW**: both screens are over 1 quarter old,
  so REVIEW before any add.
- **COMPLIANCE_GATE does NOT fire -> BMNR**: it reads only the recorded field.
  The pre-check FAIL is visible only in this report.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add (based on the stale recorded P/E).
- **VOL_THROTTLE fired -> BMNR (ATR 8.9%), NOW (ATR 7.0%)**: de-risk / size down.
- **DRAWDOWN_REVIEW not fired**: NOW is at -11.1% vs the -20% trigger.
- **TRAIL_STOP**: both prices are **below** their chandelier levels, but
  `trade_type: core` exempts both. If either were tagged `swing`, this rule
  would have fired a SELL.
- **review_cadence_days (90)**: NOW's `last_review` is 2026-06-15, which is 153
  days ago and overdue. BMNR has never been reviewed.

*If you execute anything from this report, run `/apply-trade` so the holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | -$6.53 | $17.58 | n/m: the model doesn't fit an ETH-treasury business | growth 5% (default), terminal 2.5%, discount 10% |
| NOW | $119.65 | $102.25 | +17.0% | growth_5y 18%, terminal 3%, discount 10%. If growth runs nearer the 18.5% cRPO guide and keeps slowing, 18% over 5 years is optimistic |

## New ideas

`watchlist.md` is still empty, so step 4 had nothing to research.
`recommend.py` returned **0 BUY-CANDIDATEs**. That is expected, because no card
has been flipped to `status: planned`.

## Draft & planned setups — 50 leads, 26 new DRAFT cards

**5 leads clear to LEAD tier** (the other 45 are capped at RESEARCH by the
asymmetry or catalyst-horizon gate):

| Ticker | Discovery R:R | Catalyst | Card |
|---|---|---|---|
| KEYS | 10.8:1 | earnings 2026-11-19 (4 days) | new DRAFT |
| AVGO | 5.2:1 | earnings 2026-12-09 | existing DRAFT |
| JBL | 20.0:1 (capped) | earnings 2026-12-16 | new DRAFT |
| PENG | 14.8:1 | earnings 2027-01-05 | new DRAFT |
| SNX | 7.3:1 | earnings 2027-01-07 | existing DRAFT |

**RESEARCH — DRAFT awaiting your review (set status: planned to approve).**
Example card, KEYS (`setups/keys.md`): `earnings_run`, entry ~$297.68 / stop
$293.25 (chandelier: HH22 $344.81 - 3x ATR $17.19) / T1 $304.32 (+1.5R) / T2
$310.96 (+3R); structure ceiling at the 52w high of $390.14. Gap plan:
`exit_before`. Invalidation: no positive drift 5 sessions before the print, or
a give-back of more than 1 ATR. Shariah pre-check: business and ratios OK,
**UNVERIFIED**. Note that the 10.8:1 discovery R:R measures to the 52w high,
while the card's own T1/T2 work out to 1.5R/3R. The stop is very tight
($4.43) against a $17 ATR, so a normal day's range could trigger it. Every
level is a formula output.

Other new DRAFT cards: AEM, AMAT, ANET, APA, ASML, BBY, COHR, CRH, DIOD, FN,
FRO, HSY, KLAC, LSCC, NTAP, NTNX, ORCL-PD (see flag 6), SANM, SMTC, STLD,
TECK, UI, VIAV. The full rows are in `leads.md`.

**Flags before you spend review time:**
- **Several "n/a" R:R rows** (FRO, P, DELL, NTAP, NTNX, NVDA, KLIC, SMTC, DINO):
  the computed stop sits **above** entry. These are stop-artifact rows, not setups.
- **Mining / metals cluster** (AEM, TECK, AR, AA, STLD): this is the same open
  financing-structure question as in earlier runs. Screen these properly first.
- **ORCL-PD**: preferred share, likely structural fail (see flag 6).

## Follow-ups (priority order)

1. **[Urgent, 2nd run] Re-screen BMNR in Zoya/Musaffa** on the business-activity
   question, ideally before its ~Nov 20 earnings. Then update `shariah.status`
   in `holdings/bmnr.md` so COMPLIANCE_GATE can act on it.
2. **[Urgent] Decide whether NOW's Q4 cRPO guide (~18.5%) trips your written
   "what would change my mind" condition.** If it does, set `invalidation_hit:
   true`. Either way, fill in `initial_stop`, `target_price` and `pre_mortem`
   and refresh `last_review`; the position is 80% of the book and has no exit
   plan.
3. **[Mandate] Re-screen NOW**, since the screen from June is stale.
4. **[Housekeeping] Refresh the recorded P/E and price fields** in
   `holdings/now-servicenow.md` (P/E 119 and $106.40 are June values).
5. **[Housekeeping] Delete or ignore `setups/orcl-pd.md`**, and consider a
   preferred-share filter in `discover.py`.
6. **[Infrastructure, still open]** No ledger. Log the past FIG sale and BMNR
   buy via `/apply-trade` to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical pre-check, neither a fatwa. Verify independently
in Zoya/Musaffa before acting.

Sources:
- [Earnings call transcript: ServiceNow Q3 2026 — Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-q3-2026-revenue-beats-shares-sink-after-hours-93CH-4981127)
- [ServiceNow Just Dropped 30% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [ServiceNow: Capitalizing On A 32% Post-Earnings Collapse — Seeking Alpha](https://seekingalpha.com/article/4964887-servicenow-capitalizing-on-a-32-percent-post-earnings-collapse)
- [NOW Stock Faces the Last Support — FX Leaders](https://www.fxleaders.com/news/2026/11/10/now-stock-faces-the-last-support-on-anthropic-workplace-news-as-servicenow-shares-decline-following-third-quarter-earnings-report/)
- [Top 5 analyst questions from ServiceNow's Q3 call — Globe and Mail](https://www.theglobeandmail.com/investing/markets/stocks/NOW/pressreleases/8586317/the-top-5-analyst-questions-from-servicenows-q3-earnings-call/)
- [Bitmine Form 8-K (Nov 2026) — SEC](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226050647/ex99-1.htm)
- [Bitmine says crypto holdings reach $14.5B — Seeking Alpha](https://seekingalpha.com/news/4662175-bitmine-says-crypto-holdings-reach-145b)
- [Bitmine Immersion (BMNR) — StockAnalysis](https://stockanalysis.com/stocks/bmnr/)
- [Bitmine Immersion — Investing.com](https://www.investing.com/equities/bitmine-immersion-tech)
