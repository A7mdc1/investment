---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $500.50 holding the uptrend (no breakdown on volume)"
entry_price: 500.50
stop_price: 437.41
stop_logic: "chandelier trail: HH22 $580.00 - 3x ATR $47.53 = $437.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 595.15
target_logic: "T1 $595.15 = entry $500.50 + 1.5x R (R=$63.10); T2 $689.79 = entry + 3x R; structure ceiling = 52w high $799.39"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4068.3M; pass"
invalidation: "loses EMA20 $500.50 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
