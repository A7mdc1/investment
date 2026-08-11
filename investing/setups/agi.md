---
ticker: AGI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $30.68 holding the uptrend (no breakdown on volume)"
entry_price: 30.68
stop_price: 30.10
stop_logic: "chandelier trail: HH22 $33.82 - 3x ATR $1.24 = $30.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 31.55
target_logic: "T1 $31.55 = entry $30.68 + 1.5x R (R=$0.58); T2 $32.42 = entry + 3x R; structure ceiling = 52w high $55.29"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $148.1M; pass"
invalidation: "loses EMA20 $30.68 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
