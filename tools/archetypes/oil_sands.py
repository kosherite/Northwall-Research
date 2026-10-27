"""Oil sands SAGD producer (e.g. Greenfire). EBITDA per barrel is anchored to the company's
own leverage guidance at US$70 WTI and flexed for WTI; no cash taxes before 2030 (tax pools)."""

def lines(cfg):
    F = '={%s}'
    return [
        dict(section='Production and pricing'),
        dict(key='prod', label='Bitumen production', unit='kbbl/d', fmt='n1', spec={'A': '={prod}', 'FY': '={prod}', 'F': '={prod}'}),
        dict(key='wti', label='WTI, house deck', unit='US$/bbl', fmt='n1', spec={'F': '={wti}'}),
        dict(key='ebitda_bbl', label='Adjusted EBITDA per barrel', unit='C$/bbl', fmt='n2', spec={'F': '={{ebitda_anchor}}+{{ebitda_sens}}*([wti]-{{anchor_wti}})'}, note='C$1.17/bbl per US$1 WTI after royalties, at 1.38 USD/CAD'),
        dict(section='Cash flow'),
        dict(key='ebitda', label='Adjusted EBITDA', unit='C$M', bold=True, spec={'F': '=[prod]*365*[ebitda_bbl]/1000'}),
        dict(key='interest', label='Interest', unit='C$M', spec={'F': '={interest}'}),
        dict(key='aff', label='Adjusted funds flow', unit='C$M', bold=True, spec={'A': '={aff_act}', 'F': '=[ebitda]-[interest]'}, note='No cash taxes expected before 2030'),
        dict(key='shares', label='Basic shares', unit='M', fmt='n1', spec={'FY': '={shares}', 'F': '={shares}'}),
        dict(key='cfps', label='Adjusted funds flow per share', unit='C$', fmt='ps', bold=True, spec={'F': '=[aff]/[shares]'}),
        dict(key='capex', label='Capital expenditures', unit='C$M', spec={'A': '={capex_act}', 'F': '={capex}'}),
        dict(key='fcf', label='Free cash flow', unit='C$M', bold=True, spec={'A': '={fcf_act}', 'F': '=[aff]-[capex]'}),
        dict(key='fcff', label='Free cash flow to the firm', unit='C$M', spec={'F': '=[fcf]+[interest]'}),
        dict(section='Balance sheet'),
        dict(key='netdebt', label='Net debt, period end', unit='C$M', bold=True, spec={'FY': '={netdebt_ye}', 'F': '=[netdebt<]-[fcf]'}),
        dict(key='lev', label='Opening net debt / EBITDA', unit='x', fmt='n2', spec={'F': '=[netdebt<]/[ebitda]'}),
    ]


def target_methods(m, ws, r):
    S = m.S
    r = m.block(ws, r, [
        ('#', 'Target method 1: P/NAV (2P reserves) — method 2: EV/EBITDA'),
        ('nav_gfr', 'Greenfire 2P after-tax PV10, YE2025 (C$M)', f"={S('pv10_gfr')}", 'm0', m.cfg['scalars']['pv10_gfr']['source']),
        ('nav_conn', 'Connacher 2P value (C$M)', f"={S('nav_connacher')}", 'm0', m.cfg['scalars']['nav_connacher']['source']),
        ('nd26', 'Net debt, Dec 31, 2026E (C$M)', f"={m.M('netdebt', '2026E')}", 'm0', ''),
        ('navps', 'NAV per share (C$)', None, 'ps', ''),
        ('mult1', 'Target P/NAV multiple', f"={S('mult1')}", 'x', m.cfg['scalars']['mult1']['source']),
        ('v1', 'Method 1 value per share (C$)', None, 'ps', ''),
        ('ebitda27', 'Adjusted EBITDA, 2027E (C$M)', f"={m.M('ebitda', '2027E')}", 'm0', ''),
        ('mult2', 'Target EV/EBITDA multiple, 2027E', f"={S('mult2')}", 'x', m.cfg['scalars']['mult2']['source']),
        ('v2', 'Method 2 value per share (C$)', None, 'ps', ''),
        ('ev_bbl', 'Current EV per flowing barrel (C$)', None, 'm0', 'EV / current production'),
    ])
    c = lambda k: ws[m.ref(k).split('!')[1].replace('$', '')]
    c('navps').value = f"=({m.ref('nav_gfr')}+{m.ref('nav_conn')}-{m.ref('nd26')})/{m.ref('shares')}"
    c('v1').value = f"={m.ref('mult1')}*{m.ref('navps')}"
    c('v2').value = f"=({m.ref('mult2')}*{m.ref('ebitda27')}-{m.ref('nd26')})/{m.ref('shares')}"
    c("ev_bbl").value = f"={m.ref('ev')}*1000000/{S('current_prod')}"
    m.out('navps', m.ref('navps'))
    return r


def sens_axes(m):
    S = m.S
    return dict(m1=[0.7, 0.775, 0.85, 0.925, 1.0], m1_fmt='0.00"x"', m1_label='P/NAV',
                m2=[4.0, 4.5, 5.0, 5.5, 6.0], m2_fmt='0.0"x"', m2_label='EV/EBITDA 2027E',
                formula=lambda a, b: f"=({S('w1')}*{a}*{m.ref('navps')}+(1-{S('w1')})*({b}*{m.ref('ebitda27')}-{m.ref('nd26')})/{m.ref('shares')})/{S('fx_price')}")


def ratio_lines():
    G = ['2027E', '2028E', '2029E', '2030E']
    return [
        dict(label='Opening net debt / EBITDA', tmpl='=[netdebt<]/[ebitda]', fmt='n2', periods=G),
        dict(label='Reinvestment rate (capital / adjusted funds flow)', tmpl='=[capex]/[aff]', periods=['2025A'] + G),
        dict(label='Free cash flow conversion (FCF / AFF)', tmpl='=[fcf]/[aff]', periods=['2025A'] + G),
        dict(label='EBITDA margin per barrel at deck (C$/bbl)', tmpl='=[ebitda_bbl]', fmt='n2', periods=G),
    ]


def checks(m):
    p = m.cfg['published']
    return [
        ('2027E adjusted EBITDA equals the published estimate', f"={m.M('ebitda', '2027E')}", p['ebitda_2027'], 'num'),
        ('2027E AFF per share equals the published estimate', f"={m.M('cfps', '2027E')}", p['cfps_2027'], 'num'),
        ('Blended value (C$) equals the published C$ target', f"={m.ref('blend')}", p['target_cad'], 'num'),
        ('NAV per share equals the published NAVPS', f"={m.ref('navps')}", p['navps'], 'num'),
    ]
