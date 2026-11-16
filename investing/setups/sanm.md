---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $162.81 holding the uptrend (no breakdown on volume)"
entry_price: 162.81
stop_price: 149.55
stop_logic: "chandelier trail: HH22 $186.99 - 3x ATR $12.48 = $149.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 182.71
target_logic: "T1 $182.71 = entry $162.81 + 1.5x R (R=$13.26); T2 $202.60 = entry + 3x R; structure ceiling = 52w high $288.61"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $173.1M; pass"
invalidation: "loses EMA20 $162.81 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
