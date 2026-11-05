---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $262.79 holding the uptrend (no breakdown on volume)"
entry_price: 262.79
stop_price: 260.04
stop_logic: "chandelier trail: HH22 $287.70 - 3x ATR $9.22 = $260.04 — exit when decline exceeds ~3 average daily ranges"
target_price: 266.92
target_logic: "T1 $266.92 = entry $262.79 + 1.5x R (R=$2.75); T2 $271.05 = entry + 3x R; structure ceiling = 52w high $287.81"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $370.6M; pass"
invalidation: "loses EMA20 $262.79 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
