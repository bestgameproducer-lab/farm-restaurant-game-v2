# One authoritative owner per state

| State | Logical owner | Consumers | First demo |
|---|---|---|---|
| Time/pause/speed | SimulationClock | jobs, patience, growth, service | yes |
| Staff actual runtime | EmployeeRegistry | employment, simulation | yes |
| Employee claims/knowledge | RecruitmentKnowledge | public profile builder | narrow subset |
| Public employee info | CandidateProfile projection | recruitment/UI | yes |
| Job state/reservations | JobBoard | workers/debug UI | yes |
| Money / transactions | Ledger | service/hiring/HUD | minimal |
| Stock/reservations | Inventory | recipes/order service | minimal |
| Seats/workstation occupancy | SpatialRegistry | seating/navigation/jobs | yes |
| Orders/payments lifecycle | OrderService | kitchen/service/customers | yes |
| UI navigation/modal state | UIController | views | yes |
| Asset presentation | CharacterPresenter | render scenes | yes |
| Relationship graph | RelationshipService | teamwork/events | later |
| Careers/qualifications | CareerService | jobs/training/recruitment | later |
| Household/background people | LifeContext | individual goals/events | later |
| Event history/promises | EventLedger | employee decisions/read models | one sample |
| Save format | SaveService | domain owners | scoped |

Names are proposed logical ownership, not a demand for singleton classes. The same small module may own several closely related rows initially if it preserves boundaries. Review any new owner against this table to avoid duplication.
