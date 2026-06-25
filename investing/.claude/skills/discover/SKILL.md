---
name: discover
description: Auto-discover fresh Shariah-plausible candidate ideas each run (no manual list needed) — builds a pool from halal-ETF holdings + yfinance screens, runs the PM edge/asymmetry/catalyst gates, and rewrites watchlist.md with the top 20 by max benefit. Use when the user asks to auto-generate, discover, or find new candidates from scratch.
---

# Discover (auto-generate candidates)

Build a candidate set automatically and surface the best 20 — the user does NOT
hand-list anything. This is the deliberate exception to "never invent tickers,"
scoped to discovery. Every name is an UNVERIFIED lead to research, NOT a buy.
Needs live Yahoo data (blocked in cloud sandboxes — run locally).

## Steps

1. Run `python scripts/discover.py` and read the JSON. It:
   - Builds a pool = halal-ETF holdings (`discover_etfs`, e.g. SPUS — already
     business-screened) MERGED with yfinance predefined screens
     (`discover_screens`), deduped.
   - Applies the PM pipeline in order: **Shariah ratio knockout first** (a ratio
     FLAG = absolute AVOID, dropped), then technicals, then an auto-fetched
     **earnings-date catalyst**, then **reward:risk asymmetry**.
   - Assigns a verdict mechanically (choice: BUY-CANDIDATE allowed on
     mechanics — clean ratios + reward:risk ≥ `reward_risk_min_swing` + catalyst
     within `catalyst_horizon_days`). EDGE is ALWAYS flagged NOT SUPPLIED.
   - Keeps the **top `discover_top_n` (20)** by a max-benefit composite
     (asymmetry-led, then signal score, then catalyst proximity) and **rewrites
     watchlist.md** with them (preserving its header/themes/hard-rules sections).

2. Present a ranked table: rank, ticker, verdict, reward:risk, catalyst date,
   source (ETF/screen), and the binding gate for any RESEARCH name. Lead by
   stating plainly:
   - These are **auto-generated leads to investigate**, not buys or predictions.
   - **Shariah = UNVERIFIED** on every row — the ratio pre-check is not a business
     screen; the user MUST confirm each in Zoya/Musaffa before any add.
   - **EDGE = not supplied** — a BUY-CANDIDATE here cleared the *mechanical* bar
     only; the variant view (why the market is wrong) is still the user's to add,
     by editing that name's `why` in watchlist.md or a holding thesis.

3. Note that `watchlist.md` was refreshed, so `/assess-portfolio` and
   `python scripts/recommend.py` will now ingest these names.

## Rules
- Compliance is a GATE: a ratio FLAG is excluded; everything else is UNVERIFIED,
  never "compliant." Never imply a name is Shariah-cleared.
- "High reward" always stated with its paired risk/stop. No price targets framed
  as promises; no "will rise."
- If discover.py returns an empty pool / DATA_GAP (e.g. no network), say so
  plainly — never fabricate tickers, catalysts, or compliance.
- For any name the user decides to act on (after their own verification), point
  to /apply-trade so holdings + ledger update.
- Reminder: short-term trading usually trails buy-and-hold after costs.
