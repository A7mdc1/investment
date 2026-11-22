---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $347.51 holding the uptrend (no breakdown on volume)"
entry_price: 347.51
stop_price: 334.91
stop_logic: "chandelier trail: HH22 $360.83 - 3x ATR $8.64 = $334.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 366.40
target_logic: "T1 $366.40 = entry $347.51 + 1.5x R (R=$12.60); T2 $385.29 = entry + 3x R; structure ceiling = 52w high $360.97"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $17228.8M; pass"
invalidation: "loses EMA20 $347.51 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
