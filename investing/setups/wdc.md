---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $524.92 holding the uptrend (no breakdown on volume)"
entry_price: 524.92
stop_price: 445.69
stop_logic: "chandelier trail: HH22 $601.50 - 3x ATR $51.94 = $445.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 643.76
target_logic: "T1 $643.76 = entry $524.92 + 1.5x R (R=$79.23); T2 $762.61 = entry + 3x R; structure ceiling = 52w high $800.45"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3972.4M; pass"
invalidation: "loses EMA20 $524.92 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
