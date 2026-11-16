---
ticker: VIAV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $32.02 holding the uptrend (no breakdown on volume)"
entry_price: 32.02
stop_price: 27.66
stop_logic: "chandelier trail: HH22 $36.51 - 3x ATR $2.95 = $27.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 38.55
target_logic: "T1 $38.55 = entry $32.02 + 1.5x R (R=$4.36); T2 $45.09 = entry + 3x R; structure ceiling = 52w high $60.43"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $203.8M; pass"
invalidation: "loses EMA20 $32.02 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
