---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $61.27 holding the uptrend (no breakdown on volume)"
entry_price: 61.27
stop_price: 59.67
stop_logic: "chandelier trail: HH22 $65.17 - 3x ATR $1.83 = $59.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.67
target_logic: "T1 $63.67 = entry $61.27 + 1.5x R (R=$1.60); T2 $66.07 = entry + 3x R; structure ceiling = 52w high $69.92"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $522.0M; pass"
invalidation: "loses EMA20 $61.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
