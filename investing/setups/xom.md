---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $154.25 holding the uptrend (no breakdown on volume)"
entry_price: 154.25
stop_price: 150.32
stop_logic: "chandelier trail: HH22 $161.67 - 3x ATR $3.78 = $150.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 160.13
target_logic: "T1 $160.13 = entry $154.25 + 1.5x R (R=$3.92); T2 $166.02 = entry + 3x R; structure ceiling = 52w high $175.18"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2177.9M; pass"
invalidation: "loses EMA20 $154.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
