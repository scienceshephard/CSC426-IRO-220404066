# Printing and physical submission

The lecturer's brief asks for the SRS, use-case diagrams, Ishikawa diagram, object listing, and code listing to be printed at **10 pt** after the email is acknowledged.

## Suggested print order

1. [`SRS.md`](SRS.md)
2. [`USE-CASES.md`](USE-CASES.md), followed by both diagram previews from `../diagrams/`
3. [`ISHIKAWA-ANALYSIS.md`](ISHIKAWA-ANALYSIS.md), followed by `../diagrams/Ishikawa.svg`
4. [`OBJECT-LISTING.md`](OBJECT-LISTING.md)
5. [`CODE-LISTING.txt`](CODE-LISTING.txt)

Open [`SUBMISSION-PACK.html`](SUBMISSION-PACK.html) in a browser and print at 100% scale; its print stylesheet sets body and code text to **10 pt** and places the wide fishbone on a landscape page. Regenerate the source listing and print bundle after edits with `python3 tools/build-code-listing.py` and `python3 tools/build-print-bundle.py` from the repository root. The Google Form script and simulated CSV can be added as appendices if required.

Keep the email draft unsent until the repository and, if required, the live Google Form have been reviewed and the lecturer has acknowledged receipt. The assignment brief gives a deadline of 10 July 2026; this package is being prepared after that date.
