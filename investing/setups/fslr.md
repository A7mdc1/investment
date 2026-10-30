---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $176.85 holding the uptrend (no breakdown on volume)"
entry_price: 176.85
stop_price: 167.87
stop_logic: "chandelier trail: HH22 $187.85 - 3x ATR $6.66 = $167.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 190.32
target_logic: "T1 $190.32 = entry $176.85 + 1.5x R (R=$8.98); T2 $203.79 = entry + 3x R; structure ceiling = 52w high $320.97"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $345.7M; pass"
invalidation: "loses EMA20 $176.85 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
