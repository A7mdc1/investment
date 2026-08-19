---
ticker: FORM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $119.61 holding the uptrend (no breakdown on volume)"
entry_price: 119.61
stop_price: 110.01
stop_logic: "chandelier trail: HH22 $139.80 - 3x ATR $9.93 = $110.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 134.01
target_logic: "T1 $134.01 = entry $119.61 + 1.5x R (R=$9.60); T2 $148.42 = entry + 3x R; structure ceiling = 52w high $160.26"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $145.4M; pass"
invalidation: "loses EMA20 $119.61 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
