---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $26.71 ahead of the 2026-10-29 print"
entry_price: 26.71
stop_price: 26.68
stop_logic: "chandelier trail: HH22 $30.81 - 3x ATR $1.38 = $26.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.77
target_logic: "T1 $26.77 = entry $26.71 + 1.5x R (R=$0.04); T2 $26.83 = entry + 3x R; structure ceiling = 52w high $32.15"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $104.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
