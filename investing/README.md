# Portfolio assessment routine (Claude Code)

A local routine that reads your holdings as markdown and assesses them across
**price/performance**, **Shariah compliance**, and **DCF valuation**.

## Layout
```
investing/
├── CLAUDE.md                         # project memory (Claude reads on launch)
├── requirements.txt
├── .claude/skills/assess-portfolio/  # the /assess-portfolio routine
│   └── SKILL.md
├── holdings/                         # one .md per position
│   └── _example.md                   # copy this to add a holding
├── scripts/                          # deterministic number-crunching
│   ├── common.py   prices.py   shariah.py   dcf.py
└── reports/                          # dated assessments land here
```

## Setup
1. `pip install -r requirements.txt`
2. Copy `holdings/_example.md` → e.g. `holdings/2222-aramco.md`, fill it in. Repeat per position.
3. Open the folder in Claude Code and run `/assess-portfolio`.

You can also run any script standalone, e.g. `python scripts/dcf.py`.

## Auto-discovery (run locally)
`python scripts/discover.py` (or `/discover`, also run automatically at the start
of `/assess-portfolio`) auto-builds a candidate pool from halal-ETF holdings
(e.g. SPUS) + yfinance screens, runs the PM edge/asymmetry/catalyst gates, and
**rewrites `watchlist.md`** with the top 20 by max benefit — no manual list
needed. Tune it in `rules.md` (`discover_*` knobs).
- Needs **live Yahoo data**, so run it on your own machine — managed sandboxes
  block Yahoo, leaving the pool empty.
- Output is **leads to research, not buys**: Shariah is UNVERIFIED (confirm in
  Zoya/Musaffa) and EDGE is never auto-supplied (you add the variant view).

## Notes
- Tadawul tickers use the `.SR` suffix (2222.SR = Aramco).
- The Shariah ratio pre-check is a heads-up, **not** a replacement for Zoya/Musaffa.
- Everything is your own analysis, not financial advice.
