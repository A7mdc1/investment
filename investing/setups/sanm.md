---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $158.76 holding the uptrend (no breakdown on volume)"
entry_price: 158.76
stop_price: 137.86
stop_logic: "chandelier trail: HH22 $177.19 - 3x ATR $13.11 = $137.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 190.10
target_logic: "T1 $190.10 = entry $158.76 + 1.5x R (R=$20.90); T2 $221.45 = entry + 3x R; structure ceiling = 52w high $288.76"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $178.6M; pass"
invalidation: "loses EMA20 $158.76 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
