---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $353.35 holding the uptrend (no breakdown on volume)"
entry_price: 353.35
stop_price: 293.93
stop_logic: "chandelier trail: HH22 $385.97 - 3x ATR $30.68 = $293.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 442.49
target_logic: "T1 $442.49 = entry $353.35 + 1.5x R (R=$59.43); T2 $531.63 = entry + 3x R; structure ceiling = 52w high $749.45"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $401.3M; pass"
invalidation: "loses EMA20 $353.35 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
