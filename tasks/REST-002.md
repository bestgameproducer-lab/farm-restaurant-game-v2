# REST-002 — workstations, reservations and autonomous staff

Status: Backlog. Dependency: REST-001 spatial contract; actual visual approval may remain a separate blocker for visual delivery, not domain tests. Owner: gameplay_engineer. Reviews: game_designer + QA.

Implement reachable workstation slots, one authoritative job board, eligibility checks, task reservation/release, deterministic priority tie-breaking, worker runtime transitions and temporary override. No customer/order engine yet: use controlled fixture jobs that visibly carry a prop/work.

Acceptance: two workers cannot claim the same exclusive job/slot; completion/cancel/unreachable target releases ownership; pause stops work progression; override respects qualifications/access and returns to autonomy; inspection gives current job, selection reason and blockers. No every-frame full-repo logic or random walking to fake autonomy. Allowed: game/domain/jobs/, game/services/, game/scenes/restaurant_demo/, tests/jobs/, reports/. Map exact allowed files before changes; one writer to core files.
