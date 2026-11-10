---
ticker: STLD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $238.45 holding the uptrend (no breakdown on volume)"
entry_price: 238.45
stop_price: 229.33
stop_logic: "chandelier trail: HH22 $259.24 - 3x ATR $9.97 = $229.33 — exit when decline exceeds ~3 average daily ranges"
target_price: 252.14
target_logic: "T1 $252.14 = entry $238.45 + 1.5x R (R=$9.12); T2 $265.82 = entry + 3x R; structure ceiling = 52w high $287.36"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $257.4M; pass"
invalidation: "loses EMA20 $238.45 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
