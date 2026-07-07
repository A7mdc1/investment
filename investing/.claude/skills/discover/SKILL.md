---
name: discover
description: Auto-discover fresh Shariah-plausible LEADS each run (no manual list needed) — builds a pool from halal-ETF holdings + yfinance screens, applies liquidity floors + the Shariah/asymmetry/catalyst gates, and writes leads.md with the top 20 by max benefit. Use when the user asks to auto-generate, discover, or find new candidates from scratch.
---

# Discover (auto-generate LEADS)

Build a candidate set automatically and surface the best 20 — the user does NOT
hand-list anything. This is the deliberate exception to "never invent tickers,"
scoped to discovery. Every name is a **LEAD**: an UNVERIFIED, no-setup-card,
no-edge idea to research — never a buy. Needs live Yahoo data (blocked in cloud
sandboxes — run locally; degrades to an empty pool gracefully).

## Steps

1. Run `python scripts/discover.py` and read the JSON. It:
   - Builds a pool = halal-ETF holdings (`discover_etfs`, e.g. SPUS — already
     business-screened) MERGED with yfinance predefined screens
     (`discover_screens`), deduped.
   - Applies the pipeline in order: **liquidity floor** (drops names under
     `screen_min_mcap` / `screen_min_avg_dollar_vol` — untradeable "reward"),
     **Shariah ratio knockout** (a ratio/business FLAG = absolute AVOID, dropped),
     technicals, an auto-fetched **earnings-date catalyst**, then **reward:risk**.
   - Assigns a mechanical verdict: **LEAD** (clean ratios + reward:risk ≥
     `discover_rr_floor` + catalyst within `catalyst_horizon_days`) or RESEARCH.
     **Discovery never emits BUY-CANDIDATE** — a machine pass with no setup card
     and no verified Shariah screen is a LEAD. EDGE is ALWAYS flagged NOT SUPPLIED.
   - Keeps the **top `discover_top_n` (20)** by a max-benefit composite and writes
     them to **`leads.md`** (machine-generated, overwritten every run). It does
     NOT touch `watchlist.md` (hand-curated).

2. Present a ranked table: rank, ticker, verdict (LEAD/RESEARCH), reward:risk,
   catalyst date, source (ETF/screen), whether it already HAS a setup card, and
   the binding gate for any RESEARCH name. Lead by stating plainly:
   - These are **auto-generated leads to investigate**, not buys or predictions.
   - **Shariah = UNVERIFIED** on every row — the ratio pre-check is not a business
     screen; the user MUST confirm each in Zoya/Musaffa before any add.
   - **EDGE = not supplied** — to promote a lead, the user writes
     `setups/<ticker>.md` (the ~10-min setup card) and screens the name compliant;
     `recommend.py` then re-gates it, and only then can it become BUY-CANDIDATE.

3. Note that `leads.md` was refreshed. To act on a lead, the user writes a setup
   card and (optionally) copies the name into the hand-curated `watchlist.md`;
   `recommend.py` / `/assess-portfolio` gate cards + curated names, not raw leads.

## Rules
- Compliance is a GATE: a ratio/business FLAG is excluded; everything else is
  UNVERIFIED, never "compliant." Never imply a name is Shariah-cleared.
- Discovery output tops out at LEAD — never call a discovered name BUY-CANDIDATE.
- "High reward" always stated with its paired risk/stop. No price targets framed
  as promises; no "will rise."
- If discover.py returns an empty pool / DATA_GAP (e.g. no network), say so
  plainly — never fabricate tickers, catalysts, or compliance.
- For any name the user decides to act on (after their own verification), point
  to /apply-trade so holdings + ledger + journal update.
- Reminder: short-term trading usually trails buy-and-hold after costs.
