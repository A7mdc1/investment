---
ticker: EVR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $286.91 holding the uptrend (no breakdown on volume)"
entry_price: 286.91
stop_price: 279.64
stop_logic: "chandelier trail: HH22 $315.00 - 3x ATR $11.79 = $279.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 297.82
target_logic: "T1 $297.82 = entry $286.91 + 1.5x R (R=$7.27); T2 $308.72 = entry + 3x R; structure ceiling = 52w high $385.76"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $140.9M; pass"
invalidation: "loses EMA20 $286.91 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
