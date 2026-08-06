---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $848.59 holding the uptrend (no breakdown on volume)"
entry_price: 848.59
stop_price: 704.59
stop_logic: "chandelier trail: HH22 $937.54 - 3x ATR $77.65 = $704.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 1064.59
target_logic: "T1 $1064.59 = entry $848.59 + 1.5x R (R=$144.00); T2 $1280.59 = entry + 3x R; structure ceiling = 52w high $1144.26"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4572.2M; pass"
invalidation: "loses EMA20 $848.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
