---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $290.42 holding the uptrend (no breakdown on volume)"
entry_price: 290.42
stop_price: 287.07
stop_logic: "chandelier trail: HH22 $340.43 - 3x ATR $17.79 = $287.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 295.44
target_logic: "T1 $295.44 = entry $290.42 + 1.5x R (R=$3.35); T2 $300.46 = entry + 3x R; structure ceiling = 52w high $389.85"
holding_window_days: 21
catalyst: "2027-02-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $499.5M; pass"
invalidation: "loses EMA20 $290.42 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
