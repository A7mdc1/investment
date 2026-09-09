---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $23.66 ahead of the 2026-11-04 print"
entry_price: 23.66
stop_price: 22.20
stop_logic: "chandelier trail: HH22 $24.09 - 3x ATR $0.63 = $22.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.86
target_logic: "T1 $25.86 = entry $23.66 + 1.5x R (R=$1.46); T2 $28.05 = entry + 3x R; structure ceiling = 52w high $24.10"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $208.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.63)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
