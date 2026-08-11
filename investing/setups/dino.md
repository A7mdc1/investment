---
ticker: DINO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $85.32 holding the uptrend (no breakdown on volume)"
entry_price: 85.32
stop_price: 83.06
stop_logic: "chandelier trail: HH22 $94.22 - 3x ATR $3.72 = $83.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 88.72
target_logic: "T1 $88.72 = entry $85.32 + 1.5x R (R=$2.26); T2 $92.11 = entry + 3x R; structure ceiling = 52w high $94.25"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $269.4M; pass"
invalidation: "loses EMA20 $85.32 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
