---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $184.09 holding the uptrend (no breakdown on volume)"
entry_price: 184.09
stop_price: 177.61
stop_logic: "chandelier trail: HH22 $202.24 - 3x ATR $8.21 = $177.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 193.81
target_logic: "T1 $193.81 = entry $184.09 + 1.5x R (R=$6.48); T2 $203.53 = entry + 3x R; structure ceiling = 52w high $254.15"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $373.5M; pass"
invalidation: "loses EMA20 $184.09 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
