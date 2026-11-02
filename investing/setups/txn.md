---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $291.18 holding the uptrend (no breakdown on volume)"
entry_price: 291.18
stop_price: 281.52
stop_logic: "chandelier trail: HH22 $311.55 - 3x ATR $10.01 = $281.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 305.67
target_logic: "T1 $305.67 = entry $291.18 + 1.5x R (R=$9.66); T2 $320.15 = entry + 3x R; structure ceiling = 52w high $330.64"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2063.6M; pass"
invalidation: "loses EMA20 $291.18 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
