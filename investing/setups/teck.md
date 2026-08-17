---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $63.07 holding the uptrend (no breakdown on volume)"
entry_price: 63.07
stop_price: 61.34
stop_logic: "chandelier trail: HH22 $68.10 - 3x ATR $2.25 = $61.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.66
target_logic: "T1 $65.66 = entry $63.07 + 1.5x R (R=$1.73); T2 $68.25 = entry + 3x R; structure ceiling = 52w high $71.18"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $190.6M; pass"
invalidation: "loses EMA20 $63.07 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
