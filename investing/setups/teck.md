---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.87 holding the uptrend (no breakdown on volume)"
entry_price: 62.87
stop_price: 60.55
stop_logic: "chandelier trail: HH22 $68.11 - 3x ATR $2.52 = $60.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 66.34
target_logic: "T1 $66.34 = entry $62.87 + 1.5x R (R=$2.32); T2 $69.81 = entry + 3x R; structure ceiling = 52w high $72.46"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $176.8M; pass"
invalidation: "loses EMA20 $62.87 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
