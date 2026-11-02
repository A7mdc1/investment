---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $166.57 holding the uptrend (no breakdown on volume)"
entry_price: 166.57
stop_price: 163.84
stop_logic: "chandelier trail: HH22 $175.75 - 3x ATR $3.97 = $163.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 170.67
target_logic: "T1 $170.67 = entry $166.57 + 1.5x R (R=$2.73); T2 $174.77 = entry + 3x R; structure ceiling = 52w high $235.94"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $261.2M; pass"
invalidation: "loses EMA20 $166.57 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
