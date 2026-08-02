---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $319.08 ahead of the 2026-08-18 print"
entry_price: 319.08
stop_price: 303.88
stop_logic: "chandelier trail: HH22 $345.20 - 3x ATR $13.77 = $303.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 341.88
target_logic: "T1 $341.88 = entry $319.08 + 1.5x R (R=$15.20); T2 $364.68 = entry + 3x R; structure ceiling = 52w high $374.95"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $402.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.77)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
