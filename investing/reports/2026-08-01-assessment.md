# Portfolio Assessment — 2026-08-01

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (24 new DRAFT setup cards auto-filled for names
without one; 38 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run (one transient `$BMNR: possibly delisted` warning from
`recommend.py`'s internal history fetch self-recovered; `prices.py`,
`shariah.py`, and `verdict.py` all pulled BMNR data cleanly, so the figures
below are live, not stale/fabricated). `journal.py` still reports 0 closed
trades — no `transactions.csv` activity yet, so the discipline guard stays
dormant until trades are logged via `/apply-trade`.

Since the last report (2026-07-13): FIG was sold and the compliance flag
that had been open for 7 consecutive runs is now closed; BMNR (Bitmine
Immersion Technologies) was bought as a new position. The book is now
BMNR + NOW, two names.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.28**,
**+12.0%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.2:1 (skew argues against holding, not for adding) |
| Shariah | recorded PASS (broker app, screened 2026-07-07, not stale) — **but see Action flag #1** |
| DCF intrinsic value | $0.72 vs. $17.28 price -> -95.8% — **model mismatch, not a real signal** (see below) |
| Trailing stop (chandelier) | $14.6136 — price is ~18.5% above it |
| 6m momentum (skip last month) | -47.0% |
| Portfolio note | ATR 7.15% — size down per vol throttle |
| Would buy today? | Mechanically "yes" per recommend.py's default; conviction flagged LOW absent a stated variant view |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.0 >= pe_rich 50).
Live price **$111.23**, **-3.3%** vs. the $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 0.7:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $111.23 price -> +8.0% upside to the model |
| Trailing stop (chandelier) | $98.4905 — price is $12.74 above it |
| 6m momentum (skip last month) | -9.4% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.28 | 10 | $15.43 | $172.80 | +12.0% | 18.2% |
| NOW | $111.23 | 7 | $114.97 | $778.61 | -3.3% | 81.8% |

**Total value: $951.41** | Cost: $958.09 | **Total return: ~-0.7%** (-$6.68 unrealised)

The book is heavily concentrated in NOW (81.8% of value) purely as a
byproduct of the FIG sale + small BMNR add — not a sized decision under the
`max_position_pct: 22` cap, since concentration rules stay muted below 4
names per rules.md. Worth noting the weight is high in absolute terms
regardless of what the rule engine currently enforces.

## Action flags (priority order)

1. **[Mandate / BMNR] Shariah ratio pre-check flag conflicts with the
   recorded compliant status.** `shariah.py`'s automated business-activity
   check classifies BMNR's Yahoo industry tag as `Capital Markets`
   (`Financial Services` sector) — a classification that would normally trip
   the conventional-finance knockout. The holding's front-matter records
   `status: compliant` (broker app, screened 2026-07-07), and a separate web
   check shows Musaffa has historically screened BMNR halal/compliant on
   AAOIFI methodology (as of Q3 2025, ahead of a re-verify you should do
   yourself given the classification quirk). This is the kind of
   discrepancy the ratio pre-check exists to surface — it's a heads-up, not
   an override, but it's worth a fresh Zoya/Musaffa screen given BMNR's
   Yahoo sector/industry tag reads as a financial-markets business, not
   "digital asset treasury." [Musaffa](https://musaffa.com/stock/BMNR/)
2. **[Data quality / BMNR] Holding file has no thesis, risks, or notes
   filled in.** `holdings/bmnr.md` only says "NEW position — screen
   compliance in Zoya/Musaffa before adding more" — no `conviction`,
   `initial_stop`, `target_price`, `invalidation`, or `pre_mortem` fields
   are set. verdict.py can't compute an R-multiple or apply thesis-based
   rules without them, and the DCF flag below is the direct consequence of
   an unfilled record.
3. **[DCF / BMNR] The -95.8% DCF "downside" is a model-mismatch artifact,
   not a real valuation signal.** BMNR is an Ethereum-treasury company (per
   its own filings, holding ~5.79M ETH / ~$10.8B as of early August 2026);
   a standard discounted-*cash-flow* model built for an operating business
   with 5% growth assumptions is the wrong tool for a treasury vehicle whose
   value tracks ETH holdings and share count, not FCF. Flagging so this
   number isn't mistaken for a real signal — a NAV-based view (ETH held x
   ETH price, per share) would be the right model here and isn't something
   this repo's `dcf.py` computes today.
4. **[Valuation / NOW] P/E ~119 (recorded) — rich; VALUATION_RICH holds.**
   Do not add.
5. **[Catalyst / NOW, data hygiene] The front-matter catalyst is stale — Q2
   FY2026 earnings already reported.** ServiceNow reported Q2 2026 on
   2026-07-22: EPS $0.90 (beat $0.76 consensus by 18.4%), revenue $3.99B
   (beat), subscription revenue +23% cc (beat guidance by 1.5pts), and
   raised FY2026 subscription guidance to $15.76-15.78B (~21% cc growth).
   [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html) ·
   Next earnings **2026-10-28** is 88 days out — beyond the 60-day
   `catalyst_horizon_days`/`dead_money_days` window, though not yet "dead
   money" since the just-reported beat is 10 days old, not 60. Update
   `holdings/now-servicenow.md`'s `catalyst.date` so it reflects the next
   real event rather than the one that already happened.
6. **[New leads this run]** Fresh discovery (50-name pool, generated
   2026-08-01) surfaced several LEADs with the highest max-benefit rank:
   **SFD, LIF, SMCI, GWRE, PLTR** — see the Draft & planned setups table
   below. All are UNVERIFIED Shariah (ratio pre-check only, no business
   screen) and none clear the BUY-CANDIDATE gates on their own.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep:** BMNR is up +12.0% since the $15.43 cost basis. The company
disclosed crypto/cash/securities holdings of roughly $11.3B, including
~5.79M ETH (~4.8% of total ETH supply, one of the largest corporate ETH
treasuries), and was added to the Russell 1000 in June 2026. Late-July 2026
buyback activity and bullish ETH sentiment drove a reported +13% move.
[Simply Wall St](https://simplywall.st/stocks/us/software/nyse-bmnr/bitmine-immersion-technologies/news/bitmine-immersion-technologies-bmnr-is-down-60-after-reveali) ·
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-immersion-technologies-achieves-largest-ethereum-treasury)

**Case to watch closely:** the position's whole return is a leveraged bet on
ETH price and treasury execution, not an operating-business thesis — 6m
momentum is -47.0% (this is a volatile name, ATR 7.15% triggers the vol
throttle) and the holding record has no stop, target, or invalidation
written down (Action flag #2). The Shariah ratio pre-check flag (#1) is a
real discrepancy worth resolving, not because it's decisive on its own, but
because "compliant, screened once, no re-check" is thinner ground than the
mandate is meant to stand on for an 18% position.

**Verdict: HOLD (DEFAULT — no rule fired).** That's an artifact of missing
front-matter (no stop = no HARD_STOP/TRAIL_STOP possible to evaluate beyond
the mechanical chandelier), not a considered "thesis intact" call — filling
in the PM fields would let the engine actually test this position rather
than defaulting to HOLD by omission.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 beat across the board (EPS, revenue, subscription
growth) and FY guidance was raised, not cut — the enterprise-workflow /
AI-agent growth story is intact through this print. Armis integration is
contributing (~125bp to subscription growth) with acknowledged near-term
margin drag (~75bp to Q2 operating margin), which is the expected trade-off
of a recent acquisition, not a surprise. DCF shows +8.0% upside to intrinsic
value at the recorded assumptions (18% 5y growth, 10% discount).
[Investing.com](https://www.investing.com/news/company-news/servicenow-q2-2026-slides-revenue-beats-margins-face-ai-pressure-93CH-4807204) ·
[eciks](https://eciks.org/15201-66238-servicenow-q2-earnings-beat-subscription-growth)

**Case to trim / watch:** P/E ~119 remains VALUATION_RICH; 6m momentum is
still negative (-9.4%, though improved from -27.5% last cycle); the next
real catalyst (Q3 earnings, 2026-10-28) is 88 days out, outside the 60-day
horizon the rules treat as "needs a nearer catalyst to justify new capital."
Price is currently $12.74 above the chandelier trailing stop, so no
technical stop is close to firing.

**Verdict: HOLD (VALUATION_RICH — do not add).** The beat argues the thesis
is intact; the multiple argues against adding at this price regardless.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add. Recorded P/E ~119 >=
  `pe_rich` 50.
- **VOL_THROTTLE note -> BMNR**: ATR 7.15% — informational; size any future
  add down accordingly, not a trade trigger on its own.
- **DEFAULT (no rule fired) -> BMNR**: HOLD by omission, not by a positive
  thesis test — see Action flag #2 (no stop/target/invalidation on record
  means most Stage-3/4 rules in rules.md have nothing to evaluate).
- **DEAD_MONEY not yet firing -> NOW**: the Q2 catalyst just resolved
  (10 days ago); would fire if 60 days pass with no re-rating and no nearer
  catalyst added to the record.
- No SELL, TRIM, or HARD_STOP rule fired for either holding this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $17.28 | -95.8% | growth_5y 5%, terminal 2.5%, discount 10% — **FCF-based model on an ETH-treasury company; see Action flag #3, not a usable signal here** |
| NOW | $120.12 | $111.23 | +8.0% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run, as expected: no setup card has been
reviewed and flipped to `status: planned` yet (all 62 non-template cards in
`setups/` remain `status: draft`). All new-idea surfacing this cycle comes
from machine discovery below instead.

## Draft & planned setups — 50 leads, 24 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank, up from the 20-name pool in the
prior report). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for the 24 leads that didn't already have one
(SFD, SMCI, GWRE, LLY, AEM, KGC, TS, AA, WDC, DELL, BBY, ARW, NEM, NVDA, P,
AVGO, HST, DLO, FLYW, SNX, ESE, PDFS, CORZ, CLS, HBM, UTHR, BKR, APH, STX,
VLO, TECK); 38 existing cards (including LIF, PLTR, ADI, DUOL, AMD, ZS,
CNQ, MSFT, GOOGL, RCL, and others carried from prior runs) were left
unchanged. **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.** None can reach BUY-CANDIDATE
until you review the card, edit anything you disagree with, set
`status: planned`, and screen the name compliant in Zoya/Musaffa.

Top 20 by max-benefit rank this run:

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| SFD | LEAD | new | 11.9:1 | earnings 2026-08-11 | 10 |
| LIF | LEAD | existing | 8.7:1 | earnings 2026-08-10 | 9 |
| SMCI | LEAD | new | 10.2:1 | earnings 2026-08-11 | 10 |
| GWRE | LEAD | new | 11.9:1 | earnings 2026-09-03 | 33 |
| PLTR | LEAD | existing | 14.2:1 | earnings 2026-08-03 | 2 |
| ADI | LEAD | existing | 7.8:1 | earnings 2026-08-19 | 18 |
| DUOL | LEAD | existing | 5.5:1 | earnings 2026-08-05 | 4 |
| LLY | LEAD | new | 5.5:1 | earnings 2026-08-05 | 4 |
| AEM | RESEARCH | new | 20.0:1 | earnings 2026-10-28 | 88 |
| AMD | LEAD | existing | 4.6:1 | earnings 2026-08-04 | 3 |
| PAY | RESEARCH | existing | 2.8:1 | earnings 2026-08-03 | 2 |
| KGC | RESEARCH | new | 10.4:1 | earnings 2026-11-10 | 101 |
| TER | RESEARCH | existing | 7.0:1 | earnings 2026-10-21 | 81 |
| TS | LEAD | new | 3.5:1 | earnings 2026-08-05 | 4 |
| AA | RESEARCH | new | 20.0:1 | earnings 2026-10-15 | 75 |
| WDC | RESEARCH | new | 2.9:1 | earnings 2026-08-05 | 4 |
| ZS | LEAD | existing | 4.4:1 | earnings 2026-09-02 | 32 |
| DELL | RESEARCH | new | 1.4:1 | earnings 2026-09-03 | 33 |
| CF | RESEARCH | existing | 2.1:1 | earnings 2026-08-05 | 4 |
| KEYS | LEAD | new | 3.7:1 | earnings 2026-08-18 | 17 |

All cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **AEM, KGC, AA — RESEARCH despite eye-catching 10-20:1 headline R:R.**
  These are capped by the catalyst-horizon gate (75-101 days out, past the
  60-day window), not the asymmetry math — the ratio itself looks
  attractive but there's nothing dated close enough to close the gap yet.
- **PLTR (2 days to catalyst)** carries the government/defense
  business-activity question flagged in prior reports — still open, still
  worth a real Zoya/Musaffa screen before spending review time on the card.
- **Mining/royalty names (AEM, KGC, TECK, NEM, HBM)** carry the same
  financing-structure Shariah nuance noted in earlier reports — precious-
  and base-metals miners often have debt/financing structures worth a
  closer business-activity look, not just the clean ratio pre-check.

## Follow-ups (priority order)

1. **[BMNR] Fill in the holding record** — `conviction`, `initial_stop`,
   `target_price`, `invalidation`, `pre_mortem` are all unset in
   `holdings/bmnr.md`. Until then the engine can only default to HOLD
   rather than actually testing the position.
2. **[BMNR] Re-verify Shariah in Zoya/Musaffa** given the ratio pre-check's
   `Capital Markets` industry flag conflicts with the recorded compliant
   status (Action flag #1) — a heads-up, not an override, but worth
   resolving for an 18% position rather than leaning on a single
   2026-07-07 broker-app screen.
3. **[NOW] Update `catalyst.date`** in `holdings/now-servicenow.md` — Q2
   FY2026 earnings already reported 2026-07-22; the next real catalyst is
   Q3 earnings 2026-10-28.
4. **[Both]** No urgent technical trigger on either name this run (both
   comfortably above their chandelier trailing stops) — the open items are
   data-hygiene and compliance re-verification, not price action.

---
Not financial advice — decision support only. Every buy/sell/hold call
above is yours to make. Shariah status shown is either the broker app's
recorded screen or an automated ratio pre-check; confirm compliance
independently in Zoya/Musaffa before acting on anything in this report.
