---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1314.39 holding the uptrend (no breakdown on volume)"
entry_price: 1314.39
stop_price: 1311.57
stop_logic: "chandelier trail: HH22 $1453.00 - 3x ATR $47.14 = $1311.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 1318.61
target_logic: "T1 $1318.61 = entry $1314.39 + 1.5x R (R=$2.81); T2 $1322.83 = entry + 3x R; structure ceiling = 52w high $1452.79"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3877.9M; pass"
invalidation: "loses EMA20 $1314.39 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
