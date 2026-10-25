---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $347.73 ahead of the 2026-11-02 print"
entry_price: 347.73
stop_price: 332.76
stop_logic: "chandelier trail: HH22 $351.73 - 3x ATR $6.32 = $332.76 — exit when decline exceeds ~3 average daily ranges"
target_price: 370.18
target_logic: "T1 $370.18 = entry $347.73 + 1.5x R (R=$14.97); T2 $392.63 = entry + 3x R; structure ceiling = 52w high $351.60"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $13062.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
