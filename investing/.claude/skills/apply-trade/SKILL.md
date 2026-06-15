---
name: apply-trade
description: Record a trade the user has ALREADY executed and update the holding .md files + ledger. Use when the user says they bought/sold/closed a position (e.g. "I sold all my FIG at 19.30", "bought 3 more NOW at 108").
---

# Apply Trade

The user executed a trade in their broker; record it. This is bookkeeping only —
never trade, never decide. Parse what they did and update the files.

## Steps
1. Parse: ticker, action (buy/sell), shares (a number or "all"), price, and a name
   if it's a brand-new ticker. If anything is missing or ambiguous, ASK before running.
2. Confirm the parsed trade back to the user in one line and get a yes.
3. Run: `python scripts/apply_txn.py --ticker <T> --action <buy|sell> --shares <n|all> --price <p> [--name "<Name>"]`
4. Report the result: new share count, new avg cost (buys) or realized P/L (sells),
   and whether a position was closed or a new gated stub was created.

## Rules
- Only record trades the user states they already made. Never infer or suggest one.
- A brand-new buy creates a holding with compliance status "unknown" — remind the
  user to screen it in Zoya/Musaffa; it stays gated until they do.
- If a sell would exceed shares held, stop and flag the mismatch.
