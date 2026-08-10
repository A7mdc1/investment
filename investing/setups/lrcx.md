---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $310.97 holding the uptrend (no breakdown on volume)"
entry_price: 310.97
stop_price: 286.54
stop_logic: "chandelier trail: HH22 $357.25 - 3x ATR $23.57 = $286.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 347.62
target_logic: "T1 $347.62 = entry $310.97 + 1.5x R (R=$24.43); T2 $384.26 = entry + 3x R; structure ceiling = 52w high $438.34"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3365.6M; pass"
invalidation: "loses EMA20 $310.97 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
