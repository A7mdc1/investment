---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.92 holding the uptrend (no breakdown on volume)"
entry_price: 62.92
stop_price: 58.88
stop_logic: "chandelier trail: HH22 $66.64 - 3x ATR $2.59 = $58.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 68.99
target_logic: "T1 $68.99 = entry $62.92 + 1.5x R (R=$4.04); T2 $75.05 = entry + 3x R; structure ceiling = 52w high $72.46"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $175.0M; pass"
invalidation: "loses EMA20 $62.92 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
