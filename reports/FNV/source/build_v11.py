"""Franco-Nevada company report v1.1: same content as v1.0, rebuilt in the one-pager house layout."""
import json
from weasyprint import HTML
m = json.load(open('model.json')); Y = m['y']
o = json.load(open('/home/claude/northwall-research/coverage/FNV/outputs.json'))
PX = m['px']; PT = 250.0; DPS = 1.76
ret = PT / PX - 1; yld = DPS / PX; allin = (ret + yld) * 100
navps = m['navps']; cobre_ps = m['cobre_ps']
def f(v, d=2): return f"{v:,.{d}f}"
def mm(v): return f"{v:,.0f}"
yrs = ['2025', '2026', '2027', '2028', '2029', '2030']
lab = ['2025A', '2026E', '2027E', '2028E', '2029E', '2030E']
port_ps = m['port'] / 193; expl_ps = m['explor'] / 193; cash_ps = m['cash'] / 193; inv_ps = m['invest'] / 193
nav_comp = 2.0 * navps; cf_comp = 25 * Y['2027']['cfps']; ev = m['ev']

mark = '''<svg width="30" height="30" viewBox="0 0 36 36"><rect x="3" y="11" width="8" height="23" fill="#2F5D7C"/><rect x="14" y="2" width="8" height="32" fill="#0F1A2B"/><rect x="25" y="11" width="8" height="23" fill="#2F5D7C"/></svg>'''
smark = mark.replace('width="30" height="30"', 'width="14" height="14"')

est_rows = [('Gold price (US$/oz)', ['–', '4,200 (H2)', '4,000', '3,800']), ('GEOs sold (000 oz)', [f(Y[k]['geo'], 1) for k in yrs[:4]]),
            ('Revenue (US$M)', [mm(Y[k]['rev']) for k in yrs[:4]]), ('Adj. EBITDA (US$M)', [mm(Y[k]['ebitda']) for k in yrs[:4]]),
            ('Adj. EPS (US$)', [f(Y[k]['eps']) for k in yrs[:4]]), ('CFPS (US$)', [f(Y[k]['cfps']) for k in yrs[:4]]),
            ('P/E (x)', [f(PX / Y[k]['eps'], 1) + 'x' for k in yrs[:4]]), ('P/CF (x)', [f(PX / Y[k]['cfps'], 1) + 'x' for k in yrs[:4]]),
            ('DPS (US$)', [f(Y[k]['dps']) for k in yrs[:4]])]
est = ''.join(f'<tr><td>{r}</td>' + ''.join(f'<td>{v}</td>' for v in vals) + '</tr>' for r, vals in est_rows)
fin_rows = [('Gold price assumption (US$/oz)', ['–', '4,200 (H2)', '4,000', '3,800', '3,600', '3,500'], ''),
            ('GEOs sold (000 oz)', [f(Y[k]['geo'], 1) for k in yrs], ''), ('Revenue', [mm(Y[k]['rev']) for k in yrs], 'b'),
            ('Cost of sales', [f"({mm(Y[k]['cos'])})" for k in yrs], ''), ('Adj. EBITDA', [mm(Y[k]['ebitda']) for k in yrs], 'b'),
            ('Adj. EBITDA margin', [f"{Y[k]['margin'] * 100:.0f}%" for k in yrs], ''), ('Depletion and depreciation', [f"({mm(Y[k]['da'])})" for k in yrs], ''),
            ('Adj. net income', [mm(Y[k]['ani']) for k in yrs], 'b'), ('Basic shares (M)', [f(Y[k]['shares'], 1) for k in yrs], ''),
            ('Adj. EPS (US$)', [f(Y[k]['eps']) for k in yrs], 'b'), ('Operating cash flow', [mm(Y[k]['ocf']) for k in yrs], ''),
            ('CFPS (US$)', [f(Y[k]['cfps']) for k in yrs], 'b'), ('Dividend per share (US$)', [f(Y[k]['dps']) for k in yrs], ''),
            ('Cash, year-end (no debt)', [mm(Y[k]['cash']) for k in yrs], 'b')]
fin = ''.join(f"<tr class='{c}'><td>{r}</td>" + ''.join(f"<td>{v}</td>" for v in vals) + "</tr>" for r, vals, c in fin_rows)
sens = ''.join(f"<tr {'class=me' if g['lt'] == 3500 else ''}><td>US${g['lt']:,}</td><td>{f(g['navps'])}</td><td>{f(PX / g['navps'], 2)}x</td><td>{f(g['cfps'])}</td><td>{f(g['pt'], 0)}</td><td>{(g['pt'] / PX - 1) * 100:+.0f}%</td></tr>" for g in m['grid'])

html = f'''<!doctype html><html><head><meta charset="utf-8"><title>Franco-Nevada Corporation (FNV) - Northwall Research</title><style>
@font-face {{ font-family:'Pal'; src:url('file:///usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf'); }}
@font-face {{ font-family:'Pal'; font-weight:bold; src:url('file:///usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf'); }}
@page {{ size: Letter; margin: 0.72in 0.5in 0.5in 0.5in;
  @top-left {{ content: element(rh); }}
  @bottom-left {{ content: "October 27, 2026"; font: 7.6pt 'Liberation Sans'; color:#0F1A2B; }}
  @bottom-right {{ content: counter(page); font: 7.6pt 'Liberation Sans'; color:#0F1A2B; }} }}
@page :first {{ margin-top: 0.4in; @top-left {{ content: none; }} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:'Liberation Sans',Arial,sans-serif; font-size:8.5pt; line-height:1.44; color:#0F1A2B; }}
.rh {{ position: running(rh); display:table; width:7.5in; border-bottom:1px solid #C9CFD6; padding-bottom:4px; font-size:7.4pt; }}
.rh > div {{ display:table-cell; vertical-align:middle; }} .rh .lk {{ font-weight:bold; letter-spacing:2.2px; font-size:7pt; }} .rh .lk svg {{ vertical-align:-3px; margin-right:5px; }}
.rh .r {{ text-align:right; color:#5A6B7C; }}
.logo {{ display:table; }} .logo > div {{ display:table-cell; vertical-align:middle; }}
.w1 {{ font-family:'Pal'; font-weight:bold; font-size:13pt; letter-spacing:4px; line-height:1; padding-left:8px; }}
.w2 {{ font-size:6.4pt; letter-spacing:5.3px; color:#5A6B7C; padding-left:8px; margin-top:2px; }}
.top {{ display:table; width:7.5in; }} .top > div {{ display:table-cell; vertical-align:top; }} .tr {{ text-align:right; font-size:8pt; font-weight:bold; }}
.id {{ display:table; width:7.5in; margin-top:12px; table-layout:fixed; }} .id > div {{ display:table-cell; vertical-align:bottom; }} .idl {{ width:3.75in; padding-right:0.25in; }}
.co {{ font-weight:bold; font-size:12.5pt; line-height:1.2; }}
.who {{ font-size:8pt; font-weight:bold; margin-top:3px; line-height:1.45; }} .who span {{ font-weight:normal; color:#5A6B7C; }}
.box {{ width:3.75in; background:#E9EEF2; padding:7px 12px; }} .box table {{ width:100%; border-collapse:collapse; }} .box td {{ width:50%; padding:3px 0; vertical-align:top; }}
.box .bl {{ font-size:6.6pt; letter-spacing:1px; text-transform:uppercase; color:#5A6B7C; }} .box .bv {{ font-family:'Pal'; font-weight:bold; font-size:11.5pt; color:#2F5D7C; line-height:1.15; }}
.cols {{ display:table; width:7.5in; table-layout:fixed; }} .c1 {{ display:table-cell; width:3.75in; vertical-align:top; padding-right:0.25in; }} .c2 {{ display:table-cell; width:3.75in; vertical-align:top; }}
.main {{ display:table-cell; width:4.9in; vertical-align:top; padding-right:0.25in; }} .side {{ display:table-cell; width:2.6in; vertical-align:top; border-left:1px solid #C9CFD6; padding-left:0.15in; }}
.mt {{ margin-top:10px; }} .rule {{ border-top:1px solid #C9CFD6; padding-top:9px; margin-top:4px; }}
h1 {{ font-family:'Pal'; font-weight:bold; font-size:15pt; margin:0 0 3px; line-height:1.2; }}
.lede {{ font-size:9pt; color:#5A6B7C; margin:0 0 10px; text-align:left; }}
h2 {{ font-size:9.6pt; font-weight:bold; color:#2F5D7C; margin:0 0 2px; }}
h3 {{ font-size:8.8pt; font-weight:bold; margin:9px 0 2px; }} h3:first-child {{ margin-top:0; }}
p {{ margin:0 0 7px; text-align:justify; }}
.ex {{ margin-bottom:10px; page-break-inside:avoid; }}
.ext {{ font-size:8.4pt; color:#2F5D7C; margin-bottom:3px; }}
.ex img {{ display:block; width:100%; }}
.src {{ font-size:6.5pt; color:#5A6B7C; margin-top:2px; line-height:1.3; text-align:left; }}
table.t {{ width:100%; border-collapse:collapse; font-size:7.6pt; }}
table.t th {{ text-align:right; font-size:6.8pt; border-bottom:1px solid #0F1A2B; padding:1px 4px 2px; font-weight:bold; vertical-align:bottom; }}
table.t td {{ text-align:right; padding:2.3px 4px; border-bottom:1px solid #E6E9EC; vertical-align:top; }}
table.t th:first-child, table.t td:first-child {{ text-align:left; padding-left:0; }} table.t th:last-child, table.t td:last-child {{ padding-right:0; }}
table.t tr.b td, table.t tr.me td {{ font-weight:bold; }} table.t tr.pt td {{ font-weight:bold; color:#2F5D7C; border-top:1px solid #0F1A2B; }}
table.txt td, table.txt th {{ text-align:left !important; }}
.call {{ background:#E9EEF2; padding:8px 10px; font-size:8pt; margin-top:4px; }}
.pb {{ page-break-before:always; }}
.disc {{ font-size:6.3pt; color:#5A6B7C; line-height:1.38; columns:2; column-gap:0.25in; text-align:justify; }}
.disc b {{ color:#0F1A2B; }} .disc p {{ margin:0 0 4px; }}
</style></head><body>
<div class="rh"><div class="lk">{smark}NORTHWALL RESEARCH</div><div class="r">Franco-Nevada Corporation (NYSE/TSX: FNV) &nbsp;|&nbsp; Hold &nbsp;|&nbsp; Target US$250.00</div></div>

<!-- PAGE 1 -->
<div class="top"><div><div class="logo"><div>{mark}</div><div><div class="w1">NORTHWALL</div><div class="w2">RESEARCH</div></div></div></div>
<div class="tr">Gold Royalties &amp; Streaming</div></div>
<div class="id"><div class="idl"><div class="co">Franco-Nevada Corporation<br>(NYSE/TSX: FNV)</div>
<div class="who">Basel Al-Ghousein (Analyst), Northwall Research<br><span>October 27, 2026</span></div></div>
<div><div class="box"><table>
<tr><td><div class="bl">Rating</div><div class="bv">Hold</div></td><td><div class="bl">Closing price</div><div class="bv">USD {f(PX)}</div></td></tr>
<tr><td><div class="bl">Price target</div><div class="bv">USD {f(PT)}</div></td><td><div class="bl">Implied all-in return</div><div class="bv">{allin:.1f}%</div></td></tr></table></div></div></div>

<div class="cols mt"><div class="c1">
<h1>Best in class, and priced like it</h1>
<h2>Investment summary</h2>
<p>Franco-Nevada is the largest and most diversified gold-focused royalty and streaming company, with no debt and an adjusted EBITDA margin above 90%. We rate the shares Hold with a US$250.00 target. We like the business without reservation; our hesitation is the price. The shares trade at {f(PX / navps)}x our NAV and {f(PX / Y['2027']['cfps'], 1)}x our 2027E cash flow, and our deck has gold easing from about US$4,000/oz toward US$3,500/oz by 2030. That leaves a {allin:.1f}% all-in return, below our 15% hurdle for a Buy.</p>
<h2>Investment thesis</h2>
<p>We base our view on four points: (1) <b>quality is real and measurable</b>, with H1 2026 revenue of US$1.23 billion (+67% y/y) converting to US$1.12 billion of adjusted EBITDA, a 91% margin, and no asset above 10% of revenue; (2) <b>growth is visible but measured</b>, with 552k GEOs in 2026E rising to 600k by 2030E, about 3% a year and inside management's 555–615k outlook; (3) <b>Cobre Panamá is the swing factor</b>, which we carry at a 35% probability of restart (US${f(cobre_ps)}/sh) against ~US${f(m['cobre_full_ps'], 0)}/sh unrisked; and (4) <b>the balance sheet is a call option on deals</b>, with US$4.3 billion of available capital that we do not pay for in advance.</p>
<h2>Valuation</h2>
<p>Our US$250.00 target is a 50/50 blend of 2.0x our NAVPS of US${f(navps)} and 25x our 2027E CFPS of US${f(Y['2027']['cfps'])}. With a {o['ke']*100:.1f}% CAPM cost of equity, today's price implies about {o['g_impl']*100:.1f}% perpetual growth in cash flow, above the ~3% volume growth we forecast. Absolute models sit well below the price (Exhibit 12).</p>
<h2>Upcoming catalysts</h2>
<p>Near-term milestones include: (1) Q3 2026 results with the first Cobre Panamá stockpile deliveries (Nov 11, 2026); (2) the Côté Gold/IAMGOLD reserve update and 40ktpd plan (4Q26); (3) the Copper World/Hudbay sanction decision (late 2026); (4) Castle Mountain and AurMac investment decisions (1H27); (5) 2027 guidance and a likely 20th straight dividend increase (Mar 2027); and (6) a ruling from Panama's ministerial commission on Cobre Panamá (timing open).</p>
<h2>Risks to rating and price target</h2>
<p>We highlight: (1) gold, where each US$250/oz move changes 2027E CFPS by about {m['cf_sens250'] * 100:.0f}%; (2) permanent closure of Cobre Panamá, which removes US${f(cobre_ps)}/sh; (3) ramp-up at Candelaria, Côté Gold and Valentine; (4) acquisitions at cycle-high prices; and (5) tax, including CRA reassessments and a global minimum tax.</p>
</div>
<div class="c2">
<div class="ex"><div class="ext">Exhibit 1 - Northwall estimates</div>
<table class="t"><tr><th>FY Dec</th><th>2025A</th><th>2026E</th><th>2027E</th><th>2028E</th></tr>{est}</table>
<div class="src">All values in US$. Priced at the October 26, 2026 close. 2026E combines reported H1 2026 with our H2 forecast. Source: company filings, Northwall estimates.</div></div>
<div class="ex"><div class="ext">Exhibit 2 - Key statistics</div>
<table class="t"><tr><td>Shares outstanding (M)</td><td>192.9</td><td>Market cap (US$M)</td><td>{mm(m['mcap'])}</td></tr>
<tr><td>Dividend (US$)</td><td>1.76</td><td>Dividend yield</td><td>{yld * 100:.1f}%</td></tr>
<tr><td>Northwall NAVPS (US$)</td><td>{f(navps)}</td><td>P/NAV</td><td>{f(PX / navps)}x</td></tr>
<tr><td>Cash (US$M)</td><td>1,014</td><td>Debt</td><td>Nil</td></tr>
<tr><td>EV (US$M)</td><td>{mm(ev)}</td><td>EV/EBITDA 2027E</td><td>{f(ev / Y['2027']['ebitda'], 1)}x</td></tr>
<tr><td>Available capital (US$B)</td><td>4.3</td><td>52-week range (US$)</td><td>181.50–285.67</td></tr></table></div>
<div class="ex"><div class="ext">Exhibit 3 - Valuation ranges (US$/share)</div><img src="v11/range.png">
<div class="src">Bear: US$3,000 gold, no Cobre restart, 1.5x NAV, 20x CF. Bull: US$4,500 gold, full restart, 2.25x NAV, 28x CF. Source: Northwall estimates.</div></div>
<div class="src" style="border-top:1px solid #E6E9EC;padding-top:4px;margin-top:2px">Ratings: Buy, expected 12-month total return above 15%; Hold, 0–15%; Sell, below 0%. Facts are from company filings; estimates, target and rating are Northwall Research opinions. See important disclosures on page 5.</div>
</div></div>

<!-- PAGE 2: THESIS -->
<div class="pb"><h1>A premium franchise at a premium price</h1>
<p class="lede">Franco-Nevada does almost everything right. At US${f(PX)}, the question is not whether this is a good company, but how much of that is already in the share price.</p>
<div class="cols"><div class="main">
<h3>The quality is real and visible in the numbers</h3>
<p>Royalty and stream holders take a share of a mine's output without paying for its operating costs or capital overruns. Franco-Nevada runs that model at scale: Q2 2026 cost of sales was US$45.9 million against US$580.9 million of revenue, and adjusted EBITDA margin was 91%. The company carries no debt, held US$1.01 billion of cash at June 30, 2026, and reports US$4.3 billion of available capital including undrawn credit facilities and equity investments.</p>
<p>Diversification is the second pillar. In Q2 2026, 86% of revenue came from precious metals (70% gold, 14% silver, 2% PGM), 88% came from the Americas, and no single asset generated more than 10% of revenue (Exhibit 5). This is what lets FNV absorb events that would be existential for a single-asset producer. The loss of Cobre Panamá, once its largest asset, in late 2023 is the clearest example.</p>
<h3>Growth is visible, but measured</h3>
<p>Our 2026E of 552k GEOs sits in the upper half of the 510–570k guidance range, consistent with management's commentary. H1 2026 delivered 269k GEOs. We expect a heavier second half as Candelaria moves into higher-grade Phase 12 ore, Côté Gold runs near capacity after its crusher and conveyor fixes, and Tocantinzinho, Greenstone and Valentine step up.</p>
<p>Beyond 2026 the pipeline is credible: Stibnite (2029), Copper World (2H29), Bullabulling (4Q28), the Detour underground, Odyssey at Canadian Malartic and the Valentine Phase 2 expansion. Management's own 2030 outlook of 555–615k GEOs, excluding Cobre Panamá, implies about 13% total growth from 2025. We model 600k GEOs in 2030E, or about 3% a year (Exhibit 4). That is respectable at this size, but it does not on its own justify a premium multiple expanding further.</p>
<h3>Cobre Panamá: real progress, unresolved outcome</h3>
<p>Panama authorized stockpile processing in April 2026, first concentrate followed in May, and the SGS integral audit reported 87.7% overall compliance. First Quantum expects about 70,000 tonnes of copper from the stockpiles across 2026 and 2027, which FNV expects to translate into roughly 23,100 oz of gold and 265,000 oz of silver, about one third in H2 2026. We include all of it in our forecasts.</p>
<p>A full restart is a different matter. Management has indicated the stream could deliver 150–175k GEOs a year at full capacity, roughly a quarter of today's portfolio. A ministerial commission is reviewing the mine's future, with no timeline. We value a restart from 2029 at 150k GEOs a year and apply a 35% probability, worth US${f(cobre_ps)} per share. Unrisked, the stream would add ~US${f(m['cobre_full_ps'], 0)} per share to our NAV. This is the largest single source of upside to our target.</p>
<h3>The balance sheet is a call option on deals</h3>
<p>Franco-Nevada has US$4.3 billion of available capital and no debt, the most firepower in the senior group (Exhibit 9). We model US$500 million a year of acquisitions from 2027 but take no production credit for them, so any accretive deal is upside to our estimates. The risk runs the other way too: deploying capital at cycle-high gold prices can lock in low returns, which is why we do not pay for deals in advance.</p>
<h3>The valuation already credits the quality</h3>
<p>At US${f(PX)}, FNV trades at {f(PX / navps)}x our NAVPS and {f(PX / Y['2027']['cfps'], 1)}x our 2027E CFPS. The stock is down about 12% over the past month as gold pulled back toward US$4,000/oz, but remains about 12% higher year to date. Our gold deck steps down from US$4,000/oz in 2027 to US$3,500/oz long term, below spot. If gold holds at today's level our framework supports about US$266; at US$3,000/oz our value falls to about US$206 (Exhibit 11).</p>
</div>
<div class="side">
<div class="ex"><div class="ext">Exhibit 4 - GEOs sold (000 oz)</div><img src="v11/geo.png">
<div class="src">2024A–2025A navy; Northwall estimates steel blue. 2026E–2027E include Cobre Panamá stockpile deliveries; no restart assumed. Management's 2030 outlook is 555–615k GEOs. Source: company filings, Northwall estimates.</div></div>
<div class="ex"><div class="ext">Exhibit 5 - Q2 2026 revenue by commodity</div><img src="v11/mix.png">
<div class="src">Total US$580.9M. Source: FNV Q2 2026 release.</div></div>
<div class="ex"><div class="ext">Exhibit 6 - What we are paying for</div>
<table class="t"><tr><td>P/NAV (Northwall)</td><td>{f(PX / navps)}x</td></tr><tr><td>P/CF 2027E</td><td>{f(PX / Y['2027']['cfps'], 1)}x</td></tr><tr><td>P/E 2027E</td><td>{f(PX / Y['2027']['eps'], 1)}x</td></tr>
<tr><td>Adj. EBITDA margin 2026E</td><td>{Y['2026']['margin'] * 100:.0f}%</td></tr><tr><td>GEO growth 2025A–2030E</td><td>{((Y['2030']['geo'] / Y['2025']['geo']) ** 0.2 - 1) * 100:.1f}% a year</td></tr><tr><td>Dividend yield</td><td>{yld * 100:.1f}%</td></tr></table>
<div class="src">At the October 26, 2026 close. Source: Northwall estimates.</div></div>
<div class="call"><b>Where we would change our mind.</b> A pullback below ~US$215 would lift the expected total return above our 15% Buy hurdle. A confirmed Cobre Panamá restart path, or a large acquisition at an attractive return, would raise our target directly.</div>
</div></div></div>

<!-- PAGE 3: VALUATION -->
<div class="pb"><h1>Price target derivation</h1>
<p class="lede">We value FNV on a 50/50 blend of P/NAV and P/CF. NAV captures the long life of the portfolio; cash flow anchors the target to what the business earns today.</p>
<div class="cols"><div class="c1">
<div class="ex"><div class="ext">Exhibit 7 - Net asset value (valuation date Dec 31, 2026)</div>
<table class="t"><tr><th>Component</th><th>US$M</th><th>US$/sh</th></tr>
<tr><td>Royalty and stream portfolio (5% real)</td><td>{mm(m['port'])}</td><td>{f(port_ps)}</td></tr>
<tr><td>Cobre Panamá restart (35% risked)</td><td>{mm(m['cobre_rw'])}</td><td>{f(cobre_ps)}</td></tr>
<tr><td>Exploration and undeveloped optionality</td><td>{mm(m['explor'])}</td><td>{f(expl_ps)}</td></tr>
<tr><td>Cash (2026E year-end)</td><td>{mm(m['cash'])}</td><td>{f(cash_ps)}</td></tr>
<tr><td>Equity investments (incl. LIORC)</td><td>{mm(m['invest'])}</td><td>{f(inv_ps)}</td></tr>
<tr class="pt"><td>Net asset value</td><td>{mm(m['nav'])}</td><td>{f(navps)}</td></tr></table>
<div class="src">Portfolio cash flows follow our GEO forecast to 2030E, flat at 600k GEOs to 2035, then a 4% annual decline to 2060. After-tax cash flow is 81% of EBITDA. Mid-year discounting.</div></div>
</div><div class="c2">
<div class="ex"><div class="ext">Exhibit 8 - Price target build</div>
<table class="t"><tr><th>Method</th><th>Metric</th><th>Multiple</th><th>Value</th><th>Weight</th></tr>
<tr><td>P/NAV</td><td>{f(navps)}</td><td>2.0x</td><td>{f(nav_comp)}</td><td>50%</td></tr>
<tr><td>P/CF 2027E</td><td>{f(Y['2027']['cfps'])}</td><td>25.0x</td><td>{f(cf_comp)}</td><td>50%</td></tr>
<tr class="b"><td>Blended value</td><td></td><td></td><td>{f(0.5 * nav_comp + 0.5 * cf_comp)}</td><td></td></tr>
<tr class="pt"><td>Price target (rounded)</td><td></td><td></td><td>250.00</td><td></td></tr></table></div>
<p>We apply 2.0x NAV, a premium that reflects FNV's diversification, debt-free balance sheet and execution record. Our 25x 2027E cash flow multiple is close to where the shares trade on trailing cash flow today (~25x) and above the ~15–20x at which the two closest peers trade on annualized H1 2026 cash flow (Exhibit 9).</p>
</div></div>
<div class="ex rule"><div class="ext">Exhibit 9 - Senior royalty and streaming peers</div>
<table class="t"><tr><th>Company</th><th>Ticker</th><th>Price (US$)</th><th>Market cap (US$B)</th><th>P/E (H1-26 ann.)</th><th>P/CF (H1-26 ann.)</th><th>Net cash (debt)</th></tr>
<tr class="b"><td>Franco-Nevada</td><td>FNV</td><td>230.76</td><td>44.5</td><td>27.5x</td><td>22.2x</td><td>US$1.0B</td></tr>
<tr><td>Wheaton Precious Metals</td><td>WPM</td><td>124.59</td><td>56.6</td><td>25.1x</td><td>20.0x</td><td>(US$1.9B)</td></tr>
<tr><td>Royal Gold</td><td>RGLD</td><td>234.11</td><td>19.8</td><td>22.9x</td><td>14.8x</td><td>(US$0.3B)</td></tr></table>
<div class="src">P/E and P/CF use H1 2026 adjusted EPS and operating cash flow per share, annualized (Royal Gold: Q2 2026 annualized). FNV and RGLD at the October 26, 2026 close; WPM October 27 intraday. Net debt at June 30, 2026 (RGLD after its July repayment). Source: company Q2 2026 filings, Northwall calculations.</div></div>
<div class="cols rule"><div class="c1">
<div class="ex"><div class="ext">Exhibit 10 - Sensitivity to gold (flat deck from 2027)</div>
<table class="t"><tr><th>Long-term gold</th><th>NAVPS</th><th>P/NAV</th><th>CFPS 27E</th><th>Value</th><th>vs. price</th></tr>{sens}</table>
<div class="src">Value applies 2.0x NAV and 25x CFPS at each price. The bold row approximates our base deck; our base case is slightly higher because 2027–2029 sit above US$3,500/oz.</div></div>
</div><div class="c2">
<div class="ex"><div class="ext">Exhibit 11 - Value and NAVPS vs. flat gold price (US$/share)</div><img src="v11/val.png">
<div class="src">Flat gold price from 2027 on the horizontal axis. Source: Northwall estimates.</div></div>
</div></div>
<div class="cols rule"><div class="c1">
<div class="ex"><div class="ext">Exhibit 12 - CFA Level II cross-checks</div>
<table class="t"><tr><th>Measure</th><th>Value</th><th>vs. price</th></tr>
<tr><td>CAPM cost of equity (4.97% + 0.58 × 5.0%)</td><td>{o['ke']*100:.2f}%</td><td></td></tr>
<tr><td>WACC (no debt)</td><td>{o['wacc']*100:.2f}%</td><td></td></tr>
<tr><td>Two-stage FCFF DCF, 2% terminal growth</td><td>US${f(o['dcf_ps'])}</td><td>{(o['dcf_ps']/PX-1)*100:+.0f}%</td></tr>
<tr><td>Residual income value</td><td>US${f(o['ri_ps'])}</td><td>{(o['ri_ps']/PX-1)*100:+.0f}%</td></tr>
<tr><td>NAV per share (5% real)</td><td>US${f(navps)}</td><td>{(navps/PX-1)*100:+.0f}%</td></tr>
<tr class="b"><td>Growth implied by price (ke − CF1/P)</td><td>{o['g_impl']*100:.2f}%</td><td></td></tr></table>
<div class="src">DCF: FCFF 2027E–2030E at WACC, Gordon terminal value (79% of EV). Residual income: RI held flat after 2030 (persistence of 1). Source: Northwall Excel model v2026Q2.</div></div>
</div><div class="c2">
<h2>What the cross-checks say</h2>
<p>Absolute methods value FNV well below the share price: our DCF gives US${f(o['dcf_ps'])} and residual income US${f(o['ri_ps'])}, because the business earns high returns on a small book. That gap is the premium the market pays for scarcity, optionality and the balance sheet, and it is why we anchor the target on the multiples where royalty companies actually trade.</p>
<p>The reverse DCF frames the debate. At US${f(PX)}, the market discounts about {o['g_impl']*100:.1f}% perpetual growth in cash flow at a {o['ke']*100:.1f}% cost of equity. Our forecast has GEO volumes growing about 3% a year. The price needs execution and some deal-making to hold, which is consistent with a Hold rather than a Buy.</p>
</div></div>
</div>

<!-- PAGE 4: CATALYSTS AND RISKS -->
<div class="pb"><h1>Catalysts and risks</h1>
<p class="lede">Most near-term catalysts de-risk growth already in our model. Cobre Panamá is the one binary event, and gold is the one variable that moves everything.</p>
<div class="ex"><div class="ext">Exhibit 13 - Catalyst calendar</div>
<table class="t txt"><tr><th style="width:17%">Timing</th><th style="width:33%">Event</th><th>Why it matters</th></tr>
<tr><td>Nov 11, 2026</td><td>Q3 2026 results</td><td>First Cobre Panamá stockpile deliveries; tests the H2 weighting and our 138k GEO Q3 estimate</td></tr>
<tr><td>4Q26</td><td>Côté Gold reserve and mine plan (IAMGOLD)</td><td>Path to 40ktpd on a 7.5% gross metal royalty; 20.3 Moz M&amp;I resource now consolidated with Gosselin</td></tr>
<tr><td>4Q26</td><td>Archimedes first gold (i-80 Gold)</td><td>New Nevada production on a 1.5% royalty</td></tr>
<tr><td>Late 2026</td><td>Copper World sanction (Hudbay); PSJ Cobre Mendocino feasibility</td><td>Two long-life copper-gold assets that underpin growth from 2029</td></tr>
<tr><td>4Q26–1H27</td><td>Castle Mountain and AurMac permits, then investment decisions</td><td>Converts development royalties into funded projects</td></tr>
<tr><td>1Q27</td><td>Bullabulling definitive feasibility study</td><td>PFS outlines ~150 koz/yr for 19 years from 4Q28 on a 2.45% royalty</td></tr>
<tr><td>Mar 2027</td><td>2027 guidance; annual dividend decision</td><td>Guidance reset at new price assumptions; 20th straight increase likely</td></tr>
<tr><td>Open</td><td>Panama ministerial commission on Cobre Panamá</td><td>Restart worth up to ~US${f(m['cobre_full_ps'], 0)}/sh unrisked; closure removes our US${f(cobre_ps)}/sh</td></tr>
<tr><td>2H27–2029</td><td>Candelaria underground ramp; Valentine Phase 2; Stibnite start-up</td><td>Delivers the 2030 outlook</td></tr></table></div>
<div class="ex rule"><div class="ext">Exhibit 14 - Risks, sized</div>
<table class="t txt"><tr><th style="width:17%">Risk</th><th>Description</th><th style="width:30%">Estimated impact</th></tr>
<tr><td>Gold price</td><td>About 70% of revenue is gold. Our deck already sits below spot, but a deeper correction would compress earnings and multiples.</td><td>Each US$250/oz moves 2027E CFPS by ~{m['cf_sens250'] * 100:.0f}%</td></tr>
<tr><td>Cobre Panamá</td><td>Permanent closure, or a restart on terms that impair the stream.</td><td>–US${f(cobre_ps)}/sh to NAV (~{cobre_ps / navps * 100:.0f}%)</td></tr>
<tr><td>Operator execution</td><td>Grade sequencing at Candelaria, Côté ramp-up, Valentine guidance cut after the Orla merger.</td><td>10% GEO shortfall in 2027 ≈ {abs(m['geo_short10']) * 100:.0f}% lower CFPS</td></tr>
<tr><td>Capital allocation</td><td>Pressure to deploy US$4.3 billion at cycle-high gold prices risks overpaying for growth.</td><td>Hard to size; value-destructive at scale</td></tr>
<tr><td>Tax</td><td>CRA reassessments, global minimum tax, PFIC status for U.S. holders.</td><td>Each 1pt on the tax rate ≈ 1.3% of earnings</td></tr>
<tr><td>Energy prices</td><td>Oil, gas and NGL were ~12% of Q2 2026 revenue.</td><td>US$10/bbl WTI ≈ 12% of oil revenue (company)</td></tr>
<tr><td>Multiple compression</td><td>Royalty premiums can narrow when gold equities fall out of favour.</td><td>1.5x NAV and 20x CF ≈ US$194/sh</td></tr></table></div>
<div class="cols rule"><div class="c1">
<h2>Bear, base and bull</h2>
<p>Our bear case of ~US${f(m['bear'], 0)} assumes US$3,000/oz gold flat, no Cobre Panamá restart, 1.5x NAV and 20x cash flow. Our bull case of ~US${f(m['bull'], 0)} assumes US$4,500/oz gold, a full restart, 2.25x NAV and 28x cash flow. From today's price that is about US${PX - m['bear']:.0f} of downside against US${m['bull'] - PX:.0f} of upside, a skew that supports holding the shares but not adding at this price.</p>
<p>The swing variables are not symmetric. Gold moves every line of the model, while Cobre Panamá is a single event with a binary outcome. We would rather own that option at a lower entry point than pay for it now.</p>
</div><div class="c2">
<div class="ex"><div class="ext">Exhibit 15 - Revenue and adjusted EBITDA (US$M)</div><img src="v11/rev.png">
<div class="src">Labels show adjusted EBITDA margin. Source: company filings, Northwall estimates.</div></div>
</div></div></div>

<!-- PAGE 5: MODEL AND DISCLOSURES -->
<div class="pb"><h1>Northwall model</h1>
<p class="lede">2025A from the annual report; 2026E combines reported H1 results with our H2 forecast. US$ millions unless noted.</p>
<div class="ex"><div class="ext">Exhibit 16 - Financial summary</div>
<table class="t"><tr><th>FY Dec</th>{''.join(f'<th>{l}</th>' for l in lab)}</tr>{fin}</table>
<div class="src">Key assumptions: realized revenue per GEO at 97% of the gold price (in line with H1 2026); cost of sales 7.8% of revenue; G&amp;A and share-based compensation US$42M growing 3% a year; tax rate 22% (H1 2026 effective ~22%); cash taxes 80% of the total; US$500M a year of acquisitions from 2027 with no production credit taken; dividend growing ~US$0.16/share a year. 2026 GEOs at the company's fixed guidance conversion ratios. 2026E adjusted EPS includes the US$63.8M Q1 Cascabel buy-back gain, which FNV no longer excludes from adjusted net income.</div></div>
<div class="ex"><div class="ext">Exhibit 17 - Financial analysis ratios</div>
<table class="t"><tr><th>Ratio</th><th>2025A</th><th>2026E</th><th>2027E</th><th>2028E</th><th>2029E</th></tr>
<tr><td>Adjusted EBITDA margin</td><td>90.9%</td><td>90.7%</td><td>90.3%</td><td>90.1%</td><td>90.0%</td></tr>
<tr><td>Net margin (adjusted NI / revenue)</td><td>59.0%</td><td>62.5%</td><td>58.5%</td><td>57.6%</td><td>56.7%</td></tr>
<tr><td>Equity turnover (revenue / average equity)</td><td>–</td><td>0.29x</td><td>0.24x</td><td>0.21x</td><td>0.19x</td></tr>
<tr class="b"><td>Return on average equity (DuPont: margin × turnover)</td><td>–</td><td>18.2%</td><td>14.1%</td><td>12.0%</td><td>10.7%</td></tr>
<tr><td>Cash conversion (operating cash flow / net income)</td><td>1.39x</td><td>1.28x</td><td>1.34x</td><td>1.36x</td><td>1.39x</td></tr>
<tr><td>Dividend payout (DPS / EPS)</td><td>27.2%</td><td>22.8%</td><td>28.6%</td><td>33.3%</td><td>37.6%</td></tr>
<tr><td>Reinvestment ((dividends + acquisitions) / OCF)</td><td>–</td><td>–</td><td>50.1%</td><td>54.8%</td><td>58.2%</td></tr></table>
<div class="src">No debt, so equity turnover carries the DuPont leverage term. ROE falls as cash builds on the balance sheet faster than we deploy it. Source: Northwall Excel model v2026Q2 (Ratios sheet).</div></div>
<div class="rule" style="margin-top:6px"><h2 style="margin-bottom:6px">Important disclosures</h2>
<div class="disc">
<p><b>Rating definitions.</b> Buy: expected 12-month total return (price appreciation plus dividends) above 15%. Hold: expected total return between 0% and 15%. Sell: expected total return below 0%. Price targets are 12-month forward.</p>
<p><b>Sources and methodology.</b> Financial information is taken from Franco-Nevada Corporation's public disclosure, including its news release and condensed interim financial statements for the quarter ended June 30, 2026 (dated August 11, 2026) and its 2025 annual results (dated March 10, 2026). Peer data are drawn from Wheaton Precious Metals' and Royal Gold's Q2 2026 releases. Market prices are as at October 26, 2026 unless otherwise stated. All forecasts, the net asset value, the price target and the rating are Northwall Research's own estimates and reflect our assumptions on commodity prices, production, costs and discount rates, any of which may prove wrong.</p>
<p><b>General disclaimer.</b> This report has been prepared by Northwall Research for informational purposes only. It does not constitute an offer to sell, or a solicitation of an offer to buy, any security, and it is not personalized investment advice. Investors should make their own decisions based on their own objectives and circumstances and consult a registered adviser where appropriate. The information herein is believed to be reliable but is not guaranteed as to accuracy or completeness. Opinions and estimates are as of the date of this report and are subject to change without notice. Past performance is not indicative of future results.</p>
<p><b>Forward-looking statements.</b> Statements regarding Franco-Nevada's operations, the operations of the third-party mines that underlie its royalties and streams, commodity prices, and the outcome of regulatory processes, including those relating to Cobre Panamá, are inherently uncertain. Actual results may differ materially.</p>
<p><b>Analyst certification.</b> The views expressed in this report accurately reflect the analyst's personal views about the subject company and its securities. No part of the analyst's compensation was, is, or will be directly or indirectly related to the specific recommendation or views contained in this report. Basel Al-Ghousein is a Level II candidate for the CFA designation. Northwall Research is not a registered dealer.</p>
<p>© 2026 Northwall Research. All rights reserved.</p>
</div></div></div>
</body></html>'''
open('v11/report.html', 'w').write(html)
HTML('v11/report.html', base_url='.').write_pdf('v11/FNV_v11.pdf')
print('built')
