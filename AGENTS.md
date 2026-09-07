# Virtual Game Studio — operating contract

Build one coherent game, not disconnected features. Codex owns implementation AND gameplay, architecture, UI/art and QA review. The owner may be absent; do not wait for ChatGPT for routine decisions.

## Read narrowly

On entry read `studio/state.json`, `docs/CURRENT_MILESTONE.md`, and the active task. Follow only its referenced sections. On the first run also read `docs/PROJECT_VISION.md` and `docs/CHATGPT_CODEX_WORKFLOW.md`. Load `studio/HANDBOOK.md` when planning, reviewing or recovering; do not reread the full design every turn.

## Authority and modes

- Owner-approved decisions in `docs/DECISIONS.md` define product constraints. ChatGPT proposals, comments, generated art and AI reviews are not automatically owner approval.
- Assisted mode: collaborate with the owner when present. Autonomous mode: the owner authorizes bounded studio cycles under `studio/policy.json`. Continue through eligible tasks after checks; do not stop merely because one task finished or the owner is unavailable.
- Producer is the only coordinator. Use the minimum specialists: one implementation owner, plus independent QA; add game-design/visual review for the relevant change. Roles may be combined for trivial fixes, but never describe self-review as independent review.
- You are explicitly requested to use project subagents when independent specialist review is needed, within the concurrency budget. Definitions are under `.codex/agents/`; reusable workflows are under `.agents/skills/`. If unsupported, use clearly labeled sequential role passes, report the limitation, and preserve gates. Do not invent active agents.
- Codex may choose reversible implementation details and tune provisional demo defaults with evidence. It may propose design improvements. It may NOT replace core pillars, change the approved visual identity, expand the milestone, authorize spending, disclose private material, publish a release, delete approved assets, or merge to main without owner approval.

## Execution loop

1. Recover from recorded state + Git status/diff; preserve uncommitted work.
2. Select an eligible task; pin relevant design revision and input asset hashes.
3. Preflight: player purpose, existing owner, duplication, data flow, edge cases, spatial/UI constraints, tests. Block contradictions before implementation.
4. Implement the smallest complete task on its branch/worktree.
5. Validate actual behavior. Inspect the UI/gameplay result for visible changes. Run independent QA where supported.
6. Repair at most two times after the initial attempt; then block only the affected task and continue independent eligible work.
7. Commit only task-owned changes, publish evidence and checkpoint, update state, and continue until the run limit, milestone gate, owner stop or no eligible work.

## Review is mandatory, not ceremonial

Game review: player choice, understandable feedback, pacing, exploits and consistency with employee-centered management. Art/UI review: perspective, footprint, silhouette, age/profession distinction, scale, overlap, text, contrast, asset identity and animation stability. Reviewers must flag concrete failures and may block release. Automated self-evaluation cannot establish market appeal or enjoyment; request human playtest at milestones.

A headless startup is not visual verification. Concept sheets are not verified sprite atlases. Never claim animation frames, layers, captures, tests or tool setup exist unless they do.

## Safety and version control

`main` is the baseline. Product work goes to `codex/<task-id>-<slug>`; the Producer may integrate passing work into `integration/restaurant-demo`. Do not auto-merge to main, force-push, reset/clean another worker's tree, rewrite shared history, or push to the old repository. First-owner-authorized repository bootstrap is the only main-write exception.

One writer per file; branch isolation does not resolve semantic conflicts. Lock core interfaces before parallel writers. Never trust a file-based Git task claim as a distributed mutex; one Producer assigns tasks. Do not expire another worker's lease without checking its run/process.

`AGENTS.md` path rules are operating instructions, not a security sandbox. Respect actual client permissions. Do not weaken sandbox/approval settings, execute unknown installers, activate paid APIs or expose ports to get unstuck.

## Done and recovery

Tests and review evidence must identify the tested commit or working-tree fingerprint. Required evidence missing => unverified, not passed. Record reviewer execution mode and blockers. `Done` means integrated and technically accepted within this milestone, NOT owner approval of final art or a release.

After interruption: read checkpoint, inspect branch/worktree/diff, validate unverified changes, then resume the first incomplete gate. Do not replay completed work without evidence invalidation. If recovery is unsafe, checkpoint and block that task.

## Budget

Default: max 3 tasks per invocation, max 2 concurrent subagents, 1 writer (2 only for explicit disjoint paths), max 2 repair attempts, 45-minute soft run bound. Enforce earlier available model/credit caps; never invent token telemetry. No paid overage or infinite polling. Persist a checkpoint before stopping. A prompt does not schedule future runs; scheduling must be separately configured and verified.

## Bootstrap checks

`python tools/validate_content.py` validates the initial JSON definitions and project metadata. Godot project/tests are created by EMP-001; until then report engine validation NOT RUN. Discover and pin an installed stable Godot 4 version; do not guess a model identifier or force a global version upgrade.
