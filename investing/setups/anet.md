---
ticker: ANET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $185.28 holding the uptrend (no breakdown on volume)"
entry_price: 185.28
stop_price: 173.68
stop_logic: "chandelier trail: HH22 $212.15 - 3x ATR $12.83 = $173.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 202.69
target_logic: "T1 $202.69 = entry $185.28 + 1.5x R (R=$11.60); T2 $220.10 = entry + 3x R; structure ceiling = 52w high $217.40"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1575.7M; pass"
invalidation: "loses EMA20 $185.28 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
