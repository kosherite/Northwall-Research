"""Conventional and unconventional oil and gas producer (e.g. Whitecap).
Funds flow per boe is anchored to the latest reported quarter and flexed for WTI with a
company-specific sensitivity; free funds flow = funds flow - capital."""

def lines(cfg):
    calc = lambda f: {'H2': f, 'F': f}
    return [
        dict(section='Production and pricing'),
        dict(key='prod', label='Production', unit='kboe/d', fmt='n1', spec={'H1': '={prod}', 'H2': '={prod}', 'F': '={prod}', 'FY': 'wavg:days'}),
        dict(key='days', label='Days in period', unit='days', fmt='int', spec={'H1': '={days}', 'H2': '={days}', 'F': '={days}', 'FY': 'sum'}),
        dict(key='vol', label='Volume', unit='MMboe', fmt='n1', spec={'H1': '=[prod]*[days]/1000', 'H2': '=[prod]*[days]/1000', 'F': '=[prod]*[days]/1000', 'FY': 'sum'}),
        dict(key='wti', label='WTI, house deck', unit='US$/bbl', fmt='n1', spec=calc('={wti}')),
        dict(key='ffpb', label='Funds flow per boe', unit='C$/boe', fmt='n2', spec={'H1': '=[ff]/[vol]', 'H2': '={{ff_anchor}}+{{ff_sens}}*([wti]-{{anchor_wti}})', 'F': '={{ff_anchor}}+{{ff_sens}}*([wti]-{{anchor_wti}})', 'FY': '=[ff]/[vol]'}, note='Anchored to Q2-26 actual, flexed C$0.60/boe per US$1 WTI'),
        dict(section='Cash flow'),
        dict(key='ff', label='Funds flow', unit='C$M', bold=True, spec={'H1': '={ff_act}', 'H2': '=[vol]*[ffpb]', 'F': '=[vol]*[ffpb]', 'FY': 'sum'}),
        dict(key='shares', label='Basic shares', unit='M', fmt='n1', spec={'all': '={shares}'}),
        dict(key='cfps', label='Funds flow per share', unit='C$', fmt='ps', bold=True, spec={'H1': '=[ff]/[shares]', 'H2': '=[ff]/[shares]', 'F': '=[ff]/[shares]', 'FY': '=[ff]/[shares]'}),
        dict(key='capex', label='Capital expenditures', unit='C$M', spec={'H1': '={capex_act}', 'H2': '={capex}', 'F': '={capex}', 'FY': 'sum'}),
        dict(key='fff', label='Free funds flow', unit='C$M', bold=True, spec={'H1': '=[ff]-[capex]', 'H2': '=[ff]-[capex]', 'F': '=[ff]-[capex]', 'FY': 'sum'}),
        dict(key='fffps', label='Free funds flow per share', unit='C$', fmt='ps', spec={'H1': '=[fff]/[shares]', 'H2': '=[fff]/[shares]', 'F': '=[fff]/[shares]', 'FY': '=[fff]/[shares]'}),
        dict(key='dacf', label='Debt-adjusted cash flow (FF + after-tax interest)', unit='C$M', spec={'FY': '=[ff]+{{at_interest}}', 'F': '=[ff]+{{at_interest}}'}),
        dict(key='fcff', label='Free cash flow to the firm', unit='C$M', spec={'F': '=[fff]+{{at_interest}}'}),
        dict(key='dps', label='Dividend per share', unit='C$', fmt='ps', spec={'H1': '={dps}', 'H2': '={dps}', 'F': '={dps}', 'FY': 'sum'}),
        dict(key='divpaid', label='Dividends', unit='C$M', spec={'H2': '=[dps]*[shares]', 'F': '=[dps]*[shares]'}),
        dict(section='Balance sheet'),
        dict(key='netdebt', label='Net debt, period end (negative = net cash)', unit='C$M', bold=True, spec={'H1': '={netdebt_act}', 'H2': '=[netdebt<]-[fff]+[divpaid]', 'F': '=[netdebt<]-[fff]+[divpaid]', 'FY': 'last'}, note='No buybacks assumed'),
    ]


def target_methods(m, ws, r):
    S = m.S
    r = m.block(ws, r, [
        ('#', 'Target method 1: EV/DACF — method 2: free cash flow yield'),
        ('dacf27', 'DACF, 2027E (C$M)', f"={m.M('dacf', '2027E')}", 'm0', ''),
        ('mult1', 'Target EV/DACF multiple', f"={S('mult1')}", 'x', m.cfg['scalars']['mult1']['source']),
        ('nd26', 'Net debt, Dec 31, 2026E (C$M)', f"={m.M('netdebt', '2026E')}", 'm0', ''),
        ('v1', 'Method 1 value per share', None, 'ps', '(multiple x DACF - net debt) / shares'),
        ('fff27', 'Free funds flow, 2027E (C$M)', f"={m.M('fff', '2027E')}", 'm0', ''),
        ('mult2', 'Target free funds flow yield', f"={S('mult2')}", 'pct', m.cfg['scalars']['mult2']['source']),
        ('v2', 'Method 2 value per share', None, 'ps', 'FFF / yield / shares'),
        ('evdacf_now', 'Current EV / 2027E DACF', None, 'x', ''),
        ('fcfy_now', 'Current 2027E free funds flow yield', None, 'pct', ''),
    ])
    c = lambda k: ws[m.ref(k).split('!')[1].replace('$', '')]
    c('v1').value = f"=({m.ref('mult1')}*{m.ref('dacf27')}-{m.ref('nd26')})/{m.ref('shares')}"
    c('v2').value = f"={m.ref('fff27')}/{m.ref('mult2')}/{m.ref('shares')}"
    c('evdacf_now').value = f"={m.ref('ev')}/{m.ref('dacf27')}"
    c('fcfy_now').value = f"={m.ref('fff27')}/{m.ref('mcap')}"
    # dividend breakeven WTI (free funds flow per share = dividend), 2027E volumes and capital
    r = m.block(ws, r, [
        ('#', 'Dividend coverage'),
        ('be_wti', 'WTI at which 2027E free funds flow covers the dividend (US$/bbl)', None, 'n1', 'Solves FF(WTI) - capital = dividends'),
    ])
    c('be_wti').value = (f"={S('anchor_wti')}+(({m.M('dps', '2027E')}*{m.M('shares', '2027E')}+{m.M('capex', '2027E')})/{m.M('vol', '2027E')}-{S('ff_anchor')})/{S('ff_sens')}")
    m.out('be_wti', m.ref('be_wti'))
    return r


def sens_axes(m):
    S = m.S
    return dict(m1=[5.5, 6.0, 6.5, 7.0, 7.5], m1_fmt='0.0"x"', m1_label='EV/DACF',
                m2=[0.07, 0.075, 0.08, 0.09, 0.10], m2_fmt='0.0%', m2_label='FFF yield',
                formula=lambda a, b: f"=({S('w1')}*({a}*{m.ref('dacf27')}-{m.ref('nd26')})/{m.ref('shares')}+(1-{S('w1')})*{m.ref('fff27')}/{b}/{m.ref('shares')})/{S('fx_price')}")


def ratio_lines():
    G = ['2026E', '2027E', '2028E', '2029E', '2030E']
    return [
        dict(label='Reinvestment rate (capital / funds flow)', tmpl='=[capex]/[ff]', periods=['H1-26A', 'H2-26E'] + G),
        dict(label='Dividend payout of free funds flow', tmpl='=[dps]*[shares]/[fff]', periods=G),
        dict(label='Net debt / funds flow', tmpl='=[netdebt]/[ff]', fmt='n2', periods=G),
        dict(label='Funds flow per share growth', tmpl='=[cfps]/[cfps<]-1', periods=['2027E', '2028E', '2029E', '2030E'], note='Mostly price-driven: the deck falls from US$91.5 to US$70'),
    ]


def checks(m):
    p = m.cfg['published']
    return [
        ('2027E funds flow per share equals the published estimate', f"={m.M('cfps', '2027E')}", p['cfps_2027'], 'num'),
        ('2027E free funds flow equals the published estimate', f"={m.M('fff', '2027E')}", p['fff_2027'], 'num'),
        ('Net debt at Dec 31, 2026E equals the published estimate', f"={m.M('netdebt', '2026E')}", p['nd_2026'], 'num'),
        ('Dividend breakeven WTI equals the published ~US$63', f"={m.ref('be_wti')}", p['be_wti'], 'num'),
    ]
