---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $849.46 holding the uptrend (no breakdown on volume)"
entry_price: 849.46
stop_price: 708.93
stop_logic: "chandelier trail: HH22 $937.54 - 3x ATR $76.20 = $708.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 1060.26
target_logic: "T1 $1060.26 = entry $849.46 + 1.5x R (R=$140.53); T2 $1271.05 = entry + 3x R; structure ceiling = 52w high $1144.74"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4548.0M; pass"
invalidation: "loses EMA20 $849.46 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
