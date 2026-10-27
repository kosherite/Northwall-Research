#!/usr/bin/env python3
"""Rebuild the coverage tracker from each company's model outputs.

    python tools/tracker.py

Writes data/coverage_tracker.csv and prints any name whose implied return has crossed a rating band
(a review trigger under the Northwall research policy). Prices come from each model_inputs.yaml, so
refresh prices there (Research Associate, every Monday) and rebuild the models first.
"""
import csv, json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def band(ret, buy=0.15):
    return 'Buy' if ret > buy else ('Hold' if ret >= 0 else 'Sell')


rows, flags = [], []
for d in sorted((ROOT / 'coverage').iterdir()):
    if not (d / 'outputs.json').exists():
        continue
    cfg = yaml.safe_load(open(d / 'model_inputs.yaml'))
    out = json.load(open(d / 'outputs.json'))
    pub = cfg['published']
    rows.append({
        'ticker': d.name, 'company': cfg['company']['name'], 'sector': cfg['company']['sector'],
        'currency': cfg['company']['price_ccy'], 'published_rating': pub['rating'], 'published_target': pub['target'],
        'published_date': pub['date'], 'price': cfg['scalars']['price']['value'], 'price_source': cfg['scalars']['price']['source'],
        'model_target': out['target'], 'implied_all_in_return': round(out['ret_all'], 4),
        'band_rating': band(out['ret_all']), 'model_checks_pass': out['all_checks'], 'model_file': out['model_file'],
    })
    if band(out['ret_all']) != pub['rating'] or out['target'] != pub['target']:
        flags.append(f"{d.name}: published {pub['rating']} / {pub['target']} vs model {band(out['ret_all'])} / {out['target']} -> review")

with open(ROOT / 'data' / 'coverage_tracker.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
print(f"Tracker: {len(rows)} names written to data/coverage_tracker.csv")
print('\n'.join(flags) if flags else 'No rating triggers fired.')
