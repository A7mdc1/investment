---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $23.95 ahead of the 2026-11-04 print"
entry_price: 23.95
stop_price: 22.35
stop_logic: "chandelier trail: HH22 $24.20 - 3x ATR $0.62 = $22.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.34
target_logic: "T1 $26.34 = entry $23.95 + 1.5x R (R=$1.59); T2 $28.73 = entry + 3x R; structure ceiling = 52w high $24.21"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $208.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.62)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
