# Portfolio Assessment — 2026-11-13

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 164-name raw pool, 3 dropped on liquidity,
76 dropped on the ratio pre-check, top 50 kept) → `scaffold.py --all-leads`
(27 new DRAFT setup cards; 23 existing cards left unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live. Yahoo was rate-limited (HTTP 429 / 401 "Invalid Crumb" during scaffold)
but every script returned data; no gaps in the holding numbers. Note: the
sandbox needed `python -m pip install -r requirements.txt` before the scripts
would import yfinance. `journal.py` not run — still no `transactions.csv`.

**Since the last report (2026-08-19), no trades recorded.** Two big changes:
NOW reported Q3 on 2026-10-28 and had its worst day on record, and **both
holdings' Shariah screens have now gone stale** (>100 days old).

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically — not advice.

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Price **$17.47**, **+13.2%**
vs. $15.43 cost (was +33.1% last run).

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW — missing reward:risk and a stated thesis |
| Shariah | **REVIEW** — recorded compliant (broker app, 2026-07-07) but **stale**; mechanical pre-check **FAILS** (`Capital Markets` industry) — second run in a row |
| Target / method | DCF $-6.53 (meaningless for a crypto-treasury business — see DCF) |
| Trailing stop (chandelier) | $19.85 — **price is ~12% BELOW it** (core exempt from TRAIL_STOP) |
| 6m momentum (skip last month) | +17.6% |
| Would buy today? | recommend.py says yes, but that ignores the pre-check fail + stale screen |
| What changes verdict | Zoya/Musaffa business-activity re-screen; `thesis_broken: true` |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 ≥ 50 → hold, do not add).
Price **$101.09**, **-12.1%** vs. $114.97 cost (was +11.8% last run).

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW — no reward:risk / variant view supplied |
| Shariah | **REVIEW** — recorded compliant (2026-06-09) but **stale**; ratio pre-check clean (debt 2.3%, liquid 6.0%) |
| Target / method | DCF $119.65 → +18.4% |
| Trailing stop (chandelier) | $138.05 — **price is ~27% BELOW it** (core exempt from TRAIL_STOP) |
| 6m momentum (skip last month) | +56.3% (lookback excludes the post-earnings month — misleading here) |
| Would buy today? | recommend.py says yes (gates only) |
| What changes verdict | thesis_broken flag, or guidance/growth break per your own "what would change my mind" |

- Note: only 2 holdings — concentration rules muted until ≥ 4 names.
- **Portfolio notes (vol throttle, new this run):** BMNR ATR 8.96%, NOW ATR
  7.07% — "size down per vol throttle".

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.47 | 10 | $15.43 | $174.70 | +13.2% | 19.8% |
| NOW | $101.09 | 7 | $114.97 | $707.60 | -12.1% | 80.2% |

**Total value: $882.30** | Cost: $959.09 | **Total return: ~-8.0%** (-$76.79
unrealised). Down from $1,105.51 last run (-20.2%).

## Action flags (priority order)

1. **[Mandate — NEW] Both Shariah screens are stale.** BMNR (screened
   2026-07-07, 129 days) and NOW (2026-06-09, 157 days) now read
   `stale: true`; recommend.py downgrades both to Shariah REVIEW. The whole
   book is now outside your own freshness rule — a policy issue, not a price
   call. Re-screen both in Zoya/Musaffa.
2. **[Mandate — carried, 2nd run] BMNR business-activity pre-check FAILS**
   (`industry 'Capital Markets' — core business fails screen`). Nov 9
   company release: 6.07M ETH (~4.97% of supply), 5.23M ETH staked,
   projected ~$359M annualized staking rewards, plus stakes in Beast
   Industries and Eightco. The business is still a crypto treasury earning
   staking yield — exactly what the last run flagged. Per Gate 1, a confirmed
   fail is a hard SELL independent of return. Still unresolved; the stale
   flag now makes the re-screen doubly due.
   [Chainwire](https://chainwire.org/2026/11/09/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-6-07-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-14-3-billion/) ·
   [Finviz](https://finviz.com/news/419085/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-607-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-143-billion)
3. **[Price / NOW — NEW] Record post-earnings drop.** Weekly closes went from
   ~$159 (week of Oct 23) to ~$105 the next week; the stock is now below
   cost and ~27% under its chandelier level. Q3 itself was roughly in line
   (revenue +~20.5%, subscription +21% to $3.99B, adj. EPS $1.00 vs ~$1.02
   est.); the selloff came from a Q4 cRPO growth guide of 18.5% vs ~19%
   expected, with management citing Middle East deal delays and
   deployment-support investments on large deals. Management raised its AI
   sales target to $1.7B. Coverage on the size of the drop varies (15-27%
   depending on after-hours / intraday / close).
   [The Next Web](https://thenextweb.com/news/servicenow-results-shares-record-drop-crpo-outlook) ·
   [Bloomberg Gov](https://news.bgov.com/mergers-and-acquisitions/servicenow-posts-lukewarm-sales-on-middle-east-deal-delays) ·
   [INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook) ·
   [MarketBeat](https://www.marketbeat.com/articles/servicenows-18-drop-is-ai-fears-continue-but-may-be-overblown/)
4. **[Rule-design gap] Both holdings sit below their trailing stops, but
   `trade_type: core` exempts them from TRAIL_STOP**, so verdict.py stays
   HOLD. NOW is also -12.1% — not yet at the 20% DRAWDOWN_REVIEW threshold.
   Neither position has an `initial_stop` set, so there is no
   price-based exit of your own recorded anywhere.
5. **[Valuation / NOW] P/E ~119 (recorded, stale field — `last_price` in the
   file is $106.40)** keeps VALUATION_RICH active.

## Per-holding read

### BMNR — Bitmine Immersion Technologies
**Case to keep:** ETH count still rising week over week (6.06M → 6.07M);
staking scale-up projects ~$359M/yr; still +13.2% on cost.
**Case to trim/exit:** Compliance question unresolved for two runs and the
screen is now stale; price has slid from ~$27.6 (late Sept) to $17.47
alongside ETH (~$2,234 on Nov 8), and sits below its chandelier level. The
holding file still has no thesis, stop, target, or pre-mortem.
**Verdict: HOLD (no rule fired) — resolve compliance first.**

### NOW — ServiceNow
**Case to keep:** Core growth still ~20%+ (subscription +21%); AI sales
target raised to $1.7B; DCF (18% growth, 10% discount) now shows +18.4% to
$119.65; some analysts call the reaction overdone.
**Case to trim:** Guidance-driven derating on top of AI-disruption fears for
software; stock fell after January and April reports too; your own "what would
change my mind" is "subscription growth decelerating meaningfully below
~21-22% YoY, or a guidance cut" — an 18.5% cRPO guide is close enough to
that line that it deserves an explicit re-underwrite (`last_review` is
2026-06-15). P/E still rich.
**Verdict: HOLD (VALUATION_RICH) — re-underwrite against your own invalidation text.**

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **Shariah staleness -> BMNR, NOW**: recommend.py flags both REVIEW — your
  rule is re-screen before any add.
- **COMPLIANCE_GATE does NOT fire -> BMNR**: it only reads the recorded
  status field, so it stays silent despite the pre-check fail.
- **TRAIL_STOP**: price is below the chandelier on both, but does NOT fire
  (`trade_type: core` exempt).
- **DRAWDOWN_REVIEW**: not firing (NOW -12.1%, threshold -20%).
- **VOL_THROTTLE**: fired as portfolio notes for both — size down any adds.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $-6.53 | $17.46 | -137.4% (not meaningful — cash-flow model doesn't fit a crypto treasury) | growth 5% (default), terminal 2.5%, discount 10% |
| NOW | $119.65 | $101.09 | +18.4% | growth 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md` is still empty. `recommend.py` returned **0 ideas /
0 BUY-CANDIDATEs** — all 90 cards in `setups/` are `draft`; none is
`planned`.

## Draft & planned setups — 50 leads, 27 new DRAFT cards

**Every card is a formula output, unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.** New cards: KEYS AEM CRH STLD
KLAC ORCL-PD SANM VIAV TECK FN UI COHR BBY HSY FRO APA NTAP NTNX LSCC DIOD
ANET SMTC AAPL HST TS TXN LLY. Existing cards left unchanged: LIF AA AR SNX
DLO FORM AVGO GDDY ADI MKSI P DELL MSFT TSLA AMD APH NVDA NET FOX KLIC CF
HAS DINO.

Only 3 of 50 reach LEAD tier (47 capped at RESEARCH, mostly by the 60-day
catalyst-horizon gate — most next prints are late Jan/Feb):

| Ticker | Verdict | Card | Discovery R:R | Catalyst | Days |
|---|---|---|---|---|---|
| KEYS | LEAD | new | 10.8:1 | earnings 2026-11-19 (web sources say Nov 17 or Nov 23 — unconfirmed) | 6 |
| SNX | LEAD | existing | 8.6:1 | earnings 2027-01-07 | 55 |
| AVGO | LEAD | existing | 5.6:1 | earnings 2026-12-09 | 26 |

**KEYS** — `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`
- setup_type: earnings_run; entry ~$296.77, stop $293.25 (chandelier: HH22
  $344.81 − 3×ATR $17.19), target T1 $302.04 (1.5R) / T2 $307.32 (3R);
  structure ceiling = 52w high $389.97.
- **Inconsistency:** the card's T1-based R:R is 1.5:1, not discovery's 10.8:1
  (discovery uses the 52w-high ceiling). The stop is only ~1.2% under entry
  while ATR is ~$17 — a normal day's noise would hit it.
- Gap plan: `exit_before` (machine default). Shariah pre-check: business and
  ratios OK — verify in Zoya/Musaffa.
- Invalidation: no positive drift 5 sessions pre-print / gives back >1 ATR.
[Earnings date sources: TipRanks](https://www.tipranks.com/stocks/GB:0A7N/earnings) ·
[Earnings Whispers](https://beta.earningswhispers.com/go/x/KEYS) ·
[Tickzen](https://tickzen.app/stocks/keys/earnings)

**SNX / AVGO — existing cards are stale.** SNX's card still targets the
2026-09-24 print and AVGO's the 2026-09-02 print (AVGO's card also has a
stop *above* entry and no target). Both catalysts have passed; scaffold
left them unchanged because cards exist — re-run `scaffold.py --force` for
these if you want fresh levels.

Flags: **ORCL-PD** is a preferred-share listing (fixed-dividend instrument;
no earnings date) — very likely not something a Shariah screen passes and not
a real swing setup. **PLTR** and the precious-metals cluster (AGI, IAG, KGC,
EGO, CDE) didn't make this run's top 50 but their old cards remain.

## Follow-ups (priority order)

1. **[Urgent] Re-screen BMNR and NOW in Zoya/Musaffa** — both stale; BMNR
   also failing the business-activity pre-check for the second run.
2. **[Urgent] Re-underwrite NOW** after the Oct 28 guide; compare the 18.5%
   cRPO guide with your own invalidation text and set `initial_stop`,
   `invalidation`, `last_review`.
3. **[Housekeeping] BMNR holding file** still has no thesis, stop, target,
   or pre-mortem (four months after entry).
4. **[Optional] Decide whether `core` should stay exempt from TRAIL_STOP** —
   both names are well below their chandelier levels and the engine is silent.
5. **[Cleanup] Refresh/delete stale cards** (AVGO, SNX and others whose
   catalysts have passed); 90 draft cards now, none planned.
6. **[Infrastructure — still open]** No `transactions.csv` — log the FIG sale
   and BMNR buy via `/apply-trade` to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow shares fall a record 25% after its bookings outlook misses — The Next Web](https://thenextweb.com/news/servicenow-results-shares-record-drop-crpo-outlook)
- [ServiceNow Stock Has Worst Day Ever on Disappointing Sales — Bloomberg Government](https://news.bgov.com/mergers-and-acquisitions/servicenow-posts-lukewarm-sales-on-middle-east-deal-delays)
- [ServiceNow Stock Plunges 18% After Q3 2026 Earnings — INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook)
- [ServiceNow's 18% Drop: AI Fears Continue, But May Be Overblown — MarketBeat](https://www.marketbeat.com/articles/servicenows-18-drop-is-ai-fears-continue-but-may-be-overblown/)
- [ServiceNow Shares Sink After Hours as Q4 cRPO Guide Lands Below Street — AI Weekly](https://aiweekly.co/alerts/servicenow-shares-sink-15-after-hours-as-q4-crpo-guide-lands-below-street)
- [Bitmine ETH holdings reach 6.07M tokens, $14.3B total — Chainwire](https://chainwire.org/2026/11/09/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-6-07-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-14-3-billion/)
- [Bitmine ETH holdings reach 6.07M tokens — Finviz](https://finviz.com/news/419085/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-607-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-143-billion)
- [Bitmine ETH holdings reach 6.06M tokens, $14.5B — Finviz](https://finviz.com/news/413195/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-145-billion)
- [Keysight earnings date — TipRanks](https://www.tipranks.com/stocks/GB:0A7N/earnings)
- [Keysight earnings date — Earnings Whispers](https://beta.earningswhispers.com/go/x/KEYS)
- [Keysight earnings date — Tickzen](https://tickzen.app/stocks/keys/earnings)
