# Employee system — consolidated design

Status: long-term design baseline. Mechanism directions come from owner discussion; formulas, content volume and thresholds are not final. Only the subset in `RESTAURANT_VERTICAL_SLICE.md` is currently executable scope.

## EMP-D01 Core experience

Hire a person with incomplete information. Observe work and hidden value. Support or decline ambitions. Grow skills and professional status. Form attachments over time. Keep a costly loyal veteran, replace them, arrange a successor or create a different role: no choice is always optimal. Employees make their own significant life decisions from goals, circumstances, relationships and player history.

## EMP-D02 Shared model and non-overlapping concepts

Farm/restaurant use one employee framework. Separate immutable content definition, actual runtime person, employment/contract, public knowledge/assessments, visual presentation and save state.

| Concept | Purpose | Not equivalent to |
|---|---|---|
| XP / personal level | General accumulated working experience and growth | Professional qualification |
| Professional skills | Task-specific mastery through work/training/mentoring | Universal character level |
| Profession | Current field of work | Current organizational appointment |
| Title / qualification | Career recognition with requirements and assessments | Automatic level reward |
| Appointment / authority | Duties and management permissions in this organization | Age or certification alone |
| Career branch | Specialization and new responsibilities | More identical stat boosts |
| Talent / potential | Unusual capability or growth profile | Guaranteed current performance |
| Happiness / fatigue | Short-term state and sustainable workload | Long-term loyalty |
| Loyalty / trust | Relationship with the organization/player | Eternal obedience |
| Professional reputation | External recognition and credible achievements | Company rating |
| Development choices | Deliberate specializations; loyalty can unlock opportunities | A mandatory extra currency for every subsystem |

Level may increase baseline capability; task skills must still govern specialist work. High-level servers do not automatically become competent chefs. Exact attribute growth, caps, training cost and loyalty-point mechanism remain proposals, not frozen rules.

## EMP-D03 Recruitment and rarity

Combine coherent archetype + controlled random variation + background + traits + goals + fixed authored characters. Do not generate mutually contradictory traits without an intentional story. Rarity describes an uncommon combination, special skill, potential or story, not universal superiority. Ordinary employees can become exceptional contributors. Rarity, transparency, assessment difficulty and deception are separate properties. Final rarity names, colors and probabilities are open; no paid gacha system is assumed.

Sample archetypes: talented sensitive cook, diligent server who dreams of cooking, experienced conservative farmer, seemingly ordinary team anchor, overstated resume with genuine ability, observant future manager. Templates create reusable stories; individual characters use the same systems.

## EMP-D04 Signature resume and personnel file

Three distinct layers: candidate claims; manager evidence/annotations; continuing personnel record after hiring. Portraits, career history, desired salary, work hours, verified achievements and accessible skills must be legible. Notes/stamps/underlines establish identity but cannot obscure decision-critical data. The original resume remains in history while assessments change; training, promotions, promises, events and departure accumulate over years.

Known information states: uninvestigated, insufficient evidence, estimated, suspected, verified, privately withheld, event-only. Avoid one wall of question marks. State what evidence is missing and what can reveal it. Current skill observations expire or update as people learn; a verified historic claim remains historic, not forever-current capability.

## EMP-D05 Truth, observations and deception

Keep actual values, employee claims, manager estimates, evidence source, confidence and assessment time separate. Unknown is null/absent, not zero. UI receives an explicit whitelisted public profile; never pass hidden truth to the UI and merely hide controls.

Uncertainty may come from little experience, self-assessment, biased references, assessment error or deliberate misrepresentation. Deliberate deception is limited and motivated, not every applicant falsifying every field. The system may support distortion across recruitment fields, but each case targets a coherent subset. Hidden information can be good or bad. Avoid punishments with no clues/counterplay. Practical work, records, interviews and trial periods supply evidence.

## EMP-D06 Managers and automated investigation

Player sets hiring policy, budget and priorities; managers investigate automatically and report. Example policies: fast, standard, deep, talent-first, stability-first. Manager skill improves evidence gathering, estimate precision and discovery speed, not omniscient access to secrets. Shared talent-management branches: investigation, assessment, practical evaluation, career planning, mentor matching and conflict handling. Farm/restaurant add domain specialisms. Without a manager, basic recruitment still works with less information.

Loyalty encourages disclosure of private goals and willingness to discuss careers. Observable work must reveal capability even for a disloyal employee. Do not hide every skill until a loyalty threshold. Trial employment costs and dismissal rules remain balancing decisions.

## EMP-D07 Careers and titles

Careers have branches and shared skills. Example cook directions: research, quality, throughput, cuisine specialization, leadership. Server directions: service speed, guest relations, training, management. Farm directions: crops, livestock, mechanization, quality, operations.

Promotion can require personal level, a skill group, achievements, reputation, loyalty/recommendation and periodic evaluation. The owner proposed quarterly title assessment with a chance of success. Separate external qualification from internal appointment: whether loyalty gates a credential or only sponsorship is an unresolved decision; do not silently choose.

Show eligibility, missing preparation and assessment evidence. Probability is not arbitrary dice; failures give feedback and maintain prior progress. Salary expectations can change with status without automatic unaffordable raises. Exact title names and ladders in earlier conversation were examples.

A server can seek chef training; the player bears coverage/training cost, arranges mentoring and makes offers. The employee can accept, delay or seek opportunities elsewhere. Preserve prior experience/relationships without granting unrelated mastery. Loyalty-based development opportunities remain planned; do not delete them just because XP also exists.

## EMP-D08 Work autonomy and sustainable growth

Staff select eligible unreserved jobs using enabled duties, skill, urgency, priority, availability and reachable locations. A temporary player override returns to autonomy after success/failure/cancellation; it cannot bypass missing qualifications or unreachable targets. Inspect current action, selection reason and blockers.

Work/training/events grant XP; corresponding work develops skills. Happiness may support effort and learning, but fatigue/overwork prevents an infinite happy-overtime XP exploit. Family pressure may increase willingness without eliminating costs. Balance should include diminishing returns and recovery, not reward abuse as universally optimal.

## EMP-D09 Relationships and teamwork

Full directional network among meaningfully acquainted people: A's trust/affinity/respect for B can differ from B's for A. Sparse storage does not weaken the design; create records upon interaction and update on events/shifts, not all pairs every frame. Mentor/apprentice, friend, rival, conflict, lover, spouse and kin are tags with constraints.

Private affection and domain teamwork familiarity differ. Professional rivals may work well. Daily efficiency is the primary operational effect through handoff, help, teaching, leadership acceptance, communication and recovery. Downstream effects may reach all systems through explicit interfaces, not ubiquitous direct reads of relationship matrices. No generic unexplained company-wide family/relationship modifier.

Player shapes schedules, teams, mentoring, working conditions and conflict policy rather than clicking each pair to increase affection. Explain material effects with examples and recorded interactions.

## EMP-D10 Goals, economy and agency

People have different motives: achievement, change, stability, relationships, life balance, mission, independence or legacy. Goals evolve. Personal economy abstracts income, costs, savings, pressure and ambitions; no full private transaction simulation. Financial information is not automatically public.

Relationships influence priorities. Marriage can create a household context but preserves individual identities, careers, autonomy and loyalties. Major decisions weigh personality, goals, finances, relationships, happiness, loyalty, external offers and fulfilled/broken promises. Player choices change conditions, not guarantee obedience. Managers may provide uncertain explanatory assessments. Record promise deadlines and fulfillment as durable events.

## EMP-D11 Romance, family and generations

Employees can fall in love, marry and form families. Effects on efficiency/careers are contextual, not a spouse speed buff. Family events directly affect the involved employee/household; organizational impacts occur via actual absence, choices and work. Do not simulate a private-life world beyond management relevance.

Children begin as lightweight background identities with age/household/interests; no child employees or player-controlled childhood training. At adult working age, generate an independent candidate where relevant. A still-employed parent may recommend them; a manager may discover their resume. Career is autonomous, not inherited deterministically; application and quality are not guaranteed. Record family relationship and independent assessment to make possible conflicts legible. Working-age threshold is a fictional content rule to decide before implementation, not a legal claim.

## EMP-D12 Aging, departure and legacy

Visual aging, role, title, outfit and personality are independent. Older employees are not automatically managers or mentors; young managers and older apprentices must be representable. Age may change physical work preference/capacity, while experience, stability, teaching and knowledge can retain value. Do not assign universal decline at an unapproved birthday.

Resignation, retirement and eventual death are allowed. Different departures can improve or damage the organization. Hidden contributions must have causal evidence: mentoring, guest relationships, conflict prevention, coverage or unique knowledge. Not every ordinary veteran secretly becomes optimal.

Retirement commonly has notice, reduced-hours discussion, succession and final ambitions. Death should be respectful and not frequent random punishment; detailed presentation remains open. Legacies may include recipes, methods, trained successors, memories or outside contacts. Organizationally learned recipes are not deleted just because their inventor departs; actual mastery/unique dependencies must be modeled explicitly.

## EMP-D13 Events

Shared data-driven operational, personal, career and world events. Challenges include difficult guests, regulars, festivals, shortages and evaluations. Each event needs trigger context, involved actors, choices, eligibility, effects, employee resolution, recurrence limit and history. Store resolution outcome/random seed for save reproducibility; reopening an event must not apply effects twice. Limit simultaneous interruptions; ordinary updates may enter a digest while only consequential choices interrupt play.

## EMP-D14 Production limits

First demo: small named fixture cast, skill/traits, observable jobs, XP/happiness, one uncertain resume field, one reveal and one management decision. Everything else remains this design plus optional future data boundaries—not empty fully simulated subsystems. Asset volume and eventual staff count are still open. Do not implement a full relationship/household/year engine merely because this document describes them.
