"""Assemble the Northwall pages.
python app/build.py              -> app/northwall.html (claude.ai artifact body, data embedded)
python app/build.py --site DIR   -> DIR/index.html (public front end) and DIR/desk/index.html (signed-in back end, no data embedded)
"""
import json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
rd = lambda f: open(f if os.path.isabs(f) else os.path.join(here, f), encoding='utf-8').read()
engine = rd('engine.js').replace("if (typeof module !== 'undefined') module.exports = NW;", '')
app = rd('app.src.html')


def desk_page(embed):
    src = app.replace('/*ENGINE*/', engine)
    if embed:
        src = src.replace('/*SEED*/', json.dumps(json.loads(rd('seed_full.json')), separators=(',', ':'))).replace('/*XLSX*/', rd('xlsx.json'))
        src = src.replace('/*LIB*/', rd('lib.json')).replace('/*PRICES*/', rd('prices.json') if os.path.exists(os.path.join(here, 'prices.json')) else 'null')
        src = src.replace("const S = { deck: SEED.deck, coverage: SEED.coverage, events: [], ratinglog: [],", "const S = { deck: SEED.deck, coverage: SEED.coverage, events: SEED.events || [], ratinglog: SEED.ratinglog || [],")
    else:
        src = src.replace('/*SEED*/', '{"deck":null,"coverage":{}}').replace('/*XLSX*/', '{}').replace('/*LIB*/', '[]').replace('/*PRICES*/', 'null').replace('/*DESK*/false', 'true')
        src = src.replace('<title>Northwall Research</title>', '<title>Northwall Desk</title><meta name="robots" content="noindex">')
    return src


def wrap(body):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="description" content="Northwall Research: independent equity research on North American oil and gas, and metals and mining.">'
            '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
            '</head><body>' + body + '</body></html>')


if '--site' in sys.argv:
    out = sys.argv[sys.argv.index('--site') + 1]; os.makedirs(os.path.join(out, 'desk'), exist_ok=True)
    desk = desk_page(False)
    open(os.path.join(out, 'desk', 'index.html'), 'w', encoding='utf-8').write(wrap(desk))
    css = re.search(r'<style>(.*?)</style>', app, re.S).group(1)
    pub = rd(os.path.join(root, 'site', 'public.src.html')).replace('/*CSS*/', css)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(wrap(pub))
    open(os.path.join(here, 'check.js'), 'w').write('\n'.join(re.findall(r'<script>(.*?)</script>', desk, re.S)))
    open(os.path.join(here, 'check_public.js'), 'w').write('\n'.join(re.findall(r'<script>(.*?)</script>', pub, re.S)))
    print('wrote', out + '/index.html and desk/index.html')
else:
    src = desk_page(True)
    open(os.path.join(here, 'check.js'), 'w').write('\n'.join(re.findall(r'<script>(.*?)</script>', src, re.S)))
    open(os.path.join(here, 'northwall.html'), 'w', encoding='utf-8').write(src)
    print('wrote northwall.html')
