# IRO object listing

This list distinguishes objects implemented in the static prototype from objects required by a future multi-user system.

| Object | Type | Main attributes/responsibility | State / relationships |
|---|---|---|---|
| `IROPage` | Browser page | Renders the landing page, privacy notice, report form, and issue board. | Contains form and board sections. |
| `IssueReport` | Data object | `id`, `category`, `area`, `title`, `description`, `status`, `date`, `urgency`, `reporterGroup`, `anonymous`, `sample`. | Created by form or supplied as fictional sample data. |
| `ReportForm` | UI component | Captures group, category, area, title, description, urgency, anonymity, and consent. | Validates and creates an `IssueReport`. |
| `LocalReportStore` | Browser storage adapter | Reads/writes practice reports under key `iro-demo-reports-v1`. | Uses browser `localStorage`; one browser only, not protected server storage. |
| `IssueBoard` | UI component | Renders safe report fields and counts; filters all, in-progress, and resolved entries. | Reads `IssueReport` objects; does not expose reporter contact details. |
| `StatusLabel` | UI value | Displays Received, In progress, or Resolved on prototype cards. | In production, status history belongs to `StatusUpdate`. |
| `SurveyResponse` | Coursework data record | Synthetic CSV row with pseudonymous sample ID, respondent group, broad area, multi-select issue types/barriers, frequency, and expected update. | All rows carry `Simulated`; never evidence of actual participants. |
| `Coordinator` | Proposed domain object | Authorized user who reviews, classifies, assigns, and updates a case. | Requires authenticated account/role; absent in prototype. |
| `StatusUpdate` | Proposed domain object | `updateId`, report reference, status, public message, timestamp, coordinator reference. | Linked to `IssueReport`; public and internal text must have separate access rules. |
| `Category` | Proposed domain object | Approved category ID, label, active flag. | Managed by an administrator and referenced by a report. |
| `IRO API` | Proposed service | Validates server-side requests, stores reports, returns references, and enforces permissions. | Not present in the static prototype. |
| `ReportDatabase` | Proposed persistence object | Stores report and status records under a retention and access policy. | Not present in the static prototype. |

## Implemented prototype behavior

`app/app.js` defines the fictional sample report array and creates report records from `FormData`. It reads/writes the local store, escapes text before rendering report cards, computes counts, and filters by status. It deliberately does not send report data over the network.
