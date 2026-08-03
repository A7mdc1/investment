---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $58.28 holding the uptrend (no breakdown on volume)"
entry_price: 58.28
stop_price: 56.93
stop_logic: "chandelier trail: HH22 $62.67 - 3x ATR $1.91 = $56.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.32
target_logic: "T1 $60.32 = entry $58.28 + 1.5x R (R=$1.35); T2 $62.35 = entry + 3x R; structure ceiling = 52w high $70.16"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $546.5M; pass"
invalidation: "loses EMA20 $58.28 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
