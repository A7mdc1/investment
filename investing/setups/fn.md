---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $346.33 holding the uptrend (no breakdown on volume)"
entry_price: 346.33
stop_price: 288.43
stop_logic: "chandelier trail: HH22 $379.80 - 3x ATR $30.46 = $288.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 433.18
target_logic: "T1 $433.18 = entry $346.33 + 1.5x R (R=$57.90); T2 $520.03 = entry + 3x R; structure ceiling = 52w high $748.05"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $403.0M; pass"
invalidation: "loses EMA20 $346.33 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
