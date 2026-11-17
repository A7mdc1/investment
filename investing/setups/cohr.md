---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $222.45 holding the uptrend (no breakdown on volume)"
entry_price: 222.45
stop_price: 181.35
stop_logic: "chandelier trail: HH22 $246.90 - 3x ATR $21.85 = $181.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 284.09
target_logic: "T1 $284.09 = entry $222.45 + 1.5x R (R=$41.10); T2 $345.74 = entry + 3x R; structure ceiling = 52w high $439.92"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2055.1M; pass"
invalidation: "loses EMA20 $222.45 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
