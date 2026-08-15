---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $21.30 holding the uptrend (no breakdown on volume)"
entry_price: 21.30
stop_price: 19.12
stop_logic: "chandelier trail: HH22 $24.66 - 3x ATR $1.85 = $19.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 24.58
target_logic: "T1 $24.58 = entry $21.30 + 1.5x R (R=$2.18); T2 $27.85 = entry + 3x R; structure ceiling = 52w high $30.44"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $295.9M; pass"
invalidation: "loses EMA20 $21.30 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
