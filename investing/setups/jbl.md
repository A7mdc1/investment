---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $305.32 holding the uptrend (no breakdown on volume)"
entry_price: 305.32
stop_price: 292.41
stop_logic: "chandelier trail: HH22 $331.58 - 3x ATR $13.06 = $292.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 324.68
target_logic: "T1 $324.68 = entry $305.32 + 1.5x R (R=$12.91); T2 $344.05 = entry + 3x R; structure ceiling = 52w high $428.99"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $461.6M; pass"
invalidation: "loses EMA20 $305.32 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
