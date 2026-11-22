---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $335.39 holding the uptrend (no breakdown on volume)"
entry_price: 335.39
stop_price: 283.63
stop_logic: "chandelier trail: HH22 $379.43 - 3x ATR $31.93 = $283.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 413.05
target_logic: "T1 $413.05 = entry $335.39 + 1.5x R (R=$51.77); T2 $490.70 = entry + 3x R; structure ceiling = 52w high $748.14"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $407.6M; pass"
invalidation: "loses EMA20 $335.39 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
