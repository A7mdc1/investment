---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $608.08 holding the uptrend (no breakdown on volume)"
entry_price: 608.08
stop_price: 603.79
stop_logic: "chandelier trail: HH22 $698.54 - 3x ATR $31.58 = $603.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 614.53
target_logic: "T1 $614.53 = entry $608.08 + 1.5x R (R=$4.30); T2 $620.98 = entry + 3x R; structure ceiling = 52w high $1097.20"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $53.6M; pass"
invalidation: "loses EMA20 $608.08 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
