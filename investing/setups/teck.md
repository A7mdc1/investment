---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.87 holding the uptrend (no breakdown on volume)"
entry_price: 62.87
stop_price: 61.25
stop_logic: "chandelier trail: HH22 $68.10 - 3x ATR $2.28 = $61.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.30
target_logic: "T1 $65.30 = entry $62.87 + 1.5x R (R=$1.62); T2 $67.72 = entry + 3x R; structure ceiling = 52w high $71.14"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $198.5M; pass"
invalidation: "loses EMA20 $62.87 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
