#!/usr/bin/env python3
"""Create data/state.json, the desk's working file, from the repository's source files.

The desk (site/desk) reads and writes data/state.json. tools/sync_state.py writes desk changes back
to the source files, so model_inputs.yaml, price_deck.yaml, onepager.yaml and the CSV logs stay the
record of truth for the Excel models and PDFs.

    python tools/make_state.py           # only if data/state.json does not exist
    python tools/make_state.py --force   # rebuild it from the source files
"""
import csv, json, re, sys, time
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data' / 'state.json'
DOC = {'OnePager': 'Company note', 'Initiation': 'Initiation', 'EarningsReview': 'Earnings review', 'FlashNote': 'Flash note'}


def library(cov):
    lib = {}
    for i, f in enumerate(sorted((ROOT / 'reports' / 'published').glob('*.pdf'), reverse=True)):
        m = re.match(r'(\d{4}-\d\d-\d\d)_([A-Z]+)_([A-Za-z]+)_v(\d+\.\d+)\.pdf', f.name)
        if not m:
            continue
        date, t, kind, ver = m.groups()
        p = cov.get(t, {}).get('published', {})
        dt = DOC.get(kind, kind)
        if kind == 'Initiation' and ver != '1.0':
            dt = 'Company report'
        lib[f'{t}_{kind}_v{ver}'] = {'ts': int(time.mktime(time.strptime(date, '%Y-%m-%d'))) * 1000 + 1000 - i, 'date': date, 'ticker': t,
                                    'doc_type': dt, 'title': '' if ver == '1.0' else f'v{ver}', 'rating': p.get('rating'), 'target': p.get('target'),
                                    'ccy': cov.get(t, {}).get('company', {}).get('price_ccy', 'USD'), 'url': f'reports/{f.name}', 'file': f.name}
    return lib


def build():
    cov = {d.name: yaml.safe_load(open(d / 'model_inputs.yaml')) for d in sorted((ROOT / 'coverage').iterdir()) if (d / 'model_inputs.yaml').exists()}
    deck = yaml.safe_load(open(ROOT / 'data' / 'price_deck.yaml'))
    deck['as_of'] = str(deck['as_of'])
    events = {}
    for i, r in enumerate(csv.DictReader(open(ROOT / 'data' / 'event_calendar.csv'))):
        events[f'ev-{i + 1}'] = {**r, 'sort': '9999' if r['date'] == 'TBC' else r['date']}
    rlog = {}
    for i, r in enumerate(csv.DictReader(open(ROOT / 'compliance' / 'rating_pt_log.csv'))):
        num = lambda v: float(v) if v not in ('', None) else None
        rlog[f'rl-{i + 1}'] = {'ts': int(time.mktime(time.strptime(r['date'], '%Y-%m-%d'))) * 1000 + i, 'date': r['date'], 'ticker': r['ticker'], 'action': r['action'],
                               'old_rating': r['old_rating'] or None, 'new_rating': r['new_rating'], 'old_target': num(r['old_target']),
                               'new_target': num(r['new_target']), 'price': num(r['price']), 'reason': r['reason'], 'file': r.get('file', '')}
    reports = {}
    for t in cov:
        p = ROOT / 'reports' / t / 'onepager.yaml'
        if p.exists():
            y = yaml.safe_load(open(p))
            reports[t] = {k: y.get(k, '') for k in ('sector', 'date', 'date_long', 'summary', 'valuation', 'risks')}
    return {'updated': int(time.time() * 1000), 'config': {'deck': deck}, 'coverage': cov, 'events': events, 'ratinglog': rlog,
            'notes': {}, 'library': library(cov), 'activity': {}, 'reports': reports}


if __name__ == '__main__':
    if OUT.exists() and '--force' not in sys.argv:
        print('data/state.json exists; use --force to rebuild it'); sys.exit(0)
    json.dump(build(), open(OUT, 'w'), indent=1, default=str)
    print('wrote', OUT)
