---
ticker: YUMC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $46.50 holding the uptrend (no breakdown on volume)"
entry_price: 46.50
stop_price: 45.88
stop_logic: "chandelier trail: HH22 $49.11 - 3x ATR $1.08 = $45.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.44
target_logic: "T1 $47.44 = entry $46.50 + 1.5x R (R=$0.63); T2 $48.38 = entry + 3x R; structure ceiling = 52w high $57.68"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $73.8M; pass"
invalidation: "loses EMA20 $46.50 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
