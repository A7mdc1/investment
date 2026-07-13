# Portfolio Assessment — 2026-07-13 (post-trade re-run)

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

**This supersedes the earlier 2026-07-13 report.** Between the two runs you
executed a trade: sold all 35 FIG shares @ $23.00 (realized P/L +$54.95,
discretionary/compliance exit — closes the FIG mandate flag that had been
unresolved for 7 consecutive runs) and opened a new 10-share BMNR position @
$15.43 avg cost. This run reflects the portfolio as it stands now: **NOW +
BMNR**.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 by max-benefit rank — widened from 20
this run, now also rendering entry/target/stop per lead) → `scaffold.py
--all-leads` (30 new DRAFT setup cards auto-filled for the wider pool; 20
existing cards unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps.

## Verdicts (lead with this)

**FIG — closed this run.** No longer a holding; see the trade note above.
Realized P/L +$54.95 on the compliance exit, logged to `journal.csv` /
`transactions.csv`.

**BMNR -> HOLD** (no rule fired — this is a brand-new position with no
`initial_stop`/`conviction`/`catalyst` recorded yet, so `verdict.py` has
nothing to gate on beyond the default). Live price **$14.45**, **-6.4%**
vs. the $15.43 cost basis, one day or so into the position.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — no reward:risk or stated thesis to self-assess |
| Shariah | broker app: **PASS** (recorded compliant, screened 2026-07-07) — **but see the flag below, this is not clean** |
| DCF intrinsic value | **$0.76** vs. $14.45 price -> **-94.7%** (DCF is a poor fit for a crypto-treasury vehicle — see note) |
| Trailing stop (chandelier) | $14.6545 — price is **already $0.19 below it** |
| 6m momentum (skip last month) | -50.0% |
| Portfolio note | ATR 7.29% — vol-throttle note |
| Would buy today? | Mechanically yes per recommend.py (no gate blocks a `core` position with no thesis on file); conviction LOW |
| What changes verdict | thesis_broken flag, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$111.69**, **-2.9%** vs. $114.97 cost basis. Now **84.4%** of the
book (was 49% before the FIG close), since it's your only other holding.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.6:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $111.69 price -> **+7.8% upside** to the model |
| Trailing stop (chandelier) | $97.3885 — price ~13.1% above it |
| 6m momentum (skip last month) | -27.5% |
| Would buy today? | Mechanically yes; conviction still LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $14.45 | 10 | $15.43 | $144.45 | -6.4% | 15.6% |
| NOW | $111.60 | 7 | $114.97 | $781.20 | -2.9% | 84.4% |

**Total value: $925.65** (down from $1,610.49 pre-trade — the FIG proceeds
weren't reinvested in full: BMNR is a $154.35 position vs. FIG's $821.45
value, so ~$666 of that came out of the market entirely, likely sitting as
uninvested cash from the sale minus the BMNR purchase — worth confirming
against your actual cash balance since `prices.py` only sums invested
positions, not cash on hand.)

## Action flags (priority order)

1. **[Mandate — new, worth acting on before this grows] BMNR Shariah
   business-activity conflict.** The broker app shows BMNR compliant
   (screened 2026-07-07, the badge in your screenshot), but this run's
   mechanical ratio pre-check independently flags it: `industry 'Capital
   Markets' matches 'capital markets' — core business fails screen`.
   That's not a false positive from stale data — it lines up with what BMNR
   actually does now: it's an Ethereum-treasury vehicle holding **5.67M ETH
   (~4.7% of total ETH supply) plus $601M cash/securities**, funded partly
   by a **$273.8M 9.50% Series A Perpetual Preferred Stock (BMNP)** offering
   paying regular weekly cash dividends — a fixed-rate, debt-like
   instrument. [Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_06/)
   A separate Musaffa page rates it Shariah-compliant, but that's dated
   "as of Q3 2025" — **before** this treasury/preferred-stock strategy
   scaled up, so it may not reflect the current business. [Musaffa](https://musaffa.com/stock/BMNR/)
   Recommend a fresh Zoya/Musaffa screen specifically dated after the BMNP
   raise before adding to this position.
2. **[Technical] BMNR price is already below its computed chandelier
   trailing stop** ($14.45 vs. $14.65) one day or so into the position —
   mechanically inert since `trade_type: core` exempts it from
   `verdict.py`'s TRAIL_STOP rule (the same structural gap flagged for NOW
   in prior runs), but worth noting given how fresh the position is.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
4. **[Data quality / BMNR DCF]** The DCF model (5% growth, 10% discount)
   puts "intrinsic value" at $0.76 vs. a $14.45 price — a -94.7% figure
   that's not a meaningful signal here. `dcf.py`'s formula is built for a
   conventional cash-flow business; BMNR's value is now driven by its ETH
   holdings and treasury strategy, which a standard DCF doesn't model.
   Treat this number as noise, not as evidence of overvaluation.
5. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22 — 9 days out.**
   Unchanged from the morning run: ~21-21.5% cc subscription growth guided,
   watch for the ~75bp Middle-East deal-delay headwind on the call.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** added to multiple Russell equity indexes (Russell 1000,
Russell 3000) this cycle; combined crypto/cash/treasury holdings of $10.7B
reported; management continues scaling the ETH-treasury strategy, which is
the entire investment case here — a levered bet on ETH price plus the
treasury premium/discount to NAV that these vehicles trade at.
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_01/)

**Case to exit / reconsider before adding:** the business-activity Shariah
question above is not a technicality — a capital-markets/treasury vehicle
funded in part by a fixed-rate preferred instrument is a materially
different profile than the "compliant" badge suggests if that badge predates
the BMNP raise. No `initial_stop`, `conviction`, `catalyst`, or
`invalidation` is recorded on this holding yet, so there's no written plan
to hold you to if it moves against you — worth writing one now, this early,
rather than after a bigger move either direction.

**No verdict override yet — HOLD by default (no rule fired).** The
Shariah conflict above is the thing to resolve first, independent of price.

### NOW — ServiceNow, Inc.
Unchanged from the morning run: Q2 FY2026 earnings 2026-07-22 (9 days out),
DCF +7.8% upside, P/E ~119 still VALUATION_RICH, 6m momentum -27.5%. Now
84.4% of the book following the FIG close — worth noting concentration has
risen even though the compliance flag is resolved.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE — FIG: resolved.** Sold in full this run; no longer
  carried forward.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW or BMNR**: both within the 20% threshold.
- **TRAIL_STOP -> BMNR**: does NOT fire (`trade_type: core`) even though
  price is already below the computed level — same structural gap as NOW's
  prior open question; worth a deliberate policy call on whether new
  positions should default to a `trade_type` that lets the technical stop
  actually bind.
- **VOL_THROTTLE note -> BMNR**: ATR 7.29% — size down per the vol throttle
  if adding.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.76 | $14.45 | -94.7% | growth_5y 5%, terminal 2.5%, discount 10% — poor model fit, see flag #4 |
| NOW | $120.42 | $111.66 | +7.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md` is still empty. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** this run — no card has been reviewed and flipped to
`status: planned` yet.

## Draft & planned setups — 50 leads this run (widened from 20), 30 fresh DRAFT cards

`discover.py`'s `discover_top_n` was raised 20 -> 50 this run per your
request, and `render_rows()` now prints each lead's discovery-stage
`entry / target / stop` alongside reward:risk. `scaffold.py --all-leads`
filled DRAFT cards for the 30 newly-surfaced names without one: AVGO, P,
DELL, LLY, STX, AAPL, DINO, CIEN, NVDA, FLYW, WDC, ARW, GWRE, PSX, TTMI,
DLO, BKR, BBY, TS, PDFS, APH, FSLR, AA, CLS, AMKR (20 cards from last run —
CNQ, LIF, ALKT, RCL, ZS, MT, PLTR, TSLA, MSFT, CVE, FICO, GOOGL, ULTA, DUOL,
VRNS, SIMO, JNJ, CRDO, GDDY, PAY, plus CF/AMD/ALAB/KLIC/MU — were left
unchanged).

Full 50-name table omitted here for length — see `leads.md` directly for
every ticker's entry/target/stop, reward:risk, score, and catalyst date.
**Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to
review and edit, never buys.** None can reach BUY-CANDIDATE until you
review the card, edit anything you disagree with, set `status: planned`,
and screen the name compliant in Zoya/Musaffa.

**Flags carried over / worth noting:**
- PLTR, AU/CDE-style mining names, MT's tight engineered band — same open
  questions as prior runs, nothing new to add.
- **AVGO, NVDA (new, SPUS holdings)** and **AAPL, LLY (new, SPUS holdings)**
  now have DRAFT cards — standard mega-cap ratio profile, still need a real
  business-activity screen before treating as more than a LEAD.

## Follow-ups (priority order)

1. **[New — urgent, before adding to BMNR] Shariah re-screen BMNR** —
   specifically dated after the BMNP 9.50% preferred-stock raise, not the
   Q3 2025 Musaffa screen the broker badge may be echoing. The mechanical
   ratio pre-check disagrees with the recorded status for a substantive
   reason (business-activity classification), not a data glitch.
2. **[New] Write BMNR's PM record** — `initial_stop`, `target_price`/
   `target_method`, `conviction`, `catalyst`, `thesis_one_liner`,
   `invalidation`, `pre_mortem`. Nothing is recorded yet; happy to fill in
   whatever you tell me, but won't invent these fields.
3. **[Carried over] NOW earnings 2026-07-22** — 9 days out; watch the
   Middle-East deal-delay headwind on the call.
4. **[Housekeeping] Confirm cash balance** — total invested value dropped
   from $1,610 to $926 across this trade; if that gap isn't sitting as cash
   in the brokerage, the numbers here won't reconcile with your actual
   account.
5. **[Housekeeping] 30 new DRAFT setup cards** from the widened 50-name
   pool; none are `planned` yet.
6. **[Infrastructure — still open]** No `journal.py` review run yet on the
   newly-closed FIG trade — worth a look once you have more than one closed
   trade logged, to see realized R and expectancy build up.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Immersion Technologies (BMNR) — Timothy Sykes](https://www.timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_06/)
- [Is Bitmine Immersion Technologies Inc - BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [BMNR Stock Climbs As Ethereum Treasury Strategy Scales Up — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_01/)
- [ServiceNow's Q2 2026 Earnings: What to Expect — Barchart](https://www.barchart.com/story/news/3052357/servicenows-q2-2026-earnings-what-to-expect)
