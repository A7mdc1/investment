---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $73.77 ahead of the 2026-11-25 print"
entry_price: 73.77
stop_price: 69.34
stop_logic: "chandelier trail: HH22 $75.98 - 3x ATR $2.21 = $69.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 80.41
target_logic: "T1 $80.41 = entry $73.77 + 1.5x R (R=$4.43); T2 $87.05 = entry + 3x R; structure ceiling = 52w high $75.97"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $171.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.21)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
