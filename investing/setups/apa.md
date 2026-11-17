---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $47.25 holding the uptrend (no breakdown on volume)"
entry_price: 47.25
stop_price: 47.20
stop_logic: "chandelier trail: HH22 $52.96 - 3x ATR $1.92 = $47.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.32
target_logic: "T1 $47.32 = entry $47.25 + 1.5x R (R=$0.05); T2 $47.39 = entry + 3x R; structure ceiling = 52w high $52.95"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $273.3M; pass"
invalidation: "loses EMA20 $47.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
