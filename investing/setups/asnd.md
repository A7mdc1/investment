---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $233.73 holding the uptrend (no breakdown on volume)"
entry_price: 233.73
stop_price: 225.85
stop_logic: "chandelier trail: HH22 $244.58 - 3x ATR $6.24 = $225.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 245.54
target_logic: "T1 $245.54 = entry $233.73 + 1.5x R (R=$7.88); T2 $257.36 = entry + 3x R; structure ceiling = 52w high $282.00"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $172.7M; pass"
invalidation: "loses EMA20 $233.73 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
