---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $860.59 holding the uptrend (no breakdown on volume)"
entry_price: 860.59
stop_price: 760.97
stop_logic: "chandelier trail: HH22 $990.61 - 3x ATR $76.55 = $760.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 1010.02
target_logic: "T1 $1010.02 = entry $860.59 + 1.5x R (R=$99.62); T2 $1159.45 = entry + 3x R; structure ceiling = 52w high $1143.57"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4534.7M; pass"
invalidation: "loses EMA20 $860.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
