# How Northwall builds a model: the CFA framework

Northwall models follow the sequence the CFA Program teaches in Level II Equity Valuation and Financial Statement Analysis. Every step below names the curriculum topic it comes from and the place it lives in a Northwall workbook.

## The sequence

| Step | CFA Level II topic | What we do | Where it lives |
| --- | --- | --- | --- |
| 1. Understand the business | Equity: Industry and Company Analysis | Identify the few drivers that explain revenue and cost: volume, price, unit cost, capital intensity | Model sheet, top section |
| 2. Forecast the drivers | Equity: Industry and Company Analysis (forecasting) | Revenue = volume × price; costs split into variable (per unit) and fixed; capital split into sustaining and growth | Inputs (blue) → Model |
| 3. Anchor to reported numbers | FSA: Evaluating Quality of Financial Reports | Load reported actuals with their source; use H1 actual + H2 estimate so the forecast starts from what the company reported | Inputs, Model columns H1-26A / H2-26E |
| 4. Adjust for reporting quality | FSA: Integration of FSA Techniques; Quality of Financial Reports | Use adjusted earnings only when the adjustment is explained; check cash conversion (OCF / NI); flag accrual build-ups | Ratios sheet |
| 5. Analyse returns | FSA: Integration of FSA Techniques (DuPont) | ROE = margin × turnover × leverage; ask whether returns are earned by margin, asset use or debt | Ratios sheet |
| 6. Set the required return | Equity: Return Concepts; Corporate Issuers: Cost of Capital | CAPM cost of equity (rf + β × ERP); WACC at market weights; real discount rates for asset-life NAV | Valuation, first block |
| 7. Choose the valuation model that fits the cash flows | Equity: FCF Valuation; Residual Income; Market-Based Valuation; DDM | Resource companies: asset-life NAV (a finite-horizon DCF) plus a cash-flow multiple. Cross-check with FCFF DCF, residual income and justified P/E | Valuation, NAV |
| 8. Price the market's expectations | Equity: DDM / FCF (reverse Gordon) | Solve for the growth rate today's price implies and compare it with the forecast | Valuation, cross-check 2 |
| 9. Test the conclusion | Equity: Industry and Company Analysis (scenario and sensitivity) | Grids on the two target multiples and on WACC × terminal growth; commodity deck scenarios in the report | Sensitivity |
| 10. Communicate fact vs. opinion | Ethics: Standards V(A), V(B), V(C) | Every input sourced; estimates labelled as Northwall's; model versions kept | Inputs source column, Log, Checks |

## Why each model choice was made

**Revenue as volume × price.** The curriculum's preferred forecasting approach for commodity businesses is driver-based rather than a growth rate on last year's revenue. For producers the volume is ounces, barrels or boe; for a royalty company it is gold-equivalent ounces (GEOs).

**Sustaining vs. growth capital.** FCFF and FCFE require fixed-capital investment to be forecast explicitly. Separating sustaining capital (needed to stand still) from growth capital (optional) shows how much cash the business generates before it chooses to grow.

**NAV for resource companies.** Mines and oil reserves deplete, so a Gordon-growth terminal value overstates them. The curriculum's multistage FCF model with a finite horizon is the right tool: the NAV sheet discounts asset-life cash flows at a real rate and adds net cash and investments. This is a sum-of-the-parts approach.

**Why the target is not the DCF.** Mining equities trade on P/NAV and P/CF in practice, so the target blends those two (the method of comparables). The two-stage FCFF DCF, residual income model and justified P/E sit beside it as cross-checks (the method based on forecasted fundamentals). When they disagree, the report says why. Franco-Nevada is the clearest example: its price implies about 4% perpetual growth, well above what the cash flows support on their own.

**Residual income where it is meaningful.** Residual income values a firm from book value plus the PV of earnings above the cost of equity. The curriculum favours it when free cash flow is negative or dividends are small. It is built for the gold names, where book value is modelled; for the oil names cash flow models carry the analysis.

**Justified P/E.** P/E = payout / (r − g), with g = retention × ROE. When g ≥ r the model returns "n/m", which is itself a lesson: single-stage models fail for high-ROE companies, so multistage models are needed.

## House modelling standards

1. **Separate inputs, calculations and outputs.** Inputs sheet only for typed numbers; Model and Valuation are formulas; Cover shows outputs.
2. **Colour code.** Blue typed input, black formula, green link to another sheet, yellow fill for key assumptions.
3. **Every input has a source.** Filing and page, or "Northwall assumption" with the reasoning.
4. **No hard-coded numbers in formulas.** A rate or multiple lives in its own input cell.
5. **Integrity checks must pass.** The Checks sheet ties the model to the published report; the build fails if any check fails.
6. **Version, never overwrite.** Each quarter is a new file (`<date>_<TICKER>_Model_v<YYYY>Q<n>.xlsx`); the Log sheet records every change and its effect on the target.

## Year-end roll-forward

The period columns are set in `tools/engine.py` (`PERIODS`). After Q4 results, the Financial Modeler rolls them forward (2026A, H1-27A, H2-27E, 2027E … 2031E), moves reported 2026 numbers into the 2026A inputs and extends the forecast a year. Within the year, Q3 actuals are entered by splitting H2-26E into Q3 actual plus Q4 estimate in the input's source note.
