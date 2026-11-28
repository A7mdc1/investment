---
ticker: VLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $354.27 holding the uptrend (no breakdown on volume)"
entry_price: 354.27
stop_price: 352.73
stop_logic: "chandelier trail: HH22 $399.14 - 3x ATR $15.47 = $352.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 356.57
target_logic: "T1 $356.57 = entry $354.27 + 1.5x R (R=$1.54); T2 $358.88 = entry + 3x R; structure ceiling = 52w high $460.04"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1057.8M; pass"
invalidation: "loses EMA20 $354.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
