# Portfolio Assessment — 2026-07-27

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data; `discover_top_n` was bumped 20 -> 50 last run,
so this is the first cycle with the wider 50-name pool) -> `scaffold.py
--all-leads` (28 new DRAFT setup cards auto-filled for leads without one; 22
existing cards left unchanged) -> `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps this
run. `journal.py` not run separately — still 0 closed trades logged
(no `transactions.csv` yet — discipline guard stays dormant until you start
logging via `/apply-trade`).

Since the last assessment (2026-07-13) the book changed: **FIG was sold**
(closed 2026-07-13, +$54.95 realized, compliance-driven exit) and **BMNR
(Bitmine Immersion Technologies) was bought** — a new, thinly-documented
position that raises its own compliance question below.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$17.49**, up
**+13.4%** vs. the $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -6.3:1 (DCF target below price; see DCF caveat below) |
| Shariah | Broker app: PASS (compliant, screened 2026-07-07, not stale) — **but see ratio pre-check flag** |
| DCF intrinsic value | **$0.72** vs. $17.49 price -> **-95.9%** — **not a meaningful read for this business; see caveat** |
| Trailing stop (chandelier) | $14.85 — price ~17.7% above it |
| 6m momentum (skip last month) | -53.7% (reflects the underlying stock's longer history, not your ~3-week hold) |
| Portfolio note | ATR 6.46% — vol-throttle: size down, this is a volatile name |
| Would buy today? | Mechanically "yes" per recommend.py's gates; conviction flagged LOW absent your own stated edge — **and no thesis fields are filled in at all** |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$106.44**, **-7.4%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk 1.25:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.12** vs. $106.44 price -> **+12.8% upside** to the model |
| Trailing stop (chandelier) | $95.42 — price is $11.02 above it |
| 6m momentum (skip last month) | -32.7% (worse than last run's -27.5%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules (`max_position_pct`
  22%) are structurally muted until >= 4 names, even though NOW alone is now
  **81% of the book** (see Action flag #4).

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $17.49 | 10 | $15.43 | $174.90 | +13.4% | 19.0% |
| NOW | $106.44 | 7 | $114.97 | $745.08 | -7.4% | 81.0% |

**Total value: ~$920.47** | Cost: $959.09 | **Total return: ~-4.0%** (-$38.62
unrealised, before the +$54.95 FIG already realized this cycle).

## Action flags (priority order)

1. **[Mandate — new this run] BMNR ratio pre-check flags a business-activity
   conflict.** The mechanical pre-check classifies BMNR's industry as
   **"Capital Markets"** and notes "core business fails screen" — while the
   broker app's recorded screen says `compliant` (2026-07-07). This is the
   same *shape* of conflict that took seven runs to resolve with FIG (recorded
   status vs. mechanical flag disagreeing), so flagging it immediately rather
   than letting it season. Context that cuts both ways: BMNR isn't an
   operating "capital markets" firm in the traditional sense — it's an
   Ethereum treasury/staking vehicle (5.79M ETH, ~$11.8B combined crypto+cash
   as of 2026-07-26), and a third-party screener (Musaffa) currently lists it
   halal-compliant. But a levered digital-asset-treasury model with staking
   income is exactly the kind of structure where "compliant per one source,
   flagged per another" deserves your own re-verification in Zoya/Musaffa
   before this grows further, not an assumption that the broker's screen
   settles it.
2. **[Data completeness] BMNR's holding file has no PM-grade fields filled
   in** — `conviction`, `thesis_one_liner`, `variant_view`, `catalyst`,
   `initial_stop`, `target_price`, `invalidation`, `pre_mortem` are all
   absent (the file only has ticker/shares/cost/currency/shariah). This is
   the same gap NOW had four cycles ago — worth closing before the position
   grows, since right now there's no engineered stop or target driving the
   -6.3:1 "reward:risk" other than a DCF number that doesn't fit this
   business (see #3).
3. **[DCF / BMNR] The intrinsic-value read is not meaningful for this name.**
   BMNR's holding file has no `dcf:` block, so `dcf.py` fell back to generic
   defaults (5% growth, 2.5% terminal, 10% discount) built for an
   operating-cash-flow business. BMNR's value driver is its ETH treasury +
   staking yield, not discounted free cash flow — the resulting "$0.72
   intrinsic value / -95.9% downside" is a formula artifact, not a signal.
   Either supply treasury-appropriate assumptions or treat this field as N/A
   for BMNR.
4. **[Concentration, structural] NOW is 81% of a 2-name book.** The
   `max_position_pct` (22%) rule would ordinarily fire TRIM at this weight,
   but `min_names_for_concentration: 4` mutes it entirely below four
   holdings — so the rule stays silent regardless of how concentrated the
   book actually is. Flagging again (same open policy question as last run):
   worth deciding whether that threshold should apply differently to a
   small, non-diversified book.
5. **[Valuation / NOW] P/E ~119 (recorded)** — still VALUATION_RICH; do not add.
6. **[Catalyst data is stale / NOW]** The holding file's catalyst still reads
   "Q2 FY2026 earnings + Armis integration progress" with `date: null` —
   **that earnings report already happened on 2026-07-22**, 5 days before
   this run. Worth updating the field to the next dated catalyst (Q3 FY2026
   earnings, not yet announced) so the card doesn't point at a stale event.
7. **[New leads pool tripled]** `discover_top_n` moved 20 -> 50 last cycle;
   this is the first run reflecting that — 50 leads now in `leads.md` (27
   LEAD-grade, 23 capped at RESEARCH), vs. 20 last time. See the full table
   below.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep:** Up +13.4% since the 2026-07-07 buy. Ethereum treasury
continues to scale — 5.79M ETH staked/held, ~$11.8B combined crypto+cash
holdings as of 2026-07-26, with ~4.92M ETH already staked via its MAVAN
platform (projected annualized staking revenue ~$235-284M). Added to the
Russell 1000 (more institutional visibility/liquidity). Company has executed
the largest-ever common-stock buyback among ETH/BTC digital-asset-treasury
peers (11M+ shares repurchased). [PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-79-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-8-billion-302834876.html) ·
[TimothySykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20-2/)

**Case to review:** The ratio pre-check's "Capital Markets" business flag
(Action flag #1) is the central open question — independent of price. B.
Riley cut its price target to $25 from $33 (still Buy-rated) citing "ETH
sensitivity and capital structure changes." ATR 6.46% marks this as a
genuinely volatile name (vol-throttle note). No thesis/stop/target fields
are filled in on the holding file, so there's no written answer yet to "what
would make me sell this."

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 (reported 2026-07-22) **beat** on both lines —
EPS $0.90 vs. ~$0.76 expected (+18%), subscription revenue $3,877M (+24.5%
y/y, 23% cc), cRPO $13.20B (+21% y/y), operating margin 29.5% (3pts above
guide), 123 deals >$1M net-new ACV (+~40% y/y). ServiceNow AI crossed **$1B**
in ACV. Full-year subscription guidance was **raised** to $15.76-15.78B (from
$15.53-15.57B). DCF still shows +12.8% upside to intrinsic value ($120.12) at
the recorded assumptions. Stock has recovered sharply since the print — from
an initial post-earnings low near $91.94 back to $106.44 today, a ~+15%
rebound in ~3-4 trading days.
[ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx) ·
[Benzinga transcript](https://www.benzinga.com/news/26/07/60627210/full-transcript-servicenow-q2-2026-earnings-call)

**Case to trim / watch:** The initial post-earnings drop (-3.7% to $91.94)
was driven by **H2 guidance softness** — initial midpoint estimates put H2
subscription revenue ~$44.5M lower than prior modeling, despite the
full-year raise. P/E ~119 still VALUATION_RICH. 6m momentum -32.7% (worse
than last run's -27.5%). [ts2.tech](https://ts2.tech/en/servicenow-inc-nysenow-shares-drop-3-7-after-2026-outlook-hints-at-weaker-h2/) ·
[24/7 Wall St.](https://247wallst.com/investing/2026/07/22/live-will-servicenows-q2-earnings-tonight-drive-a-rebound-after-38-ytd-decline/liveupdates/8/)

## Suggested actions (from YOUR rules, rules.md)

- **DEFAULT (no rule fired) -> BMNR**: HOLD. No engineered stop/target on
  file yet (see Action flags #2-3) — this is a mechanical default, not an
  endorsement.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **VOL_THROTTLE note -> BMNR**: ATR 6.46% — size down if adding; informational only.
- **Concentration rule (structurally muted) -> NOW at 81% weight**: no rule
  fires because `min_names_for_concentration: 4` and you hold 2 names — flag
  stands regardless (Action flag #4).
- **DRAWDOWN_REVIEW not firing -> NOW**: -7.4% vs. the 20% threshold.
- **TRAIL_STOP -> both**: does NOT fire (`trade_type: core` exempts both from
  the technical trailing-stop rule); both remain above their computed levels.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $17.49 | -95.9% | **defaults (no `dcf:` block on file)** — not a meaningful model for a treasury/staking business; see Action flag #3 |
| NOW | $120.12 | $106.44 | +12.8% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below instead. `recommend.py`'s `ideas`
array returned **0 BUY-CANDIDATEs** this run — expected, since no card has
been reviewed and flipped to `status: planned` yet.

## Draft & planned setups — 50 leads (top 20 shown), 28 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** — now the top **50** by max-benefit rank (widened from 20 last
cycle per the `discover_top_n` change). `scaffold.py --all-leads` auto-filled
a DRAFT `setups/<ticker>.md` card for every lead that didn't already have one
(22 cards existed already and were left unchanged; **28 new DRAFT cards**
written: SMCI, UTHR, AEM, AGI, NVDA, TS, PAAS, KGC, P, AVGO, NEM, DELL, STX,
DINO, GWRE, ARW, SFD, AAPL, WDC, DLO, LLY, AMKR, APH, HAS, FLYW, ESE, BBY —
plus UTHR). **Every DRAFT card is unreviewed and Shariah UNVERIFIED —
proposals to review and edit, never buys.** None can reach BUY-CANDIDATE
until you review the card, edit anything you disagree with, set
`status: planned`, and screen the name compliant in Zoya/Musaffa.

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| SMCI | LEAD | new | 16.6:1 | earnings 2026-08-11 | 15 |
| ALKT | LEAD | existing | 9.9:1 | earnings 2026-07-29 | 2 |
| UTHR | LEAD | new | 9.7:1 | earnings 2026-08-05 | 9 |
| CNQ | LEAD | existing | 8.5:1 | earnings 2026-08-06 | 10 |
| AEM | LEAD | new | 20.0:1 | earnings 2026-07-29 | 2 |
| AGI | LEAD | new | 12.9:1 | earnings 2026-07-29 | 2 |
| LIF | LEAD | existing | 9.8:1 | earnings 2026-08-10 | 14 |
| NVDA | LEAD | new | 10.9:1 | earnings 2026-08-26 | 30 |
| CVE | LEAD | existing | 5.0:1 | earnings 2026-07-29 | 2 |
| TS | LEAD | new | 5.7:1 | earnings 2026-08-05 | 9 |
| PAAS | LEAD | new | 8.1:1 | earnings 2026-08-12 | 16 |
| VRNS | LEAD | existing | 4.4:1 | earnings 2026-07-28 | 1 |
| AU | LEAD | existing | 7.1:1 | earnings 2026-07-31 | 4 |
| AMD | LEAD | existing | 5.3:1 | earnings 2026-08-04 | 8 |
| AR | LEAD | existing | 6.5:1 | earnings 2026-07-29 | 2 |
| CF | LEAD | existing | 5.0:1 | earnings 2026-08-05 | 9 |
| MSFT | LEAD | existing | 5.6:1 | earnings 2026-07-29 | 2 |
| KGC | LEAD | new | 6.3:1 | earnings 2026-07-29 | 2 |
| P | LEAD | new | 7.8:1 | earnings 2026-08-26 | 30 |
| FICO | LEAD | existing | 4.5:1 | earnings 2026-07-29 | 2 |

Full 50-row list (27 LEAD / 23 RESEARCH-capped) is in `leads.md` — not
reproduced in full here to keep this report scannable.

**Flags worth your attention before reviewing any of these:**
- **Gold/silver-miner cluster (AU, AEM, AGI, KGC, NEM, PAAS — 6 of the 50
  leads).** These move on one shared driver (metals prices) — size them as
  ONE correlated bet, not six independent ones, the same way the watchlist
  doc already flags the semiconductor cluster. Royalty/streaming and mining
  finance structures also carry their own Shariah nuance worth checking name
  by name.
- **PLTR, MT** — carried over from prior runs' flags (government/defense
  business-activity question for PLTR; MT's implausibly tight engineered
  entry/stop/target band). Nothing new to add — still open.
- **NVDA / AVGO / AMD (SPUS-holding mega-caps, new or refreshed this run)**
  — clean on the ratio pre-check, but each carries interest-income and
  customer-concentration nuances worth an actual Zoya/Musaffa screen rather
  than assuming "SPUS holds it, so it's fine."
- **TSLA / GOOGL / JNJ** — surfaced as leads last cycle, **absent from the
  top 50 this run** (fell out of the ranked pool; not a compliance or data
  event, just rank movement).

## Follow-ups (priority order)

1. **[New, Action flag #1] BMNR business-activity re-screen** — the ratio
   pre-check's "Capital Markets" flag conflicts with the broker's recorded
   `compliant` status; re-verify in Zoya/Musaffa given the ETH-treasury /
   staking-income structure, rather than letting this season the way FIG's
   conflict did.
2. **[New, Action flags #2-3] Fill in BMNR's PM-grade fields** — conviction,
   thesis, initial stop, target (with a method that actually fits a
   treasury/staking business, not a generic DCF), invalidation, pre-mortem.
3. **[Housekeeping] Update NOW's stale catalyst field** — Q2 FY2026 earnings
   already reported 2026-07-22; point the card at the next dated catalyst.
4. **[Ongoing, structural] Concentration policy** — decide whether
   `min_names_for_concentration: 4` should still fully mute the
   `max_position_pct` rule when one name is 81% of a 2-name book.
5. **[Housekeeping] 28 new DRAFT setup cards** added this run (50 total
   candidates tracked); none are `planned`, none can reach BUY-CANDIDATE.
   Several earnings dates in the pool land within the next 1-2 weeks if you
   want to prioritize review.
6. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [Full Transcript: ServiceNow Q2 2026 Earnings Call — Benzinga](https://www.benzinga.com/news/26/07/60627210/full-transcript-servicenow-q2-2026-earnings-call)
- [ServiceNow Inc. (NYSE:NOW) Shares Drop 3.7% After 2026 Outlook Hints at Weaker H2 — ts2.tech](https://ts2.tech/en/servicenow-inc-nysenow-shares-drop-3-7-after-2026-outlook-hints-at-weaker-h2/)
- [Live: Will ServiceNow's Q2 Earnings Drive a Rebound After 38% YTD Decline? — 24/7 Wall St.](https://247wallst.com/investing/2026/07/22/live-will-servicenows-q2-earnings-tonight-drive-a-rebound-after-38-ytd-decline/liveupdates/8/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.79 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-79-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-8-billion-302834876.html)
- [BMNR Stock Climbs As Massive Ethereum Bet Takes Center Stage — TimothySykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20-2/)
- [Is Bitmine Immersion Technologies Inc - BMNR Stock Halal and Shariah Compliant? — Musaffa](https://musaffa.com/stock/BMNR/)
