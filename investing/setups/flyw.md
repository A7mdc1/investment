---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $17.25 holding the uptrend (no breakdown on volume)"
entry_price: 17.25
stop_price: 16.80
stop_logic: "chandelier trail: HH22 $18.98 - 3x ATR $0.73 = $16.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 17.93
target_logic: "T1 $17.93 = entry $17.25 + 1.5x R (R=$0.45); T2 $18.60 = entry + 3x R; structure ceiling = 52w high $18.98"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $39.3M; pass"
invalidation: "loses EMA20 $17.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
