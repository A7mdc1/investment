---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $40.67 holding the uptrend (no breakdown on volume)"
entry_price: 40.67
stop_price: 40.40
stop_logic: "chandelier trail: HH22 $45.05 - 3x ATR $1.55 = $40.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 41.08
target_logic: "T1 $41.08 = entry $40.67 + 1.5x R (R=$0.27); T2 $41.49 = entry + 3x R; structure ceiling = 52w high $45.06"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $230.4M; pass"
invalidation: "loses EMA20 $40.67 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
