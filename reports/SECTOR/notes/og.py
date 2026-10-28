from kit import *
import kit
def pair(a, ta, sa, b, tb, sb):
    n1 = kit.EX[0] + 1; n2 = n1 + 1; kit.EX[0] = n2
    raw(f'''<div class="ex wide" style="border:0;padding:0"><table style="width:100%;border-collapse:collapse;table-layout:fixed"><tr>
<td style="width:50%;vertical-align:top;padding-right:9pt;border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding-top:4pt;padding-bottom:4pt"><div class="ext">Exhibit {n1}: {ta}</div><img src="{a}" style="width:100%"><div class="src">Source: {sa}</div></td>
<td style="width:50%;vertical-align:top;padding-left:9pt;border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding-top:4pt;padding-bottom:4pt"><div class="ext">Exhibit {n2}: {tb}</div><img src="{b}" style="width:100%"><div class="src">Source: {sb}</div></td></tr></table></div>''')
    return n1, n2

kit.EX[0] = 2  # Exhibits 1 and 2 sit on the front page

FRONT = '''<div class="fp-title"><h1>Canadian Oil: Windfall Prices, Narrowing Exits</h1>
<div class="sub">WTI near US$100 is a cash windfall our deck does not count on. The bigger Canadian risk is a widening WCS discount as pipelines fill. We prefer Whitecap (Buy) over Greenfire (Buy, higher risk).</div></div>
<div class="fp-who"><b>Basel Al-Ghousein</b> (Analyst), Northwall Research <span>&nbsp;|&nbsp; Prices as of October 27, 2026</span></div>
<div class="fp"><div class="l">
<h2 style="margin-top:0">Our view</h2>
<p>Oil is priced for disruption. Brent closed at US$109.44 and WTI at US$99.87 on October 27, with 4.8 million bbl/d of Middle East crude still shut in during September. Our deck fades WTI to US$80 in 2027 and US$70 from 2029, close to the EIA&rsquo;s own path. We value our names on that deck, so today&rsquo;s prices are upside to cash flow rather than to our targets.</p>
<h2>Key points</h2>
<ul class="kp">
<li><b class="n">(1) Supply, not demand, sets the price.</b> Shut-ins peaked at 10.9 million bbl/d in May. The EIA expects 4.5 million bbl/d in 4Q26 and a return to normal by end-2Q27, taking Brent to about US$74 by 4Q27.</li>
<li><b class="n">(2) Canada is filling its pipes.</b> Trans Mountain hit apportionment in June and Enbridge&rsquo;s Mainline cut heavy nominations 16% in October. WCS at Hardisty traded US$28 under WTI on October 21, the widest since November 2023.</li>
<li><b class="n">(3) Whitecap is the cleaner exposure.</b> At our US$80 deck it earns C$2.3 billion of free funds flow in 2027E, a 9.4% yield. Its dividend breaks even at US$63.40 WTI, and the stock stays a Buy down to about US$79.</li>
<li><b class="n">(4) Greenfire carries the differential risk.</b> A sustained US$28 WCS discount would cut its 2027E EBITDA by about one-third and its target to US$6.75. The Connacher deal doubles its scale, but at 0.82x 2027E leverage it has less room for error.</li>
</ul>
<div class="ex" style="border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding:4pt 0;margin-top:8pt"><div class="ext">Exhibit 2: Implied 12-Month Total Return vs. WTI Held Flat from 2027</div><img src="img/o_returns.png">
<div class="src">Source: Northwall Excel models (v2026Q2) run through the house engine; Greenfire at our US$15 WCS discount; returns include the forward dividend</div></div></div>
<div class="r">
<div class="side-t">Coverage</div>
<table class="cv"><tr><th>Company</th><th>Rating</th><th>Price</th><th>Target</th><th>Return</th></tr>
<tr><td>Whitecap (WCP)</td><td class="Buy">Buy</td><td>C$20.43</td><td>C$24.00</td><td>21.0%</td></tr>
<tr><td>Greenfire (GFR)</td><td class="Buy">Buy</td><td>US$7.00</td><td>US$8.25</td><td>17.9%</td></tr></table>
<div class="side-t">Northwall oil deck</div>
<table class="cv"><tr><th></th><th>H2-26E</th><th>2027E</th><th>2028E</th><th>2029E+</th></tr><tr><td>WTI (US$/bbl)</td><td>91.5</td><td>80</td><td>72</td><td>70</td></tr>
<tr><td>WCS disc. (US$)</td><td>15</td><td>15</td><td>15</td><td>15</td></tr><tr><td>USD/CAD</td><td>1.40</td><td>1.38</td><td>1.38</td><td>1.38</td></tr>
<tr><td>Spot, Oct 27</td><td colspan="4">WTI US$99.87 &middot; Brent US$109.44</td></tr></table>
<div class="ex" style="border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding:4pt 0"><div class="ext">Exhibit 1: Middle East Crude Shut-Ins (Million bbl/d)</div><img src="img/o_shutins.png">
<div class="src">Source: US EIA, Short-Term Energy Outlook, October 2026</div></div>
<div class="disc-mini">Total return includes the forward dividend. Ratings: Buy above 15%, Hold 0&ndash;15%, Sell below 0%. Estimates, targets and ratings are Northwall Research opinions. See important disclosures at the end of this report.</div>
</div></div>'''

# ---------------- 1. Global oil ----------------
sec('Global Oil: Priced for Disruption', 'global', 'The 2026 oil market is a supply story. Prices will follow how fast Middle East barrels return, not how fast demand grows.')
side('A single attack on the East-West pipeline sent Brent to US$131 for a day in September.')
p(f'The conflict involving Iran has shut in Middle East crude since the spring. Shut-ins peaked at 10.9 million bbl/d in May, fell to 5.8 million in August and 4.8 million in September (Exhibit 1). Convoys, ship-to-ship transfers and bypass pipelines are slowly raising exports. Attacks on Saudi Arabia&rsquo;s East-West pipeline, the main route around the Strait of Hormuz, sent Brent to US$131/bbl on September 15 (Exhibit {nextex()}).')
exhibit('The Gulf&rsquo;s Chokepoints and Bypass Routes', 'img/map_hormuz.png', 'US EIA, Short-Term Energy Outlook, October 2026 (shut-ins and the September 15 Brent spike); Natural Earth; Northwall Research. Routes schematic')
p('Global inventories fell an estimated 1.9 million bbl/d in Q3 and are forecast to fall a further 0.7 million bbl/d in Q4. Record tanker rates, higher insurance costs and tight diesel markets add to the premium. The EIA raised its 4Q26 Brent forecast by US$14 to about US$105/bbl.')
h2('Our deck assumes the premium fades')
p(f'We model WTI at US$91.50 for H2-26, US$80 in 2027, US$72 in 2028 and US$70 from 2029 (Exhibit {nextex()}). That is close to the EIA&rsquo;s path, which has WTI averaging US$79.74 in 2027 and Brent falling to US$87 by 2Q27 and US$74 by 4Q27. The EIA expects inventories to rebuild in 2027 as production outpaces demand, with OECD commercial stocks rising from 2,645 to 3,102 million barrels.')
exhibit('Spot and Forecasts: Northwall Deck vs. EIA STEO (US$/bbl)', 'img/o_deck.png', 'US EIA STEO, October 2026; Northwall market tape (October 27 close); Northwall Research', wide=True)
side('Every month that WTI stays near US$100 adds cash our targets do not count.')
p('The gap between spot and our deck is a windfall rather than a forecast. Each month WTI stays near US$100 adds cash flow our targets do not count. For Whitecap, a US$10/bbl move in 2027 WTI changes funds flow per share by about C$0.72, or 20%.')

# ---------------- 2. Canada egress ----------------
sec('Canada: The Pipes Are Filling Again', 'egress', 'Two years after Trans Mountain&rsquo;s expansion, Canadian production has caught up with export capacity. The WCS discount is the variable to watch.')
p(f'Western Canadian crude moves to market on three main systems (Exhibit {nextex()}). Trans Mountain carries up to 890,000 bbl/d to the Pacific coast, where tankers serve China, Korea and Japan. Enbridge&rsquo;s Mainline runs to the US Midwest and averaged 3.1 million bbl/d in Q2 2026. Keystone runs to Cushing and the Gulf Coast. WCS is priced at Hardisty, where the three systems meet.')
h2('From surplus capacity to apportionment')
side('Trans Mountain was only about 84% full last summer. By June 2026 it was rationing space.')
p('Trans Mountain was only about 84% full in summer 2025. It reached apportionment in June 2026 for the first time since its expansion, and was apportioned 7% in October. Enbridge cut heavy nominations by 16% at Superior and 7% at Kerrobert. Both companies cite rising demand, led by Asian buyers on Trans Mountain.',
  f'Canada produced a record 5.3 million bbl/d in 2025, and S&amp;P Global expects 5.5 million in 2026, 5.8 million in 2027 and 6.0 million in 2028. That is about 700,000 bbl/d of growth against roughly 730,000 bbl/d of announced capacity additions, much of it not due until 2027 or later (Exhibit {nextex() + 1}).')
exhibit('Western Canada: Producing Plays, Northwall Coverage and Export Routes', 'img/map_wcsb.png', 'Natural Earth (boundaries); CER, CAPP and company disclosures; Northwall Research. Play outlines and routes schematic', wide=True)

h2('The discount is already widening')
p(f'WCS at Hardisty traded US$28.00 under WTI on October 21, the widest since November 2023 (Exhibit {nextex() + 1}). Heavy barrels from Venezuela competing on the US Gulf Coast add to the pressure. CAPP estimates the discount averaged about US$13 after Trans Mountain&rsquo;s expansion, roughly US$3 narrower than before it. Before the expansion, constraints widened it by as much as US$20/bbl.')
pair('img/o_egress.png', 'Supply Growth vs. Announced Egress Additions, 2025&ndash;2028E (Million bbl/d)', 'S&amp;P Global Energy CERA via IndexBox; Reuters via BOE Report; CAPP. Mainline figure is an upper bound',
     'img/o_wcs.png', 'WCS Discount to WTI: Reference Points (US$/bbl)', 'CAPP, April 2026 (averages); Greenfire Q2-26 release; IndexBox (October 21, 2026)')
p(f'Exhibit {nextex()} shows the prices that set each benchmark. Light oil producers such as Whitecap sell close to WTI and Edmonton light prices. Oil sands producers such as Greenfire sell bitumen blends priced off WCS, so a wider discount hits them directly.')
exhibit('North American Crude Routes and Price Hubs', '<img src="img/map_routes.png" style="width:4.2in;display:block;margin:0 auto">', 'Natural Earth (boundaries); CER; Enbridge and Trans Mountain apportionment notices (October 2026); Northwall Research. Routes schematic')
p('Shell sanctioned LNG Canada Phase 2 in late September, which would add about 2 Bcf/d of gas demand and double capacity to 28 Mt a year in the early 2030s. AECO gas still traded near C$1.94/GJ in late September, because production is growing faster than LNG demand. Whitecap&rsquo;s Montney gas benefits over time, but we do not count on higher AECO prices.')

# ---------------- 3. Value ----------------
sec('Where the Value Is', 'value', 'Whitecap offers a large margin of safety on oil price. Greenfire offers more upside but depends on the WCS discount staying near our US$15 assumption.')
p('Exhibit 2 on page 1 runs both models with WTI held flat from 2027. Whitecap stays in our Buy band down to about US$79 WTI and turns negative below about US$74. Greenfire needs about US$78 WTI to stay a Buy at our US$15 discount, and turns negative below about US$69.')
tbl(['', 'Whitecap (WCP)', 'Greenfire (GFR)'], [
    ['Rating and target', 'Buy, C$24.00', 'Buy, US$8.25 (C$11.73)'], ['Share price', 'C$20.43 (Oct 23)', 'US$7.00 (C$9.81)'], ['Implied all-in return', '21.0%', '17.9%'],
    ['Valuation method', '50% EV/DACF (6.5x) + 50% free-funds-flow yield (8%)', '50% P/NAV (0.85x) + 50% EV/EBITDA 2027E (5.0x)'],
    ['2027E cash flow per share', 'C$3.65', 'C$2.50'], ['2027E free funds flow / free cash flow', 'C$2,335M', 'C$270M'],
    ['Net debt / leverage, 2027E', 'Net cash C$133M by year-end', '0.82x EBITDA'], ['Dividend breakeven WTI', 'US$63.40', 'No dividend'],
    ['CAPM cost of equity', '8.42% (beta 0.69)', '11.47% (beta 1.30)'], ['Target at WTI held flat at US$100', 'C$37', 'US$11.00'],
], widths=['34%', '33%', '33%'])
B[-1] = B[-1].replace('<table class="t ', f'<div class="ext">Exhibit {nextex()}: Coverage Valuation Summary</div><table class="t ', 1) + '<div class="src">Source: Northwall Excel models v2026Q2; company filings</div>'
kit.EX[0] += 1
exhibit('Valuation: Producers on Cash Flow and Heavy Oil on Flowing Barrels', 'img/o_comps.png', 'Company filings; Northwall calculations. Prices: WCP Oct 23, TOU Oct 22, SCR Oct 15, ATH Oct 16, GFR Oct 27, 2026', wide=True)
p('Whitecap trades at 5.0x EV to cash flow with a 14.9% free cash flow yield on annualized Q2 results, in line with Strathcona and well below Tourmaline. Greenfire trades at C$86,000 per flowing barrel, a discount to Strathcona and Athabasca Oil that reflects its smaller scale and higher leverage.')

# ---------------- 4. Companies ----------------
sec('Company Snapshots', 'companies')
raw('<div class="co-h"><div class="n">Whitecap Resources (TSX: WCP)</div><div class="t"><b>Buy</b> &nbsp;|&nbsp; Target C$24.00 &nbsp;|&nbsp; Return 21.0%</div></div>')
p(f'Whitecap is the largest Montney and Duvernay producer after its 2025 merger with Veren, at about 390,000 boe/d in H1 2026. It also runs light oil in the Viking and southeast Saskatchewan, including the Weyburn CO<sub>2</sub> flood. Our model has production growing about 3% a year on C$2.1 billion of annual capital. At our US$80 deck, 2027E free funds flow of C$2.3 billion covers the C$887 million base dividend 2.6 times (Exhibit {nextex()}).')
pair('img/o_wcp_fff.png', 'Whitecap: 2027E Free Funds Flow vs. WTI (C$ Millions)', 'Northwall Excel model v2026Q2; base dividend of C$0.73 per share on 1,215.7 million shares',
     'img/o_gfr_grid.png', 'Greenfire Price Target (US$) by WTI and WCS Discount', 'Northwall Excel model v2026Q2. Green: Buy; amber: Hold; red: Sell at US$7.00. Outlined: base case')
p('Net debt falls from C$2.5 billion at mid-year to about C$1.3 billion by December, and the company is net cash during 2027 at our deck. That gives room for buybacks or dividend growth. Q3 results and the 2027 budget are the next catalysts; dates are not yet confirmed.')
raw('<div class="co-h"><div class="n">Greenfire Resources (NYSE: GFR)</div><div class="t"><b>Buy</b> &nbsp;|&nbsp; Target US$8.25 &nbsp;|&nbsp; Return 17.9%</div></div>')
p(f'Greenfire runs SAGD oil sands projects at Hangingstone, south of Fort McMurray. The Connacher acquisition adds the Great Divide assets and takes production from about 16,000 bbl/d in 2025 to 40,000 bbl/d in 2027E. At our deck, 2027E EBITDA is C$645 million and leverage falls from 0.82x to net cash by 2029.',
  'The risk is the WCS discount. Exhibit 12 shows the target across WTI and the discount. Holding our US$80 WTI but widening the discount to US$28, today&rsquo;s level, cuts 2027E EBITDA to about C$423 million and the target to US$6.75, a Hold. The Q3 report, the first quarter with Connacher, is the next test.')

# ---------------- 5. Risks ----------------
sec('Risks to Our View', 'risks')
p('We highlight: (1) a fast end to the Middle East disruption, which could take WTI below our deck sooner than the EIA expects; (2) a wider and longer-lasting WCS discount as pipelines fill, the main risk for Greenfire; (3) cost inflation in steel, labour and services, which tends to follow high oil prices; (4) Canadian policy, including the federal emissions cap and carbon pricing; and (5) integration risk at Greenfire after the Connacher acquisition. Upside risks include (6) a longer disruption, (7) faster Trans Mountain and Mainline optimization, and (8) earlier LNG-driven AECO strength for Whitecap&rsquo;s Montney gas.')

# ---------------- 6. Catalysts ----------------
sec('Catalyst Calendar', 'catalysts')
exhibit('Sector and Coverage Catalysts, November 2026 to 2029', 'img/o_catalysts.png', 'US EIA; Trans Mountain; Enbridge; company disclosures; Northwall Research', wide=True)
tbl(['Date', 'Company or market', 'Event', 'What we will watch'], [
    ['Ongoing', 'Oil market', 'Middle East shut-ins and Hormuz convoys', 'Monthly EIA shut-in estimate vs. 4.5 million bbl/d assumed for 4Q26'],
    ['Monthly', 'Canada', 'Enbridge and Trans Mountain apportionment notices', 'Heavy apportionment above 15% signals a wider WCS discount'],
    ['TBC (Nov)', 'WCP', 'Q3 2026 results and 2027 budget', 'Capital near C$2.1 billion; buybacks; dividend growth'],
    ['TBC (Nov)', 'GFR', 'Q3 2026 results', 'First quarter with Connacher; realized WCS discount; integration costs'],
    ['End-2Q27', 'Oil market', 'EIA expects Middle East output near normal', 'The point where our deck and spot should converge'],
    ['2027 or later', 'Enbridge', 'Mainline optimization, up to 400,000 bbl/d', 'Timing of relief for heavy apportionment'],
    ['End-2028', 'Trans Mountain', 'Optimization adds about 300,000 bbl/d', 'Pacific access for heavy barrels'],
], widths=['13%', '16%', '35%', '36%'])

# ---------------- Disclosures ----------------
sec('Important Disclosures', 'disclosures')
raw('''<div class="disc"><p><b>Ratings and targets.</b> Whitecap Resources Inc.: Buy, 12-month target C$24.00. Greenfire Resources Ltd.: Buy, 12-month target US$8.25. Both as published October 27, 2026; this note does not change either rating or target. Buy: expected 12-month total return above 15%. Hold: 0% to 15%. Sell: below 0%. Total return includes the forward dividend.</p>
<p><b>Sources.</b> Facts are attributed to their sources in the text. Third-party forecasts (the US EIA, S&amp;P Global Energy CERA, CAPP) are cited as published and are not Northwall estimates. Estimates, sensitivities, targets and ratings are Northwall Research&rsquo;s own and come from our Excel models (v2026Q2).</p>
<p><b>General.</b> This report is for information only. It is not investment advice or an offer or solicitation to buy or sell any security. Information is believed reliable but is not guaranteed. Opinions are as of the date of this report and may change without notice. Northwall Research is not a registered dealer or adviser. The analyst holds no position in the companies covered. <b>Analyst certification.</b> The views expressed accurately reflect the analyst&rsquo;s personal views, and no part of the analyst&rsquo;s compensation is related to any rating or view. Basel Al-Ghousein is a Level II candidate for the CFA designation. &copy; 2026 Northwall Research. All rights reserved.</p></div>''')
