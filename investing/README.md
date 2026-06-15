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

## Notes
- Tadawul tickers use the `.SR` suffix (2222.SR = Aramco).
- The Shariah ratio pre-check is a heads-up, **not** a replacement for Zoya/Musaffa.
- Everything is your own analysis, not financial advice.
