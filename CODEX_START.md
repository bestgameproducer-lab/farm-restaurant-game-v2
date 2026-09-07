# Copy into Codex in this repository

Read AGENTS.md, docs/BOOTSTRAP_REPORT.md, docs/CURRENT_MILESTONE.md, studio/state.json and studio/policy.json. On this first run also read docs/PROJECT_VISION.md and docs/CHATGPT_CODEX_WORKFLOW.md. Do not copy code or old design rules from the legacy repository.

Act as Producer of the virtual game studio. I authorize bounded autonomous development while I am away, including independent gameplay, architecture, visual/UI and QA review using the appropriate project subagents/skills. You are not just a coding executor. Use minimal necessary delegation; verify available capabilities and label fallback/self-review honestly.

First run locally:

```sh
python tools/materialize_assets.py
python tools/validate_content.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

Use the Python 3 executable available on this machine. The included art previews are only 320px references, not original production assets. If the original-source ZIP is attached or available locally, unpack it safely and run `python tools/import_benchmarks.py --source PATH_TO_SOURCE_DIRECTORY`. Never claim original PNGs are present without checking. Do not block data-layer tasks on high-resolution art; use labelled placeholders for technical tasks, and keep production-art review pending.

Start EMP-001, complete its tests/review/checkpoint, then continue eligible restaurant-demo tasks within the run budget. No per-task approval pause. Decompose approved roadmap items as needed without adding product scope. Follow studio-cycle and recover from repository state, not chat memory.

Preserve approved core/art decisions. Use latest benchmark references only for their declared purpose: they are not final atlases or proof of a running game. On real design conflicts create a concise blocker with evidence/options; continue independent work. Do not spend money, change security settings, activate a schedule, merge main or publish releases.

Pin input revisions; work on task/integration branches; return tested changes, real captures, review findings, blockers and next checkpoint. Stop cleanly at the configured limit or owner playtest gate. Never say a scheduler or notification channel is active without having configured and verified it.
