# Swing-trade decision support (Claude Code)

A local, Shariah-gated decision-support system for **short-horizon,
high-asymmetry swing trades**. It reads your holdings and setup cards as
markdown and sharpens each *individual trade decision*: a verified setup, honest
asymmetry math, gap-aware risk, a hard Shariah gate, and a feedback loop that
measures which setups actually pay. It gates trade **quality** — it never caps
trade **quantity** or sizing; those are your decisions.

## The workflow (swing-first)

```
discover.py → leads.md → scaffold.py → DRAFT cards → you review/edit + status:planned → Zoya/Musaffa → recommend.py → you size & execute → /apply-trade → journal.py
  (machine,    (machine,   (machine     (proposed      (approve: research,          (you verify   (re-gates:         (your call on        (logs         (review by
   wide net)    refreshed)  fills cards) trade plans)   edit, flip to planned)       compliance)   BUY-CANDIDATE)     volume & size)       entry+exit)   setup type)
```

1. **Discover** — `python scripts/discover.py` builds a pool (halal-ETF holdings +
   yfinance screens), applies liquidity floors + Shariah/asymmetry/catalyst gates,
   and writes **`leads.md`** (machine, overwritten each run). Never touches `watchlist.md`.
2. **Scaffold** — `python scripts/scaffold.py --all-leads` auto-fills a **DRAFT**
   setup card (`status: draft`) for every lead: complete proposed plans
   (entry/stop/target/logic/invalidation) from Yahoo formula outputs. The
   assessment report presents these for review.
3. **Review & approve** — read the draft plans, do your own research, edit anything
   you disagree with, then set **`status: planned`**. *The card is the "edge"* — a
   defined setup, not a fundamental thesis. A draft can never become a buy candidate
   on its own.
4. **Screen** the name in Zoya/Musaffa; record `shariah.status: compliant`/date on
   the card (the scaffold leaves it `unverified` — only you set compliant).
5. **Recommend** — `python scripts/recommend.py` re-gates. Only a completed,
   **planned**, compliant, fresh card with reward:risk ≥ floor and a catalyst in the
   window clears to **BUY-CANDIDATE**. Everything else is RESEARCH; discovery output
   is only ever **LEAD**; a draft is only ever RESEARCH.
6. **You size and execute** — informed by the gap-adjusted numbers (a stop does
   not execute through an earnings gap).
7. **Journal** — `/apply-trade` logs entry and exit to `journal.csv`.
8. **Review** — `python scripts/journal.py` reports **per-setup expectancy**:
   which setups pay you, hit rate, avg win/loss R, slippage on stops, and P&L vs a
   benchmark counterfactual.

**Two invariants:** a machine-filled DRAFT card can never reach BUY-CANDIDATE
without your `status: planned` approval; the scaffold never writes
`shariah: compliant` — only a human Zoya/Musaffa screen does.

## Layout
```
investing/
├── CLAUDE.md                         # project memory (Claude reads on launch)
├── PM_FRAMEWORK.md                   # the buy-side decision framework
├── requirements.txt
├── .claude/skills/                   # /assess-portfolio /screen-ideas /discover /apply-trade
├── holdings/         one .md per open position (_example.md = template)
├── setups/           one card per prospective trade (_template.md, README.md)
├── scripts/          discover.py scaffold.py recommend.py verdict.py journal.py apply_txn.py …
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
