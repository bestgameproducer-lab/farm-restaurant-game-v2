# Shared workflow — assisted and autonomous

## W1 Roles

Owner is final product authority. ChatGPT helps discuss and produce design/content/visual assets and can write authorized repository changes through the actual available connector. Codex is an active studio: designs local solutions, challenges mechanics/art, implements, tests, captures evidence and reviews. It is NOT prohibited from thinking about gameplay or art.

## W2 Durable bridge

GitHub is shared storage, not a live chat bus. This ChatGPT conversation does not automatically see local files or every future commit; Codex does not automatically read this conversation or newly generated attachments. In an active turn, publish approved deliverables and report the resulting commit/PR. Codex fetches relevant updates at a task boundary, records a design revision, and works against that snapshot. Do not pull changing specifications halfway through a write. Conflicts become a small decision issue.

Design changes should arrive on `design/<change-id>` with status Proposed or Owner-approved. Codex implementation uses `codex/<task-id>` and optional `integration/restaurant-demo`; main stays the owner-approved baseline. No same-file parallel writers across ChatGPT/Claude/Codex. No implicit permission to publish unrelated personal chat history, credentials or financial records.

## W3 Assisted mode

Discuss important product choices with the owner. Record only the delta: decision, reason, scope, acceptance, superseded clause. Art generation first enters reference/candidate status; owner approval applies to a named revision and use, not everything a model later generates.

## W4 Autonomous mode

The owner explicitly authorizes Codex to activate studio mode when unavailable. No need to ask permission before each scoped review or task. Producer decomposes the approved milestone, confirms task eligibility, uses specialist reviews and can integrate passing work into the integration branch. It can tune provisional timing/layout/implementation defaults and record `Delegated` decisions. It cannot mark a new art direction or expanded feature as owner-approved.

Block only tasks whose uncertainty truly affects correctness, irreversible state or product identity. Continue independent eligible work. Local UI spacing, non-destructive runtime asset preparation, reason-code design and test choices are autonomous. Hidden truth semantics, removing employee agency, paid tools, replacing approved art, main merges and releases need owner input.

## W5 Review handoff

Codex writes a compact `reports/<task-id>.md`: base/design revision, tested commit or tree fingerprint, changed paths, implementation outcome, tests with commands/exit codes, real screenshots/recording paths, independent/self-review disclosure, gameplay and art findings, blockers and next action. No long copied logs; raw logs stay local or artifact storage. GitHub issues/PRs can carry blockers; creating an issue does not guarantee a ChatGPT mobile notification.

## W6 Scheduling is a separate capability

These files do not create a daemon, scheduled task, notification subscription or unlimited allowance. Configure an available client automation or scheduler only after a supervised dry run, capability check and budget approval. A run needs an online execution environment and required permissions. Do not use an endless paid-model polling loop. No automatic overage purchase. Current bootstrap does NOT enable a schedule.

## W7 Recovery and concurrency

`studio/state.json` is the concise index, task checkpoint records evidence. Validate Git status/diff, actual worker states and pinned inputs. An old PASS becomes stale when affected code/spec/assets change. One coordinator; file timestamps or Git push success alone are not cross-machine atomic locks. Multi-host scheduling is deferred until genuinely needed.
