# Save boundary contract

Version every save. Persist stable ids, simulation time/seed, changing staff state, employment, acquired knowledge, inventory/reservations, orders/seats/job ownership, ledger and resolved event/choice ids for the implemented slice. Static definitions are referenced by id/revision, not duplicated as changing runtime objects. Never persist UI nodes or absolute machine paths.

Unknown future version => readable refusal, not silent corruption. Missing optional fields get explicit defaults. Migrations are separate tested functions and retain a backup. A save with hidden employee truth is game-internal data; UI must still use the knowledge projection (this is not cryptographic anti-cheat secrecy).

Test a canonical snapshot round trip and interrupted order/hiring behavior. Use safe-boundary save first only if the task explicitly scopes that limitation. Never claim arbitrary-time save support from a menu-only test.
