---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $106.85 (52w high) on >1.2x 20d avg volume"
entry_price: 106.85
stop_price: 94.51
stop_logic: "chandelier trail: HH22 $106.83 - 3x ATR $4.11 = $94.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 125.37
target_logic: "T1 $125.37 = entry $106.85 + 1.5x R (R=$12.35); T2 $143.89 = entry + 3x R; structure ceiling = 52w high $106.85"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $329.1M; pass"
invalidation: "closes back below the breakout level $106.85 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
