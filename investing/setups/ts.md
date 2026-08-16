---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $55.10 holding the uptrend (no breakdown on volume)"
entry_price: 55.10
stop_price: 54.55
stop_logic: "chandelier trail: HH22 $58.86 - 3x ATR $1.44 = $54.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 55.93
target_logic: "T1 $55.93 = entry $55.10 + 1.5x R (R=$0.55); T2 $56.76 = entry + 3x R; structure ceiling = 52w high $64.63"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $80.3M; pass"
invalidation: "loses EMA20 $55.10 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
