---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $338.36 holding the uptrend (no breakdown on volume)"
entry_price: 338.36
stop_price: 300.33
stop_logic: "chandelier trail: HH22 $378.00 - 3x ATR $25.89 = $300.33 — exit when decline exceeds ~3 average daily ranges"
target_price: 395.40
target_logic: "T1 $395.40 = entry $338.36 + 1.5x R (R=$38.03); T2 $452.45 = entry + 3x R; structure ceiling = 52w high $473.94"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $828.3M; pass"
invalidation: "loses EMA20 $338.36 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
