---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $245.26 holding the uptrend (no breakdown on volume)"
entry_price: 245.26
stop_price: 240.11
stop_logic: "chandelier trail: HH22 $258.16 - 3x ATR $6.02 = $240.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 252.99
target_logic: "T1 $252.99 = entry $245.26 + 1.5x R (R=$5.15); T2 $260.71 = entry + 3x R; structure ceiling = 52w high $282.15"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $143.7M; pass"
invalidation: "loses EMA20 $245.26 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
