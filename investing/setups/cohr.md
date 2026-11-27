---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $214.34 holding the uptrend (no breakdown on volume)"
entry_price: 214.34
stop_price: 170.38
stop_logic: "chandelier trail: HH22 $246.90 - 3x ATR $25.51 = $170.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 280.28
target_logic: "T1 $280.28 = entry $214.34 + 1.5x R (R=$43.96); T2 $346.22 = entry + 3x R; structure ceiling = 52w high $439.86"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2187.2M; pass"
invalidation: "loses EMA20 $214.34 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
