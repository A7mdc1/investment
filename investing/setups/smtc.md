---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $132.15 holding the uptrend (no breakdown on volume)"
entry_price: 132.15
stop_price: 121.12
stop_logic: "chandelier trail: HH22 $155.77 - 3x ATR $11.55 = $121.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 148.70
target_logic: "T1 $148.70 = entry $132.15 + 1.5x R (R=$11.03); T2 $165.24 = entry + 3x R; structure ceiling = 52w high $177.26"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $425.2M; pass"
invalidation: "loses EMA20 $132.15 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
