"""Northwall sector note builder: research-note front page, then the primer's house layout."""
import re, sys, importlib
sys.path.insert(0, '/home/claude/primer')
from weasyprint import HTML

PRIMER_CSS = re.search(r"CSS = '''(.*?)'''", open('/home/claude/primer/build.py').read(), re.S).group(1)
MARK = '''<svg width="{s}" height="{s}" viewBox="0 0 36 36"><rect x="3" y="11" width="8" height="23" fill="#2F5D7C"/><rect x="14" y="2" width="8" height="32" fill="{c}"/><rect x="25" y="11" width="8" height="23" fill="#2F5D7C"/></svg>'''

EXTRA = '''
@page :first { margin-top: 0.45in; @top-left { content: none; } }
.fp-top { display: table; width: 7.3in; border-bottom: 0.8pt solid #0F1A2B; padding-bottom: 7pt; }
.fp-top > div { display: table-cell; vertical-align: bottom; }
.fp-top .w1 { font-family: 'Pal'; font-weight: bold; font-size: 13pt; letter-spacing: 4px; line-height: 1; padding-left: 8px; }
.fp-top .w2 { font-size: 6.4pt; letter-spacing: 5.3px; color: #5A6B7C; padding-left: 8px; margin-top: 2px; }
.fp-top .r { text-align: right; font-size: 7.8pt; letter-spacing: 1.5px; } .fp-top .r b { color: #2F5D7C; }
.fp-title { margin: 12pt 0 4pt; } .fp-title h1 { font-family: 'Pal'; font-size: 21pt; line-height: 1.12; margin: 0; color: #0F1A2B; }
.fp-title .sub { font-family: 'Pal'; font-size: 11.5pt; color: #2F5D7C; margin-top: 4pt; line-height: 1.35; }
.fp-who { font-size: 8pt; margin: 6pt 0 10pt; } .fp-who span { color: #5A6B7C; }
.fp { display: table; width: 7.3in; table-layout: fixed; } .fp .l { display: table-cell; width: 4.55in; padding-right: 0.22in; vertical-align: top; }
.fp .r { display: table-cell; width: 2.75in; vertical-align: top; border-left: 0.8pt solid #C9CFD6; padding-left: 0.16in; }
.fp p { font-size: 8.7pt; } .fp h2 { margin-top: 8pt; }
.kp { margin: 0; padding: 0; list-style: none; } .kp li { margin: 0 0 6pt; padding-left: 0; font-size: 8.7pt; text-align: justify; }
.kp li b.n { color: #2F5D7C; }
.side-t { font-size: 8.2pt; font-weight: bold; color: #2F5D7C; margin: 0 0 3pt; }
table.cv { width: 100%; border-collapse: collapse; font-size: 7.4pt; margin-bottom: 9pt; }
table.cv th { font-size: 6.6pt; text-align: right; border-bottom: 0.8pt solid #0F1A2B; padding: 1pt 2pt 2pt; color: #5A6B7C; }
table.cv td { text-align: right; padding: 3pt 2pt; border-bottom: 0.5pt solid #DCE2E8; }
table.cv th:first-child, table.cv td:first-child { text-align: left; } table.cv .Buy { color: #2E7D5B; font-weight: bold; } table.cv .Hold { color: #A86A12; font-weight: bold; }
.fp .ex { margin: 4pt 0 6pt; } .fp .ex img { width: 100%; }
.disc-mini { font-size: 6pt; color: #5A6B7C; line-height: 1.35; border-top: 0.5pt solid #DCE2E8; padding-top: 4pt; margin-top: 6pt; text-align: justify; }
.alert { background: #F6E3E1; border-left: 3pt solid #B5473A; padding: 7pt 10pt 3pt; margin: 8pt 0 10pt; page-break-inside: avoid; }
.alert .bt { font-weight: bold; color: #B5473A; font-size: 8.8pt; margin-bottom: 3pt; } .alert p { font-size: 8.5pt; }
.co-h { display: table; width: 100%; border-bottom: 0.8pt solid #0F1A2B; padding-bottom: 3pt; margin: 14pt 0 6pt; page-break-after: avoid; }
.co-h > div { display: table-cell; vertical-align: bottom; } .co-h .n { font-family: 'Pal'; font-size: 12pt; font-weight: bold; width: 62%; } .co-h .t { text-align: right; font-size: 7.8pt; white-space: nowrap; }
.co-h .t b { color: #2F5D7C; }
'''


def build(mod_name, out_pdf, sector, short, date_long='October 28, 2026'):
    import kit
    kit.B.clear(); kit.TOC.clear(); kit.EX[0] = 0
    mod = importlib.import_module(mod_name)
    front = mod.FRONT
    run = f'''<div id="hl" class="run"><span>{date_long}</span><span class="r">{short}</span></div>
<div id="hr" class="run"><span>{short}</span><span class="r">{date_long}</span></div>
<div id="fl" class="foot"><span><span class="pg"></span>&nbsp;&nbsp; Northwall Research &nbsp;|&nbsp; {sector}</span><span style="text-align:right"><span class="lk">{MARK.format(s=12, c="#0F1A2B")}NORTHWALL RESEARCH</span></span></div>
<div id="fr" class="foot"><span><span class="lk">{MARK.format(s=12, c="#0F1A2B")}NORTHWALL RESEARCH</span></span><span style="text-align:right">Northwall Research &nbsp;|&nbsp; {sector} &nbsp;&nbsp;<span class="pg"></span></span></div>'''
    top = f'''<div class="fp-top"><div><table style="border-collapse:collapse"><tr><td>{MARK.format(s=30, c="#0F1A2B")}</td><td><div class="w1">NORTHWALL</div><div class="w2">RESEARCH</div></td></tr></table></div>
<div class="r">SECTOR NOTE &nbsp;|&nbsp; <b>{sector.upper()}</b><br><span style="letter-spacing:0.5px">{date_long}</span></div></div>'''
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{short} - Northwall Research</title><style>{PRIMER_CSS}{EXTRA}</style></head><body>{run}{top}{front}
<div class="body" style="page-break-before:always">{"".join(kit.B)}</div></body></html>'''
    open(out_pdf.replace('.pdf', '.html'), 'w').write(html)
    HTML(out_pdf.replace('.pdf', '.html'), base_url='/home/claude/sector/').write_pdf(out_pdf)
    print('built', out_pdf, 'exhibits', kit.EX[0])


if __name__ == '__main__':
    which = sys.argv[1]
    if which == 'mm': build('mm', '/home/claude/sector/Northwall_Research_Metals_Mining_Sector_Note.pdf', 'Metals & Mining', 'Metals &amp; Mining Sector Note')
    else: build('og', '/home/claude/sector/Northwall_Research_Oil_Gas_Sector_Note.pdf', 'Oil & Gas', 'Oil &amp; Gas Sector Note')
