---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $26.70 ahead of the 2026-10-29 print"
entry_price: 26.70
stop_price: 26.60
stop_logic: "chandelier trail: HH22 $30.56 - 3x ATR $1.32 = $26.60 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.85
target_logic: "T1 $26.85 = entry $26.70 + 1.5x R (R=$0.10); T2 $27.00 = entry + 3x R; structure ceiling = 52w high $32.13"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $100.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
