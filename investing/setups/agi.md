---
ticker: AGI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $31.34 holding the uptrend (no breakdown on volume)"
entry_price: 31.34
stop_price: 30.74
stop_logic: "chandelier trail: HH22 $34.49 - 3x ATR $1.25 = $30.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.24
target_logic: "T1 $32.24 = entry $31.34 + 1.5x R (R=$0.60); T2 $33.13 = entry + 3x R; structure ceiling = 52w high $55.32"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $147.3M; pass"
invalidation: "loses EMA20 $31.34 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
