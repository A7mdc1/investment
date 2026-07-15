---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $194.50 ahead of the 2026-08-05 print"
entry_price: 194.50
stop_price: 185.05
stop_logic: "chandelier trail: HH22 $201.66 - 3x ATR $5.54 = $185.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 208.68
target_logic: "T1 $208.68 = entry $194.50 + 1.5x R (R=$9.45); T2 $222.86 = entry + 3x R; structure ceiling = 52w high $201.76"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $522.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.54)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
