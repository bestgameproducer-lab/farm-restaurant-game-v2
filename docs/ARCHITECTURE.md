# Architecture proposal for implementation

Status: delegated technical starting point, not existing code. Engine: Godot 4, GDScript; exact version discovered/pinned by EMP-001. Keep a small composition-based architecture; do not instantiate every future service now.

## A1 Ownership and boundaries

Definitions are immutable resources/data. Runtime instances own changing per-person state. Employment holds role, wage, duties and organization references. Knowledge holds evidence/estimates with provenance; public read models expose only permitted fields. UI sends commands and renders read models, not domain rules in button handlers.

`SYSTEM_OWNERSHIP.md` owns the service map. Stable string ids identify employees, tables, recipes, events and definitions; display names/file paths are not identity. Use typed data and explicit signals/commands. Prefer scoped composition over global singleton proliferation.

## A2 Proposed layout

`game/domain/` rules/resources; `game/services/` clock, jobs, orders and inventory when needed; `game/scenes/` scenes/controllers; `game/presentation/` visual adapters; `game/ui/` views/themes; `tests/` focused and integration tests. Existing project conventions can replace this after a documented local decision. Do not rename everything for aesthetic reasons.

## A3 Jobs and reservations

A shared job system evaluates hard eligibility before preference score. Reserve job plus necessary station/item/seat ownership atomically within the simulation tick. Tie reservations to owner and lifecycle; release on cancellation/failure/exit. Use reason codes; avoid random movement as a substitute for work. Paused time must not accidentally expire simulation leases. Worker-process task leases and in-game job reservations are different systems.

## A4 Render and simulation

Footprint grid determines spatial legality. Navigation uses walkable paths/work slots. Visual sprite bounds may extend above occupancy. Foot anchors and ordered layers decide occlusion. Use a single clock for simulation; render/interpolation can run separately. Off-screen rules will later run without requiring active visual scenes.

## A5 Validation and compatibility

Keep deterministic seeds and stepable time for tests. Test collisions/ownership/cancellation and state transitions, not only file loading. Schema docs are design contracts; runtime JSON input must still be validated. Save a version and stable ids; reject unsupported versions clearly or run explicit migrations. Do not store visual nodes in saved domain data. See `schemas/SAVE_SCHEMA.md`.

## A6 Performance

Measure first. Event-driven updates, bounded candidate jobs and sparse significant relations; no per-frame all-pairs social loop or full UI rebuild. Debug reason traces are bounded. Caches need invalidation. No premature dependency injection framework or generic plugin engine.
