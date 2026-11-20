# Portfolio Assessment — 2026-11-20

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. I am not a financial advisor. Shariah status shown below is either the
broker app's recorded screen or a mechanical ratio/business-activity pre-check,
neither a fatwa — verify independently in Zoya/Musaffa before acting.

## What ran this cycle

`discover.py` (live Yahoo, 169-name pool; 4 dropped on liquidity, 76 dropped on
Shariah ratio/business flag; top 50 kept) → `scaffold.py --all-leads` (**27 new
DRAFT cards**, 23 existing cards unchanged) → `prices.py` / `shariah.py` /
`dcf.py` / `signals.py` / `verdict.py` / `recommend.py` — all live, no data gaps.
`recommend.py` returned **0 watchlist ideas** (nothing in `watchlist.md` is
gated). No `transactions.csv`, so the discipline guard / `journal.py` stays dormant.

**Since the last report (2026-08-19, ~3 months ago):** no trades recorded. The
book has gone from **+15.3%** to **-19.2%** (−$331 of value), driven by a
software-sector sell-off (NOW) and ETH weakness (BMNR).

## Verdicts (lead with this)

These are YOUR rules in `rules.md` resolving mechanically — not advice.

**NOW -> REVIEW** (RULE: DRAWDOWN_REVIEW — down −21.0% vs cost, > `drawdown_review_pct` 20; also VALUATION_RICH, recorded P/E ~119 ≥ 50 → do not add).
Price **$90.81** vs $114.97 cost. 6m momentum (skip last month) +53.7%.
Chandelier trailing stop **$139.75** — price is ~35% *below* it, but TRAIL_STOP
only fires for `swing`/`momentum`/`catalyst` trade types; NOW is tagged `core`,
so it did not trigger. No `initial_stop` is set, so HARD_STOP cannot fire either.

| PM-grade record (recommend.py — mechanical proxy, not a conviction call) | |
|---|---|
| Conviction | LOW — no reward:risk / stated variant view on file |
| Shariah | **REVIEW** — recorded compliant, but screened 2026-06-09 (>100 d, stale) |
| Target / method | $119.65 — DCF intrinsic value (+31.8%) |
| Stop | $139.75 chandelier (above price — not meaningful as a stop here) |
| Time horizon | core |
| Would buy today? | **No** (recommend.py) |
| What changes verdict | thesis_broken flag, a set `initial_stop`, or the Shariah screen flipping |

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Price **$13.84** vs $15.43
cost (−10.3%). 6m momentum +19.2%. Chandelier stop **$18.94** — price ~27%
below it; again not enforced because BMNR has no `trade_type` (defaults `core`).

| PM-grade record (recommend.py — mechanical proxy) | |
|---|---|
| Conviction | LOW — no thesis on file (holding body still says "NEW position — screen compliance") |
| Shariah | **REVIEW** — recorded compliant 2026-07-07 (>100 d, stale) **and** ratio pre-check FAILS (industry: Capital Markets) |
| Target / method | DCF −$6.53 — model does not fit a crypto-treasury business; ignore |
| Would buy today? | Mechanically "yes", but that reads the recorded Shariah field and ignores the pre-check fail |

Portfolio notes: only 2 holdings — concentration rules muted until ≥ 4 names.
Vol throttle: **BMNR ATR 10.15%, NOW ATR 7.25%** — both above `vol_throttle_atr_pct` → size down.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| NOW | $90.82 | 7 | $114.97 | $635.74 | −21.0% | 82.1% |
| BMNR | $13.85 | 10 | $15.43 | $138.45 | −10.3% | 17.9% |

**Total value: $774.19** | Cost: $959.09 | **Total return: −19.3%** (−$184.90 unrealised)

## Action flags (priority order)

1. **[Mandate] Both Shariah screens are stale** (>100 days). NOW last screened
   2026-06-09 (164 d); BMNR 2026-07-07 (136 d). Re-screen both in Zoya/Musaffa.
2. **[Mandate — carried over, 2nd run] BMNR ratio pre-check FAILS**
   (`industry 'Capital Markets' — core business fails screen`). Its revenue is
   predominantly ETH staking income off a ~$9.5B ETH treasury (Nov 16 update:
   5.23M staked ETH). This conflicts with the recorded "compliant". Unresolved
   since 2026-08-19.
3. **[Rule] NOW DRAWDOWN_REVIEW** — down −21% vs cost; the 52-week-range
   position is 6% (near the low).
4. **[Hygiene] NOW `last_review` is 2026-06-15** — 158 days, past
   `review_cadence_days: 90`. NOW still has no `initial_stop`, `target_price`,
   `invalidation`, `variant_view` or `pre_mortem`; BMNR has no thesis at all.
5. **[Valuation] NOW recorded P/E ~119** (stale front-matter figure) — VALUATION_RICH → do not add.
6. **[Structural] Trailing stops are not enforced on `core` holdings** — both
   names are far below their chandelier stops with no rule firing. If you want
   stop discipline on these, set `initial_stop` or reclassify `trade_type`.

## Per-holding read

**NOW.** The fall is sector-wide, not company-specific: no earnings/filing on the
Nov 17 −6.5% day (Salesforce −9.5% the same day); coverage links the software
sell-off to AI-competition fears (new agentic AI tools) plus valuation pressure
and rotation. Down ~45% over 12 months; next hard catalyst is Q4 FY2026 earnings
in **late January 2027** (outside the 60-day horizon by a few days — date not yet confirmed).
- *Case to keep:* no thesis-breaking company news found; DCF (18% growth, 10% discount) puts value at ~$120, above price; the recorded thesis (subscription growth ~20%+) has not been shown wrong by any reported number.
- *Case to trim/exit:* the drawdown rule fired; the "AI expansion" thesis is precisely what the market is now questioning (AI agents as a substitute for seat-based workflow software); 82% single-name concentration; no stop/invalidation was ever written, so there is no pre-committed exit.

**BMNR.** Effectively a leveraged ETH proxy. ETH weakness (management cited
Nvidia-related margin selling and the upcoming Anthropic IPO drawing flows); B. Riley
cut its target to $27 from $34 (Nov 13). An earnings release was listed for
**Nov 20, 2026** — result not confirmed at time of writing.
- *Case to keep:* small position (18%); 52-week low $12.80 is nearby; price well under analyst targets.
- *Case to exit:* the unresolved Shariah business-activity question (flag #2) is a gate, not a tiebreaker; no thesis on file; ATR >10%.

## Suggested actions (from YOUR rules, rules.md)

- Rule **DRAWDOWN_REVIEW** fired on NOW → your pre-set action: *REVIEW — re-run the full thesis test.*
- Rule **VALUATION_RICH** fired on NOW → *HOLD, do not add.*
- **Review cadence** (90 d) exceeded on NOW → *re-underwrite.*
- **Shariah staleness** on NOW and BMNR → *re-screen before any add.*
- **Vol throttle** on both → *size down* any adds.

The routine never auto-trades. If you execute anything, run `/apply-trade` so
holdings + ledger update.

## DCF (live)

| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $90.81 | +31.8% | 5y growth 18%, terminal 3%, discount 10% |
| BMNR | −$6.53 | $13.85 | n/m | 5y growth 5%, terminal 2.5%, discount 10% — model unsuitable for a crypto treasury |

NOW's +31.8% is entirely a function of the 18% growth assumption — if the
market is right that AI compresses growth, that figure falls fast.

## New ideas

`watchlist.md` produced no gated ideas this run. Discovery wrote 50 **LEADS**
to `leads.md` — all RESEARCH, Shariah UNVERIFIED, EDGE not supplied. Top by
rank: UI, SNA, NET, LSCC, FOX, VIAV, COHR, SANM, FN, BBY. Many R:R figures are
the winsorized cap (20:1) from tight formula stops — treat as artifacts, not
asymmetry. Near-term earnings among leads: FRO (11-20), SMTC (11-23), BBY / NTNX /
DELL / ADI (11-24), NTAP / CRDO (12-01).

## Draft & planned setups

**27 new DRAFT cards** this run: AAPL, ANET, APA, ASND, BBY, COHR, EXPE, FN,
FRO, HSY, JBL, LLY, LSCC, NTAP, NTNX, NUE, PR, PSX, SANM, SMTC, SNA, STLD,
TXN, UI, VIAV, VLO, XOM.

Verdict for every one: **RESEARCH — DRAFT awaiting your review (set status:
planned to approve).** Every level is a Yahoo formula output; approval means
editing what you disagree with, flipping `status: planned`, and screening the
name compliant yourself. No PLANNED/LIVE cards exist → **no BUY-CANDIDATE this run.**

## Follow-ups

1. Re-screen **BMNR** in Zoya/Musaffa (business activity) — open since August.
2. Re-screen **NOW** (stale).
3. Re-underwrite NOW: write `initial_stop`, `invalidation`, `variant_view`, `pre_mortem`; update stale P/E / 52w fields.
4. Write a thesis (or close) BMNR; check its Nov 20 earnings.
5. Decide whether `core` holdings should carry a hard stop.
6. Optionally review the 27 new draft cards (prune ones you'll never trade).

Sources: [Benzinga — NOW drops 7% as software sell-off deepens](https://www.benzinga.com/trading-ideas/movers/26/11/63358717/servicenow-stock-drops-7-as-software-sell-off-deepens) ·
[Benzinga — NOW drops amid new AI tools](https://www.benzinga.com/trading-ideas/movers/26/11/63116691/servicenow-stock-drops-amid-anthropics-new-ai-tools) ·
[GuruFocus — NOW −6.5%](https://www.gurufocus.com/news/9205950/servicenow-now-shares-drop-65-amid-market-selloff-trading-well-below-gf-value) ·
[Trefis — What is driving NOW](https://www.trefis.com/stock/now/articles/626283/what-is-driving-servicenow-stock/2026-11-18) ·
[Investing.com — BMNR](https://www.investing.com/equities/bitmine-immersion-tech) ·
[CNBC — BMNR](https://www.cnbc.com/quotes/BMNR) ·
[SEC 8-K — BMNR](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226052063/ex99-1.htm)

*Not financial advice. Verify all Shariah status in Zoya/Musaffa.*
