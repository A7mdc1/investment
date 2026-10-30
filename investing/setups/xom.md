---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $187.15 ahead of the 2026-10-30 print"
entry_price: 187.15
stop_price: 176.88
stop_logic: "chandelier trail: HH22 $188.50 - 3x ATR $3.87 = $176.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 202.56
target_logic: "T1 $202.56 = entry $187.15 + 1.5x R (R=$10.27); T2 $217.96 = entry + 3x R; structure ceiling = 52w high $188.47"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2005.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.87)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
