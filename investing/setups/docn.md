---
ticker: DOCN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $127.53 holding the uptrend (no breakdown on volume)"
entry_price: 127.53
stop_price: 110.25
stop_logic: "chandelier trail: HH22 $144.52 - 3x ATR $11.42 = $110.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 153.45
target_logic: "T1 $153.45 = entry $127.53 + 1.5x R (R=$17.28); T2 $179.37 = entry + 3x R; structure ceiling = 52w high $187.47"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $431.1M; pass"
invalidation: "loses EMA20 $127.53 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
