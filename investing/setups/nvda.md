---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $219.40 ahead of the 2026-08-26 print"
entry_price: 219.40
stop_price: 199.81
stop_logic: "chandelier trail: HH22 $223.63 - 3x ATR $7.94 = $199.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 248.79
target_logic: "T1 $248.79 = entry $219.40 + 1.5x R (R=$19.59); T2 $278.18 = entry + 3x R; structure ceiling = 52w high $236.17"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $26141.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.94)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
