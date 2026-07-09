---
ticker: TSLA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $404.46 ahead of the 2026-07-22 print"
entry_price: 404.46
stop_price: 373.80
stop_logic: "chandelier trail: HH22 $432.86 - 3x ATR $19.69 = $373.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 450.44
target_logic: "T1 $450.44 = entry $404.46 + 1.5x R (R=$30.66); T2 $496.43 = entry + 3x R; structure ceiling = 52w high $498.72"
holding_window_days: 21
catalyst: "2026-07-22 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $18600.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($19.69)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
