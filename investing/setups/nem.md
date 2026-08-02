---
ticker: NEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $94.15 holding the uptrend (no breakdown on volume)"
entry_price: 94.15
stop_price: 88.72
stop_logic: "chandelier trail: HH22 $98.93 - 3x ATR $3.40 = $88.72 — exit when decline exceeds ~3 average daily ranges"
target_price: 102.28
target_logic: "T1 $102.28 = entry $94.15 + 1.5x R (R=$5.43); T2 $110.42 = entry + 3x R; structure ceiling = 52w high $134.26"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $675.0M; pass"
invalidation: "loses EMA20 $94.15 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
