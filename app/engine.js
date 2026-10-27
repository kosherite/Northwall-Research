// Northwall model engine (JavaScript port of tools/engine.py + archetypes). Pure functions.
const NW = (() => {
  const P = ['2025A', 'H1-26A', 'H2-26E', '2026E', '2027E', '2028E', '2029E', '2030E'];
  const F = ['2027E', '2028E', '2029E', '2030E'];
  const num = (v) => {
    if (typeof v === 'number') return v;
    if (typeof v === 'string' && /^=[\d.+\-*/() ]+$/.test(v)) return Function('"use strict";return (' + v.slice(1) + ')')();
    return v == null ? undefined : Number(v);
  };
  const ser = (c, k, p) => { const s = c.series[k]; return s && s.values[p] != null ? num(s.values[p]) : undefined; };
  const sc = (c, k, deck) => {
    if (c.scalars[k]) return num(c.scalars[k].value);
    if (deck.scalars[k]) return num(deck.scalars[k].value);
    throw new Error('missing scalar ' + k);
  };
  const dk = (deck, k, p) => num(deck.series[k].values[p]);
  const mround = (x, m) => Math.round(x / m) * m;
  const L = () => ({});
  const sumH = (o) => (o['H1-26A'] ?? 0) + (o['H2-26E'] ?? 0);
  const prev = { 'H2-26E': 'H1-26A', '2027E': '2026E', '2028E': '2027E', '2029E': '2028E', '2030E': '2029E' };

  function royalty(c, deck) {
    const S = (k) => sc(c, k, deck), m = {};
    ['geo', 'gold', 'rev', 'cos', 'ga', 'ebitda', 'da', 'fin', 'pretax', 'taxes', 'ni', 'shares', 'eps', 'ocf', 'cfps', 'fcff', 'dps', 'divpaid', 'acq', 'cash', 'netdebt', 'equity'].forEach(k => m[k] = L());
    for (const p of P) m.shares[p] = ser(c, 'shares', p);
    for (const p of ['2025A', 'H1-26A']) {
      m.geo[p] = ser(c, 'geo', p); m.rev[p] = ser(c, 'revenue_act', p); m.cos[p] = ser(c, 'cos_act', p); m.ga[p] = ser(c, 'ga_act', p);
      m.ebitda[p] = ser(c, 'ebitda_act', p); m.da[p] = ser(c, 'da_act', p); m.ni[p] = ser(c, 'ni_act', p); m.ocf[p] = ser(c, 'ocf_act', p);
      m.cash[p] = ser(c, 'cash_act', p); m.equity[p] = ser(c, 'equity_act', p); m.dps[p] = ser(c, 'dps', p);
    }
    for (const p of ['H2-26E', ...F]) {
      m.geo[p] = ser(c, 'geo', p); m.gold[p] = dk(deck, 'gold', p);
      m.rev[p] = m.geo[p] * m.gold[p] * S('realization') / 1000; m.cos[p] = m.rev[p] * S('cos_pct'); m.ga[p] = ser(c, 'ga', p);
      m.ebitda[p] = m.rev[p] - m.cos[p] - m.ga[p]; m.da[p] = m.geo[p] * ser(c, 'da_per_geo', p) / 1000; m.fin[p] = ser(c, 'fin_income', p);
      m.pretax[p] = m.ebitda[p] - m.da[p] + m.fin[p]; m.taxes[p] = m.pretax[p] * S('tax_rate'); m.ni[p] = m.pretax[p] - m.taxes[p];
      m.ocf[p] = m.ebitda[p] + m.fin[p] - S('cash_tax_share') * m.taxes[p]; m.dps[p] = ser(c, 'dps', p);
      m.divpaid[p] = m.dps[p] * m.shares[p]; m.acq[p] = ser(c, 'acquisitions', p);
      if (p === 'H2-26E') { m.cash[p] = m.cash['H1-26A'] + m.ocf[p] - m.divpaid[p] - m.acq[p]; m.equity[p] = m.equity['H1-26A'] + m.ni[p] - m.divpaid[p]; }
    }
    for (const k of ['geo', 'rev', 'cos', 'ga', 'ebitda', 'da', 'ni', 'ocf', 'dps']) m[k]['2026E'] = sumH(m[k]);
    m.cash['2026E'] = m.cash['H2-26E']; m.equity['2026E'] = m.equity['H2-26E'];
    for (const p of F) { m.cash[p] = m.cash[prev[p]] + m.ocf[p] - m.divpaid[p] - m.acq[p]; m.equity[p] = m.equity[prev[p]] + m.ni[p] - m.divpaid[p]; m.fcff[p] = m.ocf[p]; }
    for (const p of P) { if (m.ni[p] != null) m.eps[p] = m.ni[p] / m.shares[p]; if (m.ocf[p] != null) m.cfps[p] = m.ocf[p] / m.shares[p]; if (m.cash[p] != null) m.netdebt[p] = -m.cash[p]; }
    // NAV
    let port = 0, opt = 0, geo = 0;
    for (let y = 2027; y <= 2060; y++) {
      const lbl = y + 'E';
      geo = y <= 2030 ? m.geo[lbl] : (y <= 2035 ? S('nav_flat_geo') : geo * (1 - S('nav_decline')));
      const gold = y <= 2030 ? dk(deck, 'gold', lbl) : S('gold_lt');
      const ebitda = geo * gold * S('realization') / 1000 * (1 - S('cos_pct')) - S('nav_ga');
      const df = 1 / Math.pow(1 + S('nav_disc'), y - 2026 - 0.5);
      port += ebitda * (1 - S('nav_cash_tax')) * df;
      if (y >= S('cobre_start') && y <= 2050) opt += S('cobre_geo') * S('gold_lt') * S('realization') / 1000 * (1 - S('cos_pct')) * (1 - S('nav_cash_tax')) * df;
    }
    const nav = port + opt * S('cobre_prob') + S('nav_exploration') + m.cash['2026E'] + S('investments');
    const navps = nav / S('nav_shares');
    return { m, extra: { navps, cobre_ps: opt * S('cobre_prob') / S('nav_shares'), cobre_full_ps: opt / S('nav_shares'), nav_port: port },
      v1: navps * S('mult1'), v2: m.cfps['2027E'] * S('mult2'),
      methods: ['P/NAV', 'P/CF 2027E'], metrics: [navps, m.cfps['2027E']] };
  }

  function goldProducer(c, deck) {
    const S = (k) => sc(c, k, deck), m = {};
    ['oz', 'gold', 'aisc', 'margin', 'rev', 'aisc_m', 'taxes', 'shares', 'eps', 'ni', 'ocf', 'cfps', 'sust', 'growth', 'expl', 'fcf', 'fcff', 'dps', 'divpaid', 'buyback', 'netdebt', 'equity'].forEach(k => m[k] = L());
    for (const p of P) m.shares[p] = ser(c, 'shares', p);
    for (const p of ['2025A', 'H1-26A']) {
      m.oz[p] = ser(c, 'oz', p); m.gold[p] = ser(c, 'gold_real_act', p); m.aisc[p] = ser(c, 'aisc', p); m.rev[p] = ser(c, 'rev_act', p);
      m.eps[p] = ser(c, 'eps_act', p); m.ocf[p] = ser(c, 'ocf_act', p); m.fcf[p] = ser(c, 'fcf_act', p); m.dps[p] = ser(c, 'dps', p);
    }
    m.netdebt['H1-26A'] = ser(c, 'netdebt_act', 'H1-26A'); m.equity['H1-26A'] = ser(c, 'equity_act', 'H1-26A');
    for (const p of ['H2-26E', ...F]) {
      m.oz[p] = ser(c, 'oz', p); m.gold[p] = dk(deck, 'gold', p); m.aisc[p] = ser(c, 'aisc', p);
      m.rev[p] = m.oz[p] * m.gold[p] / 1000;
      m.eps[p] = (m.gold[p] - m.aisc[p] - S('da_excess')) * m.oz[p] / 1000 * (1 - S('mining_tax')) / m.shares[p];
      m.dps[p] = ser(c, 'dps', p);
    }
    for (const p of ['2025A', 'H1-26A', 'H2-26E', ...F]) { m.margin[p] = m.gold[p] - m.aisc[p]; m.aisc_m[p] = m.margin[p] * m.oz[p] / 1000; m.ni[p] = m.eps[p] * m.shares[p]; }
    for (const p of ['H2-26E', ...F]) {
      m.taxes[p] = m.aisc_m[p] * S('mining_tax');
      m.ocf[p] = (m.gold[p] - m.aisc[p] + S('sust_per_oz')) * m.oz[p] / 1000 - m.taxes[p];
      m.sust[p] = S('sust_per_oz') * m.oz[p] / 1000; m.growth[p] = ser(c, 'growth_capex', p); m.expl[p] = ser(c, 'expl', p);
      m.fcf[p] = m.ocf[p] - m.sust[p] - m.growth[p] - m.expl[p];
      m.divpaid[p] = m.dps[p] * m.shares[p]; m.buyback[p] = ser(c, 'buybacks', p);
      const q = prev[p];
      m.netdebt[p] = m.netdebt[q === '2026E' ? '2026E' : q] - m.fcf[p] + m.divpaid[p] + m.buyback[p];
      m.equity[p] = m.equity[q] + m.ni[p] - m.divpaid[p] - m.buyback[p];
      if (p === 'H2-26E') { m.netdebt['2026E'] = m.netdebt[p]; m.equity['2026E'] = m.equity[p]; }
    }
    for (const k of ['oz', 'rev', 'aisc_m', 'eps', 'ni', 'ocf', 'fcf', 'dps']) m[k]['2026E'] = sumH(m[k]);
    m.gold['2026E'] = (m.gold['H1-26A'] * m.oz['H1-26A'] + m.gold['H2-26E'] * m.oz['H2-26E']) / m.oz['2026E'];
    m.aisc['2026E'] = (m.aisc['H1-26A'] * m.oz['H1-26A'] + m.aisc['H2-26E'] * m.oz['H2-26E']) / m.oz['2026E'];
    m.margin['2026E'] = m.gold['2026E'] - m.aisc['2026E'];
    for (const p of P) if (m.ocf[p] != null) m.cfps[p] = m.ocf[p] / m.shares[p];
    for (const p of F) m.fcff[p] = m.fcf[p];
    let port = 0, oz = 0;
    for (let y = 2027; y <= 2050; y++) {
      const lbl = y + 'E', inM = y <= 2030;
      oz = inM ? m.oz[lbl] : (y <= 2036 ? S('nav_flat_oz') : oz * (1 - S('nav_decline')));
      const gold = inM ? dk(deck, 'gold', lbl) : S('gold_lt'), aisc = inM ? m.aisc[lbl] : S('aisc_lt');
      const cf = (gold - aisc) * oz / 1000 * (1 - S('mining_tax')) - (inM ? m.growth[lbl] : 0) - (inM ? m.expl[lbl] : S('expl_lt'));
      port += cf / Math.pow(1 + S('nav_disc'), y - 2026 - 0.5);
    }
    const navps = (port - m.netdebt['2026E']) / S('shares');
    return { m, extra: { navps }, v1: navps * S('mult1'), v2: m.cfps['2027E'] * S('mult2'), methods: ['P/NAV', 'P/CF 2027E'], metrics: [navps, m.cfps['2027E']] };
  }

  function epCashflow(c, deck) {
    const S = (k) => sc(c, k, deck), m = {};
    ['prod', 'days', 'vol', 'wti', 'ffpb', 'ff', 'shares', 'cfps', 'capex', 'fff', 'fffps', 'dacf', 'fcff', 'dps', 'divpaid', 'netdebt'].forEach(k => m[k] = L());
    for (const p of P) m.shares[p] = ser(c, 'shares', p);
    const H = ['H1-26A', 'H2-26E', ...F];
    for (const p of H) { m.prod[p] = ser(c, 'prod', p); m.days[p] = ser(c, 'days', p); m.vol[p] = m.prod[p] * m.days[p] / 1000; m.dps[p] = ser(c, 'dps', p); }
    m.ff['H1-26A'] = ser(c, 'ff_act', 'H1-26A'); m.capex['H1-26A'] = ser(c, 'capex_act', 'H1-26A');
    m.ffpb['H1-26A'] = m.ff['H1-26A'] / m.vol['H1-26A']; m.netdebt['H1-26A'] = ser(c, 'netdebt_act', 'H1-26A');
    for (const p of ['H2-26E', ...F]) {
      m.wti[p] = dk(deck, 'wti', p); m.ffpb[p] = S('ff_anchor') + S('ff_sens') * (m.wti[p] - S('anchor_wti'));
      m.ff[p] = m.vol[p] * m.ffpb[p]; m.capex[p] = ser(c, 'capex', p); m.divpaid[p] = m.dps[p] * m.shares[p];
    }
    for (const p of H) m.fff[p] = m.ff[p] - m.capex[p];
    for (const k of ['days', 'vol', 'ff', 'capex', 'fff', 'dps']) m[k]['2026E'] = sumH(m[k]);
    m.prod['2026E'] = (m.prod['H1-26A'] * m.days['H1-26A'] + m.prod['H2-26E'] * m.days['H2-26E']) / m.days['2026E'];
    m.ffpb['2026E'] = m.ff['2026E'] / m.vol['2026E'];
    m.netdebt['H2-26E'] = m.netdebt['H1-26A'] - m.fff['H2-26E'] + m.divpaid['H2-26E']; m.netdebt['2026E'] = m.netdebt['H2-26E'];
    for (const p of F) { m.netdebt[p] = m.netdebt[prev[p]] - m.fff[p] + m.divpaid[p]; m.fcff[p] = m.fff[p] + S('at_interest'); }
    for (const p of ['2026E', ...F]) m.dacf[p] = m.ff[p] + S('at_interest');
    for (const p of [...H, '2026E']) { m.cfps[p] = m.ff[p] / m.shares[p]; m.fffps[p] = m.fff[p] / m.shares[p]; }
    const sh = S('shares'), nd26 = m.netdebt['2026E'];
    const be = S('anchor_wti') + ((m.dps['2027E'] * m.shares['2027E'] + m.capex['2027E']) / m.vol['2027E'] - S('ff_anchor')) / S('ff_sens');
    return { m, extra: { be_wti: be }, v1: (S('mult1') * m.dacf['2027E'] - nd26) / sh, v2: m.fff['2027E'] / S('mult2') / sh,
      methods: ['EV/DACF 2027E', 'FFF yield 2027E'], metrics: [m.dacf['2027E'], m.fff['2027E']] };
  }

  function oilSands(c, deck) {
    const S = (k) => sc(c, k, deck), m = {};
    ['prod', 'wti', 'ebitda_bbl', 'ebitda', 'interest', 'aff', 'shares', 'cfps', 'capex', 'fcf', 'fcff', 'netdebt', 'lev'].forEach(k => m[k] = L());
    for (const p of ['2025A', '2026E', ...F]) m.prod[p] = ser(c, 'prod', p);
    for (const p of ['2026E', ...F]) m.shares[p] = ser(c, 'shares', p);
    m.aff['2025A'] = ser(c, 'aff_act', '2025A'); m.capex['2025A'] = ser(c, 'capex_act', '2025A'); m.fcf['2025A'] = ser(c, 'fcf_act', '2025A');
    m.netdebt['2026E'] = ser(c, 'netdebt_ye', '2026E');
    for (const p of F) {
      m.wti[p] = dk(deck, 'wti', p); m.ebitda_bbl[p] = S('ebitda_anchor') + S('ebitda_sens') * (m.wti[p] - S('anchor_wti'));
      m.ebitda[p] = m.prod[p] * 365 * m.ebitda_bbl[p] / 1000; m.interest[p] = ser(c, 'interest', p); m.aff[p] = m.ebitda[p] - m.interest[p];
      m.cfps[p] = m.aff[p] / m.shares[p]; m.capex[p] = ser(c, 'capex', p); m.fcf[p] = m.aff[p] - m.capex[p]; m.fcff[p] = m.fcf[p] + m.interest[p];
      m.lev[p] = m.netdebt[prev[p]] / m.ebitda[p]; m.netdebt[p] = m.netdebt[prev[p]] - m.fcf[p];
    }
    const sh = S('shares'), nd26 = m.netdebt['2026E'];
    const navps = (S('pv10_gfr') + S('nav_connacher') - nd26) / sh;
    return { m, extra: { navps }, v1: S('mult1') * navps, v2: (S('mult2') * m.ebitda['2027E'] - nd26) / sh,
      methods: ['P/NAV (2P)', 'EV/EBITDA 2027E'], metrics: [navps, m.ebitda['2027E']] };
  }

  const ARCH = { royalty, gold_producer: goldProducer, ep_cashflow: epCashflow, oil_sands: oilSands };

  function run(c, deck) {
    const S = (k) => sc(c, k, deck);
    const r = ARCH[c.company.archetype](c, deck);
    const m = r.m, price = S('price'), fx = S('fx_price'), sh = S('shares');
    const priceModel = price * fx, mcap = priceModel * sh, ev = mcap + S('netdebt_now');
    const ke = S('rf') + S('beta') * S('erp');
    const dw = S('gross_debt') / (S('gross_debt') + mcap);
    const wacc = ke * (1 - dw) + S('kd') * (1 - S('tax_rate')) * dw;
    const w1 = S('w1'), blend = w1 * r.v1 + (1 - w1) * r.v2, blendPx = blend / fx;
    const target = mround(blendPx, S('round_to'));
    const retPx = target / price - 1, retDiv = S('dps_fwd') / price, retAll = retPx + retDiv;
    const rating = retAll > S('buy_band') ? 'Buy' : (retAll >= 0 ? 'Hold' : 'Sell');
    let pv = 0; F.forEach((p, i) => pv += m.fcff[p] / Math.pow(1 + wacc, i + 1));
    const g = S('g_term'), tv = m.fcff['2030E'] * (1 + g) / (wacc - g), pvTv = tv / Math.pow(1 + wacc, 4);
    const dcfPs = (pv + pvTv - m.netdebt['2026E'] + S('investments')) / sh;
    const gImpl = ke - m.cfps['2027E'] / priceModel;
    let riPs = null, peJust = null;
    if (c.company.has_ri) {
      let s = 0, ri = 0;
      F.forEach((p, i) => { ri = m.ni[p] - ke * m.equity[prev[p]]; s += ri / Math.pow(1 + ke, i + 1); });
      riPs = (m.equity['2026E'] + s + ri / ke / Math.pow(1 + ke, 4)) / sh;
      const payout = m.dps['2027E'] / m.eps['2027E'], roe = m.ni['2027E'] / ((m.equity['2026E'] + m.equity['2027E']) / 2), gs = (1 - payout) * roe;
      peJust = ke > gs ? payout / (ke - gs) : null;
    }
    const out = { ...r.extra, target, rating, ret_all: retAll, ret_px: retPx, ret_div: retDiv, v1: r.v1, v2: r.v2, blend, blend_px: blendPx,
      ke, wacc, dcf_ps: dcfPs, g_impl: gImpl, ri_ps: riPs, pe_just: peJust, price, price_model: priceModel, mcap, ev,
      methods: r.methods, metrics: r.metrics, ccy: c.company.price_ccy, model_ccy: c.company.model_ccy, fx };
    out.checks = checks(c, out, m);
    out.all_checks = out.checks.every(x => x.pass);
    return { out, m };
  }

  function checks(c, o, m) {
    const p = c.published, near = (a, b) => Math.abs(a - b) <= Math.max(0.01, Math.abs(b) * 0.005);
    const L = [['Price target equals the published target', o.target, p.target], ['Rating equals the published rating', o.rating, p.rating]];
    const a = c.company.archetype;
    if (a === 'royalty') L.push(['NAV per share', o.navps, p.navps], ['2026E adjusted EPS', m.eps['2026E'], p.eps_2026], ['2027E CFPS', m.cfps['2027E'], p.cfps_2027]);
    if (a === 'gold_producer') L.push(['NAV per share', o.navps, p.navps], ['2026E adjusted EPS', m.eps['2026E'], p.eps_2026], ['2027E CFPS', m.cfps['2027E'], p.cfps_2027], ['2028E free cash flow', m.fcf['2028E'], p.fcf_2028]);
    if (a === 'ep_cashflow') L.push(['2027E funds flow per share', m.cfps['2027E'], p.cfps_2027], ['2027E free funds flow', m.fff['2027E'], p.fff_2027], ['Net debt, Dec 2026E', m.netdebt['2026E'], p.nd_2026], ['Dividend breakeven WTI', o.be_wti, p.be_wti]);
    if (a === 'oil_sands') L.push(['2027E adjusted EBITDA', m.ebitda['2027E'], p.ebitda_2027], ['2027E AFF per share', m.cfps['2027E'], p.cfps_2027], ['Blended value (C$)', o.blend, p.target_cad], ['NAV per share', o.navps, p.navps]);
    return L.map(([label, model, exp]) => ({ label, model, expected: exp, pass: typeof exp === 'string' ? model === exp : near(model, exp) }));
  }

  return { run, P, F, num };
})();
if (typeof module !== 'undefined') module.exports = NW;
