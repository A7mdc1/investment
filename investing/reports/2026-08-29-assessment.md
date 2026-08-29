# Portfolio Assessment — 2026-08-29

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data) → `scaffold.py --all-leads` (10 new DRAFT
setup cards: AMKR, NTNX, BKR, LLY, BBY, BLSH, EXPE, ASND, APA, FLYW; the rest
of the existing 63 cards left unchanged, 73 total now) → `prices.py` /
`shariah.py` / `dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all
live, no data gaps this run. `journal.py` returned 0 closed trades —
`transactions.csv` still doesn't exist locally (it's gitignored personal
data; the discipline guard stays dormant until you log trades on your own
machine).

**Since the last report (2026-08-19):** no trades recorded. BMNR is up
another ~+15.9% (from $20.54 to $23.80); NOW is up ~+12.5% (from $128.63 to
$144.71). The BMNR compliance question flagged last run is still open.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$23.80**, up
**+54.2%** vs. the $15.43 cost basis. **The mechanical Shariah
business-activity pre-check still disagrees with the recorded "compliant"
status — this is now the 2nd consecutive run flagging it, unresolved.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -31.7:1 (DCF-derived target sits far below the stop; see DCF caveat below) |
| Shariah (recorded) | PASS — broker_app compliant, screened 2026-07-07, not stale |
| Shariah (mechanical ratio pre-check, this run) | **FAIL** — industry classified `Capital Markets`; core business fails the screen |
| DCF intrinsic value | $0.72 vs. $23.80 price -> -97.0% (see caveat: DCF model does not fit an ETH-treasury business) |
| Trailing stop (chandelier) | $23.072 — price only ~3.1% above it (closest of the two positions to its stop) |
| 6m momentum (skip last month) | -18.8% |
| Would buy today? | Mechanically yes per recommend.py's gates — but that check reads the *recorded* Shariah field, not this run's ratio-precheck fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$144.71**, **+25.9%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -0.99:1 (recommend.py can't self-assess without a stated thesis-vs-price edge) |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | $120.12 vs. $144.71 price -> -17.0% (price meaningfully rich to the model — wider gap than last run's -6.6%) |
| Trailing stop (chandelier) | $119.97 — price is ~17.1% above it |
| 6m momentum (skip last month) | +5.9% (turned positive since last run's -5.3%) |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction still flagged LOW absent your own stated edge |
| What changes verdict | thesis_broken: true, or the Shariah screen going stale/flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $23.80 | 10 | $15.43 | $238.00 | +54.2% | 19.0% |
| NOW | $144.71 | 7 | $114.97 | $1,012.97 | +25.9% | 81.0% |

**Total value: $1,250.97** | Cost: $959.09 | **Total return: ~+30.4%** (+$291.88 unrealised)

Both positions rallied hard since 2026-08-19 (BMNR +15.9%, NOW +12.5%), and
the book is still heavily concentrated in NOW (81.0%) — a function of BMNR's
small share count, not a deliberate sizing decision recorded anywhere in the
files.

## Action flags (priority order)

1. **[Mandate — 2nd run flagged, still open] BMNR's mechanical Shariah ratio
   pre-check FAILS**, `industry 'Capital Markets' matches 'capital markets' —
   core business fails screen`. This still conflicts with the recorded
   `compliant` status. This run's independent research supports treating the
   GICS tag as likely a **classification artifact**: BMNR's actual business is
   described as an Ethereum treasury/staking company (largest ETH treasury
   holder, ~5.85M ETH / ~$14.9B as of ~Aug 27, plus legacy immersion-cooled
   BTC mining) — not a broker-dealer or capital-markets operating business in
   substance. That said, the yield-generating treasury structure (staking
   income, a $280M 9.50% Series A Preferred raise funding further ETH buys, a
   $4B buyback) is close enough to what a business-activity screen is built to
   catch that it is not a clear-cut false positive either. Per this repo's own
   Gate 1 ("Shariah knockout — non-compliant / ratio-or-business flag ->
   AVOID/SELL, absolute"), a confirmed fail would be a hard SELL, independent
   of the +54.2% return. **`recommend.py`'s "would buy today" check only reads
   the recorded field and cannot see this flag — it will not resolve itself.**
   This is the second consecutive run this has gone unresolved on a position
   that has grown to +54.2%; recommend re-screening the business-activity
   question specifically in Zoya/Musaffa before adding to this position or
   treating "compliant" as settled.
2. **[Valuation / NOW] P/E ~119 (recorded), DCF gap widened to -17.0%**
   (from -6.6% last run) as the price rallied faster than the DCF model's
   18%-growth assumption implies. VALUATION_RICH holds. Do not add.
3. **[DCF caveat / BMNR]** The -97.0% DCF "downside" is not a meaningful
   signal — `dcf.py`'s cash-flow model (5% growth, 10% discount, no
   BMNR-specific override in the holding file) does not fit an ETH-treasury
   business whose value is driven by crypto holdings and staking yield, not
   discounted operating cash flow. Treat this as a data gap, not a valuation
   call.
4. **[Catalyst / NOW]** Next earnings (Q3 FY2026) land **~2026-10-28** (60
   days out — right at the catalyst-horizon edge). BofA raised its price
   target to $150 (from $130) on 2026-08-19; ServiceNow launched "Autonomous
   Security & Risk" at Knowledge 2026, integrating the Armis acquisition with
   Veza for AI-agent/identity governance — a direct extension of the Armis
   thesis. No guidance cuts or downgrades found in the last 30 days.
5. **[Catalyst / BMNR]** Fiscal Q4 2026 earnings likely land mid-to-late
   November (~91+ days out, outside the 60-day window — no near-term
   earnings catalyst). The nearer informal catalyst is management's stated
   target of holding 5% of global ETH supply, which Tom Lee has suggested
   could be reached by year-end.
6. **[Discovery] 55 leads this run** (up slightly from 50 last run), 15
   clearing to LEAD tier (up from 9 last run) — the rest capped at RESEARCH
   by the asymmetry/catalyst gates. 10 fresh DRAFT cards were scaffolded
   (AMKR, NTNX, BKR, LLY, BBY, BLSH, EXPE, ASND, APA, FLYW); AMKR and BKR
   both cleared straight to LEAD tier on their first run. **PLTR** still
   carries its unresolved government/defense business-activity question from
   prior runs — nothing new to add, still open.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep (fundamental):** Continues growing its core Ethereum position
(~5.85M ETH, ~$14.9B, as of ~Aug 27) toward management's 5%-of-supply target,
funded partly through a $280M preferred raise rather than further common
dilution, alongside an ongoing $4B buyback. Stock up +54.2% since the $15.43
cost basis; recorded compliance status is "compliant."

**Case to flag (compliance, independent of the price story):** The
mechanical ratio pre-check disagrees with the recorded status for the second
run in a row — see Action Flag #1. The holding file itself is still
incomplete: no `thesis_one_liner`, `variant_view`, `initial_stop`,
`target_price`, or `pre_mortem` have been filled in, six weeks after the
position was opened, so there is no PM-grade record to weigh the compliance
question against beyond the mechanical LOW-conviction default.

**Verdict: HOLD (no technical rule fired) — but the compliance question is
still the thing to resolve first, not the price action, and it's now been
open two runs.**

### NOW — ServiceNow, Inc
**Case to keep:** Continued AI-platform momentum via the new "Action Fabric"
headless/MCP-agent integration and the "Autonomous Security & Risk" launch
tying Armis + Veza together; BofA raised its price target to $150 on
2026-08-19. 6m momentum turned positive (+5.9%) this run after being
negative last run.

**Case to watch:** P/E ~119 keeps VALUATION_RICH active; the DCF gap widened
to -17.0% as price outran the model's growth assumption. Next earnings not
until ~2026-10-28 (60 days out, right at the catalyst-horizon edge) — no
near-term binary catalyst to react to yet.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE does NOT fire -> BMNR**: the rule only reads the
  *recorded* `shariah.status` field (currently `compliant`), so it stays
  silent despite two runs of ratio-precheck fails now. That gap is worth
  naming explicitly: nothing in the automated pipeline will re-flag this on
  its own until you update the recorded status — the follow-up is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing** — both positions are up sharply, not down 20%.
- **TRAIL_STOP -> BMNR / NOW**: does NOT fire for either (`trade_type: core`
  exempts both from the technical trailing-stop rule); BMNR's price is now
  only ~3.1% above its computed chandelier stop, the closest either position
  has been to triggering a technical exit this cycle.
- **VOL_THROTTLE**: no `portfolio_notes` surfaced this run.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $23.80 | -97.0% (not a meaningful signal — see caveat) | growth_5y 5% (default, no override), terminal 2.5%, discount 10% |
| NOW | $120.12 | $144.71 | -17.0% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing comes
from machine discovery below instead. `recommend.py`'s `ideas` array returned
**0 BUY-CANDIDATEs** this run (expected — no card has been reviewed and
flipped to `status: planned` yet; all 73 cards in `setups/` are still
`draft`).

## Draft & planned setups — 55 leads, 10 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool and wrote **`leads.md`** (55
names kept this run, up from 50 last run). `scaffold.py --all-leads`
auto-filled a DRAFT `setups/<ticker>.md` card for every lead without one (10
new cards: AMKR, NTNX, BKR, LLY, BBY, BLSH, EXPE, ASND, APA, FLYW; the
remaining 63 existing cards left unchanged). **Every DRAFT card is
unreviewed and Shariah UNVERIFIED — proposals to review and edit, never
buys.**

15 of the 55 leads clear to LEAD tier this run (up from 9 last run):

| Ticker | R:R | Entry / Target / Stop | Catalyst | Days out | Card |
|---|---|---|---|---|---|
| AMKR | 20.0:1 | 51.74 / 88.44 / 51.22 | earnings 2026-10-26 | 58 | new |
| CLS | 13.5:1 | 317.38 / 473.70 / 309.74 | earnings 2026-10-26 | 58 | existing |
| CIEN | 9.4:1 | 399.85 / 637.72 / 374.46 | earnings 2026-09-03 | 5 | existing |
| STX | 9.0:1 | 847.20 / 1144.86 / 814.55 | earnings 2026-10-27 | 59 | existing |
| TER | 8.5:1 | 372.06 / 487.63 / 362.47 | earnings 2026-10-21 | 53 | existing |
| AA | 7.8:1 | 51.19 / 73.70 / 48.30 | earnings 2026-10-15 | 47 | existing |
| BKR | 5.6:1 | 62.11 / 69.94 / 60.72 | earnings 2026-10-22 | 54 | new |
| TSLA | 5.0:1 | 354.81 / 471.09 / 331.62 | earnings 2026-10-21 | 53 | existing |
| CRDO | 4.7:1 | 240.24 / 308.79 / 225.50 | earnings 2026-09-01 | 3 | existing |
| AGI | 4.7:1 | 37.88 / 52.12 / 34.84 | earnings 2026-10-28 | 60 | existing |
| ZS | 3.9:1 | 187.30 / 273.54 / 165.10 | earnings 2026-09-03 | 5 | existing |
| LRCX | 3.9:1 | 318.58 / 438.21 / 287.50 | earnings 2026-10-21 | 53 | existing |
| HAS | 3.7:1 | 94.18 / 104.64 / 91.33 | earnings 2026-10-22 | 54 | existing |
| APH | 3.7:1 | 161.38 / 178.52 / 156.73 | earnings 2026-10-28 | 60 | existing |
| MU | 3.5:1 | 935.39 / 1255.56 / 843.55 | earnings 2026-09-30 | 32 | existing |

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
- **40 RESEARCH-tier leads** — full list in `leads.md`; not reproduced here
  to keep this report readable.

## Follow-ups (priority order)

1. **[Urgent — 2nd run open] BMNR Shariah re-screen**: the mechanical ratio
   pre-check has now disagreed with the recorded "compliant" status for two
   consecutive runs on the business-activity question specifically. This is
   the largest compliance question in the book (19.0% weight, +54.2% return)
   and the automated pipeline will NOT re-surface it on its own — see the
   COMPLIANCE_GATE note above. Recommend prioritizing this over reviewing new
   draft cards.
2. **[Housekeeping] BMNR holding file is still missing PM-grade fields** —
   `thesis_one_liner`, `variant_view`, `initial_stop`, `target_price`,
   `pre_mortem` are all still null/empty, six weeks after the position was
   opened.
3. **[Time-boxed] NOW earnings ~2026-10-28** — 60 days out (right at the
   catalyst horizon); no action needed yet, but track the Action
   Fabric / Autonomous Security & Risk narrative between now and then.
4. **[Housekeeping] 10 new DRAFT setup cards** added this run (73 total in
   `setups/`); none are `planned`. AMKR and BKR are worth a first look — both
   cleared to LEAD tier on their debut run.
5. **[Infrastructure — still open]** No ledger yet — start logging trades to
   `transactions.csv` (or via `/apply-trade`) to unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- ServiceNow Newsroom — Autonomous Security & Risk / Action Fabric launch coverage (Aug 2026)
- Constellation Research, CIO.com — ServiceNow Knowledge 2026 AI-agent platform coverage (Aug 2026)
- TheStreet — BofA price target raise to $150 (2026-08-19)
- TipRanks, stockanalysis.com — ServiceNow earnings calendar and price/valuation data (accessed Aug 2026)
- PRNewswire, CoinDesk, Benzinga — BitMine Immersion Technologies ETH treasury holdings updates (Aug 2026)
- TradingKey, CoinGecko, 99bitcoins — BMNR business-model background (Ethereum treasury/staking) (2026)
- Yahoo Finance, StocksToTrade — BMNR $280M Series A Preferred offering, buyback program (Aug 2026)
