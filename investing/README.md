# Swing-trade decision support (Claude Code)

A local, Shariah-gated decision-support system for **short-horizon,
high-asymmetry swing trades**. It reads your holdings and setup cards as
markdown and sharpens each *individual trade decision*: a verified setup, honest
asymmetry math, gap-aware risk, a hard Shariah gate, and a feedback loop that
measures which setups actually pay. It gates trade **quality** — it never caps
trade **quantity** or sizing; those are your decisions.

## The workflow (swing-first)

```
discover.py  →  leads.md  →  setups/<ticker>.md  →  Zoya/Musaffa  →  recommend.py  →  you size & execute  →  /apply-trade  →  journal.py
   (machine,      (machine,     (you: the ~10-min       (you: verify        (re-gates:            (your call on          (logs entry+exit)   (monthly review
    wide net)      refreshed)    setup card = edge)      compliance)          BUY-CANDIDATE)        volume & size)                          by setup type)
```

1. **Discover** — `python scripts/discover.py` builds a pool (halal-ETF holdings +
   yfinance screens), applies liquidity floors + Shariah/asymmetry/catalyst gates,
   and writes **`leads.md`** (machine, overwritten each run). It never touches
   `watchlist.md`.
2. **Scan leads** — pick the few worth planning.
3. **Write a setup card** — copy `setups/_template.md` → `setups/<ticker>.md`
   (~10 min): entry trigger, stop logic, target logic, earnings plan, invalidation.
   *This card is the "edge"* — not a fundamental thesis.
4. **Screen** the name in Zoya/Musaffa; record `shariah.status`/date on the card.
5. **Recommend** — `python scripts/recommend.py` re-gates. Only a completed,
   compliant, fresh card with reward:risk ≥ floor and a catalyst in the window
   clears to **BUY-CANDIDATE**. Everything else is RESEARCH; discovery output is
   only ever **LEAD**.
6. **You size and execute** — informed by the gap-adjusted numbers (a stop does
   not execute through an earnings gap).
7. **Journal** — `/apply-trade` logs entry and exit to `journal.csv`.
8. **Review** — `python scripts/journal.py` reports **per-setup expectancy**:
   which setups pay you, hit rate, avg win/loss R, slippage on stops, and P&L vs a
   benchmark counterfactual.

## Layout
```
investing/
├── CLAUDE.md                         # project memory (Claude reads on launch)
├── PM_FRAMEWORK.md                   # the buy-side decision framework
├── requirements.txt
├── .claude/skills/                   # /assess-portfolio /screen-ideas /discover /apply-trade
├── holdings/         one .md per open position (_example.md = template)
├── setups/           one card per prospective trade (_template.md, README.md)
├── scripts/          discover.py recommend.py verdict.py journal.py apply_txn.py …
├── leads.md          MACHINE-generated (discover.py overwrites it) — do not hand-edit
├── watchlist.md      HAND-curated — no script writes it
└── reports/          dated assessments land here
```

## Setup
1. `pip install -r requirements.txt`
2. Copy `holdings/_example.md` → e.g. `holdings/2222-aramco.md`, fill it in. Repeat per position.
3. Open the folder in Claude Code and run `/assess-portfolio`.

You can also run any script standalone, e.g. `python scripts/journal.py`.

## Division of labor
- The system gates **quality**: setup completeness, honest asymmetry, a gap plan,
  and compliance. A raw discovery row or an unverified name can never become a buy.
- **You** decide quantity and sizing, informed by the gap-adjusted numbers and the
  journal's per-setup expectancy.
- Discovery needs **live Yahoo data** — run it on your own machine; managed
  sandboxes block Yahoo and leave the pool empty (handled gracefully).

## Notes
- Tadawul tickers use the `.SR` suffix (2222.SR = Aramco).
- The Shariah ratio pre-check is a heads-up, **not** a replacement for Zoya/Musaffa.
- Institutional process raises decision *quality*; it does not guarantee returns —
  most retail short-term traders lose money net of costs. Everything here is your
  own analysis, **not financial advice**.
