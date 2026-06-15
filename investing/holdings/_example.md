---
# Copy this file, rename it (e.g. 2222-aramco.md), and fill it in.
# The front-matter below is parsed by the scripts; the body is read by Claude.
ticker: 2222.SR          # Tadawul uses .SR ; US tickers as-is (e.g. AAPL)
name: Saudi Aramco
shares: 100
cost_basis: 32.50        # per share, in `currency`
currency: SAR
shariah:
  source: Zoya           # Zoya | Musaffa
  status: compliant      # compliant | non-compliant | doubtful
  screened: 2026-03-15   # last time you checked — flagged stale after ~1 quarter
dcf:                     # optional per-name overrides; omit to use defaults
  growth_5y: 0.04
  terminal_growth: 0.02
  discount_rate: 0.10
---

## Thesis
Why I own this. What has to stay true for the thesis to hold.

## Risks
What would break it.

## Notes
Anything Claude should weigh when assessing — recent earnings, purification
estimate, target weight, when to trim/add.
