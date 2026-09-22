---
ticker: ONON
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $29.82 ahead of the 2026-11-11 print"
entry_price: 29.82
stop_price: 28.24
stop_logic: "chandelier trail: HH22 $31.16 - 3x ATR $0.97 = $28.24 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.17
target_logic: "T1 $32.17 = entry $29.82 + 1.5x R (R=$1.57); T2 $34.53 = entry + 3x R; structure ceiling = 52w high $51.05"
holding_window_days: 21
catalyst: "2026-11-11 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $271.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.97)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
