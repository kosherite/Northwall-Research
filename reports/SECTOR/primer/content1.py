from kit import *

# ---------------- 1. Metals & Mining Defined ----------------
sec('Metals &amp; Mining Defined', 'defined',
    'A mining equity is a leveraged claim on metal in the ground. Its value depends on how much metal there is, at what grade, at what cost to extract, in which jurisdiction and at what price.')
side('Unlike oil and gas, there is no single &ldquo;barrel.&rdquo; The first question for any mining stock is which commodity drives its cash flow.')
p('Unlike oil and gas, there is no single &ldquo;barrel&rdquo; in mining. Each metal has its own demand drivers, price benchmark and processing route. The first question for any mining stock is therefore which commodity drives its cash flow, and the second is where the company sits on the value chain.')
h2('Commodity Families')
tbl(['Family', 'Examples', 'Main demand drivers', 'Where the price is set'], [
    ['<b>Precious metals</b>', 'Gold, silver', 'Investment (ETFs, bars, coins), central-bank buying, jewellery; silver also industrial (solar, electronics)', 'LBMA (London), COMEX (New York)'],
    ['<b>Platinum group metals</b>', 'Platinum, palladium, rhodium', 'Autocatalysts, jewellery, chemicals, hydrogen electrolysis', 'LPPM, NYMEX'],
    ['<b>Base metals</b>', 'Copper, nickel, zinc, lead, aluminum, tin', 'Construction, power grids, vehicles, industrial production; strongly tied to China', 'LME (London), COMEX, SHFE (Shanghai)'],
    ['<b>Bulk and steelmaking</b>', 'Iron ore, metallurgical coal, manganese', 'Steel output, above all in China', 'Index-priced: 62% Fe fines (SGX, Dalian); premium hard coking coal (Platts)'],
    ['<b>Battery and critical minerals</b>', 'Lithium, cobalt, graphite, rare earths, vanadium', 'Electric vehicles, grid storage, permanent magnets, defence', 'Price assessments (Fastmarkets, Benchmark); GFEX lithium futures'],
    ['<b>Energy minerals</b>', 'Uranium', 'Nuclear fuel procurement by utilities', 'Spot and long-term contract assessments (UxC, TradeTech)'],
], widths=['19%', '21%', '33%', '27%'])
h2('The Value Chain', 'valuechain')
side('Where a company sits on the value chain sets how exposed its earnings are to the metal price.')
p('The mining value chain runs from finding a deposit to delivering metal to a fabricator (Exhibit 1). Where a company sits on it sets how exposed its earnings are to the metal price.')
exhibit('Mining Value Chain', 'img/value_chain.png', 'Northwall Research')
ul(['<b>Upstream (explorers, developers, producers).</b> Owns the orebody and sells metal or concentrate at the market price less costs. Earnings move most with the commodity price: this is where the operating leverage sits, and where most listed mining equities live.',
    '<b>Midstream (smelters, refiners, traders).</b> Converts concentrate into refined metal for a processing fee (treatment and refining charges, TC/RCs) plus by-product sales. Margins depend on concentrate supply and demand more than on the metal price.',
    '<b>Downstream (fabricators and end users).</b> Turns refined metal into wire, rod, sheet, steel, batteries and jewellery. Metal is a pass-through cost.'])
p('Some companies choose one segment: a junior drilling a copper porphyry, a pure producer such as Freeport-McMoRan, or a royalty company such as Franco-Nevada that owns a slice of revenue without operating. Diversified majors such as BHP, Rio Tinto and Glencore span several commodities and, in Glencore&rsquo;s case, smelting and trading as well.')

# ---------------- 2. Geology ----------------
sec('Geology &amp; Deposit Types', 'geology',
    'An ore deposit is a rare, natural concentration of metal high enough to mine at a profit. Geology decides the three numbers that drive every mine&rsquo;s economics: size, grade and shape.')
side('A mineable copper deposit needs 50 to 100 times the crustal average; a gold deposit 250 times or more.')
p('The average crust holds about 0.006% copper and 0.004 g/t gold. A mineable copper deposit needs roughly 50 to 100 times that concentration, and a gold deposit 250 times or more. Geology decides size (tonnes), grade (metal per tonne) and shape (how deep, how continuous, how much waste must be moved).')
h2('How Ore Deposits Form')
p('Most metal deposits form when hot, metal-bearing fluids move through rock and drop their metal where temperature, pressure or chemistry changes abruptly. Others form by settling in ancient seas or basins, by weathering that leaves metal behind (laterites), or by crystallizing in magma. The formation process controls a deposit&rsquo;s size, grade, depth and metallurgy, so geologists classify deposits into types with predictable characteristics. Exhibit 2 maps the type examples used in this primer.')
exhibit('Major Deposits of the World by Commodity', 'img/map_deposits.png', 'Natural Earth (base map); company disclosures; Northwall Research', wide=True)
h2('Major Deposit Types')
tbl(['Deposit type', 'Main metals', 'Typical size and grade', 'Mining style', 'Examples'], [
    ['<b>Porphyry</b>', 'Copper, gold, molybdenum', 'Very large (500 Mt to several Bt); low grade (0.3% to 1.0% Cu)', 'Large open pit, later block cave', 'Escondida (Chile), Grasberg (Indonesia), Oyu Tolgoi (Mongolia)'],
    ['<b>Sediment-hosted copper</b>', 'Copper, cobalt', 'Large; higher grade (2% to 6% Cu)', 'Underground and open pit', 'Kamoa-Kakula (DRC), Zambian Copperbelt'],
    ['<b>Volcanogenic massive sulphide (VMS)</b>', 'Copper, zinc, lead, silver, gold', 'Small to medium (5 to 100 Mt); high grade, polymetallic', 'Mostly underground', 'Kidd Creek (Canada), Neves-Corvo (Portugal)'],
    ['<b>Iron oxide copper-gold (IOCG)</b>', 'Copper, gold, uranium', 'Large, variable grade', 'Underground', 'Olympic Dam (Australia)'],
    ['<b>Orogenic gold</b>', 'Gold', 'Small to large; 2 to 10+ g/t in narrow veins', 'Underground, some open pit', 'Timmins and Kirkland Lake (Canada), Kalgoorlie (Australia)'],
    ['<b>Epithermal</b>', 'Gold, silver', 'Small to medium; can be very high grade near surface', 'Open pit or underground', 'Lihir (Papua New Guinea), Yanacocha (Peru)'],
    ['<b>Banded iron formation</b>', 'Iron ore', 'Billions of tonnes; 55% to 65% Fe', 'Massive open pit', 'Pilbara (Australia), Carajás (Brazil)'],
    ['<b>Magmatic sulphide</b>', 'Nickel, copper, PGMs', 'Medium; 1% to 3% Ni or 3 to 10 g/t PGM', 'Underground', 'Sudbury (Canada), Norilsk (Russia), Bushveld (South Africa)'],
    ['<b>Nickel laterite</b>', 'Nickel, cobalt', 'Large, shallow; 1% to 2% Ni', 'Shallow open pit, then HPAL or smelting', 'Sulawesi (Indonesia), New Caledonia'],
    ['<b>Lithium pegmatite and brine</b>', 'Lithium', 'Hard rock 1% to 1.5% Li<sub>2</sub>O; brine 500 to 2,000+ mg/L Li', 'Open pit (spodumene) or evaporation ponds', 'Greenbushes (Australia), Salar de Atacama (Chile)'],
    ['<b>Unconformity uranium</b>', 'Uranium', 'Small footprint, extremely high grade (up to 15%+ U<sub>3</sub>O<sub>8</sub>)', 'Underground, freeze methods', 'Cigar Lake, McArthur River (Canada)'],
    ['<b>Sandstone uranium</b>', 'Uranium', 'Low grade, permeable host rock', 'In-situ recovery (ISR)', 'Kazakhstan, Wyoming'],
], widths=['17%', '15%', '24%', '19%', '25%'], cls='small')
h2('Grade, Tonnage and Strip Ratio')
side('Grade is the single most important number in mining. Continuity matters just as much.')
ul(['<b>Grade</b> is the concentration of metal: grams per tonne (g/t) for gold, silver and PGMs; percent for base metals and lithium oxide (Li<sub>2</sub>O). A 2 g/t gold deposit produces twice the metal per tonne processed as a 1 g/t deposit for nearly the same mining cost.',
    '<b>Tonnage</b> is the mass of mineralized rock. Contained metal = tonnes &times; grade. Example: 100 Mt at 0.5% Cu contains 500,000 t of copper, or about 1.1 billion lb.',
    '<b>Cut-off grade</b> is the lowest grade that pays to process. Rising metal prices lower the cut-off and can grow reserves; rising costs do the opposite.',
    '<b>Strip ratio</b> is tonnes of waste moved per tonne of ore in an open pit. A 3:1 strip ratio means 3 t of waste for every 1 t of ore. Higher strip ratios raise unit costs and capital needs.',
    '<b>Metallurgy</b> is how easily the metal can be extracted. &ldquo;Free-milling&rdquo; gold leaches easily; &ldquo;refractory&rdquo; gold locked in sulphides needs roasting, autoclaves or bio-oxidation and costs more.'])
p('Geologists often note that grade is king, but continuity matters just as much. A high-grade deposit that is erratic and hard to model carries more risk than a lower-grade, predictable one.')

# ---------------- 3. Resources & Reserves ----------------
sec('Resources &amp; Reserves', 'reserves',
    'Mineral Reserves are the only part of a deposit a company can call economically mineable. Investors pay most for reserves, less for Measured and Indicated resources, and least for Inferred.')
h2('Reporting Codes')
side('Under NI 43-101, a Qualified Person signs off every resource and reserve estimate.')
p('Public mining companies must report resources and reserves under a recognized code, signed off by a Qualified Person (QP) or Competent Person. The codes share one framework through CRIRSCO, the Committee for Mineral Reserves International Reporting Standards, so the categories line up across jurisdictions.')
tbl(['Code', 'Jurisdiction', 'Who signs off', 'Notes'], [
    ['<b>NI 43-101</b> (with CIM Definition Standards)', 'Canada (TSX, TSX-V)', 'Qualified Person', 'Requires a technical report for material properties; the most common code for juniors worldwide'],
    ['<b>JORC Code</b>', 'Australia (ASX); also Asia and Africa', 'Competent Person', 'Requires Table 1 disclosure of sampling and estimation methods'],
    ['<b>S-K 1300</b>', 'United States (SEC registrants)', 'Qualified Person', 'Replaced Industry Guide 7 in 2021; now allows resource disclosure'],
    ['<b>PERC, SAMREC</b>', 'Europe, South Africa', 'Competent Person', 'CRIRSCO-aligned'],
], widths=['24%', '24%', '17%', '35%'])
h2('The Classification Ladder')
p(f'Resources move up the ladder with more drilling, which raises geological confidence. They convert to reserves by applying <b>modifying factors</b>: mining method, dilution and recovery, metallurgy, costs, metal prices, infrastructure, permits, and environmental and social conditions (Exhibit {nextex()}).')
exhibit('Mineral Resource and Reserve Classification (CIM and CRIRSCO)', 'img/classification.png', 'CIM Definition Standards; CRIRSCO; Northwall Research')
tbl(['', 'Category', 'Confidence', 'Can it support a mine plan?'], [
    ['<b>Reserves</b>', 'Proven', 'Highest: converted from Measured resources with modifying factors applied', 'Yes: basis for feasibility studies and financing'],
    ['', 'Probable', 'High: converted from Indicated (or Measured) resources', 'Yes'],
    ['<b>Resources</b>', 'Measured', 'Close-spaced drilling; grade and continuity confirmed', 'Only after conversion to reserves'],
    ['', 'Indicated', 'Drilling adequate to assume continuity', 'Only after conversion; usable in PFS/FS'],
    ['', 'Inferred', 'Limited drilling; continuity assumed, not verified', 'No: only in PEAs, with cautionary language'],
    ['<b>Exploration target</b>', 'Target or potential', 'Conceptual, no resource estimated', 'No: a range of tonnes and grade only'],
], widths=['17%', '18%', '37%', '28%'])
p('A Mineral Reserve is reported as the ore actually delivered to the mill, after dilution and mining losses, so reserve grade is normally lower than resource grade. Two reporting conventions deserve attention:')
side('Adding resources to reserves when resources are reported inclusive double-counts metal.')
ul(['<b>Inclusive vs. exclusive.</b> Some companies report resources <i>inclusive</i> of reserves (the reserve is a subset); others report them <i>exclusive</i> (additional to reserves). Adding the two when resources are inclusive double-counts metal.',
    '<b>Price deck.</b> Reserves are calculated at a stated metal price. A company using US$2,000/oz gold for reserves while spot trades above US$4,000/oz has a conservative estimate with built-in upside; one using a price near spot has little cushion.'])
h2('Study Stages')
p(f'Each engineering study refines the estimate of capital, operating costs and economics, and costs more to complete (Exhibit {nextex()}).')
exhibit('Accuracy of the Capital Estimate by Study Stage', 'img/studies.png', 'CIM; AACE International; Northwall Research')
tbl(['Study', 'Resources it may use', 'Purpose'], [
    ['<b>Scoping study / PEA</b> (Preliminary Economic Assessment)', 'Measured, Indicated and Inferred', 'First look at economics; cannot declare reserves'],
    ['<b>Pre-feasibility study (PFS)</b>', 'Measured and Indicated', 'Selects the preferred development option; first declaration of reserves'],
    ['<b>Feasibility study (FS or DFS)</b>', 'Measured and Indicated', 'Basis for the construction decision and project finance'],
], widths=['36%', '28%', '36%'])
h2('Operational Metrics')
side('Persistently below 100% reserve replacement means the company is shrinking.')
p('<b>Reserve life (years)</b> is reserves divided by annual production. A mine with 5 Moz of gold reserves producing 400 koz a year has a 12.5-year reserve life. Gold investors typically want 10+ years; shorter lives force a company to keep buying or discovering ounces.',
  '<b>Reserve replacement ratio</b> is reserves added in a year divided by reserves mined. A producer that mined 500 koz and added 600 koz through drilling has a 120% replacement ratio. Persistently below 100% means the company is shrinking.',
  '<b>Conversion rate</b> is the share of Inferred resources that become Indicated (or of resources that become reserves) after infill drilling. Historical conversion of 60% to 80% at a given mine is a useful guide for valuing its remaining Inferred ounces.',
  '<b>Discovery cost</b> is exploration spend divided by new ounces or pounds discovered. A junior that spends US$20 million and adds 1 Moz of resources has a discovery cost of US$20/oz.')

# ---------------- 4. Mining Methods ----------------
sec('Mining Methods', 'methods',
    'The mining method is set by the orebody&rsquo;s depth, shape and grade, and it fixes most of the cost structure.')
side('Open pits move huge tonnages cheaply but must strip waste; underground mines need grades several times higher.')
p(f'Open pits move huge tonnages cheaply but must strip waste; underground mines move less rock at a higher cost per tonne, so they need higher grades (Exhibit {nextex()}).')
exhibit('Open Pit, Underground and Block Cave Mining (Schematic)', 'img/mining_methods.png', 'Northwall Research; schematic, not to scale', wide=True)
h2('Surface Mining')
p('<b>Open pit.</b> Benches are drilled, blasted, loaded by shovels or excavators and hauled by trucks, widening and deepening the pit over time. This suits large, near-surface, lower-grade deposits (porphyry copper, bulk gold, iron ore). Mining costs are typically US$2 to US$5 per tonne of material moved, so economics hinge on the strip ratio and haul distances.',
  '<b>Strip mining.</b> Used for flat-lying deposits such as coal, bauxite and mineral sands. Overburden is removed in strips, ore is mined, and waste is backfilled behind the advancing face.',
  '<b>Placer and alluvial mining.</b> Recovers gold, tin, diamonds and mineral sands from loose sediments using gravity separation. Low capital, and often artisanal.')
h2('Underground Mining')
p('Underground mines are accessed by a vertical <b>shaft</b>, which hoists ore in skips, or a <b>decline</b> (ramp), which trucks drive to surface. Costs typically run US$50 to US$150+ per tonne of ore, so grades must be several times higher than an open pit&rsquo;s.')
tbl(['Method', 'How it works', 'Suited to', 'Cost and recovery'], [
    ['<b>Block caving</b>', 'Undercut the base of the orebody; it collapses under gravity and is drawn from drawpoints below', 'Very large, low-grade bodies (porphyry copper at depth)', 'Lowest underground cost (US$10 to US$20/t); high capital, long build (5 to 10 years)'],
    ['<b>Sublevel caving</b>', 'Ore is blasted level by level and the hanging wall caves behind', 'Large, steep bodies (iron ore, Kiruna)', 'Low cost; higher dilution'],
    ['<b>Long-hole (sublevel) open stoping</b>', 'Large rooms blasted between levels, later backfilled', 'Steep, competent, medium-width bodies', 'Moderate cost; good recovery'],
    ['<b>Cut-and-fill</b>', 'Ore mined in horizontal slices, each backfilled to form the floor for the next', 'Narrow, irregular or weak ground; high-grade veins', 'High cost; very selective, low dilution'],
    ['<b>Room-and-pillar</b>', 'Rooms mined with pillars left for support', 'Flat-lying deposits (potash, some base metals)', 'Low cost; 20% to 40% of ore left in pillars'],
], widths=['19%', '31%', '25%', '25%'])
h2('Solution Mining')
p('<b>In-situ recovery (ISR).</b> A leaching solution is pumped through permeable ore via injection wells and recovered through production wells; no rock is moved. Most of Kazakhstan&rsquo;s and much of US uranium is produced this way, at low cost and with low surface disturbance.',
  '<b>Brine extraction.</b> Lithium-rich brine is pumped from beneath salt flats into evaporation ponds that concentrate it over 12 to 24 months. Direct lithium extraction (DLE) uses adsorbents or ion exchange to cut this to days, but remains early in commercial scale-up.')
h2('Dilution and Mining Recovery')
side('Grades persistently below reserve grade are one of the most common causes of guidance misses.')
ul(['<b>Dilution</b> is waste rock mined along with ore, lowering grade. 10% dilution turns 5.0 g/t in situ into roughly 4.5 g/t delivered to the mill.',
    '<b>Mining recovery</b> is the share of in-situ ore actually extracted; pillars, losses and unrecoverable edges reduce it.',
    'Both are built into reserves. When an operating mine reports grades persistently below the reserve grade, it is usually a sign that dilution or the geological model was too optimistic, one of the most common causes of guidance misses.'])

# ---------------- 5. Processing ----------------
sec('Processing &amp; Metallurgy', 'processing',
    'Processing turns ore into a saleable product: a concentrate, doré bars or refined metal. Every point of recovery falls straight to revenue.')
side('Recovery typically runs 85% to 95% for copper flotation and gold leaching.')
p(f'Recovery, the share of metal in the ore that ends up in the product, typically runs 85% to 95% for copper flotation and gold leaching. Exhibit {nextex()} shows the three most common routes from mine to metal.')
exhibit('Main Processing Routes, from Mine to Metal', 'img/flowsheet.png', 'Northwall Research', wide=True)
h2('Main Process Routes')
tbl(['Step', 'What happens', 'Used for'], [
    ['<b>Comminution</b> (crushing and grinding)', 'Ore is crushed, then ground in SAG and ball mills to sand or flour size to free the mineral grains', 'Almost all hard-rock ore; often the largest energy and cost item in the plant'],
    ['<b>Gravity separation</b>', 'Dense particles separated by weight (jigs, spirals, centrifugal concentrators)', 'Coarse gold, tin, mineral sands, iron ore'],
    ['<b>Froth flotation</b>', 'Chemicals make sulphide minerals water-repellent; air bubbles carry them into a froth skimmed off as concentrate (20% to 40% Cu, 50%+ Zn)', 'Copper, zinc, lead, nickel sulphides, PGMs'],
    ['<b>Cyanide leaching</b> (CIL/CIP)', 'Ground ore is leached with dilute cyanide; dissolved gold is captured on activated carbon, stripped and poured as doré (gold-silver bars)', 'Free-milling gold'],
    ['<b>Heap leaching</b>', 'Crushed or run-of-mine ore is stacked on lined pads and irrigated with cyanide (gold) or acid (copper)', 'Low-grade gold and oxide copper; low capital, lower recovery (50% to 80%)'],
    ['<b>Pressure oxidation, roasting, bio-oxidation</b>', 'Breaks down sulphides that lock up gold before leaching', 'Refractory gold'],
    ['<b>SX-EW</b> (solvent extraction, electrowinning)', 'Copper in acid leach solution is purified and plated directly as 99.99% cathode at the mine', 'Oxide copper; avoids smelting'],
    ['<b>HPAL</b> (high-pressure acid leach)', 'Laterite ore leached with acid in autoclaves to produce nickel-cobalt intermediates', 'Indonesian nickel laterites'],
    ['<b>Pelletizing and beneficiation</b>', 'Low-grade iron ore upgraded and formed into pellets', 'Magnetite iron ore'],
    ['<b>Spodumene concentration and conversion</b>', 'Lithium ore concentrated to about 6% Li<sub>2</sub>O (SC6), then refined into carbonate or hydroxide, mostly in China', 'Hard-rock lithium'],
], widths=['27%', '45%', '28%'], cls='small')
h2('Smelting and Refining')
side('Most miners do not own smelters, so the terms on which concentrate is sold matter as much as the metal price.')
p('Concentrate is sold to a smelter, which melts it to produce impure metal (blister or anode copper at about 99%), then refines it electrolytically to 99.99% cathode. China operates more than half of global copper smelting capacity, and most miners do not own smelters, so the terms on which concentrate is sold matter as much as the metal price.')
h2('How Concentrate Is Priced')
p('A miner is not paid the full value of the metal in its concentrate. The smelter keeps a share and charges fees:')
ul(['<b>Payable metal.</b> Typically 96% to 97% of contained copper (or the contained amount less about one unit), 85% for zinc, and 90% to 97% of gold and silver in a copper concentrate.',
    '<b>Treatment charge (TC).</b> A fee per dry metric tonne of concentrate for smelting.',
    '<b>Refining charge (RC).</b> A fee per payable pound (copper) or ounce (precious metals) for refining.',
    '<b>Penalties.</b> Deductions for impurities above set limits, such as arsenic, bismuth, mercury or fluorine.',
    '<b>Freight and insurance</b> to the smelter port, plus the pricing period (often the average price in the month after arrival, called &ldquo;M+1&rdquo;).'])
p('TC/RCs are set annually in benchmark talks between major miners and Chinese smelters, and also trade on the spot market. When concentrate is scarce, as in 2025 when smelter capacity outgrew mine supply, spot TCs can fall to zero or below; smelters lose money while miners keep more of the metal value.')
h3('Worked example: net smelter return on 1 dry tonne of copper concentrate')
tbl(['Item', 'Calculation', 'US$ per dmt'], [
    ['Contained copper', '28% grade &times; 2,204.6 lb = 617.3 lb', ''],
    ['Payable copper', '96.5% &times; 617.3 lb = 595.7 lb', ''],
    ['Gross payable value', '595.7 lb &times; US$6.65/lb', '3,961'],
    ['Less treatment charge', 'Illustrative US$25/dmt', '(25)'],
    ['Less refining charge', '595.7 lb &times; US$0.025/lb', '(15)'],
    ['Less freight and insurance', 'Illustrative', '(60)'],
    ['Net smelter return', '', '3,861'],
], widths=['34%', '46%', '20%'], bold_last=True, num_cols=(2,))
exhibit('Net Smelter Return Bridge, One Dry Tonne of Copper Concentrate', 'img/nsr.png', 'Northwall Research; illustrative terms')
p('The miner keeps about 97% of the gross metal value at a US$25 TC. At an US$80 TC and 8&cent; RC, levels seen in 2021 and 2022, the NSR falls by roughly US$90 per tonne, about 2.2%. For a mine selling 1 Mt of concentrate a year, that difference is about US$90 million of revenue.')
