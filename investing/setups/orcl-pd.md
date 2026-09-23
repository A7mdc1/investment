---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $46.71 holding the uptrend (no breakdown on volume)"
entry_price: 46.71
stop_price: 46.13
stop_logic: "chandelier trail: HH22 $51.31 - 3x ATR $1.72 = $46.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.57
target_logic: "T1 $47.57 = entry $46.71 + 1.5x R (R=$0.57); T2 $48.43 = entry + 3x R; structure ceiling = 52w high $69.27"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $38.6M; pass"
invalidation: "loses EMA20 $46.71 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
