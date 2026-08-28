---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1203.40 holding the uptrend (no breakdown on volume)"
entry_price: 1203.40
stop_price: 1165.45
stop_logic: "chandelier trail: HH22 $1292.65 - 3x ATR $42.40 = $1165.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 1260.33
target_logic: "T1 $1260.33 = entry $1203.40 + 1.5x R (R=$37.95); T2 $1317.26 = entry + 3x R; structure ceiling = 52w high $1292.92"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3322.3M; pass"
invalidation: "loses EMA20 $1203.40 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
