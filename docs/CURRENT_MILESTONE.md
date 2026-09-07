# Current milestone: restaurant demo

Scope: `RESTAURANT_VERTICAL_SLICE.md`. Fresh project, no old code import. Game product implementation has not started. Read bootstrap report before starting.

Start EMP-001; then REST-001/002 per dependency table. Producer may split remaining approved roadmap items into bounded task cards, mark Ready after preflight, and continue automatically within `studio/policy.json`. No need for owner approval after each small task. Stop at run cap, real blockers or final owner playtest gate.

| Task | Outcome | Dependencies |
|---|---|---|
| EMP-001 | Godot bootstrap + employee definition/load/validation + safe profile projection | none |
| REST-001 | Real restaurant scene, spatial footprints, visible paths, one animated character test | EMP-001 |
| REST-002 | Workstation/job reservation and runtime staff autonomy | REST-001 |
| REST-003 | Seat reservation + customer lifecycle | REST-002 |
| REST-004 | Inventory/order/cook/pass/serve/payment/clean loop | REST-003 |
| REST-005 | Management HUD, priorities, override and inspection | REST-004 |
| EMP-002 | Resume lite, candidate hire, one reveal/employee decision | REST-005 |
| REST-006 | Save/reload, regression, visual/playable review package | EMP-002 |

Future employee careers/relationships/families remain documented only. Do not create ten new foundational systems in EMP-001.
