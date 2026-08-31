---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $318.29 holding the uptrend (no breakdown on volume)"
entry_price: 318.29
stop_price: 303.94
stop_logic: "chandelier trail: HH22 $341.51 - 3x ATR $12.52 = $303.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 339.82
target_logic: "T1 $339.82 = entry $318.29 + 1.5x R (R=$14.35); T2 $361.34 = entry + 3x R; structure ceiling = 52w high $341.53"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $469.6M; pass"
invalidation: "loses EMA20 $318.29 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
