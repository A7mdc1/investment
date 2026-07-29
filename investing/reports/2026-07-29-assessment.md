# Portfolio Assessment — 2026-07-29

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (25 new DRAFT setup cards auto-filled for leads
without one; 25 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` not run — still 0 closed trades logged
(`transactions.csv` doesn't exist yet; the FIG exit and BMNR buy on
2026-07-13 were recorded directly in the holdings files, not through
`/apply-trade`, so the discipline guard stays dormant).

**16 days since the last run (2026-07-13).** Since then: FIG was sold
(closed, +$54.95 realized) and BMNR opened — this is the first assessment
of the new two-name book.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.01**, up
**+10.2%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -7.6:1 (target is the DCF intrinsic value, which is far below price — see DCF note below; this ratio is not meaningful for this business) |
| Shariah | recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see Action flag #1**: the mechanical ratio pre-check disagrees |
| DCF intrinsic value | **$0.72** vs. $16.99 price — see caveat below; standard earnings-based DCF does not fit a young, crypto-treasury balance sheet |
| Trailing stop (chandelier) | $14.8531 — price is **12.6%** above it |
| 6m momentum (skip last month) | -52.9% (extremely volatile name; short listing history skews this) |
| Portfolio note | ATR 6.8% — vol-throttle note; size down |
| Would buy today? | Mechanically "yes" (gate default) — but no `initial_stop`/`target_price`/`conviction`/`pre_mortem` are filled in yet, so this isn't a real answer |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$116.51**, up **+1.3%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.2:1 (skew too thin for a fresh add) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); ratio pre-check also clean (debt ratio 2%, liquid ratio 5.2%) |
| DCF intrinsic value | **$120.12** vs. $116.51 price -> **+3.1% upside** to the model |
| Trailing stop (chandelier) | $98.3059 — price is **$18.20 above it** |
| 6m momentum (skip last month) | -24.2% |
| Would buy today? | Mechanically yes per the gates; conviction still LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
- BMNR ATR 6.8% — vol-throttle note (size down per rules.md).

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.01 | 10 | $15.43 | $170.10 | +10.2% | 17.3% |
| NOW | $116.51 | 7 | $114.97 | $815.57 | +1.3% | 82.7% |

**Total value: $985.67** | Cost: $959.09 | **Total return: ~+2.8%** (+$26.58 unrealised)

Total tracked value is lower than the pre-sale $1,610.49 (2026-07-13) because
only ~$154 of the ~$805 FIG sale proceeds was redeployed into BMNR — the rest
sits outside what this repo tracks (cash isn't a modeled position here).
NOW is now **82.7% of the book**, well above the 22% `max_position_pct` cap —
but the CONCENTRATION rule is explicitly muted below 4 names
(`min_names_for_concentration: 4`), so no TRIM fires mechanically. Worth
noting anyway: a two-name book with one name at 83% carries real
single-stock risk regardless of what the rule threshold says.

## Action flags (priority order)

1. **[Mandate — new this run] BMNR ratio pre-check disagrees with the
   recorded compliance status.** The broker app recorded BMNR **compliant**
   on 2026-07-07. This repo's own mechanical ratio pre-check flags the
   opposite: yfinance classifies BMNR's sector as "Financial Services" and
   industry as **"Capital Markets"** — a business-activity category this
   screen treats as a hard knockout regardless of financial ratios. BitMine
   is functionally an Ethereum-treasury holding company (buys/holds/stakes
   ETH on its balance sheet, funded via equity raises), which is exactly the
   kind of business a "capital markets" classification is meant to catch.
   **This is a heads-up, not a fatwa** (per convention, Zoya/Musaffa are the
   source of truth) — but the disagreement between the broker's recorded
   screen and this repo's own pre-check on a position you're already +10.2%
   into is worth resolving before it grows further, not after.
2. **[Data hygiene] BMNR's PM decision record is still empty three weeks
   after opening.** No `conviction`, `initial_stop`, `target_price`,
   `invalidation`, or `pre_mortem` set in `holdings/bmnr.md` — `verdict.py`
   can't compute an R-multiple, and `recommend.py`'s reward:risk figure
   (-7.6:1) is an artifact of falling back to the DCF intrinsic value as a
   target, which doesn't fit a crypto-treasury balance sheet. Worth filling
   in your own stop/target so the mechanical checks mean something here.
3. **[Catalyst / NOW — earnings already happened since last run]** Q2 FY2026
   earnings reported **2026-07-22** (beat: EPS $0.90 vs. $0.76 est.;
   subscription revenue +24.5% y/y cc; AI now >$1B annual contract value;
   98% renewal rate) and the stock rallied ~6% same-day on an Accenture
   AI-security joint offering announcement. The holding's `catalyst.date` is
   still `null` and `last_review` still reads 2026-06-15 — rules.md calls
   for a re-underwrite on every earnings print; that hasn't happened yet in
   the file. Next earnings: **2026-10-28** (91 days out — outside the
   60-day catalyst horizon until then). [gurufocus](https://www.gurufocus.com/news/8970231/servicenow-now-set-to-report-q2-earnings-with-strong-growth-expectations) · [timothysykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_07_23/)
4. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH holds. Do not add.
5. **[Discovery pool refreshed]** 12 leads dropped off vs. last run (TSLA,
   GOOGL, JNJ, NVDA, RCL, CRDO, VRNS, DG, DINO, PSX, AA, CIEN — mostly
   earnings dates rolling past or R:R compressing), 12 new (AU, KGC, SMCI,
   NEM, SFD, HST, CRH, UTHR, AR, SNX, ESE, FORM) — several gold/mining names
   (AU, KGC, NEM) newly surfaced from the `undervalued_large_caps` screen.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** Momentum has been strong — stock ran from the mid-$14s to
the high-$17s over the past few weeks (touched $18.01 intraday on
2026-07-27). BitMine holds ~$11.8B in crypto + cash (ETH treasury,
~4.9-5.8M ETH depending on source/date), remains the #1 ETH treasury and
#2 digital-asset treasury globally behind Strategy (MSTR), and has executed
what's reported as the largest-ever common stock buyback among ETH/BTC
treasury vehicles. [stockstotrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_27/) · [prnewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-79-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-8-billion-302834876.html)

**Case to trim/watch:** This is effectively a leveraged bet on the ETH price
via a corporate treasury vehicle — 6m momentum of -52.9% (short listing
history, high volatility) and an ATR of 6.8% flag this as a name to size
carefully, which rules.md's vol-throttle note already does. Independent of
price action: the **Capital Markets industry classification** (Action flag
#1) is a mandate question, not a price call, and hasn't been reconciled with
the broker's recorded compliant status.

**Verdict: HOLD (no technical rule fired).** The open item here isn't price —
it's finishing the compliance reconciliation and filling in the PM record
(stop/target/invalidation) that's been missing since entry.

### NOW — ServiceNow, Inc.
**Case to keep:** Beat-and-raise Q2 print (2026-07-22): subscription revenue
+24.5% y/y cc, non-GAAP operating margin near 30%, RPO growing ~21%, AI ACV
crossed $1B, 98% renewal rate, and a new AI-powered cybersecurity offering
with Accenture. DCF still shows a modest +3.1% upside to intrinsic value at
recorded assumptions. Price is $18.20 above the trailing chandelier stop.
[gurufocus](https://www.gurufocus.com/news/8970231/servicenow-now-set-to-report-q2-earnings-with-strong-growth-expectations) · [seekingalpha](https://seekingalpha.com/news/4127126-servicenow-q2-earnings-preview-improving-customer-activity-levels-and-gen-ai-in-focus)

**Case to trim/watch:** P/E ~119 is still VALUATION_RICH — priced for
continued high growth, so any deceleration hits hard. 6m momentum remains
negative (-24.2%) despite the earnings pop, and the next catalyst (2026-10-28
earnings) is 91 days out, past the 60-day catalyst horizon — a quiet stretch
where the "would I buy this here today?" test matters more than usual.

**Verdict: HOLD (VALUATION_RICH).** Nothing here argues for adding at this
multiple; nothing argues for selling a compliant, in-thesis position either.
The real follow-up is procedural: update `catalyst.date`/`last_review` in
the holding file to reflect the print that already happened.

## Suggested actions (from YOUR rules, rules.md)

- **No hard rule fired on either holding** this run — no COMPLIANCE_GATE,
  HARD_STOP, TRAIL_STOP, MOMENTUM_STOP, or THESIS_BREAK triggered.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DEFAULT (no rule) -> BMNR**: HOLD — but this is a weak signal given how
  much of BMNR's PM record is still unfilled (see Action flag #2); treat it
  as "nothing mechanical fired" rather than "all clear."
- **VOL_THROTTLE note -> BMNR**: ATR 6.8% — size down if adding.
- **DRAWDOWN_REVIEW not firing** on either name (BMNR +10.2%, NOW +1.3% — both well inside the 20% threshold).

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync — that's also what will finally start the
discipline-guard sample (`transactions.csv` is still empty).*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $16.99 | -95.8% | growth_5y 5%, terminal 2.5%, discount 10% |
| NOW | $120.12 | $116.51 | +3.1% | growth_5y 18%, terminal 3%, discount 10% |

**Caveat on BMNR's DCF:** a standard discounted-earnings/cash-flow model is
a poor fit for a young, crypto-treasury balance sheet whose value is
dominated by ETH holdings and equity-raise dynamics, not recurring operating
cash flow. The -95.8% "downside" here is a modeling artifact, not a market
call — don't read it as a price target either way. This also explains why
`recommend.py` shows BMNR's reward:risk as a nonsensical -7.6:1 (it defaults
to the DCF value as `target_price` when none is set in front-matter): fill
in your own `target_price`/`target_method` on the holding to get a
meaningful number.

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet). All new-idea surfacing this cycle
comes from machine discovery below.

## Draft & planned setups — 50 leads, 25 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, widened to a
top-50 pool per the 2026-07-13 change) and wrote **`leads.md`**.
`scaffold.py --all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for
every lead without one (25 new: TS, KGC, SMCI, P, DELL, STX, AVGO, ARW, NEM,
SNX, CLS, GWRE, AAPL, LLY, WDC, DLO, BKR, HST, SFD, FLYW, APH, ESE, BBY,
PDFS, UTHR, FSLR, CRH, TTMI, FORM; 25 existing cards — AU, PLTR, ALKT, LIF,
FICO, MSFT, AR, DUOL, GDDY, CVE, MT, CNQ, CF, SIMO, ZS, PAY, ULTA, ALAB, AMD,
KLIC — left unchanged). **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.** None can reach
BUY-CANDIDATE until you review the card, edit anything you disagree with,
set `status: planned`, and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| DELL | LEAD | new | 5.8:1 | earnings 2026-09-03 | 36 |
| MSFT | LEAD | existing | 4.9:1 | earnings 2026-07-29 | 0 |
| FICO | LEAD | existing | 3.6:1 | earnings 2026-07-29 | 0 |
| AR | LEAD | existing | 4.7:1 | earnings 2026-07-29 | 0 |
| ALKT | LEAD | existing | 6.0:1 | earnings 2026-07-29 | 0 |
| KGC | LEAD | new | 13.5:1 | earnings 2026-07-29 | 0 |
| STX | RESEARCH | new | 9.2:1 | earnings 2026-10-27 | 89 |
| TS | LEAD | new | 10.8:1 | earnings 2026-08-05 | 7 |
| DUOL | LEAD | existing | 3.9:1 | earnings 2026-08-05 | 7 |
| P | LEAD | new | 13.4:1 | earnings 2026-08-26 | 28 |
| AU | LEAD | existing | 20.0:1 | earnings 2026-07-31 | 2 |
| GDDY | LEAD | existing | 3.5:1 | earnings 2026-07-30 | 1 |
| AVGO | LEAD | new | 9.2:1 | earnings 2026-09-03 | 36 |
| SMCI | LEAD | new | 20.0:1 | earnings 2026-08-11 | 13 |
| PLTR | LEAD | existing | 10.2:1 | earnings 2026-08-03 | 5 |
| ARW | LEAD | new | 5.3:1 | earnings 2026-08-06 | 8 |
| LIF | LEAD | existing | 5.4:1 | earnings 2026-08-10 | 12 |
| NEM | RESEARCH | new | 20.0:1 | earnings 2026-10-22 | 84 |
| SNX | LEAD | new | 5.7:1 | earnings 2026-09-24 | 57 |
| CVE | RESEARCH | existing | 1.9:1 | earnings 2026-07-29 | 0 |
| MT | RESEARCH | existing | 1.7:1 | earnings 2026-07-30 | 1 |
| CLS | RESEARCH | new | 7.6:1 | earnings 2026-10-26 | 88 |
| CNQ | RESEARCH | existing | 1.9:1 | earnings 2026-08-06 | 8 |
| CF | RESEARCH | existing | 1.5:1 | earnings 2026-08-05 | 7 |
| SIMO | RESEARCH | existing | n/a | earnings 2026-07-29 | 0 |
| ZS | LEAD | existing | 3.9:1 | earnings 2026-09-02 | 34 |
| GWRE | LEAD | new | 3.5:1 | earnings 2026-09-03 | 35 |
| PAY | RESEARCH | existing | 1.0:1 | earnings 2026-08-03 | 5 |
| AAPL | RESEARCH | new | 0.1:1 | earnings 2026-07-30 | 1 |
| ULTA | LEAD | existing | 3.6:1 | earnings 2026-08-27 | 29 |
| LLY | RESEARCH | new | 0.4:1 | earnings 2026-08-05 | 7 |
| ...and 19 more (mostly RESEARCH-capped or n/a R:R) | | | | | |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **AU, KGC, NEM (new this run, gold miners)** — carry the same
  royalty/streaming-financing-structure question flagged on prior mining
  names; check the specific corporate structure, not just "gold mining is
  fine," before screening.
- **PLTR, MT** — carried-over open questions from earlier runs (PLTR's
  government/defense revenue mix; MT's implausibly tight engineered
  entry/stop/target band from the formula) — nothing new to add.
- **Several catalysts land today (2026-07-29) or within days** — MSFT,
  FICO, AR, ALKT, KGC, CVE, SIMO all show earnings on/around this date;
  R:R and price levels on those cards will be stale within hours if you
  don't review promptly.

## Follow-ups (priority order)

1. **[New, mandate] Resolve the BMNR compliance disagreement** — recorded
   compliant (broker app) vs. this repo's own ratio pre-check flagging
   "Capital Markets" as a knockout business category. Independent
   Zoya/Musaffa re-verification, specifically on the business-activity
   screen (not just the ratios), is the next step.
2. **[Housekeeping] Fill in BMNR's PM record** — `conviction`,
   `initial_stop`, `target_price`/`target_method`, `invalidation`,
   `pre_mortem` are all still `null` three weeks after entry; the mechanical
   reward:risk figure is meaningless until this is done.
3. **[Housekeeping] Update NOW's `catalyst.date` and `last_review`** to
   reflect the 2026-07-22 print (beat) and set the next catalyst to
   2026-10-28 — rules.md calls for a re-underwrite on every earnings print.
4. **[Time-boxed] Several draft cards' catalysts land today/this week**
   (MSFT, FICO, AR, ALKT, KGC, AU, GDDY, DUOL, PLTR, TS — see table) — review
   promptly if any interest you, since the auto-filled entry/stop/target
   levels are formula snapshots that go stale fast around earnings.
5. **[Infrastructure — still open]** No ledger yet — the FIG exit and BMNR
   buy were hand-recorded, not logged via `/apply-trade`. Start logging
   through `/apply-trade` going forward to unlock `journal.py`'s
   expectancy report and the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Trader Focus — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_27/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.79 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-79-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-8-billion-302834876.html)
- [ServiceNow (NOW) Set to Report Q2 Earnings with Strong Growth Expectations — GuruFocus](https://www.gurufocus.com/news/8970231/servicenow-now-set-to-report-q2-earnings-with-strong-growth-expectations)
- [ServiceNow (NOW) Rallies As AI-Fueled Q2 Earnings Crush Expectations — TimothySykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_07_23/)
- [ServiceNow Q2 earnings preview: Improving customer activity levels and Gen AI in focus — SeekingAlpha](https://seekingalpha.com/news/4127126-servicenow-q2-earnings-preview-improving-customer-activity-levels-and-gen-ai-in-focus)
