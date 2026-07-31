# Portfolio Assessment — 2026-07-31

Decision support, not financial advice. Every Shariah status below is a broker-app
record or a mechanical ratio pre-check — neither is a fatwa; verify independently
in Zoya/Musaffa before acting on anything here.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired)
- Price $17.01 | trailing stop $14.61 (chandelier, 14% below price) | R-multiple: n/a (no entry stop recorded) | 6m momentum: -47.0%
- Portfolio note: BMNR daily ATR 7.26% > `vol_throttle_atr_pct` (6%) — size down per the vol throttle if adding.
- PM record (recommend.py, mechanical proxy): conviction **LOW** — "reward:risk -6.7:1 — skew too thin." Target used is DCF intrinsic value ($0.72, see DCF section) against a $17.01 price and a $14.61 downside stop — the negative R:R is an artifact of a cash-flow DCF applied to a crypto-treasury balance-sheet story, not a real read on the trade; treat this number as noise, not signal. `would_buy_today: true` per the mechanical check, but no `conviction`, `variant_view`, `target_price`, or `pre_mortem` are filled in the holding file — those are yours to write if you want the PM record to mean anything here.

**NOW -> HOLD** (RULE: VALUATION_RICH — P/E ~119.02, hold, do not add)
- Price $111.02 | trailing stop $98.58 (chandelier, 11.2% below price) | R-multiple: n/a (no entry stop recorded) | 6m momentum: -9.4%
- PM record: conviction **LOW** — "reward:risk 0.7:1 — skew too thin" (DCF target $120.12 vs stop $98.58 is a shallow band relative to current price). Thesis one-liner on file: "Durable enterprise-workflow subscription grower; AI-agent expansion is the forward driver." `variant_view`, `target_price`, `invalidation`, `pre_mortem` are still blank in the holding file (last_review 2026-06-15, now 46 days stale against `review_cadence_days: 90` — not yet due, but worth a fresh look given the earnings print below).

Portfolio note (verdict.py): only 2 holdings — concentration rule stays muted until >= 4 names (`min_names_for_concentration`).

## Snapshot

| Ticker | Value | Weight | Return | Price |
|---|---|---|---|---|
| BMNR | $170.20 | 18.0% | +10.3% | $17.02 |
| NOW | $777.21 | 82.0% | -3.4% | $111.03 |
| **Total** | **$947.41** | | | |

Since the 2026-07-13 report: FIG was sold (closed 2026-07-13, realized P/L +$54.95), closing out the 7-run compliance flag that had topped every prior report's follow-up list. BMNR was added as a new position. The book is now 2 names, both technically HOLD.

## Action flags (priority order)

1. **[Mandate-level — new] BMNR Shariah ratio pre-check flag.** Recorded status is `compliant` (broker app, screened 2026-07-07), but the mechanical ratio pre-check flags: *"industry 'Capital Markets' matches 'capital markets' — core business fails screen."* Sector is Financial Services / Capital Markets. This is exactly the shape of issue that made FIG a 7-run flag — a broker-app "compliant" tag sitting on top of a business-activity conflict the ratio screen catches. Re-screen BMNR in Zoya/Musaffa specifically on the business-activity test (not just the ratio test) before adding to this position.
2. **[Valuation] NOW P/E ~119** (signals.py, priority 3) — "rich; growth has to keep delivering to justify it." This is the VALUATION_RICH rule firing in the verdict above, not new information, but worth restating: it caps the position at HOLD, do-not-add, regardless of the earnings beat below.
3. **[Data gap]** Neither holding file has `conviction`, `target_price`, `initial_stop`, `invalidation`, or `pre_mortem` filled in. The engine correctly refuses to invent these — until you write them, the PM records above are mechanical placeholders, not real underwriting.

## Per-holding read

**BMNR (Bitmine Immersion Technologies)** — Recent news (late July 2026): the company is trading as a leveraged Ethereum proxy — ETH treasury holdings are being staked (~4.92M ETH staked as of 2026-07-26, ~$9.6B, projected ~$254M annualized staking revenue at scale), and BMNR has been running the largest common-stock buyback of any ETH/BTC digital-asset-treasury company (11.6M shares repurchased since 2026-07-01). Total crypto + cash + "moonshot" holdings were reported at $11.8B. Stock popped ~12.7% on 2026-07-27 on this. [BMNR Stock Climbs As Massive Ethereum Bet Draws Trader Focus](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_27/) — the case to keep: buyback + staking-yield narrative is intact and price is +10.3% on your cost basis; the case to trim/watch: a DCF built for a cash-flow business (5% growth, 2.5% terminal, 10% discount) is structurally the wrong tool for a crypto-NAV vehicle and returns a meaningless -95.8% "downside" — don't use it to size this position — and the Shariah business-activity flag above is unresolved. 6m momentum is deeply negative (-47%) despite the recent pop, so this is a name whose price action has been volatile; the ATR-based vol throttle already flags it for smaller sizing.

**NOW (ServiceNow)** — Q2 FY2026 earnings are already out (reported late July 2026, ahead of this assessment): subscription revenue +23% cc ($3.88B, beat consensus $3.82B), operating margin 29.5% (3pts above guidance), adjusted EPS $0.90 (beat). Stock rose ~4.75% after-hours to ~$99.99 on the print and has continued higher to the current $111.02. Management leaned hard on Armis/Veza and the "AI Control Tower" (>$1B AI ACV, guiding to $1.5B by year-end) as the forward narrative for the $7.75B Armis acquisition. [Earnings call transcript — Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-beats-q2-2026-forecasts-shares-rebound-after-hours-93CH-4807190), [ServiceNow's latest earnings show why it paid $7.75 billion for Armis](https://www.calcalistech.com/ctechnews/article/s1thnxksmg). The case to keep: growth and margin both beat, AI narrative has real revenue behind it now, Shariah ratio pre-check is clean (debt ratio 2.1%, liquid ratio 5.5%). The case to trim/watch: P/E ~119 is priced for continued high growth (VALUATION_RICH rule), and the position is 82% of a 2-name book — any stumble concentrates risk. Note the holding file's `catalyst.desc` ("Q2 FY2026 earnings...") is now stale since that catalyst already fired; worth updating with the next dated catalyst (Q3 earnings, not yet announced) at your next review.

## Suggested actions (from YOUR rules, rules.md)

No SELL/TRIM/REVIEW rule fired for either holding this run — both resolve to HOLD (BMNR on DEFAULT, NOW on VALUATION_RICH, which is itself a "hold, do not add" rule, not a sell signal). Rules checked and not fired: HARD_STOP, TRAIL_STOP (both prices sit above their chandelier stops), MOMENTUM_STOP, EMA_BREAK, THESIS_BREAK, TARGET_REACHED, TIME_STOP, DEAD_MONEY, REWARD_RISK_COMPRESSED, CONCENTRATION (muted, <4 names).

If you execute anything from this report, run `/apply-trade` so the holding file + ledger update.

## DCF

| Ticker | Intrinsic value | Price | Upside/Downside | Assumptions (5y growth / terminal / discount) |
|---|---|---|---|---|
| BMNR | $0.72 | $17.02 | -95.8% | 5% / 2.5% / 10% — **not a meaningful read for a crypto-treasury balance sheet; flagged above, don't act on this number** |
| NOW | $120.12 | $110.99 | +8.2% | 18% / 3% / 10% |

## New ideas

`watchlist.md` is currently empty (hand-curated list — no names have been added yet), so `recommend.py`'s `ideas` array is empty this run. All candidate generation this run came from `discover.py` (machine-wide, Shariah-unverified LEADs only — see `leads.md`, 50 rows, regenerated 2026-07-31) plus `scaffold.py`, which auto-filled **31 new DRAFT setup cards** this run (61 total in `setups/`, all still `status: draft` — none promoted to `planned`). None of these are BUY-CANDIDATE; a DRAFT card cannot become one until you review it, edit what you disagree with, and flip `status: planned`, and then screen it compliant in Zoya/Musaffa.

Two leads worth flagging for attention given tight catalyst windows already inside the next 2 weeks:
- **AU** (Anglo American / gold) — earnings 2026-07-31 (today) — reward:risk 14.0:1 per discovery estimate; has a setup card.
- **MT** (per the 2026-07-13 report, carried a flag for an implausibly tight engineered entry/stop/target band) — not in this run's top-50, dropped off the list; if still tracking it, note it's not in the current discovery output.
- **RCL, ALKT** from the 2026-07-13 run also aged out of this week's top-50 (discovery re-ranks every run; if you were mid-review on either, they still have setup cards on disk even though `leads.md` no longer lists them).

Given the sheer volume (61 draft cards), this report doesn't re-render each one — treat `setups/` as a standing review queue, not something to clear in one sitting.

## Follow-ups (priority order)

1. **[Mandate — new this run]** BMNR business-activity ratio flag ("Capital Markets" industry) — re-screen in Zoya/Musaffa before adding to the position. This is the same shape of issue FIG carried for 7 runs; catch it earlier this time.
2. **[Housekeeping]** 31 new DRAFT setup cards added this run (61 total in `setups/`); none are `planned`. Review at your own pace.
3. **[Data completeness]** Both holding files are missing `conviction`, `target_price`, `initial_stop`, `invalidation`, `pre_mortem` — fill these in to make the PM records load-bearing rather than placeholders.
4. **[Stale catalyst]** NOW's `catalyst.desc` references the Q2 earnings print that already happened; update with the next dated catalyst.
5. **[Infrastructure — still open]** No ledger yet (`transactions.csv` / `journal.csv` don't exist) — start logging trades via `/apply-trade` to unlock the discipline guard and the journal.py expectancy report. FIG's close (+$54.95 realized) would have been the first entry.
6. **[Resolved from last report]** FIG compliance flag — closed via sale on 2026-07-13. No longer open.

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag or a mechanical ratio pre-check, neither a fatwa — verify independently in
Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Trader Focus — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_27/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.79 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-79-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-8-billion-302834876.html)
- [Earnings call transcript: ServiceNow beats Q2 2026 forecasts, shares rebound after hours — Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-servicenow-beats-q2-2026-forecasts-shares-rebound-after-hours-93CH-4807190)
- [ServiceNow's latest earnings show why it paid $7.75 billion for Armis — Calcalistech](https://www.calcalistech.com/ctechnews/article/s1thnxksmg)
- [ServiceNow Q2 2026 slides: revenue beats, margins face AI pressure — Investing.com](https://www.investing.com/news/company-news/servicenow-q2-2026-slides-revenue-beats-margins-face-ai-pressure-93CH-4807204)
