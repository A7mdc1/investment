# Portfolio Assessment — 2026-07-25

Not financial advice. This is decision support only — every buy/sell/hold call
is yours. Shariah status shown below is either the broker app's recorded
screen or a mechanical ratio pre-check; verify independently in Zoya/Musaffa
before acting on anything here.

## What ran this cycle

`discover.py` (live Yahoo data, 50-name pool by max-benefit rank — widened
from 20 last run) → `scaffold.py --all-leads` (29 new DRAFT setup cards
auto-filled for names without one; 21 existing cards left unchanged, 61
total in `setups/`) → `prices.py` / `shariah.py` / `dcf.py` / `signals.py` /
`verdict.py` / `recommend.py` — all live, no data gaps this run. `journal.py`
not run separately — still no `transactions.csv` in this sandbox (gitignored
personal ledger; discipline guard stays dormant until logged via
`/apply-trade`).

Since the last report (2026-07-13): FIG was sold (compliance exit, 7th run
resolved) and BMNR was bought — see `holdings/closed/fig-figma.md` and
`holdings/bmnr.md`. **This is the first assessment cycle to actually run the
scripts against BMNR**, and it surfaced a new mandate flag — see below.

## Verdicts (lead with this)

**BMNR -> HOLD** (RULE: DEFAULT — no rule fired). Live price **$15.79**,
**+2.3%** vs. $15.43 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | LOW — reward:risk -18.6:1 (skew argues against the position as-is) |
| Shariah | Recorded **compliant** (broker app, screened 2026-07-07, not stale) — **but see the new ratio pre-check flag below** |
| DCF intrinsic value | $0.72 vs. $15.79 price -> **-95.5%** — the DCF model does not fit a crypto-treasury vehicle (no conventional FCF profile); flagged as a caveat, not a real signal here |
| Trailing stop (chandelier) | $14.9806 — price is $0.81 (5.1%) above it |
| 6m momentum (skip last month) | -51.5% |
| Portfolio note | ATR 6.88% — vol-throttle note |
| Would buy today? | Mechanically yes per recommend.py's gates; conviction flagged LOW |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

**NOW -> HOLD** (RULE: VALUATION_RICH, recorded P/E ~119 >= pe_rich 50). Live
price **$98.78**, **-14.1%** vs. $114.97 cost basis.

| PM-grade record (recommend.py, live) | |
|---|---|
| Conviction | HIGH — reward:risk 7.2:1 with a stated thesis |
| Shariah | PASS — recorded compliant (screened 2026-06-09, not stale); ratio pre-check clean (business_ok, debt_ratio 2.4%, liquid_ratio 6.2%) |
| DCF intrinsic value | $120.12 vs. $98.78 price -> **+21.6% upside** to the model |
| Trailing stop (chandelier) | $96.0205 — price is $2.76 (2.8%) above it |
| 6m momentum (skip last month) | -27.0% |
| Would buy today? | Mechanically yes per recommend.py's gates |
| What changes verdict | thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping |

- Portfolio note: only 2 holdings — concentration rule is nominally muted
  until >= 4 names, but **NOW is 81.4% of the book** — see Action flag #2.

## Snapshot (live)

| Ticker | Price | Shares | Cost basis | Value | Return | Weight |
|---|---|---|---|---|---|---|
| BMNR | $15.79 | 10 | $15.43 | $157.90 | +2.3% | 18.6% |
| NOW | $98.78 | 7 | $114.97 | $691.46 | -14.1% | 81.4% |

**Total value: $849.36** | Cost: $958.30 | **Total return: ~-11.4%** (-$108.94 unrealised)

## Action flags (priority order)

1. **[Mandate — NEW] BMNR ratio pre-check FAILS**: `shariah.py`'s mechanical
   business-activity pre-check now flags BMNR's industry classification —
   `"industry 'Capital Markets' matches 'capital markets' — core business
   fails screen"`. The broker app's recorded status is still `compliant`
   (screened 2026-07-07), so this is a **conflict between the recorded
   screen and the mechanical pre-check**, not an automatic verdict — but
   this is exactly the pattern that flagged FIG seven runs running before it
   was sold. BitMine's business model is functionally an Ethereum treasury/
   staking vehicle (see catalyst research below), which is a materially
   different activity profile than a conventional operating company;
   worth a fresh Zoya/Musaffa screen given the pre-check disagreement,
   not just relying on the July 7 broker-app screen.
2. **[Concentration] NOW is 81.4% of the book** — the 4-name minimum keeps
   the mechanical CONCENTRATION rule dormant, but with only two holdings a
   single name at >80% is a structural concentration risk regardless of
   whether the rule fires. This is a fact for you to weigh, not a rule
   violation.
3. **[Valuation / NOW] P/E ~119 (recorded)** — rich; VALUATION_RICH holds. Do not add.
4. **[DCF / BMNR] Model doesn't fit the business** — a -95.5% DCF gap on a
   crypto-treasury company is a modeling-mismatch artifact (BMNR's value is
   driven by its ETH holdings and staking yield, not discounted operating
   cash flow), not a signal to act on. Included for completeness only.
5. **[Catalyst / NOW — just occurred] Q2 FY2026 earnings beat, 2026-07-22**:
   subscription revenue +23% cc (beat guidance by 1.5 pts), operating margin
   29.5% (3 pts above guidance), full-year subscription guidance raised to
   $15.77B (+21% y/y). AI Control Tower ACV is tracking toward $1.5B by
   year-end. [ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
6. **[Catalyst / BMNR] Russell 1000 inclusion + analyst target cut**: added
   to the Russell 1000 (institutional-ownership tailwind), but B. Riley cut
   its price target to $25 from $33 (still Buy) on ETH-price sensitivity and
   capital-structure changes. [TimothySykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20/)

## Per-holding read

### BMNR — BitMine Immersion Technologies, Inc.
**Case to keep:** ETH treasury continues to grow — ~5.74-5.78M ETH
(~4.8% of total supply) and $11.1-11.5B combined crypto/cash/securities
holdings as of mid-to-late July, with ~4.9M ETH staked via MAVAN targeting
$235-284M in annualized staking revenue; Russell 1000 inclusion should
support institutional demand; price is up modestly (+2.3%) vs. cost and
still above its trailing stop.
[PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-78-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-5-billion-302829332.html)

**Case to trim / re-screen:** Q2 revenue ~$46.5M against a net loss of
~$83.6M — deeply negative margins are structural for this business model
(mark-to-market on crypto holdings, financing costs), not a one-off; 6m
momentum -51.5% is the steepest of anything in this two-name book; B. Riley
cut its target 24% even while keeping Buy; and — the item that most needs
your attention — the ratio pre-check disagreement on Action flag #1. A
capital-markets/treasury-vehicle business model raises different Shariah
questions (interest-bearing cash, staking-yield character, leverage) than a
conventional operating business; the July 7 broker screen predates this
run's pre-check flag.

**Verdict: HOLD (DEFAULT — no rule fired)**, but flagged for a mandate
re-check, not a price call.

### NOW — ServiceNow, Inc.
**Case to keep:** Q2 beat on every headline metric (subscription growth,
margin, guidance raise, AI ACV trajectory) — the fundamental thesis
(durable enterprise-workflow subscription growth + AI-agent expansion) was
reinforced, not weakened, by this print; DCF shows +21.6% upside to
intrinsic value at recorded assumptions; price is still above its trailing
stop.

**Case to trim / watch:** P/E ~119 remains VALUATION_RICH — the stock is
priced for the growth it just delivered, so the bar for the *next* print is
higher, not lower; 6m momentum is -27.0% (deteriorated further vs. the
07-13 report's -27.5%, i.e. still negative on that lookback despite the
July 22 pop, since the window includes the pre-earnings drawdown); price is
still down -14.1% from your $114.97 cost basis even after the beat —
worth noting the cost basis was set before the split-adjusted rally
context, so the drawdown reflects the entry price more than the current
setup.

**Verdict: HOLD (VALUATION_RICH — hold, do not add)**.

## Suggested actions (from YOUR rules, rules.md)

- **VALUATION_RICH fired -> NOW**: HOLD, do not add.
- **No rule fired -> BMNR**: DEFAULT HOLD; the ratio pre-check conflict
  (Action flag #1) is not a `rules.md` mechanical trigger — it's a data
  point for your own Zoya/Musaffa re-screen.
- **DRAWDOWN_REVIEW not firing -> NOW**: -14.1% vs. the 20% threshold —
  getting closer than last run's -2.0%, worth watching if it keeps drifting.
- **TRAIL_STOP -> BMNR / NOW**: neither fires; both `trade_type: core`,
  exempt from the mechanical trailing-stop rule (same structural gap noted
  last run — core positions never get a mechanical TRAIL_STOP, a policy
  decision you haven't made either way).
- **VOL_THROTTLE note -> BMNR, NOW**: ATR 6.88% / 6.0% — informational,
  size any new adds down accordingly.

*If you execute anything from this report, run `/apply-trade` so holdings
files and ledger stay in sync.*

## DCF (live)

| Ticker | Intrinsic value | Price | Upside/(downside) | Assumptions |
|---|---|---|---|---|
| BMNR | $0.72 | $15.79 | -95.5% | growth_5y 5%, terminal 2.5%, discount 10% — **model mismatch, see flag #4** |
| NOW | $120.12 | $98.78 | +21.6% | growth_5y 18%, terminal 3%, discount 10% |

## New ideas (watchlist.md)

`watchlist.md`'s hand-curated ticker list is still **empty** — nothing for
step-4 idea generation to research this run. All new-idea surfacing this
cycle comes from machine discovery below. `recommend.py`'s `ideas` array
returned **0 BUY-CANDIDATEs** this run (expected — no card has been
reviewed and flipped to `status: planned` yet).

## Draft & planned setups — 50 leads this run (pool widened from 20), 29 fresh DRAFT cards

`discover.py`'s pool was widened to 50 names (previously 20). 21 leads
already had a setup card from prior runs (MSFT, DUOL, FICO, PLTR, VRNS, AU,
ZS, GDDY, PAY, AR, ULTA, CF, CVE, AMD, MT, SIMO, CNQ, RCL, ALAB, KLIC, TER)
and were left unchanged; **29 new DRAFT cards** were auto-filled this run
(UTHR, SMCI, AEM, AGI, ARW, PAAS, GWRE, ESE, KGC, BKR, AVGO, NEM, TS, P,
DINO, SFD, DELL, STX, HAS, AAPL, NVDA, DLO, LLY, WDC, AMKR, APH, BBY, PDFS,
FLYW). **Every DRAFT card is unreviewed and Shariah UNVERIFIED — proposals
to review and edit, never buys.**

### LEAD tier (clears the discovery-stage asymmetry bar) — 23 names

| Ticker | Has card | Leads R:R | Catalyst | Days out |
|---|---|---|---|---|
| AEM | new | 20.0:1 | earnings 2026-07-29 | 4 |
| AGI | new | 12.7:1 | earnings 2026-07-29 | 4 |
| UTHR | new | 12.0:1 | earnings 2026-08-05 | 11 |
| PLTR | existing | 16.6:1 | earnings 2026-08-03 | 9 |
| DUOL | existing | 10.7:1 | earnings 2026-08-05 | 11 |
| MSFT | existing | 9.7:1 | earnings 2026-07-29 | 4 |
| SMCI | new | 9.1:1 | earnings 2026-08-11 | 17 |
| GWRE | new | 9.1:1 | earnings 2026-09-03 | 40 |
| ZS | existing | 9.4:1 | earnings 2026-09-02 | 39 |
| FICO | existing | 9.5:1 | earnings 2026-07-29 | 4 |
| PAAS | new | 8.5:1 | earnings 2026-08-12 | 18 |
| AU | existing | 7.8:1 | earnings 2026-07-31 | 6 |
| ARW | new | 6.4:1 | earnings 2026-08-06 | 12 |
| ULTA | existing | 6.2:1 | earnings 2026-08-27 | 33 |
| KGC | new | 6.0:1 | earnings 2026-07-29 | 4 |
| AVGO | new | 5.7:1 | earnings 2026-09-03 | 40 |
| ESE | new | 5.6:1 | earnings 2026-08-06 | 12 |
| VRNS | existing | 5.4:1 | earnings 2026-07-28 | 3 |
| P | new | 5.3:1 | earnings 2026-08-26 | 32 |
| GDDY | existing | 4.9:1 | earnings 2026-07-30 | 5 |
| PAY | existing | 4.8:1 | earnings 2026-08-03 | 9 |
| AR | existing | 4.3:1 | earnings 2026-07-29 | 4 |
| BKR | new | 3.8:1 | earnings 2026-07-26 | 1 |

### RESEARCH tier (mechanical asymmetry/edge bar not cleared) — 27 names

DELL, STX, AAPL, NVDA, AMD, CNQ, MT, SIMO, ALAB, KLIC, TER, RCL, DLO, LLY,
WDC, AMKR, APH, BBY, PDFS, FLYW, NEM, TS, DINO, CF, SFD, CVE, HAS — all
capped RESEARCH by the ASYMMETRY_GATE (reward:risk below `reward_risk_min`)
or an n/a reward:risk (no computable target/stop this run). None are
AVOID — no hard Shariah knockout fired on the ratio pre-check for these.

**Flags worth your attention before reviewing any of these:**
- **Gold/silver miners cluster (AEM, AGI, KGC, PAAS, AU, NEM)** — six
  precious-metals names surfaced this run, mostly via the
  `undervalued_large_caps` screen. Royalty/streaming and mining-finance
  structures in this sector carry their own Shariah nuance (financing
  arrangements, hedging/derivative use) distinct from a straightforward
  operating-company screen — same caution as BMNR's Action flag #1, applied
  here to a different reason (business-financing structure vs. treasury/
  capital-markets classification). Don't treat "score" as a compliance
  signal for any of these.
- **PLTR** — carried over from prior runs: government/defense data-contract
  business-activity question, still unresolved, still worth a real screen
  before spending review time on the card.
- **MT** — carried over: implausibly tight engineered entry/stop/target
  band flagged in a prior run; still present in today's pool (RESEARCH
  tier this time, reward:risk 1.1:1).
- **BKR (1 day to catalyst)** — earnings tomorrow (2026-07-26); if you're
  looking at this card at all, that's a very tight window to underwrite it
  properly first.

## Follow-ups (priority order)

1. **[New, top priority] BMNR ratio pre-check conflict** — re-screen in
   Zoya/Musaffa given the mechanical pre-check flags the capital-markets/
   treasury-vehicle business model; the recorded compliant status is three
   weeks old (2026-07-07) and predates this flag.
2. **[Structural] NOW at 81.4% of a 2-name book** — not a rule violation
   (concentration muted below 4 names) but a fact worth weighing on its
   own regardless of what the rules say.
3. **[Housekeeping] 29 new DRAFT setup cards** added this run (61 total in
   `setups/`); none are `planned`, none can reach BUY-CANDIDATE. The
   gold/silver-miner cluster and PLTR need a compliance answer before
   they're worth reviewing further.
4. **[Infrastructure — still open]** No ledger yet in this environment —
   start logging trades to `transactions.csv` (or via `/apply-trade`) to
   unlock the discipline guard.

---

Not a financial advisor. Shariah compliance shown here is a broker-app
recorded flag or a mechanical ratio pre-check, neither a fatwa — verify
independently in Zoya/Musaffa before acting.

Sources:
- [ServiceNow Reports Second Quarter 2026 Financial Results — ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx)
- [ServiceNow (NOW) Rallies As AI-Fueled Q2 Earnings Crush Expectations — Timothy Sykes](https://www.timothysykes.com/news/servicenow-inc-now-news-2026_07_23/)
- [Full Transcript: ServiceNow Q2 2026 Earnings Call — Benzinga](https://www.benzinga.com/news/26/07/60627210/full-transcript-servicenow-q2-2026-earnings-call)
- [BMNR Stock Climbs As Massive Ethereum Bet Draws Traders — Timothy Sykes](https://timothysykes.com/news/bitmine-immersion-technologies-inc-bmnr-news-2026_07_20/)
- [Bitmine Immersion Technologies (BMNR) Announces ETH Holdings Reach 5.78 Million Tokens — PR Newswire](https://www.prnewswire.com/news-releases/bitmine-immersion-technologies-bmnr-announces-eth-holdings-reach-5-78-million-tokens-and-total-crypto-and-total-cash-holdings-of-11-5-billion-302829332.html)
