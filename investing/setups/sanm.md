---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $161.55 holding the uptrend (no breakdown on volume)"
entry_price: 161.55
stop_price: 146.54
stop_logic: "chandelier trail: HH22 $183.50 - 3x ATR $12.32 = $146.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 184.06
target_logic: "T1 $184.06 = entry $161.55 + 1.5x R (R=$15.01); T2 $206.57 = entry + 3x R; structure ceiling = 52w high $288.56"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $173.3M; pass"
invalidation: "loses EMA20 $161.55 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
