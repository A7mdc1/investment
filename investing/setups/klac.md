---
ticker: KLAC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $157.09 holding the uptrend (no breakdown on volume)"
entry_price: 157.09
stop_price: 146.95
stop_logic: "chandelier trail: HH22 $175.43 - 3x ATR $9.49 = $146.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 172.31
target_logic: "T1 $172.31 = entry $157.09 + 1.5x R (R=$10.15); T2 $187.53 = entry + 3x R; structure ceiling = 52w high $307.18"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2167.4M; pass"
invalidation: "loses EMA20 $157.09 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
