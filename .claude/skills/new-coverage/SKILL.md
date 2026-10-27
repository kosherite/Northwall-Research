---
name: new-coverage
description: Initiate Northwall coverage of a new company (for example "/new-coverage K92 Mining"). Researches the company, builds the sourced input file and model on the right archetype, writes the initiation and one-pager, and takes them through compliance.
---

# New coverage: $ARGUMENTS

1. **research-associate**: collect the last annual and latest quarterly filings, guidance, reserves or asset data, share data and two or three peers. Save sources under `coverage/<T>/sources/`.
2. **financial-modeler**: choose an archetype (or write a new one, see the modeler agent); create `coverage/<T>/model_inputs.yaml` with every reported value sourced and every judgement marked "Northwall assumption"; build the model; all checks except the "published" ones must pass (there is no published target yet, so set `published:` from the analyst's first answer).
3. **equity-analyst**: set forecasts and multiples following `docs/CFA_Modelling_Framework.md`; write the thesis, valuation, numbered catalysts and risks, and choose three exhibits that prove the thesis (one chart, one peer table, one estimates or sensitivity table). Create `reports/<T>/onepager.yaml`.
4. **supervisory-analyst** reviews; **publishing-desk** publishes as `<date>_<T>_Initiation_v1.0.pdf` or `OnePager`.

Add the name to `data/event_calendar.csv` with its next results date.
