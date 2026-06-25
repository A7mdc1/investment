# Portfolio Assessment — 2026-06-25

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is the broker app's recorded screen;
verify in Zoya/Musaffa before acting on it.

## Data gaps (be upfront about these)
- `scripts/dcf.py` and the technical block of `scripts/verdict.py` (chandelier
  trailing stop, EMA_fast/slow, 6m momentum, R-multiple) could not run — the
  sandbox's egress policy blocks `fc.yahoo.com` (yfinance `history()`), so no
  DCF intrinsic value or technical levels are available this run. Re-run
  `python scripts/dcf.py` and `python scripts/verdict.py` from an environment
  with full network access to fill these in.
- Live spot price (`fast_info.last_price`) DID come through for both names.
- `watchlist.md` has no tickers entered (only commented examples), so there
  is no new-ideas section this run — nothing to research.

## Verdicts (lead with this)
- **FIG -> SELL** (RULE: COMPLIANCE_GATE — recorded non-compliant; off-mandate
  irrespective of price). Trailing stop/R-multiple/momentum: unavailable (data
  gap above). This is your own pre-set rule firing, not a price call.
- **NOW -> HOLD** (RULE: VALUATION_RICH — P/E ~119, "hold, do not add").
  Trailing stop/R-multiple/momentum: unavailable (data gap above).
- Portfolio note: only 2 holdings, so the concentration rule (`max_position_pct`)
  is muted until >= 4 names (per `verdict.py`).

## Snapshot
| Ticker | Price | Shares | Cost basis | Return | Weight* |
|---|---|---|---|---|---|
| FIG | $19.26 | 35 | $21.43 | -10.1% | 47.5% |
| NOW | $106.40 | 7 | $114.97 | -7.5% | 52.5% |

*Weights are of the two-name book only (no cash line tracked by the scripts run).

## Action flags (priority order, from signals.py)
1. **[Mandate] FIG flagged NON-compliant** — off-policy for a Shariah mandate
   independent of price. This is a policy issue, not a price call. Verify in
   Zoya/Musaffa, then decide on exit/timing.
2. **[Valuation] NOW P/E ~119** — rich; growth has to keep delivering to
   justify it.

## Per-holding read

### FIG — Figma, Inc.
- **Case to keep**: Q1 beat (+41-46% rev growth depending on source) with
  raised full-year guidance; AI-feature adoption is real. Stock is down
  ~35-38% YTD and recently lost $3.5-3.8B in market cap over a 6-7 day
  losing streak, which on fundamentals alone could read as overdone.
- **Case to trim/exit**: the position is already recorded **non-compliant**
  by your broker's Shariah screen (since 2026-06-09) — under your mandate
  that overrides the fundamental case entirely; you don't average down or
  hold for a recovery on a name that fails the gate. Separately, short
  interest >36%, AI-native competitive pressure (e.g., Google), and an
  activist investor reportedly raising questions about Figma's ties to
  Anthropic (StocksToTrade, 2026-06-17) add thesis risk on top of the
  compliance issue.
- **Catalyst that just passed**: Figma's Config 2026 investor/analyst session
  was held 2026-06-24 (yesterday). Per Yahoo Finance coverage, it was framed
  as a test of whether the AI growth story can offset the weak share price —
  the session and stock reaction are worth checking in your own tracker,
  since this report's data fetch can't pull the day-after price move.
- I could not verify the FIG compliance status independently — that is
  exactly what Zoya/Musaffa is for; this report only relays the broker's
  recorded flag.

### NOW — ServiceNow, Inc.
- **Case to keep**: durable subscription growth (~21% revenue / ~23%
  earnings in 2025), AI-agent platform (Now Assist, AI Control Tower,
  "Zurich") with AI revenue expectations raised from ~$1B to ~$1.5B per
  recent reporting, Q1 2026 beat on subscription revenue, RPO, margin and
  free cash flow, and an additional $5B buyback authorized. Benchmark raised
  its price target to $130 (from $125) on 2026-06-15; IBM/ServiceNow
  announced expanded collaboration on 2026-06-11.
- **Case to trim/hold off adding**: P/E ~119 is priced for continued
  high growth — any deceleration would likely hit the stock hard, which is
  exactly the VALUATION_RICH rule firing. Note also CNBC reported NOW stock
  fell ~14% around 2026-04-22 on subscription revenue impact tied to the
  Iran war — a reminder this name is sensitive to macro/geopolitical
  disruption to enterprise IT spend, not just execution.
- **Upcoming catalyst**: next earnings call ~2026-07-22 (about 4 weeks out) —
  no TIME_STOP concern yet.
- Recorded compliant per broker app (purification 3.35%) — verify
  independently in Zoya/Musaffa as always.

## Suggested actions (from YOUR rules, rules.md)
- **COMPLIANCE_GATE fired -> FIG**: "screened non-compliant -> SELL (exit;
  cure/purify per Zoya/Musaffa)." Supporting fact: `holdings/fig-figma.md`
  front-matter `shariah.status: non-compliant`, screened 2026-06-09, not
  stale.
- **VALUATION_RICH fired -> NOW**: "P/E >= pe_rich (50) -> HOLD, do not add."
  Supporting fact: recorded P/E ~119.02, current threshold `pe_rich: 50`.
- No SELL triggers from Stage 4 (HARD_STOP/TRAIL_STOP/MOMENTUM_STOP/EMA_BREAK)
  could be evaluated this run — technical data unavailable (see data gaps).

If you execute anything from this report, run `/apply-trade` so the holdings
files and ledger stay in sync.

## DCF
Unavailable this run — `yfinance` historical-data fetch was blocked by the
sandbox's egress policy (CONNECT to `fc.yahoo.com` denied, 403). Recorded
assumptions for reference, re-run `python scripts/dcf.py` with network access
to get intrinsic value vs. price:
- FIG: growth_5y 30%, terminal growth 3%, discount rate 12%.
- NOW: growth_5y 18%, terminal growth 3%, discount rate 10%.

## New ideas
None this run — `watchlist.md` has no tickers entered (only commented
examples). Add names/themes there for the next assessment to research.

## Follow-ups
1. Verify FIG's non-compliant status in Zoya/Musaffa and decide on
   exit/timing given the COMPLIANCE_GATE rule.
2. Re-run `python scripts/dcf.py` and `python scripts/verdict.py` from a
   network-unrestricted environment to get DCF intrinsic value and the
   trailing-stop / EMA / momentum technical readout.
3. Populate `watchlist.md` with tickers/themes if you want new-idea
   generation next time.
4. Check FIG's actual post-Config-2026-session price action (session was
   2026-06-24); this report's price data is same-day spot only.

---
Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag, not a fatwa — verify independently in Zoya/Musaffa before
acting.

Sources:
- [Figma Config 2026 Session Tests AI Growth Story And Weak Share Price](https://finance.yahoo.com/markets/stocks/articles/figma-config-2026-session-tests-071718475.html)
- [Figma to Host Investor and Analyst Session at Config 2026](https://investor.figma.com/news-events/news/news-details/2026/Figma-to-Host-Investor-and-Analyst-Session-at-Config-2026/default.aspx)
- [FIG Stock Jumps As Activist Targets Figma–Anthropic Ties](https://stockstotrade.com/news/figma-inc-fig-news-2026_06_17/)
- [ServiceNow stock sinks 14% as subscription revenue takes hit from Iran war](https://www.cnbc.com/2026/04/22/servicenow-now-earnings-q1-2026.html)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports - TipRanks](https://www.tipranks.com/stocks/now/earnings)
