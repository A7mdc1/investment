---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $70.81 ahead of the 2026-11-25 print"
entry_price: 70.81
stop_price: 69.51
stop_logic: "chandelier trail: HH22 $75.98 - 3x ATR $2.16 = $69.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 72.76
target_logic: "T1 $72.76 = entry $70.81 + 1.5x R (R=$1.30); T2 $74.71 = entry + 3x R; structure ceiling = 52w high $75.98"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $168.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.16)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
