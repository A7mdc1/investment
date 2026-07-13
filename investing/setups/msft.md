---
ticker: MSFT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $392.77 ahead of the 2026-07-29 print"
entry_price: 392.77
stop_price: 369.30
stop_logic: "chandelier trail: HH22 $405.04 - 3x ATR $11.91 = $369.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 427.98
target_logic: "T1 $427.98 = entry $392.77 + 1.5x R (R=$23.47); T2 $463.19 = entry + 3x R; structure ceiling = 52w high $550.87"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $17518.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.91)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
