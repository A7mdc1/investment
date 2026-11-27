---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $324.42 holding the uptrend (no breakdown on volume)"
entry_price: 324.42
stop_price: 278.99
stop_logic: "chandelier trail: HH22 $379.43 - 3x ATR $33.48 = $278.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 392.57
target_logic: "T1 $392.57 = entry $324.42 + 1.5x R (R=$45.43); T2 $460.71 = entry + 3x R; structure ceiling = 52w high $748.52"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $392.0M; pass"
invalidation: "loses EMA20 $324.42 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
