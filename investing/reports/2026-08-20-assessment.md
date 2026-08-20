# Portfolio Assessment — 2026-08-20

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded screen
or a mechanical ratio/business-activity pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, top 50 kept per `discover_top_n: 50`) →
`scaffold.py --all-leads` (**6 new DRAFT cards**: ASND, EXPE, PR, SMCIP, TECK,
VLO; 44 existing cards left unchanged) → `prices.py` / `shariah.py` / `dcf.py` /
`signals.py` / `verdict.py` / `recommend.py` — all live. `journal.py` ran and
returned 0 closed trades (`transactions.csv` / `journal.csv` are gitignored and
this container is ephemeral, so the ledger is empty every run — the discipline
guard is structurally dormant, not merely under-sampled).

**Data gap this run:** Yahoo rate-limited hard after `discover.py` finished, so
the per-lead ATR cross-check in the "degenerate asymmetry" note below could not
be computed. Stop *distances* are quoted straight from `leads.md`; ATR multiples
are not.

**Since the last report (2026-08-19):** one session. No trades. BMNR $20.54 →
$21.72 (+5.7%), NOW $128.63 → $130.46 (+1.4%). The substantive change is
evidence, not price — the BMNR compliance question moved from news-article
inference to primary SEC filings (Action Flag #1).

## Verdicts (lead with this)

These are your own rules in `rules.md` resolving against live data. Not advice.

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live **$21.72**, **+40.8%** vs.
the $15.43 cost basis. **See Action Flag #1 — the mechanical Shariah
business-activity pre-check fails, for the second run running, and this run's
primary-source research makes the flag harder to dismiss.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.8:1 (DCF target sits below the stop; see DCF caveat) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical pre-check, this run) | **FAIL** — industry `Capital Markets`; core business fails screen |
| DCF intrinsic value | $0.72 vs. $21.72 → -96.7% (**not a meaningful signal** — see caveat) |
| Trailing stop (chandelier) | $18.1258 — price ~16.6% above it |
| 6m momentum (skip last month) | -11.1% |
| Would buy today? | recommend.py says yes — but it reads the *recorded* field and is blind to the pre-check fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen, either direction |

**NOW -> HOLD** (RULE: VALUATION_RICH, front-matter P/E 119.02 ≥ `pe_rich` 50).
Live **$130.46**, **+13.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.5:1 (no stated variant view for the engine to read) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); ratio pre-check clean (debt 1.8%, liquid 4.7%) |
| DCF intrinsic value | $120.12 vs. $130.46 → -7.9% (modest premium to the model) |
| Trailing stop (chandelier) | $110.4868 — price ~15.3% above it |
| 6m momentum (skip last month) | -11.1% |
| Would buy today? | Mechanically yes; conviction still LOW absent your own stated edge |
| What changes verdict | `thesis_broken: true`, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until ≥ 4 names
  (`min_names_for_concentration: 4`). No `portfolio_notes` / vol throttle fired.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $21.72 | 10 | $15.43 | $217.45 | +40.8% | 19.2% |
| NOW | $130.50 | 7 | $114.97 | $913.50 | +13.5% | 80.8% |

**Total value: $1,130.95** | Cost: $959.09 | **Total return: ~+17.9%**
(+$171.86 unrealised)

NOW at **80.8%** is far above the `max_position_pct: 22` cap. That cap is
*muted*, not satisfied — `min_names_for_concentration: 4` switches concentration
rules off below four names, so nothing flags it. Worth knowing that the silence
there is a config choice, not a clean bill of health.

## Action flags (priority order)

### 1. [Mandate] BMNR — the business-activity flag now has primary-source support

The mechanical pre-check fails again: `industry 'Capital Markets' matches
'capital markets' — core business fails screen`. Yesterday's report treated this
as a question raised by news coverage. This run's research resolves where the
classification comes from and what sits behind it, from SEC filings:

- **BMNR files under SIC code 6199 — "Finance Services."** That is the company's
  own EDGAR classification, not a Yahoo mis-tag. The `Capital Markets` label the
  pre-check trips on is downstream of BMNR's own filing code.
  ([EDGAR submissions, CIK 0001829311](https://data.sec.gov/submissions/CIK0001829311.json))
- **The 10-Q self-description** (fiscal Q3 2026, quarter ended 2026-05-31):
  *"We are a digital asset focused company… management expanded its existing
  digital asset business to primarily focus on the Ethereum blockchain and ETH…
  expanding toward an asset light operating model."*
  ([10-Q](https://www.sec.gov/Archives/edgar/data/1829311/000162828026048157/bmnr-20260531.htm))
- **Balance sheet is ~93.5% crypto**: crypto assets at fair value $10,871.9M of
  $11,630.3M total assets; cash $340.3M; equity $11,599.6M. Nine-month revenue
  was **$59.9M** against an $11.6B balance sheet — the operating business is
  rounding error next to the treasury.
- **Revenue is overwhelmingly staking yield** off that treasury (MAVAN validator
  network + the acquired Pier Two node business), with small self-mining,
  consulting and equipment leasing alongside. 5,067,309 of 5,815,164 ETH (~87%)
  are staked at a 7-day annualised 2.61%, ~$250M projected annual staking
  revenue. ([8-K Ex-99.1, 2026-08-17](https://www.sec.gov/Archives/edgar/data/1829311/000149315226038652/ex99-1.htm))
- **It has issued fixed-rate perpetual preferred stock.** June 2026: 3.5M shares
  of **9.50% Series A Perpetual Preferred** (NYSE: BMNP), $100 stated amount,
  priced at $80.00, ~$273.8M net, explicitly to buy more ETH. Preferred dividends
  were declared 2026-06-12 ($0.32), 2026-06-30 ($0.11), and again 2026-08-14.
  ([424B5](https://www.sec.gov/Archives/edgar/data/1829311/000149315226027521/form424b5.htm) ·
  [8-K 2026-08-14](https://www.sec.gov/Archives/edgar/data/1829311/000149315226038012/form8-k.htm))

Read together — self-declared finance-services filer, 93.5% financial-asset
balance sheet, income that is yield on that balance sheet, funded partly by a
9.50% fixed-rate perpetual preferred — this is the profile a business-activity
screen exists to catch. **This report does not rule on it. Zoya/Musaffa do.**
But the question is now specific enough to put to them directly: *does the
9.50% perpetual preferred and the staking-yield-on-treasury model change BMNR's
business-activity status?*

Per this repo's Gate 1 ("Shariah knockout — non-compliant / ratio-or-business
flag → AVOID/SELL, absolute"), a confirmed fail is a hard exit regardless of the
+40.8% gain. **Nothing in the pipeline will escalate this on its own** —
`compliance_gate` reads the *recorded* `shariah.status` field only, which still
says `compliant`. This is the same shape of issue that ran seven cycles unresolved
on FIG, on the position that replaced FIG.

### 2. [Data integrity] Stale hand-entered front-matter is driving a live rule

`holdings/now-servicenow.md` carries hand-entered fields last touched ~2026-06-09
that no script refreshes:

| Field | Recorded | Actual | Effect |
|---|---|---|---|
| `last_price` | 106.40 | $130.46 | -18% stale; used as fallback only |
| `week52_high` | 239.62 | ~$194.73 | `signals.py` reports `pct_of_52w_range: 31`; on the correct range it is ~43% |
| `pe` | 119.02 | not re-fetched | **VALUATION_RICH — the only rule firing on NOW — fires off this number** |

`verdict.py:103` and `signals.py:56` both read `pe` from front-matter and never
from live data. NOW's Q2 2026 results (below) and a forward P/E in the high 20s
suggest 119.02 is a trailing GAAP figure from June that may no longer represent
the multiple you think you are gating on. **Either refresh these fields or make
the scripts fetch them** — right now a June hand-entry is producing an August
"do not add."

### 3. [DCF caveat] BMNR's -96.7% is a data gap, not a valuation

`dcf.py` runs 5% growth / 2.5% terminal / 10% discount with no BMNR override.
A discounted-operating-cash-flow model cannot value a company whose worth is
5.8M ETH marked to market. For scale: market cap ~$13.05B against $11.4B of
crypto + cash + stakes, i.e. roughly 1.14x NAV — a far more relevant frame than
$0.72. Note also the crypto cost basis is **$19,074.4M against $10,871.9M fair
value** (~$8.2B underwater), which is what drove the -$9,106.1M nine-month net
loss. Either set a BMNR-specific method or exclude it from the DCF table.

### 4. [Catalyst] Neither holding has a confirmed near-term print

- **NOW Q3 FY2026: ~2026-10-28 — vendor estimate, NOT company-confirmed.**
  ServiceNow had not issued its results-date press release as of today; it
  historically announces ~3 weeks ahead. 69 days out either way, outside the
  60-day `catalyst_horizon_days`.
- **BMNR FY2026 Q4: ~2026-11-20 — vendor estimate, NOT confirmed.** Fiscal year
  ends Aug 31; FY2025 results landed 2025-11-21. Note BMNR publishes **weekly
  Reg-FD operational updates every Monday**, which is the real information
  cadence for this name, not the quarterly print.

### 5. [Pipeline] A preferred share entered the discovery pool

**SMCIP** — Super Micro's preferred stock — was picked up by the
`growth_technology_stocks` screen, cleared the liquidity floor, ranked #29, and
got a DRAFT card scaffolded (`setups/smcip.md`). scaffold.py logged
`No earnings dates found, symbol may be delisted` and wrote the card anyway with
`no dated catalyst found`.

This is a defect worth fixing, on two counts. Mechanically, a preferred share has
no earnings and cannot satisfy the catalyst gate — it will sit in `leads.md` as
permanent RESEARCH noise. Substantively, a fixed-dividend preferred is exactly
the instrument class this mandate screens out, and the pipeline generated a
trade plan for one. Suggested fix: drop tickers whose Yahoo `quoteType` is not
`EQUITY`, or that return no earnings calendar at all, before scaffolding.

### 6. [Pipeline] 30 of 50 draft cards carry levels 5–6 weeks stale

`scaffold.py` skips any ticker that already has a card (`card exists — use
--force to overwrite`). Nothing ages them out. Thirty cards still carry levels
scaffolded 2026-07-07 or 2026-07-13, and `leads.md` — regenerated today — now
disagrees with them materially for the same names:

| Ticker | Card entry (scaffolded) | leads.md entry (today) | Divergence |
|---|---|---|---|
| ULTA | $452.49 (2026-07-07) | $522.48 | **+15.5%** |

The engine itself is safe: `recommend.py` derives price, stop, target, and
`cat_days` from live data and the watchlist row, **not** from the card's stored
numbers, so stale levels cannot mis-size a trade. The damage is to *review*. The
owner-approval step — the one control standing between a machine draft and a
BUY-CANDIDATE — asks you to read a card, and for these 30 names the card shows
July's market.

Related and now visible: **ULTA, CRDO and ZS** each carry
`earnings_plan: no_earnings_in_window`, which was true when written and is false
now — their prints are 7, 13 and 13 days out inside a 21-day window. This one
fails safe: `no_earnings_in_window` is not an accepted plan value, so
`recommend.py` raises **GAP_PLAN_MISSING** and blocks BUY-CANDIDATE
(`recommend.py:246`). Correct outcome, but by accident of the value not being on
the allow-list rather than by design. Suggested fix: `--refresh-stale` on
scaffold, re-running any `draft` card older than N days.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc

**Case to keep:** The treasury strategy is executing and the capital-return mode
has flipped from issuing to buying back. Since 2026-07-01 the company has
repurchased **20.8M+ common shares** under a $4B authorisation (1.7M in the week
to Aug 17). Holdings reached **5,815,164 ETH — 4.8% of the 120.7M ETH supply** —
plus 210 BTC, a $180M stake in Beast Industries and $73M in Eightco, $11.4B all
in. Added to the **Russell 1000** effective 2026-06-26. Position is +40.8%.
([8-K Ex-99.1, 2026-08-17](https://www.sec.gov/Archives/edgar/data/1829311/000149315226038652/ex99-1.htm))

**Case to flag:** Two things, one of which the price action hides.

*Compliance* — Action Flag #1. Unresolved into a second run.

*Prior dilution was enormous, and it is recent.* In the nine months to
2026-05-31 the company sold **340,748,312 shares** through its ATM for **~$11.87B
net**. Share count went 493.9M (Feb 28) → 579.7M (May 31) → ~603.2M now. The
$4B buyback is real but is retiring a fraction of what was issued. The ATM
remains the funding mechanism for the ETH-accumulation strategy, so treat the
current buyback posture as a policy that can reverse, not a structural change.

*The holding file is still empty.* No `thesis_one_liner`, `variant_view`,
`initial_stop`, `target_price`, `pre_mortem`, or `last_review`. Since 2026-07-07
this position has had no PM-grade record at all — which is why every mechanical
read comes back LOW conviction by default rather than by judgement. On a name
whose compliance status is under question, that gap matters more than usual.

**Verdict: HOLD (no technical rule fired) — the compliance question is what to
resolve, not the price.**

### NOW — ServiceNow, Inc

**Case to keep:** Q2 2026 (reported 2026-07-22) beat the high end of guidance on
every topline and profitability metric.
([Q2 2026 release](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/erq2fy26.htm))

| Metric | Q2 2026 | YoY |
|---|---|---|
| Subscription revenues | $3,877M | **+24.5%** (+23% cc) |
| cRPO | $13.20B | +21% |
| RPO | $29.0B | +21% |
| Non-GAAP operating margin | 29.5% | — |
| Non-GAAP EPS (post-split) | $0.90 | — |
| Free cash flow | $634M (16% margin) | — |

**ServiceNow AI crossed $1B in ACV.** 123 deals >$1M net-new ACV (+~40% YoY);
658 customers >$5M ACV (+~23%). FY2026 subscription guidance was **raised** to
$15,760–15,780M (+22.5%). Financial Analyst Day (2026-05-04) set long-term
targets of $30B+ subscription revenue and Rule of 60+ by 2030.

**Armis is integrating and is quantified**, which is unusual disclosure and
useful: it closed 2026-04-20 for ~$7.6B cash (goodwill $5,323M, intangibles
$2,530M) and contributed **~125bps** to each of Q2 subscription growth, Q2 cRPO
growth, and the FY2026 guide. Product-level integration shipped at Knowledge 2026
as the Autonomous Security & Risk AI specialist (Armis + Veza + AI Control Tower).
([Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000076/now-20260630.htm))

Consensus PT **$142.23** (49 analysts, Strong Buy, S&P Global via
[stockanalysis.com](https://stockanalysis.com/stocks/now/forecast/)) and
**$144.24** (42 analysts, MarketBeat, range $72–$248) — **both post-split**, vs.
$130.46 now.

> ⚠️ **Split-basis warning for future runs.** NOW split 5-for-1 effective
> 2025-12-18. Any price target in the $900–$1,200 range circulating in search
> results is **pre-split**. Specifically, "Oppenheimer raises PT to $1,100 /
> $1,150" items are 2025 pre-split and equate to $220 / $230 post-split. Divide
> pre-split figures by 5 before comparing to anything in this repo.

**Case to watch:** Front-matter P/E 119.02 keeps VALUATION_RICH firing — but see
Action Flag #2 on whether that number is still real. 6m momentum is **-11.1%**,
worse than last run's -5.3%, despite the price being higher — the trailing window
is rolling past a stronger period. DCF shows a -7.9% premium. Q3 guidance implies
deceleration to **+20.5%** subscription growth from +24.5%, which is the number
to watch against the multiple. Acquisition cadence is brisk (Veza ~$1.2B March,
Armis ~$7.6B April, AI.Work July) — mostly tuck-ins, but goodwill is accumulating.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired → NOW**: HOLD, do not add. (Caveat: fires off a stale
  hand-entered `pe`. See Action Flag #2.)
- **COMPLIANCE_GATE does NOT fire → BMNR**: the rule reads only the recorded
  `shariah.status` (`compliant`), so it stays silent through a second consecutive
  pre-check fail. Nothing automates this — the Zoya/Musaffa re-screen is on you.
- **DRAWDOWN_REVIEW**: not firing — both positions are up.
- **TRAIL_STOP → BMNR / NOW**: does not fire; `trade_type: core` exempts both,
  and both prices sit well above their chandelier levels regardless.
- **VOL_THROTTLE**: no `portfolio_notes` this run.
- **REVIEW_CADENCE (`review_cadence_days: 90`)**: NOW's `last_review` is
  **2026-06-15 — 66 days ago**. Not yet due, but within a month of it. BMNR has
  **no `last_review` at all**, so the cadence rule has nothing to measure and
  cannot fire on it.
- **MAX_POSITION_PCT (22%)**: NOW is at 80.8%. Muted by
  `min_names_for_concentration: 4`, not satisfied.

*If you execute anything from this report, run `/apply-trade` so holdings files
and the ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $21.70 | -96.7% — **not a meaningful signal**, see Flag #3 | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $130.43 | -7.9% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for step-4
idea generation. `recommend.py`'s `ideas` array returned **0 BUY-CANDIDATEs**,
which is the expected and correct output: no card has been reviewed and flipped
to `status: planned`, so Gate 3 caps everything at RESEARCH by construction.
All new-idea surfacing comes from machine discovery below.

## Draft & planned setups — 50 leads, 6 fresh DRAFT cards

`discover.py` rebuilt the pool from SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens and rewrote
`leads.md` (top 50 by max-benefit rank). `scaffold.py --all-leads` added DRAFT
cards for **ASND, EXPE, PR, SMCIP, TECK, VLO**; 44 existing cards were left
untouched (see Flag #6 on what that means).

**Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals to review
and edit, never buys.** Every level is a formula output. Approving one means
reading it, editing what you disagree with, flipping `status: planned`, and
screening the name in Zoya/Musaffa.

**8 of 50 clear to LEAD tier** (the rest capped at RESEARCH by the asymmetry or
catalyst gate):

| Ticker | Card | R:R | Entry | Stop | Stop dist | Target | Catalyst | Days out |
|---|---|---|---|---|---|---|---|---|
| ULTA | existing (stale) | 20.0:1 | $522.48 | $515.88 | **1.26%** | $691.99 | earnings 2026-08-27 | 7 |
| AA | existing | 20.0:1 | $49.76 | $48.92 | **1.69%** | $70.18 | earnings 2026-10-15 | 56 |
| CIEN | existing | 10.2:1 | $394.86 | $371.15 | 6.00% | $637.90 | earnings 2026-09-03 | 14 |
| ZS | existing (stale) | 7.9:1 | $177.71 | $167.97 | 5.48% | $254.38 | earnings 2026-09-03 | 14 |
| CRDO | existing (stale) | 6.5:1 | $231.60 | $219.78 | 5.10% | $308.80 | earnings 2026-09-01 | 12 |
| SNX | existing | 5.5:1 | $250.79 | $242.55 | 3.29% | $295.75 | earnings 2026-09-24 | 35 |
| DELL | existing | 3.8:1 | $434.23 | $413.04 | 4.88% | $513.88 | earnings 2026-09-01 | 12 |
| GWRE | existing | 3.6:1 | $182.87 | $158.25 | 13.46% | $272.53 | earnings 2026-09-03 | 14 |

**Read the top two rows sceptically.** ULTA and AA are ranked #1 and #7 on a
20.0:1 reward:risk — which is the *cap*, not a measurement. Both get there
through a stop placed **1.26%** and **1.69%** from entry, against 5–13% for every
other name on the list. Reward:risk is a ratio, and a stop that tight inflates
the denominator toward zero; it does not make the trade asymmetric, it makes the
arithmetic unstable. A stop 1.26% below entry on a $522 stock **seven days before
an earnings print** would be taken out by ordinary intraday noise long before the
catalyst. The asymmetry gate is being cleared here by a degenerate stop, not by
genuine skew. *(Yahoo rate-limiting blocked the ATR cross-check that would
quantify this — the July ULTA card's own ATR of $15.45 implies roughly 3% daily
range, which would make a 1.26% stop about 0.4 ATR, but that figure is six weeks
old and is not a live measurement.)*

**Other flags before reviewing any of these:**

- **ULTA, CRDO, ZS** — stale cards with contradictory gap plans (Flag #6). ULTA's
  card shows a July entry 15.5% below today's market. Do not review these cards
  as written; re-scaffold with `--force` first.
- **ULTA earnings are 7 days out.** Inside any realistic holding window. A gap
  plan is mandatory before this can be anything but RESEARCH.
- **SMCIP** — a preferred share, not equity (Flag #5). Should not be in the pool.
- **PLTR** — carries over again with the unresolved government/defence
  business-activity question flagged in prior runs. Nothing new.
- **CDE, AR, AGI, IAG, KGC, EGO, TECK** — the recurring precious-metals/mining
  cluster from the `undervalued_large_caps` screen. All ratio-clean, all
  business-unverified.
- **VLO, PR, CVE, DINO, EXPE** — new/returning energy and travel names ranking
  on score but failing the asymmetry gate badly (R:R 0.2–0.3:1). High composite
  score with near-zero skew is a signal the screen and the gate disagree, not a
  signal to look closer.
- All 50 cleared the liquidity floor and a clean **ratio** pre-check. That is not
  a business-activity screen. Shariah status on every card is `unverified` by
  construction.

## Follow-ups (prioritised)

1. **Re-screen BMNR in Zoya/Musaffa on business activity specifically.** Put the
   concrete question: does a 93.5%-crypto balance sheet, staking-yield revenue,
   and a 9.50% perpetual preferred change the ruling? Record the answer in
   `holdings/bmnr.md` either way — the recorded field is the only thing
   `compliance_gate` can see.
2. **Fill in `holdings/bmnr.md`.** `thesis_one_liner`, `variant_view`,
   `initial_stop`, `target_price`, `pre_mortem`, `last_review`. Six weeks held
   with no PM record.
3. **Refresh or automate NOW's `pe` / `last_price` / `week52_*`.** A live rule is
   firing off a June hand-entry (Flag #2).
4. **Fix the scaffold staleness gap** — add `--refresh-stale`, or re-run
   `scaffold.py --force` for ULTA / CRDO / ZS at minimum before reviewing them.
5. **Filter non-equity tickers out of discovery** (`quoteType != EQUITY`, or no
   earnings calendar) so SMCIP-class names stop generating trade plans.
6. **Consider whether the R:R cap of 20 is doing you a favour.** Ranking on a
   ratio with an unbounded denominator puts the tightest, least survivable stops
   at the top of the list. A minimum stop distance in ATR terms would fix the
   ordering.
7. **Set a BMNR-specific DCF method or exclude it** from the DCF table (Flag #3).
8. **The ledger is structurally empty.** `transactions.csv` / `journal.csv` are
   gitignored and the container is ephemeral, so `journal.py` will report 0
   closed trades on every scheduled run forever. The discipline guard — the
   check on whether this activity beats buy-and-hold after costs — cannot ever
   fire as configured. Worth deciding whether to persist the ledger somewhere
   durable or to accept that the guard is off.

---

*Not financial advice. Decision support only. Every buy, sell, hold, and sizing
decision is yours. Shariah status must be verified independently in
Zoya/Musaffa — the pre-checks in this repo are mechanical heuristics, not
rulings.*
