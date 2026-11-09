---
ticker: HL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $14.93 holding the uptrend (no breakdown on volume)"
entry_price: 14.93
stop_price: 14.90
stop_logic: "chandelier trail: HH22 $17.38 - 3x ATR $0.83 = $14.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 14.98
target_logic: "T1 $14.98 = entry $14.93 + 1.5x R (R=$0.03); T2 $15.04 = entry + 3x R; structure ceiling = 52w high $34.15"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $427.6M; pass"
invalidation: "loses EMA20 $14.93 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
