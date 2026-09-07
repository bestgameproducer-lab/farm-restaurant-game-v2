# Restaurant vertical slice

Status: delegated reversible demo defaults under the owner's restaurant-first decision. Counts/timings below are fixture parameters, not final balance. Target a 15–30 minute demonstrable session; do not simulate years to force future stories into it.

## VS-01 Minimum scope

One small Western restaurant, high readable 2D management view. Four two-seat tables, one entrance/exit, waiting point, storage, prep station, stove, pass and clear walk lanes. Start with one chef and two servers; offer one controlled recruitment opening from the sample candidates. Three simple recipes with explicit finite stock. No farm map; supplies are an explicit demo inventory fixture.

Pause/1x/2x; start/close service; inspect staff/orders; set duties/priority and a temporary override. Fixed layout first; object footprints/access points are real so later constrained placement is possible.

## VS-02 Observable loop

Enter -> reserve a valid seat -> navigate/sit -> order -> queue food -> reserve ingredients/station -> prep/cook -> food ready -> pickup -> serve correct table -> eat -> pay exactly once -> exit -> table dirty -> clean/release. Keep intermediates minimal but observable. No teleporting work or infinite ghost ingredients.

State ownership must cover concurrent seat reservations, job reservations, cancellation, unreachable targets, absent workers, insufficient stock and close-of-service draining. Failed jobs release resources; repeated callbacks cannot duplicate revenue or consume stock twice. A carrying worker visibly holds a prop; job text must agree with actual animation/state.

## VS-03 Employee identity proof

Profiles show portrait/name/role/known skills/salary/traits/current work. One candidate includes a legitimate estimated skill and undisclosed goal; evidence must not leak truth. Demonstrate one hidden-information reveal triggered by observed work and one career/shift support choice whose effect can be seen. No complete career tree, families, rarity generator or title-election system yet.

## VS-04 Acceptance

- Launch on the recorded Godot 4 version; no parser/runtime errors during the fixed test scenario.
- Complete at least 20 deterministic orders without double payments, negative stock, permanent reservations or stuck paths.
- Pause freezes simulation time and all simulation-owned timers; UI inspection still works.
- A blocked station/job produces an understandable reason and safe recovery.
- Higher-priority work or a temporary override visibly affects selection, without violating reservations/eligibility.
- Staff are selectable; profession silhouettes readable; furniture bounds/work points do not overlap illegally.
- At 1280x720 and 1920x1080, essential panels/buttons are readable, reachable and not overlapping. Test 16:9 first; other aspect ratios get a documented fallback.
- Save/reload supported demo state reproduces money, stock, staff and order ownership. A safe-boundary save may be an explicitly documented first step, not misrepresented as arbitrary-time support.
- Provide real rendered screenshots and a short captured sequence; a generated concept image is not execution evidence.
- Gameplay reviewer describes one meaningful choice and measured before/after consequence. Visual reviewer reports concrete defects or checks. Owner playtest remains necessary to judge appeal.

## VS-05 Delivery gates

G0 data/core bootstrap; G1 spatial and character runtime benchmark; G2 autonomous operating loop; G3 employee-facing identity/decision; G4 integrated playtest build. Continue automatically between passing tasks under policy. At G1 the reviewer may choose reversible technical sprite defaults; owner approval is required before replacing visual identity or treating them as final production standards.

## Deferred

Farming/animals, procedural maps, general free building, complex inventory pricing, loans campaign, full title branches, full relationships/romance/households, aging/death/generations, localization production, multiplayer, paid AI assets and brand-licensed content.
