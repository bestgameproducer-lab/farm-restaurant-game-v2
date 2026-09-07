# Farm & Restaurant — Employee-Centered Management Studio

Fresh Godot 4 / GDScript project. Mouse-driven management, not avatar micromanagement. First milestone: a compact restaurant demo. Long-term differentiator: recruit imperfectly known people, watch them work and grow, and make meaningful organizational decisions.

## Ready to begin

The studio bootstrap, design baseline, sample content, validation scripts and lightweight visual references are committed. The Godot game itself has not been implemented yet.

Open this repository in Codex and follow [CODEX_START.md](CODEX_START.md). Local Python 3 checks:

```sh
python tools/materialize_assets.py
python tools/validate_content.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

Then execute [EMP-001](tasks/EMP-001.md). The Producer may continue eligible milestone tasks within the autonomy budget without waiting for owner approval after every task.

## Start reading

1. [AGENTS.md](AGENTS.md) — compact operating contract.
2. [Current milestone](docs/CURRENT_MILESTONE.md), [state](studio/state.json), [budget](studio/policy.json).
3. The active task and only its referenced specs.
4. [Full studio handbook](studio/HANDBOOK.md) only for relevant policies.
5. [Bootstrap report](docs/BOOTSTRAP_REPORT.md) — what was actually tested and what remains unverified.

## Collaboration

Owner + ChatGPT make design decisions, create content/art, and review results. Codex owns implementation AND its own gameplay, architecture, UI/art and QA review. Git commits carry durable decisions and evidence. ChatGPT is not a mandatory online dependency; the owner being away does not stop an approved task.

Rules are model-neutral. Use an actually available model in the client; do not guess IDs or claim a text prompt has started a scheduler. Project agent definitions are under `.codex/agents/`; skills are under `.agents/skills/`. First run must verify the client actually loads them.

## Main documents

- [Project vision](docs/PROJECT_VISION.md)
- [Game design](docs/GAME_DESIGN.md)
- [Employee system](docs/EMPLOYEE_SYSTEM.md)
- [Restaurant demo](docs/RESTAURANT_VERTICAL_SLICE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [UI rules](docs/UI_GUIDELINES.md)
- [Art direction](docs/ART_DIRECTION.md)
- [Character asset contract](docs/CHARACTER_ASSET_CONTRACT.md)
- [ChatGPT/Codex workflow](docs/CHATGPT_CODEX_WORKFLOW.md)
- [Decisions](docs/DECISIONS.md)

## Art: exact delivery status

[Approved reference manifest](assets/approved/manifest.json) and [usage rules](assets/approved/README.md).

The restaurant is included as a 320px JPEG preview. The character 320px preview is included as verified encoded fragments; `materialize_assets.py` creates the JPEG without network access. Never read encoded image text into the agent context; run the script and inspect the resulting image instead.

Full-resolution original PNGs are in the companion ChatGPT source ZIP, **not yet in GitHub**. When available locally, import with `python tools/import_benchmarks.py --source PATH_TO_SOURCE_DIRECTORY`. This limitation does not block EMP-001; it does prevent treating thumbnails as final art or detailed sprite specifications.

Neither reference is a production atlas, a layered rig or evidence of in-game animation. Original generated text/ages/job labels do not override the approved game rules.

## Safety and verification

No secrets, old code history, paid services, release publishing, scheduled jobs or automatic main merges are enabled by this bootstrap. Use branches after initial setup. Automated review checks compliance; it does not prove that real players enjoy the game.
