---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $108.50 holding the uptrend (no breakdown on volume)"
entry_price: 108.50
stop_price: 95.91
stop_logic: "chandelier trail: HH22 $123.18 - 3x ATR $9.09 = $95.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 127.39
target_logic: "T1 $127.39 = entry $108.50 + 1.5x R (R=$12.59); T2 $146.28 = entry + 3x R; structure ceiling = 52w high $157.04"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $315.4M; pass"
invalidation: "loses EMA20 $108.50 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
