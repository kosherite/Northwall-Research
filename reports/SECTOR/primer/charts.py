"""Charts and diagrams for Metals & Mining Made Simple (Northwall Research), drawn at print size."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon as MPoly, Rectangle, FancyArrowPatch
from matplotlib import font_manager as fm
for w in ['Regular', 'Bold']: fm.fontManager.addfont(f'/usr/share/fonts/truetype/liberation/LiberationSans-{w}.ttf')
NAVY = '#0F1A2B'; STEEL = '#2F5D7C'; SLATE = '#5A6B7C'; LIGHT = '#9DB3C6'; PALE = '#E9EEF2'; GRID = '#E6E9EC'; AMBER = '#C98A12'; TEAL = '#3E8E7E'
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 6.8, 'axes.edgecolor': SLATE, 'axes.labelcolor': SLATE, 'xtick.color': SLATE, 'ytick.color': SLATE,
                     'xtick.labelsize': 6.5, 'ytick.labelsize': 6.5, 'axes.titlesize': 7, 'text.parse_math': False})
O = '/home/claude/primer/img/'; MAIN = 5.45; FULL = 7.3


def style(ax, grid='y'):
    for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.5); ax.tick_params(axis='y', length=0); ax.tick_params(axis='x', length=2)
    if grid: ax.grid(axis=grid, color=GRID, linewidth=0.5); ax.set_axisbelow(True)


def box(ax, x, y, w, h, title, body='', fc='white', ec=STEEL, tc=NAVY, lw=0.8, fs=6.8, r=0.02):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}', fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h - 0.035 if body else y + h / 2, title, ha='center', va='top' if body else 'center', fontsize=fs, fontweight='bold', color=tc)
    if body: ax.text(x + w / 2, y + h - 0.105, body, ha='center', va='top', fontsize=fs - 0.8, color=SLATE if fc == 'white' else tc, linespacing=1.35)


def arrow(ax, x0, y0, x1, y1, c=SLATE, lw=0.8):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=6, color=c, lw=lw))


def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=300); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_axis_off(); return fig, ax


# 1. Value chain
fig, ax = canvas(MAIN, 1.45)
st = [('Exploration', 'Map, sample,\ndrill, model'), ('Development', 'Studies, permits,\nconstruction'), ('Mining', 'Drill, blast,\nload and haul'),
      ('Processing', 'Crush, grind,\nconcentrate, leach'), ('Refining', 'Smelt and refine\nto pure metal'), ('End use', 'Wire, steel,\nbatteries, jewellery')]
w = 0.148; g = (1 - 6 * w) / 5
for i, (t, b) in enumerate(st):
    x = i * (w + g); box(ax, x, 0.38, w, 0.58, t, b, fc=PALE if i < 4 else 'white', ec=STEEL if i < 4 else LIGHT)
    if i < 5: arrow(ax, x + w + 0.002, 0.67, x + w + g - 0.002, 0.67)
seg = [(0, 3, 'Upstream: explorers, developers and producers', STEEL, 'white'), (4, 4, 'Midstream', LIGHT, NAVY), (5, 5, 'Downstream', PALE, NAVY)]
for a, b, t, fc, tc in seg:
    x0 = a * (w + g); x1 = b * (w + g) + w
    ax.add_patch(FancyBboxPatch((x0, 0.04), x1 - x0, 0.2, boxstyle='round,pad=0,rounding_size=0.02', fc=fc, ec='none'))
    ax.text((x0 + x1) / 2, 0.14, t, ha='center', va='center', fontsize=6.6, fontweight='bold', color=tc)
fig.savefig(O + 'value_chain.png'); plt.close(fig)

# 2. Resource and reserve classification (CIM / CRIRSCO)
fig, ax = canvas(MAIN, 2.55)
ax.text(0.17, 0.95, 'Mineral Resources', ha='center', fontsize=7.4, fontweight='bold', color=NAVY)
ax.text(0.71, 0.95, 'Mineral Reserves', ha='center', fontsize=7.4, fontweight='bold', color=NAVY)
box(ax, 0.02, 0.06, 0.3, 0.22, 'Inferred', 'Limited drilling; continuity\nassumed, not verified', fc='#F3F5F7', ec=LIGHT)
box(ax, 0.02, 0.33, 0.3, 0.22, 'Indicated', 'Drilling adequate to\nassume continuity', fc=PALE, ec=LIGHT)
box(ax, 0.02, 0.60, 0.3, 0.22, 'Measured', 'Close-spaced drilling;\ncontinuity confirmed', fc=LIGHT, ec=STEEL)
box(ax, 0.56, 0.33, 0.3, 0.22, 'Probable', 'Mine plan from Indicated\n(or Measured) resources', fc=PALE, ec=STEEL)
box(ax, 0.56, 0.60, 0.3, 0.22, 'Proven', 'Mine plan from Measured\nresources', fc=STEEL, ec=STEEL, tc='white')
for y0, y1 in [(0.44, 0.44), (0.71, 0.71)]: arrow(ax, 0.325, y0, 0.555, y1, c=NAVY, lw=1)
arrow(ax, 0.325, 0.68, 0.555, 0.47, c=NAVY, lw=0.6)
ax.text(0.44, 0.585, 'Modifying\nfactors', ha='center', va='center', fontsize=6.4, color=NAVY, fontweight='bold', bbox=dict(fc='white', ec='none', pad=1))
ax.text(0.44, 0.17, 'Mining, processing,\nmetallurgy, economics,\nmarketing, legal,\nenvironmental, social,\ngovernment', ha='center', va='center', fontsize=5.8, color=SLATE, linespacing=1.3)
ax.annotate('', xy=(0.94, 0.86), xytext=(0.94, 0.06), arrowprops=dict(arrowstyle='-|>', color=SLATE, lw=0.8))
ax.text(0.965, 0.46, 'Increasing geological knowledge and confidence', rotation=90, ha='center', va='center', fontsize=6, color=SLATE)
fig.savefig(O + 'classification.png'); plt.close(fig)

# 3. Mining methods cross-section (illustrative)
fig, ax = canvas(FULL, 2.7)
ax.add_patch(Rectangle((0, 0), 1, 0.78, fc='#EEF0EC', ec='none'))
ax.add_patch(Rectangle((0, 0.78), 1, 0.22, fc='white', ec='none'))
ax.plot([0, 1], [0.78, 0.78], color='#8C9A86', lw=1.2)
# open pit with benches
xs = [0.03, 0.06, 0.06, 0.09, 0.09, 0.12, 0.12, 0.15, 0.15, 0.25, 0.25, 0.28, 0.28, 0.31, 0.31, 0.34, 0.34, 0.37]
ys = [0.78, 0.78, 0.70, 0.70, 0.62, 0.62, 0.54, 0.54, 0.46, 0.46, 0.54, 0.54, 0.62, 0.62, 0.70, 0.70, 0.78, 0.78]
ax.add_patch(MPoly(list(zip(xs, ys)), closed=True, fc='white', ec='#8C9A86', lw=0.8))
ax.add_patch(MPoly([(0.11, 0.62), (0.29, 0.62), (0.27, 0.30), (0.13, 0.30)], fc=AMBER, alpha=0.55, ec='none'))
ax.text(0.2, 0.86, 'Open pit', ha='center', fontsize=7.4, fontweight='bold', color=NAVY)
ax.text(0.2, 0.37, 'Near-surface,\nlower-grade orebody', ha='center', fontsize=5.8, color=NAVY)
ax.annotate('Benches 10–15 m', (0.075, 0.70), xytext=(0.0, 0.58), fontsize=5.8, color=SLATE, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.annotate('Waste stripped', (0.33, 0.70), xytext=(0.36, 0.60), fontsize=5.8, color=SLATE, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
# underground: shaft + decline + stopes
ax.add_patch(Rectangle((0.5, 0.08), 0.012, 0.70, fc=NAVY))
ax.add_patch(Rectangle((0.493, 0.78), 0.026, 0.12, fc='white', ec=NAVY, lw=0.8)); ax.text(0.506, 0.92, 'Headframe', ha='center', fontsize=5.8, color=NAVY)
for y in [0.62, 0.48, 0.34, 0.20]: ax.add_patch(Rectangle((0.512, y), 0.16, 0.012, fc=NAVY))
ax.add_patch(MPoly([(0.62, 0.70), (0.66, 0.70), (0.70, 0.12), (0.66, 0.12)], fc=AMBER, alpha=0.55, ec='none'))
for y in [0.48, 0.34]: ax.add_patch(Rectangle((0.633, y - 0.075), 0.045, 0.075, fc='white', ec=SLATE, lw=0.5, hatch='////'))
ax.text(0.585, 0.86, 'Underground', ha='center', fontsize=7.4, fontweight='bold', color=NAVY)
ax.annotate('Shaft (ore hoisted in skips)', (0.506, 0.40), xytext=(0.38, 0.22), fontsize=5.8, color=SLATE, ha='center', arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.annotate('Levels and drifts', (0.56, 0.625), xytext=(0.54, 0.70), fontsize=5.8, color=SLATE, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.annotate('Long-hole stopes,\nbackfilled after mining', (0.655, 0.27), xytext=(0.53, 0.09), fontsize=5.8, color=SLATE, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.text(0.71, 0.75, 'Narrow, steep,\nhigh-grade vein', ha='center', fontsize=5.8, color=NAVY)
# block cave
ax.add_patch(MPoly([(0.80, 0.78), (0.95, 0.78), (0.93, 0.70), (0.82, 0.70)], fc='white', ec='#8C9A86', lw=0.8))
ax.text(0.875, 0.86, 'Block cave', ha='center', fontsize=7.4, fontweight='bold', color=NAVY)
ax.add_patch(MPoly([(0.80, 0.62), (0.95, 0.62), (0.95, 0.22), (0.80, 0.22)], fc=AMBER, alpha=0.35, ec='none'))
ax.add_patch(MPoly([(0.82, 0.70), (0.93, 0.70), (0.95, 0.30), (0.80, 0.30)], fc='#D8D2C2', ec=SLATE, lw=0.4, hatch='..'))
ax.add_patch(Rectangle((0.79, 0.20), 0.17, 0.02, fc=NAVY)); ax.add_patch(Rectangle((0.775, 0.20), 0.008, 0.58, fc=NAVY))
ax.annotate('Caved zone\ncollapses under\ngravity', (0.87, 0.48), xytext=(0.965, 0.55), fontsize=5.8, color=SLATE, ha='left', arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.text(0.875, 0.12, 'Drawpoints on the\nextraction level', ha='center', fontsize=5.8, color=NAVY)
ax.text(0.875, 0.02, 'Large, low-grade porphyry at depth', ha='center', fontsize=5.8, color=NAVY)
ax.set_xlim(-0.01, 1.07)
fig.savefig(O + 'mining_methods.png'); plt.close(fig)

# 4. Processing flowsheet
fig, ax = canvas(FULL, 2.45)
def node(x, y, t, fc='white', ec=STEEL, w=0.115, h=0.17, tc=NAVY):
    box(ax, x - w / 2, y - h / 2, w, h, t, fc=fc, ec=ec, tc=tc, fs=6.4)
rows = [('Sulphide copper (flotation)', 0.80, ['Run-of-mine\nore', 'Crushing', 'SAG and\nball mills', 'Froth\nflotation', 'Concentrate\n20–40% Cu', 'Smelter', 'Refinery', 'Cathode\n99.99% Cu']),
        ('Free-milling gold (CIL)', 0.47, ['Run-of-mine\nore', 'Crushing', 'Grinding', 'Cyanide leach\nand carbon', 'Elution and\nelectrowinning', 'Doré bars', 'Refinery', 'Bullion\n99.99% Au']),
        ('Oxide copper and low-grade gold (heap leach)', 0.14, ['Run-of-mine\nore', 'Crushing', 'Heap leach\npads', 'Pregnant\nsolution', 'SX-EW (Cu)\nor carbon (Au)', 'Cathode or\ndoré', '', ''])]
xs = np.linspace(0.07, 0.93, 8)
for label, y, steps in rows:
    ax.text(0.005, y + 0.13, label, fontsize=6.6, fontweight='bold', color=STEEL)
    last = None
    for i, s in enumerate(steps):
        if not s: continue
        fc = PALE if i in (3, 4) else ('white' if i < 5 else '#F3F5F7')
        if s.startswith(('Cathode', 'Bullion')): fc = STEEL
        node(xs[i], y, s, fc=fc, tc='white' if fc == STEEL else NAVY, ec=STEEL if i < 5 else LIGHT)
        if last is not None: arrow(ax, xs[last] + 0.058, y, xs[i] - 0.058, y)
        last = i
ax.add_patch(Rectangle((xs[4] + 0.06, 0.02), 0.002, 0.93, fc=LIGHT)); ax.set_ylim(0, 1.07)
ax.text(xs[4] + 0.07, 1.06, 'Usually off site: smelters and refiners →', fontsize=6, color=SLATE, va='top')
ax.text(xs[4] + 0.05, 1.06, '← Mine site: concentrator or leach plant', fontsize=6, color=SLATE, va='top', ha='right')
fig.savefig(O + 'flowsheet.png'); plt.close(fig)

# 5. NSR waterfall (worked example)
fig, ax = plt.subplots(figsize=(MAIN, 2.1), dpi=300)
items = [('Gross payable\nvalue', 3961, 'tot'), ('Treatment\ncharge', -25, 'd'), ('Refining\ncharge', -15, 'd'), ('Freight and\ninsurance', -60, 'd'), ('Net smelter\nreturn', 3861, 'tot')]
cum = 0
for i, (l, v, k) in enumerate(items):
    if k == 'tot':
        ax.bar(i, v, 0.55, color=STEEL if i == 0 else NAVY); cum = v; ax.text(i, v + 10, f'{v:,}', ha='center', fontsize=6.6, color=NAVY, fontweight='bold')
    else:
        ax.bar(i, -v, 0.55, bottom=cum + v, color=AMBER); ax.text(i, cum + 10, f'({-v})', ha='center', fontsize=6.6, color=NAVY); cum += v
ax.set_xticks(range(5)); ax.set_xticklabels([x[0] for x in items]); ax.set_ylim(3700, 4020); style(ax)
ax.set_ylabel('US$ per dry tonne of concentrate')
plt.subplots_adjust(left=0.1, right=0.99, top=0.96, bottom=0.2); fig.savefig(O + 'nsr.png'); plt.close(fig)

# 6. Gold and copper prices, annual averages
yrs = list(range(2010, 2026))
gold = [1224.52, 1571.52, 1668.98, 1411.23, 1266.40, 1160.06, 1250.80, 1257.15, 1268.49, 1392.60, 1769.64, 1798.61, 1800.09, 1940.54, 2386.20, 3431.50]
cu = [7535, 8828, 7962, 7332, 6863, 5510, 4868, 6170, 6530, 6010, 6181, 9317, 8822, 8478, 9147, 9921]
fig, axs = plt.subplots(1, 2, figsize=(FULL, 2.2), dpi=300)
for ax, data, spot, col, ttl, unit, fmt in [(axs[0], gold, 4076, AMBER, 'Gold, LBMA annual average', 'US$/oz', '{:,.0f}'), (axs[1], cu, 14680, STEEL, 'Copper, annual average', 'US$/t', '{:,.0f}')]:
    ax.fill_between(yrs, data, color=col, alpha=0.12, lw=0); ax.plot(yrs, data, color=col, lw=1.6)
    ax.scatter([2026.8], [spot], s=22, color=NAVY, zorder=5); ax.plot([2025, 2026.8], [data[-1], spot], color=NAVY, lw=0.8, ls=(0, (2, 2)))
    ax.annotate(f'Oct 27, 2026\nspot {fmt.format(spot)}', (2026.8, spot), xytext=(-6, 0), textcoords='offset points', ha='right', va='center', fontsize=6, color=NAVY)
    ax.annotate(f'2025: {fmt.format(data[-1])}', (2025, data[-1]), xytext=(-5, 4), textcoords='offset points', ha='right', fontsize=6, color=NAVY)
    ax.set_title(f'{ttl} ({unit})', loc='left', color=NAVY, fontweight='bold', fontsize=7); ax.set_xlim(2009.5, 2027.5); ax.set_ylim(0, max(spot, max(data)) * 1.15); style(ax)
    ax.set_xticks([2010, 2014, 2018, 2022, 2026])
plt.subplots_adjust(left=0.07, right=0.99, top=0.88, bottom=0.11, wspace=0.18); fig.savefig(O + 'prices.png'); plt.close(fig)

# 7. Gold supply and demand, WGC 2024 vs 2025
fig, ax = plt.subplots(figsize=(MAIN, 2.3), dpi=300)
cats = ['Jewellery', 'Technology', 'Bar and coin', 'ETFs', 'Central banks', 'OTC and other']
v24 = [2026.6, 326.2, 1188.3, -2.9, 1092.4, 331.3]; v25 = [1638.0, 322.8, 1374.1, 801.2, 863.3, 2.9]
y = np.arange(len(cats))[::-1]
ax.barh(y + 0.19, v24, 0.36, color=LIGHT, label='2024'); ax.barh(y - 0.19, v25, 0.36, color=AMBER, label='2025')
for yy, a, b in zip(y, v24, v25):
    ax.text(max(a, 0) + 20, yy + 0.19, f'{a:,.0f}', va='center', fontsize=6, color=SLATE); ax.text(max(b, 0) + 20, yy - 0.19, f'{b:,.0f}', va='center', fontsize=6, color=NAVY, fontweight='bold')
ax.set_yticks(y); ax.set_yticklabels(cats, color=NAVY); ax.set_xlim(-60, 2350); style(ax, 'x'); ax.set_xlabel('Tonnes')
ax.legend(frameon=False, fontsize=6.4, loc='lower right')
plt.subplots_adjust(left=0.17, right=0.98, top=0.98, bottom=0.15); fig.savefig(O + 'gold_demand.png'); plt.close(fig)

# 8. Illustrative AISC cost curve
rng = np.random.default_rng(7)
n = 60; prod = rng.uniform(150, 900, n); cost = np.sort(rng.normal(1650, 420, n).clip(850, 2900))
cost[-4:] = [2650, 2850, 3100, 3350]
fig, ax = plt.subplots(figsize=(MAIN, 2.3), dpi=300)
x = 0; tot = prod.sum(); q = [tot * k / 4 for k in (1, 2, 3)]
for p_, c in zip(prod, cost):
    col = TEAL if x < q[0] else STEEL if x < q[1] else LIGHT if x < q[2] else AMBER
    ax.bar(x + p_ / 2, c, p_, color=col, ec='white', lw=0.3); x += p_
ax.axhline(4076, color=NAVY, lw=0.9, ls='--'); ax.text(tot * 0.01, 4130, 'Gold spot US$4,076/oz', fontsize=6.2, color=NAVY)
ax.axhline(2600, color=SLATE, lw=0.7, ls=':'); ax.text(tot * 0.01, 2650, '90th percentile: the long-run floor', fontsize=6.2, color=SLATE)
for i, (lab, col) in enumerate([('1st quartile', TEAL), ('2nd', STEEL), ('3rd', LIGHT), ('4th', AMBER)]):
    ax.add_patch(Rectangle((tot * (0.50 + i * 0.125), 3650), tot * 0.02, 120, color=col)); ax.text(tot * (0.525 + i * 0.125), 3710, lab, fontsize=6, color=NAVY, va='center')
ax.set_xlim(0, tot); ax.set_ylim(0, 4500); ax.set_xlabel('Cumulative production (koz)'); ax.set_ylabel('AISC (US$/oz)'); style(ax)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'{v / 1000:,.0f},000' if v else '0'))
plt.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.17); fig.savefig(O + 'cost_curve.png'); plt.close(fig)

# 9. AISC build (worked example)
fig, ax = plt.subplots(figsize=(MAIN, 2.1), dpi=300)
steps = [('Mining,\nprocessing,\nsite G&A', 1000), ('Royalties\nand taxes', 200), ('By-product\ncredits', -40), ('Cash\ncost', None), ('Sustaining\ncapital', 300),
         ('Exploration,\nreclamation', 60), ('Corporate\nG&A', 80), ('AISC', None), ('Growth\ncapital', 240), ('AIC', None)]
cum = 0
for i, (l, v) in enumerate(steps):
    if v is None:
        ax.bar(i, cum, 0.6, color=NAVY if l != 'Cash\ncost' else STEEL); ax.text(i, cum + 40, f'{cum:,}', ha='center', fontsize=6.6, fontweight='bold', color=NAVY)
    else:
        b = cum if v > 0 else cum + v
        ax.bar(i, abs(v), 0.6, bottom=b, color=LIGHT if v > 0 else AMBER); ax.text(i, cum + max(v, 0) + 40, f'{v:+,}', ha='center', fontsize=6.2, color=SLATE); cum += v
ax.set_xticks(range(len(steps))); ax.set_xticklabels([s[0] for s in steps], fontsize=5.6); ax.set_ylim(0, 2100); ax.set_ylabel('US$/oz on 250 koz sold'); style(ax)
plt.subplots_adjust(left=0.09, right=0.99, top=0.97, bottom=0.24); fig.savefig(O + 'aisc.png'); plt.close(fig)

# 10. Operating leverage
gp = np.linspace(3000, 5000, 41)
def margin(p, aisc_ex):  # AISC rises with royalties at 5% of revenue
    return p - (aisc_ex + 0.05 * p)
fig, ax = plt.subplots(figsize=(MAIN, 2.15), dpi=300)
for aisc, col, lab in [(1400, STEEL, 'Low-cost producer (AISC US$1,600 at US$4,000)'), (2800, AMBER, 'High-cost producer (AISC US$3,000 at US$4,000)')]:
    m0 = margin(4000, aisc); ch = (margin(gp, aisc) / m0 - 1) * 100
    ax.plot((gp / 4000 - 1) * 100, ch, color=col, lw=1.8, label=lab)
ax.plot((gp / 4000 - 1) * 100, (gp / 4000 - 1) * 100, color=SLATE, lw=0.8, ls='--', label='Gold price')
ax.axhline(0, color=SLATE, lw=0.5); ax.axvline(0, color=SLATE, lw=0.5)
ax.set_xlabel('Change in gold price from US$4,000/oz (%)'); ax.set_ylabel('Change in margin (%)'); ax.set_ylim(-110, 110); style(ax, 'both')
ax.legend(frameon=False, fontsize=6.2, loc='upper left')
plt.subplots_adjust(left=0.1, right=0.99, top=0.97, bottom=0.18); fig.savefig(O + 'leverage.png'); plt.close(fig)

# 11. Lassonde curve
fig, ax = plt.subplots(figsize=(MAIN, 2.3), dpi=300)
t = np.linspace(0, 10, 400)
from scipy.interpolate import PchipInterpolator
v = PchipInterpolator([0, 1, 2.1, 3.2, 4.4, 5.6, 7.0, 8.6, 10], [0.08, 0.3, 0.98, 0.55, 0.3, 0.36, 0.68, 0.8, 0.68])(t)
ax.plot(t, v, color=STEEL, lw=2)
stages = [(0, 'Concept'), (1.2, 'Discovery'), (3.0, 'Studies'), (4.6, 'Permitting'), (6.0, 'Construction'), (7.6, 'Production')]
for x0, s in stages: ax.axvline(x0, color=GRID, lw=0.6); ax.text(x0 + 0.08, -0.08, s, fontsize=6.2, color=SLATE, va='top')
ax.annotate('Speculative peak on discovery', (2.1, 0.98), xytext=(2.6, 1.08), fontsize=6.3, color=NAVY, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.annotate('Orphan period: value sags', (4.4, 0.30), xytext=(4.9, 0.12), fontsize=6.3, color=NAVY, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.annotate('Re-rating as cash flow starts', (7.8, 0.68), xytext=(7.4, 0.95), fontsize=6.3, color=NAVY, arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4))
ax.axvspan(3.4, 5.6, color=AMBER, alpha=0.08, lw=0); ax.text(4.5, 0.62, 'Where majors\nbuy juniors', ha='center', fontsize=6, color=AMBER, fontweight='bold')
ax.set_xlim(0, 10); ax.set_ylim(-0.02, 1.2); ax.set_yticks([]); ax.set_xticks([]); ax.set_ylabel('Company value', fontsize=6.6)
for s in ['top', 'right']: ax.spines[s].set_visible(False)
ax.spines['left'].set_linewidth(0.5); ax.spines['bottom'].set_linewidth(0.5)
plt.subplots_adjust(left=0.05, right=0.99, top=0.97, bottom=0.1); fig.savefig(O + 'lassonde.png'); plt.close(fig)

# 12. Project timeline Gantt (typical Canadian gold project)
tasks = [('Grassroots exploration', 0, 3, LIGHT), ('Discovery and delineation drilling', 2, 6, LIGHT), ('First resource estimate', 4.5, 5, AMBER),
         ('Preliminary economic assessment', 5, 6.5, STEEL), ('Pre-feasibility study', 6.5, 8, STEEL), ('Feasibility study', 8, 9.5, STEEL),
         ('Environmental assessment and permits', 6.5, 11, NAVY), ('Indigenous and community agreements', 6, 11, NAVY), ('Financing', 9.5, 11, STEEL),
         ('Construction decision', 11, 11.25, AMBER), ('Construction', 11, 13.5, NAVY), ('Commissioning and ramp-up', 13.5, 14.5, STEEL), ('Commercial production', 14.5, 20, TEAL)]
fig, ax = plt.subplots(figsize=(FULL, 2.6), dpi=300)
for i, (n_, a, b, c) in enumerate(tasks):
    y = len(tasks) - 1 - i
    if b - a < 0.4: ax.scatter([a], [y], marker='D', s=26, color=c, zorder=4)
    else: ax.barh(y, b - a, left=a, height=0.55, color=c)
    ax.text(-0.2, y, n_, ha='right', va='center', fontsize=6.3, color=NAVY)
    if i % 2 == 0: ax.axhspan(y - 0.5, y + 0.5, color='#F5F6F8', zorder=0, lw=0)
ax.set_xlim(0, 20); ax.set_ylim(-0.6, len(tasks) - 0.4); ax.set_yticks([]); ax.set_xticks(range(0, 21, 2)); ax.set_xlabel('Years from first exploration')
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5); ax.grid(axis='x', color=GRID, lw=0.5); ax.set_axisbelow(True)
plt.subplots_adjust(left=0.29, right=0.99, top=0.98, bottom=0.14); fig.savefig(O + 'timeline.png'); plt.close(fig)

# 13. SampleCo NAV bridge (US$/share)
fig, ax = plt.subplots(figsize=(MAIN, 2.2), dpi=300)
br = [('Mine A\n(Ontario)', 12.0), ('Mine B\n(Mexico)', 4.5), ('Project C\n(risked)', 3.0), ('Other\nresources', 1.0), ('Total asset\nvalue', None),
      ('Corporate\nG&A', -1.25), ('Reclamation', -0.75), ('Cash', 2.5), ('Debt', -4.0), ('NAV per\nshare', None)]
cum = 0
for i, (l, v) in enumerate(br):
    if v is None:
        ax.bar(i, cum, 0.6, color=NAVY); ax.text(i, cum + 0.4, f'{cum:.2f}', ha='center', fontsize=6.6, fontweight='bold', color=NAVY)
    else:
        b = cum if v > 0 else cum + v
        ax.bar(i, abs(v), 0.6, bottom=b, color=STEEL if v > 0 else AMBER); ax.text(i, max(cum, cum + v) + 0.4, f'{v:+.2f}', ha='center', fontsize=6.2, color=SLATE); cum += v
ax.text(-0.3, 25.2, 'At a US$20.40 share price, SampleCo trades at 1.20x P/NAV', fontsize=6.4, color=NAVY, va='top')
ax.set_xticks(range(len(br))); ax.set_xticklabels([b[0] for b in br], fontsize=5.9); ax.set_ylim(0, 25.5); ax.set_ylabel('US$ per share'); style(ax)
plt.subplots_adjust(left=0.08, right=0.99, top=0.97, bottom=0.22); fig.savefig(O + 'nav.png'); plt.close(fig)

# 14. P/NAV ranges by company type
fig, ax = plt.subplots(figsize=(MAIN, 1.9), dpi=300)
pn = [('Royalty and streaming', 1.5, 2.5), ('Senior gold producers', 1.0, 1.5), ('Diversified majors, senior base metals', 0.8, 1.3),
      ('Mid-tier and junior producers', 0.6, 1.1), ('Developers', 0.3, 0.7)]
for i, (l, a, b) in enumerate(pn):
    y = len(pn) - 1 - i; ax.barh(y, b - a, left=a, height=0.5, color=STEEL if i else NAVY)
    ax.text(a - 0.04, y, f'{a:.1f}x', ha='right', va='center', fontsize=6.2, color=NAVY); ax.text(b + 0.04, y, f'{b:.1f}x', ha='left', va='center', fontsize=6.2, color=NAVY)
ax.scatter([230.76 / 138.88, 30.21 / 42.35], [4, 1], marker='D', s=24, color=AMBER, zorder=5)
ax.text(230.76 / 138.88, 4.38, 'FNV 1.66x', ha='center', fontsize=6, color=AMBER, fontweight='bold'); ax.text(30.21 / 42.35, 1.38, 'AGI 0.71x', ha='center', fontsize=6, color=AMBER, fontweight='bold')
ax.set_yticks(range(len(pn))); ax.set_yticklabels([p[0] for p in pn][::-1], color=NAVY); ax.set_xlim(0, 2.9); ax.set_ylim(-0.6, 4.7); style(ax, 'x')
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'{v:.1f}x'))
plt.subplots_adjust(left=0.36, right=0.98, top=0.98, bottom=0.12); fig.savefig(O + 'pnav.png'); plt.close(fig)

# 15. Study accuracy
fig, ax = plt.subplots(figsize=(MAIN, 1.35), dpi=300)
for i, (l, a, b) in enumerate([('Scoping study / PEA', 35, 50), ('Pre-feasibility study', 25, 30), ('Feasibility study', 10, 15)]):
    y = 2 - i
    ax.barh(y, 2 * b, left=-b, height=0.5, color=PALE); ax.barh(y, 2 * a, left=-a, height=0.5, color=[LIGHT, STEEL, NAVY][i])
    ax.text(b + 2, y, f'±{a}% to {b}%', va='center', fontsize=6.3, color=NAVY)
ax.set_yticks([2, 1, 0]); ax.set_yticklabels(['Scoping study / PEA', 'Pre-feasibility study', 'Feasibility study'], color=NAVY)
ax.set_xlim(-55, 70); ax.axvline(0, color=SLATE, lw=0.6); ax.set_xlabel('Accuracy of the capital cost estimate (%)'); style(ax, 'x')
plt.subplots_adjust(left=0.24, right=0.98, top=0.96, bottom=0.27); fig.savefig(O + 'studies.png'); plt.close(fig)
print('charts ok')
