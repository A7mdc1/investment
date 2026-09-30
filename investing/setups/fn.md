---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $416.54 ahead of the 2026-11-02 print"
entry_price: 416.54
stop_price: 376.28
stop_logic: "chandelier trail: HH22 $430.00 - 3x ATR $17.91 = $376.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 476.93
target_logic: "T1 $476.93 = entry $416.54 + 1.5x R (R=$40.26); T2 $537.32 = entry + 3x R; structure ceiling = 52w high $749.17"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $295.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($17.91)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
