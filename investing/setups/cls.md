---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $336.33 holding the uptrend (no breakdown on volume)"
entry_price: 336.33
stop_price: 303.46
stop_logic: "chandelier trail: HH22 $378.00 - 3x ATR $24.85 = $303.46 — exit when decline exceeds ~3 average daily ranges"
target_price: 385.63
target_logic: "T1 $385.63 = entry $336.33 + 1.5x R (R=$32.87); T2 $434.93 = entry + 3x R; structure ceiling = 52w high $474.34"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $763.5M; pass"
invalidation: "loses EMA20 $336.33 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
