---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $365.75 ahead of the 2026-10-22 print"
entry_price: 365.75
stop_price: 362.90
stop_logic: "chandelier trail: HH22 $379.60 - 3x ATR $5.57 = $362.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 370.03
target_logic: "T1 $370.03 = entry $365.75 + 1.5x R (R=$2.85); T2 $374.30 = entry + 3x R; structure ceiling = 52w high $420.40"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $105.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.57)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
