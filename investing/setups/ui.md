---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $636.42 holding the uptrend (no breakdown on volume)"
entry_price: 636.42
stop_price: 603.51
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $31.65 = $603.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 685.80
target_logic: "T1 $685.80 = entry $636.42 + 1.5x R (R=$32.92); T2 $735.18 = entry + 3x R; structure ceiling = 52w high $1095.06"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $55.0M; pass"
invalidation: "loses EMA20 $636.42 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
