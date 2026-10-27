---
name: earnings-review
description: Run the Northwall earnings-review workflow for one covered ticker after it reports quarterly results (for example "/earnings-review AGI"). Loads actuals, updates the model, writes the review and takes it through compliance to publication.
---

# Earnings review: $ARGUMENTS

Target: published within 24 hours of the results release.

1. **research-associate**: save the release, MD&A and statements to `coverage/<T>/sources/<YYYY-Qn>/`; load actuals into `model_inputs.yaml` with sources; write `variance.md` (actual vs. our estimate for volume, price, unit cost, capital, cash flow); list guidance changes.
2. **financial-modeler**: bump `company.version`, run `python tools/build_model.py <T>`. If a check now fails only because actuals moved published estimates, report it; do not change the check targets.
3. **equity-analyst**: decide which forecasts change and why; edit the "Northwall" inputs with reasons and a `log` row; rebuild; read the new target, return and band rating from `outputs.json`. Write the review in `reports/<T>/onepager.yaml` (lead: what beat or missed, what changed in our numbers, rating reaffirmed or changed). Update `published:` only after approval.
4. **supervisory-analyst**: review the draft (`python tools/build_onepager.py <T>`) and sign or block.
5. **publishing-desk**: publish, log, update tracker, commit.

Finish with a three-line summary: result vs. estimate, estimate and target change, rating.
