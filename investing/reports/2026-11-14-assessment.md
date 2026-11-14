# Portfolio Assessment — 2026-11-14

Not financial advice. This is decision support only. Every buy, sell or hold
call is yours. The Shariah status shown below is either the broker app's
recorded screen or a mechanical ratio/business-activity pre-check. Neither is a
fatwa. Verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data: 170-name raw pool, 4 dropped on liquidity, 76
dropped on the Shariah ratio/business knockout, top 50 kept), then
`scaffold.py --all-leads` (**27 new DRAFT cards**; 23 existing cards left
unchanged), then `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` / `journal.py`. All ran live with no data gaps.
There is still no `transactions.csv`, so the journal shows 0 closed trades and
the discipline guard stays dormant.

**Since the last report (2026-08-19):** no trades were recorded. The book is
down from $1,105.51 to **$891.55**. NOW reported Q3 on 2026-10-28 and fell
afterwards. BMNR gave back most of its gain.

## Verdicts (lead with this)

These are YOUR rules resolving mechanically, not advice.

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired). Price **$17.58**, **+13.9%**
vs the $15.43 cost basis (it was +33.1% last run).

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW — "missing reward:risk or a stated thesis" |
| Shariah (recorded) | compliant (broker app, 2026-07-07) — **now STALE (>100 days)**; recommend.py: `REVIEW — re-screen` |
| Shariah (ratio pre-check) | **FAIL** — industry `Capital Markets`, core business fails the screen (2nd run in a row) |
| Trailing stop (chandelier) | $19.85 — **price is 11.4% BELOW it** (TRAIL_STOP exempt only because `trade_type: core` by default) |
| EMA fast | $20.33 — price is below it |
| 6m momentum (skip last month) | +17.6% |
| DCF | -$6.53 intrinsic. This is meaningless for an ETH-treasury business (see DCF caveat) |
| Would buy today? | recommend.py says yes, but it only reads the recorded Shariah field |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= 50). Price
**$102.25**, **-11.1%** vs the $114.97 cost basis.

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW — no stated edge, target or stop in the holding file |
| Shariah (recorded) | compliant (broker app, 2026-06-09, purification 3.35%) — **now STALE (>100 days)**; ratio pre-check passes (debt 2.3%, liquid 5.9%) |
| Trailing stop (chandelier) | $138.00 — **price is 26% BELOW it** (core-exempt) |
| EMA fast | $116.55 — price is below it |
| 6m momentum | +56.3% (the skip-month window still includes the summer rally) |
| 52w range position | 13% (near the lows) |
| DCF | $119.65 vs $102.25, **+17.0%** (it was -6.6% last run) |
| Would buy today? | recommend.py says yes; conviction is LOW without your own edge |

Portfolio notes (verdict.py):
- There are only 2 holdings, so concentration rules stay muted until there are 4 or more.
- **VOL_THROTTLE:** BMNR ATR 8.9% and NOW ATR 7.0%. Size down per the vol throttle (new this run).

## Snapshot (live)

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.58 | 10 | $15.43 | $175.80 | +13.9% | 19.7% |
| NOW | $102.25 | 7 | $114.97 | $715.75 | -11.1% | 80.3% |

**Total: $891.55** | Cost $959.09 | **Unrealised -$67.54 (-7.0%)**. That is a
swing from +15.3% at the last report.

## Action flags (priority order)

1. **[Mandate] Both holdings' Shariah screens are now STALE.** NOW was screened
   2026-06-09 and BMNR on 2026-07-07, both more than one quarter ago. Your
   rule **COMPLIANCE_SCREEN** ("screen > 1 quarter old -> REVIEW before any
   add") applies to both. `recommend.py` reports `shariah_status: REVIEW` for
   both, but **`verdict.py` still prints HOLD**. The stale-screen rule is not
   wired into verdict.py. Re-screen both in Zoya/Musaffa.
2. **[Mandate, carried over] BMNR fails the business-activity pre-check for the
   second run in a row.** It is classified Capital Markets. Its own Nov 9
   release describes $14.3B of holdings: 6.07M ETH, BTC, equity stakes, $475M
   cash/securities, ~5.23M ETH staked (projected ~$359M/yr staking income), and
   a listed preferred share (BMNP). That profile is what a business screen is
   built to catch. A confirmed fail = **COMPLIANCE_GATE -> SELL**, regardless
   of P/L. This has now been open since 2026-08-19.
3. **[Risk] Both holdings trade well below their chandelier stops and fast
   EMAs.** NOW is 26% under and BMNR is 11% under. TRAIL_STOP does not fire
   only because neither holding file sets `trade_type`, so both default to
   `core`, which is exempt. If either was meant as a swing/momentum trade, the
   stop rule would have fired a SELL. Confirm the classification is
   deliberate.
4. **[Valuation / NOW] VALUATION_RICH is reading a stale `pe: 119.02`** from
   the holding file (recorded when price was ~$106). Update it. DCF now shows
   +17% to intrinsic under your recorded 18%-growth assumption.
5. **[Housekeeping] Neither holding has a stop, target, invalidation, or
   pre-mortem.** BMNR has no thesis at all. NOW's catalyst field still says
   "Q2 FY2026 earnings" with `date: null`, and Q3 has already printed.

## Per-holding read

### NOW — ServiceNow
**Case to keep:**
- Q3 2026 (reported Oct 28): revenue **$4.106B, +20.5% YoY**; subscription
  $3.988B, +20.5% cc.
- AI ACV year-end target raised to **$1.7B** (from $1B).
- FY FCF margin target raised 100bp to 36%.
- Q4 subscription guide $4.24–4.25B (~+23%).
- Your own invalidation text ("subscription growth decelerating meaningfully
  below ~21–22%") is borderline but **not clearly hit** (20.5% cc, guided
  back up to ~23%).
- DCF: +17%.

**Case to watch:**
- The stock fell after the print despite the revenue beat.
- Non-GAAP EPS $1.00 vs $1.02 expected.
- GAAP net income $277M vs $502M a year ago.
- GAAP operating margin 9.5% (Armis integration costs are a likely factor).
- Position is -11.1%, near the bottom of the 52w range, and below every
  technical stop level.
- It is 80% of the book.

[Securities.io](https://www.securities.io/servicenow-q3-subscription-revenue-rises-21-to-3-988-million/) ·
[Constellation Research](https://www.constellationr.com/insights/news/servicenow-q3-mixed-strong-control-tower-demand) ·
[Finviz/press release](https://finviz.com/news/410638/servicenow-reports-third-quarter-2026-financial-results) ·
[Diginomica](https://diginomica.com/node/31392)

### BMNR — Bitmine Immersion Technologies
**Case to keep:**
- ETH count keeps rising (6.06M -> 6.07M week over week).
- Staking scale-up projects ~$359M/yr annualized.
- Russell 1000 member.
- Still +13.9% on cost.

**Case to flag:**
- The compliance question (flag #2) is unresolved.
- Holdings fell $14.5B -> $14.3B week over week on lower ETH ($2,261 -> $2,234).
  The stock is effectively a leveraged ETH proxy (ATR 8.9%).
- There is no thesis on file to judge it against.
- No independent coverage was found. The figures come from company press
  releases.

[Chainwire (Nov 9 release)](https://chainwire.org/2026/11/09/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-6-07-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-14-3-billion/) ·
[Finviz (Nov 2 release)](https://finviz.com/news/413195/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-145-billion)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_SCREEN matches -> BMNR, NOW:** screen > 1 quarter old, so
  REVIEW before any add.
- **COMPLIANCE_GATE does not fire yet -> BMNR:** the recorded status is still
  `compliant`. If a re-screen confirms the business-activity fail, your
  pre-set action is SELL (exit, purify per Zoya/Musaffa).
- **VALUATION_RICH fired -> NOW:** HOLD, do not add (based on the stale P/E).
- **VOL_THROTTLE fired -> BMNR, NOW:** size down.
- **TRAIL_STOP:** the price condition is met for both, but the action is
  suppressed by the `core` exemption.
- **DRAWDOWN_REVIEW:** not firing (NOW -11%, below the 20% threshold).

*If you execute anything, run `/apply-trade` so holdings and the ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic | Price | Up/(down) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $102.25 | +17.0% | growth_5y 18%, terminal 3%, discount 10% |
| BMNR | -$6.53 | $17.58 | n/m | default 5% / 2.5% / 10%. Operating-cash-flow DCF does not fit a crypto-treasury company. Treat as a data gap |

## New ideas (watchlist.md)

`watchlist.md` is still empty. `recommend.py`'s ideas array returned
**0 BUY-CANDIDATEs**. That is expected: all 90 cards in `setups/` are
`status: draft`, and none are planned or Shariah-verified.

## Draft & planned setups — 50 leads, 27 new DRAFT cards

**5 LEADs** clear the discovery gates. **45 are RESEARCH**: most are blocked by
CATALYST_GATE (next earnings 61 or more days out), BBY and ADI by
ASYMMETRY_GATE. Every row is Shariah **UNVERIFIED** and every level is a
formula output.

Each LEAD carries the verdict **RESEARCH — DRAFT awaiting your review (set
status: planned to approve).**

| Ticker | Setup | Card entry / stop / T1 (R:R) | Catalyst | Discovery R:R* |
|---|---|---|---|---|
| KEYS | earnings_run | 297.68 / 293.25 / 304.32 (1.5) — gap plan `exit_before` | earnings 2026-11-19 (5d) | 10.8 |
| JBL | earnings_run | 254.25 / 251.81 / 257.91 (1.5) | earnings 2026-12-16 (32d) | 20.0 |
| PENG | earnings_run | 47.36 / 47.11 / 47.73 (1.5) | earnings 2027-01-05 (52d) | 14.8 |
| AVGO | — | **stale card from a prior run** (entry 364.41, stop 384.52 *above* entry, Sept catalyst) — rescaffold with `--force` | earnings 2026-12-09 (25d) | 5.2 |
| SNX | — | **stale card** (Sept 24 catalyst already passed) — rescaffold with `--force` | earnings 2027-01-07 (54d) | 7.3 |

\* **Read the discovery R:R with care.** Discovery measures reward to the 52w
high against a stop only a few dollars below entry. On these names the stop
sits **well inside one ATR** of entry. For example, PENG has R = $0.25 against
an ATR of $5.74, and KEYS has R = $4.43 against an ATR of $17.19. Normal daily
noise would likely hit those stops, so the 10–20:1 figures are not realistic.
The cards' own T1 targets are only 1.5R. This is a scaffold/discovery formula
weakness worth fixing before trusting the LEAD ranking.

Other flags:
- **ORCL-PD** is a **preferred share** (fixed-dividend instrument). It is
  generally not Shariah-permissible by structure, yet it passed the ratio
  knockout. Its card should likely be abandoned, and discovery should filter
  `-P*` tickers.
- The recurring mining/metals cluster (AEM, TECK, AR, AA, STLD, LIF) and
  APA/FRO (energy/shipping) need a real business screen before you spend
  review time on them.
- New cards: KEYS, CRH, JBL, AEM, PENG, TECK, KLAC, STLD, AMAT, ASML, ORCL-PD,
  SANM, VIAV, FN, BBY, UI, HSY, COHR, FRO, NTAP, SNA, NTNX, APA, LSCC, DIOD,
  ANET, SMTC. Full table in `leads.md`.

## Follow-ups (priority order)

1. **[Urgent] Re-screen BMNR in Zoya/Musaffa on the business-activity
   question.** It has been open 3 months, and a fail = SELL under your rules.
2. **[Urgent] Re-screen NOW.** The screen is stale (>1 quarter); confirm the
   purification %.
3. **[Decision] Both positions are below their chandelier stops.** Confirm the
   `core` classification is intentional (set `trade_type` explicitly in
   bmnr.md).
4. **[Housekeeping]** Update NOW's `pe`, `catalyst`, `last_review`. Fill in
   BMNR's thesis, stop, target, and invalidation.
5. **[Tooling]** Wire COMPLIANCE_SCREEN (stale screen) into verdict.py.
   Filter preferred shares in discovery. Rescaffold stale cards whose
   catalyst has passed (AVGO, SNX).
6. **[Infrastructure]** Start `transactions.csv` (log the FIG sale and BMNR
   buy) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app recorded
flag or a mechanical ratio/business pre-check, neither a fatwa. Verify
independently in Zoya/Musaffa before acting. Short-term trading usually
trails buy-and-hold after costs.
