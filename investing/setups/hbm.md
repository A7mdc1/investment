---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $27.84 ahead of the 2026-10-29 print"
entry_price: 27.84
stop_price: 27.03
stop_logic: "chandelier trail: HH22 $30.82 - 3x ATR $1.26 = $27.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 29.06
target_logic: "T1 $29.06 = entry $27.84 + 1.5x R (R=$0.81); T2 $30.28 = entry + 3x R; structure ceiling = 52w high $32.15"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $120.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.26)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
