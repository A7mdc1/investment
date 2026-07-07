---
ticker: MU
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1032.92 holding the uptrend (no breakdown on volume)"
entry_price: 1032.92
stop_price: 949.32
stop_logic: "chandelier trail: HH22 $1254.81 - 3x ATR $101.83 = $949.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 1158.32
target_logic: "T1 $1158.32 = entry $1032.92 + 1.5x R (R=$83.60); T2 $1283.71 = entry + 3x R; structure ceiling = 52w high $1254.46"
holding_window_days: 21
catalyst: "2026-09-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $60831.2M; pass"
invalidation: "loses EMA20 $1032.92 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
