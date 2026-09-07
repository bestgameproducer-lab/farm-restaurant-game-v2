# Bootstrap report — STUDIO-001

## Delivered

Fresh repository; no old source tree, private history, secrets or legacy design documents imported. Public visibility explicitly authorized by owner.

Core studio rules, model-neutral Codex configurations, five specialist role definitions, three skills, current scope, system ownership, employee design, schemas, fixture data, task roadmap and bounded autonomy policy were committed in the bootstrap.

Owner availability is not a per-task gate. Codex may perform its own gameplay/design, architecture, UI/art and QA review and continue eligible tasks until the run budget or a real blocker. ChatGPT is a collaborator, not a mandatory always-online orchestrator.

## Checks actually executed in the ChatGPT container

- Source employee fixture validation: PASS for five employees and their knowledge profiles.
- `python -m unittest discover -s tests -p 'test_*.py' -v`: 16/16 PASS.
- Cases include duplicate IDs, unknown references, nonfinite/boolean/invalid skill values, negative wages, orphan/missing profiles, accidental disclosure of hidden truth, reversed ranges and false verified values.
- Incorrect manager estimates and intentionally inaccurate unverified resume claims remain valid content.
- Thumbnail materialization and checksums: PASS; repeated run is idempotent.
- Original source PNG import and checksums: PASS in this container only, not evidence of GitHub original-source delivery.

The fixture files were reconstructed locally from the fetched repository JSON. This is not a full cloned-repository or Godot runtime test. Codex must rerun these commands in its actual checkout.

## Precise art-delivery status

Two approved reference thumbnails are included in the repository. Restaurant is a JPEG; character is a checksum-verified encoded resource materialized by the startup script. Both are only 320 pixels wide.

High-resolution original PNGs are retained in the downloadable ChatGPT source bundle and have NOT been uploaded to this repository. `tools/import_benchmarks.py` imports that bundle safely when available locally. Missing source art must block production-art approval, not isolated data-layer tasks.

No atlas, rig, animation playback, transparent frame alignment, visual gameplay test or production-art approval is claimed.

## Not executed or proven

- Godot project implementation, parsing, rendering, screenshots or exports.
- Native Codex agent/skill loading in the user's client.
- A 24-hour scheduler, push notifications, automated PR merging or deployment.
- Whole-game balance, playability or player enjoyment.

These require actual local execution and evidence. Do not report them as passing because scaffolding exists.

## Start

Use `CODEX_START.md`. First materialize preview resources, run content validation and unit tests, then start EMP-001 on a task branch. Continue only eligible tasks under `studio/policy.json`.
