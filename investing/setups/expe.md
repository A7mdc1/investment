---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $316.16 holding the uptrend (no breakdown on volume)"
entry_price: 316.16
stop_price: 304.32
stop_logic: "chandelier trail: HH22 $341.51 - 3x ATR $12.40 = $304.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 333.93
target_logic: "T1 $333.93 = entry $316.16 + 1.5x R (R=$11.85); T2 $351.70 = entry + 3x R; structure ceiling = 52w high $341.60"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $485.6M; pass"
invalidation: "loses EMA20 $316.16 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
