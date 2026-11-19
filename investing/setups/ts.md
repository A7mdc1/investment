---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $58.90 holding the uptrend (no breakdown on volume)"
entry_price: 58.90
stop_price: 56.76
stop_logic: "chandelier trail: HH22 $62.22 - 3x ATR $1.82 = $56.76 — exit when decline exceeds ~3 average daily ranges"
target_price: 62.11
target_logic: "T1 $62.11 = entry $58.90 + 1.5x R (R=$2.14); T2 $65.32 = entry + 3x R; structure ceiling = 52w high $64.58"
holding_window_days: 21
catalyst: "2027-02-17 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $65.8M; pass"
invalidation: "loses EMA20 $58.90 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
