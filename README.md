# Northwall Research

Independent equity research on North American precious metals and energy, run as a one-analyst sell-side desk with Claude Code agents in the support roles.

Analyst: Basel Al-Ghousein, Level II candidate for the CFA designation.

**Live site: https://kosherite.github.io/Northwall-Research/**

## The site

**Public front end** (`/`): coverage by sector (Oil & Gas, Metals & Mining), a page per company with the thesis, estimates, valuation and a target-versus-commodity chart, the research library with PDF downloads, and disclosures. It is built from `public.json`, which `tools/public_data.js` computes from the models. Model inputs, sources and Excel files are never copied to the site.

**Desk** (`/desk/`, analyst only): sign in with a fine-grained GitHub token for this repository (Contents and Actions: read and write). GitHub checks the token can write to the repo before the desk loads. The desk edits model inputs, the house deck, events and one-pager text; runs the five agents (with your Anthropic API key and live web search); downloads the Excel models; and starts builds.

**How a change flows:** the desk saves to `data/state.json` → `.github/workflows/desk.yml` runs `tools/sync_state.py` (writes the changes into `model_inputs.yaml`, `price_deck.yaml`, `onepager.yaml` and the CSV logs) → rebuilds the affected Excel models with their checks → renders a one-pager draft or final PDF when asked → commits → redeploys the site. Final PDFs are never overwritten; a second final on the same day becomes v1.1.

**Prices:** `.github/workflows/site.yml` rebuilds the site every 15 minutes in market hours with delayed quotes from `tools/fetch_prices.py`.

## Coverage

| Ticker | Company | Rating | Target | Model |
| --- | --- | --- | --- | --- |
| AGI | Alamos Gold | Buy | US$39.00 | `models/AGI/` |
| FNV | Franco-Nevada | Hold | US$250.00 | `models/FNV/` |
| GFR | Greenfire Resources | Buy | US$8.25 | `models/GFR/` |
| WCP | Whitecap Resources | Buy | C$24.00 | `models/WCP/` |

Published research: `reports/published/` (index in `reports/README.md`). Live tracker: `data/coverage_tracker.csv`.

## How the shop runs

```
research-associate ─▶ financial-modeler ─▶ equity-analyst ─▶ supervisory-analyst ─▶ publishing-desk
 filings, prices,       builds Excel models     forecasts, valuation,   CFA Standards review,     final PDF, logs,
 sourced inputs         and integrity checks    rating, report text     sign or block             tracker, git commit
```

Each role is a Claude Code agent in `.claude/agents/`. The main Claude session acts as Director of Research and follows `CLAUDE.md`. Recurring work is packaged as slash commands in `.claude/skills/`:

| Command | When |
| --- | --- |
| `/weekly-update` | Every Monday: prices, model rebuild, tracker, rating triggers |
| `/earnings-review AGI` | Within 24 hours of a covered company's results |
| `/refresh-deck` | Monthly, or when gold or oil moves more than 10% |
| `/new-coverage <company>` | Initiating on a new name |
| `/publish AGI OnePager` | Taking a finished draft through compliance to publication |

## Models are built from sourced inputs

Nobody types numbers into Excel. Each company has `coverage/<TICKER>/model_inputs.yaml`, where every input carries its source. `tools/build_model.py` turns it, plus the house price deck in `data/price_deck.yaml`, into a formula-driven workbook:

| Sheet | Contents |
| --- | --- |
| Cover | Rating, target, return, key outputs, colour legend |
| Inputs | Every typed number, in blue, with its source |
| Model | Operations and financials: H1 actual + H2 estimate, 2027E–2030E |
| Valuation | Target methods, CAPM and WACC, FCFF DCF, reverse DCF, residual income, justified P/E |
| NAV | Asset-life discounted cash flow for resource companies |
| Sensitivity | Target vs. the two multiples; DCF vs. WACC and terminal growth |
| Ratios | DuPont, cash conversion, payout, leverage |
| Comps · Checks · Log | Peers; integrity checks (all must be TRUE); dated change log |

The method follows the CFA Level II curriculum step by step. See `docs/CFA_Modelling_Framework.md`.

## Setup

```
pip install -r requirements.txt          # openpyxl, pyyaml, weasyprint
# LibreOffice is needed to recalculate workbooks (apt install libreoffice-calc / brew install --cask libreoffice)
python tools/build_model.py --all        # builds, recalculates and checks all four models
python tools/check_report.py FNV AGI WCP GFR
python tools/tracker.py
```

Open the folder in Claude Code and ask, for example: "Use the research-associate to load Alamos's Q3 results", or run `/earnings-review AGI`.

## Repository map

```
.claude/agents/        five role agents
.claude/skills/        workflow commands
coverage/<T>/          model_inputs.yaml, outputs.json, sources/
data/                  price deck, tracker, event calendar
models/<T>/            generated Excel models, one per version
reports/<T>/           one-pager text and exhibits; drafts/ and published/
compliance/            checklist, signed checklists, rating log, holdings, corrections, distribution
tools/                 model engine, archetypes, report builder, checks
docs/                  CFA modelling framework, brand kit
```

Every push runs the model build and report checks in GitHub Actions (`.github/workflows/models.yml`).

---
Research samples for information only; not investment advice. Northwall Research is not a registered dealer.
