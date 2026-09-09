---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $259.19 holding the uptrend (no breakdown on volume)"
entry_price: 259.19
stop_price: 247.65
stop_logic: "chandelier trail: HH22 $272.47 - 3x ATR $8.27 = $247.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 276.49
target_logic: "T1 $276.49 = entry $259.19 + 1.5x R (R=$11.54); T2 $293.80 = entry + 3x R; structure ceiling = 52w high $282.03"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $138.1M; pass"
invalidation: "loses EMA20 $259.19 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
