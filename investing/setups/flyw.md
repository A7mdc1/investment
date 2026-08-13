---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $17.31 holding the uptrend (no breakdown on volume)"
entry_price: 17.31
stop_price: 16.79
stop_logic: "chandelier trail: HH22 $18.98 - 3x ATR $0.73 = $16.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 18.10
target_logic: "T1 $18.10 = entry $17.31 + 1.5x R (R=$0.52); T2 $18.88 = entry + 3x R; structure ceiling = 52w high $18.99"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $37.8M; pass"
invalidation: "loses EMA20 $17.31 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
