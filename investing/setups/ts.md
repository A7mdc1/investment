---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $57.79 holding the uptrend (no breakdown on volume)"
entry_price: 57.79
stop_price: 56.88
stop_logic: "chandelier trail: HH22 $62.22 - 3x ATR $1.78 = $56.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.15
target_logic: "T1 $59.15 = entry $57.79 + 1.5x R (R=$0.90); T2 $60.50 = entry + 3x R; structure ceiling = 52w high $64.60"
holding_window_days: 21
catalyst: "2027-02-17 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $64.0M; pass"
invalidation: "loses EMA20 $57.79 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
