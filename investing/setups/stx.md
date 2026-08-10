---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $840.99 holding the uptrend (no breakdown on volume)"
entry_price: 840.99
stop_price: 701.75
stop_logic: "chandelier trail: HH22 $936.49 - 3x ATR $78.25 = $701.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 1049.86
target_logic: "T1 $1049.86 = entry $840.99 + 1.5x R (R=$139.25); T2 $1258.73 = entry + 3x R; structure ceiling = 52w high $1144.85"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4644.7M; pass"
invalidation: "loses EMA20 $840.99 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
