---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $256.88 holding the uptrend (no breakdown on volume)"
entry_price: 256.88
stop_price: 243.58
stop_logic: "chandelier trail: HH22 $292.72 - 3x ATR $16.38 = $243.58 — exit when decline exceeds ~3 average daily ranges"
target_price: 276.83
target_logic: "T1 $276.83 = entry $256.88 + 1.5x R (R=$13.30); T2 $296.78 = entry + 3x R; structure ceiling = 52w high $292.85"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1245.2M; pass"
invalidation: "loses EMA20 $256.88 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
