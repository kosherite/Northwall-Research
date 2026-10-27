"""Gold producer (e.g. Alamos Gold). Cash flow is driven by ounces x (gold price - AISC),
with sustaining capital inside AISC and growth capital and exploration below it."""
from archetypes._nav import nav_sheet

def lines(cfg):
    calc = lambda f: {'H2': f, 'F': f}
    return [
        dict(section='Production and costs'),
        dict(key='oz', label='Gold production', unit='koz', fmt='n1', spec={'A': '={oz}', 'H1': '={oz}', 'H2': '={oz}', 'F': '={oz}', 'FY': 'sum'}),
        dict(key='gold', label='Realized gold price', unit='US$/oz', fmt='m0', spec={'A': '={gold_real_act}', 'H1': '={gold_real_act}', 'H2': '={gold}', 'F': '={gold}', 'FY': 'wavg:oz'}, note='Actuals as reported; forecasts at the house deck'),
        dict(key='aisc', label='All-in sustaining cost', unit='US$/oz', fmt='m0', spec={'A': '={aisc}', 'H1': '={aisc}', 'H2': '={aisc}', 'F': '={aisc}', 'FY': 'wavg:oz'}),
        dict(key='margin_oz', label='AISC margin', unit='US$/oz', fmt='m0', spec={'all': '=[gold]-[aisc]'}),
        dict(section='Income statement'),
        dict(key='rev', label='Revenue', unit='US$M', bold=True, spec={'A': '={rev_act}', 'H1': '={rev_act}', 'H2': '=[oz]*[gold]/1000', 'F': '=[oz]*[gold]/1000', 'FY': 'sum'}),
        dict(key='aisc_m', label='AISC margin', unit='US$M', spec={'A': '=[margin_oz]*[oz]/1000', 'H1': '=[margin_oz]*[oz]/1000', 'H2': '=[margin_oz]*[oz]/1000', 'F': '=[margin_oz]*[oz]/1000', 'FY': 'sum'}),
        dict(key='taxes', label='Income and mining taxes', unit='US$M', spec=calc('=[aisc_m]*{{mining_tax}}'), note='Effective rate on AISC margin'),
        dict(key='shares', label='Basic shares', unit='M', fmt='n1', spec={'all': '={shares}'}),
        dict(key='eps', label='Adjusted EPS', unit='US$', fmt='ps', bold=True, spec={'A': '={eps_act}', 'H1': '={eps_act}', 'H2': '=([gold]-[aisc]-{{da_excess}})*[oz]/1000*(1-{{mining_tax}})/[shares]', 'F': '=([gold]-[aisc]-{{da_excess}})*[oz]/1000*(1-{{mining_tax}})/[shares]', 'FY': 'sum'}, note='Depreciation in excess of sustaining capital deducted'),
        dict(key='ni', label='Adjusted net income', unit='US$M', spec={'A': '=[eps]*[shares]', 'H1': '=[eps]*[shares]', 'H2': '=[eps]*[shares]', 'F': '=[eps]*[shares]', 'FY': 'sum'}),
        dict(section='Cash flow'),
        dict(key='ocf', label='Operating cash flow', unit='US$M', bold=True, spec={'A': '={ocf_act}', 'H1': '={ocf_act}', 'H2': '=([gold]-[aisc]+{{sust_per_oz}})*[oz]/1000-[taxes]', 'F': '=([gold]-[aisc]+{{sust_per_oz}})*[oz]/1000-[taxes]', 'FY': 'sum'}),
        dict(key='cfps', label='Cash flow per share', unit='US$', fmt='ps', bold=True, spec={'all': '=[ocf]/[shares]'}),
        dict(key='sust', label='Sustaining capital', unit='US$M', spec=calc('={{sust_per_oz}}*[oz]/1000')),
        dict(key='growth', label='Growth capital', unit='US$M', spec=calc('={growth_capex}')),
        dict(key='expl', label='Capitalized exploration', unit='US$M', spec=calc('={expl}')),
        dict(key='fcf', label='Free cash flow', unit='US$M', bold=True, spec={'A': '={fcf_act}', 'H1': '={fcf_act}', 'H2': '=[ocf]-[sust]-[growth]-[expl]', 'F': '=[ocf]-[sust]-[growth]-[expl]', 'FY': 'sum'}),
        dict(key='fcff', label='Free cash flow to the firm', unit='US$M', spec={'F': '=[fcf]'}, note='After-tax interest on US$200M is immaterial'),
        dict(key='dps', label='Dividend per share', unit='US$', fmt='ps', spec={'A': '={dps}', 'H1': '={dps}', 'H2': '={dps}', 'F': '={dps}', 'FY': 'sum'}),
        dict(key='divpaid', label='Dividends paid', unit='US$M', spec=calc('=[dps]*[shares]')),
        dict(key='buyback', label='Share buybacks', unit='US$M', spec=calc('={buybacks}')),
        dict(section='Balance sheet'),
        dict(key='netdebt', label='Net debt (negative = net cash)', unit='US$M', bold=True, spec={'H1': '={netdebt_act}', 'H2': '=[netdebt<]-[fcf]+[divpaid]+[buyback]', 'F': '=[netdebt<]-[fcf]+[divpaid]+[buyback]', 'FY': 'last'}),
        dict(key='equity', label="Shareholders' equity, period end", unit='US$M', spec={'H1': '={equity_act}', 'H2': '=[equity<]+[ni]-[divpaid]-[buyback]', 'F': '=[equity<]+[ni]-[divpaid]-[buyback]', 'FY': 'last'}, note='H1 uses Mar 31, 2026 reported equity as a proxy'),
    ]


def target_methods(m, ws, r):
    S = m.S
    years = list(range(2027, 2051))
    lbl = {2027: '2027E', 2028: '2028E', 2029: '2029E', 2030: '2030E'}
    def oz(y, L, P, R):
        if y in lbl: return f"={m.M('oz', lbl[y])}"
        if y <= 2036: return f"={S('nav_flat_oz')}"
        return f"={P}{R['oz']}*(1-{S('nav_decline')})"
    rows = [
        ('oz', 'Gold production', 'koz', 'n1', oz),
        ('gold', 'Gold price', 'US$/oz', 'm0', lambda y, L, P, R: f"={m.I('gold', lbl[y])}" if y in lbl else f"={S('gold_lt')}"),
        ('aisc', 'AISC', 'US$/oz', 'm0', lambda y, L, P, R: f"={m.M('aisc', lbl[y])}" if y in lbl else f"={S('aisc_lt')}"),
        ('growth', 'Growth capital', 'US$M', 'm0', lambda y, L, P, R: f"={m.M('growth', lbl[y])}" if y in lbl else '=0'),
        ('expl', 'Exploration', 'US$M', 'm0', lambda y, L, P, R: f"={m.M('expl', lbl[y])}" if y in lbl else f"={S('expl_lt')}"),
        ('cf', 'After-tax free cash flow', 'US$M', 'm0', lambda y, L, P, R: f"=({L}{R['gold']}-{L}{R['aisc']})*{L}{R['oz']}/1000*(1-{S('mining_tax')})-{L}{R['growth']}-{L}{R['expl']}"),
        ('df', 'Discount factor (mid-year)', '', 'n3', lambda y, L, P, R: f"=1/(1+{S('nav_disc')})^({y}-2026-0.5)"),
        ('pv', 'Present value', 'US$M', 'm0', lambda y, L, P, R: f"={L}{R['cf']}*{L}{R['df']}"),
    ]
    nws, R, rr, a, b = nav_sheet(m, f"{m.cfg['company']['name']} — Net asset value (5% real, Dec 31, 2026)",
                                 'Production per Model to 2030E, flat to 2036, then a 7% annual decline to 2050.', years, rows)
    m.block(nws, rr, [
        ('#', 'NAV summary'),
        ('nav_ops', 'Operating mines and projects', f"=SUM({a}{R['pv']}:{b}{R['pv']})", 'm0', ''),
        ('nav_cash', 'Net cash, Dec 31, 2026E', f"=-{m.M('netdebt', '2026E')}", 'm0', ''),
        ('nav', 'Net asset value', None, 'm0', ''),
        ('navps', 'NAV per share (US$)', None, 'ps', ''),
    ])
    nws[m.ref('nav').split('!')[1].replace('$', '')] = f"={m.ref('nav_ops')}+{m.ref('nav_cash')}"
    nws[m.ref('navps').split('!')[1].replace('$', '')] = f"={m.ref('nav')}/{S('shares')}"
    m.out('navps', m.ref('navps'))
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
    return dict(m1=[0.8, 0.9, 1.0, 1.1, 1.2], m1_fmt='0.00"x"', m1_label='P/NAV',
                m2=[8, 9, 10, 11, 12], m2_fmt='0.0"x"', m2_label='P/CF 2027E',
                formula=lambda a, b: f"=({S('w1')}*{a}*{m.ref('navps_v')}+(1-{S('w1')})*{b}*{m.ref('cf27')})/{S('fx_price')}")


def ratio_lines():
    F = ['2025A', 'H1-26A', 'H2-26E', '2026E', '2027E', '2028E', '2029E', '2030E']
    G = ['2027E', '2028E', '2029E', '2030E']
    return [
        dict(label='AISC margin (% of gold price)', tmpl='=[margin_oz]/[gold]', periods=F),
        dict(label='Free cash flow conversion (FCF / OCF)', tmpl='=[fcf]/[ocf]', periods=F),
        dict(label='Reinvestment rate ((growth capital + exploration) / OCF)', tmpl='=([growth]+[expl])/[ocf]', periods=['H2-26E'] + G),
        dict(label='Return on average equity', tmpl='=[ni]/AVERAGE([equity<],[equity])', periods=G, note='Equity rolled forward from a Q1-26 proxy; directional only'),
        dict(label='Dividend payout (DPS / EPS)', tmpl='=[dps]/[eps]', periods=['2025A', '2026E'] + G),
        dict(label='Net debt / OCF', tmpl='=[netdebt]/[ocf]', fmt='n2', periods=['2026E'] + G),
    ]


def checks(m):
    p = m.cfg['published']
    return [
        ('NAV per share equals the published NAVPS', f"={m.ref('navps')}", p['navps'], 'num'),
        ('2026E adjusted EPS equals the published estimate', f"={m.M('eps', '2026E')}", p['eps_2026'], 'num'),
        ('2027E CFPS equals the published estimate', f"={m.M('cfps', '2027E')}", p['cfps_2027'], 'num'),
        ('2028E free cash flow equals the published estimate', f"={m.M('fcf', '2028E')}", p['fcf_2028'], 'num'),
    ]
