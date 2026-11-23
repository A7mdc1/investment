---
ticker: VIAV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $30.85 holding the uptrend (no breakdown on volume)"
entry_price: 30.85
stop_price: 25.78
stop_logic: "chandelier trail: HH22 $34.46 - 3x ATR $2.89 = $25.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 38.45
target_logic: "T1 $38.45 = entry $30.85 + 1.5x R (R=$5.07); T2 $46.05 = entry + 3x R; structure ceiling = 52w high $60.40"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $204.2M; pass"
invalidation: "loses EMA20 $30.85 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
