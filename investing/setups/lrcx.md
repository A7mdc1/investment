---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $312.05 holding the uptrend (no breakdown on volume)"
entry_price: 312.05
stop_price: 294.17
stop_logic: "chandelier trail: HH22 $369.95 - 3x ATR $25.26 = $294.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 338.88
target_logic: "T1 $338.88 = entry $312.05 + 1.5x R (R=$17.88); T2 $365.71 = entry + 3x R; structure ceiling = 52w high $438.30"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3422.3M; pass"
invalidation: "loses EMA20 $312.05 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
