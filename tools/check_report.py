#!/usr/bin/env python3
"""Pre-publication number check (Supervisory Analyst tool).

    python tools/check_report.py AGI

Fails (exit 1) when:
  - the model's integrity checks do not all pass, or the workbook has formula errors;
  - the narrative quotes a price target or implied return that differs from coverage/<T>/outputs.json;
  - the narrative never states the target, so a reader could not tie it to the model.
It does not judge the thesis: that is the Supervisory Analyst's checklist (compliance/checklist.md).
"""
import sys, json, re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(t):
    out = json.load(open(ROOT / 'coverage' / t / 'outputs.json'))
    rep = yaml.safe_load(open(ROOT / 'reports' / t / 'onepager.yaml'))
    text = re.sub('<[^>]+>', ' ', rep['valuation'] + ' ' + rep['summary'])
    problems = []
    if out.get('all_checks') is not True:
        problems.append('model integrity checks do not all pass (see the Checks sheet)')
    if out.get('formula_errors'):
        problems.append(f"formula errors in workbook: {out['formula_errors'][:5]}")
    tgt = out['target']
    quoted = [float(x.replace(',', '')) for x in re.findall(r'(?:US\$|C\$)([\d,]+\.\d\d) price target', text)]
    if not quoted:
        problems.append(f'narrative never states the price target (expected {tgt:,.2f} before the words "price target")')
    for q in quoted:
        if abs(q - tgt) > 0.005:
            problems.append(f'narrative target {q:,.2f} differs from model target {tgt:,.2f}')
    ret = round(out['ret_all'] * 100, 1)
    for q in [float(x) for x in re.findall(r'([\d.]+)% implied (?:all-in )?return', text)]:
        if abs(q - ret) > 0.05:
            problems.append(f'narrative implied return {q}% differs from model {ret}%')
    print(f"{t}: {'PASS' if not problems else 'FAIL'}")
    for p in problems:
        print('  -', p)
    return not problems


if __name__ == '__main__':
    ok = all([check(t) for t in sys.argv[1:]])
    sys.exit(0 if ok else 1)
