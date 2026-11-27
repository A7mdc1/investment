---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $107.00 holding the uptrend (no breakdown on volume)"
entry_price: 107.00
stop_price: 95.21
stop_logic: "chandelier trail: HH22 $123.18 - 3x ATR $9.32 = $95.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 124.70
target_logic: "T1 $124.70 = entry $107.00 + 1.5x R (R=$11.80); T2 $142.39 = entry + 3x R; structure ceiling = 52w high $156.92"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $323.4M; pass"
invalidation: "loses EMA20 $107.00 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
