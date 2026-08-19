---
ticker: DOCN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $126.90 holding the uptrend (no breakdown on volume)"
entry_price: 126.90
stop_price: 109.11
stop_logic: "chandelier trail: HH22 $144.52 - 3x ATR $11.80 = $109.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 153.59
target_logic: "T1 $153.59 = entry $126.90 + 1.5x R (R=$17.79); T2 $180.28 = entry + 3x R; structure ceiling = 52w high $187.61"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $385.3M; pass"
invalidation: "loses EMA20 $126.90 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
