import json, re, os
seed=json.load(open('seed_full.json'))
src=open('app.src.html').read()
src=src.replace('/*ENGINE*/',open('engine.js').read().replace("if (typeof module !== 'undefined') module.exports = NW;",''))
src=src.replace('/*SEED*/',json.dumps(seed,separators=(',',':')))
src=src.replace('/*XLSX*/',open('xlsx.json').read())
lib=json.load(open('lib.json')) if os.path.exists('lib.json') else []
src=src.replace('/*LIB*/',json.dumps(lib))
src=src.replace("const S = { deck: SEED.deck, coverage: SEED.coverage, events: [], ratinglog: [],","const S = { deck: SEED.deck, coverage: SEED.coverage, events: SEED.events || [], ratinglog: SEED.ratinglog || [],")
open('northwall.html','w').write(src)
open('check.js','w').write('\n'.join(re.findall(r'<script>(.*?)</script>',src,re.S)))
