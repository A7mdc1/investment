---
ticker: ARW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $212.64 holding the uptrend (no breakdown on volume)"
entry_price: 212.64
stop_price: 204.61
stop_logic: "chandelier trail: HH22 $230.45 - 3x ATR $8.61 = $204.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 224.68
target_logic: "T1 $224.68 = entry $212.64 + 1.5x R (R=$8.03); T2 $236.72 = entry + 3x R; structure ceiling = 52w high $237.23"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $124.4M; pass"
invalidation: "loses EMA20 $212.64 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
