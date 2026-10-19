---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $178.35 ahead of the 2026-10-30 print"
entry_price: 178.35
stop_price: 168.98
stop_logic: "chandelier trail: HH22 $179.30 - 3x ATR $3.44 = $168.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 192.41
target_logic: "T1 $192.41 = entry $178.35 + 1.5x R (R=$9.37); T2 $206.46 = entry + 3x R; structure ceiling = 52w high $179.25"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1867.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.44)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
