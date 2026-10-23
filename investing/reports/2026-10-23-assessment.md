# Portfolio Assessment — 2026-10-23

Not financial advice. Decision support only — every buy/sell/hold call is
yours. Shariah status below is the broker app's recorded screen or a mechanical
ratio/business pre-check, neither a fatwa — verify in Zoya/Musaffa.

## What ran this cycle

`discover.py` (live Yahoo, top 50 kept) → `scaffold.py --all-leads` (19 new
DRAFT cards, 84 cards in `setups/` total; two Yahoo 401 errors during scaffold
were non-fatal) → `prices` / `shariah` / `dcf` / `signals` / `verdict` /
`recommend`, all live. **Web catalyst research was not done in this automated
run** — catalyst dates below come only from Yahoo/discovery. No
`transactions.csv` yet, so the discipline guard stays dormant.

## Verdicts

**BMNR -> HOLD** (DEFAULT, no rule fired). $22.77, **+47.6%** vs $15.43 cost.
Trailing stop $23.98 — **price is now BELOW the chandelier stop (~5.1%)**, yet
verdict.py shows HOLD; treat the stop level as a prompt to review your own exit.
EMA20 $23.79 (price also under it). 6m momentum +26.6%. Conviction LOW (no
stated thesis / reward:risk). Vol throttle: ATR 6.46% — size down.

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 >= 50: hold, do not add). $157.50,
**+37.0%** vs $114.97. Trailing stop $140.63 (~10.7% below). EMA20 $144.42.
6m momentum +52.8%. Conviction LOW (DCF reward:risk -2.2:1).

Both are mechanical proxies of YOUR rules, not advice. Only 2 holdings —
concentration rules muted (< 4 names).

## Snapshot

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $22.77 | 10 | $15.43 | $227.75 | +47.6% | 17.1% |
| NOW | $157.49 | 7 | $114.97 | $1,102.46 | +37.0% | 82.9% |

Total: **$1,330.21**. NOW is 82.9% of the book — above `max_position_pct` 22,
though the cap is muted while holdings < 4.

## Action flags (priority order)

1. **Shariah — BMNR**: ratio pre-check FAILS the business screen (industry
   `Capital Markets`) while the recorded broker-app "compliant" (2026-07-07) is
   now >100d stale. Still unresolved from the 2026-08-19 report. Re-screen in
   Zoya/Musaffa.
2. **Shariah — NOW**: recorded compliant, screened 2026-06-09, now stale (>100d).
   Pre-check clean (debt 1.5%, liquid 3.9%). Re-screen.
3. **BMNR below trailing stop** (see above).
4. **NOW valuation**: P/E ~119 rich; DCF $120.12 vs $157.55 (-23.8%).

## Per-holding read

- **BMNR** — Keep: +47.6%, positive 6m momentum. Trim/exit case: below chandelier
  stop and EMA20, ATR 6.5%, compliance question open, and the card still lacks
  thesis/variant view/stop/target/pre-mortem (now ~3.5 months in).
- **NOW** — Keep: +37% and strong momentum (+52.8% 6m), price above all trend
  levels. Trim case: P/E ~119, DCF below price, 83% of book in one name.
  **Earnings expected ~2026-10-28 (5 days out)** — a gap risk through the
  print; a stop does not execute through a gap.

## DCF (assumptions visible)

| Ticker | Intrinsic | Price | Upside | growth 5y / terminal / discount |
|---|---|---|---|---|
| BMNR | $0.72 | $22.76 | -96.8% | 5% / 2.5% / 10% — model does not fit a crypto-treasury business; ignore |
| NOW | $120.12 | $157.55 | -23.8% | 18% / 3% / 10% |

## New ideas

`recommend.py` ideas array is empty (no `planned` cards), so **no
BUY-CANDIDATE**. All leads below are LEAD/RESEARCH, Shariah UNVERIFIED, EDGE not
supplied. Top by discovery rank (full 50 in `leads.md`); R:R is a formula output:

| Ticker | Verb | R:R | Earnings | Card |
|---|---|---|---|---|
| FSLR | LEAD | 20.0 | 2026-10-29 | new draft |
| RCL | LEAD | 8.5 | 2026-10-27 | existing |
| BKR | LEAD | 8.3 | 2026-10-27 | new draft |
| ADI | LEAD | 8.9 | 2026-11-24 | existing |
| NET | LEAD | 5.3 | 2026-11-05 | existing |
| FICO | LEAD | 7.0 | 2026-11-04 | existing |
| PAY | LEAD | 4.3 | 2026-11-02 | existing |
| PLTR | LEAD | 3.0 | 2026-11-02 | existing |
| MSFT | LEAD | 3.0 | 2026-10-28 | existing |
| DINO | RESEARCH | 1.0 | 2026-10-28 | existing |

Several earnings land within days (RCL, BKR 10-27; MSFT, DINO 10-28; FSLR, GDDY
10-29) — each needs a valid `earnings_plan` before it could clear the gap gate.
Very high R:R (e.g. FSLR 20:1 with a stop ~1.5% away) usually means a tight
formula stop, not a real edge.

## Draft & planned setups

None `planned`. All 19 newly scaffolded cards are
`RESEARCH — DRAFT awaiting your review (set status: planned to approve)`; levels
are formula outputs, not recommendations. Review/edit in `setups/`.

## Follow-ups

1. Re-screen BMNR (fails pre-check) and NOW (stale) in Zoya/Musaffa.
2. Decide on BMNR vs its trailing stop; fill its PM fields.
3. Plan for NOW earnings ~10-28 (gap risk, 83% weight).
4. Review the new DRAFT cards at your pace.
5. Start logging trades via `/apply-trade` to enable the discipline guard.

---
Not a financial advisor. Verify Shariah status in Zoya/Musaffa before acting.
