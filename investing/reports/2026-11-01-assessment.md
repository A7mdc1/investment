# Portfolio Assessment — 2026-11-01

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is a broker-app recorded screen or a mechanical pre-check,
neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran this cycle
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (24 new DRAFT
cards; setups/ now 87 cards, all `draft`) → `prices / shariah / dcf / signals /
verdict / recommend` — all live, no data gaps. Web research was light (2 searches);
`journal.py` not run (no `transactions.csv`).

## Verdicts
**BMNR -> HOLD** (DEFAULT, no rule fired). $20.18, **+30.8%** vs $15.43 cost.
Conviction LOW (no reward:risk/thesis recorded). Shariah: recorded `compliant`
(2026-07-07) but **stale (>100d)**, and the mechanical business-activity pre-check
**still FAILS** (`Capital Markets`). Mechanical chandelier stop $23.86 sits *above*
price (core trade type exempts it from TRAIL_STOP). 6m momentum +22.2%.

**NOW -> HOLD** (VALUATION_RICH, P/E ~119: hold, do not add). $105.12, **-8.6%**
vs $114.97 cost (was $128.63 / +11.8% on 08-19). Conviction LOW. Shariah recorded
`compliant` (2026-06-09), **stale**. Chandelier stop $136.60 is ~30% above price
(core exempt). 52w-range position 15%. Next-earnings note in the holding file is
outdated (see below).

Proxies above are mechanical, not a real conviction call. Portfolio note: ATR
~7.2% on both names (vol-throttle: size down); concentration muted (<4 names).

## Snapshot
| Ticker | Price | Shares | Cost | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $20.18 | 10 | $15.43 | $201.80 | +30.8% | 21.5% |
| NOW | $105.12 | 7 | $114.97 | $735.84 | -8.6% | 78.5% |

**Total $937.64** (down from $1,105.51 on 08-19, -15.2%). NOW is 78.5% of the book.

## Action flags
1. **[Mandate] Both Shariah screens are stale** (BMNR 07-07, NOW 06-09; >100d), and
   BMNR's business-activity pre-check fail from the 08-19 report is unresolved.
   Re-screen both in Zoya/Musaffa. Per Gate 1 a confirmed BMNR fail is a hard SELL.
2. **[NOW] Earnings passed.** One automated source (Quiver Quant, uncorroborated)
   reports the Q3 print on 2026-10-28 missed (EPS $1.00 vs $1.03; revenue ~$4.106B vs
   ~$4.136B) with a ~-16.6% share reaction — consistent with the drop from $128.63
   to $105.12. Verify against ServiceNow's release; update the holding's catalyst
   and `last_review` (still 2026-06-15). [Quiver Quant](https://www.quiverquant.com/news/SERVICENOW+%28%24NOW%29+Releases+Q3+2026+Earnings)
3. **[NOW] Valuation** P/E ~119 (recorded) — VALUATION_RICH holds; DCF now shows
   +13.8% upside, but see DCF assumptions (18% growth).
4. **[BMNR] Next earnings** listed ~2026-11-23 (one calendar, unverified).
   [Earnings Whispers](https://beta.earningswhispers.com/go/w/BMNR)
5. **[Concentration/PM fields]** BMNR still lacks thesis_one_liner, variant_view,
   initial_stop, target_price, pre_mortem; NOW lacks variant_view, target, invalidation.

## Per-holding read
**BMNR — keep:** +30.8% vs cost; 6m momentum +22%; buyback programme reported.
**Flag:** unresolved compliance question; DCF is not meaningful for a crypto-treasury
company; no recorded stop/thesis. Verdict stays HOLD mechanically; resolve
compliance first.

**NOW — keep:** durable subscription growth, AI-agent narrative, DCF $119.65 vs
$105.12. **Trim/review case:** down 8.6% vs cost, fresh post-earnings drop on a
reported miss, price ~30% below trailing stop (core exempt), 78.5% of the book, P/E
still rich. The thesis is untested by this print — re-underwrite (`last_review`
is 5 months old). I'm not choosing for you.

## Suggested actions (your rules.md)
- VALUATION_RICH fired -> NOW: hold, do not add.
- COMPLIANCE_GATE reads only the recorded field, so it does not fire for BMNR
  despite the pre-check fail; staleness (>100d) is the actionable trigger for both.
- DRAWDOWN_REVIEW: NOW -8.6%, below the -20% trigger — not firing.
- TRAIL_STOP: not applicable (core). VOL_THROTTLE: ATR ~7% both — size down.

If you execute anything, run `/apply-trade`.

## DCF
| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $20.18 | -96.4% (not meaningful) | growth 5%, terminal 2.5%, discount 10% |
| NOW | $119.65 | $105.12 | +13.8% | growth 18%, terminal 3%, discount 10% |

## New ideas
`watchlist.md` is empty; `recommend.py` ideas = **0 BUY-CANDIDATE** (no card is
`planned`).

## Draft setups — 50 leads, 24 new DRAFT cards
New cards: AAPL, APA, ASND, BBY, BKR, DDOG, EXPE, FLYW, FRO, FSLR, HPE, HSY, HST,
KEYS, LLY, NTAP, NTNX, ORCL-PD, PR, SMTC, SNA, STLD, TS, TXN, VRNS (see `setups/`).
Every card is a formula-based proposal, Shariah **UNVERIFIED** — review and edit,
never buys.

LEAD tier (5): 
| Ticker | R:R | Catalyst | Card |
|---|---|---|---|
| FOX | 13.4:1 | earnings 2026-11-02 | existing |
| FICO | 20.0:1 | earnings 2026-11-04 | existing |
| PAY | 5.5:1 | earnings 2026-11-02 | existing |
| LIF | 5.4:1 | earnings 2026-11-09 | existing |
| EXPE | 3.2:1 | earnings 2026-11-04 | new |

Several catalysts are 1–3 days out, and FOX/FICO stop levels sit very close to
entry (FOX stop $55.83 vs entry $56.20), which inflates R:R — check before trusting
the ratio. Remaining 45 are RESEARCH (asymmetry or catalyst gate); full list in
`leads.md`. Recurring open questions: PLTR (defense business), precious-metals
cluster, and ORCL-PD (a preferred-share symbol — likely not a normal equity).

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa (both stale; BMNR pre-check fail).
2. Verify NOW's Q3 result and re-underwrite; update holding file.
3. Fill BMNR PM fields (thesis, stop, target, pre-mortem).
4. Review leads/draft cards at your pace; none are `planned`.
5. Start logging trades to `transactions.csv` via `/apply-trade`.

---
Not a financial advisor. Verify Shariah status independently in Zoya/Musaffa.
