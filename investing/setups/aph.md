---
ticker: APH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $159.06 ahead of the 2026-07-29 print"
entry_price: 159.06
stop_price: 156.96
stop_logic: "chandelier trail: HH22 $178.52 - 3x ATR $7.19 = $156.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 162.21
target_logic: "T1 $162.21 = entry $159.06 + 1.5x R (R=$2.10); T2 $165.36 = entry + 3x R; structure ceiling = 52w high $178.52"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1432.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.19)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
