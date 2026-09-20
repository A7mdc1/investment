---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $46.72 holding the uptrend (no breakdown on volume)"
entry_price: 46.72
stop_price: 46.19
stop_logic: "chandelier trail: HH22 $51.30 - 3x ATR $1.71 = $46.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.51
target_logic: "T1 $47.51 = entry $46.72 + 1.5x R (R=$0.53); T2 $48.30 = entry + 3x R; structure ceiling = 52w high $69.18"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $39.0M; pass"
invalidation: "loses EMA20 $46.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
