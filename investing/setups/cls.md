---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $337.42 holding the uptrend (no breakdown on volume)"
entry_price: 337.42
stop_price: 299.39
stop_logic: "chandelier trail: HH22 $378.00 - 3x ATR $26.20 = $299.39 — exit when decline exceeds ~3 average daily ranges"
target_price: 394.47
target_logic: "T1 $394.47 = entry $337.42 + 1.5x R (R=$38.03); T2 $451.52 = entry + 3x R; structure ceiling = 52w high $474.16"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $861.5M; pass"
invalidation: "loses EMA20 $337.42 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
