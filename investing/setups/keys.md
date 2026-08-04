---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $342.98 ahead of the 2026-08-18 print"
entry_price: 342.98
stop_price: 302.74
stop_logic: "chandelier trail: HH22 $343.19 - 3x ATR $13.48 = $302.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 403.33
target_logic: "T1 $403.33 = entry $342.98 + 1.5x R (R=$40.24); T2 $463.69 = entry + 3x R; structure ceiling = 52w high $374.84"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $381.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.48)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
