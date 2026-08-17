---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $117.98 ahead of the 2026-08-26 print"
entry_price: 117.98
stop_price: 103.50
stop_logic: "chandelier trail: HH22 $118.81 - 3x ATR $5.10 = $103.50 — exit when decline exceeds ~3 average daily ranges"
target_price: 139.69
target_logic: "T1 $139.69 = entry $117.98 + 1.5x R (R=$14.48); T2 $161.41 = entry + 3x R; structure ceiling = 52w high $118.81"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $254.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.10)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
