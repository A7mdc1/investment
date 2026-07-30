---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $57.78 holding the uptrend (no breakdown on volume)"
entry_price: 57.78
stop_price: 56.83
stop_logic: "chandelier trail: HH22 $62.67 - 3x ATR $1.95 = $56.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.20
target_logic: "T1 $59.20 = entry $57.78 + 1.5x R (R=$0.95); T2 $60.63 = entry + 3x R; structure ceiling = 52w high $70.21"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $578.8M; pass"
invalidation: "loses EMA20 $57.78 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
