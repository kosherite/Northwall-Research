from kit import *

# ---------------- 9. Project Life Cycle ----------------
sec('Project Life Cycle', 'lifecycle',
    'A major new mine typically takes 10 to 20 years from discovery to first production, and only a small fraction of discoveries ever become mines.')
side('Each stage removes a different risk, and a single-asset company&rsquo;s share price tends to follow a predictable path as those risks fall away.')
p(f'Each stage removes a different risk, and the share price of a single-asset company tends to follow a predictable path as those risks fall away (Exhibit {nextex()}).')
exhibit('Typical Timeline for a Canadian Gold Project', 'img/timeline.png', 'Company reports; Northwall Research; illustrative', wide=True)
h2('Stages and Typical Durations')
tbl(['Stage', 'What happens', 'Typical duration', 'Main risk removed'], [
    ['<b>Grassroots exploration</b>', 'Mapping, geochemistry, geophysics, first drill holes', '1 to 5 years', 'Is there mineralization?'],
    ['<b>Discovery and delineation</b>', 'Step-out and infill drilling, first resource estimate', '2 to 5 years', 'Is it big and continuous enough?'],
    ['<b>Studies</b> (PEA, PFS, FS)', 'Metallurgical testwork, mine design, cost estimates, reserves', '2 to 5 years', 'Is it economic?'],
    ['<b>Permitting and approvals</b>', 'Environmental and social impact assessment, consultation, Indigenous agreements, permits', '2 to 10 years', 'Can it be built?'],
    ['<b>Financing and construction</b>', 'Debt, equity, streams; build mine, plant, tailings, power and roads', '2 to 5 years', 'Can it be funded and built on budget?'],
    ['<b>Commissioning and ramp-up</b>', 'Plant reaches design throughput and recovery', '6 to 24 months', 'Does it work as designed?'],
    ['<b>Production</b>', 'Steady-state mining, expansions, exploration near the mine', '10 to 50+ years', 'Can it sustain output and costs?'],
    ['<b>Closure and reclamation</b>', 'Decommissioning, land rehabilitation, water treatment, monitoring', 'Years to decades', 'Liabilities settled'],
], widths=['24%', '38%', '16%', '22%'])
h2('The Lassonde Curve')
side('The orphan period is where many acquisitions happen: majors buy de-risked deposits from juniors that cannot fund construction.')
p(f'Named after Franco-Nevada co-founder Pierre Lassonde, the curve shows why junior mining stocks often peak on discovery headlines, fall through the &ldquo;orphan period&rdquo; of studies and permitting, and re-rate as construction is de-risked and cash flow begins (Exhibit {nextex()}). In the orphan period, speculators have left and producers&rsquo; investors have not yet arrived. It is where many acquisitions happen: majors buy de-risked deposits from juniors that cannot fund construction themselves.')
exhibit('The Lassonde Curve: Typical Share-Price Path from Idea to Mine', 'img/lassonde.png', 'Conceptual, after Pierre Lassonde; Northwall Research')
h2('Construction Risk')
p('Capital cost overruns and delays are the norm rather than the exception: studies of large mining projects consistently find average overruns of 20% to 60%. Common causes are inflation in labour and materials, weaker ground or metallurgy than modelled, and scope changes. Ramp-ups that take longer than planned erode NPV because the most valuable early-year cash flows are pushed back.')
h2('ESG and the Social Licence to Operate')
side('A permit is a legal licence; the social licence is the ongoing acceptance of communities, Indigenous rights-holders and governments.')
p('A permit is a legal licence; the social licence is the ongoing acceptance of local communities, Indigenous rights-holders and governments. Losing it can stop a mine even after billions are spent. First Quantum&rsquo;s Cobre Panamá copper mine, one of the world&rsquo;s newest and largest, was ordered closed in late 2023 after nationwide protests and a Supreme Court ruling against its contract. Key ESG issues for mining investors:')
ul(['<b>Tailings.</b> Waste from processing is stored behind dams. The 2019 Brumadinho dam collapse in Brazil killed 270 people and led to the Global Industry Standard on Tailings Management (GISTM).',
    '<b>Water.</b> Use in arid regions (Chile, Peru, Australia), and acid rock drainage after closure.',
    '<b>Emissions.</b> Diesel haul fleets, grid power, smelting and, for steel, the coking coal and iron ore chain. Electrification and renewable power purchase agreements are now common.',
    '<b>Indigenous rights and community agreements.</b> Impact-benefit agreements, free, prior and informed consent, and local hiring.',
    '<b>Safety and labour.</b> Fatality rates, contractor safety, and artisanal mining in the supply chain (particularly DRC cobalt).'])
h2('Closure and Reclamation')
p('Mines must post closure plans and financial assurance (bonds, letters of credit) before construction. The present value of reclamation costs is a balance-sheet liability (asset retirement obligation) that analysts deduct in the NAV. Long-tail liabilities such as perpetual water treatment can make closure far more expensive than first estimated.')

# ---------------- 10. Fiscal & Jurisdiction ----------------
sec('Fiscal Regimes &amp; Jurisdictional Risk', 'fiscal',
    'Governments own most mineral rights and take their share through royalties, taxes and equity stakes. Jurisdiction is a direct input to valuation.')
side('Total government take ranges from about 35% of pre-tax cash flow in mining-friendly jurisdictions to over 60% elsewhere.')
p('Total government take typically ranges from about 35% of pre-tax cash flow in mining-friendly jurisdictions to over 60% where governments hold large free stakes or windfall taxes, and the rules can change mid-life. Jurisdiction therefore enters valuation directly, usually through a higher discount rate or a lower P/NAV multiple.')
h2('Royalty Types')
tbl(['Royalty', 'Basis', 'Who usually holds it', 'Comment'], [
    ['<b>Net smelter return (NSR)</b>', '% of revenue after smelting, refining and transport deductions', 'Governments, royalty companies, prospectors', 'The most common private royalty; simple and paid from first production'],
    ['<b>Gross revenue royalty (GRR)</b>', '% of gross revenue, no deductions', 'Governments, royalty companies', 'Highest burden on the operator'],
    ['<b>Net profits interest (NPI)</b>', '% of profit after operating and often capital costs are recovered', 'Former owners, partners', 'Pays nothing until costs are recovered; harder to audit'],
    ['<b>Sliding-scale royalty</b>', 'Rate rises with metal price', 'Governments, some private holders', 'Captures upside at high prices'],
    ['<b>Production-based</b> (per tonne)', 'Fixed amount per tonne or ounce', 'Some governments', 'Simple; can bite hard at low prices'],
], widths=['22%', '28%', '24%', '26%'])
p('A 2% NSR on a mine with US$1 billion of annual net smelter revenue costs the operator US$20 million a year, roughly 5% of its value at typical margins. Royalty companies buy these interests from prospectors and juniors, building diversified portfolios with no operating cost exposure.')
h2('Other Fiscal Levers')
ul(['<b>Corporate income tax.</b> Commonly 25% to 35%, plus provincial or state taxes in Canada, Australia and the US.',
    '<b>Mining taxes.</b> Profit-based mining taxes (for example Ontario&rsquo;s 10% and Quebec&rsquo;s 16% to 28%) on top of corporate tax.',
    '<b>State participation.</b> Free-carried or paid equity stakes: the DRC&rsquo;s mining code requires a 10% free-carried interest; Indonesia required foreign-owned miners to divest 51% to Indonesian interests, which is how the state became majority owner of Grasberg.',
    '<b>Export duties and bans.</b> Indonesia&rsquo;s ban on unprocessed nickel ore exports (2020) built a domestic processing industry; Zambia and others have used concentrate export duties.',
    '<b>Windfall taxes and royalty reforms.</b> Chile introduced a new copper royalty for large producers in 2023; Mali rewrote its mining code in 2023 with higher state stakes.',
    '<b>Withholding taxes and repatriation limits</b> affect how easily cash can be returned to shareholders.'])
h2('Resource Nationalism')
side('Resource nationalism tends to rise late in commodity upcycles, exactly when miners&rsquo; profits are largest.')
p('When metal prices rise, governments often seek a larger share of the windfall through tax increases, contract renegotiations, forced local ownership or, at the extreme, expropriation. Recent examples include the closure of Cobre Panamá (2023), contract disputes and detentions of mine staff in Mali and Burkina Faso, the nationalization of lithium in Mexico (2022), and Chile&rsquo;s state-led lithium strategy giving Codelco control of new Salar de Atacama projects. Resource nationalism tends to rise late in commodity upcycles, exactly when miners&rsquo; profits are largest.')
h2('Assessing Jurisdictional Risk')
p(f'Investors combine several inputs. The most widely cited is the Fraser Institute&rsquo;s Annual Survey of Mining Companies, which ranks jurisdictions on mineral potential and policy perception (Exhibit {nextex()}). In the 2025 survey, Nevada ranked first, with Ontario second and Saskatchewan third; China ranked last, behind Burkina Faso, Egypt, the Philippines and Mali.')
tbl(['Rank', 'Jurisdiction', 'Rank', 'Jurisdiction'], [
    ['1', '<b>Nevada</b>', '6', 'Western Australia'], ['2', '<b>Ontario</b> (15th in 2024)', '7', 'Botswana'], ['3', '<b>Saskatchewan</b> (7th in 2024)', '8', 'Norway'],
    ['4', 'South Australia', '9', 'Sweden'], ['5', 'Arizona', '10', 'Saudi Arabia']], widths=['10%', '40%', '10%', '40%'])
B[-1] = B[-1].replace('<table class="t ', '<div class="ext">Exhibit ' + str(nextex()) + ': Fraser Institute Investment Attractiveness Index, Top 10, 2025 Survey</div><table class="t ', 1) + '<div class="src">Source: Fraser Institute Annual Survey of Mining Companies 2025, via Mining Weekly (February 26, 2026)</div>'
EX[0] += 1
ul(['<b>Permitting timelines.</b> US federal permitting can take 7 to 10 years; Canadian timelines have also lengthened. Fast-track programs for critical minerals are shortening some.',
    '<b>Political and security risk.</b> Coups (Mali, Burkina Faso, Niger), conflict near operations, and sanctions (Russia).',
    '<b>Legal recourse.</b> Stabilization agreements and access to international arbitration offer some protection, but awards can take years to collect.'])
p('As a rule of thumb, sell-side analysts use 5% real discount rates for producing mines in top-tier jurisdictions and 7.5% to 10% for higher-risk countries, and apply lower P/NAV multiples to companies with assets in them.')
h2('Canada: A Top-Tier Mining Jurisdiction', 'canada')
side('Ontario ranked second in the world in the 2025 Fraser survey; Saskatchewan ranked third.')
p(f'Canada combines world-class geology, deep capital markets on the TSX and TSX-V, and stable fiscal terms. Ontario and Quebec host the Abitibi greenstone belt, one of the most productive gold belts in the world; Saskatchewan&rsquo;s Athabasca Basin hosts the highest-grade uranium mines; and British Columbia&rsquo;s Golden Triangle and the Labrador Trough round out a diverse map (Exhibit {nextex()}).')
exhibit('Canada&rsquo;s Main Mining Camps and Northwall Coverage', 'img/map_canada.png', 'Natural Earth (boundaries); company disclosures; Northwall Research', wide=True)

# ---------------- 11. Valuation ----------------
sec('Valuation', 'valuation',
    'Mines are depleting assets with finite lives, so the sector&rsquo;s primary valuation method is net asset value, cross-checked against cash-flow multiples.')
h2('Net Asset Value (NAV)')
side('Many analysts show NAV at a long-term deck, the futures strip and spot, because the answer changes dramatically.')
p('NAV is the sum of discounted cash flows from each mine over its life, adjusted for corporate items. Stocks are then compared on price-to-NAV (P/NAV). For each asset, analysts build a life-of-mine model: annual tonnes mined and milled, grade, recovery, payable metal, price, operating costs, royalties, capital and taxes. The after-tax free cash flow is discounted to today.')
ul(['<b>Discount rate.</b> Commonly 5% real for precious metals and 8% real for base metals and bulks, higher for riskier jurisdictions or development assets.',
    '<b>Price deck.</b> A long-term consensus price (typically well below spot in strong markets), the futures strip, or spot. Many analysts show NAV at all three, because the answer changes dramatically.',
    '<b>Corporate adjustments.</b> Add cash, investments and in-the-money options and warrants; subtract debt, the NPV of corporate G&amp;A, reclamation liabilities, hedge losses and stream or royalty obligations.',
    '<b>Risking.</b> Development projects are multiplied by a probability factor that rises as they advance (for example 25% at PEA, 50% at PFS, 75% at a construction decision, 100% in production). Resources outside the mine plan and exploration upside are added at a value per ounce or pound.'])
h3('Example: SampleCo gold NAV (illustrative, US$4,000/oz long-term gold)')
tbl(['Asset', 'Stage', 'Discount rate', 'NPV unrisked (US$M)', 'Risk factor', 'NPV risked (US$M)', 'Per share (US$)'], [
    ['Mine A, Ontario', 'Producing', '5%', '2,400', '100%', '2,400', '12.00'], ['Mine B, Mexico', 'Producing', '7.5%', '900', '100%', '900', '4.50'],
    ['Project C, Nevada', 'Pre-feasibility', '5%', '1,200', '50%', '600', '3.00'], ['Resources outside mine plans', '2 Moz at US$100/oz', '', '', '', '200', '1.00'],
    ('__b__', 'Total asset value', '', '', '', '', '4,100', '20.50'), ['Corporate G&amp;A (NPV)', '', '', '', '', '(250)', '(1.25)'],
    ['Reclamation obligations', '', '', '', '', '(150)', '(0.75)'], ['Cash', '', '', '', '', '500', '2.50'], ['Debt', '', '', '', '', '(800)', '(4.00)'],
    ('__b__', 'Net asset value', '', '', '', '', '3,400', '17.00'),
], widths=['23%', '15%', '10%', '14%', '10%', '14%', '14%'], num_cols=(2, 3, 4, 5, 6), cls='small')
exhibit('SampleCo NAV Bridge (US$ per Share)', 'img/nav.png', 'Northwall Research; illustrative')
p('With 200 million shares and a share price of US$20.40, SampleCo trades at 1.20x P/NAV. If the market valued Project C at full NPV once it is built, NAV would rise by US$3.00 per share, a re-rating that can be anticipated as the project advances.')
h2('Price-to-NAV (P/NAV)')
side('A stock trading well below peers on P/NAV may be cheap, or the market may doubt its reserves, costs, jurisdiction or capital allocation.')
p(f'P/NAV captures what the market will pay for a dollar of discounted cash flow. Typical historical ranges vary through the cycle (Exhibit {nextex()}). A stock trading well below peers may be cheap, or the market may doubt the reserves, the cost guidance, the jurisdiction or management&rsquo;s capital allocation. The analyst&rsquo;s job is to find out which.')
exhibit('Typical P/NAV Ranges by Company Type, with Northwall Coverage', 'img/pnav.png', 'Northwall Research; FNV and AGI at the October 26, 2026 close against Northwall NAV estimates')
tbl(['Company type', 'Typical P/NAV', 'Why'], [
    ['Royalty and streaming companies', '1.5x to 2.5x', 'No cost exposure, free optionality on exploration, diversified'],
    ['Senior gold producers', '1.0x to 1.5x', 'Liquidity, long reserve lives, index inclusion'],
    ['Diversified majors and senior base metals', '0.8x to 1.3x', 'Long-life assets, cyclical earnings'],
    ['Mid-tier and junior producers', '0.6x to 1.1x', 'Fewer assets, higher operating risk'],
    ['Developers', '0.3x to 0.7x', 'Financing, permitting and construction risk'],
    ['Explorers', 'Not meaningful', 'Valued on EV per resource unit or comparable discoveries'],
], widths=['38%', '18%', '44%'])
h2('Trading Multiples')
tbl(['Multiple', 'Formula', 'Best for', 'What to watch'], [
    ['<b>EV/EBITDA</b>', '(Market cap + net debt) / EBITDA', 'Majors and base-metal producers', 'Use forward EBITDA at a stated price deck; cyclical peaks flatter it'],
    ['<b>P/CF</b>', 'Share price / operating cash flow per share', 'Gold producers', 'Cash flow before working-capital changes'],
    ['<b>Free-cash-flow yield</b>', 'FCF / market cap', 'Mature producers returning capital', 'Sustaining vs. growth capex split'],
    ['<b>P/E</b>', 'Share price / EPS', 'Majors and royalty companies', 'Distorted by impairments and depreciation'],
    ['<b>EV per ounce or pound in the ground</b>', 'EV / attributable reserves and resources', 'Developers and explorers', 'Weight by category; adjust for grade, jurisdiction, metallurgy'],
    ['<b>EV per unit of annual production</b>', 'EV / attributable annual output', 'Producer screening', 'Ignores reserve life and costs'],
    ['<b>Dividend yield and total shareholder return</b>', 'Dividends and buybacks / market cap', 'Majors', 'Variable dividend policies tied to free cash flow'],
], widths=['24%', '27%', '22%', '27%'], cls='small')
p('<b>EV/EBITDA vs. P/CF.</b> As with oil and gas producers, enterprise-value metrics are &ldquo;debt neutral&rdquo; and allow a cleaner comparison between companies with different balance sheets.')
h2('Valuing Royalty and Streaming Companies')
p('Royalty companies are valued on P/NAV and P/CF, but at premiums to operators because they have no exposure to operating or capital cost inflation, carry little debt, and receive exploration upside on the land under their royalties for free. Key metrics are gold-equivalent ounces (GEOs) sold, cash margin per GEO (often over 80%), portfolio diversification and the share of NAV from producing assets.')
box('Northwall coverage: Franco-Nevada (NYSE/TSX: FNV)',
    '<p>Franco-Nevada earned a 91% adjusted EBITDA margin in H1 2026 with no asset above 10% of revenue and no debt. The market pays for that quality: at US$230.76 the shares trade at 1.66x our NAV per share of US$138.88, inside the 1.5x to 2.5x range for royalty companies.</p><p>Our US$250.00 target blends 2.0x NAV with 25x 2027E cash flow per share. The 9.1% implied all-in return sits below our 15% Buy hurdle, so we rate the shares Hold: a premium franchise at a premium price.</p>')
h2('Valuing Developers and Explorers')
ul(['<b>Developers</b> are valued on a risked NAV that rises as milestones are met (PFS, FS, permits, financing, construction). The usual question is what the stock is worth once built, discounted back for time and risk.',
    '<b>Explorers</b> have no cash flow. They are valued on EV per resource ounce or pound against comparable companies, adjusted for grade, depth, metallurgy and jurisdiction, or on the market&rsquo;s expectation of a discovery. Drill results, especially grade-thickness from step-out holes, drive the share price.',
    '<b>Takeover benchmarks.</b> Recent acquisition prices per ounce or per pound set reference values for similar deposits.'])

# ---------------- 12. Investing ----------------
sec('Investing: Commodities, Equities and Credit', 'investing',
    'Investors can own metal directly or indirectly through mining equities and bonds. Equities add operating leverage and growth, and with them operating, jurisdictional, cost and capital-allocation risk.')
h2('Direct Commodity Exposure')
ul(['<b>Physical metal and physically backed ETFs.</b> Common for gold, silver, platinum and, more recently, uranium (physical trusts). Return equals the price change less storage and management fees.',
    '<b>Futures.</b> Return = spot return + collateral return (interest on cash margin) + roll return. In contango the roll return is negative; in backwardation it is positive.',
    '<b>Commodity indices and broad ETFs.</b> Diversified, but base-metal weights are small and roll costs can erode returns.'])
h2('Mining Equities')
tbl(['Tier', 'Typical profile', 'Examples', 'Investor appeal'], [
    ['<b>Diversified majors</b>', 'Multiple commodities and continents; iron ore, copper, coal, aluminum', 'BHP, Rio Tinto, Glencore, Vale, Anglo American', 'Dividends, balance-sheet strength, lower volatility'],
    ['<b>Senior producers</b>', 'One main commodity, several mines, typically over 1 Moz gold or 500 kt copper a year', 'Newmont, Agnico Eagle, Barrick, Freeport-McMoRan, Southern Copper', 'Liquid leverage to one metal'],
    ['<b>Royalty and streaming</b>', 'Portfolios of royalties and streams, no operations', 'Franco-Nevada, Wheaton Precious Metals, Royal Gold', 'Margin stability, optionality'],
    ['<b>Mid-tier and junior producers</b>', 'One to three mines', 'Many TSX- and ASX-listed names, including Alamos Gold', 'High leverage to price and execution'],
    ['<b>Developers</b>', 'Building or financing a first mine', '', 'Re-rating as risk falls; financing dilution risk'],
    ['<b>Explorers</b>', 'Drilling, no revenue', 'Thousands on the TSX-V and ASX', 'Discovery upside; most never become mines'],
], widths=['20%', '30%', '28%', '22%'])
p('Gold equities typically move 1.5 to 3 times the gold price in either direction. The correlation between a miner&rsquo;s shares and its metal varies with hedging, by-products, cost inflation, jurisdiction events and company-specific execution, and juniors often trade more on drill results and financing than on the metal price.')
h2('How Mines Are Financed')
tbl(['Source', 'Used by', 'Trade-off'], [
    ['Equity issues and private placements', 'Explorers, developers, all producers', 'Dilution; Canadian flow-through shares give investors tax deductions for exploration spending'],
    ['Project finance debt', 'Developers with a feasibility study', 'Requires hedging, completion tests and cost-overrun facilities'],
    ['Corporate bonds and revolving credit', 'Producers', 'Cheapest capital; covenants and refinancing risk'],
    ['Streams and royalties', 'Developers and producers', 'No dilution, but a permanent claim on future revenue'],
    ['Offtake-linked financing and strategic investors', 'Developers, especially battery metals', 'Often from traders, smelters, automakers or Chinese and Japanese buyers'],
    ['Government and export-credit financing', 'Critical-minerals projects', 'Low cost but slow, with conditions on processing location and offtake'],
], widths=['34%', '28%', '38%'])
h2('Mining Credit')
side('Rating agencies stress-test credit metrics at their own conservative price decks, often well below spot.')
p('Credit investors focus on a miner&rsquo;s ability to service debt through the bottom of the commodity cycle, not on upside. Growth spending, large acquisitions and shareholder returns funded by debt are generally viewed unfavourably by bondholders. Common credit metrics:')
ul(['Net debt / EBITDA (investment-grade miners usually target below 1.0x to 1.5x through the cycle)', 'EBITDA / interest', 'Funds from operations / debt',
    'Debt / proven and probable reserves (per ounce or pound)', 'Reserve life relative to debt maturity', 'Asset and commodity diversification, and position on the cost curve'])
p('Most majors are rated investment grade (A to BBB range); mid-tier producers and developers with project debt are typically high yield. Rating agencies stress-test credit metrics at their own conservative price decks, often well below spot.')
h2('Common Pitfalls')
ul(['<b>Extrapolating spot prices.</b> NAVs at spot can be 50% or more above NAVs at long-term prices in a strong market.',
    '<b>Ignoring dilution.</b> Share counts at juniors and developers often double before first production.',
    '<b>Trusting first-year guidance.</b> New mines frequently miss initial production and cost targets during ramp-up.',
    '<b>Overlooking taxes and royalties that rise with price,</b> which mute operating leverage.'])

# ---------------- Appendix I ----------------
sec('Appendix I: Sample Drill-Results Press Release', 'appendix1', newpage=True, lede=
    'The release below is fictional, written to show the language and data of a typical junior gold explorer&rsquo;s announcement. The company, project and figures are invented.')
raw('''<div class="release"><div class="rh1">NORTHFOLD MINERALS CORP. INTERSECTS 18.4 METRES OF 6.2 G/T GOLD, EXTENDS RAVEN ZONE 300 METRES DOWN-PLUNGE</div>
<div class="rsub">Fictional example &middot; Timmins, Ontario</div>
<p>Northfold Minerals Corp. (&ldquo;Northfold&rdquo; or the &ldquo;Company&rdquo;) is pleased to report results from 12 holes (6,850 metres) of its 2026 drill program at the 100%-owned Raven Gold Project, located 25 km from existing mills and highway access.</p>
<p><b>Highlights</b></p><ul><li>RV-26-041: <b>18.4 m of 6.2 g/t Au</b> from 412 m, including <b>4.1 m of 21.7 g/t Au</b></li><li>RV-26-044: 9.6 m of 4.8 g/t Au from 455 m, a 300 m step-out down-plunge of the current resource</li>
<li>RV-26-038: 22.0 m of 1.9 g/t Au from 120 m, within the planned open-pit shell</li><li>Mineralization remains open at depth and along strike</li></ul>'''
    + table(['Hole', 'From (m)', 'To (m)', 'Length (m)', 'Au (g/t)'], [['RV-26-041', '412.0', '430.4', '18.4', '6.2'], ['including', '418.2', '422.3', '4.1', '21.7'], ['RV-26-044', '455.0', '464.6', '9.6', '4.8'], ['RV-26-038', '120.0', '142.0', '22.0', '1.9']], widths=['28%', '18%', '18%', '18%', '18%'], num_cols=(1, 2, 3, 4)) +
    '''<p style="margin-top:6px">Reported intervals are core lengths; true widths are estimated at 70% to 80% of core length. Assays are uncapped. The current Mineral Resource (2025) is 1.4 Moz Indicated at 2.1 g/t and 0.9 Moz Inferred at 2.6 g/t Au. Northfold plans an updated resource and a Preliminary Economic Assessment in the first half of 2027. The Company has C$18 million in cash. Technical information has been reviewed by a Qualified Person as defined by NI 43-101.</p></div>''')
h2('Key Take-Aways and Follow-Up Questions')
for head, take, follow in [
    ('&ldquo;18.4 metres of 6.2 g/t gold&rdquo;', 'Grade &times; width (gram-metres) is the quick measure of a hole&rsquo;s quality: 18.4 &times; 6.2 = 114 g&middot;m, well above the 30 to 50 g&middot;m an underground deposit usually needs to be interesting. It is also well above the 2.1 g/t resource grade.',
     'How much of the grade comes from the 4.1 m high-grade core? Without it, the remaining 14.3 m average about 1.8 g/t. Are assays capped in the resource model? High-grade gold is often &ldquo;nuggety,&rdquo; and capping can cut resource grade by 10% to 30%.'),
    ('&ldquo;Extends Raven Zone 300 metres down-plunge&rdquo;', 'Step-out holes that extend mineralization grow the resource; infill holes inside it raise confidence but add few new ounces. A 300 m extension can add significant ounces if continuity holds.',
     'Is one hole enough to infer continuity over 300 m? What is the drill spacing in the current Indicated resource? How deep is 455 m for an open pit versus an underground mine, and what does that do to costs?'),
    ('&ldquo;True widths estimated at 70% to 80% of core length&rdquo;', 'Core length overstates the true thickness of an inclined zone. At 75%, the 18.4 m interval is about 13.8 m true width, still a robust, mineable thickness.',
     'Why are true widths estimated rather than known? Releases that omit true width deserve extra scrutiny.'),
    ('&ldquo;1.4 Moz Indicated at 2.1 g/t and 0.9 Moz Inferred at 2.6 g/t&rdquo;', 'About 2.3 Moz in total, 61% in the higher-confidence Indicated category. The Inferred portion cannot be used in a PFS until upgraded.',
     'What gold price and cut-off grade underpin the resource? Is it constrained by a pit shell and underground stope shapes (&ldquo;reasonable prospects&rdquo;)? What are the metallurgical recoveries? A resource with 95% recovery is worth far more than one at 80%.'),
    ('&ldquo;25 km from existing mills and highway access&rdquo;', 'Proximity to infrastructure lowers capital and could allow ore to be toll-milled, or the project to be sold to a nearby producer. It makes Northfold a plausible takeover target.',
     'Who owns the nearby mills, and do they have spare capacity? What is the permitting path and the status of agreements with local First Nations?'),
    ('&ldquo;C$18 million in cash&rdquo;', 'Funds the next 12 to 18 months of drilling and studies, but a PEA, then a PFS, will require more capital.',
     'What is the burn rate? How many shares and warrants are outstanding, and at what prices could financing dilute existing holders?')]:
    raw(f'<div class="qa"><div class="qh">{head}</div><p><b>Take-away.</b> {take}</p><p><b>Follow-up.</b> {follow}</p></div>')
p('<b>Valuation check.</b> If Northfold trades at an enterprise value of C$150 million, the market is paying about C$65 per resource ounce (C$150M / 2.3 Moz). Compare that with peers at a similar stage, grade and jurisdiction, and with recent takeover prices per ounce in the region.')

# ---------------- Appendix II: Glossary ----------------
GL = [('Acid rock drainage (ARD)', 'Acidic, metal-laden water formed when sulphide minerals in waste rock or tailings oxidize; a major closure liability'), ('All-in cost (AIC)', 'AISC plus growth capital and non-sustaining exploration'),
      ('All-in sustaining cost (AISC)', 'Cash costs plus sustaining capital, exploration, corporate G&amp;A and reclamation accretion, less by-product credits, per ounce sold'), ('Assay', 'Laboratory analysis that measures the metal content of a rock sample'),
      ('Autoclave', 'A pressure vessel used to oxidize refractory ores or leach laterites at high temperature and pressure'), ('Backfill', 'Waste rock, tailings or cement paste placed in mined-out underground voids for support'),
      ('Ball mill', 'Rotating cylinder with steel balls that grinds ore to a fine powder'), ('Bauxite', 'The ore of aluminum'), ('Bench', 'A horizontal step in an open pit, typically 10 to 15 m high'),
      ('Beneficiation', 'Any process that upgrades ore before smelting or sale'), ('Blister copper', 'Impure (about 98% to 99%) copper produced by a smelter, before refining'), ('Block cave', 'Bulk underground method in which ore collapses under gravity after being undercut'),
      ('Brownfield', 'Exploration or expansion at or near an existing mine'), ('By-product', 'A metal recovered incidentally to the main product; its revenue is usually credited against costs'),
      ('C1 cash cost', 'Direct cash cost per unit of payable metal, net of by-product credits'), ('Capping (top-cutting)', 'Limiting extreme assay values in a resource estimate to avoid overstating grade'),
      ('Cathode', 'Refined metal sheet (for copper, 99.99% pure) produced by electrolysis'), ('CIL / CIP', 'Carbon-in-leach / carbon-in-pulp: gold recovery onto activated carbon during or after cyanide leaching'),
      ('Collar', 'The top of a drill hole'), ('Comminution', 'Crushing and grinding of ore'), ('Competent Person / Qualified Person', 'Professional who takes responsibility for resource and reserve estimates under JORC, NI 43-101 or S-K 1300'),
      ('Concentrate', 'Upgraded product of a mill (for example 25% to 35% Cu), sold to a smelter'), ('Contained metal', 'Tonnes &times; grade, before recovery losses'),
      ('Co-product', 'A metal important enough that costs are allocated between it and the main product'), ('Core', 'Cylindrical rock sample from diamond drilling'), ('Cut-off grade', 'Minimum grade at which material is classified as ore'),
      ('Cyanidation', 'Leaching gold and silver with dilute cyanide solution'), ('Decline (ramp)', 'Sloped tunnel providing vehicle access to an underground mine'), ('Diamond drilling', 'Drilling with a diamond-studded bit that recovers solid core'),
      ('Dilution', 'Waste mixed with ore during mining, lowering grade'), ('Doré', 'Unrefined gold-silver bars poured at a mine site'), ('Drawpoint', 'Opening from which caved ore is loaded in a block or sublevel cave'),
      ('Electrowinning (EW)', 'Recovering metal from solution by electrolysis'), ('Epithermal', 'Shallow, hot-spring-related gold and silver deposits'), ('Exploration target', 'Conceptual estimate of a range of tonnes and grade, not a resource'),
      ('Feasibility study (FS)', 'Detailed engineering study (&plusmn;10% to 15% accuracy) used for construction and financing decisions'), ('Flotation', 'Separation of sulphide minerals into a froth concentrate using reagents and air'),
      ('Flow-through shares', 'Canadian shares that pass exploration tax deductions to investors'), ('Free-carried interest', 'A stake (often held by a government) that does not contribute to capital costs'),
      ('Free-milling', 'Ore from which gold is easily recovered by cyanidation'), ('Gangue', 'Worthless minerals in ore'), ('Gold equivalent (AuEq)', 'Multi-metal grade or production expressed as gold at stated prices and recoveries'),
      ('Grade', 'Concentration of metal in rock (g/t or %)'), ('Gram-metre (g&middot;m)', 'Grade &times; interval length; a quick measure of a drill intercept&rsquo;s quality'), ('Greenfield', 'Exploration in a new area with no existing mine'),
      ('Head grade', 'Grade of ore fed to the mill'), ('Heap leach', 'Leaching crushed ore stacked on lined pads'), ('Hanging wall / footwall', 'Rock above / below an inclined orebody'), ('HPAL', 'High-pressure acid leach, used for nickel laterites'),
      ('In-situ recovery (ISR)', 'Extracting metal by circulating solution through the orebody without moving rock'), ('Indicated resource', 'Resource with enough drilling to assume geological and grade continuity'),
      ('Inferred resource', 'Resource with limited drilling; continuity assumed but not verified'), ('Infill drilling', 'Drilling between existing holes to increase confidence'), ('Intercept', 'A drill-hole interval reported with its length and grade'),
      ('Laterite', 'Weathered, near-surface deposit enriched in nickel, cobalt or aluminum'), ('LBMA', 'London Bullion Market Association; sets the benchmark gold and silver prices'), ('LCE', 'Lithium carbonate equivalent'),
      ('Leach', 'Dissolve metal from ore using a chemical solution'), ('Life of mine (LOM)', 'Expected remaining years of production under the mine plan'), ('LME', 'London Metal Exchange, the benchmark for base metals'),
      ('Lassonde curve', 'Typical share-price path of a mining company from discovery to production'), ('Measured resource', 'Highest-confidence resource category, from close-spaced drilling'),
      ('Metallurgy', 'The science of extracting metal from ore; also a deposit&rsquo;s processing characteristics'), ('Mill', 'Processing plant; also the grinding equipment within it'),
      ('Modifying factors', 'Mining, processing, economic, legal, environmental and social factors used to convert resources to reserves'), ('Net smelter return (NSR)', 'Revenue after smelting, refining and transport deductions; also a royalty on that revenue'),
      ('Net profits interest (NPI)', 'Royalty paid on profit after costs are recovered'), ('NI 43-101', 'Canadian disclosure standard for mineral projects'), ('Offtake', 'Agreement to buy a mine&rsquo;s future production'),
      ('Open pit', 'Surface mine excavated in benches'), ('Ore', 'Material that can be mined and processed at a profit'), ('Orebody', 'A continuous, mineable concentration of ore'),
      ('Orogenic gold', 'Gold deposits formed in mountain-building belts, often in quartz veins'), ('Overburden', 'Soil and rock covering an orebody'), ('Payable metal', 'Share of contained metal in concentrate that the smelter pays for'),
      ('Pegmatite', 'Coarse-grained igneous rock; the host of hard-rock lithium'), ('Porphyry', 'Large, low-grade copper-gold-molybdenum deposit associated with intrusions'),
      ('Preliminary economic assessment (PEA)', 'Early economic study that may include Inferred resources'), ('Pre-feasibility study (PFS)', 'Intermediate study (&plusmn;25% accuracy) selecting the development option and declaring reserves'),
      ('Probable reserve', 'Economically mineable part of Indicated (and sometimes Measured) resources'), ('Proven reserve', 'Economically mineable part of Measured resources'),
      ('Provisional pricing', 'Invoicing concentrate at an estimated price, finalized after the quotational period'), ('Quotational period (QP)', 'Period whose average price sets the final invoice (for example M+1)'),
      ('Reclamation', 'Rehabilitating mined land after closure'), ('Recovery', 'Share of metal in the feed recovered to final product'), ('Refractory', 'Ore that needs pre-treatment (roasting, pressure oxidation, bio-oxidation) before gold can be leached'),
      ('Reserve', 'Economically mineable part of a resource, after modifying factors'), ('Resource', 'Concentration with reasonable prospects for eventual economic extraction'), ('Royalty', 'Right to a share of a mine&rsquo;s revenue or profit'),
      ('Run-of-mine (ROM)', 'Ore as delivered from the mine, before crushing'), ('SAG mill', 'Semi-autogenous grinding mill that uses ore plus some steel balls as the grinding medium'), ('Shaft', 'Vertical opening used to hoist ore and move people and materials'),
      ('Smelter', 'Plant that melts concentrate to produce impure metal'), ('Spodumene (SC6)', 'Lithium mineral; SC6 is concentrate at about 6% Li<sub>2</sub>O'), ('Step-out', 'Drill hole testing for extensions beyond known mineralization'),
      ('Stope', 'Underground excavation from which ore is mined'), ('Stream', 'Upfront payment in exchange for the right to buy a share of production at a low fixed price'), ('Strip ratio', 'Tonnes of waste moved per tonne of ore in an open pit'),
      ('Sustaining capital', 'Capital needed to maintain current production'), ('SX-EW', 'Solvent extraction and electrowinning; produces copper cathode at the mine'), ('Tailings', 'Finely ground waste left after processing, stored in tailings facilities'),
      ('Throughput', 'Tonnes of ore processed per period'), ('Toll milling', 'Processing ore at another company&rsquo;s mill for a fee'), ('Treatment and refining charges (TC/RC)', 'Fees paid by miners to smelters and refiners'),
      ('True width', 'Actual thickness of a mineralized zone, versus drilled length'), ('U<sub>3</sub>O<sub>8</sub>', 'Triuranium octoxide, the traded form of uranium concentrate (&ldquo;yellowcake&rdquo;)'),
      ('VMS', 'Volcanogenic massive sulphide deposit, rich in copper, zinc, lead, silver and gold'), ('Waste', 'Rock below cut-off grade that must be moved to reach ore')]
GL.sort(key=lambda x: x[0].lower().replace('&', ''))
sec('Appendix II: Glossary of Terms', 'glossary', newpage=True)
raw('<div class="gloss">' + ''.join(f'<div class="g"><b>{a}</b> {b}.</div>' for a, b in GL) + '</div>')

# ---------------- Sources ----------------
sec('Bibliography', 'sources', newpage=True, lede='Market prices and production figures were retrieved in October 2026. Structural content (geology, methods, reporting codes, valuation) reflects standard industry practice; worked examples, SampleCo and Northfold are illustrative.')
ul(['USGS, <i>Mineral Commodity Summaries 2026</i> (gold and copper chapters), via StatRanker and Critical Minerals News.',
    'World Gold Council, <i>Gold Demand Trends Q4 and Full Year 2025</i>, Table 1, and press release, January 29, 2026.',
    'Fraser Institute, <i>Annual Survey of Mining Companies 2025</i>, via Mining Weekly, February 26, 2026.',
    'LBMA gold price annual averages; MetalCharts, 2025 gold and copper price history.',
    'Farmonaut, citing Westmetall and Reuters (LME copper and GFEX lithium carbonate, October 2026); Reporte Minero (LME nickel, October 2026); Mining Reporters (LME aluminum, July 2026); Host Rock weekly metals rundown (silver and platinum, January 2026).',
    'Northwall Research market tape (Yahoo Finance delayed quotes), October 27, 2026 close.',
    'CIM Definition Standards for Mineral Resources and Mineral Reserves; JORC Code (2012); SEC Regulation S-K Subpart 1300.',
    'World Gold Council, Guidance Note on Non-GAAP Metrics (AISC and AIC), 2013; Global Industry Standard on Tailings Management (GISTM), 2020.',
    'Natural Earth public-domain boundaries, via the world-atlas (ISC) and sane-topojson (MIT) packages.',
    'Northwall Research company reports and models: Alamos Gold (AGI) and Franco-Nevada (FNV), October 27, 2026.'])

# ---------------- Disclosures ----------------
raw('<div style="height:14pt"></div>'); sec('Important Disclosures', 'disclosures')
raw('''<div class="disc"><p><b>About this report.</b> This primer is educational research published by Northwall Research. It describes how metals and mining companies are analysed and valued. It is not a recommendation to buy or sell any security, and it is not personalized investment advice.</p>
<p><b>Companies under coverage.</b> References to Alamos Gold Inc. (Buy, US$39.00 target) and Franco-Nevada Corporation (Hold, US$250.00 target) reflect Northwall Research&rsquo;s published ratings as of October 27, 2026. See the company reports for full methodology, risks and disclosures. Other companies are named for illustration only and are not covered.</p>
<p><b>Rating definitions.</b> Buy: expected 12-month total return (price appreciation plus dividends) above 15%. Hold: expected total return between 0% and 15%. Sell: expected total return below 0%. Price targets are 12-month.</p>
<p><b>Sources.</b> Facts are attributed to their sources in the text and the bibliography. Estimates, illustrations and opinions are Northwall Research&rsquo;s own. Market data are as at the dates stated and will change.</p>
<p><b>General disclaimer.</b> The information herein is believed to be reliable but is not guaranteed as to accuracy or completeness. Opinions and estimates are as of the date of this report and are subject to change without notice. Past performance is not indicative of future results. Forward-looking statements are inherently uncertain. Northwall Research is not a registered dealer or adviser.</p>
<p><b>Analyst certification.</b> The views expressed in this report accurately reflect the analyst&rsquo;s personal views. No part of the analyst&rsquo;s compensation was, is or will be related to the specific views contained in this report. Basel Al-Ghousein is a Level II candidate for the CFA designation.</p>
<p>&copy; 2026 Northwall Research. All rights reserved.</p></div>''')
