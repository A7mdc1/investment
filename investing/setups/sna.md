---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $363.52 ahead of the 2026-10-22 print"
entry_price: 363.52
stop_price: 363.47
stop_logic: "chandelier trail: HH22 $380.98 - 3x ATR $5.84 = $363.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 363.61
target_logic: "T1 $363.61 = entry $363.52 + 1.5x R (R=$0.06); T2 $363.70 = entry + 3x R; structure ceiling = 52w high $420.26"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $107.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
