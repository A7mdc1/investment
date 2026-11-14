---
ticker: AMAT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $390.41 holding the uptrend (no breakdown on volume)"
entry_price: 390.41
stop_price: 361.42
stop_logic: "chandelier trail: HH22 $434.56 - 3x ATR $24.38 = $361.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 433.90
target_logic: "T1 $433.90 = entry $390.41 + 1.5x R (R=$28.99); T2 $477.39 = entry + 3x R; structure ceiling = 52w high $739.52"
holding_window_days: 21
catalyst: "2027-02-11 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3210.8M; pass"
invalidation: "loses EMA20 $390.41 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
