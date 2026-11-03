---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $362.31 holding the uptrend (no breakdown on volume)"
entry_price: 362.31
stop_price: 349.19
stop_logic: "chandelier trail: HH22 $371.72 - 3x ATR $7.51 = $349.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 381.98
target_logic: "T1 $381.98 = entry $362.31 + 1.5x R (R=$13.12); T2 $401.65 = entry + 3x R; structure ceiling = 52w high $420.62"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $156.2M; pass"
invalidation: "loses EMA20 $362.31 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
