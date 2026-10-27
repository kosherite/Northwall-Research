"""Royalty and streaming company (e.g. Franco-Nevada).
Revenue = GEOs sold x gold price x realization. No operating or capital cost exposure;
growth comes from acquisitions, which are treated as discretionary investment."""
from archetypes._nav import nav_sheet
from engine import FMT

def lines(cfg):
    return [
        dict(section='Volumes and price'),
        dict(key='geo', label='GEOs sold', unit='koz', fmt='n1', spec={'A': '={geo}', 'H1': '={geo}', 'H2': '={geo}', 'F': '={geo}', 'FY': 'sum'}),
        dict(key='gold', label='Gold price, house deck', unit='US$/oz', fmt='m0', spec={'H2': '={gold}', 'F': '={gold}'}),
        dict(key='rev_geo', label='Revenue per GEO', unit='US$/oz', fmt='m0', spec={'all': '=[rev]/[geo]*1000'}, note='Realized revenue per GEO'),
        dict(section='Income statement'),
        dict(key='rev', label='Revenue', unit='US$M', bold=True, spec={'A': '={revenue_act}', 'H1': '={revenue_act}', 'H2': '=[geo]*[gold]*{{realization}}/1000', 'F': '=[geo]*[gold]*{{realization}}/1000', 'FY': 'sum'}, note='GEOs x deck gold x realization'),
        dict(key='cos', label='Costs of sales (excl. depletion)', unit='US$M', spec={'A': '={cos_act}', 'H1': '={cos_act}', 'H2': '=[rev]*{{cos_pct}}', 'F': '=[rev]*{{cos_pct}}', 'FY': 'sum'}),
        dict(key='ga', label='G&A and share-based compensation', unit='US$M', spec={'A': '={ga_act}', 'H1': '={ga_act}', 'H2': '={ga}', 'F': '={ga}', 'FY': 'sum'}),
        dict(key='ebitda', label='Adjusted EBITDA', unit='US$M', bold=True, spec={'A': '={ebitda_act}', 'H1': '={ebitda_act}', 'H2': '=[rev]-[cos]-[ga]', 'F': '=[rev]-[cos]-[ga]', 'FY': 'sum'}),
        dict(key='margin', label='Adjusted EBITDA margin', unit='%', fmt='pct', spec={'all': '=[ebitda]/[rev]'}),
        dict(key='da', label='Depletion and depreciation', unit='US$M', spec={'A': '={da_act}', 'H1': '={da_act}', 'H2': '=[geo]*{da_per_geo}/1000', 'F': '=[geo]*{da_per_geo}/1000', 'FY': 'sum'}),
        dict(key='fin', label='Finance income', unit='US$M', spec={'H2': '={fin_income}', 'F': '={fin_income}'}),
        dict(key='pretax', label='Adjusted pre-tax income', unit='US$M', spec={'H2': '=[ebitda]-[da]+[fin]', 'F': '=[ebitda]-[da]+[fin]'}),
        dict(key='taxes', label='Income taxes', unit='US$M', spec={'H2': '=[pretax]*{{tax_rate}}', 'F': '=[pretax]*{{tax_rate}}'}),
        dict(key='ni', label='Adjusted net income', unit='US$M', bold=True, spec={'A': '={ni_act}', 'H1': '={ni_act}', 'H2': '=[pretax]-[taxes]', 'F': '=[pretax]-[taxes]', 'FY': 'sum'}),
        dict(key='shares', label='Basic shares', unit='M', fmt='n1', spec={'all': '={shares}'}),
        dict(key='eps', label='Adjusted EPS', unit='US$', fmt='ps', bold=True, spec={'all': '=[ni]/[shares]'}),
        dict(section='Cash flow'),
        dict(key='ocf', label='Operating cash flow', unit='US$M', bold=True, spec={'A': '={ocf_act}', 'H1': '={ocf_act}', 'H2': '=[ebitda]+[fin]-{{cash_tax_share}}*[taxes]', 'F': '=[ebitda]+[fin]-{{cash_tax_share}}*[taxes]', 'FY': 'sum'}, note='EBITDA + finance income - cash taxes'),
        dict(key='cfps', label='Cash flow per share', unit='US$', fmt='ps', bold=True, spec={'all': '=[ocf]/[shares]'}),
        dict(key='fcff', label='Free cash flow to the firm (pre-acquisitions)', unit='US$M', spec={'F': '=[ocf]'}, note='No sustaining capital; acquisitions are discretionary growth'),
        dict(key='dps', label='Dividend per share', unit='US$', fmt='ps', spec={'A': '={dps}', 'H1': '={dps}', 'H2': '={dps}', 'F': '={dps}', 'FY': 'sum'}),
        dict(key='divpaid', label='Dividends paid', unit='US$M', spec={'H2': '=[dps]*[shares]', 'F': '=[dps]*[shares]'}),
        dict(key='acq', label='Acquisitions of royalties and streams', unit='US$M', spec={'H2': '={acquisitions}', 'F': '={acquisitions}'}, note='No production credit taken for unannounced deals'),
        dict(section='Balance sheet'),
        dict(key='cash', label='Cash and equivalents, period end', unit='US$M', bold=True, spec={'A': '={cash_act}', 'H1': '={cash_act}', 'H2': '=[cash<]+[ocf]-[divpaid]-[acq]', 'F': '=[cash<]+[ocf]-[divpaid]-[acq]', 'FY': 'last'}),
        dict(key='netdebt', label='Net debt (negative = net cash)', unit='US$M', spec={'all': '=-[cash]'}, note='No debt drawn'),
        dict(key='equity', label="Shareholders' equity, period end", unit='US$M', spec={'A': '={equity_act}', 'H1': '={equity_act}', 'H2': '=[equity<]+[ni]-[divpaid]', 'F': '=[equity<]+[ni]-[divpaid]', 'FY': 'last'}, note='Rolled forward: + NI - dividends (OCI ignored)'),
    ]


def target_methods(m, ws, r):
    S = m.S
    years = list(range(2027, 2061))
    lbl = {2027: '2027E', 2028: '2028E', 2029: '2029E', 2030: '2030E'}
    def geo(y, L, P, R):
        if y in lbl: return f"={m.M('geo', lbl[y])}"
        if y <= 2035: return f"={S('nav_flat_geo')}"
        return f"={P}{R['geo']}*(1-{S('nav_decline')})"
    def gold(y, L, P, R):
        return f"={m.I('gold', lbl[y])}" if y in lbl else f"={S('gold_lt')}"
    rows = [
        ('geo', 'GEOs', 'koz', 'n1', geo),
        ('gold', 'Gold price', 'US$/oz', 'm0', gold),
        ('ebitda', 'EBITDA', 'US$M', 'm0', lambda y, L, P, R: f"={L}{R['geo']}*{L}{R['gold']}*{S('realization')}/1000*(1-{S('cos_pct')})-{S('nav_ga')}"),
        ('cf', 'After-tax cash flow', 'US$M', 'm0', lambda y, L, P, R: f"={L}{R['ebitda']}*(1-{S('nav_cash_tax')})"),
        ('df', 'Discount factor (mid-year)', '', 'n3', lambda y, L, P, R: f"=1/(1+{S('nav_disc')})^({y}-2026-0.5)"),
        ('pv', 'Present value', 'US$M', 'm0', lambda y, L, P, R: f"={L}{R['cf']}*{L}{R['df']}"),
        ('opt', 'Cobre Panamá restart cash flow (unrisked)', 'US$M', 'm0', lambda y, L, P, R: f"=IF(AND({y}>={S('cobre_start')},{y}<=2050),{S('cobre_geo')}*{S('gold_lt')}*{S('realization')}/1000*(1-{S('cos_pct')})*(1-{S('nav_cash_tax')}),0)"),
        ('optpv', 'Cobre Panamá present value (unrisked)', 'US$M', 'm0', lambda y, L, P, R: f"={L}{R['opt']}*{L}{R['df']}"),
    ]
    nws, R, rr, a, b = nav_sheet(m, f"{m.cfg['company']['name']} — Net asset value (5% real, Dec 31, 2026)",
                                 'Portfolio GEOs per Model to 2030E, flat to 2035, then a 4% annual decline to 2060.', years, rows)
    m.block(nws, rr, [
        ('#', 'NAV summary'),
        ('nav_port', 'Royalty and stream portfolio', f"=SUM({a}{R['pv']}:{b}{R['pv']})", 'm0', ''),
        ('nav_cobre_full', 'Cobre Panamá restart, unrisked', f"=SUM({a}{R['optpv']}:{b}{R['optpv']})", 'm0', ''),
        ('nav_cobre', 'Cobre Panamá restart, risked', None, 'm0', 'x probability'),
        ('nav_expl', 'Exploration and undeveloped optionality', f"={S('nav_exploration')}", 'm0', ''),
        ('nav_cash', 'Cash, Dec 31, 2026E', f"={m.M('cash', '2026E')}", 'm0', ''),
        ('nav_inv', 'Equity investments', f"={S('investments')}", 'm0', ''),
        ('nav', 'Net asset value', None, 'm0', ''),
        ('navps', 'NAV per share (US$)', None, 'ps', ''),
        ('cobre_ps', 'Risked Cobre Panamá value per share', None, 'ps', ''),
    ])
    c = lambda k: nws[m.ref(k).split('!')[1].replace('$', '')]
    c('nav_cobre').value = f"={m.ref('nav_cobre_full')}*{S('cobre_prob')}"
    c('nav').value = f"=SUM({m.ref('nav_port')},{m.ref('nav_cobre')},{m.ref('nav_expl')},{m.ref('nav_cash')},{m.ref('nav_inv')})"
    c('navps').value = f"={m.ref('nav')}/{S('nav_shares')}"
    c('cobre_ps').value = f"={m.ref('nav_cobre')}/{S('nav_shares')}"
    m.out('navps', m.ref('navps')); m.out('cobre_ps', m.ref('cobre_ps'))
    r = m.block(ws, r, [
        ('#', 'Target method 1: P/NAV — method 2: P/CF'),
        ('navps_v', 'NAV per share (NAV sheet)', f"={m.ref('navps')}", 'ps', ''),
        ('mult1', 'Target P/NAV multiple', f"={S('mult1')}", 'x', m.cfg['scalars']['mult1']['source']),
        ('v1', 'Method 1 value per share', None, 'ps', ''),
        ('cf27', 'Cash flow per share, 2027E', f"={m.M('cfps', '2027E')}", 'ps', ''),
        ('mult2', 'Target P/CF multiple, 2027E', f"={S('mult2')}", 'x', m.cfg['scalars']['mult2']['source']),
        ('v2', 'Method 2 value per share', None, 'ps', ''),
    ])
    ws[m.ref('v1').split('!')[1].replace('$', '')] = f"={m.ref('navps_v')}*{m.ref('mult1')}"
    ws[m.ref('v2').split('!')[1].replace('$', '')] = f"={m.ref('cf27')}*{m.ref('mult2')}"
    return r


def sens_axes(m):
    S = m.S
    return dict(m1=[1.5, 1.75, 2.0, 2.25, 2.5], m1_fmt='0.00"x"', m1_label='P/NAV',
                m2=[20, 22.5, 25, 27.5, 30], m2_fmt='0.0"x"', m2_label='P/CF 2027E',
                formula=lambda a, b: f"=({S('w1')}*{a}*{m.ref('navps_v')}+(1-{S('w1')})*{b}*{m.ref('cf27')})/{S('fx_price')}")


def ratio_lines():
    F = ['2025A', '2026E', '2027E', '2028E', '2029E', '2030E']
    G = ['2026E', '2027E', '2028E', '2029E', '2030E']
    return [
        dict(label='Adjusted EBITDA margin', tmpl='=[ebitda]/[rev]', periods=F),
        dict(label='Net margin (adjusted NI / revenue)', tmpl='=[ni]/[rev]', periods=F),
        dict(label='Equity turnover (revenue / average equity)', tmpl='=[rev]/AVERAGE([equity<],[equity])', fmt='n2', periods=G),
        dict(label='Return on average equity', tmpl='=[ni]/AVERAGE([equity<],[equity])', periods=G, note='Two-step DuPont: net margin x equity turnover (no debt, so leverage ~1.0x)'),
        dict(label='Cash conversion (operating cash flow / net income)', tmpl='=[ocf]/[ni]', fmt='n2', periods=F),
        dict(label='Dividend payout (DPS / EPS)', tmpl='=[dps]/[eps]', periods=F),
        dict(label='Reinvestment rate ((dividends + acquisitions) / OCF)', tmpl='=([divpaid]+[acq])/[ocf]', periods=['2027E', '2028E', '2029E', '2030E']),
    ]


def checks(m):
    p = m.cfg['published']
    return [
        ('NAV per share equals the published NAVPS', f"={m.ref('navps')}", p['navps'], 'num'),
        ('2026E adjusted EPS equals the published estimate', f"={m.M('eps', '2026E')}", p['eps_2026'], 'num'),
        ('2027E CFPS equals the published estimate', f"={m.M('cfps', '2027E')}", p['cfps_2027'], 'num'),
        ('2026E revenue = H1 actual + H2 estimate', f"={m.M('rev', '2026E')}", f"={m.M('rev', 'H1-26A')}+{m.M('rev', 'H2-26E')}", 'num'),
    ]
