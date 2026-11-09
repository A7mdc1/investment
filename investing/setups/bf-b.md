---
ticker: BF-B
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $30.32 ahead of the 2026-12-03 print"
entry_price: 30.32
stop_price: 28.85
stop_logic: "chandelier trail: HH22 $31.64 - 3x ATR $0.93 = $28.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 32.53
target_logic: "T1 $32.53 = entry $30.32 + 1.5x R (R=$1.47); T2 $34.74 = entry + 3x R; structure ceiling = 52w high $31.65"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $75.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($0.93)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
