# Portfolio Assessment — 2026-11-11

Not financial advice. This is decision support only. Every buy/sell/hold call
is yours. Shariah status below is either the broker app's recorded screen or a
mechanical ratio/business-activity pre-check, and neither one is a fatwa.
Verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 166-name raw pool; 2 dropped on liquidity, 76
dropped on a Shariah ratio/business flag; top 50 kept) → `scaffold.py
--all-leads` (27 new DRAFT cards; 23 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py`. All of them ran on live data. Yahoo was rate-limited (HTTP 429
on the crumb fetch) but every script still returned data. There is still no
`transactions.csv`, so `journal.py` was not run and the discipline guard
stays dormant.

**Since the last report (2026-08-19):** no trades recorded. The two big
changes are NOW's post-earnings collapse and both Shariah screens going stale.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically. They are not advice.

**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 >= pe_rich 50: hold, do not add).
Live price **$102.85**, **-10.5%** vs. the $114.97 cost basis. The verdict
says HOLD, but the price action underneath it is the most important thing in
this report. See Action Flag #1.

| PM-grade record (recommend.py, mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW. Reward:risk and thesis fields are missing, so it cannot self-assess |
| Shariah | **REVIEW**. Recorded compliant, but screened 2026-06-09 (>100 days, stale) |
| DCF intrinsic value | $119.65 vs. $102.85 → +16.3% (assumes 18% 5y growth; see DCF caveat) |
| Trailing stop (chandelier) | **$137.38. Price is ~25% BELOW it.** It does not fire only because `trade_type: core` exempts this position |
| 6m momentum (skip last month) | +59.2% (that window ends before the late-October crash, so it is stale relative to today's price) |
| Weight | 78.9% of the book |
| Would buy today? | Mechanically "yes" per recommend.py's gates. That reflects missing inputs, not a positive signal |
| What changes the verdict | `thesis_broken: true`, an `initial_stop`, the Shariah re-screen, or a drop below -20% vs. cost (≈ $91.98), which would fire DRAWDOWN_REVIEW |

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Live price **$19.29**,
**+25.0%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW. Thesis and stop are still unfilled |
| Shariah (recorded) | **REVIEW**. Recorded compliant (screened 2026-07-07) but now stale |
| Shariah (ratio pre-check, this run) | **FAIL** again: industry `Capital Markets`, so the core business fails the screen (2nd consecutive run) |
| DCF intrinsic value | $0.72 vs. $19.29 (not meaningful because the DCF doesn't fit an ETH-treasury company) |
| Trailing stop (chandelier) | $19.93. **Price is ~3.3% below it** (core-exempt, so it doesn't fire) |
| 6m momentum | +10.9% |
| Weight | 21.1% |
| What changes the verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

Portfolio notes from verdict.py:
- Only 2 holdings, so the concentration rules stay muted until there are 4 or more names.
- **Vol throttle:** BMNR ATR 7.96% and NOW ATR 7.17%. Both say to size down per the throttle.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $19.29 | 10 | $15.43 | $192.90 | +25.0% | 21.1% |
| NOW | $102.85 | 7 | $114.97 | $719.95 | -10.5% | 78.9% |

**Total value: $912.85** | Cost: $959.09 | **Total return: ~-4.8%** (-$46.24 unrealised).
That is down from $1,105.51 / +15.3% at the 2026-08-19 report, a swing of
about -$193, almost all from NOW.

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are now stale.** NOW was screened 2026-06-09
   (155 days ago) and BMNR 2026-07-07 (127 days ago). `recommend.py` marks both
   `REVIEW: re-screen`. This is a policy item, not a price call, and it covers
   100% of the book.
2. **[Mandate, carried over] BMNR fails the business-activity pre-check** for
   the second run in a row (`Capital Markets`). Independent reporting still
   describes it as an Ethereum-treasury company: about 6.07M ETH (~4.97% of
   supply), 5.23M of it staked, and staking accounts for $121M of $125M FY
   revenue. A Zoya/Musaffa re-screen resolves both #1 and #2 for this name.
3. **[Thesis event] NOW had its worst day on record after Q3 (Oct 28–29).**
   Shares fell about 27% on Oct 29. Adj. EPS was $1.00 vs. $1.02 expected,
   revenue was $4.107B vs. $4.095B expected, and Q4 cRPO growth was guided to
   ~18.5% (down from 20.5%). That fed "AI-disruption" fears about the seat
   model. FY26 subscription guidance was nudged *up* to $15.78–15.79B, and the
   AI-contract year-end target was raised to ≥ $1.7B. Since then the stock
   briefly dipped below $100, and coverage on 2026-11-10 tied a further leg
   down to competition from new Anthropic workplace tools. Weekly closes went
   from $158.96 (wk of Oct 25) to $105.12 to $101.97 to $102.86.
4. **[Housekeeping, now consequential] NOW has no defensive levels.**
   `initial_stop`, `invalidation`, `target_price` and `pre_mortem` are all
   null. As a result HARD_STOP can't fire, and the only rule left between here
   and an automatic review is DRAWDOWN_REVIEW at -20% vs. cost (≈ $91.98,
   about 10.6% below today). The `catalyst` field still points at "Q2 FY2026
   earnings", which has passed twice now.
5. **[Housekeeping, carried over] BMNR holding file** still has null
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price` and
   `pre_mortem`. BMNR reports earnings on **2026-11-20**, 9 days out, after a
   10-K showing an expected FY26 net loss of ~$6.3B (mostly unrealized, from
   the decline in ETH).
6. **[Valuation] NOW P/E ~119** (signals.py priority 3). VALUATION_RICH:
   hold, do not add.

## Per-holding read

**NOW.** Does the recorded thesis ("durable enterprise-workflow subscription
grower; AI-agent expansion is the forward driver") still hold?
- *Case to keep:* Revenue beat, and FY subscription guidance went up rather
  than down. cRPO growth of ~18.5% is a deceleration, not a collapse. AI
  contract value is growing (≥ $1.7B target). The DCF at the recorded 18%
  growth assumption still shows ~16% above price. The position is only -10.5%
  vs. cost.
- *Case to trim/exit:* The market is repricing the *forward driver* in your
  own thesis. "AI-agent expansion" is exactly where the disruption fear sits.
  Growth is decelerating while the stock still trades at P/E ~119. Price is
  ~25% below the chandelier level that would have stopped out a swing-tagged
  trade. At 78.9% of the book it is a concentration risk your rules mute only
  because you hold fewer than 4 names. The Armis deal ($7.75B) adds
  integration risk.
- Either way, the cleanest next step is the one the framework asks for: a
  written "would I buy this here today?" re-underwrite. Fill in `invalidation`
  and `initial_stop` and update `last_review` (currently 2026-06-15). The
  routine does not pick a side.

**BMNR.**
- *Case to keep:* +25% vs. cost, a large ETH treasury (~$14.3B in crypto, cash
  and securities), and staking income.
- *Case to trim/exit:* The compliance question is unresolved and now
  stale-dated as well. Price has rolled over from ~$27.56 (late Sept) to about
  $19.3 and sits below its chandelier level. Earnings on Nov 20 come with a
  very large reported loss. The DCF doesn't apply, so you have no valuation
  anchor recorded at all.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired → NOW**: hold, do not add.
- **COMPLIANCE_GATE**: does not fire on its own, because it reads the recorded
  `shariah.status` (`compliant`). Staleness surfaces in `recommend.py` as
  REVIEW but doesn't change verdict.py's verb. Your own policy is to re-screen,
  and that follow-up is on you.
- **TRAIL_STOP**: would fire for **both** NOW (102.85 < 137.38) and BMNR
  (19.29 < 19.93) if they were tagged swing/momentum/catalyst. Both are tagged
  `core`, so it is exempt. This is the first run where that exemption is the
  only thing keeping a SELL off the page.
- **DRAWDOWN_REVIEW**: not firing (NOW is -10.5% vs. cost; the threshold is
  -20% ≈ $91.98).
- **HARD_STOP**: can't evaluate because neither holding has an `initial_stop`.
- **VOL_THROTTLE**: fired for both (ATR > 7%). Size down any adds.

*If you execute anything from this report, run `/apply-trade` so the holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $102.85 | +16.3% | growth_5y 18%, terminal 3%, discount 10% |
| BMNR | $0.72 | $19.29 | -96.3% (not meaningful) | growth_5y 5% (default), terminal 2.5%, discount 10% |

Caveat on NOW: the 18% 5-year growth input was set before the Q3 cRPO guide
down to ~18.5%. If you believe growth keeps decelerating, the intrinsic value
falls quickly, so re-check the input rather than reading the +16% as a margin
of safety.

## New ideas (watchlist.md)

The hand-curated ticker list in `watchlist.md` is still **empty**, so there
was nothing for step-4 idea research. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs**, which is expected. No reviewed card has
`status: planned`: all 90 cards in `setups/` are `draft`.

## Draft & planned setups: 50 leads, 27 new DRAFT cards

Pool: SPUS holdings + the `growth_technology_stocks` / `undervalued_large_caps`
screens. Only **3 of 50** clear to the LEAD tier; the other 47 are capped at
RESEARCH by the asymmetry or catalyst-horizon gate.

| Ticker | Verdict | Card | R:R (discovery) | Catalyst | Entry / target / stop (formula) |
|---|---|---|---|---|---|
| MU | LEAD | existing draft | 14.7:1 | earnings 2026-12-23 | ~819.80 / 1255.44 / 812.18 |
| DLO | LEAD | existing draft | 5.1:1 | earnings **2026-11-12 (tomorrow)** | ~13.96 / 16.16 / 13.53 |
| AVGO | LEAD | existing draft | 3.3:1 | earnings 2026-12-09 | ~354.13 / 493.22 / 311.94 |

Verdict for all three: `RESEARCH — DRAFT awaiting your review (set status:
planned to approve)`. Every level is a formula output. MU's stop sits <1%
under entry, and that tightness is what inflates its 14.7:1 ratio. DLO's print
is tomorrow, so its catalyst is effectively already here and any plan needs a
gap plan.

New DRAFT cards this run (27): ORCL-PD, KLAC, ASML, COHR, VIAV, FN, AEM, BBY,
FRO, NUE, UI, NTAP, HSY, STLD, SMTC, NTNX, KEYS, TECK, ANET, LSCC, DIOD, ASND,
SNA, TS, TXN, HST, PSX. The full table is in `leads.md`. All are Shariah
**UNVERIFIED** by construction.

**Flags before you spend review time:**
- **ORCL-PD looks like a fixed-income / preferred-type listing, not common
  stock.** Yahoo returns no name, quote type or industry, and the ratio
  pre-check was inconclusive (no market cap). An interest-bearing instrument
  would fail a Shariah screen on its face. It got past discovery because the
  ratio check passes on missing data. Treat its card as noise. This is a
  discovery-filter gap worth closing (exclude non-EQUITY quote types).
- **HST** (Host Hotels, a lodging REIT), **HSY** and **PSX**: tenant-mix /
  business-activity questions that a ratio pre-check can't answer.
- **FRO** (tanker shipping) and **TS** carry leverage that is worth checking
  against the 33% debt ratio in Zoya/Musaffa.
- The mining cluster recurs (**AEM, AGI, AU, KGC, TECK**), with the same
  royalty/streaming financing question as prior runs.

## Follow-ups (priority order)

1. **[Mandate] Re-screen NOW and BMNR in Zoya/Musaffa.** Both are stale, which
   is 100% of the book. For BMNR this also answers the business-activity fail.
2. **[Decision, time-sensitive] NOW re-underwrite.** Write `invalidation`,
   `initial_stop` and a fresh `last_review`, and update the stale `catalyst`
   field (next print is roughly late Jan 2027). Decide deliberately whether
   `trade_type: core` is still how you want this position governed, since
   that tag is the only thing suppressing a trailing-stop SELL.
3. **[Dated] BMNR earnings 2026-11-20.** Fill the holding's thesis/stop
   fields before the print so the gap-plan logic has something to work with.
4. **[Tooling] Exclude non-equity quote types (e.g. ORCL-PD) in discover.py.**
5. **[Housekeeping] 27 new DRAFT cards** (90 total, 0 planned). Review at your
   own pace.
6. **[Infrastructure, still open]** No ledger. Log the FIG sale and BMNR buy
   via `/apply-trade` to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag or a mechanical ratio/business-activity pre-check, neither a fatwa.
Verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow shares plunge 27% to worst day ever after earnings revive AI disruption fears — CNBC](https://www.cnbc.com/2026/10/29/servicenow-now-earnings-q3-2026.html)
- [ServiceNow Stock Falls 18%: Q3 2026 Earnings & Outlook — INDmoney](https://www.indmoney.com/blog/us-stocks/servicenow-stock-fall-q3-earnings-outlook)
- [Why ServiceNow Stock Plunged This Week — Motley Fool](https://www.fool.com/coverage/market-movers/2026/10/30/why-servicenow-stock-plunged-this-week/)
- [What Is Behind The Move In ServiceNow Stock? — Trefis](https://www.trefis.com/stock/now/articles/621573/what-is-behind-the-move-in-servicenow-stock/2026-10-30)
- [NOW Stock Faces the Last Support on Anthropic Workplace News — FX Leaders](https://www.fxleaders.com/news/2026/11/10/now-stock-faces-the-last-support-on-anthropic-workplace-news-as-servicenow-shares-decline-following-third-quarter-earnings-report/)
- [Bitmine (BMNR) Announces ETH Holdings Reach 6.06 Million Tokens — Nasdaq](https://www.nasdaq.com/press-release/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens)
- [Bitmine (BMNR) Stock Slips as $6.3B Paper Loss Outweighs Staking Revenue — CoinCentral](https://coincentral.com/bitmine-bmnr-stock-slips-as-6-3b-paper-loss-outweighs-staking-revenue)
- [BitMine's net loss for the fiscal year 2026 — ChainCatcher](https://www.chaincatcher.com/en/article/2303561)
- [Bitmine Immersion Technologies (BMNR) — StockAnalysis](https://stockanalysis.com/stocks/bmnr/)
