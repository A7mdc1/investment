---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $257.71 holding the uptrend (no breakdown on volume)"
entry_price: 257.71
stop_price: 256.38
stop_logic: "chandelier trail: HH22 $278.56 - 3x ATR $7.39 = $256.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 259.72
target_logic: "T1 $259.72 = entry $257.71 + 1.5x R (R=$1.34); T2 $261.73 = entry + 3x R; structure ceiling = 52w high $282.29"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $179.7M; pass"
invalidation: "loses EMA20 $257.71 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
