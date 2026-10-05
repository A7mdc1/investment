---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $307.04 holding the uptrend (no breakdown on volume)"
entry_price: 307.04
stop_price: 293.24
stop_logic: "chandelier trail: HH22 $331.58 - 3x ATR $12.78 = $293.24 — exit when decline exceeds ~3 average daily ranges"
target_price: 327.74
target_logic: "T1 $327.74 = entry $307.04 + 1.5x R (R=$13.80); T2 $348.45 = entry + 3x R; structure ceiling = 52w high $428.98"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $444.8M; pass"
invalidation: "loses EMA20 $307.04 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
