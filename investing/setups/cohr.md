---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $217.95 holding the uptrend (no breakdown on volume)"
entry_price: 217.95
stop_price: 176.51
stop_logic: "chandelier trail: HH22 $246.90 - 3x ATR $23.46 = $176.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 280.11
target_logic: "T1 $280.11 = entry $217.95 + 1.5x R (R=$41.44); T2 $342.27 = entry + 3x R; structure ceiling = 52w high $439.48"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2180.4M; pass"
invalidation: "loses EMA20 $217.95 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
