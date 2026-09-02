---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $54.64 holding the uptrend (no breakdown on volume)"
entry_price: 54.64
stop_price: 54.36
stop_logic: "chandelier trail: HH22 $58.47 - 3x ATR $1.37 = $54.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 55.06
target_logic: "T1 $55.06 = entry $54.64 + 1.5x R (R=$0.28); T2 $55.48 = entry + 3x R; structure ceiling = 52w high $64.61"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $91.2M; pass"
invalidation: "loses EMA20 $54.64 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
