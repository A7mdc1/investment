---
ticker: VIAV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $32.59 holding the uptrend (no breakdown on volume)"
entry_price: 32.59
stop_price: 32.37
stop_logic: "chandelier trail: HH22 $41.49 - 3x ATR $3.04 = $32.37 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.91
target_logic: "T1 $32.91 = entry $32.59 + 1.5x R (R=$0.21); T2 $33.23 = entry + 3x R; structure ceiling = 52w high $60.45"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $213.7M; pass"
invalidation: "loses EMA20 $32.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
