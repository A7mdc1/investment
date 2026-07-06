---
# Copy this file, rename it (e.g. 2222-aramco.md), and fill it in.
# The front-matter below is parsed by the scripts; the body is read by Claude.
ticker: 2222.SR          # Tadawul uses .SR ; US tickers as-is (e.g. AAPL)
name: Saudi Aramco
shares: 100
cost_basis: 32.50        # per share, in `currency`
currency: SAR
trade_type: core         # core | swing | momentum | catalyst
opened: 2026-01-15       # date you entered, for duration/time-stop tracking
shariah:
  source: Zoya           # Zoya | Musaffa
  status: compliant      # compliant | non-compliant | doubtful
  screened: 2026-03-15   # last time you checked — flagged stale after ~1 quarter
dcf:                     # optional per-name overrides; omit to use defaults
  growth_5y: 0.04
  terminal_growth: 0.02
  discount_rate: 0.10

# === PM decision record (see PM_FRAMEWORK.md) — fill in YOUR own judgment ===
# The engine never invents these; leave null until you've done the work.
conviction: null              # high | medium | low — edge size x evidence strength
thesis_one_liner: null        # the claim in one sentence
variant_view: null            # your view vs. consensus + which edge (informational/
                               # analytical/behavioral) — required before BUY-CANDIDATE
catalyst:
  type: null                  # hard (dated event) | soft (time/re-rating)
  desc: null
  date: null                  # YYYY-MM-DD if hard
initial_stop: null            # price-based defensive level (distinct from invalidation)
target_price: null            # the level your method points to
target_method: null           # r_multiple | structure | atr | dcf | peer_multiple
invalidation: null            # the precise, thesis-type trigger that proves you wrong
invalidation_hit: false       # set true when that trigger actually occurs -> SELL
pre_mortem:                   # top 2-3 reasons this fails, written NOW at entry
  - null
last_review: null             # YYYY-MM-DD of your last "would I buy this today?" check
---

## Thesis
Why I own this. What has to stay true for the thesis to hold.

## Variant view
Specifically why the market has this wrong, and why you're right. If you can't
write this, the position can't clear BUY-CANDIDATE — RESEARCH it further.

## Risks
What would break it. (Top items belong in `pre_mortem` above, written at entry.)

## What would change my mind
The conditions that would flip your verdict — separate from the hard stop.

## Notes
Anything Claude should weigh when assessing — recent earnings, purification
estimate, target weight, when to trim/add.
