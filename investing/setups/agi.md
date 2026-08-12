---
ticker: AGI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $30.97 holding the uptrend (no breakdown on volume)"
entry_price: 30.97
stop_price: 30.72
stop_logic: "chandelier trail: HH22 $34.49 - 3x ATR $1.26 = $30.72 — exit when decline exceeds ~3 average daily ranges"
target_price: 31.33
target_logic: "T1 $31.33 = entry $30.97 + 1.5x R (R=$0.24); T2 $31.70 = entry + 3x R; structure ceiling = 52w high $55.26"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $148.2M; pass"
invalidation: "loses EMA20 $30.97 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
