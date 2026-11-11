---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $357.29 holding the uptrend (no breakdown on volume)"
entry_price: 357.29
stop_price: 356.03
stop_logic: "chandelier trail: HH22 $449.27 - 3x ATR $31.08 = $356.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 359.18
target_logic: "T1 $359.18 = entry $357.29 + 1.5x R (R=$1.26); T2 $361.07 = entry + 3x R; structure ceiling = 52w high $748.67"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $406.6M; pass"
invalidation: "loses EMA20 $357.29 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
