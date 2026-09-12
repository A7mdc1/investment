---
ticker: BLSH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $32.04 holding the uptrend (no breakdown on volume)"
entry_price: 32.04
stop_price: 30.78
stop_logic: "chandelier trail: HH22 $37.10 - 3x ATR $2.11 = $30.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 33.91
target_logic: "T1 $33.91 = entry $32.04 + 1.5x R (R=$1.25); T2 $35.79 = entry + 3x R; structure ceiling = 52w high $75.04"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $51.1M; pass"
invalidation: "loses EMA20 $32.04 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
