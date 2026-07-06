# Investment workspace

This repo tracks an investment portfolio as markdown. Each file in `holdings/`
is one position: YAML front-matter (ticker, shares, cost basis, Shariah status,
PM decision record) plus a free-text thesis/body.

## Decision engine

The engine uses the PM-grade framework from `PM_FRAMEWORK.md` — a buy-side
decision process built on four pillars: falsifiable thesis, variant perception
(why the market is wrong), reward:risk skew, and conviction-sized positions.

**Seven labels, two domains:**
- Existing holdings → SELL > TRIM > REVIEW > HOLD (precedence order)
- New ideas (watchlist/universe) → BUY-CANDIDATE | RESEARCH | AVOID

**Gate order (runs in sequence):**
1. Shariah knockout — non-compliant → AVOID/SELL, absolute gate
2. Edge test — no articulated variant view → cap at RESEARCH
3. Asymmetry gate — reward:risk < `min_reward_risk` → cannot be BUY-CANDIDATE
4. Catalyst-within-horizon gate — no catalyst inside the window → REVIEW / DEAD_MONEY
5. Sizing — from `risk_per_trade_pct` and `max_position_pct` cap

## How to run the routines

| Slash command | What it does |
|---|---|
| `/assess-portfolio` | Full PM-grade assessment: verdicts, per-holding record, catalyst research, new ideas |
| `/screen-ideas` | Rank `universe.md` by mechanical signals, then apply edge/asymmetry/catalyst gates |
| `/apply-trade` | Record an executed trade; prompts for PM-record fields on new buys |

## Key files

| File | Purpose |
|---|---|
| `PM_FRAMEWORK.md` | Full framework reference (citations, schema, label definitions) |
| `rules.md` | Tunable knobs (YAML) + decision rules prose — edit here to change policy |
| `holdings/*.md` | One position per file; YAML front-matter + thesis body |
| `holdings/_example.md` | Template — copy when opening a new position |
| `scripts/verdict.py` | Mechanically resolves SELL/TRIM/REVIEW/HOLD per holding |
| `scripts/targets.py` | Target price, laddered sell plan, time-stop date |
| `scripts/screener.py` | Mechanical signal ranker for universe.md |
| `reports/` | Dated assessment outputs |

## Holdings front-matter schema

Scripts parse YAML between `---` markers. Key PM-grade fields the user fills in
themselves at entry (the engine never invents these):
- `conviction`, `thesis_one_liner`, `variant_view` — qualitative edge/conviction
- `catalyst` (type/desc/date) — hard or soft, when it closes the price/value gap
- `initial_stop` — price-based defensive level
- `target_price` / `target_method` — the level your method points to
- `invalidation` — thesis-type trigger that proves you wrong (distinct from stop)
- `pre_mortem` — top failure reasons written at entry, before emotion revises them
- `last_review` — date of the last "would I buy this here today?" re-underwrite

## Conventions
- Tadawul tickers use the `.SR` suffix (e.g. `2222.SR`). US tickers as-is.
- Money is for the user's own analysis — never frame output as financial advice.
- The Shariah ratio pre-check is a heads-up only; Zoya/Musaffa are the source of truth.
- Don't fabricate figures: if a data fetch fails, report the gap.

## Setup
`pip install -r requirements.txt` (yfinance + pyyaml).
