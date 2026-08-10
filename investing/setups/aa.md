---
ticker: AA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $47.76 holding the uptrend (no breakdown on volume)"
entry_price: 47.76
stop_price: 46.10
stop_logic: "chandelier trail: HH22 $51.76 - 3x ATR $1.89 = $46.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 50.26
target_logic: "T1 $50.26 = entry $47.76 + 1.5x R (R=$1.66); T2 $52.75 = entry + 3x R; structure ceiling = 52w high $84.35"
holding_window_days: 21
catalyst: "2026-10-15 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $236.1M; pass"
invalidation: "loses EMA20 $47.76 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
