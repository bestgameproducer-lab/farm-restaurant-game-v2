# REST-FURN-001 — Modular restaurant furniture correction pass

Status: Ready after current implementation branch is safely checkpointed.

## Goal

Replace the current cut-out/collage-like restaurant furniture presentation with a coherent modular furniture system following `docs/FURNITURE_ASSET_CONTRACT.md` and the approved benchmark `assets/approved/restaurant_furniture_modular_benchmark_v1.jpg`.

## Scope

Focus only on furniture/system presentation needed by the current Restaurant Vertical Slice.

Implement or refactor:

- logical furniture footprint data;
- explicit staff/guest interaction anchors;
- coherent kitchen module baseline and shared counter height;
- dining table/chair scale alignment with benchmark characters;
- height/occlusion metadata needed for correct Y-sort;
- path/clearance validation around interactive furniture;
- one assembled kitchen chain: Fridge -> Prep -> Range -> Pass;
- one assembled four-seat dining table test;
- actual in-game visual validation screenshots.

## Out of scope

Do not:

- redesign employee AI;
- expand customer behavior;
- add a large furniture catalog;
- implement unrestricted free rotation;
- replace approved character direction;
- redesign the restaurant gameplay loop.

## Acceptance

1. Kitchen modules read as one continuous built environment rather than isolated cutouts.
2. Furniture scale and rendering language are visually compatible with characters.
3. Employee feet never occupy blocked furniture footprint during work.
4. Sitting characters align to explicit chair anchors and do not intersect tables incorrectly.
5. One employee can navigate Fridge -> Prep -> Range -> Pass without invalid overlap or unreachable interaction points.
6. A four-seat table plus neighboring walkway remains navigable.
7. Front/behind movement around medium/tall furniture produces correct Y-sort/occlusion.
8. Visual reviewer inspects actual game screenshots and provides concrete findings.
9. QA checks pathing and interaction regression.
10. Do not mark production art approved solely from this task; this is a Demo visual/system correction pass.

## References

- `docs/FURNITURE_ASSET_CONTRACT.md`
- `docs/ART_DIRECTION.md`
- `docs/CHARACTER_ASSET_CONTRACT.md`
- `assets/approved/restaurant_furniture_modular_benchmark_v1.jpg`
