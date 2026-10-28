---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $56.32 holding the uptrend (no breakdown on volume)"
entry_price: 56.32
stop_price: 53.69
stop_logic: "chandelier trail: HH22 $59.09 - 3x ATR $1.80 = $53.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.26
target_logic: "T1 $60.26 = entry $56.32 + 1.5x R (R=$2.63); T2 $64.21 = entry + 3x R; structure ceiling = 52w high $69.90"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $356.9M; pass"
invalidation: "loses EMA20 $56.32 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
