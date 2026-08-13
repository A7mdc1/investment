---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $21.46 holding the uptrend (no breakdown on volume)"
entry_price: 21.46
stop_price: 19.10
stop_logic: "chandelier trail: HH22 $24.66 - 3x ATR $1.85 = $19.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.02
target_logic: "T1 $25.02 = entry $21.46 + 1.5x R (R=$2.37); T2 $28.57 = entry + 3x R; structure ceiling = 52w high $30.48"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $289.8M; pass"
invalidation: "loses EMA20 $21.46 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
