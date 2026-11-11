---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $108.23 holding the uptrend (no breakdown on volume)"
entry_price: 108.23
stop_price: 98.75
stop_logic: "chandelier trail: HH22 $121.77 - 3x ATR $7.67 = $98.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 122.45
target_logic: "T1 $122.45 = entry $108.23 + 1.5x R (R=$9.48); T2 $136.67 = entry + 3x R; structure ceiling = 52w high $156.91"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $294.8M; pass"
invalidation: "loses EMA20 $108.23 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
