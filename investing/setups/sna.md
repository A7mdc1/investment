---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $364.66 holding the uptrend (no breakdown on volume)"
entry_price: 364.66
stop_price: 350.41
stop_logic: "chandelier trail: HH22 $374.86 - 3x ATR $8.15 = $350.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 386.05
target_logic: "T1 $386.05 = entry $364.66 + 1.5x R (R=$14.26); T2 $407.43 = entry + 3x R; structure ceiling = 52w high $420.39"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $168.6M; pass"
invalidation: "loses EMA20 $364.66 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
