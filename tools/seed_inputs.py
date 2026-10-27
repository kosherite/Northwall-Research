#!/usr/bin/env python3
"""One-off: writes the initial coverage/<TICKER>/model_inputs.yaml files from the October 27, 2026
initiation work. After this first run, the YAML files are the source of truth and are edited directly."""
import yaml
from pathlib import Path

R = Path(__file__).resolve().parents[1] / 'coverage'


def S(label, value, source, unit='', fmt='n2', key=False):
    d = dict(label=label, unit=unit, value=value, fmt=fmt, source=source)
    if key:
        d['key_assumption'] = True
    return d


def V(label, values, source, unit='', fmt='m'):
    return dict(label=label, unit=unit, fmt=fmt, values=values, source=source)


def F4(a, b, c, d):
    return {'2027E': a, '2028E': b, '2029E': c, '2030E': d}


def common(price, src, fx, shares, nd, beta, bsrc, kd, tax, gd, m1, m1s, m2, m2s, dps, dsrc, rnd, g, inv):
    return {
        'price': S('Share price', price, src, fmt='ps'),
        'fx_price': S('Model currency per listing currency', fx, 'USD/CAD 1.402 on Oct 27, 2026 (fxfeed.io)' if fx != 1 else 'Same currency', fmt='n3'),
        'shares': S('Basic shares outstanding', shares, 'Latest company filing', 'M', 'n1'),
        'netdebt_now': S('Net debt at last balance sheet (negative = net cash)', nd, 'Latest quarterly filing', 'M', 'm0'),
        'beta': S('Equity beta', beta, bsrc, fmt='n2', key='assumption' in bsrc.lower()),
        'kd': S('Pre-tax cost of debt', kd, 'Northwall assumption: credit facility pricing', fmt='pct'),
        'tax_rate': S('Marginal tax rate', tax, 'Statutory combined rate', fmt='pct'),
        'gross_debt': S('Gross debt', gd, 'Latest quarterly filing', 'M', 'm0'),
        'w1': S('Weight on valuation method 1', 0.5, 'Northwall method: equal weight', fmt='pct'),
        'mult1': S('Target multiple, method 1', m1, m1s, fmt='n2', key=True),
        'mult2': S('Target multiple, method 2', m2, m2s, fmt='n2', key=True),
        'dps_fwd': S('Next-12-month dividend per share', dps, dsrc, fmt='ps'),
        'round_to': S('Target rounding increment', rnd, 'House style', fmt='n2'),
        'buy_band': S('Buy threshold: expected 12-month total return', 0.15, 'Northwall rating definitions', fmt='pct'),
        'g_term': S('Terminal growth for DCF cross-check (nominal)', g, 'Northwall: 0% for depleting oil assets, 2% for long-life gold portfolios', fmt='pct'),
        'investments': S('Investments not captured in FCFF', inv, 'Balance sheet', 'M', 'm0'),
    }


def LOG(eff):
    return [dict(date='2026-10-27', version='v2026Q2', change='Model built on house template from Q2-26 filings; ties to the published 2026-10-27 report', effect=eff)]


fnv = dict(
    company=dict(name='Franco-Nevada Corporation', ticker='FNV', exchange='NYSE/TSX', sector='Gold royalties and streaming', archetype='royalty',
                 analyst='Basel Al-Ghousein', price_ccy='USD', model_ccy='USD', has_ri=True, version='v2026Q2', model_date='2026-10-27'),
    deck_uses=['gold', 'gold_lt', 'rf', 'erp'],
    series={
        'geo': V('GEOs sold', {'2025A': 519.106, 'H1-26A': 268.758, 'H2-26E': 283.0, **F4(572, 570, 585, 600)}, '2025A: 2025 results (Mar 10, 2026). H1-26A: Q2-26 release (Aug 11, 2026). H2-26E: Northwall, Q3 138k + Q4 145k incl. Cobre stockpile deliveries. 2027E+: Northwall, inside the 555-615k 2030 outlook', 'koz', 'n3'),
        'revenue_act': V('Revenue, reported', {'2025A': 1822.8, 'H1-26A': 1231.6}, '2025 results; Q2-26 release income statement', 'US$M'),
        'cos_act': V('Costs of sales, reported', {'2025A': 168.8, 'H1-26A': 92.4}, '2025 results; Q2-26 release income statement', 'US$M'),
        'ga_act': V('G&A + share-based comp, reported', {'2025A': 35.3, 'H1-26A': 19.7}, '2025A G&A only; H1-26A G&A 17.0 + SBC 2.7 (Q2-26 release)', 'US$M'),
        'ebitda_act': V('Adjusted EBITDA, reported', {'2025A': 1656.1, 'H1-26A': 1121.6}, '2025 results; Q2-26 release non-GAAP reconciliation', 'US$M'),
        'da_act': V('Depletion and depreciation, reported', {'2025A': 306.7, 'H1-26A': 161.9}, '2025 results; Q2-26 release', 'US$M'),
        'ni_act': V('Adjusted net income, reported', {'2025A': 1075.2, 'H1-26A': 807.5}, '2025 results; Q2-26 release (includes the US$63.8M buy-back gain, no longer excluded)', 'US$M'),
        'ocf_act': V('Operating cash flow, reported', {'2025A': 1493.7, 'H1-26A': 1002.9}, '2025 results; Q2-26 release cash flow statement', 'US$M'),
        'cash_act': V('Cash, reported', {'2025A': 670.9, 'H1-26A': 1014.2}, 'Balance sheets Dec 31, 2025 and Jun 30, 2026', 'US$M'),
        'equity_act': V("Shareholders' equity, reported", {'2025A': 7635.3, 'H1-26A': 8240.7}, 'Balance sheets Dec 31, 2025 and Jun 30, 2026', 'US$M'),
        'da_per_geo': V('Depletion per GEO', {'H2-26E': 635, **F4(645, 650, 655, 660)}, 'Northwall: Q2-26 run-rate US$634/GEO (84.0 / 132.4k), rising with new assets', 'US$/oz', 'm0'),
        'fin_income': V('Finance income', {'H2-26E': 14, **F4(30, 30, 30, 30)}, 'Northwall: H1-26 US$12.3M run-rate', 'US$M'),
        'ga': V('G&A + share-based comp', {'H2-26E': 21, **F4(43.26, 44.56, 45.9, 47.27)}, 'Northwall: US$42M a year growing 3%', 'US$M', 'n2'),
        'acquisitions': V('Acquisitions', {'H2-26E': 60, **F4(500, 500, 500, 500)}, 'Northwall: H2 includes Comet Vale (US$8.4M); US$500M a year thereafter, no production credited', 'US$M'),
        'shares': V('Basic shares', {'2025A': 192.7, 'H1-26A': 192.8, 'H2-26E': 193.0, '2026E': 193.0, **F4(193.4, 193.8, 194.2, 194.6)}, 'Weighted basic shares per filings; DRIP issuance thereafter', 'M', 'n1'),
        'dps': V('Dividend per share', {'2025A': 1.52, 'H1-26A': 0.88, 'H2-26E': 0.88, **F4(1.92, 2.08, 2.24, 2.40)}, 'US$0.38 x 4 (2025); US$0.44 quarterly (2026); Northwall +US$0.16/yr', 'US$', 'ps'),
    },
    scalars={**common(230.76, 'NYSE close Oct 26, 2026 (Upstox)', 1, 192.9, -1014.2, 0.58, 'Beta 0.58 (Motley Fool, Oct 2026)', 0.055, 0.22, 0,
                      2.0, 'Northwall: premium for diversification and a debt-free balance sheet', 25, 'Northwall: near trailing P/CF of ~25x (Morningstar)',
                      1.76, 'US$0.44 quarterly (Q2-26 release)', 5, 0.02, 1215.1),
             'realization': S('Realized revenue per GEO vs. deck gold', 0.97, 'Northwall: H1-26 revenue per GEO ran 96-98% of LBMA', fmt='pct'),
             'cos_pct': S('Costs of sales, % of revenue', 0.078, 'Q2-26: 45.9 / 580.9 = 7.9%', fmt='pct'),
             'tax_rate': S('Effective tax rate', 0.22, 'H1-26: 231.2 / 1,053.8 = 21.9%', fmt='pct'),
             'cash_tax_share': S('Cash share of income taxes', 0.8, 'Northwall: deferred tax ~30% of expense in H1-26', fmt='pct'),
             'nav_flat_geo': S('NAV: GEOs held flat 2031-2035', 600, 'Northwall', 'koz', 'm0'),
             'nav_decline': S('NAV: annual GEO decline after 2035', 0.04, 'Northwall', fmt='pct'),
             'nav_ga': S('NAV: annual G&A', 42, 'Northwall', 'US$M', 'm0'),
             'nav_cash_tax': S('NAV: cash taxes as % of EBITDA', 0.19, 'Northwall', fmt='pct'),
             'nav_disc': S('NAV discount rate (real)', 0.05, 'Northwall house rate for precious metals', fmt='pct', key=True),
             'cobre_start': S('Cobre Panamá restart year', 2029, 'Northwall assumption', fmt='int'),
             'cobre_geo': S('Cobre Panamá restart GEOs a year', 150, 'Company: 150-175k GEOs at full capacity (2025 results); Northwall uses the low end', 'koz', 'm0'),
             'cobre_prob': S('Cobre Panamá restart probability', 0.35, 'Northwall assumption', fmt='pct', key=True),
             'nav_exploration': S('Exploration and undeveloped optionality', 2000, 'Northwall assumption (~US$10/share)', 'US$M', 'm0'),
             'nav_shares': S('NAV share count', 193.0, '2026E basic shares', 'M', 'n1')},
    comps=dict(note='Senior royalty and streaming peers, H1-26 annualized (Royal Gold: Q2-26 annualized). Prices: FNV and RGLD Oct 26, WPM Oct 27, 2026.',
               source='Company Q2-26 filings; Northwall calculations', columns=['Company', 'Ticker', 'Price (US$)', 'Mkt cap (US$B)', 'P/E', 'P/CF', 'Net cash (US$B)'],
               rows=[['Franco-Nevada', 'FNV', 230.76, 44.5, 27.5, 22.2, 1.0], ['Wheaton Precious Metals', 'WPM', 124.59, 56.6, 25.1, 20.0, -1.9], ['Royal Gold', 'RGLD', 234.11, 19.8, 22.9, 14.8, -0.3]]),
    published=dict(target=250, rating='Hold', navps=138.88, eps_2026=7.72, cfps_2027=9.00, date='2026-10-27'),
    log=LOG('Target US$250, Hold'))

agi = dict(
    company=dict(name='Alamos Gold Inc.', ticker='AGI', exchange='NYSE/TSX', sector='Gold producers', archetype='gold_producer',
                 analyst='Basel Al-Ghousein', price_ccy='USD', model_ccy='USD', has_ri=True, version='v2026Q2', model_date='2026-10-27'),
    deck_uses=['gold', 'gold_lt', 'rf', 'erp'],
    series={
        'oz': V('Gold production', {'2025A': 545.4, 'H1-26A': 254.5, 'H2-26E': 280.5, **F4(640, 770, 870, 960)}, '2025A: Q4-25 release. H1-26A: Q2-26 release. H2-26E: Northwall, inside revised 510-560k guidance. 2027E+: Northwall, below original 3-yr guidance (650-730k, 755-835k) and the ~1 Moz by 2030 target', 'koz', 'n1'),
        'gold_real_act': V('Realized gold price, reported', {'2025A': 3372, 'H1-26A': 4660}, 'Q4-25 release; Q2-26 release', 'US$/oz', 'm0'),
        'rev_act': V('Revenue, reported', {'2025A': 1808.8, 'H1-26A': 1190.8}, 'Q4-25 release; Q2-26 release', 'US$M'),
        'aisc': V('AISC', {'2025A': 1524, 'H1-26A': 1793, 'H2-26E': 1855, **F4(1550, 1350, 1250, 1200)}, 'Reported 2025 and H1-26; H2-26E implied by the US$1,825 guidance midpoint; Northwall thereafter (IGD expansion AISC US$1,025, Lynn Lake US$829 per company)', 'US$/oz', 'm0'),
        'eps_act': V('Adjusted EPS, reported', {'2025A': 1.40, 'H1-26A': 1.14}, 'Q4-25 release; Q2-26 release', 'US$', 'ps'),
        'ocf_act': V('Operating cash flow, reported', {'2025A': 795.3, 'H1-26A': 474.3}, 'Q4-25 release; Q2-26 release', 'US$M'),
        'fcf_act': V('Free cash flow, reported', {'2025A': 351.7, 'H1-26A': 245.2}, 'Q4-25 release; Q2-26 release', 'US$M'),
        'growth_capex': V('Growth capital', {'H2-26E': 345, **F4(600, 420, 150, 0)}, 'Northwall: 2026 guidance US$657-720M less H1; Lynn Lake US$871M remaining, IGD mill, PDA', 'US$M'),
        'expl': V('Capitalized exploration', {'H2-26E': 30, **F4(60, 60, 60, 60)}, '2026 guidance US$60M', 'US$M'),
        'shares': V('Basic shares', {'2025A': 420.0, 'H1-26A': 419.8, 'H2-26E': 418.6, '2026E': 418.6, **F4(418.6, 418.6, 418.6, 418.6)}, 'Weighted basic shares per filings; Mar 31 count 419.96M less 1.40M bought back in Q2', 'M', 'n1'),
        'dps': V('Dividend per share', {'2025A': 0.10, 'H1-26A': 0.08, 'H2-26E': 0.08, **F4(0.16, 0.16, 0.16, 0.16)}, 'US$0.04 quarterly after the Q1-26 increase', 'US$', 'ps'),
        'buybacks': V('Share buybacks', {'H2-26E': 50, **F4(0, 0, 0, 0)}, 'Northwall: Q2-26 pace for H2; none assumed thereafter', 'US$M'),
        'netdebt_act': V('Net debt, reported (negative = net cash)', {'H1-26A': -436.9}, 'Cash US$636.9M (Jun 30, 2026) less US$200M drawn (Mar 31, 2026 statements)', 'US$M'),
        'equity_act': V("Shareholders' equity, reported", {'H1-26A': 4607.8}, 'Mar 31, 2026 interim statements (proxy for Jun 30)', 'US$M'),
    },
    scalars={**common(30.21, 'NYSE close Oct 26, 2026 (Stock Analysis)', 1, 418.6, -436.9, 1.0, 'Northwall assumption pending sourcing', 0.06, 0.25, 200,
                      1.0, 'Northwall: in line with intermediate producers at a long-term deck below spot', 10, 'Northwall: below Alamos trailing 13.7x, above Kinross 5.8x',
                      0.16, 'US$0.04 quarterly (Q2-26 release)', 1, 0.02, 0),
             'mining_tax': S('Effective income and mining tax rate', 0.25, 'Northwall: Canadian and Mexican income and mining taxes', fmt='pct'),
             'sust_per_oz': S('Sustaining capital per oz (inside AISC)', 450, 'Northwall: 2026 sustaining guidance US$228-255M / ~535k oz', 'US$/oz', 'm0'),
             'da_excess': S('Depreciation in excess of sustaining capital', 200, 'Northwall: calibrated to H1-26 adjusted EPS', 'US$/oz', 'm0'),
             'nav_flat_oz': S('NAV: production held flat 2031-2036', 960, 'Northwall', 'koz', 'm0'),
             'nav_decline': S('NAV: annual decline after 2036', 0.07, 'Northwall; 15.9 Moz reserves at YE2025', fmt='pct'),
             'aisc_lt': S('NAV: long-term AISC', 1200, 'Northwall', 'US$/oz', 'm0'),
             'expl_lt': S('NAV: long-term exploration', 30, 'Northwall', 'US$M', 'm0'),
             'nav_disc': S('NAV discount rate (real)', 0.05, 'Northwall house rate for precious metals', fmt='pct', key=True)},
    comps=dict(note='Gold peers, Q2-26 annualized. Prices as of Oct 26, 2026.', source='Company Q2-26 filings; Northwall calculations',
               columns=['Company', 'Ticker', 'Price (US$)', 'Mkt cap (US$B)', 'P/E', 'P/CF', 'AISC (US$/oz)', 'FCF yield'],
               rows=[['Alamos Gold', 'AGI', 30.21, 12.6, 12.8, 13.7, 1728, '4.5%'], ['Agnico Eagle', 'AEM', 175.69, 88.2, 14.3, 10.3, 1459, '6.1%'], ['Kinross Gold', 'KGC', 22.45, 26.6, 7.9, 5.8, 1821, '10.9%']]),
    published=dict(target=39, rating='Buy', navps=42.35, eps_2026=2.22, cfps_2027=3.50, fcf_2028=934.88, date='2026-10-27'),
    log=LOG('Target US$39, Buy'))

wcp = dict(
    company=dict(name='Whitecap Resources Inc.', ticker='WCP', exchange='TSX', sector='Canadian oil and gas producers', archetype='ep_cashflow',
                 analyst='Basel Al-Ghousein', price_ccy='CAD', model_ccy='CAD', has_ri=False, version='v2026Q2', model_date='2026-10-27'),
    deck_uses=['wti', 'rf', 'erp'],
    series={
        'prod': V('Production', {'H1-26A': 390.155, 'H2-26E': 382.5, **F4(397, 409, 421.3, 433.9)}, 'H1-26A: Q1 391,416 and Q2 388,894 boe/d (releases). H2-26E: Northwall, Q3 380k / Q4 385k vs 384-386k FY guidance. 2027E+: 3% growth (company base case)', 'kboe/d', 'n1'),
        'days': V('Days', {'H1-26A': 181, 'H2-26E': 184, **F4(365, 365, 365, 365)}, 'Calendar', 'days', 'int'),
        'ff_act': V('Funds flow, reported', {'H1-26A': 2379.9}, 'Q1-26 C$1,025.3M + Q2-26 C$1,354.6M (releases)', 'C$M'),
        'capex_act': V('Capital expenditures, reported', {'H1-26A': 1106.4}, 'Q1-26 C$676.3M + Q2-26 C$430.1M', 'C$M'),
        'capex': V('Capital expenditures', {'H2-26E': '=2100-1106.4', **F4(2100, 2100, 2100, 2100)}, 'High end of the C$2.0-2.1B 2026 budget (Q2-26 release); held flat', 'C$M'),
        'shares': V('Basic shares', {'H1-26A': 1215.7, 'H2-26E': 1215.7, '2026E': 1215.7, **F4(1215.7, 1215.7, 1215.7, 1215.7)}, 'Q2-26 release: 1,215.7M; no buybacks assumed', 'M', 'n1'),
        'dps': V('Dividend per share', {'H1-26A': 0.36, 'H2-26E': 0.3648, **F4(0.7296, 0.7296, 0.7296, 0.7296)}, 'C$0.0608 monthly (Oct 15, 2026 release)', 'C$', 'ps'),
        'netdebt_act': V('Net debt, reported', {'H1-26A': 2516.8}, 'Q2-26 release', 'C$M'),
    },
    scalars={**common(20.43, 'TSX close Oct 23, 2026 (Stock Analysis)', 1, 1215.7, 2516.8, 0.69, '5-year beta 0.69 (Stock Analysis)', 0.055, 0.23, 2516.8,
                      6.5, 'Northwall: modest premium to the current 6.0x for inventory, liquids and 0.5x leverage', 0.08, 'Northwall target free funds flow yield',
                      0.7296, 'C$0.0608 monthly', 1, 0.0, 0),
             'ff_anchor': S('Funds flow per boe, Q2-26 actual', '=1354.6/(388.894*91)*1000', 'Q2-26 funds flow / Q2-26 volume', 'C$/boe', 'n2'),
             'ff_sens': S('Funds flow sensitivity per US$1 WTI', 0.60, 'Northwall: ~52% oil and condensate weighting, royalties and FX', 'C$/boe', 'n2', key=True),
             'anchor_wti': S('WTI in the anchor quarter', 92.79, 'Q2-26 average WTI (Greenfire Q2-26 release)', 'US$/bbl', 'n2'),
             'at_interest': S('After-tax interest added back for DACF', 110, 'Northwall estimate', 'C$M', 'm0')},
    comps=dict(note='Canadian producers, Q2-26 annualized. Prices: WCP Oct 23, TOU Oct 22, SCR Oct 15, 2026.', source='Company Q2-26 filings; Northwall calculations',
               columns=['Company', 'Ticker', 'Price (C$)', 'Mkt cap (C$B)', 'EV/CF', 'FCF yield', 'Div yield', 'ND/CF'],
               rows=[['Whitecap', 'WCP', 20.43, 24.8, '5.0x', '14.9%', '3.6%', '0.5x'], ['Tourmaline', 'TOU', 65.86, 25.7, '8.6x', '3.0%', '3.0%', '0.5x'], ['Strathcona', 'SCR', 41.73, 8.9, '5.0x', '13.3%', '2.9%', '0.9x']]),
    published=dict(target=24, rating='Buy', cfps_2027=3.65, fff_2027=2335, nd_2026=1313, be_wti=63.4, date='2026-10-27'),
    log=LOG('Target C$24, Buy'))

gfr = dict(
    company=dict(name='Greenfire Resources Ltd.', ticker='GFR', exchange='NYSE/TSX', sector='Canadian oil sands', archetype='oil_sands',
                 analyst='Basel Al-Ghousein', price_ccy='USD', model_ccy='CAD', has_ri=False, version='v2026Q2', model_date='2026-10-27'),
    deck_uses=['wti', 'rf', 'erp'],
    series={
        'prod': V('Bitumen production', {'2025A': 16.169, '2026E': 22.5, **F4(40, 46, 50, 54)}, '2025A: YE2025 release. 2026E: Northwall, inside 21.5-23.5k guidance incl. Connacher from Aug 5. 2027E+: Northwall; Pads 7, 5SE, 8 and Great Divide infill toward the ~65k long-term plan', 'kbbl/d', 'n1'),
        'aff_act': V('Adjusted funds flow, reported', {'2025A': 143.5}, 'YE2025 release', 'C$M'),
        'capex_act': V('Capital expenditures, reported', {'2025A': 111.8}, 'YE2025 release', 'C$M'),
        'fcf_act': V('Adjusted free cash flow, reported', {'2025A': 31.7}, 'YE2025 release', 'C$M'),
        'interest': V('Interest', F4(45, 38, 32, 26), 'Northwall: ~C$570M drawn at ~7.5-8%, falling with debt', 'C$M'),
        'capex': V('Capital expenditures', F4(330, 300, 300, 300), 'Northwall: Connacher sustaining ~C$75M (company) + Hangingstone pads', 'C$M'),
        'shares': V('Basic shares', {'2026E': 240.4, **F4(240.4, 240.4, 240.4, 240.4)}, 'Rights offering closing (Sep 16, 2026): 240,413,692', 'M', 'n1'),
        'netdebt_ye': V('Net debt, Dec 31, 2026E', {'2026E': 530}, 'Northwall: ~C$570M drawn (rights offering release) less ~C$40M Q4 free cash flow', 'C$M'),
    },
    scalars={**common(7.00, 'NYSE close Oct 26, 2026 (StockScan)', 1.402, 240.4, 570, 1.3, 'Northwall assumption pending sourcing', 0.08, 0.23, 570,
                      0.85, 'Northwall: discount for a 72% controlling shareholder and thin float', 5.0, 'Northwall: in line with Strathcona at ~5.0x annualized EV/CF',
                      0, 'No dividend', 0.25, 0.0, 0),
             'ebitda_anchor': S('EBITDA per bbl at US$70 WTI', 32.5, 'Company: ~1.2x debt / 2027E EBITDA at US$70 with ~C$570M drawn -> ~C$475M / 40k bbl/d', 'C$/bbl', 'n2'),
             'ebitda_sens': S('EBITDA sensitivity per US$1 WTI', 1.17, 'Northwall: 1.38 USD/CAD x ~85% after royalties', 'C$/bbl', 'n2', key=True),
             'anchor_wti': S('WTI at the anchor', 70, 'Company guidance basis', 'US$/bbl', 'n2'),
             'pv10_gfr': S('Greenfire 2P after-tax PV10, YE2025', 1990, 'YE2025 reserves release', 'C$M', 'm0'),
             'nav_connacher': S('Connacher 2P value', 2000, 'Northwall estimate: 2P NAV10 before tax C$2,124M (acquisition release); no cash tax before 2030', 'C$M', 'm0', key=True),
             'current_prod': S('Current production', 34000, 'Company, pro forma Connacher (Q2-26 release)', 'bbl/d', 'm0')},
    comps=dict(note='Oil sands and heavy oil peers, EV per flowing barrel. GFR at US$7.00 x 1.402; SCR Oct 15; ATH Oct 16, 2026.', source='Company filings; Northwall calculations',
               columns=['Company', 'Ticker', 'Price (C$)', 'Mkt cap (C$B)', 'EV (C$B)', 'Production (bbl/d)', 'EV/flowing bbl (C$k)'],
               rows=[['Greenfire', 'GFR', 9.81, 2.4, 2.9, 34000, 86], ['Strathcona', 'SCR', 41.73, 8.9, 10.9, 117022, 93], ['Athabasca Oil', 'ATH', 12.15, 5.9, 5.8, 40000, 146]]),
    published=dict(target=8.25, rating='Buy', ebitda_2027=645.32, cfps_2027=2.50, target_cad=11.73, navps=14.39, date='2026-10-27'),
    log=LOG('Target US$8.25, Buy'))

if __name__ == '__main__':
    for t, d in [('FNV', fnv), ('AGI', agi), ('WCP', wcp), ('GFR', gfr)]:
        (R / t).mkdir(parents=True, exist_ok=True)
        with open(R / t / 'model_inputs.yaml', 'w') as fh:
            fh.write(f"# {d['company']['name']} ({t}) - model inputs. Owner: Research Associate.\n"
                     f"# Every value carries its source. Edit values here, then run: python tools/build_model.py {t}\n")
            yaml.safe_dump(d, fh, sort_keys=False, allow_unicode=True, width=200)
    print('seeded')
