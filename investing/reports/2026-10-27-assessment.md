# Portfolio Assessment — 2026-10-27

Not financial advice. Decision support only — every buy/sell/hold call is yours. Shariah status below is the broker app's recorded screen or a mechanical ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo; top 50 leads) → `scaffold.py --all-leads` (22 new DRAFT cards; existing cards unchanged) → `prices / shariah / dcf / signals / verdict / recommend.py` (all live, no data gaps; one Yahoo crumb 429 in verdict.py was tolerated). `journal.py` not run (no `transactions.csv`). Last report was 2026-08-19.

## Verdicts (your rules resolving, not advice)
**BMNR -> HOLD** (RULE: DEFAULT). $21.57, **+39.8%** vs $15.43 cost. Trailing stop (chandelier) $23.85 — **price is below it (~9.6% under)** and below the 20-EMA ($23.30); the engine still says HOLD because the position is typed `core`. 6m momentum +25.0%. R-multiple n/a. Vol throttle: ATR 6.72% > 6% — size-down note.
- PM record (mechanical proxy): conviction LOW (no thesis/variant view on file), reward:risk n/a, DCF $0.72 (-96.7%; DCF model does not fit a crypto-treasury business).

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 >= 50). $155.22, **+35.0%** vs $114.97. Trailing stop $141.42 (price ~8.9% above), 20-EMA $146.75, 6m momentum +45.3%.
- PM record: conviction LOW, reward:risk -2.5:1 (target on file below price), DCF $120.12 vs price -> -22.6%.
- DCF assumptions: 5y growth 18%, terminal 3%, discount 10%.

Portfolio note: only 2 holdings, concentration rules muted (<4 names) — but NOW is **83.4%** of value (cap `max_position_pct` 22%).

## Snapshot (live)
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $21.57 | 10 | $15.43 | $215.65 | +39.8% | 16.6% |
| NOW | $155.22 | 7 | $114.97 | $1,086.54 | +35.0% | 83.4% |
| Total | | | | $1,302.19 | | |

## Action flags (priority order)
1. **Shariah — mandate/policy.** Both recorded screens are now **stale** (BMNR 2026-07-07, NOW 2026-06-09). BMNR's mechanical business pre-check still **FAILS** (industry "Capital Markets"; flagged first on 2026-08-19) while the recorded status says compliant. Re-screen both in Zoya/Musaffa; recommend.py shows both as REVIEW.
2. **NOW earnings tomorrow.** Q3 2026 results **2026-10-28 after the close** ([ServiceNow IR](https://investor.servicenow.com/news/news-details/2026/ServiceNow-to-Announce-Third-Quarter-2026-Financial-Results-on-October-28/default.aspx)). The holding card's catalyst date is still `null` — update it. A stop does not execute through an overnight gap; `earnings_gap_assumption_pct` is 25%.
3. **BMNR below trailing stop / EMA** while labelled `core`. Your call whether the chandelier applies to it.
4. NOW valuation-rich (P/E ~119).

## Per-holding read (no pick made for you)
- **BMNR** — Keep: +39.8%, positive 6m momentum, ETH-treasury exposure (a web search found no October 2026 company news; results were dated early Oct or older and conflicted on listing venue, so treat as unverified). Trim/exit: below chandelier and 20-EMA, high ATR, no written thesis/invalidation, and the Shariah ratio pre-check disagreement.
- **NOW** — Keep: strong momentum (+45%), price above stop and EMAs, recorded thesis (AI-agent expansion) intact, earnings imminent. Trim: 83% weight, rich multiple, price above DCF value, binary earnings event.

## Suggested actions (from YOUR rules.md)
- Rule VALUATION_RICH fired for NOW -> HOLD, do not add.
- Vol throttle fired for BMNR (ATR 6.72% > 6%) -> size down note.
- No SELL/TRIM rule fired. If you execute anything, run `/apply-trade`.

## New ideas
`recommend.py` ideas array (watchlist) is empty. Discovery produced 50 **LEADs** (see `leads.md`) — all Shariah UNVERIFIED, no variant view supplied. None can be BUY-CANDIDATE. Highest-scored by the screen: DINO (55.1, R:R 5.6, earnings 10-28), P (62.5, R:R 4.6), PLTR (57.6, R:R 1.4 — fails floor), DDOG (58.1, R:R 1.1 — fails floor). Several leads report extreme R:R (e.g. FICO 20:1, GDDY 19:1) because the formula stop sits ~1% under entry — treat as artifacts. Many have earnings within days (AEM, AGI, KGC, DINO, MSFT, GDDY, FSLR, BKR/RCL today): gap risk dominates. Dated-catalyst web research was not done per lead.

## Draft & planned setups
22 new DRAFT cards scaffolded: AAPL, AEM, APA, BBY, BKR, DDOG, EXPE, FLYW, FRO, FSLR, HPE, HST, LLY, NTAP, NTNX, ORCL-PD, PR, SMTC, SNA, TECK, TS, XOM. Plus existing drafts refreshed per earlier runs. Each is **RESEARCH — DRAFT awaiting your review (set status: planned to approve)**; every entry/stop/target is a Yahoo formula output, a proposal to edit, not a buy. Open each `setups/<ticker>.md` for the setup type, levels, invalidation and gap plan. Scaffold never writes `shariah: compliant`. (ORCL-PD is a preferred share — check its fit.) No PLANNED/LIVE cards, so no BUY-CANDIDATE.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa; resolve the BMNR business-activity conflict.
2. Decide NOW's pre-earnings plan (10-28 AMC); set the catalyst date on its holding file.
3. Decide whether BMNR's `core` type should be `momentum`/swing so the chandelier stop can fire.
4. Write a thesis/invalidation for each holding (conviction is LOW for lack of one).
5. Review the new DRAFT cards if any interest you; prune the rest.

_Not financial advice. Verify all Shariah status in Zoya/Musaffa._
