---
ticker: VIAV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $32.52 holding the uptrend (no breakdown on volume)"
entry_price: 32.52
stop_price: 32.45
stop_logic: "chandelier trail: HH22 $41.49 - 3x ATR $3.02 = $32.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.64
target_logic: "T1 $32.64 = entry $32.52 + 1.5x R (R=$0.08); T2 $32.76 = entry + 3x R; structure ceiling = 52w high $60.46"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $204.6M; pass"
invalidation: "loses EMA20 $32.52 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
