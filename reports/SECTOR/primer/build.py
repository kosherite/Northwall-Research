"""Build Metals & Mining Made Simple (Northwall Research) as a PDF."""
import kit
from kit import B, TOC, table
import content1, content2, content3  # noqa: F401  (each appends to kit.B)
from weasyprint import HTML

MARK = '''<svg width="{s}" height="{s}" viewBox="0 0 36 36"><rect x="3" y="11" width="8" height="23" fill="#2F5D7C"/><rect x="14" y="2" width="8" height="32" fill="{c}"/><rect x="25" y="11" width="8" height="23" fill="#2F5D7C"/></svg>'''
DATE = 'October 2026'

toc = ''.join(f'<li class="l{lv}"><a href="#{a}">{t}</a></li>' for a, t, lv in TOC)
abbr = [('oz', 'Troy ounce (31.1035 g)'), ('koz / Moz', 'Thousand / million troy ounces'), ('g/t', 'Grams per tonne (precious metals grade)'), ('% Cu, % Ni', 'Percent metal by weight (base metals grade)'),
        ('lb', 'Pound (copper, nickel, zinc, uranium prices)'), ('ppm', 'Parts per million (1 ppm = 1 g/t)'), ('AuEq / CuEq', 'Gold / copper equivalent grade'), ('t / kt / Mt', 'Metric tonne / thousand / million tonnes'),
        ('tpd / Mtpa', 'Tonnes per day / million tonnes per annum'), ('dmt / wmt', 'Dry / wet metric tonne'), ('LCE', 'Lithium carbonate equivalent'), ('U<sub>3</sub>O<sub>8</sub>', 'Uranium oxide concentrate'),
        ('AISC / AIC', 'All-in sustaining cost / all-in cost'), ('C1', 'Cash cost (Wood Mackenzie definition)'), ('NSR', 'Net smelter return'), ('TC/RC', 'Treatment and refining charges'),
        ('NAV / P/NAV', 'Net asset value / price to NAV'), ('LOM', 'Life of mine'), ('PEA / PFS / FS', 'Preliminary economic assessment / pre-feasibility / feasibility study'), ('GEO', 'Gold-equivalent ounce')]
abbr_html = '<table class="abbr">' + ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for (a, b), (c, d) in zip(abbr[:10], abbr[10:])) + '</table>'

CSS = '''
@font-face { font-family: 'Pal'; src: url('file:///usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-regular.otf'); }
@font-face { font-family: 'Pal'; font-weight: bold; src: url('file:///usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-bold.otf'); }
@font-face { font-family: 'Pal'; font-style: italic; src: url('file:///usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella-italic.otf'); }
@page { size: Letter; margin: 0.78in 0.6in 0.8in 0.6in;
  @top-left { content: element(hl); vertical-align: bottom; padding-bottom: 5pt; }
  @bottom-left { content: element(fl); vertical-align: top; padding-top: 8pt; } }
@page :left { @top-left { content: element(hl); } @bottom-left { content: element(fl); } }
@page :right { @top-left { content: element(hr); } @bottom-left { content: element(fr); } }
@page cover { margin: 0; @top-left { content: none; } @bottom-left { content: none; } @bottom-right { content: none; } }

* { box-sizing: border-box; }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 8.9pt; line-height: 1.45; color: #0F1A2B; margin: 0; }
.run { width: 7.3in; display: table; font-size: 7.6pt; color: #0F1A2B; border-bottom: 0.8pt solid #0F1A2B; padding-bottom: 3pt; }
.run > span { display: table-cell; } .run .r { text-align: right; }
.foot { width: 7.3in; border-top: 0.8pt solid #0F1A2B; padding-top: 6pt; display: table; font-size: 7.6pt; }
.foot > span { display: table-cell; vertical-align: middle; } .pg::after { content: counter(page); font-weight: bold; font-size: 8.5pt; } .foot .lk { font-weight: bold; letter-spacing: 2px; font-size: 7pt; } .foot svg { vertical-align: -3px; margin-right: 5px; }
#hl { position: running(hl); } #hr { position: running(hr); } #fl { position: running(fl); } #fr { position: running(fr); }
/* cover */
.cover { page: cover; height: 11in; position: relative; }
.cv-top { position: absolute; top: 0.55in; left: 0.6in; right: 0.6in; display: table; width: 7.3in; font-size: 8pt; letter-spacing: 2.5px; border-bottom: 0.8pt solid #0F1A2B; padding-bottom: 8pt; }
.cv-top span { display: table-cell; } .cv-top .r { text-align: right; } .cv-top b { color: #0F1A2B; }
.cv-title { position: absolute; top: 2.1in; left: 0.95in; right: 0.6in; }
.cv-title h1 { font-family: 'Pal'; font-weight: normal; font-size: 34pt; letter-spacing: 4px; color: #2F5D7C; margin: 0; line-height: 1.05; }
.cv-title .s1 { font-size: 11pt; letter-spacing: 3px; color: #2F5D7C; margin-top: 8pt; }
.cv-title .s2 { font-size: 13pt; font-weight: bold; color: #0F1A2B; margin-top: 16pt; letter-spacing: 0.5px; }
.cv-title .s3 { font-size: 9.5pt; color: #5A6B7C; margin-top: 4pt; }
.cv-band { position: absolute; top: 4.25in; left: 0; right: 0; height: 2.9in; background: #0F1A2B; overflow: hidden; }
.cv-band img { width: 8.5in; height: 2.9in; opacity: 0.9; }
.cv-logo { position: absolute; bottom: 0.75in; right: 0.6in; display: table; }
.cv-logo > div { display: table-cell; vertical-align: middle; } .cv-logo .bar { border-left: 1pt solid #2F5D7C; padding-left: 12pt; margin-left: 12pt; }
.cv-logo .w1 { font-family: 'Pal'; font-weight: bold; font-size: 17pt; letter-spacing: 6px; line-height: 1; }
.cv-logo .w2 { font-size: 7.8pt; letter-spacing: 7.4px; color: #5A6B7C; margin-top: 3pt; }
.cv-note { position: absolute; bottom: 0.78in; left: 0.95in; font-size: 7.6pt; color: #5A6B7C; width: 3.4in; line-height: 1.5; }
/* front matter */
.front { page: front; }
.front h1 { font-family: 'Pal'; font-size: 20pt; margin: 0 0 10pt; color: #0F1A2B; }
.tocl { list-style: none; padding: 0; margin: 0 0 0 1.85in; }
.tocl li { margin: 0; } .tocl li.l1 { font-weight: bold; margin-top: 5pt; font-size: 9pt; } .tocl li.l2 { padding-left: 14pt; font-size: 8.4pt; color: #2F5D7C; }
.tocl a { color: inherit; text-decoration: none; } .tocl a::after { content: leader('.') target-counter(attr(href), page); }
.abbr { margin: 18pt 0 0 1.85in; border-collapse: collapse; font-size: 7.8pt; width: 5.45in; }
.abbr td { padding: 1.6pt 4pt 1.6pt 0; vertical-align: top; } .abbr td:nth-child(odd) { font-weight: bold; width: 0.85in; } .abbr td:nth-child(2) { width: 1.85in; }
.conv { margin-left: 1.85in; font-size: 7.8pt; color: #5A6B7C; margin-top: 6pt; }
.intro { margin-left: 1.85in; }
.cov { width: 100%; border-collapse: collapse; font-size: 8.2pt; margin-top: 6pt; }
.cov th { text-align: left; font-size: 7.4pt; color: #5A6B7C; border-bottom: 0.8pt solid #0F1A2B; padding: 2pt 4pt 3pt 0; font-weight: bold; }
.cov td { padding: 4pt 4pt 4pt 0; border-bottom: 0.5pt solid #DCE2E8; }
/* body layout: main column with left margin for pull-quotes */
.body { margin-left: 1.85in; }
h1.sec { page-break-after: avoid; font-family: 'Pal'; font-weight: bold; font-size: 19pt; color: #0F1A2B; margin: 0 0 6pt -1.85in; line-height: 1.15; string-set: chap content(); }
h1.np { page-break-before: always; }
.lede { page-break-after: avoid; font-family: 'Pal'; font-size: 11pt; line-height: 1.4; color: #2F5D7C; margin: 0 0 10pt; text-align: left; }
h2 { font-size: 10.6pt; color: #2F5D7C; font-weight: bold; margin: 12pt 0 3pt; page-break-after: avoid; }
h3 { font-size: 9pt; color: #0F1A2B; font-weight: bold; margin: 9pt 0 3pt; page-break-after: avoid; }
p { margin: 0 0 6pt; text-align: justify; orphans: 2; widows: 2; }
ul, ol { margin: 0 0 7pt; padding-left: 13pt; } li { margin-bottom: 3pt; text-align: justify; } li::marker { color: #2F5D7C; }
.side { float: left; width: 1.55in; margin-left: -1.85in; margin-top: 2pt; font-family: 'Pal'; font-style: italic; font-size: 9pt; line-height: 1.35; color: #0F1A2B;
        border-top: 0.8pt solid #0F1A2B; border-bottom: 0.8pt solid #0F1A2B; padding: 4pt 0 5pt; text-align: left; break-inside: avoid; page-break-inside: avoid; }
.ex { margin: 8pt 0 10pt; border-top: 0.8pt solid #0F1A2B; border-bottom: 0.8pt solid #0F1A2B; padding: 4pt 0 4pt; page-break-inside: avoid; clear: both; }
.ex.wide { margin-left: -1.85in; }
.ext { font-size: 8.4pt; font-weight: bold; color: #2F5D7C; margin-bottom: 4pt; }
.ex img { display: block; width: 100%; }
.exn { font-size: 7pt; color: #5A6B7C; margin-top: 3pt; }
.src { font-size: 7pt; color: #2F5D7C; margin-top: 3pt; }
table.t { width: 100%; border-collapse: collapse; font-size: 7.9pt; margin: 4pt 0 9pt; line-height: 1.3; page-break-inside: auto; }
table.t thead { display: table-header-group; }
table.t th { text-align: left; font-size: 7.3pt; font-weight: bold; color: #FFFFFF; background: #0F1A2B; padding: 3pt 4pt; vertical-align: bottom; }
table.t td { padding: 3pt 4pt; border-bottom: 0.5pt solid #DCE2E8; vertical-align: top; text-align: left; }
table.t tr { page-break-inside: avoid; }
table.t tbody tr:nth-child(even) td { background: #F5F7F9; }
table.t .n { text-align: right; } table.t tr.b td { font-weight: bold; border-top: 0.8pt solid #0F1A2B; }
table.small { font-size: 7.4pt; } table.small td { padding: 2.4pt 3.5pt; }
.case { background: #E9EEF2; padding: 8pt 11pt 4pt; margin: 9pt 0 10pt; border-left: 3pt solid #2F5D7C; page-break-inside: avoid; }
.case .bt { font-weight: bold; color: #2F5D7C; font-size: 8.8pt; margin-bottom: 3pt; } .case p { font-size: 8.5pt; }
.release { border-left: 3pt solid #9DB3C6; padding: 2pt 0 2pt 11pt; margin: 4pt 0 10pt; font-size: 8.5pt; }
.release .rh1 { font-weight: bold; font-size: 9.4pt; line-height: 1.3; } .release .rsub { font-style: italic; color: #5A6B7C; margin: 3pt 0 6pt; }
.qa { margin-bottom: 7pt; page-break-inside: avoid; } .qa .qh { font-weight: bold; color: #2F5D7C; margin-bottom: 2pt; } .qa p { margin-bottom: 3pt; }
.gloss { column-count: 2; column-gap: 0.25in; font-size: 7.6pt; line-height: 1.35; margin-left: -1.85in; }
.gloss .g { margin-bottom: 3.5pt; break-inside: avoid; text-align: left; } .gloss b { color: #0F1A2B; }
.disc { font-size: 7.8pt; color: #3A4756; } .disc p { margin-bottom: 7pt; } .disc b { color: #0F1A2B; }
'''

running = f'''<div id="hl" class="run"><span>{DATE}</span><span class="r">Metals &amp; Mining Made Simple</span></div>
<div id="hr" class="run"><span>Metals &amp; Mining Made Simple</span><span class="r">{DATE}</span></div>
<div id="fl" class="foot"><span><span class="pg"></span>&nbsp;&nbsp; Northwall Research &nbsp;|&nbsp; Metals &amp; Mining</span><span style="text-align:right"><span class="lk">{MARK.format(s=12, c="#0F1A2B")}NORTHWALL RESEARCH</span></span></div>
<div id="fr" class="foot"><span><span class="lk">{MARK.format(s=12, c="#0F1A2B")}NORTHWALL RESEARCH</span></span><span style="text-align:right">Northwall Research &nbsp;|&nbsp; Metals &amp; Mining &nbsp;&nbsp;<span class="pg"></span></span></div>'''

cover = f'''<div class="cover">
<div class="cv-top"><span>{DATE.upper()}</span><span class="r">METALS &amp; MINING &nbsp;|&nbsp; <b>RESEARCH</b></span></div>
<div class="cv-title"><h1>METALS &amp; MINING<br>MADE SIMPLE</h1><div class="s1">VALUE DRIVERS FOR INVESTMENT PROFESSIONALS</div>
<div class="s2">METALS &amp; MINING RESEARCH</div><div class="s3">Basel Al-Ghousein, Analyst</div></div>
<div class="cv-band"><img src="img/cover_band.png"></div>
<div class="cv-note">Educational research. Market data as of October 27, 2026. Important disclosures appear at the end of this report.</div>
<div class="cv-logo"><div>{MARK.format(s=44, c="#0F1A2B")}</div><div class="bar"><div class="w1">NORTHWALL</div><div class="w2">RESEARCH</div></div></div>
</div>'''

about = f'''<div class="front"><h1>Metals &amp; Mining Made Simple <span style="font-weight:normal;color:#5A6B7C;font-size:13pt">(First Edition)</span></h1>
<div class="intro"><p style="font-family:Pal;font-size:11pt;color:#2F5D7C;line-height:1.4;text-align:left">Value drivers for investment professionals, from rock in the ground to a share price.</p>
<p>This primer explains what drives value in metals and mining equities. It follows the mine value chain first (geology, resources, mining and processing), then the major commodities, then costs, fiscal terms and valuation. Two appendices walk through a sample drill-results press release and a glossary of over 100 terms. Market figures are as of October 2026 unless stated; worked examples use round, hypothetical numbers.</p>
<p>Throughout, we use Northwall Research&rsquo;s own coverage to show how the concepts appear in practice: Alamos Gold for operating leverage and cost trajectory, and Franco-Nevada for the royalty model and premium valuation.</p>
<h2>Metals &amp; Mining Research</h2>
<p><b>Basel Al-Ghousein</b> (Analyst), Northwall Research. Level II candidate for the CFA designation.</p>
<table class="cov"><tr><th>Company</th><th>Ticker</th><th>Sub-sector</th><th>Rating</th><th>Target</th></tr>
<tr><td>Alamos Gold Inc.</td><td>NYSE/TSX: AGI</td><td>Gold producers</td><td>Buy</td><td>US$39.00</td></tr>
<tr><td>Franco-Nevada Corporation</td><td>NYSE/TSX: FNV</td><td>Gold royalties and streaming</td><td>Hold</td><td>US$250.00</td></tr></table>
<p style="font-size:7.8pt;color:#5A6B7C;margin-top:8pt">Ratings and targets as published October 27, 2026. Research and live coverage: kosherite.github.io/Northwall-Research</p></div></div>
<div class="front" style="page-break-before:always"><h1>Table of Contents</h1><ul class="tocl">{toc}</ul>
<div style="margin-left:1.85in;margin-top:16pt;font-weight:bold;font-size:8.6pt">Abbreviations and Units</div>{abbr_html}
<div class="conv">Conversions used throughout: 1 t = 32,150.7 oz; 1% Cu = 22.046 lb Cu per tonne of ore; 1 g/t Au = 0.03215 oz per tonne of ore.</div></div>'''

html = f'<!doctype html><html><head><meta charset="utf-8"><title>Metals &amp; Mining Made Simple - Northwall Research</title><style>{CSS}</style></head><body>{running}{cover}{about}<div class="body">{"".join(B)}</div></body></html>'
open('primer.html', 'w').write(html)
HTML('primer.html', base_url='.').write_pdf('Northwall_Research_Metals_and_Mining_Made_Simple.pdf')
print('built; exhibits:', kit.EX[0])
