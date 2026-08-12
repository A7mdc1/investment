# Portfolio Assessment — 2026-08-12

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

First run in exactly four weeks (last: 2026-07-13). `discover.py` (live Yahoo
data, 50-name pool by max-benefit rank) → `scaffold.py --all-leads` (25 new
DRAFT setup cards auto-filled for leads without one; 25 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
still shows 0 closed trades (no `transactions.csv` yet — discipline guard
stays dormant until you start logging via `/apply-trade`).

Portfolio composition changed since last run: **FIG was sold** (closed
2026-07-13, realized P/L +$54.95, exited on the seven-run-unresolved
compliance flag) and **BMNR was bought** (new position, 10 shares @ $15.43).
The book is now BMNR + NOW, two names.

## Verdicts (lead with this)

**⚠ Compliance heads-up on BMNR before anything else below.** The recorded
status is still `compliant` (broker app, screened 2026-07-07, not stale by
the 1-quarter rule), so `verdict.py`'s mechanical compliance gate does **not**
fire a SELL — that gate only reads the recorded YAML status, it does not
consult the live ratio pre-check. But `shariah.py`'s ratio pre-check, run
fresh today, flags BMNR's Yahoo industry classification as **"Capital
Markets" (sector: Financial Services) — a business-activity match, not a
debt/liquidity-ratio issue.** BMNR's actual operating model — raising equity
via a large ATM program to buy and stake ETH — is exactly the kind of
treasury/staking vehicle that deserves a fresh, specific Zoya/Musaffa screen
of *this* business model, not a rubber-stamp carry-forward of the July
screen. Per the workspace's own gate order, a ratio-or-business flag is
meant to be treated as absolute, not a tiebreaker — this is a heads-up per
`CLAUDE.md`, but it is now the single most important open item on the book.

**BMNR → HOLD** (mechanically: DEFAULT, no SELL/TRIM rule fired). Live price
**$18.10**, up **+17.3%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-7.3:1** (mechanical DCF-based skew, see caveat below) |
| Shariah | Recorded PASS (compliant, screened 2026-07-07) — **but see the ratio-precheck flag above; re-screen before adding** |
| DCF intrinsic value | $0.72 vs. $18.10 price → **-96% "upside."** Caveat: this is a standard discounted-free-cash-flow model; it does not fit a crypto-treasury company whose value is mark-to-market ETH/cash holdings ($11.6B total per company disclosures, ~5.81M ETH), not projected FCF. Treat this number as not meaningful — it is a script limitation, not a real signal. A proper comparison would be price vs. net-asset-value of the ETH+cash held per share, which isn't computed here (data gap: fully diluted share count not verified) |
| Trailing stop (chandelier) | $15.7314 — price is **13.1% above it** |
| 6m momentum (skip last month) | -18.3% |
| Portfolio note | ATR **6.57%** — above the 6% vol-throttle threshold; size down, this is a high-volatility position |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW, and the compliance question above should be resolved first |
| What changes verdict | The Zoya/Musaffa re-screen outcome, `thesis_broken: true`, or a SELL technical trigger |

**NOW → HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 ≥ `pe_rich` 50).
Live price **$124.07**, up **+7.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-0.3:1** (recommend.py can't self-assess without a stated thesis-vs-price edge; `conviction`/`variant_view` fields are still blank in the holding's front-matter) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale), ratio pre-check clean (debt ratio 1.9%, liquid ratio 4.9%) |
| DCF intrinsic value | $120.12 vs. $124.11 price → **-3.2%** (price now slightly rich to the model — this flipped from +6.9% upside last run, since price ran up faster than the model moved) |
| Trailing stop (chandelier) | $109.2491 — price is **12.0% above it** |
| 6m momentum (skip last month) | -1.5% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | Subscription growth decelerating meaningfully below ~21-22% YoY, a guidance cut tied to AI-agent/Armis traction, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until ≥ 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $18.10 | 10 | $15.43 | $180.95 | +17.3% | 17.2% |
| NOW | $124.07 | 7 | $114.97 | $868.49 | +7.9% | 82.8% |

**Total value: $1,049.44** | Cost: $959.09 | **Total return: ~+9.4%** (+$90.35 unrealised)

Both positions are up since the last snapshot (2026-07-13, book was FIG+NOW
at $1,610.49). The book is much smaller in dollar terms now — the FIG exit
realized only +$54.95, and BMNR was sized modestly (10 shares) — with NOW
now carrying 82.8% of the weight, well above any informal balance target for
a two-name book. Concentration rules stay muted per `rules.md`
(`min_names_for_concentration: 4`), but a single name at 83% of a 2-name
book is worth noting on its own terms even without the rule firing.

## Action flags (priority order)

1. **[Mandate, urgent — new this run] BMNR business-activity flag** — ratio
   pre-check on the current Yahoo classification ("Capital Markets") doesn't
   match the recorded broker-app screen from five weeks ago, before this
   position even existed in the book. Get a real Zoya/Musaffa screen on
   BMNR's *current* treasury/staking business model specifically, not a
   general company lookup. This is a policy question, independent of the
   +17.3% return.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Vol throttle / BMNR] ATR 6.57%** — above the 6% throttle threshold;
   this is a high-volatility position (ETH-linked, ATM-funded treasury
   company) — size any addition down accordingly, independent of the
   compliance question above.
4. **[DCF / NOW] Price now ~3.2% above intrinsic value** ($124.11 vs.
   $120.12 on the recorded growth/discount assumptions) — a small, second
   data point (alongside the rich P/E) against adding here, not a sell signal.
5. **[Concentration, informal] NOW is 82.8% of a 2-name book** — the formal
   rule is muted below 4 names, but this is worth a conscious decision
   (add a name, trim NOW, or accept the concentration) rather than a default.
6. **[Catalyst / NOW] Next earnings: Q3 FY2026, 2026-10-28 — 77 days out.**
   Q2 (reported 2026-07-22) beat: revenue $3.99B (+24% YoY), subscription
   revenue $3.877B (+24.5% YoY) — growth *accelerated* versus the ~21-22%
   guided into that print, and versus last cycle's flagged Middle-East
   deal-delay headwind. [StockTitan](https://www.stocktitan.net/sec-filings/NOW/10-q-service-now-inc-quarterly-earnings-report-d7f5db0cedb3.html)
7. **[New leads this run] Only 4 of 50 discovered leads clear the
   catalyst-within-60-days gate as LEAD** (rest are RESEARCH — most earnings
   dates rolled forward into Oct/Nov since the last cycle): **BBY** (earnings
   2026-08-27, 15d), **GWRE** (2026-09-03, 22d), **ZS** (2026-09-03, 22d,
   existing card), **CIEN** (2026-09-03, 22d). All Shariah UNVERIFIED by
   construction — screen before treating any as more than a LEAD.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.

**Case to keep:** BMNR is now the world's largest Ethereum treasury,
holding 5,805,238 ETH (~4.8% of ETH supply, approaching its stated "Alchemy
of 5%" target) plus 209 BTC and a $180M Beast Industries stake — total
crypto+cash disclosed at $11.6B as of 2026-08-09. It stakes essentially all
of that ETH (5,067,309 ETH staked, ~$9.8B) through its own MAVAN validator
platform, projecting ~$294M in annualized staking rewards, and MAVAN is
being extended to institutional custodians as a second revenue line beyond
simple treasury appreciation.
[The Block](https://www.theblock.co/treasuries/bmnr) ·
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)

**Case to trim/hold off adding:** Two independent concerns, neither price-driven.
(1) **Compliance** — see the flag above; recorded compliant, but the ratio
pre-check now raises a business-activity question that predates this
holding's screen. (2) **Dilution/volatility** — funded by a very large
($24.5B) ATM equity program; bulls read this as pure ETH-buying firepower,
skeptics flag that aggressive issuance dilutes existing holders if ETH
appreciation doesn't outpace the growing share count. ATR of 6.57% (above
the vol-throttle threshold) and -18.3% six-month momentum (skip last month)
both reflect a genuinely high-volatility, sentiment-driven name — separate
from, and compounding, the compliance question.
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_10/)

**Verdict: HOLD** by the mechanical engine (no SELL/TRIM rule fired; recorded
compliance still PASS). **Your call:** whether the ratio-precheck flag alone
is reason enough to re-screen before doing anything else with this position,
given it's a policy question independent of the strong return so far.

### NOW — ServiceNow, Inc.

**Case to keep:** Q2 FY2026 (reported 2026-07-22) beat guidance on both
lines — total revenue $3.99B (+24% YoY) and subscription revenue $3.877B
(+24.5% YoY) — driven by AI and cybersecurity momentum, with the Armis
($7.8B, closed April 2026) and Veza acquisitions both folded in during the
quarter. This directly answers last cycle's watch-item (the ~75bp
Middle-East deal-delay headwind flagged ahead of the print): growth held up
and then some. DCF still shows the price within ~3% of intrinsic value on
the recorded assumptions (18% 5y growth, 10% discount rate) — not a
screaming discount, but not obviously overpriced either, despite the rich
P/E multiple. [StockTitan 10-Q](https://www.stocktitan.net/sec-filings/NOW/10-q-service-now-inc-quarterly-earnings-report-d7f5db0cedb3.html) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenows-q2-2026-earnings-expect-121215371.html)

**Case to trim/hold off adding:** VALUATION_RICH still holds (P/E ~119 vs.
the 50 threshold) — growth has to keep delivering at this multiple. DCF
flipped from +6.9% upside last cycle to -3.2% this cycle purely on price
appreciation (model assumptions unchanged) — the margin of safety a value
discipline would want has narrowed, not widened, even with the strong print.
`conviction` and `variant_view` are still blank in the holding's own
front-matter five weeks on — the mechanical LOW-conviction read is a
reflection of that gap, not an independent judgment.

**Verdict: HOLD** (RULE: VALUATION_RICH — do not add at this multiple).
Price is comfortably above its trailing stop (12.0% clear) and thesis
markers (growth rate, Armis integration) are tracking as expected; next
catalyst is 77 days out (2026-10-28).

## Suggested actions (from YOUR rules)

Reading `rules.md` against today's data:
- **Rule VALUATION_RICH fired → NOW: HOLD, do not add.** P/E 119.02 ≥
  `pe_rich` (50). No other Stage-3/4 rule fired on either holding (no
  HARD_STOP, TRAIL_STOP, MOMENTUM_STOP, EMA_BREAK, THESIS_BREAK, or
  TARGET_REACHED — both positions sit clear of their trailing stops).
- **Vol-throttle note fired (not a formal Stage-3/4 rule, but a portfolio
  note) → BMNR** ATR 6.57% ≥ `vol_throttle_atr_pct` (6%) — de-risk sizing
  note, informational.
- **COMPLIANCE_SCREEN did not mechanically fire on BMNR** because the
  recorded status is `compliant`, not `unknown`/`doubtful` — the ratio
  pre-check flag above is a heads-up outside the automated rule, and is the
  one item on this list that genuinely needs your action, not just
  awareness.

If you execute anything based on this assessment, run `/apply-trade` so
holdings + the ledger update.

## DCF

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions (5y growth / terminal / discount) |
|---|---|---|---|---|
| BMNR | $0.72 | $18.10 | -96.0% (not meaningful — see caveat above) | 5% / 2.5% / 10% |
| NOW | $120.12 | $124.11 | -3.2% | 18% / 3% / 10% |

## New ideas — discovery pool (50 leads, top by max-benefit rank)

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`**. Composition turned over substantially in four weeks — 25 of
today's 50 leads are new since 2026-07-13 (mostly semiconductor-equipment,
gold/silver miners, and energy names cycling in; TSLA, GOOGL, MSFT, JNJ,
LLY, DUOL, FICO and others cycled out as their earnings-catalyst windows
closed or moved beyond the 60-day gate). `scaffold.py --all-leads`
auto-filled 25 fresh DRAFT `setups/<ticker>.md` cards this run (25 existing
cards left unchanged). **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.** None can reach
BUY-CANDIDATE until you review the card, edit anything you disagree with,
set `status: planned`, and screen the name compliant in Zoya/Musaffa.

Only 4 of 50 clear the catalyst-within-60-days gate as **LEAD**; the other
46 are **RESEARCH**, almost entirely because their next earnings print now
falls beyond the 60-day window (a symptom of the four-week gap since the
last run, not a change in the underlying names).

| Ticker | Verdict | Card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| BBY | LEAD | new | 5.8:1 | earnings 2026-08-27 | 15 |
| GWRE | LEAD | new | 4.1:1 | earnings 2026-09-03 | 22 |
| ZS | LEAD | existing | 4.3:1 | earnings 2026-09-03 | 22 |
| CIEN | LEAD | new | 3.1:1 | earnings 2026-09-03 | 22 |
| DDS | RESEARCH | new | 1.2:1 | earnings 2026-08-13 | 1 |
| DLO | RESEARCH | new | n/a* | earnings 2026-08-13 | 1 |
| FN | RESEARCH | new | 1.5:1 | earnings 2026-08-17 | 5 |
| KEYS | RESEARCH | new | 0.6:1 | earnings 2026-08-18 | 6 |
| ADI | RESEARCH | existing | 2.5:1 | earnings 2026-08-19 | 7 |
| NVDA | RESEARCH | new | 0.6:1 | earnings 2026-08-26 | 14 |
| P | RESEARCH | new | 0.2:1 | earnings 2026-08-26 | 14 |
| CRDO | RESEARCH | existing | 0.6:1 | earnings 2026-09-01 | 20 |
| AVGO | RESEARCH | new | 2.2:1 | earnings 2026-09-02 | 21 |
| DELL | RESEARCH | new | 0.2:1 | earnings 2026-09-03 | 22 |
| MU | RESEARCH | existing | 2.2:1 | earnings 2026-09-23 | 42 |
| SNX | RESEARCH | new | 2.4:1 | earnings 2026-09-24 | 43 |
| AA | RESEARCH | new | 8.2:1 | earnings 2026-10-15 | 64 |
| VICR | RESEARCH | new | 14.8:1 | earnings 2026-10-20 | 69 |
| LRCX | RESEARCH | new | 2.7:1 | earnings 2026-10-21 | 70 |
| CORZ | RESEARCH | new | 4.8:1 | earnings 2026-10-23 | 72 |
| AMKR | RESEARCH | new | 15.3:1 | earnings 2026-10-26 | 75 |
| CLS | RESEARCH | new | 3.6:1 | earnings 2026-10-26 | 75 |
| RCL | RESEARCH | existing | 9.6:1 | earnings 2026-10-27 | 76 |
| UTHR | RESEARCH | new | 6.8:1 | earnings 2026-10-28 | 77 |
| AR | RESEARCH | existing | 3.2:1 | earnings 2026-10-28 | 77 |
| CDE | RESEARCH | existing | 3.3:1 | earnings 2026-10-28 | 77 |
| AEM | RESEARCH | new | 3.9:1 | earnings 2026-10-28 | 77 |
| AGI | RESEARCH | new | 4.3:1 | earnings 2026-10-28 | 77 |
| SIMO | RESEARCH | existing | 8.0:1 | earnings 2026-10-29 | 78 |
| FOX | RESEARCH | new | 5.0:1 | earnings 2026-10-29 | 78 |
| ARW | RESEARCH | new | 4.2:1 | earnings 2026-10-29 | 78 |
| XOM | RESEARCH | new | 1.8:1 | earnings 2026-10-30 | 79 |
| PAY | RESEARCH | existing | 4.6:1 | earnings 2026-11-02 | 82 |
| PLTR | RESEARCH | existing | 2.0:1 | earnings 2026-11-02 | 82 |
| ALAB | RESEARCH | existing | 4.4:1 | earnings 2026-11-03 | 83 |
| SMCI | RESEARCH | new | 3.2:1 | earnings 2026-11-03 | 83 |
| AMD | RESEARCH | existing | 4.0:1 | earnings 2026-11-03 | 83 |
| FLYW | RESEARCH | new | 3.1:1 | earnings 2026-11-03 | 83 |
| IAG | RESEARCH | new | 4.3:1 | earnings 2026-11-03 | 83 |
| CF | RESEARCH | existing | 10.2:1 | earnings 2026-11-04 | 84 |
| MKSI | RESEARCH | new | 11.4:1 | earnings 2026-11-04 | 84 |
| IONQ | RESEARCH | new | 3.4:1 | earnings 2026-11-04 | 84 |
| APA | RESEARCH | new | 1.6:1 | earnings 2026-11-04 | 84 |
| TTMI | RESEARCH | new | 3.2:1 | earnings 2026-11-04 | 84 |
| DOCN | RESEARCH | new | 2.2:1 | earnings 2026-11-04 | 84 |
| WDC | RESEARCH | new | 13.8:1 | earnings 2026-11-05 | 85 |
| AU | RESEARCH | existing | 3.2:1 | earnings 2026-11-05 | 85 |
| ASTS | RESEARCH | new | 3.6:1 | earnings 2026-11-09 | 89 |
| KGC | RESEARCH | new | 4.2:1 | earnings 2026-11-10 | 90 |
| KLIC | RESEARCH | existing | 10.7:1 | earnings 2026-11-18 | 98 |

*DLO's card shows a stop ($14.14) essentially at/above its entry ($14.12) —
a formula-output anomaly worth a sanity check before treating the card as
usable, not a real 14x reward:risk edge case.

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, CDE — carried over from prior runs.** Government/defense
  business-activity question for PLTR; mining/royalty financing-structure
  questions for the precious-metals names. Nothing new to add — still open.
- **New gold/silver-miner cluster this run (AEM, AGI, KGC, IAG, plus
  carried-over AU/CDE)** — six precious-metals names now in the pool from
  the `undervalued_large_caps` screen. If more than one is ever promoted
  past LEAD, size the cluster as one correlated bet (same logic as the
  TSM/AMD/QCOM/NVDA semiconductor note in `watchlist.md`), not as
  independent positions.
- **DELL / P / KEYS / NVDA / CRDO / FN — reward:risk well under 1:1** (as
  low as 0.2:1) despite decent composite scores — a reminder the composite
  score (momentum/trend/RSI/volume/vol) and the asymmetry gate are
  independent checks; a high score does not imply a tradeable skew.

## Draft & planned setups

66 DRAFT cards now exist in `setups/`, **zero are `planned` or `live`** — no
name in this workspace has cleared the owner-review step yet. This run
added 25 fresh DRAFT cards (AA, AEM, AGI, AMKR, APA, ARW, ASTS, AVGO, BBY,
CIEN, CLS, CORZ, DDS, DELL, DLO, DOCN, FLYW, FN, FOX, GWRE, IAG, IONQ, KEYS,
KGC, LRCX, MKSI, SMCI, SNX, TTMI, UTHR, VICR, WDC, XOM — some of which
overlap with dropped-then-returned tickers) for leads that didn't already
have one; the other 41 (including every BMNR/NOW-adjacent name, and the
carried-over PLTR/AU/CDE/SIMO/ZS/etc.) are untouched from prior runs. Given
the volume, full per-card detail isn't reproduced here — review at your own
pace via the leads table above, prioritizing the 4 LEAD names (BBY, GWRE,
ZS, CIEN) if you want to look at anything before their catalyst windows
close.

## Follow-ups (priority order)

1. **[Urgent, new] BMNR compliance re-screen** — ratio pre-check flags
   "Capital Markets" business-activity concern that predates this position;
   get the Zoya/Musaffa screen done on the current ETH-treasury/staking
   model specifically. This is the single most important open item.
2. **[Ongoing] BMNR sizing/volatility** — ATR 6.57% (above vol-throttle
   threshold) and a very large ($24.5B) ATM program behind it; independent
   of the compliance question, this is a high-volatility position by design.
3. **[Housekeeping] NOW's own front-matter is still incomplete** —
   `conviction`, `variant_view`, `initial_stop`, `target_price`,
   `target_method`, `invalidation`, and `pre_mortem` are all still `null`
   five weeks on. This caps `recommend.py`'s conviction read at LOW by
   construction — filling these in (or explicitly deciding not to) would
   make the mechanical record match your actual thinking.
4. **[Time-boxed] 4 LEADs with near-term catalysts** — BBY (15d), GWRE/
   ZS/CIEN (22d each). Worth a look before their earnings windows close if
   any interest you; all Shariah UNVERIFIED.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.
   This is now three consecutive runs with the same open item.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [BMNR Stock Trades Sideways As Financials Signal High-Risk Setup — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_08_10/)
- [ServiceNow (NYSE: NOW) posts $3.99B Q2 sales, closes Armis and Veza deals — StockTitan](https://www.stocktitan.net/sec-filings/NOW/10-q-service-now-inc-quarterly-earnings-report-d7f5db0cedb3.html)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenows-q2-2026-earnings-expect-121215371.html)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
