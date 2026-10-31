---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $42.21 holding the uptrend (no breakdown on volume)"
entry_price: 42.21
stop_price: 40.40
stop_logic: "chandelier trail: HH22 $45.35 - 3x ATR $1.65 = $40.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 44.93
target_logic: "T1 $44.93 = entry $42.21 + 1.5x R (R=$1.81); T2 $47.65 = entry + 3x R; structure ceiling = 52w high $67.96"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $23.0M; pass"
invalidation: "loses EMA20 $42.21 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
