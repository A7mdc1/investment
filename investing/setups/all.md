---
ticker: ALL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $262.42 ahead of the 2026-11-04 print"
entry_price: 262.42
stop_price: 246.94
stop_logic: "chandelier trail: HH22 $263.03 - 3x ATR $5.36 = $246.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 285.64
target_logic: "T1 $285.64 = entry $262.42 + 1.5x R (R=$15.48); T2 $308.85 = entry + 3x R; structure ceiling = 52w high $275.94"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $391.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.36)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Insurance - Property & Casualty' matches 'insurance' — core business fails screen
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
