---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $306.19 holding the uptrend (no breakdown on volume)"
entry_price: 306.19
stop_price: 291.59
stop_logic: "chandelier trail: HH22 $331.58 - 3x ATR $13.33 = $291.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 328.10
target_logic: "T1 $328.10 = entry $306.19 + 1.5x R (R=$14.61); T2 $350.01 = entry + 3x R; structure ceiling = 52w high $428.92"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $476.8M; pass"
invalidation: "loses EMA20 $306.19 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
