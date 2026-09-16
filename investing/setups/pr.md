---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $23.12 ahead of the 2026-11-04 print"
entry_price: 23.12
stop_price: 22.53
stop_logic: "chandelier trail: HH22 $24.65 - 3x ATR $0.71 = $22.53 — exit when decline exceeds ~3 average daily ranges"
target_price: 24.01
target_logic: "T1 $24.01 = entry $23.12 + 1.5x R (R=$0.59); T2 $24.89 = entry + 3x R; structure ceiling = 52w high $24.65"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $226.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.71)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
