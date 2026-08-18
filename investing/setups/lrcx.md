---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $319.28 holding the uptrend (no breakdown on volume)"
entry_price: 319.28
stop_price: 280.40
stop_logic: "chandelier trail: HH22 $345.28 - 3x ATR $21.63 = $280.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 377.62
target_logic: "T1 $377.62 = entry $319.28 + 1.5x R (R=$38.89); T2 $435.95 = entry + 3x R; structure ceiling = 52w high $438.48"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3113.9M; pass"
invalidation: "loses EMA20 $319.28 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
