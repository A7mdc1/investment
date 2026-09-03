---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $54.87 holding the uptrend (no breakdown on volume)"
entry_price: 54.87
stop_price: 54.45
stop_logic: "chandelier trail: HH22 $58.47 - 3x ATR $1.34 = $54.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 55.49
target_logic: "T1 $55.49 = entry $54.87 + 1.5x R (R=$0.42); T2 $56.12 = entry + 3x R; structure ceiling = 52w high $64.61"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $92.2M; pass"
invalidation: "loses EMA20 $54.87 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
