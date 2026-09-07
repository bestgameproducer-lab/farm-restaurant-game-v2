# REST-001 — real spatial/visual benchmark

Status: Backlog (Producer may mark Ready after EMP-001). Owner: technical_artist with scoped engineer assistance. Review: visual_reviewer + QA.

Read RESTAURANT_VERTICAL_SLICE VS-01/04, ART_DIRECTION, CHARACTER_ASSET_CONTRACT C3/C6, approved manifest and ARCHITECTURE A4. Build one real Godot room, not a full-image fake screenshot. Fixed four-table layout with logical occupancy, separate walkable lanes/use points, foot anchors and one moving character. Placeholder assets allowed only if recorded; preserve target visual direction. Avoid using background with baked characters under moving duplicates.

Show debug occupancy/access overlays, an idle/walk/carry/serve test and pause. Report exact export cell/pivot/frame durations and inspect native target scale. Do not claim age/outfit full modular support until swaps are tested. Capture real scene at 1280x720 and 1920x1080; art reviewer flags scale, overlap, silhouette and frame jitter. If native render unavailable, keep visual gate NOT VERIFIED while independent data work continues.

Allowed: game/scenes/restaurant_demo/, game/presentation/, assets/runtime/demo/, tests/spatial/, reports/. Do not overwrite assets/approved originals. Major visual redesign requires owner; reversible test dimensions do not.
