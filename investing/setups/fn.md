---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $524.24 holding the uptrend (no breakdown on volume)"
entry_price: 524.24
stop_price: 475.96
stop_logic: "chandelier trail: HH22 $603.09 - 3x ATR $42.38 = $475.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 596.66
target_logic: "T1 $596.66 = entry $524.24 + 1.5x R (R=$48.28); T2 $669.09 = entry + 3x R; structure ceiling = 52w high $749.46"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $423.4M; pass"
invalidation: "loses EMA20 $524.24 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
