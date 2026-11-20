---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $172.12 holding the uptrend (no breakdown on volume)"
entry_price: 172.12
stop_price: 163.49
stop_logic: "chandelier trail: HH22 $180.19 - 3x ATR $5.57 = $163.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 185.06
target_logic: "T1 $185.06 = entry $172.12 + 1.5x R (R=$8.63); T2 $198.00 = entry + 3x R; structure ceiling = 52w high $233.94"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $356.8M; pass"
invalidation: "loses EMA20 $172.12 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
