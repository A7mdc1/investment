---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $290.33 holding the uptrend (no breakdown on volume)"
entry_price: 290.33
stop_price: 283.62
stop_logic: "chandelier trail: HH22 $313.07 - 3x ATR $9.82 = $283.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 300.39
target_logic: "T1 $300.39 = entry $290.33 + 1.5x R (R=$6.71); T2 $310.46 = entry + 3x R; structure ceiling = 52w high $332.49"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1946.8M; pass"
invalidation: "loses EMA20 $290.33 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
