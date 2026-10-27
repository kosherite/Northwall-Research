#!/usr/bin/env python3
"""Build a company's Excel model from its documented inputs.

    python tools/build_model.py AGI            # build, recalculate, write outputs.json
    python tools/build_model.py --all

Reads   coverage/<TICKER>/model_inputs.yaml and data/price_deck.yaml
Writes  models/<TICKER>/<date>_<TICKER>_Model_<version>.xlsx
        coverage/<TICKER>/outputs.json   (key results, read back from the recalculated workbook)
Exit code 1 if any integrity check on the Checks sheet fails.
"""
import sys, json, importlib, subprocess, shutil, tempfile, os
from pathlib import Path
import yaml
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from engine import Model                                    # noqa: E402
import common                                               # noqa: E402


def recalc(path: Path):
    """Re-save the workbook through headless LibreOffice so every formula carries a cached value
    (needed for phone/web previews and for reading outputs back). Excel recalculates on open anyway."""
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice:
        print('  ! LibreOffice not found: open the file in Excel once to calculate it.')
        return False
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory(prefix='lo_profile_') as prof:
        args = [f"-env:UserInstallation={Path(prof).as_uri()}", '--headless', '--norestore', '--calc',
                '--convert-to', 'xlsx', '--outdir', tmp, str(path)]
        env = os.environ.copy(); env['SAL_USE_VCLPLUGIN'] = 'svp'
        helper = os.environ.get('NORTHWALL_SOFFICE_HELPER')      # optional sandbox shim
        if helper:
            sys.path.insert(0, helper)
            from office.soffice import run_soffice
            run_soffice(args[1:] if False else args, check=True, capture_output=True, timeout=240)
        else:
            subprocess.run([soffice] + args, env=env, check=True, capture_output=True, timeout=240)
        shutil.copy(Path(tmp) / path.name, path)
    return True


def read_outputs(calc_path: Path, refs: dict):
    wb = load_workbook(calc_path, data_only=True)
    out = {}
    for name, ref in refs.items():
        sheet, cell = ref.split('!')
        out[name] = wb[sheet.strip("'")][cell.replace('$', '')].value
    errors = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith('#') and c.value[1:4].isupper():
                    errors.append(f"{ws.title}!{c.coordinate}={c.value}")
    return out, errors


def build(ticker: str):
    cdir = ROOT / 'coverage' / ticker
    cfg = yaml.safe_load(open(cdir / 'model_inputs.yaml'))
    deck = yaml.safe_load(open(ROOT / 'data' / 'price_deck.yaml'))
    arch = importlib.import_module(f"archetypes.{cfg['company']['archetype']}")
    m = Model(cfg, deck)
    m.build_inputs()
    m.build_model(arch.lines(cfg), cfg['company']['model_ccy'])
    common.valuation(m, arch)
    common.sensitivity(m, arch)
    common.ratios(m, arch)
    common.comps(m)
    common.checks(m, arch)
    common.log(m)
    common.cover(m)
    order = ['Cover', 'Inputs', 'Model', 'Valuation', 'NAV', 'Sensitivity', 'Ratios', 'Comps', 'Checks', 'Log']
    m.wb._sheets = [m.wb[s] for s in order if s in m.wb.sheetnames]
    co = cfg['company']
    mdir = ROOT / 'models' / ticker; mdir.mkdir(parents=True, exist_ok=True)
    path = mdir / f"{co['model_date']}_{ticker}_Model_{co['version']}.xlsx"
    m.save(path)
    print(f"  wrote {path.relative_to(ROOT)}")
    if recalc(path):
        out, errors = read_outputs(path, m.outputs)
        out = {k: (round(v, 6) if isinstance(v, float) else v) for k, v in out.items()}
        out['model_file'] = str(path.relative_to(ROOT)); out['formula_errors'] = errors
        json.dump(out, open(cdir / 'outputs.json', 'w'), indent=2, default=str)
        status = 'PASS' if out.get('all_checks') is True and not errors else 'FAIL'
        print(f"  {ticker}: target {out['target']} | rating {out['rating']} | checks {status}"
              + (f" | errors {errors[:5]}" if errors else ''))
        return status == 'PASS'
    return True


if __name__ == '__main__':
    args = sys.argv[1:]
    tickers = sorted(p.name for p in (ROOT / 'coverage').iterdir() if (p / 'model_inputs.yaml').exists()) if args == ['--all'] else args
    ok = all([build(t) for t in tickers])
    sys.exit(0 if ok else 1)
