---
ticker: MKSI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $312.47 holding the uptrend (no breakdown on volume)"
entry_price: 312.47
stop_price: 281.97
stop_logic: "chandelier trail: HH22 $349.07 - 3x ATR $22.37 = $281.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 358.23
target_logic: "T1 $358.23 = entry $312.47 + 1.5x R (R=$30.50); T2 $403.98 = entry + 3x R; structure ceiling = 52w high $447.46"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $448.4M; pass"
invalidation: "loses EMA20 $312.47 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
