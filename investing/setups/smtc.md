---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $144.56 holding the uptrend (no breakdown on volume)"
entry_price: 144.56
stop_price: 136.35
stop_logic: "chandelier trail: HH22 $170.43 - 3x ATR $11.36 = $136.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 156.88
target_logic: "T1 $156.88 = entry $144.56 + 1.5x R (R=$8.21); T2 $169.19 = entry + 3x R; structure ceiling = 52w high $177.34"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $476.0M; pass"
invalidation: "loses EMA20 $144.56 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
