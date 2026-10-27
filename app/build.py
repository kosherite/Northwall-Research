"""Assemble the Northwall web app.
python build.py              -> northwall.html (claude.ai artifact body)
python build.py --site DIR   -> DIR/index.html (standalone page for GitHub Pages)
"""
import json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: open(os.path.join(here, f), encoding='utf-8').read()
src = rd('app.src.html')
src = src.replace('/*ENGINE*/', rd('engine.js').replace("if (typeof module !== 'undefined') module.exports = NW;", ''))
src = src.replace('/*SEED*/', json.dumps(json.loads(rd('seed_full.json')), separators=(',', ':')))
src = src.replace('/*XLSX*/', rd('xlsx.json'))
src = src.replace('/*LIB*/', rd('lib.json') if os.path.exists(os.path.join(here, 'lib.json')) else '[]')
prices = os.path.join(here, 'prices.json')
src = src.replace('/*PRICES*/', rd('prices.json') if os.path.exists(prices) else 'null')
src = src.replace("const S = { deck: SEED.deck, coverage: SEED.coverage, events: [], ratinglog: [],",
                  "const S = { deck: SEED.deck, coverage: SEED.coverage, events: SEED.events || [], ratinglog: SEED.ratinglog || [],")
open(os.path.join(here, 'check.js'), 'w').write('\n'.join(re.findall(r'<script>(.*?)</script>', src, re.S)))
if '--site' in sys.argv:
    out = sys.argv[sys.argv.index('--site') + 1]; os.makedirs(out, exist_ok=True)
    head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="description" content="Northwall Research: independent equity research on North American oil and gas, and metals and mining.">'
            '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
            '</head><body>')
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(head + src + '</body></html>')
    print('wrote', os.path.join(out, 'index.html'))
else:
    open(os.path.join(here, 'northwall.html'), 'w', encoding='utf-8').write(src)
    print('wrote northwall.html')
