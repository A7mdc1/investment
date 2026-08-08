# Portfolio Assessment — 2026-08-08

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, **50-name pool** by max-benefit rank — widened
from 20 since the last assessment) → `scaffold.py --all-leads` (**34 new
DRAFT setup cards** auto-filled for names without one; 16 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
run for completeness — still 0 closed trades (no `transactions.csv` entries
yet; discipline guard stays dormant until you start logging via
`/apply-trade`). This is the first assessment since the portfolio changed:
FIG was sold (compliance exit) and BMNR was opened, both recorded 2026-07-13,
after the last report.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$18.82**, up
**+22.0%** vs. the $15.43 cost basis. First appearance of this holding in an
assessment report.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.9:1 (recommend.py's DCF-based target is not a meaningful model for this business — see DCF note below) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see Action flag #1**: this run's mechanical ratio pre-check flags the business as "Capital Markets," which is a hard knockout category under the standard screen |
| DCF intrinsic value | $0.72 vs. $18.82 price -> -96.2% ("upside") — **not a usable signal here, see note below** |
| Trailing stop (chandelier) | $15.7689 — price ~16.2% above it |
| 6m momentum (skip last month) | -15.6% |
| Portfolio note | ATR 6.25% — vol-throttle note (size down if adding) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW — treat as noise, not a signal, until the compliance question is resolved |
| What changes verdict | Zoya/Musaffa re-screen outcome, thesis_broken flag, or a SELL technical trigger |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50 — **see
Action flag #2, this field looks stale**). Live price **$124.88**, up
**+8.6%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.25:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $124.88 price -> -3.8% (price now slightly rich to the model, vs. +6.9% upside last run — the post-earnings rally outran the DCF) |
| Trailing stop (chandelier) | $105.7745 — price is $19.11 above it |
| 6m momentum (skip last month) | +6.1% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
  BMNR carries a live ATR-based vol-throttle note (6.25%) — informational, not
  a trim trigger on its own.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $18.82 | 10 | $15.43 | $188.20 | +22.0% | 17.7% |
| NOW | $124.88 | 7 | $114.97 | $874.16 | +8.6% | 82.3% |

**Total value: $1,062.36** | Cost: $959.09 | **Total return: ~+10.8%**
(+$103.27 unrealised)

This is the first snapshot with the new composition (BMNR replacing FIG) —
no like-for-like week-over-week comparison to last run is meaningful. NOW is
now the dominant position at 82.3% of the book; there is no concentration
rule enforcing a cap yet because the 4-name minimum for portfolio-level rules
hasn't been met, but a single name at over four-fifths of a 2-position book
is worth being deliberate about regardless of what the mechanical rule says.

## Action flags (priority order)

1. **[Mandate, NEW this run] BMNR business-activity ratio pre-check flag** —
   `shariah.py`'s mechanical pre-check now flags BMNR's industry as
   `Capital Markets`, which matches a hard business-activity knockout
   category on the standard screen. The position is currently recorded
   **compliant** (broker app, screened 2026-07-07), and a third-party
   screener (Musaffa) has separately listed BMNR as Shariah-compliant per
   AAOIFI methodology — but that listing is dated to Bitmine's **Q3 2025**
   report, well before its current, much larger Ethereum-treasury and
   staking business. As of early August 2026 Bitmine is running roughly
   $9.2B of staked ETH generating a reported ~$291M/yr in staking rewards
   plus an active buyback program — a materially different, larger business
   than whatever was last screened. This is a heads-up, not a verdict (per
   convention, ratio pre-checks are not the source of truth), but given the
   business has changed size and shape since the last screen, this is worth
   an actual re-screen in Zoya/Musaffa specifically covering (a) the
   business-activity classification and (b) how each screener treats
   staking-reward income, before treating "compliant" as settled.
2. **[Data hygiene] NOW's recorded `pe: 119.02` (holdings/now-servicenow.md
   front-matter) looks stale.** It is what's driving this run's
   VALUATION_RICH verdict, but it was recorded against `last_price: 106.40`
   and predates the 2026-07-22 Q2 FY2026 print. Independent reporting this
   run puts trailing P/E closer to ~56.8x post-earnings (still above the
   `pe_rich: 50` threshold either way, so the HOLD verdict itself doesn't
   change) — but the recorded figure should be refreshed from a live source
   next time you touch the file so the rule is firing on current data, not a
   six-week-old snapshot. Not fabricating a replacement number here per
   convention; flagging the gap instead.
3. **[Catalyst / NOW, resolved] Q2 FY2026 earnings reported 2026-07-22** —
   beat: subscription revenue $3,877M (+24.5% y/y) vs. prior guide, non-GAAP
   EPS $0.90 vs. $0.86 consensus, AI ACV crossed $1B. FY2026 subscription
   guidance raised to $15,760-15,780M. Next catalyst: Q3 FY2026 earnings,
   reported around **2026-10-28/11-04** (sources differ by about a week) —
   roughly 12-13 weeks out, not yet inside a near-term watch window.
4. **[Risk / NOW] Margin compression flagged post-earnings** — TTM net
   margin fell to 11.3% (from 13.8%), basic EPS growth slowed to ~0.5% y/y
   (vs. a ~35.7% historical average), and the stock's premium multiple
   leaves "little room for disappointment" per third-party analysis — a real
   counterpoint to the AI-ACV headline growth, worth weighing against the
   VALUATION_RICH flag rather than in place of it.
5. **[New leads this run, widened pool]** `discover.py`'s pool widened from
   20 to 50 names (a repo change made after the last report, not by this
   run). 34 of the 50 leads got a fresh DRAFT setup card this run; see the
   table below. Nothing here is reviewed or Shariah-verified.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** the position is up +22.0% since the 2026-07-13 entry.
Bitmine has become one of the largest corporate Ethereum treasuries in the
market — as of early August 2026 it reports ~5.8M ETH plus BTC and other
holdings worth a combined ~$11.3B, is running an active staking program
generating a reported ~$291M/yr, and has been buying back stock (4.5M shares
under a $4B program). None of that is a Shariah verdict — it's the
fundamental momentum behind the +22% move.
[PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-8-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302840749.html) ·
[TimothySykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20-2/)

**Case to trim / re-underwrite:** the compliance picture is less settled than
the recorded status suggests (Action flag #1) — a business that has pivoted
hard toward large-scale ETH staking for yield is exactly the kind of
business-model shift that should trigger a fresh screen, not a reliance on a
stale one. Separately, the DCF model here is not fit for purpose: a
cash-flow-growth DCF built for an operating business produces an "intrinsic
value" of $0.72 against an $18.82 price for a company whose balance sheet is
dominated by ~$11.3B of held crypto assets — the model isn't pricing the
treasury, so the -96% "downside" reads as a data artifact, not a real
signal. Ignore it until (or unless) the DCF assumptions get reworked for an
asset-holding-company model.

**Verdict: HOLD (no rule fired)** — but the honest state of this position is
"HOLD pending re-screen," not "HOLD, settled." The trailing stop ($15.77) and
+22% cushion give room to wait for the Zoya/Musaffa answer before deciding
anything else.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 print beat on both revenue and EPS, AI annual
contract value crossed $1B (agentic AI deployments up 9x in nine months),
123 deals over $1M in net-new ACV (+~40% y/y), and FY2026 guidance was
raised. Momentum (6m, skip last month) turned positive at +6.1% (from -27.5%
last run) and price is now comfortably clear of the trailing stop.
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html)

**Case to trim / watch closely:** VALUATION_RICH still fires (Action flag
#2), and independent margin analysis flags TTM net margin compression (13.8%
-> 11.3%) alongside EPS growth slowing to ~0.5% y/y against a much higher
historical average — "a high multiple on top of a lower margin leaves little
room for disappointment," per one analysis. That's a real tension against
the AI-ACV growth headline, not a reason on its own to act.
[Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/servicenow-now-stock-faces-margin-concerns-as-q2-eps-trails)

**Verdict: HOLD (VALUATION_RICH, recorded P/E) — do not add.** Next earnings
~12-13 weeks out; nothing time-boxed before then beyond routine monitoring.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add. (Recorded P/E input is
  stale — refresh it; the verdict itself likely doesn't change since even the
  fresher ~56.8x figure clears `pe_rich: 50`.)
- **No rule fired -> BMNR**: mechanical HOLD, but treat as provisional given
  the new compliance flag (Action flag #1) — this is a policy question for
  you to resolve, not something signals.py/verdict.py currently gate on
  (they only read the recorded `shariah.status` field, not the ratio
  pre-check).
- **VOL_THROTTLE note -> BMNR**: ATR 6.25% — size down if you add to this
  position; informational only at current size.
- **DRAWDOWN_REVIEW not firing** on either name (both are gains, not
  drawdowns).
- **CONCENTRATION not firing**: rule is muted below 4 holdings, but NOW alone
  is 82.3% of a 2-name book — worth a deliberate look even though no
  mechanical rule forces the question yet.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $18.82 | -96.2% | growth_5y 5%, terminal 2.5%, discount 10% — **not a meaningful model for an asset-holding treasury company; disregard until reworked** |
| NOW | $120.12 | $124.88 | -3.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run — expected, since no card has
been reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 50 leads, 34 fresh DRAFT cards this run

`discover.py`'s pool widened to 50 names since the last report (SPUS
holdings + `growth_technology_stocks` / `undervalued_large_caps` screens).
`scaffold.py --all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for
every lead that didn't already have one (16 cards — ALAB, LIF, KLIC, SIMO,
CVE, MU, ZS, CRDO, GOOGL, ADI, AMD, CDE, PLTR, AU, TER, PAY — already existed
and were left unchanged; 34 new DRAFT cards written this run). **Every DRAFT
card is unreviewed and Shariah UNVERIFIED — proposals to review and edit,
never buys.** None can reach BUY-CANDIDATE until you review the card, edit
anything you disagree with, set `status: planned`, and screen the name
compliant in Zoya/Musaffa. Sorted by discovery rank (highest max-benefit first):

| Ticker | Verdict (leads.md) | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| CIEN | LEAD | new | 14.6:1 | earnings 2026-09-03 | 26 |
| ALAB | RESEARCH | existing | 9.4:1 | earnings 2026-11-03 | 87 |
| DLO | LEAD | new | 6.3:1 | earnings 2026-08-13 | 5 |
| LIF | LEAD | existing | 4.0:1 | earnings 2026-08-10 | 2 |
| KLIC | RESEARCH | existing | 11.2:1 | earnings 2026-11-18 | 102 |
| LRCX | RESEARCH | new | 8.4:1 | earnings 2026-10-21 | 74 |
| SMCI | LEAD | new | 4.3:1 | earnings 2026-08-11 | 3 |
| SIMO | RESEARCH | existing | 7.1:1 | earnings 2026-10-29 | 82 |
| CVE | RESEARCH | existing | 7.4:1 | earnings 2026-10-29 | 82 |
| GWRE | LEAD | new | 3.5:1 | earnings 2026-09-03 | 26 |
| PR | RESEARCH | new | 7.1:1 | earnings 2026-11-04 | 88 |
| CLS | RESEARCH | new | 7.5:1 | earnings 2026-10-26 | 79 |
| DELL | RESEARCH | new | 0.4:1 | earnings 2026-09-03 | 26 |
| MU | LEAD | existing | 4.5:1 | earnings 2026-09-23 | 46 |
| ZS | LEAD | existing | 3.5:1 | earnings 2026-09-03 | 26 |
| CRDO | RESEARCH | existing | 1.7:1 | earnings 2026-09-02 | 25 |
| SNX | LEAD | new | 4.4:1 | earnings 2026-09-24 | 47 |
| GOOGL | RESEARCH | existing | 6.5:1 | earnings 2026-10-28 | 81 |
| DOCN | RESEARCH | new | 5.9:1 | earnings 2026-11-04 | 88 |
| FN | RESEARCH | new | 2.0:1 | earnings 2026-08-17 | 9 |
| ADI | RESEARCH | existing | 1.8:1 | earnings 2026-08-19 | 11 |
| KEYS | RESEARCH | new | 1.0:1 | earnings 2026-08-18 | 10 |
| AMD | RESEARCH | existing | 4.0:1 | earnings 2026-11-03 | 87 |
| XOM | RESEARCH | new | 4.2:1 | earnings 2026-10-30 | 83 |
| IONQ | RESEARCH | new | 4.1:1 | earnings 2026-11-04 | 88 |
| FSLR | RESEARCH | new | 4.1:1 | earnings 2026-10-29 | 82 |
| UTHR | RESEARCH | new | 3.1:1 | earnings 2026-10-28 | 81 |
| CORZ | RESEARCH | new | 5.1:1 | earnings 2026-10-23 | 76 |
| CDE | RESEARCH | existing | 3.6:1 | earnings 2026-10-28 | 81 |
| AVGO | RESEARCH | new | 1.5:1 | earnings 2026-09-02 | 25 |
| NVDA | RESEARCH | new | 0.6:1 | earnings 2026-08-26 | 18 |
| TTMI | RESEARCH | new | 4.3:1 | earnings 2026-11-04 | 88 |
| AEM | RESEARCH | new | 3.9:1 | earnings 2026-10-28 | 81 |
| P | RESEARCH | new | 0.8:1 | earnings 2026-08-26 | 18 |
| AGI | RESEARCH | new | 4.0:1 | earnings 2026-10-28 | 81 |
| KGC | RESEARCH | new | 3.3:1 | earnings 2026-11-10 | 94 |
| AA | RESEARCH | new | 3.8:1 | earnings 2026-10-15 | 68 |
| STX | RESEARCH | new | 2.9:1 | earnings 2026-10-27 | 80 |
| BBY | RESEARCH | new | n/a | earnings 2026-08-27 | 19 |
| PLTR | RESEARCH | existing | 1.4:1 | earnings 2026-11-02 | 86 |
| AU | RESEARCH | existing | 2.8:1 | earnings 2026-11-05 | 89 |
| FOX | RESEARCH | new | 2.5:1 | earnings 2026-10-29 | 82 |
| TER | RESEARCH | existing | 1.8:1 | earnings 2026-10-21 | 74 |
| EXPE | RESEARCH | new | 1.2:1 | earnings 2026-11-05 | 89 |
| HAS | RESEARCH | new | 2.4:1 | earnings 2026-10-22 | 75 |
| JAZZ | RESEARCH | new | 0.6:1 | earnings 2026-11-04 | 88 |
| BKR | RESEARCH | new | 2.2:1 | earnings 2026-10-22 | 75 |
| PAY | RESEARCH | existing | n/a | earnings 2026-11-02 | 86 |
| VLO | RESEARCH | new | 1.6:1 | earnings 2026-10-22 | 75 |
| FLYW | RESEARCH | new | 1.2:1 | earnings 2026-11-03 | 87 |

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction. Only 7 are `LEAD` (CIEN, DLO, LIF, SMCI, GWRE, SNX, MU, ZS —
clear every mechanical gate, catalyst inside the 60-day horizon); the other
43 are `RESEARCH` (asymmetry and/or catalyst-horizon gate not cleared).

**Flags worth your attention before reviewing any of these:**
- **PLTR, AU, CDE** — carried over from prior runs' flags (government/defense
  business-activity question for PLTR; mining/royalty financing structure
  questions for precious-metals names AU/CDE). Nothing new to add — still
  open, still worth checking before spending review time on the cards.
- **LIF, SMCI, DLO** — near-term catalysts (2-5 days out) among this run's
  LEAD names; if any of these interest you, the review-and-screen window is
  short.
- **AA, AGI, AEM, KGC** — a metals/mining cluster (4 of the 50 names); if
  more than one is worth pursuing, size them as one correlated bet per the
  watchlist.md convention, not four independent ones.
- Given BMNR's own fresh business-activity flag (Action flag #1), it's worth
  double-checking any future crypto/treasury-adjacent names that surface
  from this pool with the same scrutiny — the ratio pre-check alone isn't
  catching business-model nuance for this category.

## Follow-ups (priority order)

1. **[New, top priority] BMNR compliance re-screen** — Action flag #1. This
   is now the more pressing mandate question in the book (FIG's prior
   7-run-unresolved flag was closed by selling; don't let this one drift the
   same way). Re-screen in Zoya/Musaffa, specifically checking both the
   business-activity classification and staking-income treatment.
2. **[Housekeeping] Refresh NOW's recorded `pe`/`last_price` front-matter**
   fields from a live source — Action flag #2.
3. **[Ongoing] NOW margin compression vs. AI-ACV growth** — not
   time-boxed, but worth tracking into the Q3 FY2026 print (~Oct 28-Nov 4).
4. **[Housekeeping] 34 new DRAFT setup cards** added this run (50 total
   leads, 64 cards now in `setups/`); none are `planned`, none can reach
   BUY-CANDIDATE. LIF, SMCI, DLO have the nearest catalysts if you want to
   prioritize review.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.8 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-8-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302840749.html)
- [BMNR Stock Climbs As Massive Ethereum Bet Takes Center Stage — TimothySykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20-2/)
- [Is BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow (NOW) Q2 Earnings and Revenues Top Estimates — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/servicenow-now-q2-earnings-revenues-215507399.html)
- [ServiceNow (NOW) Stock Faces Margin Concerns As Q2 EPS Trails Strong Revenue Growth Narratives — Simply Wall St](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/servicenow-now-stock-faces-margin-concerns-as-q2-eps-trails)
- [ServiceNow (NOW) Earnings, Revenues Date & History — TipRanks](https://www.tipranks.com/stocks/now/earnings)
