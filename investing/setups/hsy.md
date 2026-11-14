---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $171.31 holding the uptrend (no breakdown on volume)"
entry_price: 171.31
stop_price: 164.15
stop_logic: "chandelier trail: HH22 $179.83 - 3x ATR $5.23 = $164.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 182.05
target_logic: "T1 $182.05 = entry $171.31 + 1.5x R (R=$7.16); T2 $192.79 = entry + 3x R; structure ceiling = 52w high $235.82"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $339.6M; pass"
invalidation: "loses EMA20 $171.31 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
