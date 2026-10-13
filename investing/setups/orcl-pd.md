---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $44.22 holding the uptrend (no breakdown on volume)"
entry_price: 44.22
stop_price: 42.90
stop_logic: "chandelier trail: HH22 $47.61 - 3x ATR $1.57 = $42.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 46.20
target_logic: "T1 $46.20 = entry $44.22 + 1.5x R (R=$1.32); T2 $48.18 = entry + 3x R; structure ceiling = 52w high $67.95"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $29.5M; pass"
invalidation: "loses EMA20 $44.22 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
