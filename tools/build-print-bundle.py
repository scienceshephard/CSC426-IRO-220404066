#!/usr/bin/env python3
"""Build the concise print document with the SVG diagrams embedded inline."""

from base64 import b64encode
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def png(name: str) -> str:
    data = b64encode((ROOT / "diagrams" / name).read_bytes()).decode("ascii")
    return f"data:image/png;base64,{data}"


REPORTING = png("UseCase-Reporting.png")
ADMIN = png("UseCase-Administration.png")
ISHIKAWA = png("Ishikawa.png")

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>IRO — CSC426 Submission Document</title>
<style>
@page {{ size:A4 landscape; margin:10mm; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:#19251f; font:10pt/1.34 Arial,Helvetica,sans-serif; }}
.page {{ }}
.diagram-page {{ page-break-before:always; page-break-after:always; break-before:page; break-after:page; break-inside:avoid; }}
h1 {{ margin:0 0 9pt; color:#153b35; font-size:22pt; line-height:1.08; }}
h2 {{ margin:11pt 0 5pt; color:#153b35; font-size:14pt; line-height:1.15; break-after:avoid; }}
h3 {{ margin:8pt 0 4pt; color:#31563d; font-size:11pt; break-after:avoid; }}
p {{ margin:4pt 0 7pt; }}
ul,ol {{ margin:4pt 0 7pt; padding-left:17pt; }}
li {{ margin:2pt 0; }}
table {{ width:100%; border-collapse:collapse; margin:5pt 0 8pt; }}
th,td {{ border:1px solid #cbd5cc; padding:4pt 5pt; text-align:left; vertical-align:top; }}
th {{ background:#eaf1e6; color:#20392b; }}
.eyebrow {{ color:#6c8668; font-size:8.5pt; font-weight:bold; letter-spacing:1.1pt; text-transform:uppercase; margin-bottom:6pt; }}
.meta {{ display:grid; grid-template-columns:1fr 1fr; gap:3pt 16pt; padding:8pt 10pt; background:#f1f5ed; border-left:3px solid #8ea879; margin:10pt 0; }}
.meta p {{ margin:0; }}
.linkbox {{ background:#f5f8f3; border:1px solid #d6e0d4; border-radius:5px; padding:7pt 9pt; overflow-wrap:anywhere; }}
a {{ color:#1d6541; text-decoration:underline; }}
.note {{ color:#53635a; font-size:9pt; }}
.warning {{ background:#fff6df; border-left:3px solid #d3ab4b; padding:6pt 8pt; margin:7pt 0; }}
.tight td,.tight th {{ padding:3pt 4pt; }}
.diagram-head {{ display:flex; justify-content:space-between; align-items:baseline; margin:0 0 5mm; }}
.diagram-head h2 {{ margin:0; }}
.diagram {{ width:100%; text-align:center; }}
.diagram img {{ width:1000px; height:auto; display:block; margin:0 auto; }}
.object strong {{ color:#153b35; }}
.small {{ font-size:9pt; }}
.section-label {{ color:#6c8668; font-size:8pt; font-weight:bold; letter-spacing:1pt; text-transform:uppercase; }}
</style>
</head>
<body>
<section class="page">
  <p class="eyebrow">CSC426 Weekly Dev · Weekend 3</p>
  <h1>IRO — Issues Reporting Outlet</h1>
  <p><strong>Student:</strong> Opeyemi Raphael-Ogbe &nbsp; <strong>Matric number:</strong> 220404066</p>
  <div class="meta">
    <p><strong>Document:</strong> Compact project submission</p><p><strong>Version:</strong> 1.1 · 19 October 2026</p>
    <p><strong>Audience:</strong> AAUA students and nearby residents</p><p><strong>Communities:</strong> Akungba, Iwaro, Etioro, Ayegunle</p>
  </div>
  <div class="linkbox"><strong>Live prototype:</strong> <a href="https://scienceshephard.github.io/CSC426-IRO-220404066/app/">https://scienceshephard.github.io/CSC426-IRO-220404066/app/</a><br>
  <strong>Public repository:</strong> <a href="https://github.com/scienceshephard/CSC426-IRO-220404066">github.com/scienceshephard/CSC426-IRO-220404066</a></div>
  <h2>1. Purpose and scope</h2>
  <p>IRO provides a proposed, structured route for students and local residents to report non-emergency campus and community issues, receive a reference, and follow safe status updates. A coordinator would review, categorize, route, and update reports. Public information must not expose a reporter or sensitive details.</p>
  <p>The submitted interface is a small front-end prototype. It demonstrates issue entry, validation, anonymity by default, a local reference, and a filterable issue board. It does not transmit reports, authenticate users, or provide a monitored complaint or emergency service.</p>
  <h2>2. Component interaction</h2>
  <p>Reporter selects a group, category, broad area, and urgency, then describes the issue → IRO validates and returns a reference → this prototype saves only in the browser → a future secure server routes the case to a coordinator → the coordinator publishes a safe status update.</p>
  <p class="note">The initial issue cards and sample survey responses are fictional. Do not enter real or urgent incident information into the prototype.</p>
</section>

<section class="page">
  <p class="section-label">Software Requirements Specification</p>
  <h1>3. System requirements</h1>
  <p><strong>Users:</strong> reporters (AAUA students and residents/indigenes), IRO coordinators, and system administrators. Coordinators and administrators require authenticated, role-checked access in a production deployment.</p>
  <h2>3.1 Functional requirements</h2>
  <table class="tight"><thead><tr><th>ID</th><th>Requirement</th><th>Scope</th></tr></thead><tbody>
    <tr><td>FR-01</td><td>Select reporter group, issue category, and broad area, including AAUA, Akungba, Iwaro, Etioro, and Ayegunle.</td><td>Prototype</td></tr>
    <tr><td>FR-02</td><td>Require a short title, description, and urgency; validate required fields and enforce length limits.</td><td>Prototype</td></tr>
    <tr><td>FR-03</td><td>Make anonymous reporting the default; display privacy guidance and require acknowledgment before saving.</td><td>Prototype</td></tr>
    <tr><td>FR-04</td><td>Save a practice report in local browser storage and show a reference; clearly disclose that it was not sent.</td><td>Prototype</td></tr>
    <tr><td>FR-05</td><td>Display sample/local reports without contact details and filter all, in-progress, and resolved items.</td><td>Prototype</td></tr>
    <tr><td>FR-06</td><td>Authenticate a coordinator; review scope, duplicates, sensitive details, and risk; categorize and assign a case.</td><td>Proposed</td></tr>
    <tr><td>FR-07</td><td>Record timestamped status changes and publish approved, non-identifying updates linked to a reference.</td><td>Proposed</td></tr>
    <tr><td>FR-08</td><td>Show authorized staff aggregate counts and suppress small or sensitive groups that could identify a person.</td><td>Proposed</td></tr>
    <tr><td>FR-09</td><td>Provide an anonymous needs-assessment questionnaire; analyze only consented real responses as community feedback.</td><td>Survey</td></tr>
  </tbody></table>
  <p class="note">“Prototype” requirements are demonstrated by the submitted front end. “Proposed” requirements need a secure server, database, coordinator workflow, and operational owner.</p>
</section>

<section class="page">
  <p class="section-label">Software Requirements Specification</p>
  <h1>4. Quality, data, and limitations</h1>
  <h2>4.1 Non-functional requirements</h2>
  <table class="tight"><thead><tr><th>Area</th><th>Requirement</th></tr></thead><tbody>
    <tr><td>Privacy</td><td>Collect the minimum information needed; anonymous by default; keep private notes and contact details out of public views.</td></tr>
    <tr><td>Security</td><td>Production case details require authenticated role access, HTTPS, protected storage/backups, and audit records. The local demo is not secure storage.</td></tr>
    <tr><td>Safety</td><td>State that IRO is not an emergency service. Add only a verified urgent contact route before production.</td></tr>
    <tr><td>Usability/accessibility</td><td>Plain language, visible labels, keyboard access, readable contrast, assistive-technology status feedback, and reduced-motion support.</td></tr>
    <tr><td>Responsive design</td><td>Support common mobile and desktop widths without horizontal page scrolling.</td></tr>
    <tr><td>Performance</td><td>Proposed public-page render target: under 3 seconds at the 95th percentile on broadband; measure after hosting.</td></tr>
    <tr><td>Integrity/maintenance</td><td>Production status changes are timestamped; categories and routing rules are controlled and documented.</td></tr>
    <tr><td>Availability</td><td>Production support hours and uptime target must be agreed with the responsible university/community organization.</td></tr>
  </tbody></table>
  <h2>4.2 Core data objects</h2>
  <p><strong>IssueReport:</strong> reference, group, category, broad area, title, description, urgency, status, created time, anonymity. <strong>StatusUpdate:</strong> report reference, status, public message, time, coordinator. <strong>Coordinator:</strong> account and role. <strong>SurveyResponse:</strong> pseudonymous response ID, group, broad area, and answers. Keep optional contact information separate and restricted in any production system.</p>
  <h2>4.3 Constraints</h2>
  <p>The demo uses HTML, CSS, JavaScript, and browser local storage. It has no server, authentication, notifications, file uploads, moderation, case assignment, or real status service. Browser storage may be visible to other users of the same browser profile. Production needs approved routing owners, privacy/retention rules, access control, secure storage, and a staffed response process.</p>
</section>

<section class="page">
  <p class="section-label">Questionnaire and problem analysis</p>
  <h1>5. Community needs assessment</h1>
  <p><strong>Audience:</strong> AAUA students and residents/indigenes of Akungba, Iwaro, Etioro, Ayegunle, and nearby areas. The anonymous questionnaire covers group and broad area, recent issues, issue types/frequency, reporting channels/barriers, privacy confidence, desired updates, response expectations, and optional non-identifying suggestions. It requests no name, matric number, phone, exact address, or email.</p>
  <div class="warning"><strong>Form status:</strong> The questionnaire and Google Apps Script are in the repository. A live Google Form responder URL must be generated by running <code>createIROSurvey</code> from a signed-in Google account before distributing the survey.</div>
  <h2>5.1 Simulated sample analysis</h2>
  <p>The CSV contains 15 fictional rows for coursework demonstration only; no community responses are claimed. Group mix: 9 students, 3 Akungba residents, and one each from Iwaro, Etioro, and Ayegunle. Issue types were multi-select, denominator 15.</p>
  <table class="tight"><thead><tr><th>Issue type</th><th>Count</th><th>Issue type</th><th>Count</th></tr></thead><tbody>
    <tr><td>Sanitation</td><td>10 (66.7%)</td><td>Roads</td><td>8 (53.3%)</td></tr>
    <tr><td>Safety</td><td>7 (46.7%)</td><td>Utilities</td><td>6 (40.0%)</td></tr>
    <tr><td>Facilities</td><td>5 (33.3%)</td><td>Communication</td><td>4 (26.7%)</td></tr>
    <tr><td>Transport</td><td>4 (26.7%)</td><td>Top barrier: do not know contact</td><td>8 (53.3%)</td></tr>
  </tbody></table>
  <p>Other simulated barriers: expect no follow-up 6/15; privacy concern 6/15; process takes time 4/15. Multi-select percentages may total over 100%. These fictional counts are not representative findings.</p>
  <h2>5.2 Ishikawa summary</h2>
  <p><strong>Effect investigated:</strong> fragmented, delayed, and unsafe reporting, with low trust and weak follow-up. Possible causes are people (awareness/ownership/fear), process (separate channels/no references), technology (accessibility/connectivity), governance and trust (unclear privacy/response owner), communication (no updates), and resources/environment (staff, funds, distance, infrastructure). Validate these hypotheses with genuine feedback.</p>
</section>

<section class="page">
  <p class="section-label">Use-case specification</p>
  <h1>6. Actors and main use cases</h1>
  <p><strong>Actors:</strong> Reporter (AAUA student or resident), IRO Coordinator, and System Administrator. Figures 1–2 show reporting and status tracking, coordinator review/routing/updates, aggregate summaries, and administrative access/category management. The detailed use-case narratives and editable draw.io files are in the repository.</p>
</section>

<section class="page diagram-page">
  <div class="diagram"><img src="{REPORTING}" width="1000" alt="Figure 1. Use-case diagram: reporter and IRO coordinator"></div>
</section>

<section class="page diagram-page">
  <div class="diagram"><img src="{ADMIN}" width="1000" alt="Figure 2. Use-case diagram: system administration"></div>
</section>

<section class="page diagram-page">
  <div class="diagram"><img src="{ISHIKAWA}" width="1000" alt="Figure 3. Ishikawa fishbone problem analysis"></div>
  <p class="note">Potential causes are hypotheses for validation, not measured community findings.</p>
</section>

<section class="page">
  <p class="section-label">Object listing and source references</p>
  <h1>7. Objects and code</h1>
  <table class="tight"><tbody>
    <tr><td><strong>ReportForm</strong><br>Captures group, category, broad area, title, description, urgency, and privacy acknowledgment.</td><td><strong>IssueReport</strong><br>Reference, category, broad area, title, description, status, date, urgency, anonymity/sample flags.</td></tr>
    <tr><td><strong>LocalReportStore</strong><br>Stores practice reports in browser <code>localStorage</code>; not a secure shared database.</td><td><strong>IssueBoard</strong><br>Renders safe report fields, counts, and status filters.</td></tr>
    <tr><td><strong>StatusUpdate</strong><br>Proposed status, public message, time, and coordinator reference.</td><td><strong>Coordinator / Category</strong><br>Proposed authenticated staff role and controlled issue category.</td></tr>
    <tr><td><strong>SurveyResponse</strong><br>Pseudonymous survey record; included sample rows are simulated.</td><td><strong>IRO API / Database</strong><br>Proposed server validation, protected storage, access checks, references, and audit history.</td></tr>
  </tbody></table>
  <h2>Code and project links</h2>
  <ul>
    <li><strong>Live website:</strong> <a href="https://scienceshephard.github.io/CSC426-IRO-220404066/app/">scienceshephard.github.io/CSC426-IRO-220404066/app/</a></li>
    <li><strong>Full repository:</strong> <a href="https://github.com/scienceshephard/CSC426-IRO-220404066">github.com/scienceshephard/CSC426-IRO-220404066</a></li>
    <li><strong>Web source code:</strong> <a href="https://github.com/scienceshephard/CSC426-IRO-220404066/tree/main/app">app/ (HTML, CSS, JavaScript)</a></li>
    <li><strong>Google Forms creation script:</strong> <a href="https://github.com/scienceshephard/CSC426-IRO-220404066/blob/main/google-forms/CreateIROForm.gs">CreateIROForm.gs</a></li>
    <li><strong>Editable diagrams and full SRS:</strong> <a href="https://github.com/scienceshephard/CSC426-IRO-220404066/tree/main/diagrams">diagrams/</a> · <a href="https://github.com/scienceshephard/CSC426-IRO-220404066/blob/main/docs/SRS.md">SRS.md</a></li>
  </ul>
  <p class="warning"><strong>Printing note:</strong> This compact document embeds all three diagrams. The long source listing is not printed; the code is available at the links above. Print this document at 10 pt. Survey results in the CSV are simulated, not community feedback.</p>
</section>
</body></html>'''

output = DOCS / "SUBMISSION-PACK.html"
output.write_text(html, encoding="utf-8")
print(f"Wrote {output.relative_to(ROOT)} with inline SVG diagrams and no printed source listing")
