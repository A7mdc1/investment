# Portfolio Assessment — 2026-09-02

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data) → `scaffold.py --all-leads` (13 new DRAFT
setup cards auto-filled: TS, HBM, TECK, BLSH, PAAS, SMCIP, XOM, SMTC, FLYW,
BBY, ASND, AAPL, NTNX, APA, PR, NTR; the rest of the pool already had cards)
→ `prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live. Yahoo rate-limited `recommend.py`'s price/technicals
calls (HTTP 429) after several successful calls elsewhere in the run; the
holding-level PM records below still returned complete, but treat any
`recommend.py` numbers as slightly stale vs. the fresher `prices.py`/`verdict.py`
pull. `journal.py` not run — still no `transactions.csv` (discipline guard
stays dormant).

**Since the last report (2026-08-19):** no trades logged. Both holdings are
unchanged in size; this run's news is entirely price/technical movement plus
one persistent, still-unresolved compliance flag.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$23.06**, up
**+49.4%** vs. the $15.43 cost basis. Trailing stop (chandelier) **$22.88** —
price is only **~0.7% above it**, down sharply from ~18.4% headroom last run.
**This is the number to watch, not the return.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — no stated reward:risk or thesis in the holding file |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL again** — industry classified `Capital Markets`; core business fails the screen (3rd consecutive run flagging this) |
| DCF intrinsic value | $0.72 vs. $23.05 price -> -96.9% (not a meaningful signal — see caveat below) |
| Trailing stop (chandelier) | $22.8832 — price ~0.7% above it |
| 6m momentum (skip last month) | -14.3% |
| Would buy today? | Mechanically yes per recommend.py's gates — that check only reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A close/break of the $22.88 trailing stop, or a Zoya/Musaffa business-activity re-screen |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$137.22**, **+19.3%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — recommend.py can't self-assess without a stated thesis-vs-price edge |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $137.19 price -> -12.4% (richer to the model than last run's -6.6%) |
| Trailing stop (chandelier) | $130.91 — price is ~4.8% above it |
| 6m momentum (skip last month) | +3.8% (turned positive since last run's -5.3%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $23.06 | 10 | $15.43 | $230.60 | +49.5% | 19.4% |
| NOW | $137.22 | 7 | $114.97 | $960.54 | +19.3% | 80.6% |

**Total value: $1,191.14** | Cost: $959.09 | **Total return: ~+24.2%** (+$232.05 unrealised)

Both positions are up since the last report and the book remains
NOW-concentrated (80.6%), unchanged in structure.

## Action flags (priority order)

1. **[Technical — new this run] BMNR is ~0.7% above its trailing stop
   ($22.88 vs. $23.06 live)**, down from ~18.4% headroom on 2026-08-19. The
   6-month momentum reading is also negative (-14.3%) and the stock recently
   pulled back (~$22.89, -2.1% on a session) as investors rotated out of
   crypto-treasury names generally, even as BitMine keeps buying ETH weekly
   (65th consecutive weekly purchase disclosed ~Sept 1, ~5.9M ETH held, ~5%
   of circulating supply, $15.6B total crypto+cash). `trade_type: core`
   means TRAIL_STOP doesn't mechanically fire on this position, but the
   price/stop gap has compressed enough that it's worth your own attention
   regardless of what the rule engine does.
   [PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)
2. **[Mandate — still open, 3rd run] BMNR's mechanical Shariah ratio
   pre-check still FAILS** on the same `industry 'Capital Markets'` flag
   first raised 2026-08-19. Recorded status remains `compliant` (screened
   2026-07-07); the gap between recorded and mechanical status has not been
   resolved. As before: `recommend.py`'s "would buy today" check only reads
   the recorded field and stays silent on this. This is now the
   longest-running open compliance question in the book.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
4. **[DCF caveat / BMNR]** The -96.9% DCF "downside" is still not a
   meaningful signal — the cash-flow model doesn't fit a crypto-treasury
   business valued on ETH holdings/staking yield, not discounted operating
   cash flow. Treat as a data gap, not a valuation call.
5. **[Catalyst / NOW — window changed]** Next earnings ~2026-10-28 is now
   **56 days out — inside** the 60-day `catalyst_horizon_days` window (was
   72 days/outside last run). Citi's 2026 Global TMT Conference on 2026-09-09
   is a nearer soft catalyst. [TipRanks](https://www.tipranks.com/stocks/now/earnings)
6. **[Discovery] 55 leads this run, 17 cleared to LEAD tier** (up from 9
   last run) — full list in `leads.md`. **PLTR** and the recurring
   precious-metals cluster (CDE, AR, AGI, IAG, KGC, EGO) carry over again
   with their unresolved business-activity questions from prior runs;
   nothing new to add there.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues its weekly ETH accumulation
program uninterrupted — 65th consecutive weekly purchase (~53,501 ETH,
~$131M) disclosed around Sept 1, pushing total ETH holdings to ~5.9M tokens
(~5% of supply) and total crypto+cash to ~$15.6B, part of the stated
"Alchemy of 5%" plan. Stock still up +49.5% vs. cost basis. Recorded
compliance status remains "compliant."
[PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)

**Case to flag:** Two independent things degraded this run: (1) the
technical cushion to the trailing stop has nearly vanished (~18.4% ->
~0.7%), and (2) the mechanical Shariah ratio pre-check has now failed three
runs running without resolution. The holding file is still missing
`thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`, and
`pre_mortem` — there is no PM-grade record to weigh either issue against.

**Verdict: HOLD (no technical rule fired) — but with the stop this close and
the compliance question still open, this is the position most worth a
deliberate, near-term decision rather than passive holding.**

### NOW — ServiceNow, Inc
**Case to keep:** 6-month momentum turned positive (+3.8%, was -5.3% last
run); DCF gap to price widened only to -12.4%, still not extreme. Business
narrative (AI ACV growth, Armis integration) is unchanged since last run,
with no fresh negative news found this cycle.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; earnings (~Oct 28)
have now rolled inside the 60-day catalyst window, and Citi's TMT conference
on Sept 9 is a nearer, softer catalyst to watch for guidance commentary.
[TipRanks](https://www.tipranks.com/stocks/now/earnings)

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (`compliant`), so it stays silent
  despite three straight runs of ratio-precheck failures. Nothing in the
  automated pipeline will re-flag this on its own — the follow-up is still on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT mechanically fire for either
  (`trade_type: core` exempts both) — but note BMNR's live price is now
  within ~0.7% of its computed chandelier stop regardless of the rule being exempt.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $23.05 | -96.9% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $137.19 | -12.4% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been reviewed
and flipped to `status: planned` yet; all cards in `setups/` remain `draft`).

## Draft & planned setups — 55 leads, 13 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`**.
`scaffold.py --all-leads` auto-filled DRAFT `setups/<ticker>.md` cards for
leads without one (TS, HBM, TECK, BLSH, PAAS, SMCIP, XOM, SMTC, FLYW, BBY,
ASND, AAPL, NTNX, APA, PR, NTR — 13 scaffolded, 3 of those without a card had
no earnings date found and used a fallback setup type). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never buys.**

17 of the 55 leads cleared to LEAD tier this run (up from 9 last run):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| GWRE | LEAD | existing | 10.0:1 | earnings 2026-09-03 | 1 |
| ZS | LEAD | existing | 12.8:1 | earnings 2026-09-03 | 1 |
| SNX | LEAD | existing | 8.9:1 | earnings 2026-09-24 | 22 |
| AGI | LEAD | existing | 11.9:1 | earnings 2026-10-28 | 56 |
| MU | LEAD | existing | 5.0:1 | earnings 2026-09-30 | 28 |
| AA | LEAD | existing | 7.9:1 | earnings 2026-10-15 | 43 |
| ARW | LEAD | existing | 7.0:1 | earnings 2026-10-29 | 57 |
| HBM | LEAD | new | 7.5:1 | earnings 2026-10-29 | 57 |
| HAS | LEAD | existing | 6.4:1 | earnings 2026-10-22 | 50 |
| MSFT | LEAD | existing | 5.5:1 | earnings 2026-10-28 | 56 |
| TSLA | LEAD | existing | 5.6:1 | earnings 2026-10-21 | 49 |
| SIMO | LEAD | existing | 5.5:1 | earnings 2026-10-29 | 57 |
| TECK | LEAD | new | 5.1:1 | earnings 2026-10-22 | 50 |
| APH | LEAD | existing | 5.4:1 | earnings 2026-10-28 | 56 |
| EGO | LEAD | existing | 4.4:1 | earnings 2026-10-29 | 57 |
| GDDY | LEAD | existing | 3.5:1 | earnings 2026-10-29 | 57 |
| AVT | LEAD | existing | 4.2:1 | earnings 2026-10-28 | 56 |

All 55 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again with its unresolved government/defense
  business-activity question from prior runs. Nothing new to add.
- **CDE, AR, AGI, IAG, KGC, EGO** — the recurring precious-metals/mining
  cluster; mining-royalty financing structures raised the same open question
  in earlier runs. Still worth a real screen before spending review time on
  any of these cards.
- **38 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — escalated this run] BMNR trailing-stop cushion has nearly
   closed** (~18.4% -> ~0.7% headroom in two weeks). Combined with the still
   unresolved compliance flag (#2 below), this is the position that most
   needs a deliberate decision this cycle rather than default HOLD.
2. **[Urgent — still open, 3rd run] BMNR Shariah re-screen**: the mechanical
   ratio pre-check disagrees with the recorded "compliant" status on the
   business-activity question, unchanged for three consecutive runs. Per
   this repo's Gate 1, a confirmed fail would be a hard SELL regardless of
   return. The automated pipeline will NOT re-surface this on its own.
3. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, seven weeks after
   the position was opened.
4. **[Time-boxed] NOW earnings ~2026-10-28** — now inside the 60-day
   catalyst window (56 days out); Citi TMT conference 2026-09-09 is a nearer
   soft catalyst to watch.
5. **[Housekeeping] 13 new DRAFT setup cards** added this run (`leads.md`
   has 55 rows, 17 LEAD-tier); none are `planned`. Review at your own pace.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.82 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html)
- [Bitmine Immersion Technologies (BMNR) Ethereum Holdings — The Block](https://www.theblock.co/treasuries/bmnr)
- [ServiceNow (NOW) Earnings Dates, Call Summary & Reports — TipRanks](https://www.tipranks.com/stocks/now/earnings)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
