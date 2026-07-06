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
5. If this is a brand-new BUY (new holding file created), per `PM_FRAMEWORK.md`'s
   recommendation to record the PM decision record AT ENTRY, before emotion can
   revise it: ask the user (don't fill these in yourself) for —
   `initial_stop`, `target_price` + `target_method`, `conviction`, `catalyst`
   (type/desc/date), `thesis_one_liner`, `invalidation` trigger, and a `pre_mortem`
   (top 2-3 reasons this trade fails, written now). Write whatever they give you
   into the holding's front-matter; leave any they skip as `null` rather than guessing.

## Rules
- Only record trades the user states they already made. Never infer or suggest one.
- A brand-new buy creates a holding with compliance status "unknown" — remind the
  user to screen it in Zoya/Musaffa; it stays gated until they do.
- If a sell would exceed shares held, stop and flag the mismatch.
- Never invent the PM-record fields (stop/target/conviction/invalidation/pre_mortem)
  on the user's behalf — ask, and leave null if they don't answer.
