---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $259.14 holding the uptrend (no breakdown on volume)"
entry_price: 259.14
stop_price: 247.78
stop_logic: "chandelier trail: HH22 $272.47 - 3x ATR $8.23 = $247.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 276.18
target_logic: "T1 $276.18 = entry $259.14 + 1.5x R (R=$11.36); T2 $293.22 = entry + 3x R; structure ceiling = 52w high $282.25"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $138.4M; pass"
invalidation: "loses EMA20 $259.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
