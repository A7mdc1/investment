---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $418.71 ahead of the 2026-09-02 print"
entry_price: 418.71
stop_price: 385.69
stop_logic: "chandelier trail: HH22 $432.73 - 3x ATR $15.68 = $385.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 468.24
target_logic: "T1 $468.24 = entry $418.71 + 1.5x R (R=$33.02); T2 $517.77 = entry + 3x R; structure ceiling = 52w high $494.34"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $7038.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($15.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
