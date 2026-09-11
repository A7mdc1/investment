---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $54.53 holding the uptrend (no breakdown on volume)"
entry_price: 54.53
stop_price: 53.54
stop_logic: "chandelier trail: HH22 $63.44 - 3x ATR $3.30 = $53.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 56.01
target_logic: "T1 $56.01 = entry $54.53 + 1.5x R (R=$0.99); T2 $57.49 = entry + 3x R; structure ceiling = 52w high $64.04"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1225.5M; pass"
invalidation: "loses EMA20 $54.53 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
