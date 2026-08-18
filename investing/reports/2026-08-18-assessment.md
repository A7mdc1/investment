# Portfolio Assessment — 2026-08-18

Decision support only — not financial advice. Every Shariah status below is a
broker-app record or a mechanical ratio pre-check, never a fatwa; verify
independently in Zoya/Musaffa before acting on anything here. This is the
first assessment since 2026-07-13 (36 days).

## Verdicts (lead with this)

**BMNR -> HOLD** (rule: DEFAULT, no rule fired)
Trailing stop $15.9516 (price $18.72, 14.8% above stop). R-multiple: n/a (no
`initial_stop` recorded on the card yet). 6m momentum: -17.5%.
PM record: conviction LOW (mechanical — reward:risk -6.5:1, "skew too thin"),
target $0.72 via DCF intrinsic value, would_buy_today flag: true. **Treat the
DCF target as not meaningful for this name** — BMNR's value is its ETH/BTC
treasury holdings and staking yield, not discounted cash flow from
operations; a DCF built for an operating company understates a
treasury/holding-company balance sheet. This is a model-fit caveat, not a
signal to act on.

**NOW -> HOLD** (rule: VALUATION_RICH — "P/E ~119.02 — hold, do not add")
Trailing stop $109.7768 (price $120.27, 8.7% above stop). R-multiple: n/a (no
`initial_stop` recorded). 6m momentum: -1.1%.
PM record: conviction LOW (mechanical — reward:risk -0.0:1), target $120.12
via DCF (price is basically at fair value on this DCF's assumptions:
18% 5y growth, 3% terminal, 10% discount rate), would_buy_today flag: true.

Portfolio note: only 2 holdings — concentration rules muted until >= 4 names
(per `min_names_for_concentration: 4`).

## Snapshot

| Ticker | Price | Shares | Cost basis | Value | Weight | Return |
|---|---|---|---|---|---|---|
| BMNR | $18.72 | 10 | $15.43 | $187.20 | 18.2% | +21.3% |
| NOW | $120.29 | 7 | $114.97 | $842.03 | 81.8% | +4.6% |
| **Total** | | | | **$1,029.23** | | |

## Action flags (priority order)

1. **[MANDATE — needs your attention] BMNR: broker app says compliant, the
   mechanical business-activity pre-check disagrees.** `shariah.py`'s ratio
   pre-check flags BMNR's Yahoo industry classification as **"Capital
   Markets"** — a knockout industry under this repo's own business-activity
   screen (the same screen that dropped 68 of 147 names from today's
   discovery pool for the identical reason). BMNR is recorded
   `compliant`/`broker_app`, screened 2026-07-07 — not stale by the 1-quarter
   test, but this ratio-pre-check conflict has never been surfaced before
   (BMNR was bought the same day as the last assessment, 2026-07-13, so this
   is the first run to check it). This is exactly the pattern that led to the
   FIG exit (a compliance flag that sat unresolved for 7 runs before being
   acted on) — recommend re-screening BMNR in Zoya/Musaffa now rather than
   letting it sit. This is a policy question, not a price call: the numbers
   say HOLD, but the mandate gate takes precedence over return when the two
   conflict.
2. **NOW: recorded catalyst is stale.** The card's `catalyst.desc` says "Q2
   FY2026 earnings + Armis integration progress" — Q2 FY2026 earnings already
   reported 2026-07-22 (beat: revenue $3.99B, +24% YoY; subscription revenue
   +24.5% YoY). [ServiceNow Q2 2026 results](https://www.stocktitan.net/sec-filings/NOW/10-q-service-now-inc-quarterly-earnings-report-d7f5db0cedb3.html).
   Next earnings: **2026-10-28** (Q3 FY2026, after close) — that's 71 days
   out, outside the 60-day `catalyst_horizon_days` window. Worth updating the
   card's `catalyst.date` field to 2026-10-28 so the record reflects the live
   catalyst.
3. **NOW: valuation flag** (signals.py, priority 3) — P/E ~119: rich;
   growth has to keep delivering to justify it. Informational, not a trigger.
4. No SELL/TRIM/REVIEW verdicts; no gap-plan-missing flags; no stale Shariah
   records (both within the ~1-quarter freshness test).

## Per-holding read

**BMNR (Bitmine Immersion Technologies)** — Ethereum-treasury company: holds
5.82M ETH + 210 BTC + a stake in Beast Industries, total crypto+cash ~$11.4B
as of 2026-08-16, funded partly by a 9.50% perpetual preferred (BMNP) and
running an active buyback (>20.8M shares repurchased since July 2026 under a
$4B program). [BMNR Aug 2026 holdings update](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-82-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-4-billion-302852583.html).
Thesis on file is a placeholder ("NEW position — screen compliance before
adding more") with no risks/notes filled in.
- **Case to hold**: up 21.3%, still above the trailing stop by a wide
  margin; large buyback + preferred-dividend program signals management
  confidence; broker app currently marks it compliant.
- **Case to trim/exit**: the ratio pre-check's "Capital Markets" flag is the
  same mechanism that flagged FIG for 7 runs before it was sold — if
  Zoya/Musaffa confirms non-compliant, the mandate gate overrides the return.
  Separately, ETH-treasury names are effectively leveraged, single-asset bets
  on ETH price with real dilution/preferred-servicing risk — very different
  risk profile from a diversified operating company. No thesis, stop, target,
  or invalidation are recorded on the card, so there's no written plan to
  hold this against.
- Neither case is picked for you — the compliance question in particular
  needs a human answer before the return question matters.

**NOW (ServiceNow)** — Durable subscription grower; Q2 beat delivered
24%+ revenue growth and the Armis ($7.8B) + Veza acquisitions closed in the
quarter, extending into AI-native security/identity workflow.
- **Case to hold**: thesis intact — subscription growth still ~24-25% YoY,
  well above the "meaningfully below ~21-22%" level the file lists as what
  would change the mind; DCF says price is close to fair value on stated
  assumptions, not stretched; return positive.
- **Case to trim**: P/E ~119 leaves little room for a growth deceleration;
  the position is 82% of a 2-name book (large single-name weight, even if
  the concentration *rule* is muted below 4 names); no `initial_stop`,
  `target_price`, or `variant_view` recorded on the card despite being the
  large majority of the book — the file has five `TODO` fields still open.
- Again, not a pick for you — the facts on both sides are laid out above.

## Suggested actions (from your rules)

Read against `rules.md`:
- **VALUATION_RICH fired on NOW** -> your pre-set rule: hold, do not add.
  (Fact: P/E ~119.02, `pe_rich` threshold is 50.)
- No other rule in `rules.md` (SELL / TRIM / REVIEW / DEAD_MONEY /
  COMPLIANCE_GATE / GAP_PLAN_MISSING) fired against BMNR or NOW this run.
- If you execute anything based on this report, run `/apply-trade` so the
  holding file and ledger update.

## DCF

| Ticker | Price | Intrinsic value | Upside | Assumptions |
|---|---|---|---|---|
| BMNR | $18.72 | $0.72 | -96.2% | growth_5y 5%, terminal 2.5%, discount 10% — **not a meaningful model for a crypto-treasury balance sheet; disregard the upside figure** |
| NOW | $120.27 | $120.12 | -0.1% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas

Step 0 refreshed `leads.md` (fresh run today — the checked-in copy was dated
2026-07-13, 36 days stale) and scaffolded 35 new DRAFT setup cards for leads
that didn't have one. Discovery stats: pool 147 names (SPUS holdings +
growth-tech / undervalued-large-cap screens) -> 68 dropped on the
Shariah business-activity ratio-pre-check knockout, 1 on liquidity, 2 on
missing price data -> 50 selected, top 7 classified `LEAD` (clear every
gate: asymmetry >= 2:1 swing floor + catalyst inside 60 days), 43 capped at
`RESEARCH` (missing edge / thin asymmetry / catalyst outside horizon).
`watchlist.md` (hand-curated) is still empty, so `recommend.py`'s `ideas`
array — which only reads that file — returned nothing; the table below is
read directly from `leads.md` / `discover.py`'s own classification instead.
None of these are `BUY-CANDIDATE`: every one is Shariah `UNVERIFIED`
(discovery/scaffold never write `compliant`) and none has a human-approved
(`status: planned`) setup card yet — both are hard requirements before that
label is possible.

**LEAD** (asymmetry + catalyst gates clear; still need a human variant view
+ Zoya/Musaffa screen before they can go further):

| Ticker | R:R | Score | Card? | Earnings |
|---|---|---|---|---|
| ULTA | 20.0:1 | 33.3 | has card (stale — priced 2026-07-07, entry $452 vs today's ~$522) | 2026-08-27 |
| ADI | 5.1:1 | 36.7 | has card | 2026-08-19 (tomorrow) |
| AA | 20.0:1 | 25.8 | none yet | 2026-10-15 |
| GWRE | 4.1:1 | 48.3 | none yet | 2026-09-03 |
| KEYS | 3.4:1 | 39.9 | none yet | 2026-08-18 (today) |
| ZS | 3.9:1 | 33.5 | has card | 2026-09-03 |
| CIEN | 7.8:1 | 30.5 | scaffolded today | 2026-09-03 |

ADI and KEYS both have earnings inside the next 1-2 days — too close to
scaffold a fresh entry against without knowing the print's outcome; note
rather than act.

**RESEARCH** (43 more names, capped by a thin R:R or a catalyst beyond 60
days) — full list with entry/target/stop in `leads.md`; notable ones already
carrying a setup card: AMD, MU, MSFT, GDDY, PAY, CRDO, SIMO, CF, AR, CDE,
KLIC, ALAB.

## Draft & planned setups

**35 new DRAFT cards** written today by `scaffold.py --all-leads` for leads
without a card (AA, AEM, AGI, APH, ARW, ASND, ASTS, AVGO, AVT, CIEN, CLS,
DDOG, DELL, DOCN, EGO, FN, GWRE, HBM, IAG, IONQ, KEYS, KGC, LRCX, MKSI, NET,
NVDA, P, SMCI, SNX, STX, TECK, TTMI, UTHR, VICR, WDC).
Every one is `status: draft`, Shariah `unverified`, entry/stop/target/
invalidation formula-filled from Yahoo data — none is a buy signal on its
own. **30 pre-existing draft cards from the 2026-07-13 run are still
unreviewed** (never promoted to `planned`); several of their price levels
(entry/stop/target) are now 5-6 weeks stale versus current quotes — e.g.
ULTA's card entry is $452 vs today's ~$522 lead price. Re-scaffold with
`--force` on any you intend to act on so the levels reflect current prices,
rather than trusting a July snapshot.

No card currently carries `status: planned` or `live`, so there is no
BUY-CANDIDATE this run — only the compliance-gate and edge-gate can produce
one, and neither has been cleared on any name yet.

## Discipline guard

No `transactions.csv` / `journal.csv` exist yet (no closed round-trip trades
logged besides FIG's realized +$54.95, which predates the journal script's
use). Sample too small to compare net-of-cost performance to the SPUS
benchmark — flag revisits once there's a meaningful trade count
(`journal_min_trades: 20`).

## Follow-ups

1. **Re-screen BMNR in Zoya/Musaffa** — resolve the ratio-pre-check /
   broker-app conflict before adding to the position (top priority — see
   Action flag 1).
2. Update `holdings/now-servicenow.md`'s `catalyst.date` to `2026-10-28`
   (Q3 FY2026) now that Q2 has reported.
3. Fill in the open `TODO` fields on both holding cards (`conviction`,
   `variant_view`, `initial_stop`, `target_price`, `invalidation`,
   `pre_mortem` on NOW; a written thesis/risks/notes on BMNR) — verdict.py
   and recommend.py can't compute an R-multiple or a real conviction record
   without them.
4. If any LEAD above is worth pursuing, re-scaffold its card with `--force`
   for current levels, write a variant view, screen it in Zoya/Musaffa, then
   flip `status: planned` to enter the funnel.
5. Curate `watchlist.md` if there are specific names/themes to track by hand
   — it's currently empty, so all new-idea surfacing this run came from
   machine discovery only.

---
Not financial advice. Shariah status shown here is a broker-app record or a
mechanical ratio pre-check, never a fatwa — verify independently in
Zoya/Musaffa before any trade.
