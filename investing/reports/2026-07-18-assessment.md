# Portfolio Assessment — 2026-07-18

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, pool widened to 50 names by max-benefit rank
per the 2026-07-13 config change) → `scaffold.py --all-leads` (26 new DRAFT
setup cards auto-filled for names without one; 24 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run except BMNR's
52-week range (not yet available for this recently-listed name). `journal.py`
still shows 0 closed trades — no `transactions.csv` yet, so the FIG sale's
realized P/L never made it into the ledger (see Follow-ups).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$15.69**,
**+1.7%** vs. the $15.43 cost basis. **New position since the last run** (FIG
was sold 2026-07-13 to close the 7-run compliance flag; BMNR opened the same
day) — this is its first assessment cycle.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-9.1:1** (DCF-implied downside far exceeds upside — see flag below) |
| Shariah | Broker app: **compliant** (screened 2026-07-07, not stale). **But** the mechanical ratio pre-check disagrees — see Action flags #1 |
| DCF intrinsic value | $0.72 vs. $15.69 price -> **-95.4% "downside"** — the model is not a sane fit for this business (see flag below) |
| Trailing stop (chandelier) | $14.05 — price ~11.7% above it |
| 6m momentum (skip last month) | -50.4% |
| Portfolio note | ATR 6.82% — above the 6% vol-throttle threshold; size down per policy |
| Would buy today? | recommend.py says yes mechanically, but this contradicts its own -9.1:1 reward:risk — treat as a data artifact, not a signal (see flag below) |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen result |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$103.24**, **-10.2%** vs. $114.97 cost basis — momentum has continued
to deteriorate since last run (-2.0% on 07-13).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | MEDIUM — reward:risk 2.75:1 (moderate skew) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.42 vs. $103.24 price -> **+16.6% upside** to the model |
| Trailing stop (chandelier) | $96.99 — price is $6.25 above it (buffer has narrowed from last run's $15.28 gap) |
| 6m momentum (skip last month) | -24.7% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction MEDIUM |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.69 | 10 | $15.43 | $156.90 | +1.7% | 17.8% |
| NOW | $103.24 | 7 | $114.97 | $722.68 | -10.2% | 82.2% |

**Total value: $879.58** | Cost: $959.09 | **Total return: ~-8.3%** (-$79.51 unrealised)

Composition changed materially since the last run: FIG (51% of the book) was
sold entirely on 2026-07-13, replaced by a small BMNR position, so this
week's total-value comparison isn't apples-to-apples with 07-13's
$1,610.49 — that figure included FIG. Looking only at what's still in the
book, NOW alone has kept sliding (-2.0% -> -10.2% vs. cost) while its
earnings print approaches fast.

## Action flags (priority order)

1. **[New — Shariah, BMNR] Recorded "compliant" conflicts with the mechanical
   ratio pre-check.** `shariah.py` flags: *"industry 'Capital Markets' matches
   'capital markets' — core business fails screen"* (sector: Financial
   Services). The broker app's compliant tag is from 2026-07-07, but BMNR's
   actual business — an Ethereum treasury/staking vehicle that raises capital
   via equity issuance to accumulate and stake ETH — is exactly the kind of
   conventional-finance-adjacent activity the ratio pre-check is built to
   catch. Per `rules.md`'s COMPLIANCE_SCREEN stage: a doubtful/conflicting
   screen means **REVIEW before any add** — this is a new position (5 days
   old) where you can still act before compounding it. Recommend an explicit
   Zoya/Musaffa re-screen rather than relying on the broker tag alone.
2. **[Data quality, BMNR] DCF and reward:risk numbers are not meaningful for
   this name.** The DCF model (5% growth, 2.5% terminal, 10% discount) is
   built for a cash-flow business; BMNR's actual value driver is its ETH
   treasury (reported ~$11.3B in crypto/cash holdings, ~5.77M ETH per recent
   PR Newswire filings) and staking yield, not discounted operating cash
   flow. The -95.4% "downside" and -9.1:1 reward:risk that fall out of it are
   model artifacts, not a real signal — don't read them as bearish price
   calls. This also explains why `recommend.py`'s `would_buy_today: true`
   looks contradictory next to a -9.1:1 ratio: the field isn't reward:risk
   gated. Worth a manual note in `holdings/bmnr.md`'s Notes section so future
   runs don't re-litigate this.
3. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH
   holds. Do not add.
4. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22 — 4 days out.**
   Consensus: ~$3.92B revenue (+22% y/y), EPS ~$0.86 (+4.9% y/y). Conference
   call 2 p.m. PDT. [BigGo Finance](https://finance.biggo.com/news/ir_NOW_20260701_e8087941d423) ·
   [ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx) ·
   [Yahoo Finance / Zacks](https://finance.yahoo.com/markets/stocks/articles/servicenow-set-report-q2-earnings-151900170.html)
5. **[Vol throttle / BMNR]** ATR 6.82% is above the 6% policy threshold —
   size down per the pre-set rule if adding.
6. **[New leads this run]** Pool widened to 50 names (from 20); 17 cleared
   to LEAD, 33 capped at RESEARCH by the asymmetry/catalyst gates. Nearest
   catalysts: **GOOGL** and **TSLA** both report 2026-07-22 (4 days out,
   same day as NOW) — both UNVERIFIED Shariah (ratio pre-check only).

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** small position (17.8% of a 2-name book), essentially flat
(+1.7%), and the underlying ETH-treasury strategy has kept scaling — total
crypto/cash/securities holdings reported at ~$11.3B, ~5.77M ETH (4.8% of
total ETH supply), added to the Russell 1000 and Fortune Crypto 100 this
month, with an investor presentation published 2026-07-16.
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html) ·
[Manila Times / PR Newswire](https://www.manilatimes.net/2026/07/16/tmt-newswire/pr-newswire/bitmine-immersion-technologies-bmnr-releases-july-chairmans-message-eth-is-the-cure-for-the-uncanny-valley-of-wealth/2385917/amp)

**Case to trim / re-screen:** this is the flag that matters most this run —
the mechanical ratio pre-check disagrees with the broker's compliant tag on
industry classification grounds (Capital Markets / Financial Services). A
treasury company whose entire operating model is raising capital to buy and
stake a crypto asset raises real compliance questions (financing structure,
whether staking yield reads as interest-like income) that a ratio pre-check
alone can't resolve — this needs the actual Zoya/Musaffa screen, not a
5-day-old broker tag taken at face value. Separately, 6m momentum is -50.4%
and ATR (6.82%) trips the vol-throttle note.

**COMPLIANCE_SCREEN read: this is a REVIEW-before-add situation, not a hard
SELL** — the broker's screen hasn't flipped to non-compliant, but the
disagreement with the mechanical pre-check is new information worth acting
on now, while the position is still small, rather than after it's grown.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (4 days out);
consensus +22% revenue growth, +4.9% EPS growth; DCF shows +16.6% upside to
intrinsic value ($120.42) at recorded assumptions; price remains above the
chandelier trailing stop, though the buffer has narrowed considerably since
last run ($6.25 vs. $15.28).

**Case to trim / watch closely:** P/E ~119 still VALUATION_RICH; return vs.
cost has worsened from -2.0% to -10.2% in five days; 6m momentum -24.7%
(better than last run's -27.5%, but still deeply negative); the position is
now 82% of a 2-name book — concentration rules are formally muted below 4
names, but that doesn't remove the practical risk of one name dominating the
account.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_SCREEN fired -> BMNR**: doubtful/conflicting screen — REVIEW
  before any add (see Action flag #1). Not a SELL trigger on its own; the
  broker's recorded status hasn't flipped.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **VOL_THROTTLE fired -> BMNR**: ATR 6.82% > 6% threshold — size down if
  adding.
- **DRAWDOWN_REVIEW not firing -> NOW**: -10.2% vs. the 20% threshold (getting
  closer than last run's -2.0%, but not tripped yet).
- **TRAIL_STOP -> NOW**: does NOT fire (`trade_type: core` exempts it from
  the technical trailing-stop rule); price is still above the computed level
  ($103.24 vs. $96.99) but the gap has narrowed sharply this week — worth
  watching into the earnings print.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $15.69 | -95.4% | growth_5y 5%, terminal 2.5%, discount 10% — **model mismatch, see Action flag #2; not a real price call** |
| NOW | $120.42 | $103.24 | +16.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run — expected, since no card has been
reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 50-name pool (widened from 20), 26 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, now pulling
100 names per screen and keeping the top 50 by max-benefit rank) and wrote
**`leads.md`**. `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead without one — 24 cards already
existed and were left unchanged; 26 new DRAFT cards written this run (P,
AVGO, UTHR, DELL, SFD, NVDA, STX, DLO, DINO, FLYW, LLY, WDC, GWRE, AAPL, TS,
ARW, PSX, BKR, TTMI, AMKR, APH, BBY, FSLR, NEM, PDFS, ESE). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.**

Of the 50 leads, 17 cleared every gate to `LEAD`; 33 are capped at
`RESEARCH` (mostly the asymmetry gate — reward:risk < 3.0 — or no catalyst
inside the 60-day window). The 17 `LEAD` rows, nearest catalyst first:

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| GOOGL | LEAD | existing | 10.1:1 | earnings 2026-07-22 | 4 |
| TSLA | LEAD | existing | 13.4:1 | earnings 2026-07-22 | 4 |
| ALKT | LEAD | existing | 9.0:1 | earnings 2026-07-29 | 11 |
| FICO | LEAD | existing | 7.0:1 | earnings 2026-07-29 | 11 |
| UTHR | LEAD | new | 6.3:1 | earnings 2026-07-29 | 11 |
| MSFT | LEAD | existing | 5.0:1 | earnings 2026-07-29 | 11 |
| GDDY | LEAD | existing | 4.3:1 | earnings 2026-07-30 | 12 |
| PLTR | LEAD | existing | 4.9:1 | earnings 2026-08-03 | 16 |
| AMD | LEAD | existing | 3.6:1 | earnings 2026-08-04 | 17 |
| DUOL | LEAD | existing | 4.0:1 | earnings 2026-08-05 | 18 |
| LIF | LEAD | existing | 8.1:1 | earnings 2026-08-10 | 23 |
| P | LEAD | new | 13.9:1 | earnings 2026-08-26 | 39 |
| NVDA | LEAD | new | 3.4:1 | earnings 2026-08-26 | 39 |
| ULTA | LEAD | existing | 5.0:1 | earnings 2026-08-27 | 40 |
| ZS | LEAD | existing | 4.8:1 | earnings 2026-09-02 | 46 |
| AVGO | LEAD | new | 15.0:1 | earnings 2026-09-03 | 47 |
| GWRE | LEAD | new | 3.7:1 | earnings 2026-09-03 | 47 |

All 50 cleared the liquidity floor and a clean-or-flagged ratio pre-check —
not a business-activity screen. Shariah status on every card is
`unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, CDE, MT** — carried over from prior runs (government/defense
  business-activity question for PLTR; mining/royalty financing structure
  questions for precious-metals names; MT's historically tight engineered
  entry/stop/target band, though it dropped to RESEARCH this run on a
  compressed 1.7:1 reward:risk). Still open, still worth checking before
  spending review time on the cards.
- **TSLA / GOOGL / MSFT (SPUS holdings, mega-caps)** — clean debt/liquidity
  ratios on the pre-check, but each carries its own business-activity nuance
  (Tesla's financing-arm interest income, Alphabet's ad/interest-bearing
  cash mix, Microsoft's interest income and gaming/finance-adjacent lines)
  worth the actual Zoya/Musaffa screen, not an assumption from "SPUS holds
  it."
- **BMNR is not in this lead pool** — it's already a holding, so it's
  covered under Verdicts/Action flags above, not here.

## Follow-ups (priority order)

1. **[New, act while the position is small] BMNR Shariah re-screen** — the
   ratio pre-check's Capital Markets flag conflicts with the broker's
   compliant tag; get the actual Zoya/Musaffa screen done before adding to
   this position. See Action flag #1.
2. **[Time-boxed] NOW earnings 2026-07-22** — 4 days out; trailing-stop
   buffer has narrowed to $6.25 from $15.28 last run, worth watching into
   the print.
3. **[Housekeeping] 26 new DRAFT setup cards** added this run (50 total in
   `setups/`); none are `planned`, none can reach BUY-CANDIDATE. Review at
   your own pace.
4. **[Infrastructure — still open, now compounding] No ledger yet** — the
   FIG sale's realized P/L (+$54.95) is recorded in the closed holding's
   front-matter but never made it into `transactions.csv`/`journal.csv`.
   Log it (and future trades) via `/apply-trade` to unlock the discipline
   guard and stop losing realized-trade history to individual `.md` files.
5. **[Ongoing] TSLA / GOOGL business-activity screen** — both share NOW's
   earnings date (2026-07-22); get the actual screen done before, not
   after, that date if either is being considered.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — BigGo Finance](https://finance.biggo.com/news/ir_NOW_20260701_e8087941d423)
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
- [ServiceNow Set to Report Q2 Earnings: Buy, Sell or Hold the Stock? — Yahoo Finance / Zacks](https://finance.yahoo.com/markets/stocks/articles/servicenow-set-report-q2-earnings-151900170.html)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [Bitmine Immersion Technologies (BMNR) Releases July Chairman's Message — Manila Times / PR Newswire](https://www.manilatimes.net/2026/07/16/tmt-newswire/pr-newswire/bitmine-immersion-technologies-bmnr-releases-july-chairmans-message-eth-is-the-cure-for-the-uncanny-valley-of-wealth/2385917/amp)
