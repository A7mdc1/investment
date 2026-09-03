---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $18.44 holding the uptrend (no breakdown on volume)"
entry_price: 18.44
stop_price: 17.42
stop_logic: "chandelier trail: HH22 $19.73 - 3x ATR $0.77 = $17.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 19.97
target_logic: "T1 $19.97 = entry $18.44 + 1.5x R (R=$1.02); T2 $21.51 = entry + 3x R; structure ceiling = 52w high $19.74"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $29.6M; pass"
invalidation: "loses EMA20 $18.44 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
