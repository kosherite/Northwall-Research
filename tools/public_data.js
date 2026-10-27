// Build site/public.json: everything the public front end shows, computed from data/state.json with the
// same engine the desk uses. Model inputs, sources and spreadsheets are deliberately left out.
// Usage: node tools/public_data.js OUT.json
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const NW = require(path.join(ROOT, 'app', 'engine.js'));
const st = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'state.json'), 'utf8'));
const deck = st.config.deck;
const SECTOR = { ep_cashflow: 'oil-gas', oil_sands: 'oil-gas', royalty: 'metals-mining', gold_producer: 'metals-mining' };
const LINES = {
  royalty: [['geo', 'GEOs sold (000 oz)', 1], ['rev', 'Revenue (US$M)', 0], ['ebitda', 'Adj. EBITDA (US$M)', 0], ['eps', 'Adj. EPS (US$)', 2], ['cfps', 'CFPS (US$)', 2], ['dps', 'DPS (US$)', 2]],
  gold_producer: [['oz', 'Production (koz)', 1], ['aisc', 'AISC (US$/oz)', 0], ['rev', 'Revenue (US$M)', 0], ['eps', 'Adj. EPS (US$)', 2], ['cfps', 'CFPS (US$)', 2], ['fcf', 'Free cash flow (US$M)', 0]],
  ep_cashflow: [['prod', 'Production (kboe/d)', 1], ['ff', 'Funds flow (C$M)', 0], ['cfps', 'Funds flow / share (C$)', 2], ['capex', 'Capital (C$M)', 0], ['fff', 'Free funds flow (C$M)', 0], ['netdebt', 'Net debt (C$M)', 0]],
  oil_sands: [['prod', 'Production (kbbl/d)', 1], ['ebitda', 'Adj. EBITDA (C$M)', 0], ['aff', 'Adj. funds flow (C$M)', 0], ['cfps', 'AFF / share (C$)', 2], ['capex', 'Capital (C$M)', 0], ['netdebt', 'Net debt (C$M)', 0]],
};
const COLS = ['2025A', '2026E', '2027E', '2028E', '2029E', '2030E'];
const clone = (o) => JSON.parse(JSON.stringify(o));
const r2 = (v, d = 4) => v == null || isNaN(v) ? null : +Number(v).toFixed(d);
function flatDeck(usesGold, v) { const d = clone(deck), k = usesGold ? 'gold' : 'wti'; ['2027E', '2028E', '2029E', '2030E'].forEach(p => d.series[k].values[p] = v); if (usesGold) d.scalars.gold_lt.value = v; return d; }
const companies = {};
for (const [t, cfg] of Object.entries(st.coverage)) {
  const { out: o, m } = NW.run(cfg, deck), c = cfg.company, pub = cfg.published, arch = c.archetype;
  const usesGold = (cfg.deck_uses || []).includes('gold'), lo = usesGold ? 2800 : 50, hi = usesGold ? 5200 : 110, step = (hi - lo) / 40;
  const curve = []; for (let x = lo; x <= hi + 1e-9; x += step) { try { const R = NW.run(cfg, flatDeck(usesGold, x)); curve.push([r2(x, 2), r2(R.out.blend_px, 3), R.out.target]); } catch (e) { } }
  const price = cfg.scalars.price.value, dps = (cfg.scalars.dps_fwd || {}).value || 0;
  const rep = (st.reports || {})[t] || {};
  companies[t] = {
    ticker: t, name: c.name, exchange: c.exchange, sector: SECTOR[arch], industry: rep.sector || c.sector, analyst: c.analyst, ccy: c.price_ccy, model_ccy: c.model_ccy,
    rating: pub.rating, target: pub.target, published: pub.date, price, ret: r2(pub.target / price - 1 + dps / price, 8), div_yield: r2(dps / price, 8),
    estimates: LINES[arch].map(([k, l, d]) => ({ label: l, d, values: COLS.map(p => m[k] && m[k][p] != null ? r2(m[k][p], 4) : null) })),
    valuation: { methods: o.methods, v1: r2(o.v1, 2), v2: r2(o.v2, 2), navps: r2(o.navps, 2), ke: r2(o.ke), wacc: r2(o.wacc), dcf_ps: r2(o.dcf_ps, 2), g_impl: r2(o.g_impl), ri_ps: r2(o.ri_ps, 2), be_wti: r2(o.be_wti, 1) },
    curve: { commodity: usesGold ? 'Gold' : 'WTI', unit: usesGold ? 'US$/oz' : 'US$/bbl', house: usesGold ? deck.series.gold.values['2027E'] : deck.series.wti.values['2027E'], points: curve },
    text: { summary: rep.summary || '', valuation: rep.valuation || '', risks: rep.risks || '' },
  };
}
const sortv = (o) => Object.values(o || {});
const pubLib = sortv(st.library).filter(x => x.file).sort((a, b) => (b.ts || 0) - (a.ts || 0)).map(x => ({ date: x.date, ticker: x.ticker, doc_type: x.doc_type, title: x.title || '', rating: x.rating, target: x.target, ccy: x.ccy, file: x.file }));
const out = {
  built: new Date().toISOString(), cols: COLS,
  deck: { as_of: deck.as_of, gold: deck.series.gold.values, wti: deck.series.wti.values, wcs_diff: deck.series.wcs_diff.values, usdcad: deck.series.usdcad.values, gold_lt: deck.scalars.gold_lt.value },
  companies, library: pubLib,
  events: sortv(st.events).map(e => ({ date: e.date, ticker: e.ticker, event: e.event, status: e.status })),
  ratinglog: sortv(st.ratinglog).sort((a, b) => (b.ts || 0) - (a.ts || 0)).map(r => ({ date: r.date, ticker: r.ticker, action: r.action, old_rating: r.old_rating, new_rating: r.new_rating, old_target: r.old_target, new_target: r.new_target })),
};
fs.writeFileSync(process.argv[2] || 'public.json', JSON.stringify(out));
console.log('public.json:', Object.keys(companies).join(', '), '·', pubLib.length, 'reports');
