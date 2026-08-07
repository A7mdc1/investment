---
ticker: AA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $47.34 holding the uptrend (no breakdown on volume)"
entry_price: 47.34
stop_price: 45.22
stop_logic: "chandelier trail: HH22 $50.86 - 3x ATR $1.88 = $45.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 50.53
target_logic: "T1 $50.53 = entry $47.34 + 1.5x R (R=$2.13); T2 $53.72 = entry + 3x R; structure ceiling = 52w high $84.39"
holding_window_days: 21
catalyst: "2026-10-15 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $232.7M; pass"
invalidation: "loses EMA20 $47.34 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
