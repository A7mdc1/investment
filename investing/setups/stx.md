---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $849.39 holding the uptrend (no breakdown on volume)"
entry_price: 849.39
stop_price: 694.83
stop_logic: "chandelier trail: HH22 $937.54 - 3x ATR $80.90 = $694.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 1081.22
target_logic: "T1 $1081.22 = entry $849.39 + 1.5x R (R=$154.56); T2 $1313.06 = entry + 3x R; structure ceiling = 52w high $1144.56"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4559.1M; pass"
invalidation: "loses EMA20 $849.39 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
