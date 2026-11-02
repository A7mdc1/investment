# Portfolio Assessment — 2026-11-02

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is the recorded broker-app screen or a mechanical
ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo; 159-name pool, 2 dropped no price, 2 liquidity, 69 Shariah-ratio
knockouts, top 50 kept: 7 LEAD / 43 RESEARCH) → `scaffold.py --all-leads` (26 new DRAFT
cards) → `prices / shariah / dcf / signals / verdict / recommend` all live, no data gaps
(two Yahoo 401s on auxiliary calls; core data returned). No `transactions.csv`/`journal.csv`,
so the discipline guard stays dormant. No holdings changes since 2026-08-19.

## Verdicts (your rules resolving, not advice)

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 >= 50: hold, do not add). Price **$109.17**,
**-5.0%** vs $114.97 cost (was $128.63 / +11.8% on 08-19).
- Trailing stop (chandelier) **$136.84** — price is ~20% *below* it; EMA20 $136.90. 6m momentum +46.1% (stale window, pre-drop).
- DCF $119.65 vs $109.14 (+9.6%; assumes 18% growth 5y, 10% discount, 3% terminal).
- PM record (mechanical): conviction LOW (no reward:risk/thesis edge supplied); target = DCF value, no variant view.
- **Note:** verdict.py returned HOLD even though price is under the trailing stop and EMA20; the holding is `trade_type: core`, so the technical SELL/REVIEW triggers did not fire. Whether that is intended is your call.

**BMNR -> HOLD** (DEFAULT). Price **$20.19**, **+30.9%** vs $15.43 cost.
- Trailing stop $23.90 (price ~15.5% below it); EMA20 $22.52; 6m momentum +15.3%.
- DCF $0.72 is a model-fit artifact (crypto-treasury business) — data gap, not a valuation signal.
- PM record: conviction LOW; no reward:risk. `would_buy_today: true` only reads the *recorded* Shariah field.

## Snapshot (live)
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $20.19 | 10 | $15.43 | $201.95 | +30.9% | 20.9% |
| NOW | $109.17 | 7 | $114.97 | $764.19 | -5.0% | 79.1% |

**Total $966.14** vs cost $959.09 (~+0.7%, +$7.05 unrealised; down from $1,105.51 on 08-19). Only 2 names, so concentration rules are muted; NOW is ~79% of the book.

## Action flags (priority order)
1. **[Mandate] Both Shariah screens are stale** (BMNR screened 2026-07-07, NOW 2026-06-09; >100 days). Re-screen both in Zoya/Musaffa. For BMNR the open question from 08-19 stands: its business-activity profile (ETH treasury/staking, preferred dividends) vs the earlier "Capital Markets" ratio flag. This run's ratio pre-check passed with `business_ok: null`, i.e. inconclusive, not cleared.
2. **[Price / NOW]** Fell ~16–18% after-hours on its Q3 FY26 print (Oct 28) despite a strong quarter. Per SEC 8-K: subscription revenue $3,988M (+21% y/y), total $4,106M, cRPO $13.65B, AI ACV target raised to $1.7B, FY FCF margin target raised 100 bps to 36%. Reported adj. EPS $1.00 vs $1.03 estimate, slightly light revenue vs consensus (secondary sources; drop magnitude differs by source — confirm on a live quote). The thesis hinges on AI-agent expansion; the market reaction is the new fact to weigh against it. [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm) · [INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook) · [Quiver Quant](https://www.quiverquant.com/news/SERVICENOW+%28%24NOW%29+Releases+Q3+2026+Earnings)
3. **[Stops]** Both holdings trade below their computed chandelier stops (see above); the stops are formula outputs on `core` positions and the engine did not convert them to SELL.
4. **[Valuation / NOW]** P/E ~119 on the recorded figure (likely stale after the drop) — VALUATION_RICH; do not add.
5. **[Vol throttle]** BMNR ATR 7.1%, NOW ATR 6.9% — both above the 6% threshold; size down on any adds.
6. **[BMNR news]** Searching found nothing newer than July 2026 (5.77M ETH, ~4.8% of supply). No fresh catalyst facts; not invented.
7. **[Discovery]** 50 leads; 7 clear LEAD, none BUY-CANDIDATE (no planned+compliant cards).

## Per-holding read
**NOW — keep:** subscription growth +21%, raised FCF margin and AI ACV guidance, DCF above price, ~25% below the prior trailing stop level. **Trim/exit case:** the post-earnings gap-down shows expectations repriced, price is under the chandelier/EMA20, position is -5% and 79% of the book, P/E still rich, Shariah record stale. Your call.
**BMNR — keep:** +31% vs cost, large ETH treasury, buyback/staking income (per prior report). **Trim/exit case:** below trailing stop and EMA20, business-activity Shariah question unresolved, ~21% of book in a high-volatility crypto-beta name.

## Suggested actions (from YOUR rules.md)
- Rule VALUATION_RICH fired (NOW) -> hold, do not add.
- Vol throttle fired (BMNR, NOW) -> size down on adds.
- `compliance_gate`: both recorded screens are stale (re-screen); no non-compliant record exists.
If you execute anything, run /apply-trade so holdings and the ledger update.

## DCF
NOW: intrinsic $119.65 vs $109.14 (+9.6%); assumptions 18% 5y growth, 3% terminal, 10% discount. BMNR: $0.72 (-96.4%), model does not fit the business — ignore.

## New ideas (discovery leads — all UNVERIFIED Shariah, EDGE not supplied; none are buys)
Mechanical LEADs (reward:risk ≥ floor + catalyst in window):
| Ticker | R:R | Entry / target / stop | Catalyst | Card |
|---|---|---|---|---|
| FOX | 13.3 | 55.75 / 67.49 / 55.60 | earnings 11-02 (today) | existing |
| FICO | 20.0 | 719.08 / 1138.88 / 703.01 | 11-04 | existing |
| FRO | 5.5 | 52.65 / 59.76 / 52.01 | 11-30 | new draft |
| LIF | 4.8 | 45.29 / 63.53 / 41.50 | 11-09 | existing |
| PAY | 3.2 | 34.35 / 45.32 / 30.91 | 11-02 (today) | existing |
| CVE | 4.1 | 31.21 / 34.11 / 30.50 | 11-04 | existing |
| TS | 3.1 | 58.55 / 64.62 / 56.58 | 11-04 | new draft |
Caveat: tight stops (FOX/FICO/FRO ~0.3–2% from entry) drive the very high R:R and are fragile; earnings today/this week means gap risk beyond the stop. The other 43 are RESEARCH (asymmetry or catalyst gate, or R:R n/a). Full list in `leads.md`. Some drafts (e.g. TRV) carry a pre-check note that the business fails the Shariah screen (insurance); treat as AVOID unless a proper screen says otherwise. PLTR's government/defense business-activity question remains open.

## Draft & planned setups
26 new machine-filled DRAFT cards in `setups/` (all, apa, asnd, bby, bf-b, bkr, ddog, evr, expe, flyw, fro, fslr, hst, hsy, keys, ntap, ntnx, nxt, pr, smtc, sna, stld, teck, trv, ts, txn): each is **RESEARCH — DRAFT awaiting your review (set status: planned to approve)**. Every level is a formula output; approving means editing what you disagree with and setting `status: planned`, then Zoya/Musaffa. No PLANNED/LIVE cards, so no BUY-CANDIDATE.

## Follow-ups
1. Re-screen NOW and BMNR in Zoya/Musaffa (both stale); settle BMNR's business-activity question.
2. Decide how to treat NOW after the earnings gap and stop breach (hold per core rule vs. re-underwrite; update `last_review`, add a variant view/target).
3. Review whether `core` trade_type should suppress the trailing-stop SELL on both holdings.
4. Optionally skim the 7 LEADs; avoid acting on names reporting this week without a gap plan.
5. Run /apply-trade after any trade.

Not financial advice; verify Shariah status in Zoya/Musaffa.
