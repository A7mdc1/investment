# Portfolio Assessment — 2026-11-17

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 170-name raw pool; 4 dropped on liquidity, 77
dropped on the Shariah ratio pre-check; top 50 kept) → `scaffold.py
--all-leads` (26 new DRAFT cards; 24 existing cards left unchanged) →
`prices.py` / `shariah.py` / `dcf.py` / `signals.py` / `verdict.py` /
`recommend.py` — all live. Yahoo returned some HTTP 429s (rate limiting) but no
data gaps. Still no `transactions.csv` / `journal.csv`, so `journal.py` and the
discipline guard remain dormant.

**Since the last report (2026-08-19, ~3 months ago):** no trades recorded in
the holdings files. The book is down sharply: total value **$807.30** vs.
$1,105.51 at the last report. NOW fell ~28% (most of it after its Oct 28
earnings), and BMNR gave back most of its gain.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically, not advice.

**NOW -> HOLD** (RULE: VALUATION_RICH — recorded P/E 119.02 >= pe_rich 50).
Live price **$92.40**, **-19.6%** vs. the $114.97 cost basis.

> **Note: DRAWDOWN_REVIEW (threshold 20%) missed by ~0.4 points.** `signals.py`
> rounds and already flags "Down -20% vs cost — revisit the thesis". One more
> soft day flips `verdict.py` to REVIEW. Also, the P/E driving VALUATION_RICH
> is the hand-entered `pe: 119.02` (and `last_price: 106.40`) in the holding
> file from June. Those values are stale after a ~28% drop. The HOLD label is
> resting on an old number.

| PM-grade record (recommend.py — mechanical proxies, not a conviction call) | |
|---|---|
| Conviction | LOW — "missing reward:risk or a stated thesis — cannot self-assess" |
| Shariah | **REVIEW** — recorded compliant, but screen dated 2026-06-09 is >100 days old (now stale); ratio pre-check clean (debt 2.5%, liquid 6.6%) |
| Target / method | $119.65, DCF intrinsic value (+29.5%) |
| Trailing stop (chandelier) | $139.81 — price is ~34% **below** it (`trade_type: core` exempts NOW from TRAIL_STOP) |
| 20-EMA | $112.77 — price well below |
| 6m momentum (skip last month) | +42.7% (the skip-month window excludes the post-earnings collapse, so this overstates current strength) |
| Daily ATR | 7.1% — above the 6% vol-throttle line |
| Would buy today? | Mechanically "yes" (gates read only the recorded fields) — conviction LOW; no variant view, stop, target or pre-mortem on file |
| What changes verdict | `thesis_broken: true`, a fresh Shariah screen, or the 20% drawdown line being crossed (-> REVIEW) |

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$16.05**,
**+4.0%** vs. the $15.43 cost basis (was +33.1% at the last report).

| PM-grade record (recommend.py — mechanical proxies) | |
|---|---|
| Conviction | LOW — no thesis/target/stop on file |
| Shariah (recorded) | **REVIEW** — broker_app compliant, screened 2026-07-07, now >100 days old (stale) |
| Shariah (mechanical pre-check, this run) | **FAIL — 2nd consecutive run** — industry `Capital Markets` / sector `Financial Services`; "core business fails screen" |
| DCF | -$6.53 intrinsic (meaningless for a crypto-treasury company — treat as a data gap, see DCF section) |
| Trailing stop (chandelier) | $20.19 — price ~20% **below** it (core-exempt) |
| 6m momentum | +15.8% |
| Daily ATR | 9.0% — above the vol-throttle line |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either way) |

- `verdict.py` note: only 2 holdings — concentration rules muted until >= 4 names.
- **Portfolio notes (VOL_THROTTLE):** `BMNR ATR 9.03% — size down per vol throttle`; `NOW ATR 7.1% — size down per vol throttle`.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $16.05 | 10 | $15.43 | $160.50 | +4.0% | 19.9% |
| NOW | $92.40 | 7 | $114.97 | $646.80 | -19.6% | 80.1% |

**Total value: $807.30** | Cost: $959.09 | **Total return: -15.8%** (-$151.79 unrealised)

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are now stale (>100 days).** NOW was
   screened 2026-06-09 and BMNR 2026-07-07. `recommend.py` has downgraded both to
   `shariah_status: REVIEW`. This is a policy issue, not a price call.
2. **[Mandate, 2nd run in a row] BMNR business-activity pre-check FAILS**
   (`Capital Markets`). This is unchanged from 2026-08-19 and still
   unresolved. The company's own Nov 9 release describes it as an ETH
   treasury: 6.07M ETH, 5.23M of it staked (~$11.7B), $14.3B total
   crypto/cash/securities. That is the profile a business-activity screen is
   built to question. COMPLIANCE_GATE still reads only the recorded field, so
   nothing in the pipeline will act on this until you update the holding file.
   [Finviz / company PR](https://finviz.com/news/419085/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-607-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-143-billion)
3. **[Drawdown / NOW] -19.6% vs. cost.** `signals.py` already flags the
   drawdown, and `verdict.py`'s DRAWDOWN_REVIEW (20%) is about 0.4 points away.
   Your rule's pre-set action at 20% is "REVIEW thesis".
4. **[Data hygiene / NOW]** The front-matter `pe: 119.02` / `last_price: 106.40` /
   52-week fields are hand-entered from June. They drive VALUATION_RICH and are
   now stale. The catalyst field still says "Q2 FY2026 earnings" (`date: null`),
   and that event has passed.
5. **[Catalyst / BMNR]** Earnings Whispers lists the next BMNR report for
   **~2026-11-23** (6 days out, unconfirmed — verify with company IR). There
   is no gap plan on file for a 9%-ATR name.
   [Earnings Whispers](https://beta.earningswhispers.com/go/w/BMNR)
6. **[Catalyst / NOW]** The next report is **~2027-01-27** (71 days, just
   outside the 60-day horizon).

## Per-holding read

### NOW — ServiceNow, Inc
**What happened:** Q3 2026 (Oct 28) beat on revenue. Subscription revenue
was $3.988B (+21% y/y) and cRPO was $13.65B (+20.5%). FY26 subscription
guidance edged up to $15.78–15.79B, the FCF-margin guide rose 100 bp to 36%,
and the AI net-new-ACV target was raised to $1.7B. **But** Q4 cRPO growth was
guided to 18.5% (cc), which signals deceleration, and EPS missed. Shares fell
~27% on Oct 29 (reportedly the worst day in the company's history) and kept
sliding with the Nasdaq to ~32% below the Oct 28 close. Coverage also points
to sector-wide fears that AI erodes seat-based software pricing, and to
integration risk from the Armis/Veza deals (Armis alone is a ~125 bp drag on
FY subscription growth).
[ServiceNow IR](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Third-Quarter-2026-Financial-Results/default.aspx) ·
[AI Weekly](https://aiweekly.co/alerts/servicenow-shares-sink-15-after-hours-as-q4-crpo-guide-lands-below-street) ·
[MarketBeat](https://www.marketbeat.com/instant-alerts/price-servicenow-nyse-now-shares-down-268-after-earnings-miss-2026-10-29/) ·
[TIKR](https://www.tikr.com/blog/servicenow-cfo-calls-ai-disruption-fears-false-the-stock-is-down-32-since-its-report) ·
[24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)

**Case to keep:** Your recorded thesis ("durable ~20% subscription grower; AI
agents the forward driver") is numerically intact. Revenue growth is still
~21%, the AI ACV target was raised a second time, and margins are expanding.
The DCF (18% growth / 10% discount, your overrides) now sits **~29.5% above**
price; at the last report the price was ~7% above it. The CFO publicly called
the AI-disruption fears "false".

**Case to cut/trim:** The market is re-pricing *forward* growth (cRPO
deceleration), not the trailing numbers. Price is ~34% below the chandelier
stop and far below the 20-EMA. The position is 80% of the book with no
`initial_stop`, `invalidation`, or `pre_mortem` on file to judge the drawdown
against. It is also a ~-20% loss on a name tagged `core`, which exempts it from
your technical stop rules. The next fundamental test is Jan 27.

The rule set does not pick between these; the missing invalidation line is what
would.

### BMNR — Bitmine Immersion Technologies, Inc
**What happened:** ETH holdings grew to 6.07M (Nov 9 release; ETH ~$2,234),
with ~86% staked. The stock is down ~49–55% over the trailing year per quote
sites. It was $20.54 at the last report and is $16.05 now. Its price tracks ETH
and the treasury premium, not operating cash flow.
[Simply Wall St](https://simplywall.st/stock/NYSE/BMNR?blueprint=4603518) ·
[Benzinga](https://www.benzinga.com/quote/BMNR/charts)

**Case to keep:** It is still above cost (+4%). The ETH stack and staking
yield keep growing.

**Case to flag:** This is the 2nd consecutive business-activity pre-check fail,
and the recorded screen is now stale. The holding file still has no thesis,
stop, target, or pre-mortem 4+ months after entry. A 9% daily ATR into a
likely Nov 23 print leaves no gap plan.

## Suggested actions (from YOUR rules, rules.md)

- **COMPLIANCE_GATE** — does **not** fire for either name: both still carry
  `status: compliant`. Recommend.py downgrading both to REVIEW for staleness is
  the closest the pipeline gets. Re-screening is on you.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add (on a stale recorded P/E —
  see flag 4).
- **DRAWDOWN_REVIEW -> NOW**: **not fired, -19.6% vs. the 20% threshold**. The
  rule's pre-set action, once crossed, is to REVIEW the thesis.
- **TRAIL_STOP -> NOW / BMNR**: both prices sit **below** their chandelier
  levels ($139.81 / $20.19). The rule does not fire only because
  `trade_type: core` exempts them. Name that exemption as a choice you made, not
  something the data cleared.
- **VOL_THROTTLE fired -> BMNR (9.0%) / NOW (7.1%)**: "size down" — relevant only
  if you add.

*If you execute anything from this report, run `/apply-trade` so holdings
files and the ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $92.42 | +29.5% | growth_5y 18%, terminal 3%, discount 10% (your overrides) |
| BMNR | -$6.53 | $16.06 | n/m | growth_5y 5% default, terminal 2.5%, discount 10% — the cash-flow model doesn't fit an ETH-treasury company; treat as a data gap |

The NOW upside depends on 18% 5-year growth. Q4 cRPO guided to 18.5% means the
assumption is still roughly in line, but there is no margin for further
deceleration.

## New ideas (watchlist.md)

`watchlist.md` still has no hand-curated tickers. `recommend.py`'s `ideas` array
is empty, so there are **0 BUY-CANDIDATEs** (expected: none of the 89 cards in
`setups/` has been flipped to `status: planned`).

## Draft & planned setups — 50 leads, 26 fresh DRAFT cards

Every card below is **RESEARCH — DRAFT awaiting your review (set status:
planned to approve)**. Every level is a formula output and Shariah is
UNVERIFIED. These are proposals, never buys. The full table is in
`leads.md`.

Only **3 of 50** clear to LEAD tier (R:R >= 2 and a catalyst within 60 days):

| Ticker | Verdict | Entry | Stop | Target | R:R | Catalyst | Days |
|---|---|---|---|---|---|---|---|
| SNX | LEAD | $232.22 | $229.78 | $298.10 | 12.8:1 | earnings 2027-01-07 | 51 |
| AVGO | LEAD | $336.98 | $318.35 | $493.37 | 8.4:1 | earnings 2026-12-09 | 22 |
| ADI | LEAD | $384.66 | $375.10 | $444.69 | 6.2:1 | earnings 2026-11-24 | 7 |

Caveats before you spend review time:
- **The SNX, AVGO and ADI cards on disk are stale.** They were scaffolded
  2026-08-19 and still reference August/September prints. For example, SNX's
  card says "enter near $252.66 ahead of the 2026-09-24 print". `scaffold.py`
  skips existing cards, so the levels above (from today's discovery run) do
  **not** match the card files. Re-scaffold with `--force` or edit by hand
  before approving.
- SNX's 12.8:1 comes from a stop only ~1% under entry. ADI reports in 7 days, so
  any entry needs a valid `earnings_plan`.
- **24 of 50 leads have a stop *above* entry (R:R n/a)** — e.g. NVDA, MU,
  DELL, CRDO, PLTR, MSFT. These names are trading below their chandelier
  trail (downtrends), so the formula stop is meaningless. Ignore those levels.
- Recurring Shariah questions: **PLTR** (government/defense) is still unresolved.
  New energy/shipping/REIT-adjacent names (APA, PR, PSX, DINO, FRO, HST — HST is
  a REIT, typically a lodging/finance question) need a real business screen.
- 26 new DRAFT cards: SANM, VIAV, FN, BBY, UI, COHR, SNA, DIOD, LSCC, FRO, HSY,
  ANET, NTAP, NTNX, KEYS, SMTC, ASND, LLY, TS, AAPL, PSX, TXN, HST, APA, JBL, PR.

## Follow-ups (priority order)

1. **[Mandate] Re-screen BOTH holdings in Zoya/Musaffa.** Both are stale. For BMNR,
   ask the business-activity question specifically (2nd consecutive
   pre-check fail).
2. **[Decision] NOW is at -19.6%, at the edge of your DRAWDOWN_REVIEW line, and
   80% of the book.** Write the missing `invalidation`, `initial_stop`, and
   `pre_mortem` so the next move has something to be judged against. Update the
   stale `pe` / `last_price` / catalyst (Q4 report ~2027-01-27).
3. **[Time-boxed] BMNR earnings ~2026-11-23** (unconfirmed). Decide on a gap
   plan for a 9%-ATR name, and fill the empty PM fields in `holdings/bmnr.md`.
4. **[Housekeeping] 89 DRAFT cards, many stale** (catalysts passed). Consider
   pruning, or re-scaffolding the 3 LEADs with `--force`.
5. **[Infrastructure — still open]** No ledger. Log the FIG sale and BMNR buy via
   `/apply-trade` to unlock the journal and the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Reports Third Quarter 2026 Financial Results — ServiceNow IR](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Third-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow Shares Sink 15%+ After Hours as Q4 cRPO Guide Lands Below Street — AI Weekly](https://aiweekly.co/alerts/servicenow-shares-sink-15-after-hours-as-q4-crpo-guide-lands-below-street)
- [ServiceNow shares down 26.8% after earnings miss — MarketBeat](https://www.marketbeat.com/instant-alerts/price-servicenow-nyse-now-shares-down-268-after-earnings-miss-2026-10-29/)
- [ServiceNow CFO Calls AI Disruption Fears "False" — TIKR](https://www.tikr.com/blog/servicenow-cfo-calls-ai-disruption-fears-false-the-stock-is-down-32-since-its-report)
- [ServiceNow Just Dropped 30% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [ServiceNow Q3 2026 earnings summary — Quartr](https://quartr.com/events/servicenow-now-q3-2026_3gnKPsN5)
- [Bitmine ETH holdings reach 6.07M tokens, $14.3B total — Finviz](https://finviz.com/news/419085/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-607-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-143-billion)
- [BMNR — Simply Wall St](https://simplywall.st/stock/NYSE/BMNR?blueprint=4603518)
- [BMNR charts — Benzinga](https://www.benzinga.com/quote/BMNR/charts)
- [BMNR earnings date — Earnings Whispers](https://beta.earningswhispers.com/go/w/BMNR)
