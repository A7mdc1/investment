---
ticker: VICR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $227.62 holding the uptrend (no breakdown on volume)"
entry_price: 227.62
stop_price: 213.13
stop_logic: "chandelier trail: HH22 $279.00 - 3x ATR $21.96 = $213.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 249.36
target_logic: "T1 $249.36 = entry $227.62 + 1.5x R (R=$14.49); T2 $271.10 = entry + 3x R; structure ceiling = 52w high $382.70"
holding_window_days: 21
catalyst: "2026-10-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $186.9M; pass"
invalidation: "loses EMA20 $227.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
