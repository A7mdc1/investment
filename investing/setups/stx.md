---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $849.05 holding the uptrend (no breakdown on volume)"
entry_price: 849.05
stop_price: 702.30
stop_logic: "chandelier trail: HH22 $936.49 - 3x ATR $78.06 = $702.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 1069.18
target_logic: "T1 $1069.18 = entry $849.05 + 1.5x R (R=$146.75); T2 $1289.31 = entry + 3x R; structure ceiling = 52w high $1143.59"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4572.8M; pass"
invalidation: "loses EMA20 $849.05 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
