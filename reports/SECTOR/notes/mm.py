from kit import *
import kit
kit.EX[0] = 2  # Exhibits 1 and 2 sit on the front page


def pair(a, ta, sa, b, tb, sb):
    n1 = kit.EX[0] + 1; n2 = n1 + 1; kit.EX[0] = n2
    raw(f'''<div class="ex wide" style="border:0;padding:0"><table style="width:100%;border-collapse:collapse;table-layout:fixed"><tr>
<td style="width:50%;vertical-align:top;padding-right:9pt;border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding-top:4pt;padding-bottom:4pt"><div class="ext">Exhibit {n1}: {ta}</div><img src="{a}" style="width:100%"><div class="src">Source: {sa}</div></td>
<td style="width:50%;vertical-align:top;padding-left:9pt;border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding-top:4pt;padding-bottom:4pt"><div class="ext">Exhibit {n2}: {tb}</div><img src="{b}" style="width:100%"><div class="src">Source: {sb}</div></td></tr></table></div>''')
    return n1, n2


FRONT = '''<div class="fp-title"><h1>Gold Equities: Margins Hold as Bullion Resets</h1>
<div class="sub">Producers still clear US$2,300 to US$3,000/oz over costs at today&rsquo;s price. We prefer growth with falling costs (Alamos, Buy) over premium quality (Franco-Nevada, Hold).</div></div>
<div class="fp-who"><b>Basel Al-Ghousein</b> (Analyst), Northwall Research <span>&nbsp;|&nbsp; Prices as of October 26&ndash;27, 2026</span></div>
<div class="fp"><div class="l">
<h2 style="margin-top:0">Our view</h2>
<p>Gold has fallen about 27% from its January record, but the reset leaves miners with near-record margins. Our deck already sits below spot, so the correction does not change our targets or ratings. The stock-picking question has moved from leverage to cost trajectory and balance-sheet discipline. On that test, Alamos Gold screens best in our coverage and Franco-Nevada remains fully valued.</p>
<h2>Key points</h2>
<ul class="kp">
<li><b class="n">(1) The reset has a clear cause.</b> The Iran conflict pushed oil toward US$100/bbl, which lifted inflation expectations and bond yields. The US 10-year reached 5.20% on September 24, and gold fell 8.5% that month. Markets now price Fed hikes from a 4% upper bound to 4.75%&ndash;5.0% by next summer.</li>
<li><b class="n">(2) Flows have already turned.</b> Gold ETFs added 211 t in Q3 after 45 t of Q2 outflows, and US-listed funds took in US$11.7 billion. Central banks bought 289 t in Q2, up 62% year on year. Equities lagged: about US$1 billion left GDX in September.</li>
<li><b class="n">(3) Margins are the cushion.</b> Newmont earned about US$2,863/oz over AISC in Q3, and Agnico Eagle about US$3,024/oz in Q2. Industry AISC rose 16% year on year to US$1,785/oz in Q1, so cost inflation is now the variable to watch.</li>
<li><b class="n">(4) Alamos over Franco-Nevada.</b> Alamos (Buy, US$39.00) grows output about 80% to 960 koz by 2030E as AISC falls toward US$1,200/oz. It stays a Buy down to about US$3,460/oz gold held flat. Franco-Nevada (Hold, US$250.00) needs gold held flat near US$3,960/oz to reach our Buy band.</li>
</ul>
<div class="ex" style="border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding:4pt 0;margin-top:8pt"><div class="ext">Exhibit 2: Implied 12-Month Total Return vs. Gold Price Held Flat from 2027</div><img src="img/m_returns.png">
<div class="src">Source: Northwall Excel models (v2026Q2) run through the house engine; returns include the forward dividend</div></div></div>
<div class="r">
<div class="side-t">Coverage</div>
<table class="cv"><tr><th>Company</th><th>Rating</th><th>Price</th><th>Target</th><th>Return</th></tr>
<tr><td>Alamos Gold (AGI)</td><td class="Buy">Buy</td><td>US$30.21</td><td>US$39.00</td><td>29.6%</td></tr>
<tr><td>Franco-Nevada (FNV)</td><td class="Hold">Hold</td><td>US$230.76</td><td>US$250.00</td><td>9.1%</td></tr></table>
<div class="side-t">Northwall gold deck (US$/oz)</div>
<table class="cv"><tr><th></th><th>H2-26E</th><th>2027E</th><th>2028E</th><th>LT</th></tr><tr><td>Gold</td><td>4,200</td><td>4,000</td><td>3,800</td><td>3,500</td></tr>
<tr><td>Spot, Oct 27</td><td colspan="4">US$4,076</td></tr></table>
<div class="ex" style="border-top:0.8pt solid #0F1A2B;border-bottom:0.8pt solid #0F1A2B;padding:4pt 0"><div class="ext">Exhibit 1: Realized Price vs. AISC (US$/oz)</div><img src="img/m_margins.png">
<div class="src">Source: company reports via Discovery Alert (Newmont, Agnico Eagle); World Gold Council (industry AISC); Alamos H1-26 filings; Northwall Research</div></div>
<div class="disc-mini">Total return includes the forward dividend. Ratings: Buy above 15%, Hold 0&ndash;15%, Sell below 0%. Estimates, targets and ratings are Northwall Research opinions. See important disclosures at the end of this report.</div>
</div></div>'''

# ---------------- 1. Gold ----------------
sec('Gold: A Reset, Not a Reversal', 'gold', 'Gold fell further and faster than most expected in 2026. The drivers were rates and liquidity rather than a loss of demand, and flows have already turned.')
side('Gold fell at the outbreak of the conflict instead of rising as a safe haven.')
p(f'Gold set a record near US$5,595/oz in January, then fell to a US$3,999 low on July 13 (Exhibit {nextex()}). The trigger was the Iran conflict. Oil moved toward US$100/bbl, inflation expectations rose, and the Fed lost room to cut. Gold fell at the outbreak instead of rising as a safe haven, as investors sold winning positions to cover losses elsewhere.',
  'September added a second leg. The US 10-year yield reached 5.20% on September 24, its highest since 2007, and gold fell 8.5% in the month. The dollar rose to two-month highs, and markets now price Fed hikes from a 4% upper bound to 4.75%&ndash;5.0% by next summer. Gold closed at US$4,076/oz on October 27.')
exhibit('Gold Price: 2025 Monthly Averages and Selected 2026 Observations (US$/oz)', 'img/m_gold_path.png', 'MetalCharts (2025 monthly averages); Discovery Alert citing Reuters (2026 record, July low and September); State Street Global Advisors; Northwall market tape (October 27)', wide=True)
h2('Our deck already assumes the correction')
p(f'Our deck steps from US$4,200/oz in H2-26 to US$4,000 in 2027 and US$3,500 long term. That sits at the bottom of State Street&rsquo;s bear case and well below its base case (Exhibit {nextex()}). We therefore make no deck change. Spot would need to fall about 14% and stay there before our long-term price looked generous.')
exhibit('Where Our Deck Sits Against Published Scenarios (US$/oz)', 'img/m_scenarios.png', 'State Street Global Advisors, Monthly Gold Monitor, October 2026; Northwall Research')
h2('Flows have turned before prices')
tbl(['Flow', 'Period', 'Amount', 'Read-through'], [
    ['Gold ETFs (global)', 'Q2 2026', '&minus;45 t', 'Profit-taking near the highs'],
    ['Gold ETFs (global)', 'Q3 2026', '+211 t', 'Europe and North America led the return'],
    ['US-listed gold ETFs', 'Q3 2026', '+US$11.7 billion', 'Includes +US$3.7 billion in September'],
    ['Central banks', 'Q2 2026', '289 t (+62% y/y)', 'Structural buyer; H1 total of 345 t was the lowest since 2022'],
    ['VanEck Gold Miners ETF (GDX)', 'September 2026', 'About &minus;US$1 billion', 'Equities sold harder than bullion'],
], widths=['26%', '16%', '20%', '38%'])
B[-1] = B[-1].replace('<table class="t ', f'<div class="ext">Exhibit {nextex()}: Gold Investment and Official-Sector Flows, 2026</div><table class="t ', 1) + '<div class="src">Source: State Street Global Advisors; World Gold Council and SSGA via Discovery Alert (October 27, 2026); Northwall Research</div>'
kit.EX[0] += 1
p('Bullion ETFs bought the September dip while gold equities saw outflows. In our experience that gap closes as quarterly results confirm margins, which makes the Q3 season the near-term catalyst for the group.')

# ---------------- 2. Margins and costs ----------------
sec('Miners: Margins Near Record, Costs Rising', 'margins', 'At US$4,000 gold the average producer still earns over US$2,200/oz above all-in sustaining costs. Cost inflation, not price, is now the main threat to that margin.')
side('Margins near US$3,000/oz give producers room to absorb a further pullback.')
p('Large producers reported margins close to US$3,000/oz over AISC in the most recent quarters. Newmont realized US$4,317/oz in Q3 against AISC of US$1,454/oz. Agnico Eagle realized US$4,483/oz in Q2 against AISC of US$1,459/oz. Alamos realized US$4,660/oz in H1 against AISC of US$1,793/oz, a margin of about US$2,867/oz.',
  'Costs are moving the other way. The World Gold Council put industry AISC at US$1,785/oz in Q1, up 16% year on year, and Barrick reported US$1,866/oz in Q2. RBC Capital Markets expects 2027 AISC to rise a further 4% and capital spending 16% (as reported by Discovery Alert). Royalties and production taxes rise with the gold price, so some of that inflation is the price itself.')
exhibit('Valuation: Gold Producers and Royalty Companies on Price to Cash Flow', 'img/m_comps.png', 'Company Q2-26 filings; Northwall calculations. Prices as of October 26&ndash;27, 2026', wide=True)
p('Alamos trades at 13.7x annualized Q2 cash flow, above Agnico Eagle and Kinross, because the market is looking through a trough year. On our 2027E cash flow per share of US$3.50 the multiple falls to 8.6x, and to 7.2x on 2028E. Franco-Nevada trades at 22.2x, a premium to both royalty peers that already reflects its diversification and net cash.')

# ---------------- 3. Where the value is ----------------
sec('Where the Value Is', 'value', 'We frame both names by the gold price they need to justify a rating. Alamos keeps a wide margin of safety; Franco-Nevada needs gold to hold near today&rsquo;s level.')
p(f'Exhibit 2 on page 1 runs each model with gold held flat from 2027, at every price from US$3,000 to US$5,600/oz. Alamos stays in our Buy band down to about US$3,460/oz and only turns negative below about US$3,160/oz. Franco-Nevada needs about US$3,960/oz held flat to reach the Buy band, and falls below zero near US$3,385/oz.')
tbl(['', 'Alamos Gold (AGI)', 'Franco-Nevada (FNV)'], [
    ['Rating and target', 'Buy, US$39.00', 'Hold, US$250.00'], ['Share price (Oct 26)', 'US$30.21', 'US$230.76'], ['Implied all-in return', '29.6%', '9.1%'],
    ['Valuation method', '50% P/NAV (1.0x) + 50% P/CF 2027E (10x)', '50% P/NAV (2.0x) + 50% P/CF 2027E (25x)'],
    ['NAV per share (5% real)', 'US$42.35', 'US$138.88'], ['P/NAV', '0.71x', '1.66x'], ['2027E CFPS', 'US$3.50', 'US$9.00'],
    ['CAPM cost of equity', '9.97% (beta 1.0)', '7.87% (beta 0.58)'], ['Growth implied by price (reverse DCF)', '&minus;1.6%', '4.0%'],
    ['Target at gold held flat at US$4,000/oz', 'US$43', 'US$265'],
], widths=['36%', '32%', '32%'])
B[-1] = B[-1].replace('<table class="t ', f'<div class="ext">Exhibit {nextex()}: Coverage Valuation Summary</div><table class="t ', 1) + '<div class="src">Source: Northwall Excel models v2026Q2; company filings</div>'
kit.EX[0] += 1
side('Alamos is priced as if cash flow shrinks; Franco-Nevada as if it grows 4% forever.')
p('The reverse DCF frames the debate. At US$30.21, Alamos is priced for cash flow that shrinks slightly forever, despite visible growth. At US$230.76, Franco-Nevada is priced for 4.0% perpetual growth, above the roughly 3% volume growth we forecast. That gap, rather than a view on gold, drives our relative preference.')

# ---------------- 4. Assets ----------------
sec('Where Our Coverage Operates', 'assets', 'Both names are anchored in the Americas, and both are concentrated in northern Ontario and Quebec, one of the best-ranked mining jurisdictions in the world.')
p(f'Ontario ranked second globally in the Fraser Institute&rsquo;s 2025 investment attractiveness index, up from fifteenth in 2024. Alamos earns most of its value from Island Gold, Magino and Young-Davidson in Ontario. Franco-Nevada&rsquo;s royalties on C&ocirc;t&eacute;, Detour Lake, Canadian Malartic and Greenstone sit in the same corridor (Exhibits {nextex()} and {nextex() + 1}).')
exhibit('Northwall Gold Coverage: Operations, Royalties and Streams in the Americas', '<img src="img/map_americas.png" style="width:2.95in;display:block;margin:0 auto">', 'Natural Earth (boundaries); company disclosures; Northwall Research. Locations approximate')
exhibit('Northern Ontario and Quebec: Where Both Names Overlap', 'img/map_abitibi.png', 'Natural Earth (boundaries); company disclosures; Northwall Research. Belt outline and locations approximate', wide=True)

# ---------------- 5. Company snapshots ----------------
sec('Company Snapshots', 'companies')
raw('<div class="co-h"><div class="n">Alamos Gold (NYSE/TSX: AGI)</div><div class="t"><b>Buy</b> &nbsp;|&nbsp; Target US$39.00 &nbsp;|&nbsp; Return 29.6%</div></div>')
p('Alamos is the clearest case in our coverage of growth arriving as costs fall. We model output rising from 535 koz in 2026E to 960 koz in 2030E. AISC falls from about US$1,826/oz this year to US$1,200/oz as Island Gold Phase 3+ and the Magino mill expansion arrive. Free cash flow rises from about US$364 million in 2026E to US$935 million in 2028E at our deck.')
exhibit('Alamos: Production Rises While AISC Falls (2025A&ndash;2030E)', '<img src="img/m_agi.png" style="width:3.6in;display:block;margin:0 auto">', 'Company filings (2025A, H1-26A); Northwall estimates')
p('2026 is the trough. July&rsquo;s guidance cut to 510&ndash;560 koz reflected a seismic event at Young-Davidson and slower recoveries at La Yaqui Grande. Q3 results arrive after the close today, with the call on October 29. We will look for (1) Young-Davidson back toward 5,000 tpd, (2) Phase 3+ shaft equipping on schedule, and (3) no further change to cost guidance.')
raw('<div class="co-h"><div class="n">Franco-Nevada (NYSE/TSX: FNV)</div><div class="t"><b>Hold</b> &nbsp;|&nbsp; Target US$250.00 &nbsp;|&nbsp; Return 9.1%</div></div>')
p('Franco-Nevada earned a 91% adjusted EBITDA margin in H1 2026, carries no debt and has US$4.3 billion of available capital. We forecast 552k GEOs in 2026E, rising to 600k by 2030E, inside management&rsquo;s 555&ndash;615k outlook. Cobre Panam&aacute; stockpile processing is in our numbers; a full restart is risked at 35% and worth US$8.44 per share.',
  'Our hesitation is price. At 1.66x NAV and 25.6x 2027E cash flow, the shares already credit the quality. A pullback below about US$215 would lift the expected return above our Buy hurdle. Q3 results on November 11 should show the first Cobre Panam&aacute; stockpile deliveries.')

# ---------------- 6. Risks ----------------
sec('Risks to Our View', 'risks')
p('We highlight: (1) a deeper gold correction, if real yields keep rising as markets price more Fed hikes; (2) cost inflation in labour, energy and consumables, which could erode margins faster than we model; (3) execution at Alamos on Phase 3+, Magino and Lynn Lake, where initial capital rose to US$937 million; (4) Cobre Panam&aacute;, where closure removes US$8.44 per share from Franco-Nevada&rsquo;s NAV and a restart adds up to about US$24; and (5) resource nationalism, which tends to rise late in price cycles. Upside risks include (6) a faster end to the Middle East conflict, which would lower oil and yields, and (7) renewed central-bank buying at 2022&ndash;2024 levels.')

# ---------------- 7. Catalysts ----------------
sec('Catalyst Calendar', 'catalysts')
exhibit('Coverage Catalysts, November 2026 to 2029', 'img/m_catalysts.png', 'Company disclosures; Northwall Research', wide=True)
tbl(['Date', 'Company', 'Event', 'What we will watch'], [
    ['Oct 28, 2026', 'AGI', 'Q3 2026 results (call Oct 29)', 'Young-Davidson tonnage; cost guidance; shaft progress'],
    ['Nov 11, 2026', 'FNV', 'Q3 2026 results', 'First Cobre Panam&aacute; stockpile ounces; Q3 GEOs vs. our 138k estimate'],
    ['4Q26', 'FNV', 'C&ocirc;t&eacute; Gold reserve and 40ktpd plan (IAMGOLD)', 'Scale of the 7.5% gross metal royalty'],
    ['Early 2027', 'AGI, FNV', 'New guidance', 'AGI three-year outlook; FNV 2027 GEOs and a likely 20th dividend increase'],
    ['1Q27', 'AGI', 'Island Gold Phase 3+ shaft commissioning', 'Mining rates rising to 2,400 tpd'],
    ['Mid-2027', 'AGI', 'PDA first production (Mulatos District)', 'Lower-cost Mexican ounces'],
    ['1Q28', 'AGI', 'Magino mill expansion to 20,000 tpd', 'The step that drives 2028E AISC to US$1,350/oz'],
    ['Open', 'FNV', 'Panama ruling on Cobre Panam&aacute;', 'Restart worth up to ~US$24 per share unrisked'],
], widths=['14%', '11%', '35%', '40%'])

# ---------------- Disclosures ----------------
sec('Important Disclosures', 'disclosures')
raw('''<div class="disc"><p><b>Ratings and targets.</b> Alamos Gold Inc.: Buy, 12-month target US$39.00. Franco-Nevada Corporation: Hold, 12-month target US$250.00. Both as published October 27, 2026; this note does not change either rating or target. Buy: expected 12-month total return above 15%. Hold: 0% to 15%. Sell: below 0%. Total return includes the forward dividend.</p>
<p><b>Sources.</b> Facts are attributed to their sources in the text. Third-party views (State Street Global Advisors, RBC Capital Markets, the World Gold Council) are cited as reported and are not Northwall estimates. Estimates, sensitivities, targets and ratings are Northwall Research&rsquo;s own and come from our Excel models (v2026Q2).</p>
<p><b>General.</b> This report is for information only. It is not investment advice or an offer or solicitation to buy or sell any security. Information is believed reliable but is not guaranteed. Opinions are as of the date of this report and may change without notice. Northwall Research is not a registered dealer or adviser. The analyst holds no position in the companies covered.</p>
<p><b>Analyst certification.</b> The views expressed accurately reflect the analyst&rsquo;s personal views. No part of the analyst&rsquo;s compensation is related to any rating or view. Basel Al-Ghousein is a Level II candidate for the CFA designation. &copy; 2026 Northwall Research. All rights reserved.</p></div>''')
