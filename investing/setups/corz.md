---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $21.61 holding the uptrend (no breakdown on volume)"
entry_price: 21.61
stop_price: 19.07
stop_logic: "chandelier trail: HH22 $24.66 - 3x ATR $1.86 = $19.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.42
target_logic: "T1 $25.42 = entry $21.61 + 1.5x R (R=$2.54); T2 $29.23 = entry + 3x R; structure ceiling = 52w high $30.46"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $285.6M; pass"
invalidation: "loses EMA20 $21.61 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
