---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $58.92 holding the uptrend (no breakdown on volume)"
entry_price: 58.92
stop_price: 55.99
stop_logic: "chandelier trail: HH22 $61.35 - 3x ATR $1.79 = $55.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 63.30
target_logic: "T1 $63.30 = entry $58.92 + 1.5x R (R=$2.92); T2 $67.68 = entry + 3x R; structure ceiling = 52w high $64.58"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $66.0M; pass"
invalidation: "loses EMA20 $58.92 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
