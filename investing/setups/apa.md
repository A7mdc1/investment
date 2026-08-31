---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $40.87 holding the uptrend (no breakdown on volume)"
entry_price: 40.87
stop_price: 40.32
stop_logic: "chandelier trail: HH22 $45.05 - 3x ATR $1.58 = $40.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 41.69
target_logic: "T1 $41.69 = entry $40.87 + 1.5x R (R=$0.55); T2 $42.51 = entry + 3x R; structure ceiling = 52w high $45.03"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $224.2M; pass"
invalidation: "loses EMA20 $40.87 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
