---
ticker: PAAS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $49.66 holding the uptrend (no breakdown on volume)"
entry_price: 49.66
stop_price: 47.70
stop_logic: "chandelier trail: HH22 $54.21 - 3x ATR $2.17 = $47.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.60
target_logic: "T1 $52.60 = entry $49.66 + 1.5x R (R=$1.96); T2 $55.53 = entry + 3x R; structure ceiling = 52w high $69.32"
holding_window_days: 21
catalyst: "2026-11-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $254.0M; pass"
invalidation: "loses EMA20 $49.66 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
