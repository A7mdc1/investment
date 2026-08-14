# Portfolio Assessment — 2026-08-14

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank — widened
from 20 last commit) → `scaffold.py --all-leads` (34 new DRAFT setup cards
auto-filled for leads without one; 15 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live, no data gaps this run. `journal.py` not run
separately — `transactions.csv` is intentionally gitignored and isn't present
in this environment, so the discipline guard stays dormant. This is also the
first assessment since the FIG→BMNR swap on 2026-07-13 (previous report was
2026-07-13, 32 days ago).

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$18.07**,
**+17.1%** vs. the $15.43 cost basis (10 shares, opened 2026-07-13).

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-8.0:1** (DCF-implied skew argues strongly against adding) |
| Shariah | recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see the ratio pre-check flag below** |
| DCF intrinsic value | **$0.72** vs. $18.07 price -> **-96.0%** (see caveat — DCF is a poor fit for this business) |
| Trailing stop (chandelier) | $15.9086 — price ~13.6% above it |
| 6m momentum (skip last month) | -21.8% |
| Portfolio note | **ATR 6.26% > 6% throttle — size down per vol throttle if adding** |
| Would buy today? | Mechanically yes per recommend.py's gate check; conviction stays LOW absent a stated variant view |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$125.03**, **+8.8%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.3:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.12** vs. $125.06 price -> **-3.9%** (price now slightly rich to the model, vs. +6.9% upside last run) |
| Trailing stop (chandelier) | $109.8232 — price is $15.23 above it |
| 6m momentum (skip last month) | +0.7% (first positive 6m momentum reading since tracking began) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules (`max_position_pct` 22%)
  stay muted until >= 4 names, even though NOW alone is 82.9% of the book.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $18.07 | 10 | $15.43 | $180.70 | +17.1% | 17.1% |
| NOW | $125.03 | 7 | $114.97 | $875.21 | +8.8% | 82.9% |

**Total value: $1,055.91** | Cost: $959.09 | **Total return: ~+10.1%** (+$96.82 unrealised)

Since the last report (2026-07-13), FIG was closed (sold all 35 shares
@$23.00, realized +$54.95, resolving the 7-run compliance flag) and BMNR was
opened. NOW is up +11.0% over the 32-day gap (from $112.72 to $125.03) and
has turned 6m-momentum positive for the first time; BMNR is up +17.1% since
entry a month ago. The book is now concentrated almost entirely in one name
(NOW, 82.9%) — a structural point worth noting even though the muted
concentration rule doesn't fire on a 2-name book.

## Action flags (priority order)

1. **[Mandate] BMNR ratio pre-check flag — new this run.** The recorded
   Shariah status is "compliant" (broker app, screened 2026-07-07), but the
   mechanical ratio pre-check in this run's `shariah.py` output flags
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. Two things have also changed materially since the
   2026-07-07 screen: BMNR has scaled ETH staking sharply (5.07M of 5.81M
   ETH now staked, ~$9.8B, targeting nearly all remaining unstaked ETH,
   projected $291M/yr in staking rewards) and it launched a preferred-stock
   listing (BMNP). A yield-bearing staking business at this scale is a
   different profile than a simple crypto-treasury holding company, and
   yield/staking-reward mechanics are exactly the kind of change that can
   move a name from clean to flagged on an AAOIFI-style screen. This is
   worth an actual re-screen in Zoya/Musaffa before adding to the position —
   the broker-app record is over five weeks old and predates the staking
   scale-up. [Musaffa](https://musaffa.com/stock/BMNR/) currently shows BMNR
   compliant as of its Q3 2025 report — also predating the staking scale-up.
2. **[Valuation / NOW] P/E ~119 (recorded)** — still rich; VALUATION_RICH
   holds, unchanged from last run. Do not add.
3. **[DCF / BMNR] DCF model is not a good fit here — treat the -96% figure
   as a methodology mismatch, not a signal.** `dcf.py` runs a standard
   discounted-cash-flow off BMNR's operating financials (mining/hosting
   revenue), but BMNR's actual balance-sheet value today is dominated by
   ~$11.6B in ETH + BTC + equity-stake holdings, which a cash-flow DCF
   doesn't capture. Don't read $0.72 "intrinsic value" as a real target —
   flagging so it isn't mistaken for a signal.
4. **[DCF / NOW] Price now $5 above intrinsic value ($125.06 vs. $120.12,
   -3.9%)** — flipped from +6.9% upside last run purely on the price move
   since 2026-07-13 (assumptions unchanged: 18% 5y growth, 10% discount).
5. **[Catalyst / NOW] Q2 FY2026 earnings already reported 2026-07-22 (beat:
   revenue $3.99B, +24% y/y; subscription rev $3.877B, +24.5% y/y; AI ACV
   crossed $1B) — next catalyst is Q3 FY2026 earnings, 2026-10-28, 75 days
   out.** The holding's front-matter `catalyst.date` is still null and
   pointed at the now-past Q2 print — worth updating to the Q3 date so
   `dead_money_days`/`verdict.py` logic has something current to work off.
6. **[Housekeeping] 34 fresh DRAFT setup cards this run** (from a widened
   50-name discovery pool, up from 20) — see the table below; none are
   `planned` and none can reach BUY-CANDIDATE yet.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** Largest public corporate Ethereum holder (5.81M ETH, ~4.8%
of total supply), total crypto+cash holdings of $11.6B as of 2026-08-10.
Active $4B buyback already repurchased >19M shares since July 2026. Position
is up +17.1% since entry a month ago; 6m momentum is negative (-21.8%) but
that reflects ETH's broader drawdown, not company-specific news.
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-81-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-6-billion-302846858.html)

**Case to trim / re-screen:** The ratio pre-check flag above (Capital Markets
industry classification) plus the recent scale-up into ETH staking (target:
nearly all remaining ~740K unstaked ETH, ~$291M/yr projected reward income)
is a real change to the business since the 2026-07-07 screen — staking
rewards function economically like a yield stream, which is precisely the
kind of thing Zoya/Musaffa's business-activity and ratio tests are built to
catch. The DCF's -96% reading is not usable here (see flag #3) — this is a
compliance question, not a valuation one, and it's the first thing to
resolve before considering adding.

**No verdict rule fired this run (HOLD by default)** — position is thesis-new
(opened last cycle) with no stop breach, no thesis_broken flag, and no
compliance change recorded in the front-matter yet. The ratio pre-check flag
above is new information the front-matter doesn't reflect.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 beat on both lines (revenue +24% y/y, subscription
+24.5% y/y), AI annual contract value crossed $1B with agentic AI deployments
up 9x in nine months. 6m momentum turned positive (+0.7%) for the first time
since this report started tracking it. Price is comfortably above the
chandelier trailing stop ($125.03 vs. $109.82).
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to trim / watch:** P/E ~119 still VALUATION_RICH (unchanged rule).
DCF flipped slightly negative (-3.9%) purely on the price rally since last
report — model assumptions haven't moved. Reuters/Yahoo coverage separately
notes NOW shares are still down materially year-to-date despite the Q2 beat,
a reminder the stock has been volatile around a rich multiple. Q3 FY2026
earnings land 2026-10-28 (guided ~20.5% y/y subscription growth, 31%
non-GAAP operating margin, with an FX headwind flagged) — 75 days out, so no
near-term binary event between now and then.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add (unchanged from last run).
- **VOL_THROTTLE note -> BMNR**: ATR 6.26% > 6% — size down if adding to this
  position; not a trim signal on its own.
- **DRAWDOWN_REVIEW not firing** on either name (both positions are gains, not
  drawdowns).
- **TRAIL_STOP -> both**: `trade_type: core` on NOW exempts it from the
  technical trailing-stop rule; BMNR has no `trade_type` set in front-matter
  (defaults to core) — worth confirming that's intentional given BMNR's
  6.26% daily ATR is meaningfully more volatile than a typical core holding.
- **CONCENTRATION not firing**: `min_names_for_concentration` (4) exempts a
  2-name book, but NOW alone is 82.9% of value — a structural fact the rule
  engine is silent on, not the same as the rule clearing it.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $18.07 | -96.0% | growth_5y 5%, terminal 2.5%, discount 10% — **poor model fit, see flag #3** |
| NOW | $120.12 | $125.06 | -3.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 entries** (it only evaluates `watchlist.md` names, which is
empty) and **0 BUY-CANDIDATEs** — expected, since no card has been reviewed
and flipped to `status: planned` yet. All new-idea surfacing this cycle comes
from machine discovery below instead.

## Draft & planned setups — 50 leads, 34 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, now sized to
50 names per the last commit) and wrote **`leads.md`**. `scaffold.py
--all-leads` auto-filled a DRAFT `setups/<ticker>.md` card for every lead
that didn't already have one (15 existing cards left unchanged: RCL, CF, ZS,
GDDY, ADI, ALAB, CRDO, MU, KLIC, AR, CDE, AU, PAY, SIMO, PLTR; 34 new DRAFT
cards written). **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.** None can reach BUY-CANDIDATE
until you review the card, edit anything you disagree with, set `status:
planned`, and screen the name compliant in Zoya/Musaffa.

Top 20 by max-benefit rank:

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| AVGO | LEAD | new | 11.0:1 | earnings 2026-09-02 | 19 |
| RCL | RESEARCH | existing | 10.4:1 | earnings 2026-10-27 | 74 |
| PAAS | RESEARCH | new | 20.0:1 | earnings 2026-11-16 | 94 |
| AA | RESEARCH | new | 19.4:1 | earnings 2026-10-15 | 62 |
| DLO | RESEARCH | new | 8.7:1 | earnings 2026-11-11 | 89 |
| CF | RESEARCH | existing | 9.1:1 | earnings 2026-11-04 | 82 |
| AMKR | RESEARCH | new | 15.7:1 | earnings 2026-10-26 | 73 |
| CORZ | RESEARCH | new | 11.6:1 | earnings 2026-10-23 | 70 |
| GWRE | LEAD | new | 4.8:1 | earnings 2026-09-03 | 20 |
| ZS | LEAD | existing | 4.6:1 | earnings 2026-09-03 | 20 |
| DELL | RESEARCH | new | 0.3:1 | earnings 2026-09-03 | 20 |
| GDDY | RESEARCH | existing | 7.2:1 | earnings 2026-10-29 | 76 |
| CIEN | LEAD | new | 4.1:1 | earnings 2026-09-03 | 20 |
| ADI | RESEARCH | existing | 2.5:1 | earnings 2026-08-19 | 5 |
| ALAB | RESEARCH | existing | 4.5:1 | earnings 2026-11-03 | 81 |
| CRDO | RESEARCH | existing | 1.6:1 | earnings 2026-09-01 | 18 |
| FN | RESEARCH | new | 1.9:1 | earnings 2026-08-17 | 3 |
| SNX | LEAD | new | 3.2:1 | earnings 2026-09-24 | 41 |
| MKSI | RESEARCH | new | 5.6:1 | earnings 2026-11-04 | 82 |
| DDOG | RESEARCH | new | 3.6:1 | earnings 2026-11-05 | 83 |

All 50 cleared the liquidity floor and a clean ratio pre-check on their new
DRAFT cards (all read "pre-check: business OK, ratios OK — verify in
Zoya/Musaffa") — that's a mechanical ratio/business-name pass, not a real
Zoya/Musaffa screen, and every card is `status: unverified` by construction.

**Flags worth your attention before reviewing any of these:**
- **PAAS, AGI, KGC, TECK, AEM, IAG, EGO (mining/royalty names, several new
  this run)** — precious-metals and diversified miners with royalty/streaming
  or conventional-financing structures have tripped business-activity
  questions in past runs' hand-review even when the automated ratio
  pre-check is clean; worth the same scrutiny here before spending review
  time on the cards.
- **AVGO, XOM (SPUS-holding LEADs)** — "SPUS holds it" is informative, not a
  substitute for the actual screen; XOM's conventional-financing exposure
  and AVGO's software/licensing mix are the specific things to check.
- **DELL (RESEARCH, R:R 0.3:1 despite a score of 75.1)** — a reminder the
  mechanical score and the asymmetry gate are independent; a high signal
  score with a compressed stop-to-target band still caps at RESEARCH.
- **FN (3 days to catalyst)** — nearest earnings date in the top 20
  (2026-08-17); if this is on your radar, the setup card review window is
  short.

## Follow-ups (priority order)

1. **[New, needs attention] BMNR ratio pre-check flag + staking scale-up** —
   re-screen in Zoya/Musaffa given the business has materially shifted
   toward active ETH staking since the 2026-07-07 recorded screen. See
   Action flag #1.
2. **[Housekeeping] NOW catalyst date is stale** — front-matter still points
   at the now-past 2026-07-22 Q2 print; update to 2026-10-28 (Q3 FY2026) so
   verdict/recommend logic has a live date.
3. **[Ongoing] 34 new DRAFT setup cards** added this run (50 total leads,
   several with catalysts inside the next 2-3 weeks — ADI (5d), FN (3d),
   CRDO/AVGO/GWRE/ZS/DELL/CIEN (18-20d)). Review at your own pace; nothing
   here can reach BUY-CANDIDATE without your review + a real Zoya/Musaffa
   screen.
4. **[Structural] Concentration** — NOW is 82.9% of a 2-name book. The
   `min_names_for_concentration` rule stays silent until you have 4+
   holdings, but that's a policy choice worth revisiting given how top-heavy
   the book actually is today.
5. **[Infrastructure — still open]** No ledger present in this environment
   (`transactions.csv` is gitignored by design) — the discipline guard stays
   dormant until trades are logged via `/apply-trade` in your own working
   copy.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.81 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-81-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-6-billion-302846858.html)
- [Is Bitmine Immersion Technologies (BMNR) Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow (NOW) Earnings Report Q2 2026 — 24/7 Wall St.](https://247wallst.com/companies/now/earnings/)
