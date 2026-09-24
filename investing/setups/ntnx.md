---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $67.75 holding the uptrend (no breakdown on volume)"
entry_price: 67.75
stop_price: 67.70
stop_logic: "chandelier trail: HH22 $74.42 - 3x ATR $2.24 = $67.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 67.84
target_logic: "T1 $67.84 = entry $67.75 + 1.5x R (R=$0.06); T2 $67.92 = entry + 3x R; structure ceiling = 52w high $78.42"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $187.1M; pass"
invalidation: "loses EMA20 $67.75 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
