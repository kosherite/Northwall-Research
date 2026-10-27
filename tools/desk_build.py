#!/usr/bin/env python3
"""Run a desk build on GitHub Actions.

    python tools/desk_build.py push                         # desk data changed: sync, rebuild affected models
    python tools/desk_build.py model ALL|<T>                # rebuild Excel models
    python tools/desk_build.py onepager_draft <T>           # draft PDF in reports/drafts
    python tools/desk_build.py onepager_final <T>           # final PDF in reports/published, added to the library
"""
import datetime, json, subprocess, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
py = sys.executable


def run(*a, check=True):
    print('$', ' '.join(a), flush=True); return subprocess.run(list(a), cwd=ROOT, check=check)


def main():
    task = sys.argv[1]; ticker = (sys.argv[2] if len(sys.argv) > 2 else 'ALL').upper()
    changed = json.loads(subprocess.run([py, 'tools/sync_state.py'], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip() or '[]')
    print('inputs changed:', changed)
    if task == 'push':
        targets = ['--all'] if 'DECK' in changed else [t for t in changed if t != 'DECK']
    elif task == 'model':
        targets = ['--all'] if ticker == 'ALL' else [ticker]
    else:
        targets = ['--all'] if 'DECK' in changed else sorted(set([t for t in changed if t != 'DECK'] + [ticker]))
    if targets:
        run(py, 'tools/build_model.py', *targets)
    if task.startswith('onepager'):
        if ticker == 'ALL':
            sys.exit('Choose one company for a one-pager build.')
        final = task == 'onepager_final'
        if final:
            p = ROOT / 'reports' / ticker / 'onepager.yaml'; y = yaml.safe_load(open(p)); d = datetime.date.today()
            y['date'] = d.isoformat(); y['date_long'] = d.strftime('%B %-d, %Y'); p.write_text(open(p).read().split('ticker:', 1)[0] + yaml.safe_dump(y, sort_keys=False, allow_unicode=True, width=200))
            run(py, 'tools/check_report.py', ticker)          # a final must tie to the model
        else:
            run(py, 'tools/check_report.py', ticker, check=False)  # a draft shows problems but still renders
        run(py, 'tools/build_onepager.py', ticker, *(['--final'] if final else []))
        if final:  # add the new PDF to the desk library
            st = json.load(open(ROOT / 'data' / 'state.json'))
            sys.path.insert(0, str(ROOT / 'tools')); import make_state
            lib = make_state.library(st['coverage'])
            for k, v in lib.items():
                if not any(x.get('file') == v['file'] for x in st['library'].values()):
                    st['library'][k] = v
            json.dump(st, open(ROOT / 'data' / 'state.json', 'w'), indent=1, default=str)
    run(py, 'tools/tracker.py', check=False)


if __name__ == '__main__':
    main()
