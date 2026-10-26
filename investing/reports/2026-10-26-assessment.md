# Portfolio Assessment — 2026-10-26

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is either the broker app's recorded screen or a mechanical
ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo; 158-name pool, 73 dropped on Shariah ratio/business flag,
1 on liquidity, 2 no price; top 50 kept) → `scaffold.py --all-leads` (21 new DRAFT
cards; 29 existing unchanged) → `prices / shariah / dcf / signals / verdict /
recommend` — all live, no data gaps. `journal.py` not run (no `transactions.csv`).
No holdings changed since 2026-08-19.

## Verdicts (your rules resolving — not advice)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). $21.58, +39.9% vs $15.43 cost.
Chandelier trailing stop **$23.97** is *above* price (price ~10% below it); EMA20
$23.54 also above price. 6m momentum (skip last month) +27.9%. **See flag #2 — this
HOLD looks inconsistent with the stop/EMA data.** Vol throttle: ATR 6.84% > 6% — size-down note.

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 >= 50 — hold, do not add). $155.71,
+35.4% vs $114.97. Trailing stop $141.57 (~9.1% below), EMA20 $145.62, 6m momentum +49.9%.

| Mechanical PM record (proxy, not a conviction call) | BMNR | NOW |
|---|---|---|
| Conviction | LOW (no thesis/R:R supplied) | LOW (R:R -2.5:1) |
| Shariah (recorded) | compliant, 2026-07-07 — **STALE (>100d)** | compliant, 2026-06-09 — **STALE** |
| Shariah (ratio pre-check) | **FAIL** — industry "Capital Markets" | clean (debt 1.5%, liquid 3.9%) |
| DCF intrinsic vs price | $0.72 (-96.7%) — model does not fit | $120.12 (-22.9%) |
| Would buy today (mechanical) | yes, but reads recorded field only | yes, same caveat |

## Snapshot (live)
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $21.58 | 10 | $15.43 | $215.80 | +39.9% | 16.5% |
| NOW | $155.71 | 7 | $114.97 | $1,089.97 | +35.4% | 83.5% |

**Total $1,305.77** | cost $959.09 | **+36.1% unrealised (+$346.68)**. NOW is 83.5% vs the
22% `max_position_pct`; the concentration rule is muted only because the book has < 4 names.

## Action flags (priority order)
1. **[Mandate] Both Shariah screens are stale (>100d), and BMNR's ratio pre-check
   still FAILS** on business activity (Capital Markets) — unresolved since 2026-08-19.
   Under Gate 1 a confirmed fail is an absolute SELL regardless of the +39.9%. Re-screen
   BMNR (business-activity question specifically) and NOW in Zoya/Musaffa. Do not add to either until done.
2. **[Technical / BMNR]** Price is below both the chandelier stop ($23.97) and EMA20
   ($23.54), yet verdict.py returns HOLD/DEFAULT; the "close < EMA_fast -> REVIEW" rule did
   not fire. Likely a verdict.py gap (no R-multiple because no `initial_stop` on the
   holding file) — worth checking. Reading the data by your own rules, REVIEW would be consistent.
3. **[Catalyst / NOW — 2 days out]** Q3 earnings expected **Wed 2026-10-28 after the
   close** (most sources; some list it as an estimate — [TipRanks](https://www.tipranks.com/stocks/mx:noww/earnings),
   [MarketScreener](https://uk.marketscreener.com/quote/stock/SERVICENOW-INC-10912979/calendar/) shows 10-27, likely a projection).
   NOW is 83.5% of the book, rich at P/E ~119, and has gapped hard on prints before (a
   [-17% day-after move](https://tradersunion.com/stocks/earnings/now-usd/) is reported for the April listing;
   rules.md assumes a 25% adverse gap). Binary-event exposure on the dominant position — your decision.
4. **[Data gap]** Web results conflict on BMNR's ETH holdings (a late-Oct item cites ~3.31M ETH / $14.2B total vs
   ~5.8M ETH in Aug) and could not confirm it; also reports the ETH buying spree was ending
   ([Simply Wall St](https://simplywall.st/stocks/us/software/nyse-bmnr/bitmine-immersion-technologies/news/why-is-bitmine-immersion-technologies-bmnr-pausing-its-ether),
   [TipRanks/TheFly](https://www.tipranks.com/news/the-fly/bitmine-immersion-reports-eth-holdings-of-over-3-3m-tokens-thefly)).
   Treat as unverified; check BMNR's own filings.
5. **[Valuation / NOW]** P/E ~119 rich; DCF (18% growth, 3% terminal, 10% discount) says
   -22.9% vs price. Do not add.
6. **[Incomplete holding files]** BMNR has no thesis, `initial_stop`, target or pre-mortem; NOW's
   `last_review` is 2026-06-15 (review cadence 90d -> overdue).

## Per-holding read
**BMNR** — *Keep:* +39.9% gain, 6m momentum positive, large treasury. *Trim/exit side:*
unresolved business-activity Shariah question, price under stop and EMA20, ATR 6.8%,
DCF meaningless for this model, no written thesis/stop. Not picking for you.

**NOW** — *Keep:* +35.4%, momentum +49.9%, price above stop and EMA20, recorded compliant.
*Trim side:* 83.5% weight, P/E ~119, price 22.9% above DCF, binary earnings in 2 days,
stale Shariah record. Not picking for you.

## Suggested actions (from YOUR rules.md)
- Rule VALUATION_RICH fired (NOW) -> hold, do not add.
- Rule vol throttle fired (BMNR ATR 6.84% > 6%) -> size-down note; no adds.
- Rule `review_cadence_days: 90` -> NOW last_review 2026-06-15 is overdue; BMNR never reviewed.
- Rule `max_position_pct: 22` would flag NOW (83.5%) if the book had >= 4 names (muted now).
- Rule `earnings_gap_assumption_pct: 25` -> a 25% gap on NOW is ~$272 (~21% of the book).
- Compliance gate (Gate 1) is pending the BMNR/NOW re-screens.
The routine never auto-trades. If you execute anything, run `/apply-trade`.

## DCF
Assumptions: 5y growth BMNR 5% / NOW 18%; terminal 2.5% / 3%; discount 10%. BMNR $0.72 (-96.7%)
is a model misfit (crypto treasury), not a valuation call. NOW $120.12 (-22.9%).

## New ideas (recommend.py + discovery)
No BUY-CANDIDATEs — every name is LEAD or RESEARCH (no verified Shariah, no `planned` card).
50 leads: **10 LEAD**, 40 RESEARCH. Shariah UNVERIFIED and EDGE not supplied on all.
Top by max-benefit (reward:risk / catalyst; all formula estimates):

| Ticker | Verdict | R:R | Catalyst | Card |
|---|---|---|---|---|
| AEM | LEAD* | 20.0 | earnings 10-28 | new DRAFT |
| PAY | LEAD | 8.0 | 11-02 | has card |
| LIF | LEAD | 6.8 | 11-09 | has card |
| GDDY | LEAD | 6.1 | 10-29 | has card |
| EXPE | LEAD | 5.7 | 11-04 | new DRAFT |
| BKR | LEAD | 4.8 | 10-27 | new DRAFT |
| RCL | LEAD | 4.2 | 10-27 | has card |
| DLO | LEAD | 4.0 | 11-12 | has card |
| FOX | LEAD | 3.9 | 11-02 | has card |
| NET | LEAD | 3.3 | 11-05 | has card |

*AEM's 20:1 is a stop-artifact: entry $176.37 vs chandelier stop $176.44 (stop above entry),
so target is null on the draft. Not a real asymmetry. PLTR remains RESEARCH (R:R 1.5; its
government/defense business-activity question still open). Full list: `leads.md`.

## Draft setups awaiting review
21 new DRAFT cards (`status: draft`): AAPL, AEM, APA, ASND, BBY, BKR, DDOG, EXPE, FLYW, FRO, HPE, HST,
LLY, NTAP, NTNX, PR, SMTC, STLD, TECK, TS, XOM. Each: **RESEARCH — DRAFT awaiting your review
(set status: planned to approve)**. Every entry/stop/target is a formula output; setup_type,
logic, gap plan (default `exit_before`) and invalidation are in `setups/<ticker>.md`. Shariah
is `unverified` on all. Several have earnings within days (BKR/RCL 10-27, AEM/GDDY 10-28/29), so
the gap plan matters. Approval = edit what you disagree with and flip to `planned`.

## Follow-ups
1. Re-screen BMNR (business activity) and NOW in Zoya/Musaffa; record on the holding files.
2. Decide NOW exposure before the 10-28 after-close print (hold-through vs size down).
3. Review BMNR: fill thesis, `initial_stop`, target; reconcile price < stop with HOLD.
4. Confirm BMNR's actual ETH holdings from its filings.
5. Skim the 10 LEADs; ignore AEM's artifact R:R.
6. Executed anything? `/apply-trade`.

*Not financial advice. Shariah status must be verified independently in Zoya/Musaffa.*
