---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $109.77 holding the uptrend (no breakdown on volume)"
entry_price: 109.77
stop_price: 99.77
stop_logic: "chandelier trail: HH22 $123.18 - 3x ATR $7.80 = $99.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 124.78
target_logic: "T1 $124.78 = entry $109.77 + 1.5x R (R=$10.01); T2 $139.79 = entry + 3x R; structure ceiling = 52w high $157.03"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $299.5M; pass"
invalidation: "loses EMA20 $109.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
