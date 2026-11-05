---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $244.24 holding the uptrend (no breakdown on volume)"
entry_price: 244.24
stop_price: 240.25
stop_logic: "chandelier trail: HH22 $258.16 - 3x ATR $5.97 = $240.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 250.22
target_logic: "T1 $250.22 = entry $244.24 + 1.5x R (R=$3.98); T2 $256.19 = entry + 3x R; structure ceiling = 52w high $282.11"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $144.7M; pass"
invalidation: "loses EMA20 $244.24 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
