---
name: weekly-update
description: Northwall Monday routine: refresh share prices for every covered name, rebuild all models, update the coverage tracker and flag any rating triggers or upcoming events. Use when asked for the weekly update or "/weekly-update".
---

# Weekly update

1. **research-associate**: for each ticker in `coverage/`, update the `price` scalar (close, date, source) and check `data/event_calendar.csv` for the next 30 days. Check gold, WTI and USD/CAD against `data/price_deck.yaml`; if any moved more than 10% since `as_of`, recommend `/refresh-deck`.
2. **financial-modeler**: `python tools/build_model.py --all`. Prices change returns, not the published target, so the "target equals published" check should still pass; report any failure.
3. Run `python tools/tracker.py`.
4. Report a short table: ticker, price, target, implied all-in return, published rating, band rating, next event. Name every rating trigger and recommend whether the analyst should review.
