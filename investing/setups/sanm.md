---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $153.64 holding the uptrend (no breakdown on volume)"
entry_price: 153.64
stop_price: 136.53
stop_logic: "chandelier trail: HH22 $177.19 - 3x ATR $13.55 = $136.53 — exit when decline exceeds ~3 average daily ranges"
target_price: 179.31
target_logic: "T1 $179.31 = entry $153.64 + 1.5x R (R=$17.11); T2 $204.98 = entry + 3x R; structure ceiling = 52w high $288.42"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $177.2M; pass"
invalidation: "loses EMA20 $153.64 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
