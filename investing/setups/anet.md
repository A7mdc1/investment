---
ticker: ANET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $180.57 holding the uptrend (no breakdown on volume)"
entry_price: 180.57
stop_price: 171.22
stop_logic: "chandelier trail: HH22 $212.16 - 3x ATR $13.65 = $171.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 194.59
target_logic: "T1 $194.59 = entry $180.57 + 1.5x R (R=$9.35); T2 $208.62 = entry + 3x R; structure ceiling = 52w high $217.38"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1697.3M; pass"
invalidation: "loses EMA20 $180.57 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
