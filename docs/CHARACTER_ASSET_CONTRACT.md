# Character asset contract — provisional technical benchmark

## C1 Independent axes

Identity (face/hair signature) + visual age stage + outfit + profession equipment + expression + animation + direction. Age does not unlock management clothing. Outfit cannot silently change profession/qualification. The same identity must match portrait and world sprite.

## C2 Deliverable types

- Identity reference: front/side/back, key motifs, age/outfit exploration; not runtime.
- Portrait: transparent or intentionally framed head/bust, consistent crop; native resolution recorded.
- World sprite: actual RGBA source frames/atlas, uniform cells, pivots and named clips.
- Optional layered source: body/clothing/hair/accessory/prop layers aligned to the same rig/frame index. Do not claim modularity without testing swaps during motion.

## C3 First runtime test

One adult server; front/back/left/right. Start with idle 2–4 unique frames, walk 6, carrying reusing validated walking legs with prop/arm layer, serve 4-frame one-shot; rest/talk may use static poses plus restrained secondary motion. These counts are reversible defaults, not a requirement to generate hundreds of frames immediately. Right/left mirroring only where hairclip, badge and handedness remain acceptable; otherwise distinct direction frames.

Candidate canvas 64x96; visual person approx 48x64; floor logical units independent of pixels. Pivot example bottom-center with padding is only a proposal until tested. Set exact exported pivot/cell/frame duration/loop flags in the manifest; no implicit guessing. Professional station/tools are separate props, not baked into the person.

## C4 Age and outfit proof

Test youth/adult/mature/older portraits with consistent identity and clearly different age cues beyond grey hair. World changes may use hair, face, posture and optional glasses—not arbitrary universal slowness. Compare server apron/tray, chef coat/headwear, manager tailored workwear/file, farmer utility clothing/boots. Validate multiple age x outfit pairs; do not produce the full combinatorial cross-product before this works.

## C5 Expressions

Prioritize neutral, warm smile, happy, thinking, worried, sad, tired, surprised, embarrassed, determined; anger/frustration added when scene requires. Do not draw expressions for every outfit/age combination up front. Portrait expression is different from a world animation state.

## C6 Export record

For each runtime asset: id, source reference, export path, dimensions, cell size, alpha, pivot, directions, clip frames/durations/loop, layer order, outfit/age compatibility, filtering, revision/hash, test scene and review status. Godot SpriteFrames/AnimationPlayer resources are generated only from verified entries. Disallow border bleeding, missing alpha, mislabeled repeated poses and claims of true animation from static crops.
