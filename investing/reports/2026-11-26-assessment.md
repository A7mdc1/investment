# Portfolio Assessment: 2026-11-26

This is not financial advice. It is decision support only, and every buy, sell or hold call is
yours. Shariah status below comes from the broker app's recorded screen or from a mechanical
pre-check. Neither one is a fatwa, so verify in Zoya/Musaffa before acting.

## What ran this cycle

1. `discover.py` ran on live Yahoo data and kept the top 50 leads.
2. `scaffold.py --all-leads` added 29 new DRAFT cards and left 21 existing cards unchanged.
3. `prices.py`, `shariah.py`, `dcf.py`, `signals.py`, `verdict.py` and `recommend.py` all ran on
   live data with no data gaps.

There is still no `transactions.csv`, so the discipline guard stays dormant. No trades have
been recorded since the 2026-08-19 report. The last run was 99 days ago.

## Headline: both holdings fell hard, and both Shariah screens are now stale

| | 2026-08-19 | 2026-11-26 | Change |
|---|---|---|---|
| NOW | $128.63 (+11.8% vs cost) | **$92.16 (-19.8% vs cost)** | -28% |
| BMNR | $20.54 (+33.1% vs cost) | **$13.44 (-12.9% vs cost)** | -35% |
| Portfolio | $1,105.51 | **$779.52** | **-29.5%** |

For comparison, SPUS is about -10% over the past month. ETH-USD is about $1,692, down from
about $2,687 three months ago.

## Verdicts (lead with this)

These verdicts are your own rules in `rules.md` resolving mechanically. They are not advice.

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119: hold, do not add)
- Price is **$92.16**, -19.8% vs the $114.97 cost basis, and at 7% of its 52-week range.
- The chandelier trailing stop is **$137.25**. Price is about 33% *below* it. TRAIL_STOP does
  **not** fire because `trade_type: core` is exempt by design. The stop is shown for context
  only.
- 6-1 momentum is +42.4%. That number is distorted by the skip-last-month window, which
  excludes the crash.
- The PM record from recommend.py is a mechanical proxy. Conviction is LOW because there is no
  stated reward:risk, variant view, stop or invalidation in the front-matter.
- DCF intrinsic value is $119.65 vs $92.16, or +29.8%. Assumptions: 18% growth over 5 years,
  3% terminal growth, 10% discount rate.
- The recorded catalyst is "Q2 FY2026 earnings" and is out of date. Yahoo's next earnings
  date is **2027-01-27**, with a consensus EPS of about $1.07.

**BMNR -> HOLD** (RULE: DEFAULT, no rule fired)
- Price is **$13.44**, -12.9% vs the $15.43 cost. Price is about 25% below the $17.83
  chandelier stop, which again does not apply to `core`.
- ATR is 11.3%, so the vol throttle says size down. 6-1 momentum is +12.3%, distorted the same
  way as NOW's.
- DCF gives -$6.53. The model does not fit a crypto-treasury business, so ignore it.
- The holding file still has only a placeholder thesis ("NEW position — screen compliance..."),
  with no stop, target or invalidation.

Portfolio notes: only 2 holdings, so concentration rules stay muted until there are at least 4
names. NOW is 82.8% of the portfolio. Both names trip the vol throttle (ATR ≥ 6%).

## Action flags (priority order)

1. **MANDATE: both Shariah screens are stale (>100 days).** NOW was screened on 2026-06-09 and
   BMNR on 2026-07-07. recommend.py marks both `REVIEW: re-screen`. Re-screen both in
   Zoya/Musaffa.
2. **MANDATE: BMNR fails the business-activity pre-check again.** Yahoo classifies it as
   Financial Services / Capital Markets. This conflicts with the recorded "compliant" status,
   and the conflict has been open since 2026-08-19. Resolve it in the
   re-screen.
3. **NOW drawdown:** -20% vs cost. signals.py says to revisit whether the thesis still holds.
   See the per-holding read below.
4. **NOW valuation:** the P/E ~119 figure is the recorded front-matter value. At about $92 the
   live multiple is lower, so update `pe`/`last_price` in the holding file. The VALUATION_RICH
   verdict is being driven by a stale field.
5. **Incomplete PM records:** both holdings are missing `initial_stop`, `target_price`,
   `invalidation` and `conviction`. Without them, HARD_STOP and R-multiple rules cannot fire
   for you.

## Per-holding read (catalysts and news, via web)

### NOW
**What happened.**
- Shares fell about 27% on 2026-10-29 after Q3 results. Coverage cites:
  - a smaller-than-usual beat and softer guidance
  - investor fears that AI agents will disrupt seat-based software
  - questions about whether early contract renewals flattered cRPO
- One outlet reports a Pomerantz LLP securities investigation tied to the cRPO question.
- Further selling came with a broad software selloff, for example -6.5% to about $92.90 on
  2026-11-17. Subscription growth was still reported at about 21%.

**Case to keep.**
- The recorded thesis metric, ~21-22% subscription growth, was *reported as intact*.
- The DCF now shows about +30% upside on your own assumptions.
- The price sits near the bottom of its 52-week range.

**Case to trim.**
- Your own "what would change my mind" text says "guidance cut tied to AI-agent... traction".
  Softer guidance and AI-disruption fears are exactly what drove the selloff, so check the Q3
  guide against that wording.
- The cRPO-quality question goes to the durability of the subscription thesis.
- The position is 83% of the account with no defined stop.

Sources:
- [Motley Fool](https://www.fool.com/investing/2026/11/01/why-the-27-crash-in-servicenows-stock-looks-like-a/)
- [Forbes](https://www.forbes.com/sites/petercohan/2026/11/02/servicenow-stock-down-32-a-buying-opportunity/)
- [24/7 Wall St.](https://247wallst.com/investing/2026/11/10/servicenow-just-dropped-30-in-a-month-stay-the-course-or-just-stay-away/)
- [Pluang](https://pluang.com/en/news-feed/investigasi-servicenow-now-pertanyaan-crpo-hilangnya-kapitalisasi-pasar)
- [GuruFocus/TradingView](https://www.tradingview.com/news/gurufocus:b855a0db6094b:0-servicenow-stocks-fall-6-51-despite-21-subscription-growth-as-software-selloff-deepens/)
- [Trefis](https://www.trefis.com/stock/now/articles/627538/how-risky-is-servicenow-stock-in-a-falling-market/2026-11-22)

Figures differ between sources. Check the Q3 release and 10-Q yourself.

### BMNR
**What happened.**
- BMNR trades as a leveraged proxy on ETH. ETH fell from about $2.7k to about $1.7k over three
  months.
- Per company releases, Bitmine holds about 6.09M ETH, with about 5.23M staked. Total holdings
  fell from $14.5B at the start of November to $11.1B on 2026-11-23.
- A headline reports that Tom Lee capped ETH buying at a 5% supply limit.
- A $0.01 dividend was declared, with a record date of 2026-12-08 and payment on 2026-12-29.
- Yahoo shows the next earnings on 2027-01-12.

**Case to keep.** You get ETH exposure at whatever discount or premium to NAV the stock
trades at. Check mNAV yourself.

**Case to trim.**
- No thesis is recorded.
- Volatility is extreme (ATR 11%).
- The Shariah business screen is unresolved. Staking income and treasury activity are exactly
  what the Capital Markets flag is about.

Sources:
- [Nasdaq press release](https://www.nasdaq.com/press-release/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-606-million-tokens)
- [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001829311/000149315226054131/ex99-1.htm)
- [CNN quote page](https://www.cnn.com/markets/stocks/BMNR)

## Suggested actions (from YOUR rules)

- **Rule VALUATION_RICH fired -> NOW: hold, do not add.** This rests on the stale recorded P/E.
- **Rule DEFAULT -> BMNR: HOLD.**
- TRAIL_STOP, HARD_STOP, THESIS_BREAK, TAKE_PARTIAL: **did not fire**. Trail is exempt for
  `core`. HARD_STOP has no `initial_stop` set. No `thesis_broken` flag is set.
- The routine never auto-trades. If you execute anything, run `/apply-trade` so holdings and
  the ledger update.

## DCF

| Ticker | Intrinsic | Price | Upside | Assumptions |
|---|---|---|---|---|
| NOW | $119.65 | $92.16 | +29.8% | g5=18%, tg=3%, r=10% |
| BMNR | -$6.53 | $13.44 | n/m | g5=5%, tg=2.5%, r=10%. Model unsuitable for a crypto treasury |

## New ideas / leads

recommend.py's `ideas` array is **empty**. No card is `planned` with a verified compliant
screen, so **nothing is a BUY-CANDIDATE**. All 50 discovery rows are **LEAD / RESEARCH**, and
Shariah is UNVERIFIED for every one. See `leads.md`.

New DRAFT cards this run (29):

AAPL, ANET, APA, ASND, BBY, BKR, COHR, DDOG, DIOD, FN, FRO, HSY, JBL, KEYS, LLY, LSCC, NTAP,
NUE, PR, PSX, SANM, SNA, STLD, TS, TXN, UI, VIAV, VLO, XOM.

Each one is `RESEARCH — DRAFT awaiting your review (set status: planned to approve)`. Every
level is a formula output.

Highest discovery reward:risk where stop < entry:

| Lead | Entry | Target | Stop | Discovery R:R | Earnings |
|---|---|---|---|---|---|
| SANM | ~$138.57 | $274.45 | $136.43 | 20.0:1 | 2027-02-01 |
| FN | ~$289.70 | $626.25 | $278.46 | 20.0:1 | 2027-02-01 |
| VIAV | ~$27.23 | $56.86 | $25.57 | 17.9:1 | 2027-02-03 |
| DIOD | ~$75.70 | $125.96 | $73.59 | 14.3:1 | 2027-02-09 |
| LSCC | ~$98.23 | $156.92 | $95.12 | 12.6:1 | 2027-02-08 |

R:R figures this high come from formula targets, so treat them as screening artifacts until
you set your own levels.

### Engine caveat: 30 of 50 leads have a stop at or above entry

30 of the 50 leads have a chandelier stop at or above the EMA20 pullback entry. Examples are
XOM, MSFT, AMD, MU and AVGO. This happens when the trail sits above the EMA20, so the plan is
incoherent. reward:risk shows `n/a`, and the scaffold leaves `target_price: null`.

These cards can never pass the asymmetry gate as written. Either discard them, or re-level
them by hand, for example with a structure-based stop below the entry. A code fix in
`scaffold.py`/`discover.py` would be needed to choose a different stop when
chandelier ≥ entry. That fix is not made in this run.

## Follow-ups (prioritized)

1. **Re-screen NOW and BMNR in Zoya/Musaffa.** Both screens are stale, and the BMNR business
   flag is unresolved. Record the date and status in each holding file.
2. **NOW:** read the Q3 FY2026 release, guidance and the cRPO commentary. Decide whether
   "guidance cut tied to AI-agent traction" (your own invalidation text) has been met.
3. **Set `initial_stop`, `target_price`, `invalidation` and `conviction` on both holdings**
   so your rules can act. Update NOW's stale `pe`, `last_price`, 52-week range and catalyst
   date (earnings 2027-01-27).
4. **BMNR:** write an actual thesis, or decide that it is a tactical ETH position. Note the
   dividend record date of 2026-12-08 and earnings on about 2027-01-12.
5. Review the 29 new DRAFT cards, or archive the ones with a stop at or above entry.
6. Consider fixing the scaffold's stop selection (engine caveat above).

---
*Not financial advice. Mechanical outputs and web summaries can be wrong or stale. Verify
every compliance status in Zoya/Musaffa before acting.*
