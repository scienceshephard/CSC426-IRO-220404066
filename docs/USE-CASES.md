# IRO use cases

## Actors

| Actor | Description |
|---|---|
| Reporter | AAUA student or community resident/indigene submitting or following an issue. |
| Coordinator | Authorized staff/community representative triaging cases and publishing safe updates. |
| System administrator | Person configuring categories, areas, and coordinator access. |

The reporter and coordinator interactions are shown in `UseCase-Reporting`; privileged configuration is shown in `UseCase-Administration`. The `.drawio` files are editable in diagrams.net (draw.io); SVGs are previews.

## UC-01 — Submit an issue

**Primary actor:** Reporter. **Goal:** Record a non-emergency issue with enough detail for routing.

**Preconditions:** Reporter can open the public page and understands it is not an emergency channel.  
**Trigger:** Reporter selects “Report an issue.”

**Main flow:**

1. IRO displays the privacy and scope notice.
2. Reporter selects their broad group, issue category, and community/campus area.
3. Reporter provides a short title, description, and urgency.
4. IRO validates required fields and confirms the privacy acknowledgment.
5. Reporter leaves anonymity enabled (default) or optionally provides contact information in a production system.
6. IRO stores the report and returns a reference number.
7. IRO displays the next safe status/action.

**Alternative/exception flows:** Missing fields are highlighted; an invalid entry is not saved. If the report concerns imminent danger, IRO tells the reporter not to rely on this non-emergency service and to use a verified official emergency channel. If a report includes identifying/sensitive details, a production coordinator may restrict it and request a safe redaction; the prototype only displays a warning.

**Prototype note:** Steps 2–6 work in the browser, but “store” means `localStorage` in that browser. The report is not transmitted to anyone.

## UC-02 — Review and route a report

**Primary actor:** Coordinator.

**Preconditions:** Coordinator is authenticated and has permission for the case queue. A new report exists.

**Main flow:** Coordinator reviews the description and broad area, checks scope and duplicate reports, identifies sensitive content or risk, selects an approved category, assigns the responsible unit, records an internal note, and moves the report to Under Review or Assigned. Private notes remain restricted.

**Exceptions:** Out-of-scope reports are closed with an approved explanation; urgent safety concerns follow an approved escalation procedure; a duplicate is linked to an existing case without removing its own reference.

## UC-03 — Publish a status update

**Primary actor:** Coordinator. **Supporting actor:** Reporter/public visitor.

**Preconditions:** A report exists and the coordinator has reviewed the proposed update.

**Main flow:** Coordinator selects a status, writes a factual public update without names or sensitive details, previews the public display, and publishes. IRO records the author and timestamp. A reporter looks up their reference to read the approved status.

## UC-04 — View aggregate issue summary

**Primary actor:** Coordinator.

**Preconditions:** Coordinator is authenticated with summary access; reports exist.

**Main flow:** Coordinator selects a time range, area, category, or status. IRO returns aggregate counts and suppresses small or sensitive groups where a person could be identified. It does not display private narratives or contact fields in the summary.

## UC-05 — Configure categories and access

**Primary actor:** System administrator.

**Preconditions:** Administrator has authenticated with a privileged account.

**Main flow:** Administrator updates an approved category/area list or coordinator role, confirms the change, and IRO records an audit event. Access is removed promptly when a coordinator leaves the role.

## UC-06 — Provide needs-assessment feedback

**Primary actor:** Student/community survey participant.

**Preconditions:** Participant has opened the separate anonymous Google Form and read its consent statement.

**Main flow:** Participant chooses whether to consent; if consenting, answers questions about group, broad area, issue types, reporting barriers, privacy concerns, and desired follow-up; optionally gives a non-identifying suggestion; submits the form. The student analyzes only consented genuine responses as community feedback.

**Coursework data note:** `data/synthetic-responses.csv` is fictional practice data, not responses from this use case.
