---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $225.67 holding the uptrend (no breakdown on volume)"
entry_price: 225.67
stop_price: 185.64
stop_logic: "chandelier trail: HH22 $252.28 - 3x ATR $22.21 = $185.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 285.72
target_logic: "T1 $285.72 = entry $225.67 + 1.5x R (R=$40.03); T2 $345.76 = entry + 3x R; structure ceiling = 52w high $439.71"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2013.8M; pass"
invalidation: "loses EMA20 $225.67 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
