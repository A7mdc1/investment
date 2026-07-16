# Portfolio Assessment — 2026-07-16

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, pool widened to top 50 by max-benefit rank,
per `discover_top_n: 50` in `rules.md`) → `scaffold.py --all-leads` (26 new
DRAFT setup cards auto-filled for names without one; 24 existing cards left
unchanged) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still 0 closed trades logged to `transactions.csv` (FIG's
2026-07-13 exit is recorded in `holdings/closed/fig-figma.md`, not yet in a
ledger — discipline guard stays dormant until you start logging via
`/apply-trade`).

This is the **first assessment cycle covering BMNR** (bought 2026-07-13, same
day FIG was sold) — see the compliance flag below.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$15.53**,
**+0.7%** vs. the $15.43 cost basis. **But see the Shariah flag in Action
flags #1 — the mechanical pre-check conflicts with the recorded compliant
status.**

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk **-15.4:1** (skew argues against holding, not for adding) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07) — but ratio pre-check **flags** industry "Capital Markets" as a core-business screen fail |
| DCF intrinsic value | **$0.72** vs. $15.53 price -> **-95.4%** (a conventional DCF applied to what is now an ETH-treasury/staking vehicle, not an operating business — read the number as "this model doesn't fit this company," not literally) |
| Trailing stop (chandelier) | $14.5392 — price ~6.8% above it |
| 6m momentum (skip last month) | -45.2% |
| Portfolio note | ATR 7.05% — size down per vol throttle |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW, and the Shariah conflict below should be resolved before adding |
| What changes verdict | Shariah re-screen resolving the Capital Markets flag one way or the other, or a technical SELL trigger |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$104.00**, **-9.5%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | MEDIUM — reward:risk 2.3:1 — moderate skew |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale) |
| DCF intrinsic value | **$120.42** vs. $104.00 price -> **+15.7% upside** to the model |
| Trailing stop (chandelier) | $96.8018 — price is $7.20 above it |
| 6m momentum (skip last month) | -24.6% |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction MEDIUM |
| What changes verdict | thesis_broken: true, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rules muted until >= 4 names.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.53 | 10 | $15.43 | $155.34 | +0.7% | 17.6% |
| NOW | $104.10 | 7 | $114.97 | $728.67 | -9.5% | 82.4% |

**Total value: $884.01** | Cost: $959.09 | **Total return: ~-7.8%** (-$75.08 unrealised,
before the +$54.95 realised gain already booked on the FIG exit)

Book is far smaller and far more concentrated than last cycle: FIG's ~$820
position is gone (sold 2026-07-13, +$54.95 realised), replaced by a much
smaller BMNR stake (~$155). NOW alone is now 82.4% of the book — well above
any reasonable single-name comfort level, though the concentration rule stays
mechanically muted until you hold 4+ names (`min_names_for_concentration: 4`).

## Action flags (priority order)

1. **[Mandate — NEW this run] BMNR Shariah pre-check conflict.** The broker
   app recorded BMNR **compliant** (screened 2026-07-07, before purchase),
   but the mechanical ratio pre-check flags it: *"industry 'Capital Markets'
   matches 'capital markets' — core business fails screen."* BMNR (Bitmine
   Immersion Technologies) has pivoted from bitcoin-mining infrastructure
   into operating as an **Ethereum treasury and staking vehicle** — as of
   mid-July it holds 5.77M ETH (~4.8% of total supply, ~$11.3B combined
   crypto/cash/securities) and projects **$242M-284M in annualized staking
   rewards**. [CoinDesk](https://www.coindesk.com/markets/2026/07/13/tom-lee-s-bitmine-raises-ether-holdings-to-usd5-77-million-or-4-8-of-supply) ·
   [PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
   That business model — a yield-bearing treasury/capital-markets vehicle —
   is exactly the profile a "Capital Markets" industry classification and a
   business-activity screen are built to catch, independent of the broker
   app's compliant flag. **This is a direct parallel to FIG's 7-run
   compliance conflict last month** (recorded status vs. mechanical
   pre-check disagreeing) — re-screen this specifically in Zoya/Musaffa
   before adding to the position; don't treat the broker app's 2026-07-07
   screen (pre-dating the position and possibly pre-dating the ETH-staking
   scale-up) as the last word.
2. **[Concentration] NOW is 82.4% of an 884-dollar, 2-name book.** Not a
   rule violation (concentration is muted below 4 names) but worth noting on
   its own terms — a single name now dominates the entire portfolio's
   outcome.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do
   not add.
4. **[Catalyst / NOW] Q2 FY2026 earnings land 2026-07-22 — 6 days out.**
   ServiceNow confirmed results will be announced after close on Wednesday,
   July 22, 2026. [ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
5. **[52-week range / NOW] Price sits at 14% of its 52-week range** — close
   to the 52-week low end, consistent with the -24.6% 6-month momentum
   reading. Thesis-vs-price gap is real; not itself a rule trigger.
6. **[Discovery pool widened] 50 leads this run (up from 20 last cycle)** —
   `discover_top_n` in `rules.md` was raised to 50. 26 new DRAFT setup cards
   were auto-filled; see the table below.

## Per-holding read

### BMNR — Bitmine Immersion Technologies, Inc.
**Case to keep:** essentially flat since purchase (+0.7%), inside its
trailing stop, and the underlying ETH-treasury strategy has scaled visibly
this month — ETH holdings up from 5.67M to 5.77M tokens in a week, index
inclusion in the Russell 1000, and a Fortune Crypto 100 listing added
visibility. [Fortune/TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-in-operational-update)

**Case to trim/exit — compliance, not price:** the ratio pre-check's
"Capital Markets" flag is a real, mechanical disagreement with the broker
app's compliant screen, and the underlying business (a treasury vehicle
that stakes ETH for yield and holds equity stakes in other companies —
Beast Industries, Eightco Holdings) reads more like an investment company
than an operating business. Stock is also down ~51% over H1 2026 before
this position was opened — very high realized volatility (7.05% daily ATR)
for a position sized at 17.6% of a tiny book. [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-stock-collapsed-201534056.html)

**No rule currently forces an exit** (DEFAULT — no rule fired); this is a
mandate question to resolve via a fresh Zoya/Musaffa screen, not a technical
call.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 FY2026 earnings land **2026-07-22** (6 days out); DCF
shows +15.7% upside to intrinsic value ($120.42) at recorded assumptions;
price is still above its chandelier trailing stop; thesis (durable
subscription growth + AI-agent expansion + Armis integration) is unchanged
and Shariah-compliant per the June screen.

**Case to trim/watch:** P/E ~119 still VALUATION_RICH; 6m momentum -24.6%;
price sits near the bottom of its 52-week range (14th percentile); no
`initial_stop`, `target_price`, `conviction`, or `pre_mortem` has been filled
in on the holding's front-matter yet — the PM record is running entirely on
recommend.py's mechanical proxies, not your own stated variant view.

## Suggested actions (from YOUR rules, rules.md)

- **No hard rule fired for BMNR** — DEFAULT/HOLD. The Shariah conflict above
  is a mandate question outside the mechanical rule set; resolve it directly.
- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **DRAWDOWN_REVIEW not firing -> NOW**: -9.5% vs. the 20% threshold.
- **VOL_THROTTLE fired -> BMNR**: ATR 7.05% >= `vol_throttle_atr_pct` 6% — de-risk
  note; informational, doesn't force a size change on its own.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $15.52 | -95.4% | growth_5y 5%, terminal 2.5%, discount 10% (generic defaults — a treasury/staking vehicle doesn't fit a cash-flow DCF; read this as a model-mismatch, not a valuation call) |
| NOW | $120.42 | $104.04 | +15.7% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (it only sources from watchlist.md) —
expected, since no card has been reviewed and flipped to `status: planned`
yet. All new-idea surfacing this cycle comes from machine discovery below.

## Draft & planned setups — 50 leads (pool widened), 26 fresh DRAFT cards this run

`discover.py` refreshed the candidate pool (SPUS holdings + the
`growth_technology_stocks` / `undervalued_large_caps` screens) and wrote
**`leads.md`** (top 50 by max-benefit rank — `discover_top_n` was raised from
20 to 50 since last cycle). `scaffold.py --all-leads` auto-filled a DRAFT
`setups/<ticker>.md` card for every lead that didn't already have one (26 new
cards; 24 existing cards left unchanged). **Every DRAFT card is unreviewed
and Shariah UNVERIFIED — proposals to review and edit, never buys.** None can
reach BUY-CANDIDATE until you review the card, edit anything you disagree
with, set `status: planned`, and screen the name compliant in Zoya/Musaffa.
No `setups/` card currently carries `status: planned` or `live`.

Top 20 by max-benefit rank:

| Ticker | Verdict (leads.md) | Has card | Leads R:R | Catalyst (earnings) | Days out |
|---|---|---|---|---|---|
| FICO | LEAD | existing | 10.3:1 | 2026-07-29 | 13 |
| TSLA | LEAD | existing | 12.7:1 | 2026-07-22 | 6 |
| UTHR | LEAD | new | 12.0:1 | 2026-07-29 | 13 |
| SFD | LEAD | new | 8.2:1 | 2026-07-28 | 12 |
| MT | LEAD | existing | 6.2:1 | 2026-07-30 | 14 |
| ALKT | LEAD | existing | 7.1:1 | 2026-07-29 | 13 |
| AVGO | LEAD | new | 10.9:1 | 2026-09-03 | 49 |
| LIF | LEAD | existing | 5.5:1 | 2026-08-10 | 25 |
| DUOL | LEAD | existing | 5.6:1 | 2026-08-05 | 20 |
| AMD | LEAD | existing | 3.0:1 | 2026-08-04 | 19 |
| VRNS | LEAD | existing | 3.1:1 | 2026-07-28 | 12 |
| ZS | LEAD | existing | 6.5:1 | 2026-09-02 | 48 |
| CVE | RESEARCH | existing | 2.9:1 | 2026-07-30 | 14 |
| DELL | RESEARCH | new | 2.2:1 | 2026-09-03 | 49 |
| CNQ | LEAD | existing | 3.6:1 | 2026-08-06 | 21 |
| PLTR | LEAD | existing | 4.5:1 | 2026-08-03 | 18 |
| MSFT | LEAD | existing | 3.5:1 | 2026-07-29 | 13 |
| GDDY | LEAD | existing | 3.4:1 | 2026-07-30 | 14 |
| LLY | RESEARCH | new | 2.3:1 | 2026-08-05 | 20 |
| GOOGL | RESEARCH | existing | 1.3:1 | 2026-07-22 | 6 |

(30 further leads scored lower and are not tabulated here — full list and
proposed levels are in `leads.md`; every DRAFT card lives in `setups/`.)

**Flags worth your attention before reviewing any of these:**
- **TSLA / GOOGL (both earnings 2026-07-22, same day as NOW)** — mega-caps
  with clean debt/liquidity ratios on the pre-check, but each still needs an
  actual Zoya/Musaffa business-activity screen (financing-arm interest
  income for Tesla; ad/interest-bearing cash mix for Alphabet) rather than
  assuming "SPUS holds it, so it's fine."
- **PLTR** — government/defense-adjacent business-activity question carried
  over from prior runs; worth checking before spending review time on the
  card.
- **MT** — reward:risk compressed to 6.2:1 from last cycle's tighter band;
  still worth a sanity check on the entry/stop/target formula output before
  treating it as engineered.

## Follow-ups (priority order)

1. **[Urgent — new this run] BMNR Shariah re-screen.** The ratio pre-check's
   "Capital Markets" flag directly conflicts with the broker app's recorded
   compliant status from before the position was scaled up as an
   ETH-staking treasury vehicle. Re-screen in Zoya/Musaffa before adding to
   the position — this is the same shape of conflict that took 7 runs to
   resolve on FIG.
2. **[Time-boxed] NOW earnings 2026-07-22** — 6 days out.
3. **[Concentration]** NOW is 82.4% of the book; consider whether that's
   intentional now that FIG is gone and BMNR is small, or whether it's an
   artifact of the recent trades that's worth addressing directly.
4. **[Housekeeping] 26 new DRAFT setup cards** added this run (many more in
   `setups/` now); none are `planned`, none can reach BUY-CANDIDATE. Review
   at your own pace.
5. **[Infrastructure — still open]** No `transactions.csv` ledger yet
   (FIG's exit is recorded in its holding file, not a ledger) — start
   logging trades via `/apply-trade` to unlock the discipline guard and
   `journal.py` expectancy reporting.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow to Announce Second Quarter 2026 Financial Results on July 22 — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-to-Announce-Second-Quarter-2026-Financial-Results-on-July-22/default.aspx)
- [Tom Lee's BitMine raises ether holdings to $5.77 million, or 4.8% of supply — CoinDesk](https://www.coindesk.com/markets/2026/07/13/tom-lee-s-bitmine-raises-ether-holdings-to-usd5-77-million-or-4-8-of-supply)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.77 Million Tokens — PRNewswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-77-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-3-billion-302823523.html)
- [BitMine Highlights Massive Ethereum Treasury in Operational Update — TipRanks](https://www.tipranks.com/news/company-announcements/bitmine-highlights-massive-ethereum-treasury-in-operational-update)
- [Why Bitmine Immersion Stock Collapsed 51% In The First Half of 2026 — Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/why-bitmine-immersion-stock-collapsed-201534056.html)
