# Investment Engine — Full System Overview & Rooms for Improvement

> Purpose of this document: a complete, accurate map of how the system works
> today (every file, every gate, every config knob) **and** a prioritized,
> researchable list of where it can be improved. Written so you can do deep
> research on any one area without re-reading the code.
>
> Hard framing that governs everything below: this is **decision support, not
> financial advice**. Nothing here recommends a trade. Shariah status is always
> the user's to verify in Zoya/Musaffa; the engine's ratio screen is a heads-up.
> The engine never auto-trades.

---

## 1. Design philosophy

Four principles are baked into the code, and any improvement should preserve them:

1. **The user decides; the engine surfaces facts.** Every output is a fact + the
   rule it triggered, never "buy this." Verbs (SELL/TRIM/REVIEW/HOLD,
   BUY-CANDIDATE/RESEARCH/AVOID) are *your rules resolving against data*.
2. **Compliance is a gate, not a tiebreaker.** Shariah sits first in every
   pipeline as an absolute filter, independent of price/return.
3. **Don't fabricate.** On a data-fetch failure the tools report the gap
   (DATA_GAP / null) and degrade gracefully — they never invent prices,
   catalysts, or compliance status.
4. **Policy lives in one place.** All thresholds are tunable knobs in `rules.md`
   front-matter, so behavior changes are config, not code edits.

The intellectual backbone is `docs/portfolio-manager-decision-logic.md` — a
synthesis of buy-side PM reasoning (falsifiable thesis, variant perception/edge,
≥3:1 asymmetry, conviction-scaled sizing, pre-written sell rules). The engine
encodes the *mechanical* parts of that framework and is honest that it cannot
supply the *analytical edge*, which remains human work.

---

## 2. Data flow (how a number becomes a verdict)

```
            holdings/*.md   watchlist.md   universe.md        rules.md (knobs)
                 │               │              │                  │
   ┌─────────────┼───────────────┼──────────────┼──────────────────┤
   │             ▼               │              │                  │
   │   prices / shariah / dcf /  │              │                  │
   │   signals / verdict  ───────┼──────────────┼───► /assess-portfolio ─► reports/*.md
   │   (per holding)             │              │                  │
   │                             ▼              ▼                  │
   │                    recommend.py      screener.py ─► /screen-ideas
   │                    (PM gates on       (rank a
   │                     watchlist)         universe)             │
   │                             ▲                                 │
   │                             │  rewrites watchlist.md          │
   │                    discover.py  ◄───  yfinance screens +      │
   │                    (auto-build pool)   halal-ETF holdings     │
   └─────────────────────────────────────────────────────────────┘
                 │
   executed trade ▼
            apply_txn.py ─► updates holdings/*.md + transactions.csv (+ holdings/closed/)
```

Network boundary: every script except `common.py` and `apply_txn.py` needs
**yfinance → Yahoo Finance**. This is the single external dependency and the
single point of failure (see §10, §11.2).

---

## 3. Repository layout

```
investing/
├── CLAUDE.md                  # project memory Claude reads on launch
├── README.md                  # quick start + local-run / auto-discovery
├── requirements.txt           # yfinance, PyYAML, ruamel.yaml, pandas
├── rules.md                   # YAML knobs (policy) + prose rule docs
├── universe.md                # tickers screener.py ranks (you define)
├── watchlist.md               # candidate ideas (you define OR discover.py writes)
├── transactions.csv           # ledger (created on first apply_txn)
├── holdings/                  # one .md per position (YAML front-matter + thesis)
│   ├── _example.md            # template (ignored by loaders)
│   └── closed/                # fully-exited positions are moved here
├── docs/
│   ├── portfolio-manager-decision-logic.md   # the PM framework (the "spec")
│   └── system-overview-and-improvements.md   # this file
├── scripts/                   # deterministic engines (see §5)
└── .claude/skills/            # slash commands (see §8)
    ├── assess-portfolio/  screen-ideas/  apply-trade/  discover/
```

---

## 4. Data model (the files YOU edit)

### 4.1 `holdings/<ticker>.md` — one position each
YAML front-matter (parsed by `common.load_holdings`) + free-text body
(thesis/risks/notes, read by Claude for context the numbers miss).

Key front-matter fields:
| Field | Used by | Meaning |
|-------|---------|---------|
| `ticker`, `name`, `shares`, `cost_basis`, `currency` | all | position identity & cost |
| `trade_type` (`core`/`swing`/`momentum`/`catalyst`) | verdict | which technical sell rules apply |
| `shariah: {source, status, screened, purification_pct}` | shariah, verdict, signals | recorded compliance + screen date |
| `last_price`, `week52_low`, `week52_high`, `pe` | signals, verdict | fallbacks + valuation/range flags |
| `initial_stop` | verdict, recommend | hard stop (HARD_STOP trigger) |
| `thesis_broken: true` | verdict | forces SELL (THESIS_BREAK) |
| `trimmed: true` | verdict | suppresses repeat TAKE_PARTIAL |
| `dcf: {growth_5y, terminal_growth, discount_rate}` | dcf | per-name DCF overrides |

### 4.2 `watchlist.md` — candidate ideas
Rows: `TICKER | why (your edge/variant view) | catalyst (dated, YYYY-MM-DD)`.
Comment lines (`#`) and the prose sections are ignored by the parser. Either
hand-curated **or auto-overwritten by `discover.py`** (header/themes/hard-rules
sections preserved; only the ticker block is regenerated).

### 4.3 `universe.md` — pool to rank
One ticker per line (20–60 suggested). `screener.py` ranks exactly these; it
never invents names.

### 4.4 `transactions.csv` — ledger
Columns: `date, ticker, action, shares, price, realized_pl, note`. Append-only,
written by `apply_txn.py`.

---

## 5. Script reference (exact behavior)

All scripts print JSON to stdout and warn to stderr; all tolerate missing data.

| Script | Purpose | Reads | Network | Key output |
|--------|---------|-------|---------|-----------|
| **common.py** | `load_holdings()` / `parse_holding()` helpers | holdings/*.md | no | `[{meta, thesis, path}]` |
| **prices.py** | price, return vs cost, value, weights | holdings | yes | `{total_value, positions[]}` |
| **shariah.py** | recorded status + staleness + ratio pre-check | holdings | yes | per-name compliance + `ratio_precheck` |
| **dcf.py** | 2-stage FCF DCF → intrinsic value vs price | holdings | yes | `{ok, intrinsic_value, upside_pct, assumptions}` |
| **signals.py** | review flags (mandate>drawdown>valuation>range) | holdings | yes | per-name `flags[]` by priority |
| **technicals.py** | ATR/EMA/RSI/momentum/52w/chandelier from 1y history | (ticker) | yes | indicator dict (or None) |
| **verdict.py** | ONE verb per holding (SELL>TRIM>REVIEW>HOLD) | holdings, rules | yes | `{note, portfolio_notes, verdicts[]}` |
| **screener.py** | rank universe.md by mechanical signals | universe, rules | yes | `{ranked[], disclaimer}` |
| **recommend.py** | PM-grade record per holding/idea + idea funnel | holdings, watchlist, rules | yes | `{holdings[], ideas[], disclaimer}` |
| **discover.py** | auto-build pool → top-20 → rewrite watchlist.md | rules, (live screens) | yes | `{pool_size, selected, ideas[]}` |
| **apply_txn.py** | record executed trade; update holding + ledger | holdings | no | console summary |

### 5.1 Detail on the decision engines

**technicals.py** — `fetch(ticker, cfg)` pulls `yf.Ticker(t).history(period="1y")`
and returns: `price, atr, atr_pct, ema_fast, ema_slow, chandelier_stop,
mom_12_1/6_1/3_1, rsi14, rel_volume, dist_52w_high_pct, bom_price, bom_drop_pct`.
Returns `None` on any failure (callers skip gracefully). **No earnings/catalyst
data here** — that's `discover.fetch_catalyst_date`.

**shariah.py** — `ratio_precheck(ticker)`: debt/mcap and cash/mcap from
`balance_sheet` + `fast_info.market_cap`. Thresholds `DEBT_MAX = LIQUID_MAX =
0.33` (DJIM/S&P convention). `STALE_DAYS = 100`. Returns `{ok, debt_ratio,
liquid_ratio, flags}` or `{ok: None, note}`. **No business-activity screen and
no impermissible-income (5%) test** — that's the Zoya/Musaffa gap.

**verdict.py** — `compute(cfg, hs)` resolves precedence `SELL(3) > TRIM(2) >
REVIEW(1) > HOLD(0)`. Stages: (1) compliance gate, (4) hard/technical sells
(HARD_STOP, THESIS_BREAK, TRAIL_STOP, MOMENTUM_STOP, EMA_BREAK), (3) trim/hold
(TAKE_PARTIAL at +`take_profit_r`, CONCENTRATION > `max_position_pct`,
VALUATION_RICH ≥ `pe_rich`), plus DRAWDOWN_REVIEW. Concentration is muted for a
tiny book (< `min_names_for_concentration`).

**screener.py** — `score_universe(rows, cfg)`: min-max normalizes momentum
(0.4), trend (0.25), RSI-shape (0.15), rel-volume (0.1), low-vol (0.1) →
composite 0–100. `≥ screen_buy_candidate_score` (65) → BUY-CANDIDATE, else
RESEARCH; no price / < `screen_min_price` → AVOID. Compliance weight 0
(informational).

**recommend.py** — reuses `verdict.compute()` for holdings and layers PM fields
(conviction proxy, reward:risk, target/stop, thesis one-liner). For watchlist
ideas it runs the funnel: **EDGE_GATE** (a `why` must exist), **ASYMMETRY_GATE**
(reward:risk ≥ `reward_risk_min_swing`), **CATALYST_GATE** (dated catalyst within
`catalyst_horizon_days`), Shariah. AVOID is reserved for a Shariah ratio FLAG; a
blocked price feed is **DATA_GAP → RESEARCH**, not AVOID.

**discover.py** — the auto-discovery engine (§7.4).

**apply_txn.py** — `buy`: weighted-average cost; brand-new ticker creates a
**gated stub** (`shariah.status = unknown`, so it's flagged until screened).
`sell`: avg-cost realized P/L; selling to 0 moves the file to `holdings/closed/`
with a realized-P/L note. Every trade appends to `transactions.csv`.

---

## 6. Configuration reference (`rules.md` knobs)

| Knob | Default | Controls |
|------|---------|----------|
| `risk_per_trade_pct` | 1.5 | risk per trade (1% rule) |
| `max_position_pct` | 22 | single-name cap → TRIM (CONCENTRATION) |
| `portfolio_heat_pct` | 8 | intended max total open risk *(declared, not yet enforced — see §11.6)* |
| `min_names_for_concentration` | 4 | below this, ignore concentration |
| `atr_period` / `atr_stop_mult` | 22 / 3.0 | chandelier trailing stop |
| `ema_fast` / `ema_slow` | 20 / 50 | trend / EMA-break rules |
| `momentum_stop_bom_pct` | 15 | momentum month-open drop → SELL |
| `drawdown_review_pct` | 20 | drawdown vs cost → REVIEW |
| `take_profit_r` | 1.5 | +R to TRIM partial |
| `pe_rich` | 50 | rich multiple → HOLD-don't-add |
| `vol_throttle_atr_pct` | 6 | high ATR% → size-down note |
| `screen_weight_*` | see §5.1 | screener composite weights |
| `screen_buy_candidate_score` | 65 | screener BUY-CANDIDATE threshold |
| `screen_min_price` | 1.0 | penny-stock AVOID floor |
| `reward_risk_min` / `_min_swing` | 3.0 / 2.0 | asymmetry floors (core / swing) |
| `catalyst_horizon_days` | 60 | catalyst-within-horizon window |
| `discover_top_n` | 20 | candidates kept + written to watchlist |
| `discover_etfs` | [SPUS] | halal-ETF base pool |
| `discover_screens` | growth_tech, undervalued_large_caps, most_actives | yfinance screens |
| `discover_screen_count` | 100 | names per screen |
| `discover_w_rr / _score / _catalyst` | 0.5 / 0.3 / 0.2 | max-benefit rank weights |

---

## 7. The decision logic, end to end

### 7.1 Holdings → verb (verdict.py)
Compliance gate → technical/hard sells → trim/hold → drawdown review, resolved by
SELL>TRIM>REVIEW>HOLD precedence. See §5.1.

### 7.2 Universe → rank (screener.py)
Pure mechanical score; a *signal*, not an edge.

### 7.3 Watchlist idea → funnel (recommend.py)
EDGE → ASYMMETRY → CATALYST → Shariah, capping at RESEARCH where input is missing.

### 7.4 Auto-discovery (discover.py) — the new path
1. **Pool** = `discover_etfs` holdings (`funds_data`) ⊕ `discover_screens`
   (`yf.screen`), deduped, ticker-validated.
2. **Shariah knockout first** — `ratio_precheck`; `ok is False` → AVOID, dropped.
   Everything kept is **UNVERIFIED** (business screen still needs Zoya/Musaffa).
3. **Technicals** — `technicals.fetch`; no price → dropped (DATA_GAP).
4. **Catalyst** — `fetch_catalyst_date` via `get_earnings_dates()` (fallback
   `.calendar`) → next earnings date.
5. **Asymmetry** — `technical_target_stop` (target = 52w high, stop = chandelier)
   → `reward_risk`.
6. **Verdict (mechanical, by design choice):** BUY-CANDIDATE if clean ratios +
   reward:risk ≥ floor + catalyst within horizon; else RESEARCH. **EDGE is always
   flagged `NOT SUPPLIED`** — a mechanical pass is never dressed up as conviction.
7. **Rank** by `0.5·rr + 0.3·score + 0.2·catalyst_proximity` (normalized) → keep
   `discover_top_n`.
8. **Write** the top-N into `watchlist.md`; `recommend.py` / the report ingest
   them with no further change.

### 7.5 Executed trade → books (apply_txn.py)
Avg-cost bookkeeping; new names are gated; full exits archived to `closed/`.

---

## 8. Commands (`.claude/skills/`)

| Command | Runs | Produces |
|---------|------|----------|
| `/assess-portfolio` | discover.py (step 0) → prices/shariah/dcf/signals/verdict/recommend + web research | `reports/YYYY-MM-DD-assessment.md` |
| `/screen-ideas` | screener.py + recommend.py | ranked candidate table |
| `/discover` | discover.py | top-20 table + refreshed watchlist.md |
| `/apply-trade` | apply_txn.py | updated holdings + ledger |

---

## 9. Running locally (summary)
```bash
git checkout claude/dreamy-darwin-naf5ne && cd investing
pip install -r requirements.txt
python scripts/discover.py        # refresh watchlist.md with top 20
python scripts/recommend.py       # or /assess-portfolio to grade + report
python scripts/apply_txn.py --ticker X --action buy --shares N --price P   # after you decide
```
Needs live Yahoo; managed sandboxes block it (empty pool, watchlist untouched).

---

## 10. Constraints & correctness caveats (know these before trusting output)

1. **Single data source.** Everything rides on yfinance/Yahoo. Outages, rate
   limits, and silent schema changes (e.g. `funds_data`, `screen`) all degrade
   output. Sandboxes block it entirely.
2. **Shariah ratio screen ≠ compliance.** It implements only debt/cash ratios at
   **33%** (DJIM convention), not AAOIFI's stricter **30/30/5**, and has **no
   business-activity screen and no 5% impermissible-income test**. A "clean"
   pre-check is necessary, never sufficient — Zoya/Musaffa is the source of truth.
3. **Asymmetry is crude.** Target = 52-week high, stop = chandelier. This is a
   technical proxy, not a fundamental valuation, and breaks for names near highs
   (tiny/empty upside).
4. **Catalyst = next earnings only.** Misses launches, approvals, M&A, index
   rebalances, macro prints.
5. **No edge, by construction.** The most important PM pillar (variant
   perception) cannot be automated; mechanical BUY-CANDIDATEs are flagged
   `EDGE NOT SUPPLIED` for exactly this reason.
6. **Conviction is a heuristic.** `recommend.conviction()` maps reward:risk +
   thesis-presence to HIGH/MED/LOW — a proxy, not a real conviction call.
7. **Process ≠ profit.** Per the decision-logic doc's own caveats, rigor improves
   decision *quality*, not returns; retail short-term trading usually trails
   buy-and-hold after costs.

---

## 11. Rooms for improvement (prioritized, researchable)

Each item: **current state → direction → research questions**. Ordered roughly by
impact-to-effort.

### 11.1 Shariah screening depth *(highest leverage — it's the mandate)*
- **Now:** ratios only, 33% thresholds, no business screen, no income test, no
  purification calc; `STALE_DAYS = 100`.
- **Direction:** add the AAOIFI **30/30/5** option (configurable methodology),
  add the **impermissible-income < 5%** test, add a **purification estimator**,
  and integrate a real screen (Zoya/Musaffa API, or Islamicly/Musaffa datasets).
- **Research:** Which methodology does the user's scholar follow (AAOIFI vs DJIM
  vs MSCI)? Do Zoya/Musaffa expose an API or exportable list? How to map yfinance
  revenue-segment data to business-activity buckets? Quarterly re-screen cadence?

### 11.2 Data layer resilience *(unblocks everything else)*
- **Now:** direct yfinance calls, no caching, no retries, serial fetches, fragile
  to schema drift; fully blocked in sandboxes.
- **Direction:** an abstraction layer with **caching** (on-disk, TTL), **retry/
  backoff**, **pluggable providers** (Alpha Vantage, Financial Modeling Prep,
  Polygon, Tiingo, EODHD), and **offline fixtures** so CI/sandboxes can run.
- **Research:** Which provider covers Tadawul + US + fundamentals + earnings
  calendars at acceptable cost? Free-tier rate limits? Can a halal-universe
  dataset replace ETF-holdings scraping?

### 11.3 Better asymmetry / valuation targets
- **Now:** 52w-high target, chandelier stop only.
- **Direction:** multi-method targets (DCF intrinsic, analyst consensus,
  multiple-rerating, **options-implied move**), **base/bull/bear scenarios**, and
  ATR-scaled targets; pick the binding one transparently.
- **Research:** Are analyst targets/estimate dispersion available cheaply? Does
  options-implied vol improve target realism? How to score target *method
  quality*?

### 11.4 Real catalyst discovery
- **Now:** next earnings date only.
- **Direction:** an events layer — product launches, FDA/PDUFA, M&A close dates,
  index rebalances, investor days, conferences — via news/event APIs or SEC EDGAR
  filing calendars; classify HARD vs SOFT (per the doc).
- **Research:** Best structured event sources (Wall Street Horizon, Benzinga,
  EDGAR full-text)? Can an LLM extract dated catalysts from filings/news reliably?

### 11.5 Performance & process analytics (close the loop)
- **Now:** `transactions.csv` is written but **never analyzed**. The doc says: if
  realized win-rate × payoff < 1, tighten the asymmetry gate and cut size — no
  code computes this.
- **Direction:** a `performance.py` that computes realized **edge** (win-rate,
  avg win/loss, expectancy, R-multiples), **net-of-cost return vs a Shariah
  benchmark** (e.g. SPUS), turnover, and the disposition-effect ratio — and that
  *feeds back* into the knobs (auto-suggest tightening). Add a **decision journal**
  + **pre-mortem** field (the doc mandates both) and a **review-cadence** that
  auto-sets REVIEW on earnings/catalyst dates.
- **Research:** Which benchmark(s)? How many trades before the edge estimate is
  meaningful? How to separate process quality from outcome luck (Mauboussin)?

### 11.6 Portfolio-level risk (correlation & heat)
- **Now:** `portfolio_heat_pct` is declared but **not enforced**; discovery does
  not cluster by sector/correlation, so the doc's "several names in one sector =
  one bet" warning is only a manual note.
- **Direction:** aggregate **open risk (heat)** across positions and gate new
  ideas against it; add **sector/factor caps** and **correlation-aware sizing**
  (e.g. cap a correlated cluster as one bet) inside `discover.rank_and_select`.
- **Research:** Correlation window/source? Factor model (sector vs statistical)?
  Fractional-Kelly sizing with a correlation penalty?

### 11.7 Geographic coverage (Saudi/GCC)
- **Now:** data model supports `.SR`, but `discover_screens` are US-only (yfinance
  predefined screens), and the halal ETF (SPUS) is US.
- **Direction:** add **Tadawul** discovery (TASI/MSCI Tigris constituents, GCC
  halal lists), currency-aware sizing, and Saudi-market trading-hours/settlement
  rules.
- **Research:** Where to source Tadawul constituents + fundamentals
  programmatically? Saudi Shariah-index membership as a pre-screen?

### 11.8 Engineering hygiene
- **Now:** the only tests are an **uncommitted** mocked script in scratch; no
  `tests/` dir, no CI, no type-checking; discovery fetches **serially** (slow for
  100–250 names).
- **Direction:** commit a `tests/` suite (pytest) with network mocked + offline
  fixtures; add CI; **parallelize** discovery fetches (thread pool / async);
  add `--limit`/`--dry-run` flags; structured logging.
- **Research:** Thread-pool vs async for yfinance? How to record/replay fixtures
  for deterministic tests?

### 11.9 Output schema completeness
- **Now:** `recommend.py`'s record has `key_risks`, `pre_mortem`,
  `what_changes_mind` that are static or null.
- **Direction:** populate them from the holding thesis + a research step
  (LLM-assisted extraction), so the full PM schema (doc §7) is actually emitted.
- **Research:** Can the assessment skill reliably fill PRE_MORTEM and KEY_RISKS
  from thesis text + news without hallucinating?

### 11.10 Zakat & after-tax reality
- **Now:** none.
- **Direction:** a zakat estimator on holdings (per the user's madhhab) and
  cost/spread/slippage modeling so "net-of-cost" analytics are real.
- **Research:** Which zakat methodology (market value vs trade-intent)? Saudi
  brokerage cost model?

---

## 12. Glossary
- **Edge / variant perception** — a specific, evidenced reason the consensus is
  wrong (informational, analytical, or behavioral). The thing the engine *cannot*
  supply.
- **Asymmetry / reward:risk** — upside ÷ downside off a defined target and stop;
  ≥3:1 (core) or ≥2:1 (swing) to clear the gate.
- **Catalyst** — a dated event expected to close the price-to-value gap (HARD =
  specific date; SOFT = passage of time).
- **Invalidation vs stop** — thesis-type falsification vs a defensive price level;
  the doc requires both, set at entry.
- **UNVERIFIED (Shariah)** — passed/again unknown on the *ratio* pre-check; the
  *business* screen is unconfirmed → verify in Zoya/Musaffa.
- **DATA_GAP** — a fetch failure; reported, never faked. Distinct from AVOID.

---

### Source map for deep research
- PM framework & citations: `docs/portfolio-manager-decision-logic.md`
- Policy knobs & prose rules: `rules.md`
- Gate code: `scripts/{verdict,screener,recommend,discover,shariah}.py`
- Skills/prompts: `.claude/skills/*/SKILL.md`
- This map: `docs/system-overview-and-improvements.md`
