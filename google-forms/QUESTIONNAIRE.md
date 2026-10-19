# IRO community questionnaire

## Purpose and audience

This anonymous needs-assessment survey is for AAUA students and residents/indigenes of Akungba, Iwaro, Etioro, Ayegunle, and nearby communities. It explores common issue types, existing reporting routes, privacy concerns, and useful follow-up. It is not a channel for filing a live complaint.

## Opening and consent text

> IRO (Issues Reporting Outlet) is a proposed coursework system for reporting and following non-emergency campus and community issues. This questionnaire is voluntary and should take about 3–5 minutes. Do not provide your name, phone number, exact address, medical information, identifying allegations, or other sensitive details. The form does not collect email addresses. Your answers will be summarized for a CSC426 coursework prototype. They will not be used to investigate an individual case. If you do not wish to participate, close the form.

Consent question (required): **I understand the purpose above and choose to provide anonymous feedback.**

- Yes, I consent to take part
- No, I do not consent

If the selected option is “No,” the form owner should exclude that response from analysis. Do not publish the response-level sheet.

## Questions

1. **Which group best describes you?** (multiple choice; required) AAUA student; Akungba indigene/resident; Iwaro indigene/resident; Etioro indigene/resident; Ayegunle indigene/resident; other nearby community member; prefer not to say.
2. **Which broad area are you answering about?** (multiple choice; required) AAUA campus; Akungba-Akoko; Iwaro; Etioro; Ayegunle; other nearby area; prefer not to say.
3. **In the past six months, have you experienced or witnessed an unresolved community or campus issue?** (multiple choice; required) Yes; no; not sure; prefer not to say.
4. **Which issues have you experienced or witnessed?** (checkboxes; optional) Roads and transport; water and electricity; sanitation and waste; safety and security; facilities and maintenance; student services; communication or delayed updates; other; prefer not to say.
5. **How often do issues that need attention affect your area?** (multiple choice; required) Weekly or more often; about monthly; a few times a year; rarely; not sure; prefer not to say.
6. **What makes it difficult to report an issue or get follow-up?** (checkboxes; optional) Do not know the right contact/channel; privacy concern; retaliation concern; expect no response/update; process takes too much time; unreliable internet/access; have not had a reason to report; other; prefer not to say.
7. **How would you most likely raise an issue today?** (multiple choice; required) Tell a representative/community leader; contact a university/community office; phone call/message; group/social media post; would not report; prefer not to say; other (free-text option).
8. **How confident would you feel using a reporting service that does not require your name?** (multiple choice; required) Very confident; somewhat confident; neither confident nor concerned; somewhat concerned; very concerned; not sure.
9. **Which follow-up would be most useful?** (multiple choice; required) Reference number/status page; message when status changes; public summary with no reporter details; direct coordinator response; no follow-up; other (free-text option).
10. **How soon should a coordinator acknowledge a non-emergency report?** (multiple choice; required) Within one working day; within three working days; within one week; within two weeks; not sure.
11. **Which features would make the service useful to you?** (checkboxes; optional) Anonymous reporting; clear issue categories; safe broad location; reference number; progress updates; way to correct/add context; urgent safety contact point; other.
12. **Anything else?** (paragraph; optional) Suggest improvements without naming people or including identifying details.

## Setup and distribution

The companion [`CreateIROForm.gs`](CreateIROForm.gs) script creates these questions in Google Forms, leaves email collection off, and logs the responder and editor links. To create the live questionnaire, follow the steps in the repository README. Review consent settings and the published form yourself before sharing it with the community. Do not distribute the synthetic data file as actual survey results.

## Data handling

- Do not ask for names, matric numbers, phone numbers, exact addresses, or specific incident evidence.
- Restrict editor access to the student and lecturer as needed. Share only aggregate summaries.
- Remove any response that contains unsolicited sensitive information before analysis or publication.
- Use a real response sheet only for genuine answers. The CSV included with this assignment is simulated for demonstration.
