---
ticker: FOX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $53.08 holding the uptrend (no breakdown on volume)"
entry_price: 53.08
stop_price: 52.73
stop_logic: "chandelier trail: HH22 $57.18 - 3x ATR $1.48 = $52.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 53.60
target_logic: "T1 $53.60 = entry $53.08 + 1.5x R (R=$0.35); T2 $54.12 = entry + 3x R; structure ceiling = 52w high $67.78"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $59.3M; pass"
invalidation: "loses EMA20 $53.08 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
