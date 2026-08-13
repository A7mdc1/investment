---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $337.08 holding the uptrend (no breakdown on volume)"
entry_price: 337.08
stop_price: 295.67
stop_logic: "chandelier trail: HH22 $378.99 - 3x ATR $27.77 = $295.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 399.19
target_logic: "T1 $399.19 = entry $337.08 + 1.5x R (R=$41.41); T2 $461.31 = entry + 3x R; structure ceiling = 52w high $473.88"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1096.9M; pass"
invalidation: "loses EMA20 $337.08 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
