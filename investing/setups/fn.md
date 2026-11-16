---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $350.21 holding the uptrend (no breakdown on volume)"
entry_price: 350.21
stop_price: 289.87
stop_logic: "chandelier trail: HH22 $381.37 - 3x ATR $30.50 = $289.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 440.73
target_logic: "T1 $440.73 = entry $350.21 + 1.5x R (R=$60.34); T2 $531.24 = entry + 3x R; structure ceiling = 52w high $748.07"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $406.1M; pass"
invalidation: "loses EMA20 $350.21 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
