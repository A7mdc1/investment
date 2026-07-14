# Portfolio Assessment — 2026-07-14

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank — widened
from 20 last run) → `scaffold.py --all-leads` (39 new DRAFT setup cards
auto-filled for leads without one; 11 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` not run
separately — still 0 closed trades (no `transactions.csv` yet — discipline
guard stays dormant until you start logging via `/apply-trade`).

Since last run (2026-07-13): **FIG was sold and BMNR was bought** (per the
prior commit closing the 7-run FIG compliance flag). The book is down to two
names again, and both are new open questions rather than continuations of
last week's story.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT, no verdict.py rule fired). Live price
**$15.89**, up **+3.0%** vs. the $15.43 cost basis (screened 2026-07-07).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -11.3:1 (DCF target sits far below price; see caveat below) |
| Shariah | Broker app: PASS (compliant, screened 2026-07-07, not stale). **Mechanical ratio pre-check: FAILS** — industry classified `Capital Markets`, which the business-activity screen flags as a core-business fail (see Action flag #1) |
| DCF intrinsic value | $0.76 vs. $15.89 price -> -95.2% — **not a meaningful signal here, see caveat** |
| Trailing stop (chandelier) | $14.542 — price ~9.3% above it |
| 6m momentum (skip last month) | -45.0% |
| Portfolio note | ATR 6.88% — vol-throttle note (size down) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW, and the fresh business-activity flag below should be resolved before treating this as more than "screened once" |
| What changes verdict | Business-activity flag confirmed/cleared in Zoya/Musaffa; thesis_broken trigger; a SELL technical trigger |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$107.07**, **-6.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 1.3:1 (right at the compressed floor; recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $107.07 price -> **+12.5% upside** to the model |
| Trailing stop (chandelier) | $96.90 — price is $10.17 above it |
| 6m momentum (skip last month) | -27.3% (worse than last run's -27.5%... roughly flat, still deeply negative) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.89 | 10 | $15.43 | $158.90 | +3.0% | 17.5% |
| NOW | $107.07 | 7 | $114.97 | $749.49 | -6.9% | 82.5% |

**Total value: $908.39** | Cost: $959.09 | **Total return: ~-5.3%** (-$50.70 unrealised)

The book is smaller and far more concentrated than last run: selling FIG
(51% of the prior book) and buying only a small BMNR position left NOW at
82.5% of invested equity — a concentration level the muted rule (< 4 names)
doesn't currently flag, but is worth noting on its own. NOW continued to
drift down since 2026-07-13 (-6.9% vs. cost, vs. -2.0% last run); BMNR is a
brand-new position, up modestly since the 2026-07-07 entry.

## Action flags (priority order)

1. **[Mandate] BMNR — mechanical Shariah ratio pre-check FAILS on business
   activity.** The broker app recorded BMNR compliant on 2026-07-07 (the
   entry date), but today's automated pre-check flags its Yahoo industry
   classification as `Capital Markets`, which the business-activity screen
   treats as a core-business fail — the same category (conventional
   financial services) that a Shariah screen typically knocks out. BMNR's
   public story is an Ethereum-treasury/staking strategy (see per-holding
   read below) — worth confirming directly whether Zoya/Musaffa's actual
   business-activity screen agrees with the broker app's compliant flag or
   with today's ratio pre-check, since the company's business model has
   shifted materially toward treasury/asset-management activity. This is a
   fresh, unresolved flag on a live holding, not a repeat.
2. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
3. **[Methodology caveat / BMNR DCF] The -95.2% DCF read is not a usable
   signal.** `dcf.py` prices BMNR off *operating* free cash flow (a
   standard 2-stage FCF model) — but BMNR's public value proposition is now
   an ~$11.3B Ethereum + cash treasury (per 2026-07-12 disclosures), not
   its historical operating business. A FCF-based DCF ignores the balance-
   sheet crypto holdings entirely, so $0.76/share understates whatever the
   real economic picture is. Don't read -95% as "overvalued" — it's a model
   mismatch, not a fundamental verdict. No holding-level model here
   currently captures BMNR's actual thesis (ETH accumulation/staking yield).
4. **[Catalyst / NOW] Q2 FY2026 earnings confirmed for 2026-07-22 — 8 days
   out.** ServiceNow set the date via a 2026-07-01 press release; consensus
   EPS ~$0.76 (down slightly y/y). Catalysts into the print: the AI-security
   joint offering with Accenture, and fresh sell-side target increases
   (Oppenheimer reiterated Outperform; Benchmark raised its target to $130).
   [TradersUnion](https://tradersunion.com/news/financial-news/show/2665402-servicenow-gains-3-18percent-to-usd111-14/) ·
   [BusinessWire](https://www.businesswire.com/news/home/20260701382890/en/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22)
5. **[New leads this run — discovery pool widened to 50]** `discover_top_n`
   moved from 20 to 50 (rules.md change since last run), surfacing 30 names
   not seen last week (LLY, ESE, DELL, AAPL, AVGO, P, STX, FLYW, DINO, CIEN,
   WDC, GWRE, NVDA, ARW, TTMI, APH, PSX, BKR, DLO, PDFS, AMKR, TS, CLS,
   FSLR, AA, ADI, KLIC, MU, AMD, CF). All UNVERIFIED Shariah (ratio
   pre-check only) — see the full table below.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep (fundamental, NOT the compliance question):** BMNR has scaled
an aggressive Ethereum-treasury strategy — ETH holdings reached 5.77M tokens
and total crypto + cash holdings of $11.3B as of 2026-07-12 (4.8% of ETH's
total 120.7M-token supply, 95% of the way to a stated "5% of supply"
target in 12 months), staking ~4.92M ETH for a projected ~$284M annualized
staking yield. The stock was added to the Russell 1000 on 2026-06-26, closed
a $273.8M preferred-stock raise on 2026-06-10, and is attempting a bounce
(+10%+ over recent sessions) off a year-long downtrend.
[PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html) ·
[FXLeaders](https://www.fxleaders.com/news/2026/07/14/bmnr-stock-attempts-bullish-reversal-as-bitmine-moves-closer-to-controlling-5-of-eth-supply/)

**Case to flag (compliance, independent of the fundamental story above):**
the mechanical ratio pre-check fails BMNR on business activity — Yahoo
classifies it under `Capital Markets`, which reads as a conventional
financial-services core business, exactly the category Islamic screens
typically knock out. The broker app's compliant flag predates (or is
contemporaneous with) the company's full pivot into a treasury/staking
strategy; worth a direct re-check in Zoya/Musaffa given how much the
business model has shifted in the weeks around the screen date. This is not
a "SELL" call from the engine (broker app still says compliant, so
`shariah.py`'s recorded-status gate doesn't fire it) — it's a fresh
discrepancy between two data sources on a brand-new position, worth
resolving now rather than after it compounds like the prior FIG situation.

**No hard SELL/TRIM trigger today:** price ($15.89) sits above the chandelier
trailing stop ($14.54); no `thesis_broken` or `invalidation` set (the
holding's thesis field is still just a placeholder — "screen compliance
before adding more" — nothing else filled in yet).

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (8 days out,
confirmed by a 2026-07-01 press release); DCF shows +12.5% upside to
intrinsic value ($120.42) at recorded assumptions; sell-side coverage has
gotten incrementally more bullish since last run — Oppenheimer reiterated
Outperform, and Benchmark's Yi Fu Lee raised his target from $125 to $130
— both ahead of the print. The AI-powered cybersecurity joint offering with
Accenture continues to extend the enterprise-security narrative.
[TradersUnion](https://tradersunion.com/news/financial-news/show/2665402-servicenow-gains-3-18percent-to-usd111-14/) ·
[BusinessWire](https://www.businesswire.com/news/home/20260701382890/en/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22)

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; 6m momentum
-27.3% (essentially unchanged from last run's -27.5%, still deeply negative);
reward:risk has compressed to 1.32:1 — right at the `reward_risk_compressed`
floor (1.3) that would fire a TRIM rule if it ticks down further; consensus
EPS of $0.76 for the print is a *decline* y/y, so the growth story needs the
subscription/billings numbers (not EPS) to carry the print.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **No rule fired -> BMNR**: default HOLD; the business-activity flag above
  is not a `verdict.py`/`shariah.py` hard gate (broker app still says
  compliant), but it's the kind of thing worth resolving before it becomes
  a multi-run open flag the way FIG's did.
- **REWARD_RISK_COMPRESSED not firing -> NOW**: 1.32:1 vs. the 1.3 floor —
  worth watching; a small further compression would trigger TRIM.
- **VOL_THROTTLE note -> BMNR**: ATR 6.88% — size down per policy if adding.
- **DRAWDOWN_REVIEW not firing**: neither position is down >= the 20% threshold.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.76 | $15.89 | -95.2% | growth_5y 5%, terminal 2.5%, discount 10% — **caveat: FCF-based model doesn't capture BMNR's crypto-treasury asset value, see Action flag #3** |
| NOW | $120.42 | $107.07 | +12.5% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run — expected, since no card has
been reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 50 leads (pool widened from 20), 39 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (now top 50 by max-benefit rank — `discover_top_n` was raised
from 20 to 50 in `rules.md` since last run). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead that didn't
already have one (11 cards carried over unchanged: FICO, ALKT, LIF, JNJ,
ULTA, TSLA, CVE, MSFT, KLIC, GOOGL, PLTR, ADI, DUOL, MT, VRNS, SIMO, PAY,
CRDO, GDDY, AMD, CF, CNQ, ALAB — already existed; 39 new DRAFT cards
written: LLY, ESE, DELL, AAPL, AVGO, P, STX, FLYW, DINO, CIEN, WDC, GWRE,
NVDA, ARW, TTMI, APH, PSX, BKR, DLO, PDFS, AMKR, TS, CLS, FSLR, AA).
**Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to
review and edit, never buys.** None can reach BUY-CANDIDATE until you
review the card, edit anything you disagree with, set `status: planned`,
and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Reward:risk | Catalyst | Days out |
|---|---|---|---|---|
| FICO | LEAD | 20.0:1 | earnings 2026-07-29 | 15 |
| ALKT | LEAD | 18.7:1 | earnings 2026-07-29 | 15 |
| LIF | LEAD | 8.0:1 | earnings 2026-08-10 | 27 |
| JNJ | LEAD | 5.4:1 | earnings 2026-07-15 | 1 |
| ULTA | LEAD | 9.7:1 | earnings 2026-08-27 | 44 |
| TSLA | LEAD | 6.1:1 | earnings 2026-07-22 | 8 |
| CVE | LEAD | 4.3:1 | earnings 2026-07-30 | 16 |
| MSFT | LEAD | 5.3:1 | earnings 2026-07-29 | 15 |
| KLIC | LEAD | 5.5:1 | earnings 2026-08-06 | 23 |
| LLY | LEAD (new card) | 4.9:1 | earnings 2026-08-05 | 22 |
| ESE | LEAD (new card) | 5.8:1 | earnings 2026-08-10 | 27 |
| MU | RESEARCH | 5.7:1 | earnings 2026-09-23 | 71 |
| GOOGL | LEAD | 3.8:1 | earnings 2026-07-22 | 8 |
| PLTR | LEAD | 4.5:1 | earnings 2026-08-03 | 20 |
| ADI | LEAD | 5.7:1 | earnings 2026-08-19 | 36 |
| DUOL | LEAD | 4.4:1 | earnings 2026-08-05 | 22 |
| MT | RESEARCH | 2.4:1 | earnings 2026-07-30 | 16 |
| VRNS | RESEARCH | 2.0:1 | earnings 2026-07-28 | 14 |
| SIMO | RESEARCH | 1.1:1 | earnings 2026-07-29 | 15 |
| PAY | LEAD | 4.0:1 | earnings 2026-08-03 | 20 |
| CRDO | LEAD | 5.2:1 | earnings 2026-09-02 | 50 |
| GDDY | LEAD | 3.3:1 | earnings 2026-07-30 | 16 |
| AMD | RESEARCH | 0.4:1 | earnings 2026-08-04 | 21 |
| DELL | RESEARCH (new card) | 0.1:1 | earnings 2026-09-03 | 51 |
| CF | RESEARCH | 2.3:1 | earnings 2026-08-05 | 22 |
| AAPL | RESEARCH (new card) | 0.6:1 | earnings 2026-07-30 | 16 |
| AVGO | LEAD (new card) | 3.6:1 | earnings 2026-09-03 | 51 |
| ZS | LEAD | 3.7:1 | earnings 2026-09-02 | 50 |
| P | LEAD (new card) | 3.0:1 | earnings 2026-08-26 | 43 |
| STX | RESEARCH (new card) | n/a | earnings 2026-07-28 | 14 |
| FLYW | RESEARCH (new card) | 1.2:1 | earnings 2026-08-04 | 21 |
| DINO | RESEARCH (new card) | 0.1:1 | earnings 2026-07-28 | 14 |
| ALAB | RESEARCH | n/a | earnings 2026-08-04 | 21 |
| CIEN | LEAD (new card) | 3.8:1 | earnings 2026-09-09 | 57 |
| WDC | RESEARCH (new card) | n/a | earnings 2026-07-29 | 15 |
| GWRE | LEAD (new card) | 3.8:1 | earnings 2026-09-03 | 51 |
| NVDA | RESEARCH (new card) | 1.4:1 | earnings 2026-08-26 | 43 |
| ARW | RESEARCH (new card) | n/a | earnings 2026-07-30 | 16 |
| CNQ | RESEARCH | n/a | earnings 2026-08-06 | 23 |
| TTMI | RESEARCH (new card) | n/a | earnings 2026-07-29 | 15 |
| APH | RESEARCH (new card) | n/a | earnings 2026-07-29 | 15 |
| PSX | RESEARCH (new card) | 0.0:1 | earnings 2026-08-05 | 22 |
| BKR | RESEARCH (new card) | n/a | earnings 2026-07-26 | 12 |
| DLO | RESEARCH (new card) | 1.0:1 | earnings 2026-08-13 | 30 |
| PDFS | RESEARCH (new card) | n/a | earnings 2026-08-06 | 23 |
| AMKR | RESEARCH (new card) | n/a | earnings 2026-07-27 | 13 |
| TS | RESEARCH (new card) | n/a | earnings 2026-08-05 | 22 |
| CLS | RESEARCH (new card) | n/a | earnings 2026-07-27 | 13 |
| FSLR | RESEARCH (new card) | n/a | earnings 2026-07-30 | 16 |
| AA | RESEARCH (new card) | n/a | earnings 2026-07-16 | 2 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR, MT, CNQ, ALAB** — carried over from prior runs' flags (government/
  defense business-activity question for PLTR; implausibly tight engineered
  entry/stop/target bands on MT/CNQ; ALAB has no computable reward:risk).
  Nothing new to add — still open, still worth checking before spending
  review time on the cards.
- **TSLA / GOOGL / MSFT (SPUS holdings, carried over)** — mega-caps with
  generally clean debt/liquidity ratios on the pre-check, but each carries
  its own business-activity nuance worth a real Zoya/Musaffa screen rather
  than assuming "SPUS holds it, so it's fine."
- **JNJ (1 day to catalyst) / AA (2 days)** — both have earnings essentially
  immediately; JNJ is capped at LEAD/RESEARCH-adjacent by the numbers above,
  AA shows no computable reward:risk. Not actionable timelines for a review
  you'd do carefully.
- **Several new cards show `n/a` or sub-1:1 reward:risk** (STX, ALAB, WDC,
  ARW, CNQ, TTMI, APH, BKR, PDFS, AMKR, TS, CLS, FSLR, AA, DELL, AAPL, PSX,
  DINO, AMD) — the discovery pool widening to 50 pulled in more marginal
  setups than before; these fail the asymmetry gate as designed and stay at
  RESEARCH, not LEAD.

## Follow-ups (priority order)

1. **[New — fresh flag] BMNR business-activity check**: confirm in
   Zoya/Musaffa whether the `Capital Markets` classification the mechanical
   pre-check surfaced today reflects a real compliance concern given BMNR's
   pivot to an ETH-treasury/staking strategy, or whether the broker app's
   2026-07-07 compliant screen already accounts for that. Resolve before
   this becomes a multi-run open question the way FIG's flag did.
2. **[Time-boxed] NOW earnings 2026-07-22** — 8 days out; reward:risk is
   right at the compression floor (1.32:1 vs. 1.3), worth checking again
   after the print.
3. **[Housekeeping] 39 new DRAFT setup cards** added this run (50 total
   leads in `leads.md`, most now with cards in `setups/`); none are
   `planned`, none can reach BUY-CANDIDATE. Review at your own pace.
4. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.
5. **[Policy note]** `discover_top_n` moved 20 -> 50 in `rules.md`; if that
   was intentional, no action — if it was accidental, worth a look, since it
   materially changes the size of the review queue each run.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [BMNR Stock Attempts Bullish Reversal as Bitmine Moves Closer to Controlling 5% of ETH Supply — FXLeaders](https://www.fxleaders.com/news/2026/07/14/bmnr-stock-attempts-bullish-reversal-as-bitmine-moves-closer-to-controlling-5-of-eth-supply/)
- [BMNR Stock Climbs As Massive Ethereum Bet Takes Shape — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_06/)
- [ServiceNow stock holds near $105.65-$116.63 range as upcoming Q2 earnings release approaches — TradersUnion](https://tradersunion.com/news/financial-news/show/2665402-servicenow-gains-3-18percent-to-usd111-14/)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — BusinessWire](https://www.businesswire.com/news/home/20260701382890/en/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22)
