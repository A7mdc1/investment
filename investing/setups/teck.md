---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $68.05 ahead of the 2026-10-29 print"
entry_price: 68.05
stop_price: 62.47
stop_logic: "chandelier trail: HH22 $69.38 - 3x ATR $2.30 = $62.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 76.42
target_logic: "T1 $76.42 = entry $68.05 + 1.5x R (R=$5.58); T2 $84.79 = entry + 3x R; structure ceiling = 52w high $72.47"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $181.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.30)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
