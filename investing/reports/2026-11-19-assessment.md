# Portfolio Assessment — 2026-11-19

Not financial advice. This is decision support only: every buy, sell or hold
call is yours. The Shariah status shown is either the broker app's recorded
screen or a mechanical ratio pre-check, and neither one is a fatwa. Verify in
Zoya/Musaffa before acting on anything here.

## What ran this cycle

The pipeline ran in this order: `discover.py` (161-name raw pool, top 50 kept),
then `scaffold.py --all-leads` (28 new DRAFT cards, 22 existing cards left
unchanged), then `prices.py`, `shariah.py`, `dcf.py`, `signals.py`,
`verdict.py` and `recommend.py`. Every script exited 0.

**Data quality was degraded this run.** Yahoo returned about 330 HTTP 401
("Invalid Crumb" / "Unauthorized") errors during discovery, plus 429
rate-limits. The effects:
- No `ETF:` sourced names reached the top 50. The pool looks screen-only, which
  suggests the SPUS holdings fetch failed.
- 71 names were excluded by the Shariah ratio flag. That is far more than in
  prior runs and may be partly caused by missing fundamentals rather than real
  ratio fails.
- Many leads show `reward:risk n/a` (no usable levels).
- BMNR's industry classification did not load (`business_ok: null`), so this
  run could **not** re-test the "Capital Markets" business flag raised last
  run. A "clean" pre-check this run does not resolve that question.

`journal.py` was not run because there is still no `transactions.csv`.

**Since the last report (2026-08-19):** no trades are recorded in the repo.
Both positions moved sharply lower.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically, not advice.

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW, down -22.2% vs cost; VALUATION_RICH
also fires, "hold, do not add")

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Price / cost | $89.42 / $114.97 -> **-22.2%** |
| Conviction | LOW. It cannot self-assess: no reward:risk and no stated edge |
| Shariah | **REVIEW**. Recorded compliant, but screened 2026-06-09 (>100d, stale) |
| Target / method | $119.65, DCF intrinsic value (+33.9%) |
| Trailing stop (chandelier) | $139.87. Price is ~36% *below* it (exempt: `trade_type: core`) |
| 6m momentum (skip last month) | +53.6% (this lookback still includes the pre-October run-up) |
| Would buy today? | **No** (recommend.py) |
| What changes verdict | thesis_broken flag, a SELL trigger, or the Shariah screen flipping |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired)

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Price / cost | $15.20 / $15.43 -> -1.5% |
| Conviction | LOW. No thesis, stop, target or pre-mortem recorded in the holding file |
| Shariah | **REVIEW**. Recorded compliant (2026-07-07), now stale (>100d). The business-activity question from last run is still open (see Flag #2) |
| DCF | -$6.53 (not meaningful: the cash-flow model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $20.30. Price is ~25% *below* it (exempt: `trade_type: core`) |
| 6m momentum | +22.2% |
| Would buy today? | Mechanically "yes". That check cannot see the stale screen or the open business question |

**Portfolio notes:**
- Only 2 holdings, so the concentration rules stay muted until there are 4 or more.
- **Vol throttle:** BMNR ATR 9.3%, NOW ATR 7.3%. Size down per your vol throttle.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.20 | 10 | $15.43 | $152.00 | -1.5% | 19.5% |
| NOW | $89.42 | 7 | $114.97 | $625.91 | -22.2% | 80.5% |

**Total value: $777.91** | Cost: $959.09 | **Unrealised: -$181.18 (-18.9%)**
(down from $1,105.51 / +15.3% on 2026-08-19).

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale.** NOW was last screened
   2026-06-09 and BMNR 2026-07-07, both more than 100 days ago. Re-screen both
   in Zoya/Musaffa. This is a policy gate, not a price call.
2. **[Mandate, carried over and unresolved] BMNR business-activity question.**
   Last run's pre-check classified BMNR as `Capital Markets`, which fails the
   screen. This run could not re-evaluate it because the industry data was
   missing. Public reporting still describes an ETH-treasury model:
   - about 6.08M ETH held, roughly 4.97% of supply
   - about 5.2M ETH staked
   - a $4B buyback programme

   The open question is the same one as before. Screen the business activity
   specifically, not only the ratios.
   [CryptoBriefing](https://cryptobriefing.com/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-6-08-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-11-8-billion/) ·
   [Finviz](https://finviz.com/news/419085/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-607-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-143-billion)
3. **[Drawdown / NOW] DRAWDOWN_REVIEW fired at -22%.** The cause is the Q3
   print on 2026-10-28. Revenue was $4.11B, up 20.5% YoY. However, adjusted EPS
   of $1.00 missed estimates of about $1.02-1.17, and Q4 cRPO growth guidance of
   about 18.5% came in below the street's ~19.8%. The stock fell 15-25%
   (sources differ), reportedly its worst day in more than 14 years.
   [INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook) ·
   [Stocktwits](https://stocktwits.com/news-articles/markets/equity/now-stock-on-track-to-post-worst-single-day-performance-in-over-14-years-analysts-see-ai-upside-despite-slowing-growth/cZUQrA2R9Rc) ·
   [AI Weekly](https://aiweekly.co/alerts/servicenow-shares-sink-15-after-hours-as-q4-crpo-guide-lands-below-street)
4. **[Data check / BMNR] Possible share-count or price discrepancy.** Web
   sources quote BMNR at about $24-28, and one lists an OTC `BMNRD` symbol. A
   "D" suffix often marks a recent reverse split. Yahoo prices it at $15.20.
   I could not confirm a corporate action. If one happened, `shares: 10` and
   `cost_basis: 15.43` in `holdings/bmnr.md` may need adjusting, and every BMNR
   number above would be off. Check your broker's position. BMNR's next
   earnings are listed for about 2026-11-20 (tomorrow).
   [StockAnalysis](https://stockanalysis.com/quote/otc/BMNRD/)
5. **[Valuation / NOW]** The recorded P/E of ~119 is a stale front-matter value.
   At $89 the real multiple is lower, but VALUATION_RICH still fires off the
   recorded field. Refresh `pe` / `last_price` in `holdings/now-servicenow.md`.

## Per-holding read

### NOW — ServiceNow
**Case to keep:**
- Revenue growth is still about 20%, and the miss was attributed largely to
  lower interest income and debt costs from the Armis deal rather than to
  operations.
- Cantor Fitzgerald called the selloff a buying opportunity.
- The DCF (18% growth, 10% discount) now puts intrinsic value about 34% above
  the price. That is the reverse of last run's -6.6%.

**Case to trim or exit:**
- Your own recorded invalidation is "subscription growth decelerating
  meaningfully below ~21-22% YoY". The Q4 cRPO guide of ~18.5% sits below that
  line, so this is arguably your thesis trigger, not just price noise.
- The position is 80.5% of the book.
- The front-matter still has no stop, target, conviction or pre-mortem, so
  there was no pre-committed exit to fall back on.

**The REVIEW is yours to resolve.** Decide whether the cRPO guide meets your
invalidation, and set `thesis_broken` and `last_review` accordingly.

### BMNR — Bitmine Immersion
**Case to keep:**
- It is still accumulating ETH and buying back shares.
- The price is near cost, at -1.5%.

**Case to flag:**
- ETH fell about 18% in one week in mid-November.
- The position is below its chandelier level.
- The holding file still has no PM-grade fields, four months after entry.
- Compliance has two open problems: the screen is stale, and the business
  question is unresolved.
- There is a possible corporate-action data mismatch (Flag #4).
- Earnings are about 1 day out, and no gap plan is recorded.

## Suggested actions (from YOUR rules, rules.md)

- **Rule DRAWDOWN_REVIEW fired -> NOW**: your pre-set action is REVIEW. Revisit
  whether the thesis still holds, down 22% vs cost.
- **Rule VALUATION_RICH fired -> NOW**: hold, do not add (based on the stale
  recorded P/E).
- **Shariah staleness -> BMNR, NOW**: re-screen. recommend.py downgrades both to
  Shariah REVIEW.
- **TRAIL_STOP**: price is below the chandelier level on **both** names, but
  `trade_type: core` exempts them, so the rule does not fire. If either was
  meant as a swing trade, the trailing stop would already be hit.
- **VOL_THROTTLE**: active on both. Size down on any add.

*If you execute anything, run `/apply-trade` so the holdings files and the
ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Up/(down) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $89.37 | +33.9% | growth_5y 18%, terminal 3%, discount 10% |
| BMNR | -$6.53 | $15.19 | n/m | default 5% / 2.5% / 10%. The model doesn't fit this business, so treat it as a data gap |

## New ideas

`watchlist.md` is still empty. recommend.py's `ideas` array returned **0**
entries, and there are 0 BUY-CANDIDATEs: all 91 cards are `draft`, and none are
`planned`.

## Draft & planned setups — 50 leads, 28 new DRAFT cards

Discovery returned **3 LEADs and 47 RESEARCH**. Most of the RESEARCH names are
held there by the 60-day catalyst gate, because January and February 2027
earnings fall just outside the window.

| Ticker | Verdict | Card | R:R | Catalyst | Days |
|---|---|---|---|---|---|
| SNX | LEAD | existing (stale) | 13.2:1* | earnings 2027-01-07 | 49 |
| ADI | LEAD | existing (stale) | 6.9:1* | earnings 2026-11-24 | 5 |
| AVGO | LEAD | existing (stale) | 4.1:1 | earnings 2026-12-09 | 20 |

\* **Read these R:R figures with care.** SNX's discovery stop ($229.31) sits
15 cents under its entry ($229.46), and ADI's stop ($374.51) sits $2 under its
entry ($376.63). A near-zero risk leg inflates the ratio mechanically. That is
not real asymmetry.

**All three LEAD cards are stale.** They were scaffolded in August against
prints that have already passed:
- SNX: written for the 2026-09-24 print, entry $252.66
- ADI: written for the 2026-08-19 print, entry $388.83
- AVGO: written for the 2026-09-02 print, with stop above entry and no target

`scaffold.py` skips existing cards unless you pass `--force`, so none of these
reflect today's levels. Re-scaffold with `--force` or rewrite them by hand
before reviewing.

Every card is a proposal: machine-filled levels, `status: draft`, Shariah
`unverified`. Approving one means editing the levels and flipping it to
`status: planned`.

**Business-screen flags among the new cards.** These names passed the ratio
pre-check, but their core business is likely to fail a business-activity
screen:
- **ALL** (Allstate) and **TRV** (Travelers): conventional insurance
- **EVR** (Evercore): investment banking
- **BF-B** (Brown-Forman): alcohol

Screen them before spending review time. PLTR (open defense question) and the
mining cluster carry over as before.

## Follow-ups (priority order)

1. **Re-screen NOW and BMNR in Zoya/Musaffa.** Both are stale, and BMNR's
   business-activity question is still open.
2. **Resolve NOW's REVIEW.** Decide whether the ~18.5% cRPO guide breaches your
   recorded invalidation, then set `thesis_broken` and `last_review`. Refresh
   `pe` and `last_price`.
3. **Verify BMNR's share count and price against your broker** (possible
   reverse split or `BMNRD`). Earnings are about 2026-11-20, with no gap plan.
4. **Fill in the PM fields** for both holdings: stop, target, conviction and
   pre-mortem.
5. **Refresh the stale DRAFT cards** (`scaffold.py --force` for SNX, ADI and
   AVGO at minimum). Consider whether scaffold should auto-refresh drafts whose
   catalyst date has passed.
6. **Re-run discovery locally** when Yahoo isn't returning 401s. This run's pool
   and its Shariah exclusions are probably incomplete.
7. **Start a ledger.** `transactions.csv` is still missing, so the discipline
   guard is still dormant.

---

Not financial advice. Shariah status must be verified in Zoya/Musaffa.
Short-term trading usually trails buy-and-hold after costs.
