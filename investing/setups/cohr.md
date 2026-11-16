---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $224.22 holding the uptrend (no breakdown on volume)"
entry_price: 224.22
stop_price: 182.71
stop_logic: "chandelier trail: HH22 $248.58 - 3x ATR $21.96 = $182.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 286.48
target_logic: "T1 $286.48 = entry $224.22 + 1.5x R (R=$41.51); T2 $348.74 = entry + 3x R; structure ceiling = 52w high $440.34"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2025.1M; pass"
invalidation: "loses EMA20 $224.22 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
