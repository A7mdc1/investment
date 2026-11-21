# Portfolio Assessment — 2026-11-21

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio/business-activity pre-check, neither a fatwa —
verify independently in Zoya/Musaffa before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 170-name raw pool; 4 dropped on liquidity, 76
dropped on the Shariah ratio/business knockout; top 50 kept) →
`scaffold.py --all-leads` (27 new DRAFT setup cards; 23 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps. Still no
`transactions.csv`, so the discipline guard stays dormant.

**Since the last report (2026-08-19, ~3 months ago):** no trades recorded.
The book has fallen from **$1,105.51 to $743.07 (-32.8%)**, moving from
+15.3% to **-22.5%** against cost. Both positions are now well below their
computed trailing stops.

## Verdicts (lead with this)

These are YOUR rules from `rules.md` resolving mechanically — not advice.

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW — down -23.8% vs cost; VALUATION_RICH
also active: P/E ~119, hold/do not add). Live price **$87.61** vs. $114.97 cost.

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW — "missing reward:risk or a stated thesis — cannot self-assess" |
| Shariah | **REVIEW** — recorded compliant (broker app), but screened 2026-06-09, >100 days old → stale |
| Mechanical ratio pre-check | clean (debt 2.6%, liquid 6.9%) |
| DCF intrinsic value | $119.65 vs $87.61 → +36.6% (growth 18%, terminal 3%, discount 10% — see DCF section) |
| Trailing stop (chandelier) | $139.70 — **price is ~37% below it** (TRAIL_STOP does not fire: `trade_type: core` is exempt) |
| EMA fast | $106.62 — price below |
| 6m momentum (skip last month) | +53.7% — *excludes the last month, so it does not capture the post-earnings crash; treat as stale* |
| Would buy today? | **No** (recommend.py) |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$12.98**, -15.9%
vs. $15.43 cost. **The HOLD is mechanical only — the unresolved Shariah
business-activity flag from the last report is still open (Action Flag #1).**

| PM-grade record (recommend.py, mechanical proxy) | |
|---|---|
| Conviction | LOW — no thesis/stop/target recorded |
| Shariah (recorded) | **REVIEW** — broker app "compliant", screened 2026-07-07, now >100 days old → stale |
| Mechanical pre-check | **FAIL** — industry `Capital Markets`; core business fails the screen (2nd consecutive run) |
| DCF intrinsic value | -$6.53 vs $12.98 — not meaningful (model does not fit an ETH-treasury company) |
| Trailing stop (chandelier) | $18.82 — **price is ~31% below it** (core-exempt, so no SELL fires) |
| 6m momentum (skip last month) | +19.2% — same caveat as NOW |
| Would buy today? | Mechanically "yes" — but that check cannot see the business-activity fail |
| What changes verdict | A Zoya/Musaffa business-activity re-screen (either direction) |

**Portfolio notes (verdict.py):**
- Only 2 holdings — concentration rules muted until >= 4 names.
- **VOL_THROTTLE:** BMNR ATR 11.13%, NOW ATR 7.53% — "size down per vol throttle".

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $12.98 | 10 | $15.43 | $129.80 | -15.9% | 17.5% |
| NOW | $87.61 | 7 | $114.97 | $613.27 | -23.8% | 82.5% |

**Total value: $743.07** | Cost: $959.09 | **Total return: ~-22.5%** (-$216.02 unrealised)

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are now stale (>100 days).**
   `recommend.py` downgrades both to Shariah `REVIEW`. Re-screen both names in
   Zoya/Musaffa. This is policy, not a price call.
2. **[Mandate — carried over, still unresolved] BMNR fails the mechanical
   business-activity pre-check** (`Capital Markets`). It conflicts with the
   recorded "compliant". BMNR describes itself as an Ethereum treasury
   company holding ~6.08M ETH (~4.97% of supply as of 2026-11-15). Under
   this repo's Gate 1, a confirmed fail is an absolute SELL whatever the P/L.
   COMPLIANCE_GATE still reads only the recorded field, so the pipeline
   cannot raise this flag by itself.
3. **[Drawdown / NOW] DRAWDOWN_REVIEW fired (-23.8%).** NOW fell ~26.9% on
   2026-10-29 after Q3 results: guidance for Q4 cRPO growth slowed to ~18.5%
   cc from 21% in Q3. Software sold off again in November (-6.5% on 11-17
   amid worries that AI hurts seat-based pricing). The price is near its 52-week
   low ($81.24).
4. **[Technical] Both positions are far below their chandelier trailing
   stops** (NOW ~37% below, BMNR ~31% below). TRAIL_STOP is exempt for
   `trade_type: core`. If you meant either position to be stop-managed, that
   exemption hid the signal.
5. **[Valuation / NOW] P/E ~119 (recorded)** — VALUATION_RICH still says do
   not add. The DCF now shows +36.6% to its model value, but that relies
   on 18% growth for 5 years, which is exactly what the cRPO slowdown puts
   in question.

## Per-holding read

### NOW — ServiceNow, Inc
**Case to keep:** The DCF (18% growth) now prices it ~27% below model value.
cRPO is still growing ~18.5% cc, so this is a slowdown, not a collapse. The
next hard catalyst is Q4 FY2026 earnings in **late January 2027** (~65–70 days,
just outside the 60-day horizon). The recorded thesis ("durable subscription
grower; AI-agent expansion") is not formally broken.

**Case to trim/exit:** Your own recorded "what would change my mind" is
"subscription growth decelerating meaningfully below current ~21-22% YoY".
Guided cRPO of 18.5% is a step toward that line, so check whether it is
over it by your definition. The Armis + Veza deals add integration risk
(goodwill ~$10B). The AI seat-pricing fear hits the whole sector. The stock
is below its fast EMA and far below its trailing stop. It is 82.5% of the
book, so this one name drives most of the portfolio's result.

**The rules say REVIEW: re-underwrite ("would I buy this here today?") and
fill in `invalidation`, `initial_stop` and `target_price` so future runs can
judge it.**

### BMNR — Bitmine Immersion Technologies, Inc
**Case to keep:** It is still adding ETH (6.08M tokens, ~4.97% of supply)
and has a large crypto/cash treasury (~$11.8B as of 11-15). Its price moves
with ETH, and management blamed the recent ETH drop on margin selling and
cash-raising before a large IPO, not on anything company-specific.

**Case to flag:** The business-activity compliance question (above) is the
first thing to settle. The price is -48.9% over the period Simply Wall St
shows. There is still no thesis, stop, target or pre-mortem in the holding
file, three months after entry.

**Verdict: HOLD (no rule fired) — but compliance resolution comes first.**

## Suggested actions (from YOUR rules, rules.md)

- **DRAWDOWN_REVIEW fired -> NOW** (down -23.8%): REVIEW — re-underwrite the thesis.
- **VALUATION_RICH fired -> NOW**: hold, do not add.
- **VOL_THROTTLE fired -> BMNR, NOW**: size down any adds (ATR 11.1% / 7.5%).
- **SHARIAH staleness -> BMNR, NOW**: both >100d → re-screen.
- **COMPLIANCE_GATE did NOT fire -> BMNR**: it reads only the recorded field.
  The mechanical fail needs your manual re-screen.
- **TRAIL_STOP did NOT fire** for either — `core` exemption, even though
  both are far below the computed level.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $87.61 | +36.6% | growth_5y 18%, terminal 3%, discount 10% |
| BMNR | -$6.53 | $12.98 | n/a — model does not fit a crypto-treasury business | growth_5y 5% default, terminal 2.5%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md` is still empty, so `recommend.py`'s `ideas` array returned
nothing. No card in `setups/` is `planned`, so there are **0 BUY-CANDIDATEs**,
as expected.

## Discovery — 50 leads, 27 fresh DRAFT cards

**0 of 50 leads clear to LEAD tier this run** (last run: 9). Every name is
RESEARCH:
- **CATALYST_GATE (9 names, R:R >= 3 but next earnings 72–88 days out):**
  FOX 9.9:1, SNA 14.5:1, LSCC 14.0:1, NET 8.3:1, VIAV 20:1*, COHR 20:1*,
  SANM 20:1*, FN 20:1*, CF 8.3:1, plus LLY 5.5:1 and HSY 4.6:1. (*capped at
  the R:R winsorize limit. Stops sit within ~1–6% of entry, so these ratios
  come from a tight stop and are weak.)
- **ASYMMETRY_GATE (most of the rest):** R:R "n/a", because the
  formula-derived **stop is above the current price** (e.g. DELL entry $278
  / stop $406; MU $595 / $802; CRDO $100 / $129). This is a scaffold
  artifact from the broad November selloff (stops are anchored to pre-drop
  highs). **Draft cards built in this state have unusable stop levels**, so
  fix them by hand before any review.
- Earnings inside 3 days: BBY (2.8:1), NTNX, DELL, ADI (11-24); SMTC (11-23).

27 new DRAFT cards: AAPL, ADM, ANET, APA, ASND, BBY, COHR, EXPE, FN, HSY, JBL,
LLY, LSCC, NTAP, NTNX, NUE, PR, PSX, SANM, SMTC, SNA, STLD, TXN, UI, VIAV, VLO,
XOM. That makes 90 cards in `setups/`, all `draft` and all Shariah UNVERIFIED.
They are proposals to review and edit, never buys. Every level is a formula
output. To approve one, edit what you disagree with and set `status: planned`.
Recurring screening questions: PLTR (government/defense), the energy/refiner
cluster (PSX, VLO, DINO, XOM, APA, CNQ, CVE, PR, AR), and FOX (media
business mix).

Full table: `leads.md`.

## Follow-ups (priority order)

1. **[Mandate] Re-screen BMNR and NOW in Zoya/Musaffa.** Both are stale. For
   BMNR, look at the business-activity question specifically (2nd run
   flagged).
2. **[Review] NOW re-underwrite.** DRAWDOWN_REVIEW fired. Compare guided
   cRPO of 18.5% against your own "change my mind" line, and fill in
   `invalidation`, `initial_stop`, `target_price` and `pre_mortem`.
3. **[Decision] Confirm the `core` trade_type is intentional.** That
   exemption is why no stop fired on a -32.8% quarter.
4. **[Housekeeping] Fill in BMNR's PM fields.** They are still empty.
5. **[Tooling] scaffold.py writes stops above entry after a selloff.**
   Many new drafts have stop > entry. The formula needs a guard. Fix it in
   code before relying on these cards.
6. **[Infrastructure] Start `transactions.csv` / `/apply-trade`** so the
   discipline guard can run.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio/business-activity pre-check, neither a
fatwa — verify independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Just Dropped 30% in a Month — 24/7 Wall St. (2026-11-10)](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [What Is Driving ServiceNow Stock? — Trefis (2026-11-18)](https://www.trefis.com/stock/now/articles/626283/what-is-driving-servicenow-stock/2026-11-18)
- [What Is Behind The Move In ServiceNow Stock? — Trefis (2026-10-30)](https://www.trefis.com/stock/now/articles2/621573/what-is-behind-the-move-in-servicenow-stock/2026-10-30)
- [Why ServiceNow Stock Plunged This Week — Mitrade](https://www.mitrade.com/insights/news/live-news/article-8-2219183-20261030)
- [Can Workflow Adoption Drive NOW Stock Post 25% Drop? — Nasdaq](https://www.nasdaq.com/articles/can-workflow-adoption-drive-now-stock-2026-post-25-drop)
- [Bitmine ETH holdings reach 6.08M tokens, $11.8B total — Finviz](https://finviz.com/news/423162/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-608-million-tokens-and-total-crypto-and-total-cash-marketable-securities-holdings-of-118-billion)
- [BMNR — Simply Wall St](https://simplywall.st/stock/NYSE/BMNR?blueprint=4603518)
- [BMNR chart — Benzinga](https://www.benzinga.com/quote/BMNR/charts)
