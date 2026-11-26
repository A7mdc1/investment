---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $56.53 holding the uptrend (no breakdown on volume)"
entry_price: 56.53
stop_price: 55.71
stop_logic: "chandelier trail: HH22 $60.88 - 3x ATR $1.72 = $55.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 57.76
target_logic: "T1 $57.76 = entry $56.53 + 1.5x R (R=$0.82); T2 $58.98 = entry + 3x R; structure ceiling = 52w high $63.21"
holding_window_days: 21
catalyst: "2027-02-17 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $63.4M; pass"
invalidation: "loses EMA20 $56.53 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
