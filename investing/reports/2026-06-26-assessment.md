# Portfolio Assessment — 2026-06-26

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps (be upfront about these)
- The sandbox's egress policy still blocks Yahoo (`fc.yahoo.com` / yfinance),
  so `scripts/discover.py`, `scripts/dcf.py`, and the technical block of
  `scripts/verdict.py` (chandelier trailing stop, EMA, 6m momentum, R-multiple)
  could not run this time either — same gap as 2026-06-25.
- This time the live-price fallback in `scripts/signals.py` ALSO failed (curl
  403), so the scripts returned the **stale `last_price` recorded in the
  holdings .md files** (FIG $19.26, NOW $106.40) rather than a fresh quote —
  unlike yesterday, today's script price is not even same-day spot.
- To avoid reporting stale numbers as current, I pulled approximate prices via
  web search instead (sources below). These are secondary-source estimates,
  not a verified feed — treat them as directional, not exact, and confirm in
  your own brokerage before acting.
  - **FIG**: ~$16.84–$18.64 (StocksToTrade/Investing.com, 2026-06-25/26) —
    down from the $19.26 last recorded.
  - **NOW**: ~$89–$94, range $89.39–$93.72 across sources (Motley Fool, CNN,
    StocksToTrade, 2026-06-26) — down from the $106.40 last recorded, despite
    one source noting an intraday bounce (+8% on the day quoted).
- `watchlist.md` still has no live tickers beyond yesterday's auto-discovered
  list (discovery couldn't refresh it — Yahoo blocked again).

## Verdicts (lead with this)
- **FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
  irrespective of price, unchanged from 2026-06-25). At the web-search price
  (~$17), return vs. $21.43 cost basis is roughly **-20%**, which would also
  independently trip `drawdown_review_pct` (20) if/when the technical script
  can confirm it — but COMPLIANCE_GATE already overrides this.
- **NOW -> HOLD, but watch the drawdown line** (RULE: VALUATION_RICH, P/E
  ~119, unchanged). At the web-search price (~$89–94) vs. $114.97 cost basis,
  return is roughly **-18% to -22%** — this straddles the `drawdown_review_pct`
  (20%) threshold for the first time this routine has tracked it. That rule
  (REVIEW thesis, not an auto-sell) may now be firing or about to fire; I
  can't confirm precisely because the live feed is down, so flag this for a
  same-day check in your brokerage rather than treating it as confirmed.
- Trailing stop / R-multiple / 6m momentum: still unavailable (data gap above).
- Portfolio note: only 2 holdings, so the concentration rule is still muted
  until >= 4 names (per `verdict.py`).

## Snapshot
| Ticker | Recorded last_price | Approx. current (web, unverified) | Shares | Cost basis | Approx. return |
|---|---|---|---|---|---|
| FIG | $19.26 | ~$16.84–$18.64 | 35 | $21.43 | ~-13% to -21% |
| NOW | $106.40 | ~$89.39–$93.72 | 7 | $114.97 | ~-18% to -22% |

Weights not recomputed this run — `prices.py`'s feed is down, and I don't
want to present a precise weight number built on an approximate price.

## Action flags (priority order)
1. **[Mandate] FIG flagged NON-compliant** — off-policy for a Shariah mandate,
   independent of price. Unchanged from yesterday; still unresolved.
2. **[Valuation] NOW P/E ~119** — rich; growth has to keep delivering.
3. **[New] NOW approaching/crossing the 20% drawdown-review line** — per the
   approximate prices above. Worth confirming with a live quote today; if
   confirmed, your own `drawdown_review_pct` rule says re-examine the thesis
   (not necessarily sell).

## Per-holding read

### FIG — Figma, Inc.
- **Case to keep**: Q1 beat (+41–46% rev growth depending on source), raised
  guidance, real AI-feature adoption. Several analysts (per search, June 2026)
  still carry "Buy" with price targets well above the current quote (avg.
  ~$36.78 reported by one source) — a view that the post-IPO decline (~80%
  from peak) has overshot the fundamentals.
- **Case to trim/exit**: still recorded **non-compliant** since 2026-06-09 —
  under your mandate this overrides the fundamental debate; you don't average
  down or hold for a recovery on a name that fails the gate. The stock has
  kept sliding (~37% in June alone per one source) with no compliance change
  reported.
- No catalyst-flip in the data I could find since yesterday's Config 2026
  session — the post-event price action looks like continued selling, not a
  reversal, but this is from secondary sources, not your broker.

### NOW — ServiceNow, Inc.
- **Case to keep**: AI partnership news flow continued today — expanded
  IBM collaboration (joint H2-2026 offerings) plus new partners (Inspira
  Enterprise, Hackett, HPE); Benchmark reiterated Buy with a $130 target
  (raised from $125); Street average target ~$140.63 per one source.
- **Case to trim/hold off adding**: the pullback has deepened materially —
  from a ~$139 high on 2026-06-01 down into the high-$80s/low-$90s, roughly
  a 30%+ drawdown from that high and ~18–22% below your $114.97 cost basis.
  P/E ~119 (VALUATION_RICH) is unchanged, and the stock is now closer to its
  52-week low ($81.24) than at any point this routine has tracked.
- This is a genuine tension: bullish analyst/news flow vs. a price move that's
  now brushing your own drawdown-review line. That's exactly what
  `drawdown_review_pct` exists to surface — re-examine the thesis with fresh
  eyes, not a verdict either way.
- Next catalyst: ~2026-07-22 earnings (about 4 weeks out) — no TIME_STOP issue.

## Suggested actions (from YOUR rules, rules.md)
- **COMPLIANCE_GATE fired -> FIG**: "screened non-compliant -> SELL (exit;
  cure/purify per Zoya/Musaffa)." Unchanged from 2026-06-25.
- **VALUATION_RICH fired -> NOW**: "P/E >= pe_rich (50) -> HOLD, do not add."
  Unchanged.
- **DRAWDOWN_REVIEW possibly firing -> NOW**: "down > drawdown_review_pct (20%)
  vs cost -> REVIEW thesis." Based on approximate web prices only — confirm
  with a live quote before treating this as triggered.
- No SELL triggers from Stage 4 (HARD_STOP/TRAIL_STOP/MOMENTUM_STOP/EMA_BREAK)
  could be evaluated — technical data still unavailable.

If you execute anything from this report, run `/apply-trade` so the holdings
files and ledger stay in sync.

## DCF
Unavailable again this run — same Yahoo egress block as 2026-06-25. Recorded
assumptions for reference:
- FIG: growth_5y 30%, terminal growth 3%, discount rate 12%.
- NOW: growth_5y 18%, terminal growth 3%, discount rate 10%.

## New ideas
`discover.py` returned an empty pool again (Yahoo blocked), so no fresh
auto-discovery this run. Yesterday's auto-discovered watchlist (TSM, ISRG,
AMD, QCOM, LLY, NVDA) is unchanged and still all capped at **RESEARCH** by
`recommend.py` — DATA_GAP (no price feed) prevents reward:risk computation
for all six; NVDA is additionally capped by CATALYST_GATE (catalyst 62 days
out > 60-day horizon). All Shariah status remains UNVERIFIED — screen each in
Zoya/Musaffa before doing anything else with them. No verdict has moved to
BUY-CANDIDATE.

## Follow-ups
1. **Priority**: get a live quote for NOW today and check whether it has
   actually crossed -20% vs. cost basis; if so, work through the
   DRAWDOWN_REVIEW thesis-check rather than reacting to price alone.
2. Verify FIG's non-compliant status in Zoya/Musaffa and decide on
   exit/timing given the COMPLIANCE_GATE rule — unresolved two days running.
3. Re-run `python scripts/dcf.py`, `scripts/verdict.py`, and
   `scripts/discover.py` from a network-unrestricted environment — the
   sandbox block has now affected two consecutive runs.
4. `watchlist.md` ideas are stuck at RESEARCH for lack of price data; if you
   have access to a live feed, prioritize TSM/ISRG (earnings 2026-07-16,
   soonest catalysts) for reward:risk definition.

---
Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag, not a fatwa — verify independently in Zoya/Musaffa before
acting.

Sources:
- [FIG Stock Slides As Traders Focus On Deepening Pullback](https://stockstotrade.com/news/figma-inc-fig-news-2026_06_25-2/)
- [Figma, Inc. (FIG) Stock Price, News, Quote & History - Yahoo Finance](https://finance.yahoo.com/quote/FIG/)
- [ServiceNow Stock Draws Bullish Targets As AI Deals Pile Up](https://stockstotrade.com/news/servicenow-inc-now-news-2026_06_26/)
- [ServiceNow Stock Builds AI Momentum As Analysts Boost Targets](https://stockstotrade.com/news/servicenow-inc-now-news-2026_06_26-2/)
- [ServiceNow, Inc. (NOW) Stock Price, News, Quote & History - Yahoo Finance](https://finance.yahoo.com/quote/NOW/)
- [NOW Stock Quote Price and Forecast - CNN](https://www.cnn.com/markets/stocks/NOW)
- [ServiceNow - NOW - Stock Price & News - The Motley Fool](https://www.fool.com/quote/nyse/now/)
