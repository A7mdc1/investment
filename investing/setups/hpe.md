---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $59.10 holding the uptrend (no breakdown on volume)"
entry_price: 59.10
stop_price: 54.55
stop_logic: "chandelier trail: HH22 $65.65 - 3x ATR $3.70 = $54.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.94
target_logic: "T1 $65.94 = entry $59.10 + 1.5x R (R=$4.56); T2 $72.77 = entry + 3x R; structure ceiling = 52w high $65.64"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1543.3M; pass"
invalidation: "loses EMA20 $59.10 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
