# Portfolio Assessment — 2026-10-02

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is the broker app's recorded screen or a mechanical
pre-check, neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (17 new
DRAFT cards: AAPL, AMKR, APA, BBY, BLSH, CORZ, DDOG, DDS, FLYW, FN, HBM, JBL,
LLY, NTNX, TECK, TS, XOM) → `prices / shariah / dcf / signals / verdict /
recommend` — all live, no data gaps. **Web catalyst research was not run this
cycle** (scheduled, unattended run); catalyst notes below come only from the
scripts' data. `journal.py` not run — still no `transactions.csv`.

## Verdicts

**BMNR -> HOLD** (DEFAULT, no rule fired). $26.58, +72.3% vs $15.43 cost.
Trailing stop $23.71 (~10.8% below), 6m momentum +18.6%. Portfolio note: ATR
6.46% — size down per vol throttle. **Shariah conflict still open (below).**
Mechanical record: conviction LOW (DCF-derived R:R -9:1 is meaningless for a
crypto-treasury business; treat as data gap).

**NOW -> HOLD** (VALUATION_RICH, P/E ~119 — hold, do not add). $135.76, +18.1%
vs $114.97. Trailing stop $129.59 (~4.5% below), 6m momentum +34.0%. DCF
$120.12 vs price -> -11.5%. Conviction LOW (mechanical proxy). Next earnings
~2026-10-28 (inside the 60-day horizon; gap risk if held through the print).

These are your own rules resolving, not advice.

## Snapshot

| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $26.58 | 10 | $15.43 | $265.85 | +72.3% | 21.9% |
| NOW | $135.76 | 7 | $114.97 | $950.60 | +18.1% | 78.1% |

**Total $1,216.45** | cost $959.09 | unrealised ≈ +$257 (+26.8%).

## Action flags

1. **[Mandate] BMNR ratio pre-check still FAILS** — industry `Capital Markets`
   (core business fails screen) vs recorded `compliant` (broker app, 2026-07-07,
   not stale). Unresolved since the 2026-08-19 report; `recommend.py` only reads
   the recorded field and says "would buy today: yes". A confirmed fail is a hard
   SELL under Gate 1 regardless of the +72% gain. Re-screen the business-activity
   question in Zoya/Musaffa.
2. **[Mandate] NOW Shariah screen is stale** (2026-06-09, >100 days) — re-screen.
   Ratio pre-check passes (debt 1.7%, liquid 4.5%).
3. **[Valuation] NOW P/E ~119** — rich; do not add.
4. **[Catalyst] NOW earnings ~2026-10-28** — decide the gap plan beforehand.
5. **[Cards] BMNR/NOW** lack stop/target/pre-mortem fields on the holding file
   (BMNR also no thesis), so PM records are mechanical defaults.

## DCF

NOW: $120.12 (growth 18%/5y, terminal 3%, discount 10%). BMNR: $0.72 (5%/2.5%/10%)
— model does not fit the business; ignore.

## New ideas

`recommend.py` returns no BUY-CANDIDATE/RESEARCH ideas (watchlist/universe
empty of eligible names). Discovery produced 50 leads (`leads.md`); top by
reward:risk: CORZ 20:1, BLSH 20:1, LLY 10.5:1, GOOGL 9.4:1, ASTS 12:1, STX 7.1:1.
All are LEADs only — Shariah UNVERIFIED, EDGE not supplied, new cards are DRAFT.
Note CORZ/BLSH are crypto-adjacent, similar in kind to the BMNR flag. PLTR's
earlier business-activity question remains open.

Not financial advice; verify Shariah status in Zoya/Musaffa.
