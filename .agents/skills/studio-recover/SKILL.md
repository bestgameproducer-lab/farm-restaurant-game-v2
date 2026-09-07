---
name: studio-recover
description: Recover a game task after interruption, context loss or machine handoff using persisted evidence and Git state; do not blindly replay the previous conversation.
---
Read AGENTS.md, studio/state.json, active task/checkpoint and its relevant spec revision. Inspect branch/worktree, status/diff and latest evidence. Identify completed, unverified and pending gates. Preserve user changes. Verify unverified work before further edits; invalidate only evidence affected by changes. Resume the first incomplete gate with the correct owner/reviewer. A missing agent thread is not a completed review. Check actual worker/process ownership before reassigning. Record recovery audit and safe next action. Unsafe/conflicting state blocks the task, not unrelated work. Do not reset, delete or regenerate the whole project.
