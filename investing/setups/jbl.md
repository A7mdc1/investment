---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $305.64 holding the uptrend (no breakdown on volume)"
entry_price: 305.64
stop_price: 291.74
stop_logic: "chandelier trail: HH22 $331.58 - 3x ATR $13.28 = $291.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 326.50
target_logic: "T1 $326.50 = entry $305.64 + 1.5x R (R=$13.91); T2 $347.36 = entry + 3x R; structure ceiling = 52w high $428.96"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $480.3M; pass"
invalidation: "loses EMA20 $305.64 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
