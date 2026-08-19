---
ticker: VICR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $228.67 holding the uptrend (no breakdown on volume)"
entry_price: 228.67
stop_price: 196.10
stop_logic: "chandelier trail: HH22 $255.74 - 3x ATR $19.88 = $196.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 277.54
target_logic: "T1 $277.54 = entry $228.67 + 1.5x R (R=$32.58); T2 $326.40 = entry + 3x R; structure ceiling = 52w high $382.51"
holding_window_days: 21
catalyst: "2026-10-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $183.2M; pass"
invalidation: "loses EMA20 $228.67 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
