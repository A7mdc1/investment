# Portfolio Assessment — 2026-10-04

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status below is the broker app's recorded screen or a
mechanical ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa
before acting.

## What ran this cycle

`discover.py` (live Yahoo, top 50 kept) → `scaffold.py --all-leads` (16 new
DRAFT cards: AAPL, AMKR, APA, BBY, BLSH, CORZ, DDS, FLYW, FN, HBM, JBL, LLY,
NTNX, TECK, TS, XOM — existing cards unchanged) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py`, all
live, no data gaps. **Not done this run:** per-holding web research on
catalysts/news (unattended run, no web research performed) — catalyst notes
below are from repo data only; nothing here is invented. `journal.py` not run
(no `transactions.csv`).

## Verdicts

**BMNR -> HOLD** (RULE: DEFAULT). $26.27, **+70.3%** vs $15.43 cost.
**NOW -> HOLD** (RULE: VALUATION_RICH, P/E ~119 >= pe_rich 50 — hold, do not add). $134.38, **+16.9%** vs $114.97.

| Mechanical PM record (proxies, not a conviction call) | BMNR | NOW |
|---|---|---|
| Conviction | LOW (R:R -9.8:1, DCF target below stop) | LOW (R:R -2.8:1) |
| Shariah (recorded) | PASS, screened 2026-07-07 | recorded compliant, **STALE** (screened 2026-06-09, >100d) |
| Shariah (ratio pre-check) | **FAIL — industry "Capital Markets"** | ok (debt 1.7%, liquid 4.5%) |
| DCF intrinsic | $0.72 (-97.3%) — model doesn't fit a crypto-treasury | $120.12 (-10.6%) |
| Trailing stop | $23.66 (price 9.9% above) | $129.37 (price 3.7% above) |
| 6m momentum | +18.6% | +34.0% |

Portfolio notes: only 2 holdings, concentration rules muted until >= 4 names;
BMNR ATR 6.59% — size down per vol throttle.

## Snapshot (live)

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.27 | 10 | $15.43 | $262.70 | +70.3% | 21.8% |
| NOW | $134.38 | 7 | $114.97 | $940.66 | +16.9% | 78.2% |

**Total $1,203.36** vs cost $959.09 (~+25.5%, +$244 unrealised).

## Action flags (priority order)

1. **[Mandate] NOW Shariah screen is stale** (2026-06-09, now ~117 days > 100d limit). Re-screen in Zoya/Musaffa. Ratio pre-check is clean.
2. **[Mandate — still open since 2026-08-19] BMNR ratio pre-check FAILS** (industry `Capital Markets`) while the recorded status says compliant. recommend.py reads only the recorded field, so its "would buy today: true" is blind to this. Per Gate 1 a confirmed fail is an absolute SELL regardless of the +70% gain. The 2026-08-19 report asked for a business-activity re-screen; no updated screen is recorded. Re-screen before holding further or adding.
3. **[Valuation / NOW]** P/E ~119, DCF 10.6% below price: VALUATION_RICH holds, do not add.
4. **[Stops]** NOW is only 3.7% above its trailing stop ($129.37); a close below it would fire the SELL technical trigger.
5. **[DCF caveat / BMNR]** -97% DCF is a model-fit gap, not a valuation call.
6. **[Catalyst / NOW]** Next earnings were ~2026-10-28 per the prior report (~24 days out, inside the 60-day window) — unverified this run.

## Per-holding read

**BMNR.** Keep: +70% gain, price above trailing stop and EMA, positive 6m momentum. Trim/exit: unresolved Shariah business-activity conflict (a hard gate, not a price call), high vol (ATR 6.6%), no thesis/invalidation/pre-mortem written in the holding file (thesis still reads "NEW position — screen compliance...").
**NOW.** Keep: durable subscription grower, 6m momentum +34%, ratio screen clean. Trim/caution: 78% of the book, P/E ~119, DCF below price, price near its stop, stale compliance record, no target/invalidation/pre-mortem recorded.

## Suggested actions (from YOUR rules)

- Rule VALUATION_RICH fired (NOW) -> hold, do not add.
- Shariah staleness rule (NOW) -> re-screen.
- Rule vol throttle (BMNR ATR 6.59%) -> size down on any add.
- BMNR Gate 1 is only *potentially* triggered (pre-check fail vs recorded compliant) — needs your Zoya/Musaffa call.

If you execute anything, run `/apply-trade` so holdings and the ledger update.

## New ideas

`recommend.py` returned an empty `ideas` array (watchlist.md produces none). Discovery produced 50 leads, 27 at LEAD tier, the rest capped at RESEARCH by asymmetry/catalyst gates. Top LEAD-tier by R:R (discovery-stage estimates, all Shariah UNVERIFIED, none has a `planned` card, so **none can be BUY-CANDIDATE**): CORZ 20.0:1, BLSH 20.0:1, GDDY 17.6:1 (has card), GOOGL 11.2:1 (has card), ASTS 11.8:1 (has card), LLY 9.3:1, STX 5.0:1, TSLA 5.8:1. Treat all as RESEARCH: review the draft card, screen compliance, then set `status: planned`. PLTR remains RESEARCH (R:R 1.4:1; defense business-activity question still open). CORZ/BLSH/BMNR-adjacent crypto names carry the same business-activity risk as flag #2.

## Follow-ups

1. Re-screen **BMNR** (business activity) and **NOW** (stale) in Zoya/Musaffa and record on the holding files.
2. Fill in target/invalidation/pre-mortem for both holdings.
3. Decide how to handle 78% NOW concentration (your call).
4. Review/promote or discard the 16 new DRAFT cards.

Not financial advice. Verify all Shariah status in Zoya/Musaffa.
