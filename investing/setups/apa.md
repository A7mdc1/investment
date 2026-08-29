---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $40.48 holding the uptrend (no breakdown on volume)"
entry_price: 40.48
stop_price: 40.27
stop_logic: "chandelier trail: HH22 $45.05 - 3x ATR $1.59 = $40.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 40.78
target_logic: "T1 $40.78 = entry $40.48 + 1.5x R (R=$0.20); T2 $41.09 = entry + 3x R; structure ceiling = 52w high $45.04"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $238.2M; pass"
invalidation: "loses EMA20 $40.48 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
