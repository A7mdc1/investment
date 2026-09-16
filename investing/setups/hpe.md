---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $55.06 holding the uptrend (no breakdown on volume)"
entry_price: 55.06
stop_price: 52.02
stop_logic: "chandelier trail: HH22 $62.15 - 3x ATR $3.38 = $52.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.61
target_logic: "T1 $59.61 = entry $55.06 + 1.5x R (R=$3.03); T2 $64.15 = entry + 3x R; structure ceiling = 52w high $64.09"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1344.7M; pass"
invalidation: "loses EMA20 $55.06 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
