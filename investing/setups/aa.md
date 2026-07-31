---
ticker: AA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $47.20 holding the uptrend (no breakdown on volume)"
entry_price: 47.20
stop_price: 44.43
stop_logic: "chandelier trail: HH22 $51.03 - 3x ATR $2.20 = $44.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 51.35
target_logic: "T1 $51.35 = entry $47.20 + 1.5x R (R=$2.77); T2 $55.51 = entry + 3x R; structure ceiling = 52w high $84.40"
holding_window_days: 21
catalyst: "2026-10-15 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $251.1M; pass"
invalidation: "loses EMA20 $47.20 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
