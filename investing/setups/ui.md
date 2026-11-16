---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $624.00 holding the uptrend (no breakdown on volume)"
entry_price: 624.00
stop_price: 605.50
stop_logic: "chandelier trail: HH22 $699.50 - 3x ATR $31.33 = $605.50 — exit when decline exceeds ~3 average daily ranges"
target_price: 651.74
target_logic: "T1 $651.74 = entry $624.00 + 1.5x R (R=$18.49); T2 $679.48 = entry + 3x R; structure ceiling = 52w high $1096.82"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $53.2M; pass"
invalidation: "loses EMA20 $624.00 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
