---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $527.30 holding the uptrend (no breakdown on volume)"
entry_price: 527.30
stop_price: 501.68
stop_logic: "chandelier trail: HH22 $543.56 - 3x ATR $13.96 = $501.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 565.73
target_logic: "T1 $565.73 = entry $527.30 + 1.5x R (R=$25.62); T2 $604.17 = entry + 3x R; structure ceiling = 52w high $609.04"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $266.8M; pass"
invalidation: "loses EMA20 $527.30 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
