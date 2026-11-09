---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $106.42 holding the uptrend (no breakdown on volume)"
entry_price: 106.42
stop_price: 105.88
stop_logic: "chandelier trail: HH22 $127.78 - 3x ATR $7.30 = $105.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 107.23
target_logic: "T1 $107.23 = entry $106.42 + 1.5x R (R=$0.54); T2 $108.04 = entry + 3x R; structure ceiling = 52w high $157.05"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $279.8M; pass"
invalidation: "loses EMA20 $106.42 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
