---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $343.16 holding the uptrend (no breakdown on volume)"
entry_price: 343.16
stop_price: 288.38
stop_logic: "chandelier trail: HH22 $379.43 - 3x ATR $30.35 = $288.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 425.33
target_logic: "T1 $425.33 = entry $343.16 + 1.5x R (R=$54.78); T2 $507.51 = entry + 3x R; structure ceiling = 52w high $749.16"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $403.3M; pass"
invalidation: "loses EMA20 $343.16 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
