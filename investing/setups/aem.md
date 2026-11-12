---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $183.94 holding the uptrend (no breakdown on volume)"
entry_price: 183.94
stop_price: 176.82
stop_logic: "chandelier trail: HH22 $202.24 - 3x ATR $8.47 = $176.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 194.63
target_logic: "T1 $194.63 = entry $183.94 + 1.5x R (R=$7.12); T2 $205.31 = entry + 3x R; structure ceiling = 52w high $254.10"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $354.6M; pass"
invalidation: "loses EMA20 $183.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
