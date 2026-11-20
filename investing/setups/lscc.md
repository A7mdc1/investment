---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $108.91 holding the uptrend (no breakdown on volume)"
entry_price: 108.91
stop_price: 98.17
stop_logic: "chandelier trail: HH22 $123.18 - 3x ATR $8.34 = $98.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 125.03
target_logic: "T1 $125.03 = entry $108.91 + 1.5x R (R=$10.74); T2 $141.14 = entry + 3x R; structure ceiling = 52w high $157.00"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $303.1M; pass"
invalidation: "loses EMA20 $108.91 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
