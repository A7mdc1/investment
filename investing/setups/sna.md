---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $364.62 holding the uptrend (no breakdown on volume)"
entry_price: 364.62
stop_price: 350.49
stop_logic: "chandelier trail: HH22 $378.04 - 3x ATR $9.18 = $350.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 385.81
target_logic: "T1 $385.81 = entry $364.62 + 1.5x R (R=$14.13); T2 $407.00 = entry + 3x R; structure ceiling = 52w high $420.62"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $160.4M; pass"
invalidation: "loses EMA20 $364.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
