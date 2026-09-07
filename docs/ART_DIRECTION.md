# Art direction — demo approval

## ART-01 Approved intent

Owner approved the latest restaurant and character benchmark for demo use. Warm Japanese-inspired cozy art, elevated mostly frontal/top-down-readable room, clear plan and movement lanes, cute memorable employees, less clutter than early bistro illustrations. Olive/leaf colors, friendly shapes and gentle paper-like UI are benchmark motifs, not a final commercial name.

## ART-02 Source versus production

Assets listed by `assets/approved/manifest.json` are visual-reference sheets/images. They are NOT tested Godot sprite atlases, separated clothing layers, complete animation loops or a navigable restaurant. Do not infer exact pixel dimensions or frame counts from text drawn into a generated sheet. Frames can have inconsistent scale and anatomy.

Allowed: visual targeting, reference display, documented static portrait/crop placeholders after inspection. Not allowed: claiming a screenshot with baked-in characters is a live playable scene; moving duplicate characters over baked figures; treating random rows as coherent animation; claiming clothing swap works because one overview contains several outfits.

## ART-03 Direction to preserve

High camera and clear footprint layout. Readable profession through silhouette, tools and clothing, not palette alone. Character identity through face/hair motif/accessory, with meaningful mature/older facial changes. Age does NOT assign title, profession or personality. Older apprentice and younger manager must remain possible. Owner explicitly requested greater age/profession distinction; current benchmark is a demo direction, not proof that this test passes.

## ART-04 Runtime experiment

First validate ONE character in ONE real scene with idle/walk/carry/serve, consistent camera/anchors and separate props. Proposed test canvas 64x96 with approx 48x64 character is NOT frozen. Compare native-size legibility and cost before scaling to the full cast. Pixel-art world, smooth-painted portraits and UI may use different import settings; do not force nearest filtering on every image.

## ART-05 Cosmetic extensibility

Keep outfits/accessories and small themed decoration replaceable. This is technical compatibility only. No Hello Kitty or other third-party licensed character/artwork is included or authorized. Do not generate/ship branded collaboration assets as though a deal exists.

## ART-06 Acceptance

Actual scene screenshots; consistent foot anchors; no frame jitter, baked UI, stray sheet labels, unhandled backgrounds or incorrect mirror of asymmetrical accessories. Approve runtime assets separately from benchmark references. Store source/generation identity, edits, status and content hash.
