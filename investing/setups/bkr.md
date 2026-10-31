---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $55.99 holding the uptrend (no breakdown on volume)"
entry_price: 55.99
stop_price: 53.70
stop_logic: "chandelier trail: HH22 $59.09 - 3x ATR $1.79 = $53.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.41
target_logic: "T1 $59.41 = entry $55.99 + 1.5x R (R=$2.28); T2 $62.83 = entry + 3x R; structure ceiling = 52w high $69.91"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $403.9M; pass"
invalidation: "loses EMA20 $55.99 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
