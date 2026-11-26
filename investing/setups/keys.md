---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $291.64 holding the uptrend (no breakdown on volume)"
entry_price: 291.64
stop_price: 287.20
stop_logic: "chandelier trail: HH22 $340.43 - 3x ATR $17.74 = $287.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 298.32
target_logic: "T1 $298.32 = entry $291.64 + 1.5x R (R=$4.45); T2 $304.99 = entry + 3x R; structure ceiling = 52w high $389.65"
holding_window_days: 21
catalyst: "2027-02-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $511.6M; pass"
invalidation: "loses EMA20 $291.64 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
