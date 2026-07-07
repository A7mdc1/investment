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

1. Run discovery (`discover.py`) → `leads.md`.
2. `python scripts/scaffold.py --all-leads` auto-fills a **DRAFT** card
   (`status: draft`) for every lead — complete proposed plans (entry/stop/target/
   logic/invalidation) from Yahoo formula outputs. Read them in the assessment
   report. (Or scaffold one name: `scaffold.py TICKER [--setup-type breakout]`.)
3. **Review & approve.** Do your own research; edit any level or text you disagree
   with; then set `status: planned`. This flip is the approval — a draft can never
   become a buy candidate on its own.
4. Screen the name in Zoya/Musaffa and record the verdict + date in the card's
   `shariah:` block (the scaffold leaves it `unverified` — only you set `compliant`).
5. Run `recommend.py` — a complete, **planned**, compliant, fresh card with
   reward:risk above the floor and a catalyst in the window clears to BUY-CANDIDATE.
6. You size and execute; log it with `/apply-trade`; review with `journal.py`.

### Two invariants (non-negotiable)
- A machine-filled (`draft`) card can **never** reach BUY-CANDIDATE without your
  explicit approval — the `status: draft → planned` flip.
- The scaffold **never** writes `shariah.status: compliant`. Only a human
  Zoya/Musaffa screen sets that.

## Card status lifecycle
`draft` (scaffold, unreviewed) → `planned` (you approved) → `live` (position open)
→ `closed` / `abandoned`. Only `planned`/`live` clear the edge gate.

## Fields that matter most

- **`setup_type`** — your taxonomy (breakout / pullback / earnings_run /
  post_earnings_drift / other). Keep the strings consistent: the journal groups
  expectancy by this, so a typo silently splits a bucket.
- **`earnings_plan`** — required. A stop does not execute through an overnight
  gap; the plan says whether you're flat before the print or sized down for it.
- **`invalidation`** — what tells you the setup failed *before* price hits the
  stop, so you can stand aside early.

Files starting with `_` (and this README) are ignored by the loader.
