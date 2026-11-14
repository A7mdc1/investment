---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $104.07 ahead of the 2026-11-24 print"
entry_price: 104.07
stop_price: 95.04
stop_logic: "chandelier trail: HH22 $106.83 - 3x ATR $3.93 = $95.04 — exit when decline exceeds ~3 average daily ranges"
target_price: 117.62
target_logic: "T1 $117.62 = entry $104.07 + 1.5x R (R=$9.03); T2 $131.16 = entry + 3x R; structure ceiling = 52w high $106.85"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $271.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.93)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
