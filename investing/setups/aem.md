---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $189.02 ahead of the 2026-10-28 print"
entry_price: 189.02
stop_price: 185.65
stop_logic: "chandelier trail: HH22 $204.62 - 3x ATR $6.32 = $185.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 194.08
target_logic: "T1 $194.08 = entry $189.02 + 1.5x R (R=$3.37); T2 $199.14 = entry + 3x R; structure ceiling = 52w high $254.06"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $334.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
