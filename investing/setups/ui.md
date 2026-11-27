---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $634.26 holding the uptrend (no breakdown on volume)"
entry_price: 634.26
stop_price: 579.04
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $39.81 = $579.04 — exit when decline exceeds ~3 average daily ranges"
target_price: 717.08
target_logic: "T1 $717.08 = entry $634.26 + 1.5x R (R=$55.22); T2 $799.91 = entry + 3x R; structure ceiling = 52w high $1094.75"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $60.0M; pass"
invalidation: "loses EMA20 $634.26 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
