---
ticker: FIG
name: Figma, Inc
shares: 0
cost_basis: 21.43
currency: USD
trade_type: core      # exiting on compliance
last_price: 19.26
week52_low: 16.60
week52_high: 142.85
shariah:
  source: broker_app
  status: non-compliant     # <-- conflicts with mandate; top-priority flag
  screened: 2026-06-09
dcf:
  growth_5y: 0.30
  terminal_growth: 0.03
  discount_rate: 0.12

# === PM decision record (see PM_FRAMEWORK.md) ===
conviction:                    # moot — compliance gate overrides conviction either way
thesis_one_liner: High-growth design platform, but off-mandate; exiting on 
  compliance, not price.
variant_view:                  # not applicable — this is a policy exit, not a mispricing call
catalyst:
  type: hard
  desc: Config 2026 investor/analyst session
  date: 2026-06-23
initial_stop:
target_price:
target_method:
invalidation:                   # n/a — COMPLIANCE_GATE alone is sufficient grounds to exit
invalidation_hit: false
pre_mortem: [null]
last_review: 2026-06-15
closed: '2026-07-13'
realized_pl: 54.95
---

## Thesis
(Originally) high-growth design platform. NOTE: flagged non-Shariah-compliant by
broker app — under the screening mandate this position is off-policy irrespective
of price.

## Variant view
Not applicable — this is a compliance-driven exit, not a mispricing thesis. The
mandate gate overrides any view on valuation or growth.

## Risks
AI-native design competition (e.g. Google), premium valuation, operating losses,
short interest >36%. 52-week lows despite Q1 beat (+46% rev) and raised guidance.

## What would change my mind
A re-screen in Zoya/Musaffa showing compliant status — the only thing that could
reopen the question, since the gate is the sole decision driver.

## Notes
Decision driver here is the compliance flag, not the chart. Next catalyst:
Config 2026 investor session 2026-06-23 to 06-25. Verify status in Zoya/Musaffa.


## Closed 2026-07-13
Realized P/L: 54.95
