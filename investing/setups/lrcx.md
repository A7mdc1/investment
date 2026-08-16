---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $316.35 holding the uptrend (no breakdown on volume)"
entry_price: 316.35
stop_price: 279.47
stop_logic: "chandelier trail: HH22 $345.12 - 3x ATR $21.88 = $279.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 371.67
target_logic: "T1 $371.67 = entry $316.35 + 1.5x R (R=$36.88); T2 $426.98 = entry + 3x R; structure ceiling = 52w high $438.47"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3218.9M; pass"
invalidation: "loses EMA20 $316.35 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
