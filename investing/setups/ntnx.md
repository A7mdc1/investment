---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $67.69 holding the uptrend (no breakdown on volume)"
entry_price: 67.69
stop_price: 67.52
stop_logic: "chandelier trail: HH22 $74.42 - 3x ATR $2.30 = $67.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 67.94
target_logic: "T1 $67.94 = entry $67.69 + 1.5x R (R=$0.17); T2 $68.19 = entry + 3x R; structure ceiling = 52w high $78.44"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $190.1M; pass"
invalidation: "loses EMA20 $67.69 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
