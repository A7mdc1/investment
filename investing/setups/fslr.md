---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $219.49 holding the uptrend (no breakdown on volume)"
entry_price: 219.49
stop_price: 219.17
stop_logic: "chandelier trail: HH22 $252.17 - 3x ATR $11.00 = $219.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 219.98
target_logic: "T1 $219.98 = entry $219.49 + 1.5x R (R=$0.32); T2 $220.46 = entry + 3x R; structure ceiling = 52w high $320.81"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $446.0M; pass"
invalidation: "loses EMA20 $219.49 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
