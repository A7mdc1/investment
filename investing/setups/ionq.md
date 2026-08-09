---
ticker: IONQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $39.60 holding the uptrend (no breakdown on volume)"
entry_price: 39.60
stop_price: 37.49
stop_logic: "chandelier trail: HH22 $46.00 - 3x ATR $2.84 = $37.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 42.76
target_logic: "T1 $42.76 = entry $39.60 + 1.5x R (R=$2.11); T2 $45.92 = entry + 3x R; structure ceiling = 52w high $84.63"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $819.8M; pass"
invalidation: "loses EMA20 $39.60 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
