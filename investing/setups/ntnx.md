---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $70.61 ahead of the 2026-11-25 print"
entry_price: 70.61
stop_price: 65.62
stop_logic: "chandelier trail: HH22 $71.25 - 3x ATR $1.88 = $65.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 78.10
target_logic: "T1 $78.10 = entry $70.61 + 1.5x R (R=$4.99); T2 $85.59 = entry + 3x R; structure ceiling = 52w high $77.94"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $154.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.88)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
