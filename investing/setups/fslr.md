---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $215.49 holding the uptrend (no breakdown on volume)"
entry_price: 215.49
stop_price: 211.45
stop_logic: "chandelier trail: HH22 $241.00 - 3x ATR $9.85 = $211.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 221.55
target_logic: "T1 $221.55 = entry $215.49 + 1.5x R (R=$4.04); T2 $227.61 = entry + 3x R; structure ceiling = 52w high $321.17"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $380.7M; pass"
invalidation: "loses EMA20 $215.49 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
