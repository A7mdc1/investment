---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $188.50 ahead of the 2026-10-28 print"
entry_price: 188.50
stop_price: 185.65
stop_logic: "chandelier trail: HH22 $204.62 - 3x ATR $6.32 = $185.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 192.78
target_logic: "T1 $192.78 = entry $188.50 + 1.5x R (R=$2.85); T2 $197.06 = entry + 3x R; structure ceiling = 52w high $254.04"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $324.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
