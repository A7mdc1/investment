---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $254.25 ahead of the 2026-12-16 print"
entry_price: 254.25
stop_price: 251.81
stop_logic: "chandelier trail: HH22 $292.73 - 3x ATR $13.64 = $251.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 257.91
target_logic: "T1 $257.91 = entry $254.25 + 1.5x R (R=$2.44); T2 $261.57 = entry + 3x R; structure ceiling = 52w high $428.75"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $326.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.64)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
