---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $446.87 ahead of the 2026-11-02 print"
entry_price: 446.87
stop_price: 395.85
stop_logic: "chandelier trail: HH22 $452.43 - 3x ATR $18.86 = $395.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 523.39
target_logic: "T1 $523.39 = entry $446.87 + 1.5x R (R=$51.02); T2 $599.92 = entry + 3x R; structure ceiling = 52w high $748.53"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $302.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($18.86)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
