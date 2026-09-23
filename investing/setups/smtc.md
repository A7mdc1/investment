---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $156.61 holding the uptrend (no breakdown on volume)"
entry_price: 156.61
stop_price: 155.99
stop_logic: "chandelier trail: HH22 $190.64 - 3x ATR $11.55 = $155.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 157.55
target_logic: "T1 $157.55 = entry $156.61 + 1.5x R (R=$0.62); T2 $158.49 = entry + 3x R; structure ceiling = 52w high $190.54"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $590.8M; pass"
invalidation: "loses EMA20 $156.61 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
