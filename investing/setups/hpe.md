---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $54.83 holding the uptrend (no breakdown on volume)"
entry_price: 54.83
stop_price: 52.19
stop_logic: "chandelier trail: HH22 $62.15 - 3x ATR $3.32 = $52.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 58.79
target_logic: "T1 $58.79 = entry $54.83 + 1.5x R (R=$2.64); T2 $62.75 = entry + 3x R; structure ceiling = 52w high $64.10"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1335.3M; pass"
invalidation: "loses EMA20 $54.83 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
