---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $49.41 ahead of the 2026-11-04 print"
entry_price: 49.41
stop_price: 48.02
stop_logic: "chandelier trail: HH22 $52.96 - 3x ATR $1.65 = $48.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 51.48
target_logic: "T1 $51.48 = entry $49.41 + 1.5x R (R=$1.38); T2 $53.55 = entry + 3x R; structure ceiling = 52w high $52.95"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $243.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.65)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
