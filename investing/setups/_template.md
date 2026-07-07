---
# Copy this to setups/<ticker>.md (e.g. setups/ibrx.md) and fill it in.
# Target: ~10 minutes. This card IS the "edge" for a swing trade — a defined,
# repeatable setup, not a fundamental thesis. recommend.py will not call a name
# BUY-CANDIDATE until this card is complete AND Shariah is verified below.
ticker: IBRX
status: planned            # draft | planned | live | closed | abandoned
                           # draft = machine-filled by scaffold.py, unreviewed (caps at RESEARCH);
                           # you review/edit and set `planned` to approve it.
setup_type: earnings_run   # your taxonomy: breakout | pullback | earnings_run | post_earnings_drift | other
entry_trigger: ""          # the SPECIFIC condition that puts the trade on (price/volume/event) — REQUIRED
entry_price: null
stop_price: null
stop_logic: ""             # WHY the stop is there — structure (prior low, ATR band), not a round number — REQUIRED
target_price: null
target_logic: ""           # why price can reach the target inside the holding window — REQUIRED
holding_window_days: null  # expected duration in calendar days
catalyst: null             # date + type (e.g. "2026-08-05 earnings")
earnings_plan: exit_before # exit_before | hold_through_sized_down | no_earnings_in_window — REQUIRED
liquidity_check: null      # avg $ volume + is the spread acceptable? (note a number + yes/no)
invalidation: ""           # what kills the setup BEFORE the stop (failed breakout, volume dry-up) — REQUIRED
shariah:
  status: unverified       # unverified | compliant | non-compliant  (must be `compliant` + fresh for BUY-CANDIDATE)
  source: null             # zoya | musaffa
  screened: null           # ISO date of the screen (goes stale after ~1 quarter)
---

## Notes
The plan in your own words: what you're watching for, how you'll manage it, what
would make you stand aside. Keep it short — a swing card you'll actually re-use.
