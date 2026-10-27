"""Exhibits for the FNV company report v1.1, drawn at their printed size in the one-pager style."""
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib import font_manager as fm
for w in ['Regular', 'Bold']: fm.fontManager.addfont(f'/usr/share/fonts/truetype/liberation/LiberationSans-{w}.ttf')
NAVY = '#0F1A2B'; STEEL = '#2F5D7C'; SLATE = '#5A6B7C'; GRID = '#E6E9EC'; LIGHT = '#9DB3C6'
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 6.6, 'axes.edgecolor': SLATE, 'axes.labelcolor': SLATE,
                     'xtick.color': SLATE, 'ytick.color': SLATE, 'xtick.labelsize': 6.4, 'ytick.labelsize': 6.4})
m = json.load(open('model.json')); Y = m['y']; O = 'v11/'
def style(ax, grid='y'):
    for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.5)
    ax.tick_params(axis='y', length=0); ax.tick_params(axis='x', length=2)
    ax.grid(axis=grid, color=GRID, linewidth=0.5); ax.set_axisbelow(True)

# Exhibit: GEOs sold (sidebar, 2.45in)
yrs = ['24A', '25A', '26E', '27E', '28E', '29E', '30E']
geo = [463.3, 519.1, Y['2026']['geo'], Y['2027']['geo'], Y['2028']['geo'], Y['2029']['geo'], Y['2030']['geo']]
fig, ax = plt.subplots(figsize=(2.45, 1.85), dpi=300)
ax.bar(range(7), geo, width=0.62, color=[NAVY, NAVY] + [STEEL] * 5)
for i, v in enumerate(geo): ax.text(i, v + 10, f'{v:,.0f}', ha='center', fontsize=6, color=NAVY)
ax.set_xticks(range(7)); ax.set_xticklabels(yrs); ax.set_ylim(0, 690); ax.set_xlim(-0.55, 6.55); style(ax)
plt.subplots_adjust(left=0.12, right=0.99, top=0.97, bottom=0.12); plt.savefig(O + 'geo.png'); plt.close()

# Exhibit: Q2-26 revenue by commodity (sidebar)
lab = ['Gold', 'Silver', 'Oil, gas & NGL', 'PGM', 'Iron ore & other']; val = [403.0, 83.5, 70.4, 12.2, 11.8]
fig, ax = plt.subplots(figsize=(2.45, 1.45), dpi=300)
yy = np.arange(5)[::-1]
ax.barh(yy, val, height=0.56, color=[NAVY] + [STEEL] * 4)
for y, v in zip(yy, val): ax.text(v + 6, y, f'US${v:.0f}M · {v / 580.9 * 100:.0f}%', va='center', fontsize=6, color=NAVY)
ax.set_yticks(yy); ax.set_yticklabels(lab, color=NAVY); ax.set_xlim(0, 700); ax.set_xticks([])
for s in ['top', 'right', 'bottom']: ax.spines[s].set_visible(False)
ax.spines['left'].set_linewidth(0.5); ax.tick_params(axis='y', length=0)
plt.subplots_adjust(left=0.33, right=0.99, top=0.98, bottom=0.02); plt.savefig(O + 'mix.png'); plt.close()

# Exhibit: value vs long-term gold (half width 3.55in)
g = m['grid']; x = [r['lt'] for r in g]
fig, ax = plt.subplots(figsize=(3.55, 1.95), dpi=300)
ax.plot(x, [r['pt'] for r in g], color=NAVY, lw=1.6, marker='o', ms=3.2)
ax.plot(x, [r['navps'] for r in g], color=STEEL, lw=1.6, marker='o', ms=3.2)
ax.axhline(m['px'], color=SLATE, ls='--', lw=0.8)
for r in g: ax.text(r['lt'], r['pt'] + 9, f"{r['pt']:.0f}", ha='center', fontsize=6, color=NAVY)
ax.text(3020, m['px'] + 6, f"Share price US${m['px']:.2f}", fontsize=6, color=SLATE)
ax.text(4480, g[-1]['pt'] - 26, 'Implied value', fontsize=6.2, color=NAVY, ha='right', fontweight='bold')
ax.text(4480, g[-1]['navps'] + 9, 'NAVPS', fontsize=6.2, color=STEEL, ha='right', fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels([f'US${v:,}' for v in x]); ax.set_ylim(90, 320); ax.set_xlim(2900, 4600); style(ax)
plt.subplots_adjust(left=0.08, right=0.99, top=0.97, bottom=0.12); plt.savefig(O + 'val.png'); plt.close()

# Exhibit: valuation ranges (half width)
n = m['navps']; c = Y['2027']['cfps']
rows = [('52-week range', 181.50, 285.67), ('P/NAV 1.5x–2.5x', 1.5 * n, 2.5 * n), ('P/CF 2027E 20x–28x', 20 * c, 28 * c),
        ('Gold US$3,000–4,500', g[0]['pt'], g[-1]['pt']), ('Bear to bull case', m['bear'], m['bull'])]
fig, ax = plt.subplots(figsize=(3.55, 1.95), dpi=300)
for i, (l, a, b) in enumerate(rows[::-1]):
    ax.barh(i, b - a, left=a, height=0.48, color=STEEL)
    ax.text(a - 5, i, f'{a:.0f}', ha='right', va='center', fontsize=6, color=NAVY)
    ax.text(b + 5, i, f'{b:.0f}', ha='left', va='center', fontsize=6, color=NAVY)
ax.set_yticks(range(5)); ax.set_yticklabels([r[0] for r in rows[::-1]], color=NAVY)
ax.axvline(m['px'], color=SLATE, ls='--', lw=0.8); ax.axvline(250, color=NAVY, lw=1)
ax.text(m['px'] - 3, 4.55, f"Price {m['px']:.0f}", ha='right', fontsize=6, color=SLATE)
ax.text(253, 4.55, 'Target 250', ha='left', fontsize=6, color=NAVY, fontweight='bold')
ax.set_xlim(125, 395); ax.set_ylim(-0.6, 4.95); style(ax, 'x')
plt.subplots_adjust(left=0.30, right=0.99, top=0.98, bottom=0.11); plt.savefig(O + 'range.png'); plt.close()

# Exhibit: revenue and adjusted EBITDA (half width)
yy = ['2025', '2026', '2027', '2028', '2029', '2030']
rev = [Y[k]['rev'] for k in yy]; eb = [Y[k]['ebitda'] for k in yy]; mg = [Y[k]['margin'] * 100 for k in yy]
fig, ax = plt.subplots(figsize=(3.55, 2.25), dpi=300)
xi = np.arange(6); w = 0.36
ax.bar(xi - w / 2, rev, w, color=NAVY, label='Revenue'); ax.bar(xi + w / 2, eb, w, color=STEEL, label='Adj. EBITDA')
for i in range(6): ax.text(xi[i], rev[i] + 45, f'{mg[i]:.0f}%', ha='center', fontsize=6, color=SLATE)
ax.set_xticks(xi); ax.set_xticklabels(['2025A', '2026E', '2027E', '2028E', '2029E', '2030E']); ax.set_ylim(0, 2850)
ax.legend(frameon=False, loc='upper right', ncol=2, fontsize=6, handlelength=1, bbox_to_anchor=(1, 1.04)); style(ax)
plt.subplots_adjust(left=0.10, right=0.99, top=0.97, bottom=0.12); plt.savefig(O + 'rev.png'); plt.close()
print('charts ok')
