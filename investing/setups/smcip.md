---
ticker: SMCIP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $58.06 holding the uptrend (no breakdown on volume)"
entry_price: 58.06
stop_price: 60.09
stop_logic: "chandelier trail: HH22 $70.21 - 3x ATR $3.37 = $60.09 — exit when decline exceeds ~3 average daily ranges"
target_price: null
target_logic: null           # scaffold: target unavailable (needs entry>stop for R)
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $40.0M; pass"
invalidation: "loses EMA20 $58.06 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
