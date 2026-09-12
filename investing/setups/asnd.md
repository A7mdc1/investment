---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $259.59 holding the uptrend (no breakdown on volume)"
entry_price: 259.59
stop_price: 247.68
stop_logic: "chandelier trail: HH22 $272.47 - 3x ATR $8.26 = $247.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 277.46
target_logic: "T1 $277.46 = entry $259.59 + 1.5x R (R=$11.91); T2 $295.32 = entry + 3x R; structure ceiling = 52w high $282.14"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $135.6M; pass"
invalidation: "loses EMA20 $259.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
