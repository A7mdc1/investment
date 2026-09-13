---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $46.88 holding the uptrend (no breakdown on volume)"
entry_price: 46.88
stop_price: 46.01
stop_logic: "chandelier trail: HH22 $51.31 - 3x ATR $1.76 = $46.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 48.19
target_logic: "T1 $48.19 = entry $46.88 + 1.5x R (R=$0.87); T2 $49.50 = entry + 3x R; structure ceiling = 52w high $69.26"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $40.6M; pass"
invalidation: "loses EMA20 $46.88 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
