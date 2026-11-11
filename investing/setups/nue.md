---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $259.25 holding the uptrend (no breakdown on volume)"
entry_price: 259.25
stop_price: 257.44
stop_logic: "chandelier trail: HH22 $287.70 - 3x ATR $10.09 = $257.44 — exit when decline exceeds ~3 average daily ranges"
target_price: 261.97
target_logic: "T1 $261.97 = entry $259.25 + 1.5x R (R=$1.81); T2 $264.69 = entry + 3x R; structure ceiling = 52w high $287.83"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $405.5M; pass"
invalidation: "loses EMA20 $259.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
