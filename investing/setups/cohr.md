---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $215.77 holding the uptrend (no breakdown on volume)"
entry_price: 215.77
stop_price: 172.75
stop_logic: "chandelier trail: HH22 $246.90 - 3x ATR $24.72 = $172.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 280.30
target_logic: "T1 $280.30 = entry $215.77 + 1.5x R (R=$43.02); T2 $344.83 = entry + 3x R; structure ceiling = 52w high $439.65"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2182.9M; pass"
invalidation: "loses EMA20 $215.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
