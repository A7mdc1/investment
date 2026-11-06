---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $169.44 holding the uptrend (no breakdown on volume)"
entry_price: 169.44
stop_price: 165.47
stop_logic: "chandelier trail: HH22 $179.83 - 3x ATR $4.79 = $165.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 175.40
target_logic: "T1 $175.40 = entry $169.44 + 1.5x R (R=$3.97); T2 $181.36 = entry + 3x R; structure ceiling = 52w high $235.68"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $292.6M; pass"
invalidation: "loses EMA20 $169.44 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
