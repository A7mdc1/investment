---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $318.77 holding the uptrend (no breakdown on volume)"
entry_price: 318.77
stop_price: 280.11
stop_logic: "chandelier trail: HH22 $345.28 - 3x ATR $21.72 = $280.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 376.76
target_logic: "T1 $376.76 = entry $318.77 + 1.5x R (R=$38.66); T2 $434.75 = entry + 3x R; structure ceiling = 52w high $438.64"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3193.1M; pass"
invalidation: "loses EMA20 $318.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
