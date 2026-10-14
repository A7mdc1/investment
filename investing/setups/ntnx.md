---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $70.84 ahead of the 2026-11-25 print"
entry_price: 70.84
stop_price: 70.22
stop_logic: "chandelier trail: HH22 $75.98 - 3x ATR $1.92 = $70.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 71.78
target_logic: "T1 $71.78 = entry $70.84 + 1.5x R (R=$0.62); T2 $72.71 = entry + 3x R; structure ceiling = 52w high $76.01"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $179.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.92)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
