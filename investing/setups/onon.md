---
ticker: ONON
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $30.15 ahead of the 2026-11-11 print"
entry_price: 30.15
stop_price: 28.11
stop_logic: "chandelier trail: HH22 $31.16 - 3x ATR $1.02 = $28.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 33.21
target_logic: "T1 $33.21 = entry $30.15 + 1.5x R (R=$2.04); T2 $36.27 = entry + 3x R; structure ceiling = 52w high $51.10"
holding_window_days: 21
catalyst: "2026-11-11 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $300.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.02)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
