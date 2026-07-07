# Setups — pre-trade cards (the "edge" for a swing trade)

Each file here is one **pre-trade setup card**: a lightweight, ~10-minute plan
for a single prospective swing trade. For this system, *edge* is not a
fundamental thesis — it's a **defined, repeatable setup** with a specific entry
trigger, a structural stop, a reachable target, an earnings plan, and an
invalidation that kills the setup before the stop does.

## Why this exists

A raw discovery table or a one-line `why` is not an edge. `recommend.py` will
not label a name **BUY-CANDIDATE** until:

1. a completed setup card exists here (`setups/<ticker>.md`) with non-empty
   `entry_trigger`, `stop_logic`, `target_logic`, `earnings_plan`, and
   `invalidation`, and `status: planned` or `live`; **and**
2. the card's `shariah.status` is `compliant`, screened within ~1 quarter
   (verified in Zoya/Musaffa — the ratio pre-check is never enough).

Without both, the strongest label a name can earn is **RESEARCH** (from
`recommend.py`) or **LEAD** (from `discover.py`). The system gates trade
*quality*; how many cards you write and how many trades you take is your call.

## Workflow

1. Run discovery → skim the leads.
2. For the few worth planning, copy `_template.md` → `setups/<ticker>.md` and
   fill it in (~10 min).
3. Screen the name in Zoya/Musaffa and record the verdict + date in the card's
   `shariah:` block.
4. Run `recommend.py` — a complete, compliant, fresh card with reward:risk above
   the floor and a catalyst in the window clears to BUY-CANDIDATE.
5. You size and execute; log it with `/apply-trade`.

## Fields that matter most

- **`setup_type`** — your taxonomy (breakout / pullback / earnings_run /
  post_earnings_drift / other). Keep the strings consistent: the journal groups
  expectancy by this, so a typo silently splits a bucket.
- **`earnings_plan`** — required. A stop does not execute through an overnight
  gap; the plan says whether you're flat before the print or sized down for it.
- **`invalidation`** — what tells you the setup failed *before* price hits the
  stop, so you can stand aside early.

Files starting with `_` (and this README) are ignored by the loader.
