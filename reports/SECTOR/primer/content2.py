from kit import *

# ---------------- 6. The Commodities ----------------
sec('The Commodities', 'commodities',
    'Each metal has its own supply base, demand drivers and price mechanism. Copper and gold dominate mining-equity market value; iron ore drives the diversified majors&rsquo; earnings.')
side('Lithium, nickel and uranium are smaller markets but far more volatile.')
p('Copper and gold dominate mining-equity market capitalization; iron ore drives the diversified majors&rsquo; earnings; lithium, nickel and uranium are smaller but far more volatile.')
h2('Snapshot')
tbl(['Commodity', 'Price quoted in', 'Main benchmark', 'Largest mining countries', 'Main demand'], [
    ['<b>Copper</b>', 'US$/t (LME) or US$/lb (COMEX)', 'LME Grade A cash', 'Chile, DR Congo, Peru', 'Power grids, buildings, vehicles, electronics, data centres'],
    ['<b>Gold</b>', 'US$/oz', 'LBMA Gold Price, COMEX futures', 'China, Russia, Australia, Canada', 'Jewellery, bars and ETFs, central banks'],
    ['<b>Silver</b>', 'US$/oz', 'LBMA Silver Price, COMEX', 'Mexico, China, Peru', 'Solar panels, electronics, jewellery, investment'],
    ['<b>Iron ore</b>', 'US$ per dry tonne', '62% Fe fines CFR China (SGX, Dalian)', 'Australia, Brazil', 'Steel'],
    ['<b>Metallurgical coal</b>', 'US$/t', 'Premium hard coking coal FOB Australia', 'Australia, Canada, US, Mongolia', 'Steel (blast furnaces)'],
    ['<b>Nickel</b>', 'US$/t', 'LME', 'Indonesia, Philippines', 'Stainless steel, batteries'],
    ['<b>Zinc and lead</b>', 'US$/t', 'LME', 'China, Australia, Peru', 'Galvanized steel (zinc); lead-acid batteries (lead)'],
    ['<b>Aluminum</b>', 'US$/t', 'LME plus regional premiums', 'China, India, Russia', 'Transport, packaging, construction, power lines'],
    ['<b>Lithium</b>', 'CNY/t or US$/t of carbonate or hydroxide', 'GFEX futures, assessed prices', 'Australia, Chile, China, Argentina, Zimbabwe', 'EV and storage batteries'],
    ['<b>Uranium</b>', 'US$/lb U<sub>3</sub>O<sub>8</sub>', 'Spot and long-term price assessments', 'Kazakhstan, Canada, Namibia', 'Nuclear power'],
    ['<b>PGMs</b>', 'US$/oz', 'NYMEX, LPPM', 'South Africa, Russia', 'Autocatalysts, jewellery, industry'],
], widths=['13%', '18%', '22%', '21%', '26%'], cls='small')
h2('Where Prices Stand')
side('Prices move daily: check a live quote before using any of these in a model.')
tbl(['Commodity', 'Price', 'Date and source'], [
    ['Gold', 'US$4,076/oz', 'October 27, 2026 close; Northwall market tape (Yahoo Finance, COMEX front month)'],
    ['Silver', 'US$54.56/oz', 'October 27, 2026 close; Northwall market tape'],
    ['Copper', 'US$6.66/lb (about US$14,680/t)', 'October 27, 2026 close, COMEX; LME cash US$14,751/t on October 14 (Farmonaut, citing Westmetall)'],
    ['Platinum', 'US$1,543/oz', 'October 27, 2026 close; Northwall market tape'],
    ['Palladium', 'US$1,034/oz', 'October 27, 2026 close; Northwall market tape'],
    ['Nickel', 'About US$15,830/t', 'LME, October 2026 (Reporte Minero)'],
    ['Aluminum', 'About US$3,231/t', 'LME, end of July 2026 (Mining Reporters)'],
    ['Lithium carbonate', '104,740 yuan/t (about US$15,650)', 'GFEX, October 12, 2026, roughly half its May 13 peak (Farmonaut, citing Reuters)'],
], widths=['18%', '28%', '54%'])
exhibit('Gold and Copper Prices, Annual Averages 2010–2025 and Spot', 'img/prices.png',
        'LBMA (gold annual averages; 2025 per World Gold Council); LME (copper annual averages; 2025 from MetalCharts COMEX data); Northwall market tape (October 27, 2026 spot)', wide=True)

h2('Copper', 'copper')
side('Copper is nicknamed &ldquo;Dr. Copper&rdquo; for its link to industrial activity.')
p('Copper is the bellwether of the metals complex, nicknamed &ldquo;Dr. Copper&rdquo; for its link to industrial activity. About 23 Mt was mined in 2025, flat on 2024 despite strong demand, because of falling ore grades, mine closures and disruptions such as the September 2025 incident at Grasberg in Indonesia. China mines only about 8% of supply but refines roughly 14 Mt a year, more than half the world&rsquo;s refined copper.')
exhibit('Copper Mine Production by Country, 2025 Estimates (kt of Contained Copper)', 'img/map_copper.png',
        'USGS Mineral Commodity Summaries 2026, via Critical Minerals News (world total about 23,000 kt); Natural Earth')
ul(['<b>Demand.</b> Roughly two-thirds of copper goes into electrical uses. Electrification (grids, EVs at three to four times the copper of a combustion car, renewables) and data-centre power are the growth themes on top of China&rsquo;s construction cycle.',
    '<b>Supply.</b> New mines take 15 years or more from discovery to production, average grades in Chile have fallen for two decades, and much new supply comes from higher-risk jurisdictions such as the DRC. This is why many analysts expect structural deficits.',
    '<b>By-products.</b> Gold, silver, molybdenum and cobalt credits can cut a copper mine&rsquo;s net cash cost substantially.'])

h2('Gold', 'gold')
side('Above-ground gold stocks are about 60 times annual mine supply, so investment demand, not mine output, sets the price.')
p('Gold is a monetary asset as much as a commodity. Above-ground stocks are about 60 times annual mine supply, so the price is set by investment demand rather than mine output. Mine production of about 3,670 t in 2025 (World Gold Council basis; USGS estimates about 3,300 t) has been broadly flat for a decade, topped up by about 1,400 t of recycling.')
p(f'Total demand reached a record 5,002 t in 2025 (Exhibit {nextex()}). Investment demand almost doubled to 2,175 t as ETFs added 801 t, while jewellery fell 19% in tonnes as prices rose. The LBMA price averaged US$3,432/oz, up 44% on 2024, and gold passed US$5,000/oz for the first time in January 2026.')
exhibit('Gold Demand by Sector, 2024 vs. 2025 (Tonnes)', 'img/gold_demand.png', 'World Gold Council, Gold Demand Trends Q4 and Full Year 2025 (Table 1)')
tbl(['Supply and demand (t)', '2024', '2025', 'Change'], [
    ['Mine production', '3,650', '3,672', '+1%'], ['Recycled gold', '1,365', '1,404', '+3%'], ['Net producer hedging', '(54)', '(74)', ''],
    ('__b__', 'Total supply', '4,962', '5,002', '+1%'),
    ['Jewellery fabrication', '2,027', '1,638', '&minus;19%'], ['Technology', '326', '323', '&minus;1%'], ['Bar and coin', '1,188', '1,374', '+16%'],
    ['ETFs and similar products', '(3)', '801', 'n/m'], ['Central banks and other institutions', '1,092', '863', '&minus;21%'], ['OTC and other', '331', '3', ''],
    ('__b__', 'Total demand', '4,962', '5,002', '+1%'), ('__b__', 'LBMA average price (US$/oz)', '2,386', '3,432', '+44%'),
], widths=['46%', '18%', '18%', '18%'], num_cols=(1, 2, 3))
exhibit('Gold Mine Production by Country, 2025 Estimates (Tonnes)', 'img/map_gold.png',
        'USGS Mineral Commodity Summaries 2026 (world total about 3,300 t), via StatRanker; Natural Earth')
ul(['<b>Price drivers.</b> Real interest rates (gold pays no yield), the US dollar, central-bank buying (around 1,000 t a year from 2022 to 2024 and 863 t in 2025, led by emerging-market banks diversifying away from dollar reserves), ETF flows and geopolitical risk.',
    '<b>Equity leverage.</b> A miner with an AISC of US$1,800/oz earns a US$2,276/oz margin at US$4,076 gold. A 10% rise in the gold price lifts that margin by about 18%, which is why gold equities typically move 1.5 to 3 times the metal.'])

h2('Silver')
p('About 70% of silver is mined as a by-product of lead-zinc, copper and gold mines, so supply barely responds to price. Industrial uses, led by solar panels, now take over half of demand. Silver is far more volatile than gold: it set records above US$100/oz in late January 2026 (Host Rock weekly rundown) before falling back to about US$55/oz in October. Investors watch the gold-to-silver ratio, historically 50 to 80, as a relative-value signal; it stood near 75 at the end of October.')
h2('Iron Ore and Metallurgical Coal')
side('China imports about 70% of seaborne iron ore, so Chinese steel output sets the price.')
p('Iron ore is the largest mined commodity by tonnage and the biggest earnings driver for BHP, Rio Tinto, Vale and Fortescue. China imports about 70% of seaborne ore, so Chinese steel output, particularly for property construction, sets the price.')
ul(['<b>Pricing.</b> The 62% Fe fines index (CFR China) is the benchmark. Higher-grade ore (65% Fe, pellets) earns a premium because it cuts coke use and emissions; lower-grade and high-impurity ore (alumina, silica, phosphorus) trades at a discount.',
    '<b>Supply.</b> Australia&rsquo;s Pilbara and Brazil&rsquo;s Carajás dominate with very low costs (under US$25/t C1 for the best mines). Simandou in Guinea, led by Rio Tinto and Chinese partners, began its ramp-up in late 2025 and is the largest new source of high-grade supply.',
    '<b>Met coal.</b> Coking coal makes the coke that reduces iron ore in blast furnaces. Premium hard coking coal from Queensland is the price benchmark; Elk Valley Resources (formerly Teck&rsquo;s coal business, now majority-owned by Glencore) is the major Canadian supplier.'])
h2('Nickel')
p('Indonesia now supplies over half the world&rsquo;s nickel, using Chinese-built nickel pig iron plants and HPAL refineries to process laterite ore. The surge in low-cost supply drove prices down and forced closures of higher-cost Western sulphide mines, including BHP&rsquo;s Nickel West in 2024. Investors distinguish Class 1 nickel (high purity, LME-deliverable, battery-grade) from Class 2 (ferronickel and NPI for stainless steel). Indonesian ore-mining quotas are now the single biggest swing factor for price.')
h2('Zinc and Lead')
p('Zinc and lead usually occur together in the same deposits. Zinc&rsquo;s main use is galvanizing steel against corrosion; lead&rsquo;s is lead-acid batteries, much of which is recycled. Zinc miners are unusually sensitive to treatment charges because zinc concentrate pays only about 85% of contained metal.')
h2('Aluminum')
p('Aluminum is made in three steps: bauxite is mined, refined into alumina (the Bayer process), then smelted into metal by electrolysis, which uses about 14 to 15 MWh of power per tonne. Power cost, not ore, sets the cost curve. China produces about 60% of global aluminum and has capped domestic capacity at about 45 Mt a year, which limits future supply growth.')
h2('Lithium and Battery Metals')
side('Few metals show how fast high prices create their own supply.')
p('Lithium is sold as spodumene concentrate (about 6% Li<sub>2</sub>O, &ldquo;SC6&rdquo;) from hard-rock mines, or as lithium carbonate and hydroxide from brines and converters. Prices are typically quoted per tonne of lithium carbonate equivalent (LCE).')
ul(['<b>Boom and bust.</b> Prices rose about tenfold in 2021 to 2022 on EV demand, collapsed by more than 80% by 2025 as Australian, African and Chinese supply surged, then recovered in 2026. Few metals show how fast high prices create their own supply.',
    '<b>Chemistry matters.</b> LFP (lithium iron phosphate) batteries, now dominant in China, use carbonate and no nickel or cobalt; high-nickel NMC batteries use hydroxide, nickel and cobalt.',
    '<b>Cobalt</b> is mostly a by-product of DRC copper mines; DRC export quotas have driven its price.',
    '<b>Graphite and rare earths</b> are dominated by Chinese processing, making them policy-sensitive &ldquo;critical minerals&rdquo; for Western governments.'])
h2('Uranium')
p('Uranium is sold mostly under long-term contracts between producers and nuclear utilities; the thinly traded spot market sets sentiment. Kazatomprom (Kazakhstan, mostly ISR) and Cameco (Canada, high-grade underground in the Athabasca Basin) are the two largest producers. Demand rests on reactor life extensions, new builds in China and India, and growing interest in small modular reactors and data-centre power. Supply has been slow to respond because new mines take a decade to permit and build.')
h2('Platinum Group Metals')
p('South Africa&rsquo;s Bushveld Complex produces about 70% of the world&rsquo;s platinum; Russia&rsquo;s Nornickel is the largest palladium producer. Autocatalysts take most demand, so the shift to battery EVs is a long-term risk, partly offset by hybrids, jewellery and hydrogen technologies. Deep, labour-intensive South African mines are exposed to power outages and wage cycles. Platinum rose above US$2,700/oz in late January 2026 (Host Rock weekly rundown) and closed at US$1,543/oz on October 27.')

# ---------------- 7. Pricing & Markets ----------------
sec('Pricing &amp; Markets', 'markets',
    'Most metals are priced off a handful of exchanges and assessment agencies. Over the long run, the marginal cost of supply anchors prices.')
side('When price falls below the cost of the highest-cost producers needed to meet demand, supply is cut until the market rebalances.')
p('A producer&rsquo;s realized price is the benchmark adjusted for product quality, location and contract terms. Over the long run, the marginal cost of supply anchors prices: when price falls below the cost of the highest-cost producers needed to meet demand, supply is cut until the market rebalances.')
h2('Exchanges and Benchmarks')
tbl(['Market', 'What trades there', 'Notes'], [
    ['<b>London Metal Exchange (LME)</b>', 'Copper, aluminum, zinc, nickel, lead, tin, cobalt', 'The global reference for base metals; cash and 3-month contracts; warehouse stocks watched as a supply signal'],
    ['<b>COMEX</b> (CME Group, New York)', 'Gold, silver, copper', 'Copper quoted in US&cent;/lb; COMEX can trade at a premium to LME when US tariffs or import rushes distort flows'],
    ['<b>LBMA</b> (London)', 'Gold and silver', 'Twice-daily gold auction sets the LBMA Gold Price used in most sales contracts and royalties'],
    ['<b>Shanghai Futures Exchange</b> (SHFE)', 'Copper, aluminum, zinc, nickel, gold', 'Reflects Chinese domestic demand; the Shanghai-London arbitrage drives import flows'],
    ['<b>Guangzhou Futures Exchange</b> (GFEX)', 'Lithium carbonate', 'Launched 2023; now the most-watched lithium price'],
    ['<b>SGX and Dalian Commodity Exchange</b>', 'Iron ore', 'Futures settle against the 62% Fe index'],
    ['<b>Price reporting agencies</b> (Platts, Argus, Fastmarkets, Benchmark, UxC)', 'Iron ore, coal, lithium, cobalt, rare earths, uranium', 'Assessed prices used where no liquid exchange contract exists'],
], widths=['30%', '28%', '42%'])
h2('Realized Price vs. Benchmark')
ul(['<b>Quality premiums or discounts.</b> High-grade iron ore, low-impurity concentrate and battery-grade lithium all earn premiums; impurity penalties cut realized price.',
    '<b>Regional premiums.</b> Physical buyers pay a premium over the LME price for delivered metal: for example the Rotterdam or US Midwest aluminum premium, or the Shanghai Yangshan copper premium.',
    '<b>Provisional pricing.</b> Concentrate is invoiced provisionally on shipment and finalized months later at the average price of a quotational period. If prices fall between shipment and settlement, miners book negative &ldquo;provisional price adjustments&rdquo; in their next results.',
    '<b>Hedging and forward sales.</b> Locks in a price, protecting debt service but capping upside. Investors generally prefer unhedged gold producers; project lenders often require hedging.'])
h2('Futures Curves: Contango and Backwardation')
side('LME copper in backwardation with falling warehouse stocks is a classic bullish signal.')
p('A futures curve is in <b>contango</b> when future prices are above spot, usually a sign of ample supply and inventory, and in <b>backwardation</b> when future prices are below spot, a sign of tight physical supply. LME copper in backwardation with falling warehouse stocks is a classic bullish signal. For investors holding futures or futures-based ETFs, contango creates a negative roll yield: rolling a US$10,000/t contract into a US$10,200/t contract each period loses 2% if the spot price stays flat.')
h2('The Cost Curve', 'costcurve')
p(f'An industry cost curve ranks every mine by unit cost (C1 or AISC) from lowest to highest, with cumulative production along the x-axis (Exhibit {nextex()}). Investors use it three ways:')
exhibit('Industry Cost Curve: How Investors Read It (Illustrative Gold AISC Curve)', 'img/cost_curve.png', 'Northwall Research; illustrative distribution, not company data')
ol(['<b>Price floor.</b> Prices rarely stay below the 90th-percentile cost for long: high-cost mines lose cash and close. That level is often treated as the long-term floor.',
    '<b>Incentive price.</b> The price needed to justify building the next mine, including capital and a return, is usually well above today&rsquo;s cash costs. For copper it is generally estimated well above US$4/lb; long-term analyst price decks often sit near the incentive price.',
    '<b>Position.</b> A mine in the first quartile survives any downturn; a fourth-quartile mine is a call option on higher prices.'])
h2('Offtakes, Streams and Royalties')
p('Developers fund mines partly by selling future production:')
ul(['<b>Offtake agreement.</b> A buyer (smelter, trader or end user) commits to purchase production at market-linked prices, often paired with a loan or equity investment.',
    '<b>Royalty.</b> A right to a percentage of revenue or profit from a mine (detailed under Fiscal Regimes), with no obligation to fund costs.',
    '<b>Stream.</b> An upfront cash deposit in exchange for the right to buy a fixed percentage of a mine&rsquo;s metal, often a by-product such as gold or silver from a copper mine, at a low fixed price (for example US$400/oz gold or 20% of spot). Wheaton Precious Metals, Franco-Nevada and Royal Gold are the leading streaming and royalty companies.'])
p('Streams and royalties are cheaper than equity for a developer when its share price is weak, but they reduce the cash flow left for shareholders and lenders, so they are deducted in the NAV.')

# ---------------- 8. Costs ----------------
sec('Costs &amp; Operating Metrics', 'costs',
    'The margin between price and unit cost is what investors buy. Learning to rebuild a mine&rsquo;s unit cost from its operating data is the core analytical skill.')
p('Because costs are mostly fixed in the short run (labour, power, equipment), small changes in grade, throughput or price produce large changes in profit.')
h2('Cost Definitions')
tbl(['Measure', 'What it includes', 'Used for'], [
    ['<b>Site or unit operating cost</b>', 'Mining, processing and site G&amp;A per tonne of ore (US$/t)', 'Comparing mines on an engineering basis'],
    ['<b>Cash cost (C1)</b>', 'Site costs, plus TC/RCs, freight and royalties in some definitions, less by-product credits, per unit of payable metal', 'Base metals (copper, nickel, zinc); defines the industry cost curve'],
    ['<b>C3 (fully allocated)</b>', 'C1 plus depreciation, corporate costs and interest', 'Accounting-based margin'],
    ['<b>All-in sustaining cost (AISC)</b>', 'Cash costs, royalties and production taxes, sustaining capital, sustaining exploration, corporate G&amp;A, reclamation accretion, less by-product credits (World Gold Council guidance, 2013)', 'Gold and silver; the main yardstick of free cash flow per ounce'],
    ['<b>All-in cost (AIC)</b>', 'AISC plus growth capital and non-sustaining exploration', 'Total cost including expansion; whole-company cash burn'],
], widths=['24%', '46%', '30%'])
p('Cost measures are non-GAAP, so definitions vary between companies. Always check whether by-products are treated as credits (lowering cost) or co-products (costs split pro rata by revenue), and whether royalties, freight and TC/RCs are included.')
h2('Key Operating Metrics')
ul(['<b>Throughput.</b> Tonnes of ore processed per day or year; capped by mill capacity.',
    '<b>Head grade.</b> The grade of ore actually fed to the mill. Compare it with reserve grade and with guidance each quarter.',
    '<b>Recovery.</b> The share of metal in the feed that reports to the product.',
    '<b>Production</b> = tonnes milled &times; head grade &times; recovery. Example: 10,000 tpd &times; 365 days &times; 1.5 g/t &times; 92% recovery = 5.04 t of gold, or about 162 koz a year.',
    '<b>Unit cost per tonne milled.</b> Divide total site costs by tonnes processed. A mine with US$60/t costs and 1.5 g/t ore at 92% recovery spends about US$1,350 per ounce produced before sustaining capital.',
    '<b>Sustaining vs. growth capital.</b> Sustaining capital keeps current output running (equipment replacement, tailings raises, underground development). Growth capital expands it. The classification matters because only sustaining capital is in AISC.'])
h2('Worked Example: Gold AISC')
tbl(['Item', 'US$ million', 'US$/oz (250 koz sold)'], [
    ['Mining, processing, site G&amp;A', '250', '1,000'], ['Royalties and production taxes (5% of revenue at US$4,000/oz)', '50', '200'], ['Less silver by-product credits', '(10)', '(40)'],
    ('__b__', 'Cash cost', '290', '1,160'), ['Sustaining capital', '75', '300'], ['Sustaining exploration and reclamation', '15', '60'], ['Corporate G&amp;A', '20', '80'],
    ('__b__', 'AISC', '400', '1,600'), ['Growth capital and expansion exploration', '60', '240'], ('__b__', 'AIC', '460', '1,840'),
], widths=['60%', '18%', '22%'], num_cols=(1, 2))
exhibit('From Site Costs to AISC and AIC (US$/oz)', 'img/aisc.png', 'Northwall Research; worked example')
p('At US$4,000/oz, this mine generates about US$2,400/oz of margin over AISC and US$600 million of pre-tax free cash flow before growth spending. Royalties rise with the gold price, so AISC is not fully fixed.')
h2('Worked Example: Copper C1 with By-Product Credits')
p('A copper-gold mine produces 200 Mlb of payable copper and 100 koz of payable gold a year. Site costs are US$700 million, and TC/RCs plus freight are US$100 million.')
ul(['Gross cost: (US$700M + US$100M) / 200 Mlb = US$4.00/lb.', 'Gold credit: 100 koz &times; US$4,000/oz = US$400 million, or US$2.00/lb.', '<b>C1 = US$2.00/lb</b> net of by-products.'])
side('By-product-heavy producers carry hidden exposure to the by-product price.')
p('If gold falls 25% to US$3,000/oz, the credit falls to US$1.50/lb and C1 rises to US$2.50/lb, even though nothing changed at the mine. By-product-heavy producers carry hidden exposure to the by-product price.')
h2('Operating Leverage', 'leverage')
p(f'Profit moves faster than price because costs are largely fixed. Using the gold example above (Exhibit {nextex()}):')
tbl(['Gold price (US$/oz)', 'Margin over AISC (US$/oz)', 'Change in margin vs. US$4,000'], [
    ['3,200', '1,640', '&minus;32%'], ['3,600', '2,020', '&minus;16%'], ['4,000', '2,400', '&ndash;'], ['4,400', '2,780', '+16%'], ['4,800', '3,160', '+32%']],
    widths=['30%', '35%', '35%'], num_cols=(0, 1, 2))
exhibit('Margin Sensitivity to the Gold Price: Low-Cost vs. High-Cost Producer', 'img/leverage.png', 'Northwall Research; royalties at 5% of revenue')
p('The margin moves about 1.6 times the price (AISC is adjusted for royalties at 5% of revenue). Higher-cost producers have more leverage in both directions: at an AISC of US$3,000/oz, a 10% fall in gold from US$4,000 cuts the margin by about 38%.')
box('Northwall coverage: Alamos Gold (NYSE/TSX: AGI)',
    '<p>Alamos shows why cost trajectory matters more than volume. Our model has production rising from 535 koz in 2026E to 770 koz in 2028E as the Island Gold Phase 3+ shaft and the Magino mill expansion arrive. Over the same period, AISC falls from about US$1,826/oz to US$1,350/oz.</p><p>At a flat US$4,000/oz gold price, the margin per ounce rises about 22%, but total margin rises about 75% because more ounces earn the wider margin. That combination of volume and falling cost is the core of our Buy rating and US$39.00 target.</p>')
h2('Cost Inflation Drivers')
p('Labour, energy (diesel and power are 15% to 30% of costs at many mines), reagents (cyanide, lime, sulphuric acid), explosives, tires and steel consumables, and local currency. Most mines report in US dollars but pay costs in Canadian or Australian dollars, Chilean pesos or South African rand, so a weaker local currency lowers US-dollar costs.')
