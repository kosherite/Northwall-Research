#!/usr/bin/env python3
"""Write desk changes in data/state.json back to the source files the models and PDFs are built from.

Prints a JSON list of tickers whose model inputs changed, plus "DECK" if the price deck changed.
    python tools/sync_state.py
"""
import csv, json, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


class D(yaml.SafeDumper):
    pass
D.add_representer(str, lambda d, s: d.represent_scalar('tag:yaml.org,2002:str', s, style='|' if '\n' in s else None))


def dump(path, data, header):
    body = yaml.dump(data, Dumper=D, sort_keys=False, allow_unicode=True, width=200)
    path.write_text(header + body)


def header(path):
    lines = path.read_text().splitlines(True) if path.exists() else []
    return ''.join(l for l in lines[:6] if l.startswith('#'))


def main():
    st = json.load(open(ROOT / 'data' / 'state.json'))
    changed = []
    for t, cfg in st.get('coverage', {}).items():
        p = ROOT / 'coverage' / t / 'model_inputs.yaml'
        p.parent.mkdir(parents=True, exist_ok=True)
        cur = yaml.safe_load(open(p)) if p.exists() else None
        if json.loads(json.dumps(cur, default=str)) != json.loads(json.dumps(cfg, default=str)):
            dump(p, cfg, header(p) or f'# {t} model inputs. Written by the desk (tools/sync_state.py).\n'); changed.append(t)
    deck = st['config']['deck']; p = ROOT / 'data' / 'price_deck.yaml'
    cur = yaml.safe_load(open(p)); cur['as_of'] = str(cur['as_of'])
    if json.loads(json.dumps(cur, default=str)) != json.loads(json.dumps(deck, default=str)):
        dump(p, deck, header(p)); changed.append('DECK')
    ev = sorted(st.get('events', {}).values(), key=lambda e: str(e.get('sort') or e.get('date')))
    with open(ROOT / 'data' / 'event_calendar.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, ['date', 'ticker', 'event', 'product_due', 'status'], lineterminator='\n'); w.writeheader()
        for e in ev: w.writerow({k: e.get(k, '') for k in w.fieldnames})
    p = ROOT / 'compliance' / 'rating_pt_log.csv'
    rows = list(csv.DictReader(open(p))); seen = {(r['date'], r['ticker'], r['new_rating'], str(float(r['new_target'] or 0))) for r in rows}
    new = [r for r in sorted(st.get('ratinglog', {}).values(), key=lambda r: r.get('ts', 0))
           if (r['date'], r['ticker'], r['new_rating'], str(float(r.get('new_target') or 0))) not in seen]
    if new:
        with open(p, 'a', newline='') as f:
            w = csv.writer(f, lineterminator='\n')
            for r in new: w.writerow([r['date'], r['ticker'], r['action'], r.get('old_rating') or '', r['new_rating'], r.get('old_target') or '', r.get('new_target'), r.get('price'), r.get('reason', ''), r.get('file', '')])
    for t, rep in st.get('reports', {}).items():
        p = ROOT / 'reports' / t / 'onepager.yaml'
        if not p.exists(): continue
        y = yaml.safe_load(open(p)); before = dict(y)
        for k in ('summary', 'valuation', 'risks', 'date', 'date_long'):
            if rep.get(k): y[k] = rep[k]
        if y != before: dump(p, y, header(p))
    print(json.dumps(changed))


if __name__ == '__main__':
    main()
