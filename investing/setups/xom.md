---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $180.91 ahead of the 2026-10-30 print"
entry_price: 180.91
stop_price: 173.78
stop_logic: "chandelier trail: HH22 $184.88 - 3x ATR $3.70 = $173.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 191.61
target_logic: "T1 $191.61 = entry $180.91 + 1.5x R (R=$7.13); T2 $202.31 = entry + 3x R; structure ceiling = 52w high $184.80"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $1931.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.70)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
