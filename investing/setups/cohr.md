---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $218.03 holding the uptrend (no breakdown on volume)"
entry_price: 218.03
stop_price: 174.54
stop_logic: "chandelier trail: HH22 $246.90 - 3x ATR $24.12 = $174.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 283.25
target_logic: "T1 $283.25 = entry $218.03 + 1.5x R (R=$43.48); T2 $348.48 = entry + 3x R; structure ceiling = 52w high $440.06"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2175.4M; pass"
invalidation: "loses EMA20 $218.03 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
