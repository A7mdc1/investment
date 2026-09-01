---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $18.38 holding the uptrend (no breakdown on volume)"
entry_price: 18.38
stop_price: 17.63
stop_logic: "chandelier trail: HH22 $19.73 - 3x ATR $0.70 = $17.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 19.50
target_logic: "T1 $19.50 = entry $18.38 + 1.5x R (R=$0.75); T2 $20.62 = entry + 3x R; structure ceiling = 52w high $19.73"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $34.5M; pass"
invalidation: "loses EMA20 $18.38 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
