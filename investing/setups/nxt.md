---
ticker: NXT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $81.33 holding the uptrend (no breakdown on volume)"
entry_price: 81.33
stop_price: 77.23
stop_logic: "chandelier trail: HH22 $90.62 - 3x ATR $4.46 = $77.23 — exit when decline exceeds ~3 average daily ranges"
target_price: 87.48
target_logic: "T1 $87.48 = entry $81.33 + 1.5x R (R=$4.10); T2 $93.63 = entry + 3x R; structure ceiling = 52w high $163.14"
holding_window_days: 21
catalyst: "2027-01-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $182.7M; pass"
invalidation: "loses EMA20 $81.33 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
