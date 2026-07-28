---
ticker: NEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $94.38 holding the uptrend (no breakdown on volume)"
entry_price: 94.38
stop_price: 89.35
stop_logic: "chandelier trail: HH22 $98.93 - 3x ATR $3.19 = $89.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.93
target_logic: "T1 $101.93 = entry $94.38 + 1.5x R (R=$5.03); T2 $109.47 = entry + 3x R; structure ceiling = 52w high $134.28"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $685.2M; pass"
invalidation: "loses EMA20 $94.38 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
