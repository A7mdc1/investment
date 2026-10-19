---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $230.49 holding the uptrend (no breakdown on volume)"
entry_price: 230.49
stop_price: 223.47
stop_logic: "chandelier trail: HH22 $243.68 - 3x ATR $6.74 = $223.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 241.01
target_logic: "T1 $241.01 = entry $230.49 + 1.5x R (R=$7.01); T2 $251.53 = entry + 3x R; structure ceiling = 52w high $281.98"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $176.6M; pass"
invalidation: "loses EMA20 $230.49 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
