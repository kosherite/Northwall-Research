#!/usr/bin/env python3
"""Render a company note (one-pager) PDF in the Northwall house layout.

    python tools/build_onepager.py AGI            # writes reports/drafts/<date>_AGI_OnePager_v0.1.pdf
    python tools/build_onepager.py AGI --final    # writes reports/published/<date>_AGI_OnePager_v1.0.pdf

The rating box (rating, price, target, implied return) is read from coverage/<T>/outputs.json,
which the model build writes. Narrative and exhibits come from reports/<T>/onepager.yaml.
Run tools/check_report.py first: it fails if the narrative quotes a target or return the model does not.
"""
import sys, json
from pathlib import Path
import yaml
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
CCY = {'USD': 'USD', 'CAD': 'CAD'}


def render(t, final=False):
    rep = yaml.safe_load(open(ROOT / 'reports' / t / 'onepager.yaml'))
    out = json.load(open(ROOT / 'coverage' / t / 'outputs.json'))
    cfg = yaml.safe_load(open(ROOT / 'coverage' / t / 'model_inputs.yaml'))
    ccy = CCY[cfg['company']['price_ccy']]
    css = open(ROOT / 'reports' / 'templates' / 'onepager.css').read()
    mark = open(ROOT / 'reports' / 'templates' / 'logo_mark.svg').read()
    ex = rep['exhibits']
    def exhibit(i, e):
        body = f'<img src="{e["image"]}">' if 'image' in e else e['html']
        return f'<div class="ex"><div class="ext">Exhibit {i} - {e["title"]}</div>{body}<div class="src">{e["source"]}</div></div>'
    html = f'''<!doctype html><html><head><meta charset="utf-8"><title>{rep['name']} — Northwall Research</title>
<style>{css}</style></head><body>
<div class="top"><div><div class="logo"><div>{mark}</div><div><div class="w1">NORTHWALL</div><div class="w2">RESEARCH</div></div></div></div>
<div class="tr">{rep['sector']}</div></div>
<div class="id"><div class="idl"><div class="co">{rep['name']}<br>({rep['listing']})</div>
<div class="who">{rep['analyst']} (Analyst), Northwall Research<br><span>{rep['date_long']}</span></div></div>
<div><div class="box"><table>
<tr><td><div class="bl">Rating</div><div class="bv">{out['rating']}</div></td><td><div class="bl">Closing price</div><div class="bv">{ccy} {out['price']:,.2f}</div></td></tr>
<tr><td><div class="bl">Price target</div><div class="bv">{ccy} {out['target']:,.2f}</div></td><td><div class="bl">Implied all-in return</div><div class="bv">{out['ret_all'] * 100:.1f}%</div></td></tr>
</table></div></div></div>
<div class="cols"><div class="c1"><h2>Investment summary</h2>{rep['summary']}</div>
<div class="c2"><h2>Valuation</h2>{rep['valuation']}<h2 style="margin-top:12px">Risks to rating and price target</h2>{rep['risks']}</div></div>
<div class="cols cols2"><div class="c1">{exhibit(1, ex[0])}</div><div class="c2">{exhibit(2, ex[1])}{exhibit(3, ex[2])}
<div class="disc">Ratings: Buy, expected 12-month total return above 15%; Hold, 0–15%; Sell, below 0%. Facts are from company filings; estimates, target and rating are Northwall Research opinions. The analyst certifies these views are their own. Not investment advice.</div>
</div></div>
<div class="foot"><div style="width:1.1in">{rep['date_long']}</div><div style="text-align:right">1</div></div>
</body></html>'''
    folder = ROOT / 'reports' / ('published' if final else 'drafts'); folder.mkdir(parents=True, exist_ok=True)
    name = f"{rep['date']}_{t}_OnePager_{'v1.0' if final else 'v0.1'}.pdf"
    tmp = ROOT / 'reports' / t / '_render.html'
    tmp.write_text(html.replace("url('fonts/", f"url('{(ROOT / 'reports' / 'templates' / 'fonts').as_uri()}/"))
    HTML(str(tmp), base_url=str(ROOT / 'reports' / t)).write_pdf(folder / name)
    tmp.unlink()
    print(f"  wrote {(folder / name).relative_to(ROOT)}")


if __name__ == '__main__':
    final = '--final' in sys.argv
    for t in [a for a in sys.argv[1:] if not a.startswith('--')]:
        render(t, final)
