---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $163.70 holding the uptrend (no breakdown on volume)"
entry_price: 163.70
stop_price: 150.55
stop_logic: "chandelier trail: HH22 $189.01 - 3x ATR $12.82 = $150.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 183.41
target_logic: "T1 $183.41 = entry $163.70 + 1.5x R (R=$13.14); T2 $203.13 = entry + 3x R; structure ceiling = 52w high $288.89"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $177.1M; pass"
invalidation: "loses EMA20 $163.70 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
