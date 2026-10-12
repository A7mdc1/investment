---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $172.22 ahead of the 2026-10-30 print"
entry_price: 172.22
stop_price: 161.69
stop_logic: "chandelier trail: HH22 $172.55 - 3x ATR $3.62 = $161.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 188.03
target_logic: "T1 $188.03 = entry $172.22 + 1.5x R (R=$10.53); T2 $203.83 = entry + 3x R; structure ceiling = 52w high $174.14"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2085.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.62)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
