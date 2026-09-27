---
ticker: NTNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $68.03 ahead of the 2026-11-25 print"
entry_price: 68.03
stop_price: 67.69
stop_logic: "chandelier trail: HH22 $74.42 - 3x ATR $2.24 = $67.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 68.54
target_logic: "T1 $68.54 = entry $68.03 + 1.5x R (R=$0.34); T2 $69.05 = entry + 3x R; structure ceiling = 52w high $78.47"
holding_window_days: 21
catalyst: "2026-11-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $164.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.24)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
