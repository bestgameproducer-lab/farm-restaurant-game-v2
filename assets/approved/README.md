# Demo-approved visual references

Owner approval: the latest restaurant and character benchmarks may guide the demo. Approval concerns the visual direction, not technical readiness as game assets.

## What is actually included

- `restaurant_reference_preview.jpg`: 320 x 180 JPEG thumbnail of the approved restaurant reference.
- Character reference: 320 x 240 JPEG thumbnail, transported as four checked base64 fragments in `../encoded/character_reference_preview/`. Run `python tools/materialize_assets.py` from the repository root to produce `character_reference_preview.jpg`. This performs no network request and never overwrites a different existing image.
- `manifest.json` records source identities, exact hashes, resolutions, and delivery status.

These small previews communicate composition, proportions and broad color direction. They are NOT adequate for pixel-perfect extraction, detailed age comparison, production portraits, UI typography, or animation frames.

## Full-resolution sources

The original PNGs were retained in the ChatGPT source bundle, not uploaded to this repository in the initial bootstrap:
- restaurant_demo_benchmark_v1.png — 1672 x 941
- character_demo_benchmark_v1.png — 1448 x 1086

When that optional source bundle is attached to the local Codex session, unpack it and run `python tools/import_benchmarks.py --source PATH_TO_SOURCE_DIRECTORY`. The importer checks the approved hashes before copying to `assets/approved/source/`. Commit those files on a task branch; do not claim they exist before import succeeds.

## Usage contract

Use the restaurant reference as a mood/layout target, not as a playable room with characters painted into its background. Build proper floor, furniture footprints, navigation, interaction points and actual moving staff.

Use the character sheet as an identity/style reference. It is not a uniformly gridded atlas. Age and profession are independent visual axes; captions pairing an age with a job do not impose a career rule. Create labelled temporary runtime assets until clean, aligned, transparent frames or rigs pass runtime review.

UI must be real controls, not the text painted into a concept image. No third-party collaboration characters or brand marks are authorized by these references. Source approvals never imply a third-party license or final production approval.
