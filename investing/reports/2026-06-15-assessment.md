# Portfolio Assessment — 2026-06-15

> These are mechanical rules resolving against your data — not financial advice.
> Every decision is yours. Verify Shariah status in Zoya/Musaffa before acting.
> Live prices unavailable (Yahoo Finance blocked in this environment); prices are
> from holdings front-matter. R-multiples and trailing stops not computed (no technicals).

---

## Verdicts

| Ticker | Verb | Rule | Why |
|--------|------|------|-----|
| **FIG** | **SELL** | COMPLIANCE_GATE | Non-compliant per broker app; off-mandate regardless of price |
| **NOW** | **HOLD** | VALUATION_RICH | P/E ~119 — hold, do not add |

---

## Portfolio Snapshot

| Ticker | Shares | Cost Basis | Last Price | Return | Value | Weight |
|--------|--------|-----------|-----------|--------|-------|--------|
| FIG | 35 | $21.43 | $19.26 | −10.1% | $674.10 | 47.5% |
| NOW | 7 | $114.97 | $106.40 | −7.5% | $744.80 | 52.5% |
| **Total** | | | | | **$1,418.90** | |

*Note: Web data (June 15) shows FIG ~$18.56 and NOW ~$102.88 — both are trading
slightly below recorded prices, deepening losses modestly.*

---

## Action Flags (Priority Order)

### 🔴 Priority 1 — Mandate (Policy Issue)
**FIG — NON-COMPLIANT (COMPLIANCE_GATE → SELL)**
Flagged non-compliant by broker app as of 2026-06-09. Under your rules, compliance
is a gate, not a tiebreaker. This is a policy issue, not a price call. The rule
fires regardless of thesis, return, or upcoming catalysts. Your pre-committed
action: exit. The only decision remaining is timing — before vs. after Config 2026
(June 23–25). Note: selling into a catalyst carries event risk (gap up or down).

### 🟡 Priority 3 — Valuation
**NOW — P/E 119 (VALUATION_RICH → HOLD, do not add)**
Multiple is priced for continued high growth. Your rule says hold but do not add
at this level.

---

## Per-Holding Read

### FIG — Figma, Inc.

**Numbers**: −10.1% return. Price ($19.26) is at just 2% of its 52-week range
($16.60–$142.85), deep in the lower band. Q1 2026 revenue grew 46% YoY to $333M
with net dollar retention at 139% — operationally strong.

**Near-term catalyst**: Config 2026, June 23–25 (San Francisco, Moscone Center).
Figma has scheduled an investor/analyst session at the conference. Focus will be
AI workflows and design-system expansions. Next earnings: September 9, 2026.

**Case to hold**: Q1 was a beat-and-raise; 46% revenue growth and 139% NDR are
exceptional metrics. Config could deliver an AI product reveal that re-rates the
stock. Price is near 52-week lows — selling here locks in the drawdown.

**Case to exit**: The decision driver is compliance, not price. Your mandate
treats non-compliant holdings as off-policy irrespective of return or upcoming
catalysts. Holding longer to "recover" the loss while the stock is non-compliant
conflicts with your pre-committed rules. Short interest >36% and operating losses
are additional headwinds.

**Rule fired → Your pre-committed action**: `COMPLIANCE_GATE → SELL`.
If you execute, run `/apply-trade` to update the ledger.

---

### NOW — ServiceNow, Inc.

**Numbers**: −7.5% return. Price ($106.40) is at 16% of its 52-week range
($81.24–$239.62), still in the lower-third of the range. Q1 FY2026: subscription
revenues $3,671M (+22% YoY). Compliant, purification 3.35% (screened 2026-06-09).

**Near-term catalysts**:
- Q2 FY2026 earnings expected ~late July 2026 (no confirmed date yet).
- Armis acquisition ($7.8B, closed April 2026) expands security workflow and
  AI-native vulnerability response — meaningful TAM expansion, execution risk.

**Case to hold**: Thesis intact — durable subscription growth (~22% revenue, ~23%
earnings 2025), AI-agent expansion (Zurich platform), and now Armis bolting on
security workflows. Shariah-compliant and freshly screened. The drop from the
52-week high (~$239) is macro/multiple compression, not thesis deterioration.

**Case to trim**: At P/E 119, any growth deceleration hits hard. Armis at $7.8B
is a significant acquisition that introduces integration risk. Price is ~51%
below 52-week high and showing no technical recovery yet (no live data).

**Rule fired → Your pre-committed action**: `VALUATION_RICH → HOLD, do not add`.
No additional action required unless another rule fires (e.g. HARD_STOP, TRAIL_STOP
— not computable without live technicals).

---

## DCF

Live price fetch failed (Yahoo Finance blocked). DCF computation could not run.
Assumptions on file:
- **FIG**: growth_5y 30%, terminal 3%, discount 12%
- **NOW**: growth_5y 18%, terminal 3%, discount 10%

At a 18% 5-year growth rate and 10% discount, NOW's intrinsic value would be
sensitive to any multiple compression — the recorded cost basis of $114.97 and
current price ~$106 suggest the market has already re-rated it lower since entry.

---

## New Ideas from Watchlist

Watchlist is empty — no tickers or themes added yet. Add names to `watchlist.md`
to get catalyst research and compliance pre-screening in future runs.

---

## Follow-ups (Priority Order)

1. **FIG — decide exit timing**: Rule says SELL. The only open question is
   before or after Config (June 23–25). Factor in: you may not get a better
   price if Config disappoints; compliance clock continues while you hold.
2. **Verify FIG in Zoya/Musaffa** to confirm broker-app status is current.
3. **Add live price access** — Yahoo Finance is blocked in this environment.
   Without it, technicals, trailing stops, R-multiples, and DCF cannot run.
4. **NOW Q2 earnings date** — confirm ~late July; mark calendar to reassess
   thesis vs. results, especially Armis integration progress.
5. **Populate watchlist.md** — add tickers/themes to get idea generation in
   next run.
6. **Purification for NOW**: 3.35% of gains/dividends to be set aside.
   Calculate and log after any partial sale or at year-end.

---

> **Not financial advice.** This routine applies your own pre-committed rules
> mechanically. Every buy, hold, and sell decision is yours. Shariah status must
> be verified in **Zoya** or **Musaffa** — the ratio pre-check here is
> informational only and not a substitute for a qualified screen.

Sources:
- [Figma Q1 2026 Earnings — StocksToTrade](https://stockstotrade.com/news/figma-inc-fig-news-2026_05_18/)
- [Figma Stock +13% After Q1 2026 Earnings — TIKR](https://www.tikr.com/blog/figma-stock-surged-13-after-q1-2026-earnings-is-the-recovery-real)
- [FIG Stock Dips June 12 — TimothySykes](https://www.timothysykes.com/news/figma-inc-fig-news-2026_06_12/)
- [Config 2026 — Figma Investor Session](https://investor.figma.com/news-events/news/news-details/2026/Figma-to-Host-Investor-and-Analyst-Session-at-Config-2026/default.aspx)
- [Config 2026 — Moscone Center](https://moscone.com/events/config-2026)
- [ServiceNow Q1 FY2026 8-K — SEC](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm)
- [ServiceNow NOW Stock Overview — StockAnalysis](https://stockanalysis.com/stocks/now/)
