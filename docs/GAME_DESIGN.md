# Game design baseline

Read only relevant sections. `docs/DECISIONS.md` separates owner decisions from delegated demo assumptions.

## GD-01 Controls and time

Mouse management; pause available at any time. Farm and restaurant share time and allow view switching. Staff work without constant instruction. UI-specific auto-pause, acceleration factors, exact calendar and off-line progress are not frozen. First demo offers pause/1x/2x and no off-line progress as reversible defaults. Paused production, order patience, fatigue and expenses must use the same paused simulation clock.

## GD-02 Spatial contract

Logical footprint, interaction points, collision, navigation and render bounds are separate. Every placeable object declares occupied grid cells and accessible work/use slots. Sprite size does not decide occupancy. Field cells each represent one plot. Farm expansion unlocks explicit regions. Restaurant starts with a fixed validated layout; future constrained grid placement uses zones and legal access. Never repair overlap merely by changing draw order. Foot-based sorting handles rendering, not path validity.

## GD-03 Farm-to-table loop

Seeds/animals + labor + land + facilities -> ingredient batches -> stock -> menu/recipe feasibility -> cooking -> service -> guest experience -> revenue/reputation -> staffing, training and expansion -> new production demand. Ingredient quality contributes to dish outcome but does not replace cooking skill, equipment or service. Menu choices must feed back into production planning. First demo uses explicit finite stock, not a hidden full farm simulation.

## GD-04 Restaurant identity and progression

Build a distinctive restaurant through menu, ingredients, staff specialisms, service and decor; unlock customer types and recipes. The owner requires stronger chefs/better ingredients to open recipe opportunities and restaurant progression to gate recruitment tiers. Hiring and internal training are both valid. Exact level thresholds, exceptional hiring events and recipe discovery/research/mastery phases require later balancing; do not silently hard-code earlier example values as approved numbers.

## GD-05 Employee pillar

See `EMPLOYEE_SYSTEM.md`. A reliable ordinary employee, a difficult genius, a hopeful career changer and an apparently low-output veteran must all have credible value. Grade, rarity, current skill, potential, honesty and loyalty are different concepts. Individual assets/names used in fixtures are sample content, not final casting.

## GD-06 Pressure and human tone

Slow, decision-rich management. Wages, capacity, supply and eventual debt create opportunity costs, not unavoidable rapid clicking. Debt amount/deadline/failure are open; do not implement punishment from inference. Customers, regulars, difficult encounters, festivals and professional evaluations create staff challenges. A management choice should have visible reasons and reversible learning opportunities where possible.

## GD-07 Data flow ownership

Definitions -> runtime instances -> authoritative services -> public read models -> UI. Events carry ids/context, not references to UI nodes. Recruitment claims/assessments never overwrite true capability. Family events directly affect involved individuals/household only; organization consequences flow through availability, choices, work and relationships. Relationships modify concrete interactions rather than arbitrary global percentage buffs.

## GD-08 Scope

The authoritative current implementation scope is `RESTAURANT_VERTICAL_SLICE.md`. Long-term design is not a task backlog. New systems need a distinct player purpose and owner before implementation. Reuse existing ownership; avoid two inventories, two clocks or independent farm/restaurant employee engines.
