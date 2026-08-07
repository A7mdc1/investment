---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $842.98 holding the uptrend (no breakdown on volume)"
entry_price: 842.98
stop_price: 697.80
stop_logic: "chandelier trail: HH22 $937.54 - 3x ATR $79.91 = $697.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 1060.75
target_logic: "T1 $1060.75 = entry $842.98 + 1.5x R (R=$145.18); T2 $1278.51 = entry + 3x R; structure ceiling = 52w high $1144.98"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4648.4M; pass"
invalidation: "loses EMA20 $842.98 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
