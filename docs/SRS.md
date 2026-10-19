# Software Requirements Specification

## IRO — Issues Reporting Outlet

| Document item | Value |
|---|---|
| Course | CSC426 Weekly Dev – Weekend 3 |
| Student | Opeyemi Raphael-Ogbe |
| Matric number | 220404066 |
| Version | 1.0 |
| Prepared | 19 October 2026 |
| Product type | Coursework web prototype and proposed system |
| Live prototype | [GitHub Pages demo](https://scienceshephard.github.io/CSC426-IRO-220404066/app/) |

## 1. Introduction

### 1.1 Purpose

This SRS specifies IRO, a proposed web-based service for reporting and following non-emergency issues concerning Adekunle Ajasin University students and nearby residents/indigenes, including Akungba, Iwaro, Etioro, and Ayegunle. It describes the actors, data, interfaces, functional requirements, and quality requirements needed for implementation and review.

### 1.2 Scope

IRO is intended to give community members one structured route to report an issue, receive a reference, and see safe status information. Coordinators review, categorize, route, and update reports. Public summaries must avoid disclosing the identity of the reporter or sensitive incident details.

The submitted mini interface is a static browser prototype. It demonstrates form validation, a sample issue board, filters, and browser-local storage. It has no server, account system, notifications, or operational coordinator workflow. All initially displayed reports are fictional. The Google Forms questionnaire is a separate needs-assessment artifact, and the included sample response data is simulated.

IRO is not an emergency reporting service, police service, medical service, or substitute for existing official contact channels. The prototype must not be used to submit a real or urgent report.

### 1.3 Intended readers

The intended readers are the course lecturer, student developer, prospective IRO users, and a future implementation team. This document supports coursework review and future design discussion; it is not an authorization to deploy the service.

### 1.4 Definitions

| Term | Meaning |
|---|---|
| Reporter | A student or community member who submits an issue. |
| Coordinator | An authorized person who reviews and routes incoming reports. |
| Issue report | A structured description of a non-emergency concern and its broad area. |
| Public update | A response/status message cleared for display without private reporter data. |
| Sensitive data | Information that identifies a person, reveals private circumstances, or creates safety/privacy risk. |
| Synthetic response | A fictional record used to demonstrate analysis; it is not community evidence. |

## 2. Overall description

### 2.1 Product perspective

The proposed service has a public reporter interface and a restricted coordinator interface backed by an authenticated server. A future production version would store reports in a protected database and expose only approved status messages and aggregate statistics. The coursework prototype instead runs fully in one browser and uses `localStorage` for submitted practice entries.

### 2.2 User classes

| User class | Goals | Proposed access |
|---|---|---|
| AAUA student | Report campus/shared-area issues and follow a case. | Public submission and status view. |
| Community resident/indigene | Report local infrastructure, sanitation, utility, transport, or service issues. | Public submission and status view. |
| IRO coordinator | Assess safety, classify, route, and update reports. | Authenticated case-management functions. |
| System administrator | Manage coordinator access and approved categories/areas. | Restricted configuration functions. |

The current prototype implements only a local report-entry form and a display board. It does not authenticate any of the proposed roles.

### 2.3 Operating environment

- Current prototype: modern desktop or mobile browser with JavaScript and local storage enabled; no server installation required.
- Proposed deployment: HTTPS web application, server-side application/API, protected database, authenticated coordinator accounts, backups, and a documented support/response process.
- The interface should remain usable on common mobile screen sizes and with keyboard navigation.

### 2.4 Constraints and assumptions

- Reports are non-emergency and within an agreed university/community service scope.
- The responsible university/community offices and coordinator roles must be identified before deployment.
- Collect only information needed to route and resolve an issue.
- The live survey must be reviewed and shared by the student with real participants; simulated records must not be presented as field responses.
- In the prototype, records are local to the browser and can be deleted by clearing its site storage.

## 3. System features and functional requirements

Requirements marked **Prototype** are implemented in the static demo. Requirements marked **Proposed** define the operational system and are not implemented in this coursework front end.

### 3.1 Submit an issue report

- **FR-01 — Reporter group (Prototype):** The interface shall allow a reporter to select a group, including AAUA student, Akungba, Iwaro, Etioro, Ayegunle, and other community member.
- **FR-02 — Issue details (Prototype):** The interface shall require an issue category, broad area, short title, and description before saving a report.
- **FR-03 — Urgency (Prototype):** The interface shall allow the reporter to mark a report Routine, Soon, or Urgent. The interface shall state that it is not monitored and is not suitable for emergencies.
- **FR-04 — Privacy reminder (Prototype):** Before saving, the interface shall show a warning against entering names, contact details, exact addresses, medical details, or identifying allegations and require acknowledgment of that warning.
- **FR-05 — Anonymous default (Prototype):** The reporter shall be anonymous by default. A contact field shall appear only after the reporter turns anonymity off; contact details are never required.
- **FR-06 — Local save (Prototype):** The browser prototype shall save submitted practice entries in the current browser's local storage and show the generated reference. It shall clearly state that the report was not transmitted to any authority.
- **FR-07 — Server submission (Proposed):** A deployed system shall transmit a valid report to a server over HTTPS and return a non-identifying reference number.
- **FR-08 — Validation (Prototype):** Required fields shall be validated in the browser; title and description shall have length limits.

### 3.2 Review and case management

- **FR-09 — Coordinator authentication (Proposed):** A coordinator shall authenticate before accessing private case details.
- **FR-10 — Triage (Proposed):** A coordinator shall review a new report for scope, duplicates, sensitive content, and immediate risk before routing it.
- **FR-11 — Categorize and assign (Proposed):** A coordinator shall assign an approved category and responsible unit to a report.
- **FR-12 — Status updates (Proposed):** A coordinator shall change the status among Received, Under Review, Assigned, In Progress, Resolved, and Closed, and record a timestamped internal note.
- **FR-13 — Public response (Proposed):** A coordinator shall publish an approved, non-identifying update associated with a report reference.
- **FR-14 — Duplicate handling (Proposed):** A coordinator shall link duplicate reports while preserving their individual references and protecting reporter details.

### 3.3 Status and summary views

- **FR-15 — Public status view (Prototype):** The prototype shall display sample/local issues and their status, category, broad area, reference, and date without displaying reporter contact details.
- **FR-16 — Status filters (Prototype):** The prototype shall let a visitor filter the issue board to all, in-progress, or resolved reports.
- **FR-17 — Private status lookup (Proposed):** A deployed system shall let a reporter use a reference plus an appropriate verification method to view their report's approved status without exposing another person's report.
- **FR-18 — Aggregate summary (Proposed):** An authorized coordinator shall be able to view counts by category, area, and status. Small groups and sensitive categories shall be suppressed where disclosure could identify a person.

### 3.4 Needs-assessment questionnaire

- **FR-19 — Anonymous survey (Proposed):** The Google Form shall explain its purpose and voluntary nature, avoid collecting email addresses or direct identifiers, and ask about respondent group, broad area, issue types, reporting barriers, and preferred follow-up.
- **FR-20 — Survey analysis (Coursework artifact):** The coursework shall distinguish any genuine survey responses from synthetic sample responses and state the denominator used in each percentage.

## 4. External interface requirements

### 4.1 User interface

The public interface shall use plain language, visible labels, keyboard-operable controls, a mobile layout, confirmation/status feedback, and clear privacy/emergency notices. Sensitive internal notes and reporter identity shall not appear on the public board.

### 4.2 Software interfaces

- **Prototype:** HTML, CSS, vanilla JavaScript, and browser `localStorage`; no external API.
- **Proposed production version:** HTTPS API, database, identity provider for staff, notification provider only if approved, and audit logging. Interface formats and vendors remain design decisions.
- **Questionnaire:** Google Forms generated by the supplied Apps Script; respondent and editor links are logged by Google Apps Script.

### 4.3 Communications interfaces

The production system shall use HTTPS for browser/server traffic. Notifications shall contain the reference and a minimal status message, not sensitive incident details. The prototype sends no network requests for report submission.

## 5. Data requirements

### 5.1 Core entities

| Entity | Key attributes | Notes |
|---|---|---|
| IssueReport | reportId, group, category, broadArea, title, description, urgency, status, createdAt, anonymous | Production identity/contact fields, if needed, must be separate and access-restricted. |
| StatusUpdate | updateId, reportId, status, publicMessage, createdAt, coordinatorId | Internal notes and public messages must be separate fields with separate permissions. |
| Category | categoryId, label, active | Controlled by an administrator. |
| Coordinator | coordinatorId, accountId, role, active | Authentication and account lifecycle are proposed, not in the demo. |
| SurveyResponse | responseId, respondentGroup, broadArea, answers | Questionnaire response; no direct identifier requested. Aggregate before sharing. |

### 5.2 Data minimization and retention

The deployed service shall request a broad area rather than an exact address unless the response process proves more precision is necessary. It shall not require a name or contact channel for a general report. Any optional contact detail shall be kept apart from public data and deleted under an approved retention schedule. The SRS cannot set the final retention period until the responsible organization establishes its policy.

## 6. Non-functional requirements

- **NFR-01 — Privacy:** Anonymous reporting shall be the default. Public views and analytics shall exclude direct identifiers and private coordinator notes. Collection shall be limited to operationally necessary fields.
- **NFR-02 — Access control:** In production, only authenticated, authorized coordinators may view private case details. Privileged actions shall be recorded in an audit log. The coursework prototype provides no such security boundary and must use fictional/local data only.
- **NFR-03 — Transport/storage security:** A deployed service shall use HTTPS, secure server-side storage, protected backups, and credential management appropriate to the hosting environment.
- **NFR-04 — Usability:** A first-time user should be able to identify the report action, understand required fields, and receive a save/confirmation message without specialist training.
- **NFR-05 — Accessibility:** Interactive elements shall have labels, support keyboard use, expose status messages to assistive technology, preserve readable contrast, and respect reduced-motion preferences.
- **NFR-06 — Responsiveness:** The public interface shall adapt from a 360-pixel-wide mobile viewport to desktop without horizontal page scrolling.
- **NFR-07 — Performance:** On a normal broadband connection, the deployed public landing page should render its main content within 3 seconds at the 95th percentile; this target requires measurement after hosting.
- **NFR-08 — Availability:** A production service should define an availability target and support hours with the responsible organization before launch. The local coursework demo has no uptime guarantee.
- **NFR-09 — Maintainability:** Categories, areas, and status labels should be documented and changed through controlled configuration rather than duplicated ad hoc across screens.
- **NFR-10 — Integrity:** The production service shall timestamp state changes, prevent unauthorized edits, and preserve a traceable status history.
- **NFR-11 — Safe communication:** The UI shall explain that it is not an emergency service and shall identify an approved urgent contact route before production. Until that route is confirmed, no unverified contact number shall be shown.
- **NFR-12 — Data handling:** Genuine survey results shall not be mixed with synthetic coursework data. Reports shall be analyzed with clear denominators and caveats.

## 7. Major component interactions

1. The reporter opens the public form, selects a group and broad area, enters a minimal description, and chooses urgency/anonymity.
2. The public interface validates required fields and shows the privacy and non-emergency notice.
3. In the coursework prototype, JavaScript writes a practice record to this browser's local storage, renders a reference, and updates the local board.
4. In a proposed production deployment, the public interface would send the report to an HTTPS API. The server would validate it, store it, and issue a reference.
5. An authenticated coordinator would inspect the new case, check scope/duplicates/safety, assign category and responsible unit, and create a status update.
6. The public status view would reveal only the approved status and non-identifying response. A coordinator dashboard would show protected detail and aggregate counts according to role.
7. The Google Forms questionnaire independently gathers voluntary needs-assessment feedback. Only genuine answers may be described as community survey results.

## 8. Use-case references

The use-case diagram source files are [`../diagrams/UseCase-Reporting.drawio`](../diagrams/UseCase-Reporting.drawio) and [`../diagrams/UseCase-Administration.drawio`](../diagrams/UseCase-Administration.drawio). The narrative and preconditions are in [`USE-CASES.md`](USE-CASES.md).

## 9. Acceptance criteria

The coursework prototype is acceptable when a reviewer can open the static page; select a reporter group, category, broad area, title, description, and urgency; acknowledge the privacy notice; save a report locally; see a confirmation/reference; find the entry on the board; filter the board; and distinguish synthetic sample cards from practice entries. The associated SRS, survey package, Ishikawa diagram, use-case diagrams, object listing, and source listing shall be present in the repository.

Production acceptance additionally requires approved ownership/routing, privacy and retention rules, authentication and access controls, secure server-side storage, tested backup/recovery, accessibility review, and a staffed response procedure. Those requirements are outside this mini prototype.

## 10. Limitations and future work

The demo is single-browser and client-only; its local storage is not a secure case-management database. It does not provide authentication, actual delivery, assignment, moderation, attachments, status subscriptions, email/SMS alerts, audit records, or an operational SLA. Next steps are to collect and analyze real consented feedback, confirm responsible offices and emergency alternatives, obtain privacy/security review, implement a backend and role-based coordinator workflow, and test accessibility and usability with representatives of both user groups.

## 11. References

- CSC426 Weekly Dev – Weekend 3 assignment brief supplied for this coursework (01/07/26).
- Google Apps Script Forms Service reference: [Google for Developers](https://developers.google.com/apps-script/reference/forms).
- Project artifacts: [`../google-forms/QUESTIONNAIRE.md`](../google-forms/QUESTIONNAIRE.md), [`ISHIKAWA-ANALYSIS.md`](ISHIKAWA-ANALYSIS.md), and [`USE-CASES.md`](USE-CASES.md).
