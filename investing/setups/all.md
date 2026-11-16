---
ticker: ALL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $281.25 (52w high) on >1.2x 20d avg volume"
entry_price: 281.25
stop_price: 261.16
stop_logic: "chandelier trail: HH22 $281.11 - 3x ATR $6.65 = $261.16 — exit when decline exceeds ~3 average daily ranges"
target_price: 311.39
target_logic: "T1 $311.39 = entry $281.25 + 1.5x R (R=$20.09); T2 $341.53 = entry + 3x R; structure ceiling = 52w high $281.25"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $392.3M; pass"
invalidation: "closes back below the breakout level $281.25 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Insurance - Property & Casualty' matches 'insurance' — core business fails screen
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
