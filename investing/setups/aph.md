---
ticker: APH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $163.62 holding the uptrend (no breakdown on volume)"
entry_price: 163.62
stop_price: 155.74
stop_logic: "chandelier trail: HH22 $176.33 - 3x ATR $6.86 = $155.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 175.43
target_logic: "T1 $175.43 = entry $163.62 + 1.5x R (R=$7.88); T2 $187.25 = entry + 3x R; structure ceiling = 52w high $178.54"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1068.5M; pass"
invalidation: "loses EMA20 $163.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
