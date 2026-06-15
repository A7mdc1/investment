# Investment workspace

This repo tracks an investment portfolio as markdown. Each file in `holdings/`
is one position: YAML front-matter (ticker, shares, cost basis, Shariah status,
DCF assumptions) plus a free-text thesis/risks/notes section.

## How to assess the portfolio
Run the `/assess-portfolio` skill (see `.claude/skills/assess-portfolio/SKILL.md`).
It calls the scripts in `scripts/` and writes a dated report to `reports/`.

## Conventions
- Tadawul tickers use the `.SR` suffix (e.g. `2222.SR`). US tickers as-is.
- Money is for the user's own analysis — never frame output as financial advice.
- The Shariah ratio pre-check is a heads-up only; Zoya/Musaffa are the source of truth.
- Don't fabricate figures: if a data fetch fails, report the gap.

## Setup
`pip install -r requirements.txt` (yfinance + pyyaml).
