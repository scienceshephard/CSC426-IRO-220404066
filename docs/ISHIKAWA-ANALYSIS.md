# Ishikawa problem analysis

## Effect to investigate

**Students and local residents cannot reliably report and follow up on shared campus/community issues through one trusted, safe route.** The proposed effect is a problem statement for analysis; it is not a measured finding from a completed community survey.

The editable fishbone diagram is [`../diagrams/Ishikawa.drawio`](../diagrams/Ishikawa.drawio); [`../diagrams/Ishikawa.svg`](../diagrams/Ishikawa.svg) is its preview.

## Cause branches

| Branch | Possible contributing causes |
|---|---|
| People | Residents/students may not know which office owns an issue; reporters may fear blame or retaliation; responsibilities between campus and community actors may be unclear. |
| Process | Reports arrive through unrelated calls, chats, and in-person conversations; there may be no standard minimum information; case references, routing, and close-out steps may be inconsistent. |
| Technology | People may have limited data/device access; digital channels may be inaccessible; separate channels may not share a queue or status history. |
| Governance and trust | Privacy expectations and retention rules may be unknown; no defined owner may be accountable for an update; the boundary between public facts and private details may be unclear. |
| Communication | Feedback may not reach the reporter; notices may be scattered across groups; a reporter may not know whether the issue was received, assigned, or resolved. |
| Resources and environment | Staff/funds to respond may be limited; transport, weather, or infrastructure conditions can complicate investigation; issue volume may exceed the capacity of the responsible team. |

## Coursework data analysis (simulated)

The included file contains **15 fictional rows** created to demonstrate analysis. No community survey was sent or answered in creating these rows. Respondent mix: 9 students (60%), 3 Akungba residents (20%), and 1 each from Iwaro, Etioro, and Ayegunle (6.7% each). The small sample is illustrative only and is not representative.

Issue types were multi-select; each percentage below uses **15 simulated respondents** as the denominator, so totals can exceed 100%:

| Simulated issue type | Count | Percent |
|---|---:|---:|
| Sanitation | 10 | 66.7% |
| Roads | 8 | 53.3% |
| Safety | 7 | 46.7% |
| Utilities | 6 | 40.0% |
| Facilities | 5 | 33.3% |
| Communication | 4 | 26.7% |
| Transport | 4 | 26.7% |

Reporting barriers were also multi-select (denominator 15):

| Simulated barrier | Count | Percent |
|---|---:|---:|
| Do not know the right contact | 8 | 53.3% |
| Expect no follow-up | 6 | 40.0% |
| Privacy concern | 6 | 40.0% |
| Process takes time | 4 | 26.7% |
| Retaliation concern | 2 | 13.3% |
| Unreliable internet | 1 | 6.7% |

Six fictional respondents selected weekly issue frequency, six selected monthly, and three selected rarely. These are properties of the simulated CSV only, not evidence about the community.

## Design implications

The prototype uses broad area choices, anonymous-by-default reporting, a privacy reminder, a non-emergency notice, required structured fields, a local reference, and a status board that omits contact details. A production version would also need authenticated coordinator access, a reviewed privacy/retention policy, a documented routing owner, and an agreed update target. A genuine needs assessment with consent and broader participation is required before treating these priorities as community findings.
