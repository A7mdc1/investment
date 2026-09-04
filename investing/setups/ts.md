---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $54.97 holding the uptrend (no breakdown on volume)"
entry_price: 54.97
stop_price: 52.97
stop_logic: "chandelier trail: HH22 $56.86 - 3x ATR $1.30 = $52.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 57.97
target_logic: "T1 $57.97 = entry $54.97 + 1.5x R (R=$2.00); T2 $60.97 = entry + 3x R; structure ceiling = 52w high $64.60"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $79.7M; pass"
invalidation: "loses EMA20 $54.97 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
