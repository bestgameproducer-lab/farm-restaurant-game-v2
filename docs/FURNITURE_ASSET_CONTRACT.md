# Restaurant Furniture Asset Contract V1

Status: Owner-approved demo benchmark contract.

Primary benchmark: `assets/approved/restaurant_furniture_modular_benchmark_v1.jpg`

## Goal

Restaurant furniture must read as one modular spatial system, not a collage of individually cut-out images. Visual style, footprint, navigation, interaction anchors, occlusion and character scale must agree.

## Core rules

1. All furniture uses one elevated 3/4 pseudo-3D perspective and one shared scale reference.
2. Furniture is authored as modular families. Kitchen cabinets, counters, stove, sink, prep and pass should visually connect through shared baseline, counter height, material language, perspective and lighting.
3. Gameplay collision must never be inferred directly from image alpha or decorative silhouette.
4. Each placeable object declares logical footprint, blocked cells, interaction points, required clearance, height class, Y-sort anchor and supported orientations.
5. Characters interact from explicit standing/sitting anchors. Never position employees by guessing from sprite pixels.
6. Tables and chairs are separate modules unless an authored booth is intentionally fixed.
7. New furniture is reviewed in assembled scenes, not only as isolated sprites.
8. Placement is grid-based with controlled arrangement. Invalid layouts that remove required interaction paths are rejected.
9. Decorative overhang may extend beyond the footprint without blocking navigation.
10. Furniture must match the approved character benchmark in scale, warmth, outline/detail density and material rendering.

## Benchmark logical grid

Initial logical grid target: `32 x 32` per cell. This is a demo benchmark, not a permanent production-resolution lock.

Example footprints:

- chair: 1x1
- small dining table: 2x2
- four-seat table: 3x2
- refrigerator: 1x2
- prep counter: 2x1
- range: 2x1
- pass counter: 2x1 or 3x1
- storage shelf: 2x1

## Required furniture definition

Each furniture asset should expose equivalent data to:

```yaml
id:
sprite_id:
footprint:
  width:
  height:
placement_type: floor | wall | overhead
height_class: floor | low | medium | tall | overhead
blocked_cells: []
interaction_points:
  staff: []
  guest: []
seat_points: []
attachment_points: []
item_anchors: []
required_clearance: []
y_sort_anchor:
supported_orientations: []
tags: []
```

Exact runtime format is a Technical Director decision; gameplay semantics must remain explicit and data-driven.

## Dining contract

Tables define valid chair attachment slots, plate anchors, server interaction point and cleaning point. Chairs define sitting anchor, facing direction and approach clearance. A seated character must align to the chair anchor and must not intersect the table body.

## Workstation contract

Kitchen and service stations define a working side, staff standing point, facing direction, input/output points and item-placement anchors. A work animation may visually reach over a counter, but the employee feet remain on a valid walkable interaction cell.

## Height and occlusion

- Floor: rugs and floor markings.
- Low: stools, chairs, low crates.
- Medium: tables, prep stations, service counters.
- Tall: refrigerator, tall cabinets, shelving.
- Overhead/wall: lamps, upper shelving, wall decor.

Characters are Y-sorted from feet. Tall furniture may occlude upper body only when spatially behind/in front as expected. Wrong foot occlusion is a blocker.

## Material language

Use a coherent family:

- warm dark wood for tables/counters/cabinetry;
- lighter warm wood for selected shelves/flooring;
- cream ceramic for tile/serviceware;
- brushed metal for kitchen appliances;
- deep olive upholstery/accent paint;
- restrained warm brass for handles/lights/trim.

Avoid isolated furniture with different camera elevation, outline style, light temperature or rendering density.

## Required demo set

Dining:
- 2-seat table
- 4-seat table
- dining chair
- booth/bench
- waiting bench

Kitchen:
- prep table
- range
- refrigerator
- sink
- dry-storage shelf
- plating/pass counter

Service:
- host stand
- cashier/service counter

Decor:
- floor plant
- wall plant
- menu board
- rug
- hanging lamp

## Acceptance tests

### Character interaction test
Place a benchmark character in front, behind, beside, seated and working. Reject incorrect body/furniture intersections.

### Dense dining test
Assemble a 4-seat table, chairs, neighboring table and staff walkway. Guests and staff must retain valid paths.

### Kitchen flow test
Assemble `Fridge -> Prep -> Range -> Pass`. Run one employee through the flow. Feet remain outside blocked cells and each animation aligns with its workstation anchor.

### Seam test
Connect multiple cabinet/counter modules. Shared countertop height, perspective, trim, lighting and contact shadows must read as a continuous built environment rather than separate cutouts.

### Rotation test
Validate each supported discrete orientation. No arbitrary rotation is required in the first demo.

### Visual review
Actual in-game screenshots are required. An isolated source image or successful import is not sufficient evidence.

## Current correction target

The present demo showed kitchen cabinets and dining furniture reading as individually pasted/cut-out assets, with mismatched character/furniture visual language and weak modular continuity. The next relevant restaurant visual pass must prioritize this contract before adding large furniture content volume.
