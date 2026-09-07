---
name: studio-cycle
description: Execute a bounded autonomous game-studio cycle, including relevant gameplay/art review, implementation, QA and checkpoints. Use when asked to continue studio development; not an infinite background scheduler.
---
Read AGENTS.md, studio/state.json, studio/policy.json and the active task. Recover first if needed using studio-recover. Select eligible work within the approved milestone. Delegate independent game-design/visual/QA review only when needed; default one writer. Preflight for ambiguity, ownership, spatial/UI conflicts and scope. Implement, test, inspect visible evidence, repair at most twice, commit task changes and record checkpoint. Continue eligible work without per-task human approval until task/time/client budget or milestone gate. Block only unsafe dependencies and continue independent work. Never merge main, spend money, add scope or pretend scheduled work exists. Produce one compact delta report.
