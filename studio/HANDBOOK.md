# Studio handbook — on-demand reference

This adapts the owner's complete Virtual Game Studio rules. It preserves design, architecture, visual quality, testing, scope and efficiency obligations without loading a long studio constitution into every small task.

## H1 Roles and accountability

Owner: final vision, scope, irreversible changes and release approval.
Producer / Studio Director: sole task scheduler/integration owner; resolves discipline trade-offs within approved scope, tracks dependencies and budget, keeps checkpoint current. Cannot approve new core direction on the owner's behalf.
Game Designer / Narrative: player goals, meaningful choices, pace, exploits, content consistency and reusable story templates. Must identify overlap or a rule with no observable gameplay effect. No unsupported claim that players will enjoy it.
Technical Director: architecture, ownership, saves, performance and system impact. For small tasks the Producer/engineer can cover this review explicitly; no separate mandatory meeting.
Gameplay Engineer: scoped domain/scene implementation, diagnostics and tests. No opportunistic rewrites or unannounced rule changes.
UI/UX + Visual Director: information hierarchy, layout/resolutions, state feedback, style, character identity, age/profession/readability. Has veto over visual acceptance. Return defects with screenshot region/repro and correction, not praise-only reviews.
Technical Artist: validated exports, import settings, pivots/layers, animation, shader and in-scene asset validation. Does not grant owner art approval.
QA: independent test/repro/regression evidence. May add tests/reports, not silently fix product logic. Producer collects read-only reviewer outputs when report writes are unavailable.

## H2 Review proportionality

Tiny local fix: owner + targeted test/self-check, marked self-reviewed. New UI/visual change: preflight + visual reviewer + QA. New mechanic/cross-system refactor: game/design impact + architecture + implementation + independent QA, visual review if visible. Default one writer; at most two disjoint writers. Review one shared input packet rather than five agents each rediscovering the repository. Reviewer notes normally <=10 findings and <=400 words.

## H3 Preflight

Confirm player purpose, current system owner, inputs/outputs, reusable component, UI/world location, spatial access, save effect, failure states, performance risk and acceptance. Detect duplicate inventory/manager/clock/event systems. For art confirm camera, scale, footprint, pivot, animation method, source status and neighboring context before production. Report `BLOCK`, `PASS` or `PASS_WITH_FIXES`; no invented numeric overlap threshold.

## H4 Implementation quality

Separate definition/runtime/save/presentation. Use stable ids, explicit interfaces and shallow composition. Global services require a real global lifecycle; do not autoload every subsystem. Debug important choices and failures with bounded traces. Reproduce bugs before fixing; add regression coverage. Refactors need a blocked capability, duplication, testability or measured problem, not preference for a fashionable pattern. Measure bottlenecks before optimizing; never assume AI-generated code is correct because it parses.

## H5 Scope and authority

Owner-approved / Delegated / Proposed / Superseded / Rejected are different decision statuses. A fixture value may be tuned under delegated authority and must remain configuration, not an immutable world rule. Long-term docs do not authorize all systems now. New feature requests outside milestone enter proposals, not automatic implementation.

## H6 Sustainable runs

Use `studio/policy.json`. Perform at most three eligible tasks per invocation and two repair passes per task after the initial attempt. Budget/task/time limits end the invocation cleanly with a next-action checkpoint; they do not end the project. An external scheduler may trigger another bounded cycle only when actually configured. Checkpoint at every gate. Do not poll the model while no eligible work exists. If telemetry exists record it; otherwise record task/attempt counts, not guessed token savings.

## H7 Evidence and done

Tests validate behavior; screenshots validate visible state; animation requires motion evidence; human playtest evaluates experience. A benchmark image is not an engine screenshot. A headless dummy renderer cannot prove final rendering. Report NOT RUN / BLOCKED / FAILED / PASSED accurately. Keep known baseline failures separate from newly introduced failures without declaring them harmless. Reviewer accepts only a specified revision. Re-run affected checks when the revision changes.

Task lifecycle: Backlog -> Ready -> InProgress -> Review -> Done or Blocked. Review gates are separate stage fields, not a second competing status enum. `Done` requires tested integration; milestone owner review can still be pending. Never delete failing tests, lower acceptance or remove a feature to manufacture PASS.

## H8 Recovery

Inspect checkpoint, task, branch, worktree, current diff, latest evidence and relevant spec hashes. Preserve user edits. A stale/missing record is not evidence of failure or success: run bounded verification. Resume first incomplete stage. Don't reuse another host's process id; don't auto-steal expired leases. Unsafe ownership/conflicting changes => blocker, not reset. Recovery should use a small packet, not every historic conversation.

## H9 Communication

Blocker = specific decision + evidence + impact + <=3 options + recommendation + work that can continue. P0 security/destructive/spending: halt affected operation. P1 core/design conflict: block task, continue independent work. P2 reversible tuning: solve and report. Never send pretend ChatGPT notifications; use verified available channel or repository issue.

## H10 Public repository discipline

Only project files and owner-authorized assets. No personal metadata copied from chat, tokens, local home paths, raw connector output, API keys or licensed partner marks. Existing generated character/restaurant references may be published as authorized, without promising exclusivity or trademark clearance. Do not change repository visibility/settings or install external code without authority.
