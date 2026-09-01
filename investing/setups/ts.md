---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $54.58 holding the uptrend (no breakdown on volume)"
entry_price: 54.58
stop_price: 54.47
stop_logic: "chandelier trail: HH22 $58.47 - 3x ATR $1.33 = $54.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 54.75
target_logic: "T1 $54.75 = entry $54.58 + 1.5x R (R=$0.11); T2 $54.92 = entry + 3x R; structure ceiling = 52w high $64.61"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $89.6M; pass"
invalidation: "loses EMA20 $54.58 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
