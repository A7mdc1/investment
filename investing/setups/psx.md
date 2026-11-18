---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $262.94 holding the uptrend (no breakdown on volume)"
entry_price: 262.94
stop_price: 262.37
stop_logic: "chandelier trail: HH22 $294.50 - 3x ATR $10.71 = $262.37 — exit when decline exceeds ~3 average daily ranges"
target_price: 263.78
target_logic: "T1 $263.78 = entry $262.94 + 1.5x R (R=$0.56); T2 $264.63 = entry + 3x R; structure ceiling = 52w high $299.55"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $856.4M; pass"
invalidation: "loses EMA20 $262.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
