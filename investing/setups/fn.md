---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $341.25 holding the uptrend (no breakdown on volume)"
entry_price: 341.25
stop_price: 286.91
stop_logic: "chandelier trail: HH22 $379.43 - 3x ATR $30.84 = $286.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 422.75
target_logic: "T1 $422.75 = entry $341.25 + 1.5x R (R=$54.34); T2 $504.26 = entry + 3x R; structure ceiling = 52w high $748.80"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $399.1M; pass"
invalidation: "loses EMA20 $341.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
