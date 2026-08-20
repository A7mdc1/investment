---
ticker: VLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $352.85 (52w high) on >1.2x 20d avg volume"
entry_price: 352.85
stop_price: 318.92
stop_logic: "chandelier trail: HH22 $352.70 - 3x ATR $11.26 = $318.92 — exit when decline exceeds ~3 average daily ranges"
target_price: 403.74
target_logic: "T1 $403.74 = entry $352.85 + 1.5x R (R=$33.93); T2 $454.63 = entry + 3x R; structure ceiling = 52w high $352.85"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $793.9M; pass"
invalidation: "closes back below the breakout level $352.85 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
