---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1169.84 ahead of the 2026-10-29 print"
entry_price: 1169.84
stop_price: 1117.05
stop_logic: "chandelier trail: HH22 $1215.00 - 3x ATR $32.65 = $1117.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 1249.03
target_logic: "T1 $1249.03 = entry $1169.84 + 1.5x R (R=$52.79); T2 $1328.21 = entry + 3x R; structure ceiling = 52w high $1292.64"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2526.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($32.65)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
