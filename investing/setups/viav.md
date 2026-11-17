---
ticker: VIAV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $31.73 holding the uptrend (no breakdown on volume)"
entry_price: 31.73
stop_price: 27.85
stop_logic: "chandelier trail: HH22 $36.47 - 3x ATR $2.87 = $27.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 37.56
target_logic: "T1 $37.56 = entry $31.73 + 1.5x R (R=$3.88); T2 $43.38 = entry + 3x R; structure ceiling = 52w high $60.46"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $204.4M; pass"
invalidation: "loses EMA20 $31.73 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
