# Portfolio Assessment — 2026-09-23

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 160-name raw pool, top 50 kept per
`discover_top_n: 50`) → `scaffold.py --all-leads` (17 new DRAFT setup cards
auto-filled; 33 existing cards left unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live. Yahoo was
heavily crumb-rate-limited on several earnings-date lookups during discovery
and scaffold (individual `HTTP 401`s, logged and skipped), but the pool build
and both holdings' data came through clean — no data gaps affecting this
report's numbers. `journal.py` run: still `0` closed trades — no
`transactions.csv` yet (discipline guard stays dormant).

**Since the last report (2026-08-19):** no trades recorded — still the same
two holdings (BMNR, NOW). It has been **5 weeks** since the last assessment
(longest gap between runs so far); several things moved in that time — see
Action Flags below.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$27.47**, up
**+78.0%** vs. the $15.43 cost basis. **Action Flag #1 — the mechanical
Shariah business-activity pre-check still FAILS, for the second consecutive
run.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -5.8:1 (DCF-derived target sits below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL, unchanged from last run** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $27.47 price -> -97.4% (see caveat: DCF model does not fit a crypto-treasury business) |
| Trailing stop (chandelier) | $22.9041 — price ~19.9% above it |
| 6m momentum (skip last month) | +7.3% |
| Portfolio note | ATR 6.86% — flagged for the vol-throttle (`portfolio_notes`) |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not the ratio-precheck fail (see below) |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119.02 >= pe_rich 50). Live
price **$140.21**, **+21.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -2.1:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah (recorded) | **REVIEW, NEW this run** — recorded compliant, but the 2026-06-09 screen is now >100 days old (recommend.py's own staleness note) |
| DCF intrinsic value | $120.12 vs. $140.21 price -> -14.3% (gap to the model widened from -6.6% last run) |
| Trailing stop (chandelier) | $130.8146 — price is ~7.6% above it |
| 6m momentum (skip last month) | +15.8% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping — the staleness flag is now live |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.
  BMNR's weight has grown from 18.6% (last run) to **21.9%** — close under
  the 22% `max_position_pct` cap purely from price appreciation, not an add.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $27.47 | 10 | $15.43 | $274.60 | +78.0% | 21.9% |
| NOW | $140.21 | 7 | $114.97 | $981.45 | +21.9% | 78.1% |

**Total value: $1,256.05** | Cost: $959.09 | **Total return: ~+31.0%** (+$296.96 unrealised)

NOW's weight eased slightly (81.4% -> 78.1%) not because it fell, but because
BMNR's +78% run since cost basis grew faster in relative terms this cycle.
The book is still, in practice, a two-name bet dominated by NOW.

## Action flags (priority order)

1. **[Mandate — unresolved, 2nd consecutive run] BMNR's mechanical Shariah
   ratio pre-check still FAILS**, same flag as 2026-08-19:
   `industry 'Capital Markets' matches 'capital markets' — core business
   fails screen`. Nothing in the files shows this was re-screened in
   Zoya/Musaffa since it was first raised five weeks ago, and the position
   has grown from +33.1% to +78.0% in the meantime — the dollar amount at
   stake if this flips to a hard AVOID/SELL keeps rising. Per this repo's
   own Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL independent
   of return. This is the same category of issue that took 7 runs to close
   out on FIG.
2. **[Mandate — NEW this run] NOW's Shariah screen is now stale** — recorded
   `compliant`, screened 2026-06-09, now >100 days old. `recommend.py` flags
   this as `REVIEW` this run (it did not last run). This is the account's
   largest position (78.1% of value) running on a compliance screen over a
   quarter old.
3. **[Sizing] BMNR weight (21.9%) is approaching `max_position_pct` (22%)**
   purely from price appreciation — no CONCENTRATION rule fired yet (would
   need to cross 22%), but it's one more strong week away from doing so.
4. **[Valuation / NOW] P/E ~119.02 (recorded)** — rich; VALUATION_RICH holds. Do not add.
5. **[DCF caveat / BMNR]** The -97.4% DCF "downside" is still not a
   meaningful signal — the model (5% growth, 10% discount, no BMNR-specific
   override) does not fit a crypto-treasury business whose value tracks ETH
   holdings and staking yield, not discounted operating cash flow.
6. **[Catalyst / NOW]** Next earnings **~2026-10-28** — now **35 days out**,
   inside the 60-day catalyst horizon (was 72 days / outside horizon last
   run). Several sell-side targets have moved up since: Cantor Fitzgerald to
   $174 (from $141), Needham to $155 (from $115), BTIG to $170 (from $150),
   all citing continued subscription/AI-ACV strength.
   [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-1-68-percent-as-cantor-lifts-target/70155026)
7. **[Discovery] 50 leads this run, pool widened to 160 raw names** (up from
   149); **26 clear to LEAD tier** (up sharply from 9 last run), 24 capped at
   RESEARCH. **PLTR** carries over again (still RESEARCH, R:R now only
   0.9:1) — its unresolved government/defense business-activity question
   from prior runs is unchanged, nothing new to add. The precious-metals
   cluster (**IAG, EGO**) is back at LEAD tier too — same open
   business-activity question flagged in earlier runs.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues aggressively growing its ETH
treasury — combined crypto/cash/securities holdings reached **$17.1B** as of
Sep 21, anchored by **5.98M ETH (~4.9% of global supply)**, with **5.07M ETH
staked** generating a projected **~$357M annualized** staking yield.
Chairman Tom Lee is keynoting Korea Blockchain Week on Sep 30, reiterating a
push toward 5% of total ETH supply and calling for a crypto bull market that
began in late June.
[TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2) ·
[StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_17/) ·
[PR Newswire](https://www.prnewswire.com/apac/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884418.html)

**Case to flag (compliance, independent of the price story):** Action Flag #1
— the mechanical ratio pre-check still disagrees with the recorded
"compliant" status, unresolved for five weeks. The holding file is still
missing `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
and `pre_mortem` — over two months after the position was opened (2026-07-07),
there is still no PM-grade record to weigh the compliance question against
beyond the mechanical LOW-conviction default. No confirmed next-earnings date
found this run (BMNR's last reported print was 2026-07-14 on an unusual
fiscal calendar) — not fabricating one; flag as a data gap for the gap-plan
requirement if this were ever promoted to a setup card.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
now the most time-sensitive open item in the book, growing in dollar terms
every week it stays unresolved.**

### NOW — ServiceNow, Inc
**Case to keep:** Stock at $140.21 (post the 5-for-1 split), analyst targets
moving up across the board this month — Cantor to $174, Needham to $155,
BTIG to $170 — all pointing to continued subscription/AI-agent momentum.
Beat Q2 FY2026 (reported Jul 22) with EPS $0.90 vs. $0.76 est. (+18.4%
surprise) and raised full-year subscription-revenue guidance. Q3 consensus
EPS estimate ~$1.40 (WSJ) / ~$0.93 (analyst avg per one source — figures
diverge by source; treat both as estimates, not facts) for the 2026-10-28
print.
[Cantor/ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-1-68-percent-as-cantor-lifts-target/70155026) ·
[ServiceNow Newsroom Q2 results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; DCF gap to
intrinsic value widened to -14.3% (from -6.6% last run) as price outran the
model's 18%-growth/10%-discount assumptions. The Shariah screen is now
stale (Action Flag #2) on the account's largest position by far (78.1% of
value). Earnings are 35 days out — inside the catalyst horizon now, so this
is a real near-term event to plan around, not "dead money."

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite five straight weeks of a ratio-precheck fail. Nothing in
  the automated pipeline will re-flag this on its own until the recorded
  status is updated — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); both prices sit well
  above their computed chandelier levels regardless.
- **VOL_THROTTLE -> BMNR**: `portfolio_notes` flags BMNR's 6.86% daily ATR
  for de-risking consideration — informational, no auto-action.
- **CONCENTRATION** — not yet fired (cap is 22%, BMNR is at 21.9%), but
  worth watching; the rule is muted anyway with only 2 names (`min_names_for_concentration: 4`).

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $27.47 | -97.4% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $140.21 | -14.3% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below. `recommend.py`'s `ideas` array returned **0
BUY-CANDIDATEs** this run (expected — no card has been reviewed and flipped
to `status: planned`; all 80 cards in `setups/` are still `draft`, none
`planned` or `live`).

## Draft & planned setups — 50 leads, 17 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens, 160 raw names)
and wrote **`leads.md`** (top 50 by max-benefit rank, `discover_top_n: 50`
unchanged). `scaffold.py --all-leads` auto-filled a DRAFT `setups/<ticker>.md`
card for every lead without one (17 new cards: FSLR, NUE, ORCL-PD, XOM,
TECK, NTNX, FRO, TS, APA, CORZ, BLSH, AMKR, DDOG, ONON, HPE, SMTC, AAPL; 33
existing cards left unchanged). **Every DRAFT card is unreviewed and Shariah
UNVERIFIED — proposals to review and edit, never buys.**

26 of the 50 leads clear to LEAD tier this run (up from 9 last run — the
asymmetry/catalyst gates are passing far more names now that most earnings
dates sit inside the 60-day horizon):

| Ticker | Verdict | Has card | R:R | Catalyst | Days out |
|---|---|---|---|---|---|
| ALAB | LEAD | existing | 3.1:1 | earnings 2026-11-03 | 41 |
| SMCI | LEAD | existing | 3.3:1 | earnings 2026-11-03 | 41 |
| MSFT | LEAD | existing | 3.9:1 | earnings 2026-10-28 | 35 |
| TSLA | LEAD | existing | 3.7:1 | earnings 2026-10-21 | 28 |
| LRCX | LEAD | existing | 6.0:1 | earnings 2026-10-21 | 28 |
| DINO | LEAD | existing | 5.8:1 | earnings 2026-10-28 | 35 |
| EGO | LEAD | existing | 8.0:1 | earnings 2026-10-28 | 35 |
| IAG | LEAD | existing | 12.1:1 | earnings 2026-11-03 | 41 |
| GOOGL | LEAD | existing | 17.3:1 | earnings 2026-10-28 | 35 |
| GDDY | LEAD | existing | 19.3:1 | earnings 2026-10-29 | 36 |
| FSLR | LEAD | new | 20.0:1 | earnings 2026-10-29 | 36 |
| MKSI | LEAD | existing | 16.6:1 | earnings 2026-11-04 | 42 |

(Full 26-name LEAD list and all 24 RESEARCH-tier rows are in `leads.md` —
not reproduced in full here to keep this report readable.)

All 50 cleared the liquidity floor and a clean ratio pre-check — not a
business-activity screen. Shariah status on every card is `unverified` by
construction.

**Flags worth your attention before reviewing any of these:**
- **PLTR** — carried over again, still RESEARCH (R:R compressed to 0.9:1
  this run). Its unresolved government/defense business-activity question
  from prior runs is unchanged. Nothing new to add.
- **IAG, EGO** — the recurring precious-metals/mining names, both LEAD tier
  again this run. The mining-royalty financing-structure question raised in
  earlier runs is still open; worth a real Zoya/Musaffa screen before
  spending review time on either card.
- **24 RESEARCH-tier leads** — full list in `leads.md`.

## Follow-ups (priority order)

1. **[Urgent — unresolved 5 weeks / growing] BMNR Shariah re-screen**: the
   mechanical ratio pre-check has disagreed with the recorded "compliant"
   status for two straight runs now, on a position that has grown to
   21.9% of the book (+78.0% return). The automated pipeline will not
   re-surface this on its own — see the COMPLIANCE_GATE note above.
2. **[Urgent — NEW this run] NOW Shariah re-screen**: the 2026-06-09 screen
   is now stale on the account's largest position (78.1% of value). Re-screen
   in Zoya/Musaffa and update `screened:` in `holdings/now-servicenow.md`.
3. **[Housekeeping — still open] BMNR holding file is missing PM-grade
   fields** — `thesis_one_liner`, `variant_view`, `initial_stop`,
   `target_price`, `pre_mortem` are all still null/empty, over two months
   after the position was opened.
4. **[Time-boxed] NOW earnings ~2026-10-28** — 35 days out, now inside the
   catalyst horizon; track guidance vs. the raised analyst targets.
5. **[Sizing watch] BMNR at 21.9%, cap is 22%**: one more strong week could
   trip `CONCENTRATION` even without an add.
6. **[Housekeeping] 17 new DRAFT setup cards** added this run (80 total in
   `setups/`); none are `planned`. Review at your own pace.
7. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [BitMine Highlights Record Ethereum Treasury and Staking Growth — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-record-ethereum-treasury-and-staking-growth-2)
- [BMNR Stock Rides Ethereum Wave As Analysts Hike Targets — StocksToTrade](https://stockstotrade.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_09_17/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.98 Million Tokens — PR Newswire](https://www.prnewswire.com/apac/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-98-million-tokens-and-total-crypto-and-total-cash-holdings-of-17-1-billion-302884418.html)
- [ServiceNow stock gains as Cantor lifts target to $174 — ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/servicenow-stock-gains-1-68-percent-as-cantor-lifts-target/70155026)
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
