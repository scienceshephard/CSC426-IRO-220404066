# IRO — Issues Reporting Outlet

**CSC426 Weekly Dev – Weekend 3**  
**Student:** Opeyemi Raphael-Ogbe  
**Matric number:** 220404066

**Public repository:** [github.com/scienceshephard/CSC426-IRO-220404066](https://github.com/scienceshephard/CSC426-IRO-220404066)

**Live prototype:** [scienceshephard.github.io/CSC426-IRO-220404066/app/](https://scienceshephard.github.io/CSC426-IRO-220404066/app/)

IRO is a coursework prototype for reporting and following community issues involving Adekunle Ajasin University students and residents of Akungba, Iwaro, Etioro, Ayegunle, and nearby communities.

## Open the prototype

Open [`app/index.html`](app/index.html) in a browser. The report form works locally in that browser and saves entries to `localStorage`. The issue cards included on first load are fictional examples. This is a front-end demonstration: reports are not sent to a server or to university/community authorities.

## Submission contents

- [`app/`](app/) — mini web interface.
- [`google-forms/`](google-forms/) — anonymous questionnaire and Apps Script that creates it in the user's Google account.
- [`data/synthetic-responses.csv`](data/synthetic-responses.csv) — explicitly simulated sample data for the coursework analysis.
- [`diagrams/`](diagrams/) — editable draw.io Ishikawa and use-case diagrams, with SVG previews.
- [`docs/SRS.md`](docs/SRS.md) — Software Requirements Specification.
- [`docs/USE-CASES.md`](docs/USE-CASES.md) — actors and use-case narratives.
- [`docs/OBJECT-LISTING.md`](docs/OBJECT-LISTING.md) — object listing.
- [`docs/ISHIKAWA-ANALYSIS.md`](docs/ISHIKAWA-ANALYSIS.md) — problem analysis and sample-data interpretation.
- [`docs/PRINTING.md`](docs/PRINTING.md) — font-size-10 printing checklist.
- [`docs/SUBMISSION-PACK.pdf`](docs/SUBMISSION-PACK.pdf) — nine-page, 10 pt print document with all three diagrams embedded.
- [`docs/SUBMISSION-PACK.html`](docs/SUBMISSION-PACK.html) — self-contained HTML source for the print document.
- [`docs/EMAIL-DRAFT.md`](docs/EMAIL-DRAFT.md) — email text to use after the repository and Google Form are ready.
- [`tools/build-code-listing.py`](tools/build-code-listing.py) — generates the combined source listing at `docs/CODE-LISTING.txt`.

## Create the Google Form

1. Open [script.google.com](https://script.google.com/) while signed into the Google account that should own the form.
2. Create a project, replace its starter code with `google-forms/CreateIROForm.gs`, then run `createIROSurvey`.
3. Approve Google's requested Forms permissions. The execution log prints the responder and editor links.
4. Review the form before sharing it. The included CSV is synthetic and should not be uploaded as if it were community feedback.

## Limitations

This prototype has no server, user accounts, authentication, role-based access, file uploads, notifications, or real case management. Do not enter real names, contact details, exact home addresses, or urgent/sensitive incident details. A production deployment needs a reviewed privacy notice, secure storage, access controls, retention rules, and a staffed response process.

## Project structure

```text
app/                 Static prototype
data/                Simulated response data
diagrams/             Editable draw.io source and SVG previews
docs/                 Assignment documentation
google-forms/         Questionnaire and Google Apps Script
tools/                Code-listing generator
```
