---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $226.22 holding the uptrend (no breakdown on volume)"
entry_price: 226.22
stop_price: 185.63
stop_logic: "chandelier trail: HH22 $252.28 - 3x ATR $22.22 = $185.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 287.11
target_logic: "T1 $287.11 = entry $226.22 + 1.5x R (R=$40.59); T2 $348.00 = entry + 3x R; structure ceiling = 52w high $439.82"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2059.9M; pass"
invalidation: "loses EMA20 $226.22 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
