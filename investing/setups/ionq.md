---
ticker: IONQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $39.94 holding the uptrend (no breakdown on volume)"
entry_price: 39.94
stop_price: 36.86
stop_logic: "chandelier trail: HH22 $45.45 - 3x ATR $2.86 = $36.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 44.57
target_logic: "T1 $44.57 = entry $39.94 + 1.5x R (R=$3.08); T2 $49.20 = entry + 3x R; structure ceiling = 52w high $84.60"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $795.8M; pass"
invalidation: "loses EMA20 $39.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
