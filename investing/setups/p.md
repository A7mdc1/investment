---
ticker: P
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $116.80 ahead of the 2026-08-26 print"
entry_price: 116.80
stop_price: 103.86
stop_logic: "chandelier trail: HH22 $119.10 - 3x ATR $5.08 = $103.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 136.21
target_logic: "T1 $136.21 = entry $116.80 + 1.5x R (R=$12.94); T2 $155.63 = entry + 3x R; structure ceiling = 52w high $119.06"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $265.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.08)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
