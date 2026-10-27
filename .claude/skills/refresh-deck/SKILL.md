---
name: refresh-deck
description: Refresh the Northwall house price deck (gold, WTI, WCS, USD/CAD, risk-free rate) and show the effect on every target. Use monthly or when a commodity moves more than 10%.
---

# Refresh the house price deck

1. **research-associate**: fetch current spot gold, WTI, WCS differential, USD/CAD and the US 10-year yield from dated sources. Propose new deck values with reasons; append old and new values to `data/price_deck_history.csv`.
2. **equity-analyst**: approve or amend the forecast years (the deck is a judgement, not spot). Edit `data/price_deck.yaml` and set `as_of`.
3. **financial-modeler**: `python tools/build_model.py --all`. Published-target checks will fail where the deck moved a target; list each ticker's old vs. new target and implied return.
4. Run `python tools/tracker.py` and report which ratings now need review. Do not publish target changes from this skill; each goes through `/earnings-review`-style approval or a rating-change note.
