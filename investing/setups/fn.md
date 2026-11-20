---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $335.41 holding the uptrend (no breakdown on volume)"
entry_price: 335.41
stop_price: 283.85
stop_logic: "chandelier trail: HH22 $379.43 - 3x ATR $31.86 = $283.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 412.74
target_logic: "T1 $412.74 = entry $335.41 + 1.5x R (R=$51.56); T2 $490.08 = entry + 3x R; structure ceiling = 52w high $748.53"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $398.8M; pass"
invalidation: "loses EMA20 $335.41 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
