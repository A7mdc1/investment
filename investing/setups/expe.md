---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $317.00 holding the uptrend (no breakdown on volume)"
entry_price: 317.00
stop_price: 301.97
stop_logic: "chandelier trail: HH22 $341.51 - 3x ATR $13.18 = $301.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 339.55
target_logic: "T1 $339.55 = entry $317.00 + 1.5x R (R=$15.03); T2 $362.10 = entry + 3x R; structure ceiling = 52w high $341.46"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $496.9M; pass"
invalidation: "loses EMA20 $317.00 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
