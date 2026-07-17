# Portfolio Assessment — 2026-07-17

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank) →
`scaffold.py --all-leads` (26 new DRAFT setup cards auto-filled for names
without one; 24 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data
gaps this run. `journal.py` / discipline guard not run — `transactions.csv`
and `journal.csv` are gitignored personal ledgers and aren't present in this
sandbox checkout, so net-of-cost performance can't be assessed here; run
locally if you want that section.

Since the last run (2026-07-13): FIG was closed (compliance exit, +$54.95
realized) and BMNR was opened. The book is now BMNR + NOW, 2 names.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$15.78**,
**+2.3%** vs. $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -8.75:1 (skew argues against adding, not for it) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but the mechanical ratio pre-check flags it**: industry classified `Capital Markets`, which matches the business-activity knockout list. See flag #1 below — this is the one to resolve, not skip. |
| DCF intrinsic value | $0.72 vs. $15.78 price -> **-95.5%** — but flagged below as not a meaningful read for this business (see flag #2) |
| Trailing stop (chandelier) | $14.0594 — price ~12.2% above it |
| 6m momentum (skip last month) | -50.4% (reflects ETH-price beta, not company fundamentals) |
| Portfolio note | ATR 6.76% — vol-throttle fired; size down |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$104.20**, **-9.4%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | MEDIUM — reward:risk 2.25:1 |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); ratio pre-check clean (debt ratio 0.022, liquid-asset ratio 0.058) |
| DCF intrinsic value | **$120.42** vs. $104.20 price -> **+15.6% upside** to the model |
| Trailing stop (chandelier) | $96.9859 — price is $7.21 above it |
| 6m momentum (skip last month) | -24.7% |
| Would buy today? | Mechanically yes per recommend.py's gates |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names
  (`min_names_for_concentration: 4`). Worth flagging anyway: NOW alone is
  **82.2%** of the book, well past the 22% single-name cap that will apply
  once you hold more names — a function of it being the only pre-existing
  position, not new buying.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.78 | 10 | $15.43 | $157.85 | +2.3% | 17.8% |
| NOW | $104.20 | 7 | $114.97 | $729.40 | -9.4% | 82.2% |

**Total value: $887.25** | Cost: $958.79 | **Total return: ~-7.5%** (-$71.54 unrealised)

## Action flags (priority order)

1. **[Mandate / BMNR] Ratio pre-check disagrees with the recorded compliance
   status.** `shariah.py` classifies BMNR's industry as `Capital Markets`,
   which trips the business-activity knockout list, even though the broker
   app recorded it `compliant` on 2026-07-07. BMNR is an Ethereum-treasury
   company — it now holds ~5.77M ETH (~$11.3B in crypto/cash) and is actively
   **staking** that ETH for yield (~$284M annualized projected staking
   reward per its own investor materials). Staking-for-yield on a treasury
   this size is exactly the kind of activity that can trip a stricter
   AAOIFI-style screen even where a broker's generic classifier passes it.
   This is a policy question, not a price call — worth an independent
   re-check in Zoya/Musaffa given the size of the ETH/staking business
   relative to any operating business, before treating the broker-app
   "compliant" tag as settled.
2. **[Methodology / BMNR] DCF is not a meaningful read here.** The generic
   discounted-cash-flow model (assumptions: 5% 5y growth, 2.5% terminal,
   10% discount) prices BMNR as a small operating company and returns
   -95.5% "upside," but BMNR's value is now overwhelmingly a crypto-treasury
   balance-sheet story (NAV vs. ETH holdings), not a cash-flow business —
   the DCF output isn't informative in either direction. Ignore it for BMNR
   until/unless the model is adapted to NAV-based valuation.
3. **[Catalyst / NOW] Q2 FY2026 earnings confirmed 2026-07-22 — 5 days out**
   (after close). The holding's front-matter has no `earnings_plan` — per
   the gate rules, holding through a print with no valid earnings_plan is a
   `GAP_PLAN_MISSING` condition once one is required for the trade type.
   Consensus for the print: subscription revenue growth in the low-20s%
   range. Decide before Tuesday whether to hold through, trim ahead, or set
   a gap plan (size for an adverse overnight move per
   `earnings_gap_assumption_pct: 25`).
4. **[Valuation / NOW] P/E ~119 (recorded) — rich; VALUATION_RICH holds.**
   Do not add at this multiple; growth has to keep delivering.
5. **[Vol / BMNR] ATR 6.76% — vol-throttle note fired.** Size down for new
   entries; this is already a 17.8%-weight position at that volatility.

## Per-holding read

**BMNR (Bitmine Immersion Technologies).** The thesis on file is thin — "NEW
position — screen compliance in Zoya/Musaffa before adding more" is a
placeholder, not a variant view. Facts as of this week: ETH holdings at
~5.77M tokens (~4.8% of total supply), total crypto+cash ~$11.3B, Q3 FY2026
revenue $46.5M with matching gross profit, operating cash flow $316.3M,
recent Russell 1000 and Fortune Crypto 100 inclusion. The case to keep: it's
a large, liquid, high-visibility ETH-treasury vehicle riding both ETH price
and a growing staking-yield stream; up modestly since your $15.43 cost.
The case to trim/exit: (a) the compliance question above is unresolved and
the mechanical screen actively disagrees with the recorded status; (b)
6-month momentum is -50.4% — this is a highly volatile, ETH-beta name, not
a steady compounder; (c) no stated stop/target/invalidation on the holding
card, so there's no pre-committed exit discipline in place for a position
this volatile. [Bitmine ETH holdings announcement](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html) ·
[Q3 FY2026 earnings](https://www.quiverquant.com/news/Bitmine+Immersion+Technologies+(BMNR)+Releases+Q3+2026+Earnings:+Revenue+Jumps+to+$46.5+Million,+Cash+Surges)

**NOW (ServiceNow).** Thesis on file: durable enterprise-workflow
subscription grower, AI-agent (Zurich platform) and Armis security
integration as forward drivers. Case to keep: DCF still shows ~16% upside to
the recorded growth/discount assumptions, subscription growth has been
running ~21%, and Q2 earnings (2026-07-22) is a real near-term catalyst to
test the AI-agent narrative. Case to trim/reduce: P/E ~119 is priced for
continued high growth — any deceleration signal on the call hits hard — and
the position is currently -9.4% since cost with 6m momentum -24.7%, so the
market has been pricing in some of that risk already. No gap plan is set for
a name reporting in 5 days.

## Rules fired (your own pre-set rules, from rules.md)

- **VALUATION_RICH** (NOW): recorded P/E ~119.02 >= `pe_rich` (50) -> HOLD,
  do not add.
- **Vol-throttle note** (BMNR): daily ATR% 6.76 > `vol_throttle_atr_pct` (6)
  -> de-risk note on new sizing.
- No SELL/TRIM/GAP_PLAN_MISSING rule mechanically fired this run — but see
  action flag #3: NOW's earnings-window gap plan should be set manually
  before 2026-07-22 if a rule requiring it isn't yet coded for `trade_type:
  core` holdings.

If you execute anything from this list, run `/apply-trade` so the holding
files and ledger update.

## DCF

| Ticker | Intrinsic value | Price | Upside/downside | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $15.78 | -95.5% (not meaningful — see flag #2) | growth 5%, terminal 2.5%, discount 10% |
| NOW | $120.42 | $104.20 | +15.6% | growth 18%, terminal 3%, discount 10% |

## New ideas (discovery + watchlist)

`watchlist.md` is currently empty (no hand-curated names yet) — all ideas
below come from `discover.py`'s machine pool (50 tickers, halal-ETF holdings
+ Yahoo screens), gated by liquidity/asymmetry/catalyst. **Every name is
UNVERIFIED for Shariah** until screened in Zoya/Musaffa and is capped at
RESEARCH/LEAD until a completed (non-draft) setup card exists — none of
these are BUY-CANDIDATEs.

Top LEADs by reward:risk (discovery-stage estimates, not a buy list):

| Ticker | R:R | Score | Card | Earnings |
|---|---|---|---|---|
| P (Pandora/SiriusXM) | 13.8:1 | 32.0 | no card yet | 2026-08-26 |
| TSLA | 12.9:1 | 34.5 | has card | 2026-07-22 |
| AVGO | 10.5:1 | 38.1 | DRAFT (new) | 2026-09-03 |
| GOOGL | 9.5:1 | 40.7 | has card | 2026-07-22 |
| ALKT | 9.4:1 | 38.8 | has card | 2026-07-29 |
| FICO | 8.9:1 | 41.0 | has card | 2026-07-29 |
| LIF | 8.6:1 | 34.8 | has card | 2026-08-10 |

All: `RESEARCH` (no completed card / thin asymmetry / no near catalyst) for
the remaining ~31 names in `leads.md`, including AMD, DELL, NVDA, MU, AAPL,
LLY — none exceed RESEARCH mechanically this run. Full list with
entry/target/stop estimates is in `leads.md`.

## Draft & planned setups

26 new DRAFT cards were auto-filled this run for leads without one (AVGO, P,
UTHR, SFD, DELL, DG, DLO, STX, WDC, NVDA, DINO, FLYW, LLY, GWRE, AAPL, ARW,
TS, PSX, BKR, TTMI, AMKR, APH, NEM, FSLR, PDFS, BBY) — each is
`RESEARCH — DRAFT awaiting your review (set status: planned to approve)`.
These are formula-output proposals only: review the entry-trigger / stop /
target logic and gap plan in each `setups/<ticker>.md`, edit anything you
disagree with, and flip `status: planned` only after you've supplied your
own edge and screened the name compliant. 24 existing cards (GOOGL, TSLA,
ALKT, FICO, LIF, MSFT, GDDY, DUOL, AMD, VRNS, PLTR, MT, ZS, CVE, PAY, ULTA,
JNJ, CF, CNQ, RCL, SIMO, ALAB, MU, KLIC) were left unchanged. No card in the
repo currently carries `status: planned` or a human-verified `shariah:
compliant` — there is no BUY-CANDIDATE this run.

## Follow-ups

1. Resolve the BMNR Shariah ratio-pre-check flag (Capital Markets /
   staking-yield business mix) independently in Zoya/Musaffa — don't let
   the broker-app "compliant" tag stand unexamined given the size of the
   ETH/staking business.
2. Decide a gap plan for NOW ahead of the 2026-07-22 earnings print (5 days
   out) — hold-through with a sized stop, trim ahead, or exit.
3. Fill in BMNR's thesis/stop/target/invalidation fields — currently a
   placeholder, and it's the more volatile of your two names (ATR 6.76%,
   6m momentum -50.4%).
4. When ready to add names, review the DRAFT cards above rather than acting
   on `leads.md` directly — none are underwritten yet.
5. If you want the discipline-guard section (net-of-cost performance vs.
   Shariah benchmark), run this routine from an environment that has your
   local `transactions.csv` / `journal.csv` — they're gitignored and not in
   this checkout.

---
Not financial advice — decision support only. All Shariah statuses above are
either broker-app records or a mechanical ratio pre-check; verify
independently in Zoya/Musaffa before acting on anything in this report.
