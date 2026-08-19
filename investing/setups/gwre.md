---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $183.40 ahead of the 2026-09-03 print"
entry_price: 183.40
stop_price: 158.12
stop_logic: "chandelier trail: HH22 $185.70 - 3x ATR $9.19 = $158.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 221.30
target_logic: "T1 $221.30 = entry $183.40 + 1.5x R (R=$25.27); T2 $259.21 = entry + 3x R; structure ceiling = 52w high $272.50"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $175.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($9.19)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
