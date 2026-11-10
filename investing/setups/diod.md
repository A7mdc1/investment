---
ticker: DIOD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $84.08 holding the uptrend (no breakdown on volume)"
entry_price: 84.08
stop_price: 76.48
stop_logic: "chandelier trail: HH22 $93.72 - 3x ATR $5.75 = $76.48 — exit when decline exceeds ~3 average daily ranges"
target_price: 95.49
target_logic: "T1 $95.49 = entry $84.08 + 1.5x R (R=$7.60); T2 $106.89 = entry + 3x R; structure ceiling = 52w high $125.99"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $45.9M; pass"
invalidation: "loses EMA20 $84.08 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
