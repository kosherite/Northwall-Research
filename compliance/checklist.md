# Pre-publication checklist

The supervisory-analyst copies this list into `compliance/checklists/<date>_<T>_<DocType>_checklist.md`, records evidence for each item, and ends with `DECISION: APPROVED` or `DECISION: BLOCKED — <reasons>`.

| # | Check | CFA Standard |
| --- | --- | --- |
| 1 | `tools/build_model.py` passes all integrity checks with no formula errors | V(A) |
| 2 | `tools/check_report.py` passes: target and implied return in the text match the model | V(A), I(C) |
| 3 | Every hard input used in the report has a source in `model_inputs.yaml` | V(A), V(C) |
| 4 | Prices and their dates are stated and match the tracker | V(B) |
| 5 | Facts are attributed to filings; estimates are labelled as Northwall's | V(B) |
| 6 | The rating follows the return bands and the target derivation is shown | I(B), V(B) |
| 7 | Risks name what would make the call wrong, sized where possible | V(B) |
| 8 | No text, figures, charts or estimates taken from another firm's research | I(C) |
| 9 | Holdings register checked; any position in the name is disclosed | VI(A) |
| 10 | Any reference to the CFA Program uses candidate wording only | VII(B) |
| 11 | Rating or target change logged in `rating_pt_log.csv` | V(C) |
| 12 | File named `<YYYY-MM-DD>_<T>_<DocType>_v<X.Y>.pdf` | Firm policy |
