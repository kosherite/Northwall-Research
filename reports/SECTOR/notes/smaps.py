"""Annotated maps for the Northwall sector notes (Natural Earth boundaries)."""
import sys; sys.path.insert(0, '/home/claude/primer')
from geo import *
from shapely.geometry import Polygon as SP, LineString
from shapely.ops import unary_union
import numpy as np, os
O = '/home/claude/sector/img/'; os.makedirs(O, exist_ok=True)
AMBER = '#C98A12'; TEAL = '#3E8E7E'; RED = '#B5473A'

world = clip_world(world_countries())
na = load('sane-topojson-4.0.0/dist/north-america_50m.json', 'subunits')
nac = load('sane-topojson-4.0.0/dist/north-america_50m.json', 'countries')
lakes = load('sane-topojson-4.0.0/dist/north-america_50m.json', 'lakes')
can = [f for f in na if f['props'].get('gu') == 'CAN']; usa = [f for f in na if f['props'].get('gu') == 'USA']


def fit(ax, x0, x1, y0, y1, w, h):
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2; dx, dy = x1 - x0, y1 - y0
    if dx / dy > w / h: dy = dx * h / w
    else: dx = dy * w / h
    ax.set_aspect('auto'); ax.set_xlim(cx - dx / 2, cx + dx / 2); ax.set_ylim(cy - dy / 2, cy + dy / 2)


def canvas(w, h):
    fig = plt.figure(figsize=(w, h), dpi=300); ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_aspect('equal'); return fig, ax


def lbl(ax, tr, lon, lat, text, dx=5, dy=0, ha='left', fs=5.9, bold=False, c=NAVY, line=False, box=False):
    x, y = tr.transform(lon, lat)
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va='center', fontsize=fs, color=c, zorder=9,
                fontweight='bold' if bold else 'normal', arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.45, shrinkA=1, shrinkB=2.5) if line else None,
                bbox=dict(boxstyle='round,pad=0.18', fc='white', ec='none', alpha=0.85) if box else None)


def pt(ax, tr, lon, lat, c, s=18, m='o', ec='white', lw=0.6, z=8):
    x, y = tr.transform(lon, lat); ax.scatter([x], [y], s=s, color=c, marker=m, edgecolor=ec, linewidth=lw, zorder=z)


def route(ax, tr, pts, c, lw=1.6, ls='-', z=6, arrow=False):
    xy = np.array([tr.transform(lo, la) for lo, la in pts])
    # densify to a smooth path
    t = np.linspace(0, 1, len(xy)); tt = np.linspace(0, 1, 120)
    xs = np.interp(tt, t, xy[:, 0]); ys = np.interp(tt, t, xy[:, 1])
    ax.plot(xs, ys, color='white', lw=lw + 1.4, zorder=z - 0.1, solid_capstyle='round')
    ax.plot(xs, ys, color=c, lw=lw, ls=ls, zorder=z, solid_capstyle='round')
    if arrow:
        ax.annotate('', xy=(xs[-1], ys[-1]), xytext=(xs[-6], ys[-6]), arrowprops=dict(arrowstyle='-|>', color=c, lw=lw, mutation_scale=8), zorder=z)


def legend(ax, items, x=0.015, y=0.05, dy=0.042, fs=6):
    for i, (kind, c, t) in enumerate(items):
        yy = y + (len(items) - 1 - i) * dy
        if kind == 'line': ax.plot([x, x + 0.03], [yy, yy], color=c, lw=1.8, transform=ax.transAxes, zorder=10)
        elif kind == 'area': ax.add_patch(matplotlib.patches.Rectangle((x, yy - 0.012), 0.03, 0.024, color=c, alpha=0.45, transform=ax.transAxes, zorder=10))
        else: ax.scatter([x + 0.015], [yy], s=20, color=c, marker=kind, edgecolor=NAVY if kind == 'D' else 'white', linewidth=0.7, transform=ax.transAxes, zorder=10)
        ax.text(x + 0.04, yy, t, transform=ax.transAxes, va='center', fontsize=fs, color=NAVY, zorder=10)


# ======================= OIL & GAS =======================
# 1. WCSB plays, coverage assets and export routes (Lambert conformal for Canada)
pc, trc = projector('EPSG:3978')
fig, ax = canvas(7.3, 5.0)
draw(ax, usa + [f for f in nac if f['id'] == 'USA'], pc, fill='#F1F3F5', lw=0.3)
draw(ax, can, pc, fill='#E3E8ED', edge='white', lw=0.7)
draw(ax, lakes, pc, fill='white', edge='white', lw=0.1, z=2)
PLAYS = {
    'Montney': ([(-123.6, 57.3), (-121.4, 57.9), (-118.4, 55.9), (-116.6, 54.3), (-117.7, 53.9), (-120.2, 54.9), (-122.7, 56.2)], STEEL),
    'Duvernay': ([(-118.3, 54.8), (-116.4, 55.0), (-113.0, 52.7), (-112.8, 51.6), (-114.4, 51.3), (-117.7, 53.7)], TEAL),
    'Athabasca\noil sands': ([(-114.6, 58.9), (-110.0, 58.9), (-110.0, 55.4), (-113.0, 55.1), (-114.9, 56.6)], AMBER),
    'Cold Lake': ([(-112.5, 55.25), (-110.0, 55.25), (-110.0, 53.85), (-112.3, 53.85)], AMBER),
    'Peace River': ([(-118.6, 57.2), (-116.0, 57.2), (-116.0, 55.7), (-118.4, 55.75)], AMBER),
    'Viking': ([(-110.0, 51.1), (-107.6, 51.4), (-107.6, 52.3), (-110.0, 52.1)], '#7C93A8'),
    'SE Sask light oil\n(Weyburn, Bakken)': ([(-104.8, 49.0), (-101.4, 49.0), (-101.4, 50.05), (-104.4, 50.05)], '#7C93A8')}
for name, (poly, c) in PLAYS.items():
    g = pc(SP(poly)); ax.add_patch(matplotlib.patches.Polygon(np.asarray(g.exterior.coords), closed=True, fc=c, alpha=0.38, ec=c, lw=0.6, zorder=3))
PL = {'Montney': (-124.0, 56.9, 'right'), 'Duvernay': (-116.2, 52.3, 'right'), 'Athabasca\noil sands': (-109.6, 58.4, 'left'), 'Cold Lake': (-109.6, 54.0, 'left'),
      'Peace River': (-117.3, 57.55, 'center'), 'Viking': (-107.3, 52.5, 'left'), 'SE Sask light oil\n(Weyburn, Bakken)': (-102.9, 50.75, 'center')}
for name, (lo, la, ha) in PL.items(): lbl(ax, trc, lo, la, name, dx=0, ha=ha, fs=6.1, c=SLATE)
# routes
TMX = [(-113.49, 53.55), (-116.5, 53.4), (-118.08, 52.88), (-119.3, 51.9), (-120.33, 50.67), (-121.5, 49.4), (-122.95, 49.28)]
CGL = [(-120.24, 55.76), (-122.8, 55.0), (-124.0, 54.0), (-126.5, 54.1), (-128.65, 54.05)]
MAIN = [(-113.49, 53.55), (-111.31, 52.67), (-108.0, 51.6), (-104.6, 50.45), (-100.0, 49.6), (-97.5, 49.0)]
KEY = [(-111.31, 52.67), (-109.5, 51.0), (-107.6, 49.0)]
route(ax, trc, TMX, RED, 1.8); route(ax, trc, CGL, TEAL, 1.6, ls=(0, (3, 1.5))); route(ax, trc, MAIN, NAVY, 1.8, arrow=True); route(ax, trc, KEY, '#7A5C99', 1.5, arrow=True)
lbl(ax, trc, -121.0, 51.3, 'Trans Mountain\n890 kbbl/d', dx=-8, dy=8, ha='right', fs=6, c=RED, bold=True)
lbl(ax, trc, -123.6, 55.9, 'Coastal GasLink\n2.1 Bcf/d', dx=0, dy=0, ha='center', fs=6, c=TEAL, bold=True)
lbl(ax, trc, -105.6, 50.95, 'Enbridge Mainline', dx=4, dy=8, ha='left', fs=6, c=NAVY, bold=True)
lbl(ax, trc, -108.4, 49.6, 'Keystone', dx=-6, dy=0, ha='right', fs=6, c='#7A5C99', bold=True)
for lo, la, t, dx, dy, ha in [(-113.49, 53.55, 'Edmonton', 6, 4, 'left'), (-111.31, 52.67, 'Hardisty', 6, -4, 'left'), (-114.07, 51.05, 'Calgary', -6, 0, 'right'),
                              (-111.38, 56.73, 'Fort McMurray', 6, 7, 'left'), (-122.95, 49.28, 'Westridge (Burnaby)', 4, -9, 'left'), (-128.65, 54.05, 'Kitimat (LNG Canada)', 4, -9, 'left')]:
    pt(ax, trc, lo, la, NAVY, s=9, ec='white'); lbl(ax, trc, lo, la, t, dx=dx, dy=dy, ha=ha, fs=5.8)
# coverage assets
WCPA = [(-118.9, 54.65, 'Kakwa (Montney)', -6, 6, 'right'), (-119.5, 55.1, 'Grande Prairie (Montney)', -6, 3, 'right'), (-116.8, 54.35, 'Kaybob (Duvernay)', 6, 6, 'left'),
        (-109.15, 51.47, 'Kindersley (Viking)', 6, -9, 'left'), (-103.85, 49.66, 'Weyburn (CO\u2082 flood)', 7, 9, 'left')]
for lo, la, t, dx, dy, ha in WCPA: pt(ax, trc, lo, la, STEEL, s=30, m='D', ec=NAVY, lw=0.8, z=11); lbl(ax, trc, lo, la, t, dx=dx, dy=dy, ha=ha, fs=6, bold=True, box=True)
for lo, la, t, dx, dy in [(-111.6, 56.35, 'Hangingstone', 8, 6), (-111.9, 55.95, 'Great Divide (Connacher)', 8, -5)]:
    pt(ax, trc, lo, la, AMBER, s=30, m='D', ec=NAVY, lw=0.8, z=11); lbl(ax, trc, lo, la, t, dx=dx, dy=dy, fs=6, bold=True, box=True)
x0 = min(trc.transform(-130.0, 54.5)[0], trc.transform(-125.0, 48.6)[0]); x1, _ = trc.transform(-97.5, 50.0); _, y0 = trc.transform(-113, 48.0); _, y1 = trc.transform(-118, 59.6)
fit(ax, x0, x1, y0, y1, 7.3, 5.0)
legend(ax, [('D', STEEL, 'Whitecap (WCP) core areas'), ('D', AMBER, 'Greenfire (GFR) SAGD assets'), ('line', RED, 'Trans Mountain (to Pacific and Asia)'),
            ('line', NAVY, 'Enbridge Mainline (to US Midwest)'), ('line', '#7A5C99', 'Keystone (to Cushing and Gulf Coast)'), ('line', TEAL, 'Coastal GasLink (gas to LNG Canada)')], x=0.015, y=0.03, dy=0.042)
fig.savefig(O + 'map_wcsb.png'); plt.close(fig)

# 2. North American crude routes and price hubs
pn, trn = projector('EPSG:2163')
fig, ax = canvas(5.45, 3.9)
draw(ax, [f for f in nac if f['id'] in ('USA', 'MEX', 'CAN')], pn, fill='#E3E8ED', edge='white', lw=0.5)
draw(ax, can + usa, pn, fill='#E3E8ED', edge='white', lw=0.3)
draw(ax, lakes, pn, fill='white', edge='white', lw=0.1, z=2)
route(ax, trn, [(-111.31, 52.67), (-118.08, 52.88), (-120.33, 50.67), (-122.95, 49.28)], RED, 1.8)
route(ax, trn, [(-122.95, 49.28), (-125.5, 48.0), (-129.0, 46.0), (-133, 44.5)], RED, 1.1, ls=(0, (2, 2)), arrow=True)
route(ax, trn, [(-111.31, 52.67), (-104.6, 50.45), (-97.5, 49.0), (-95.5, 47.8), (-92.1, 46.72), (-88.0, 42.6), (-87.6, 41.5)], NAVY, 1.8)
route(ax, trn, [(-87.6, 41.5), (-89.0, 39.0), (-89.2, 38.6)], NAVY, 1.2)
route(ax, trn, [(-111.31, 52.67), (-107.6, 49.0), (-103.0, 44.0), (-96.9, 40.0), (-96.77, 35.98)], '#7A5C99', 1.6)
route(ax, trn, [(-96.77, 35.98), (-95.6, 32.5), (-95.37, 29.76), (-94.0, 29.9)], '#7A5C99', 1.6)
for lo, la, t, dx, dy, ha in [(-111.31, 52.67, 'Hardisty: WCS priced here', 6, 5, 'left'), (-96.77, 35.98, 'Cushing: WTI priced here', 6, 0, 'left'),
                              (-94.0, 29.9, 'US Gulf Coast refiners', 5, -6, 'left'), (-87.6, 41.5, 'Chicago and Midwest refiners', -6, 6, 'right'),
                              (-92.1, 46.72, 'Superior', 5, 4, 'left'), (-122.95, 49.28, 'Westridge', -5, 5, 'right')]:
    pt(ax, trn, lo, la, NAVY, s=12); lbl(ax, trn, lo, la, t, dx=dx, dy=dy, ha=ha, fs=6)
lbl(ax, trn, -131.5, 45.0, 'Tankers to China,\nKorea and Japan', dx=0, dy=-12, ha='center', fs=6, c=RED, bold=True)
x0, _ = trn.transform(-137, 47); x1, _ = trn.transform(-78, 42); _, y0 = trn.transform(-95, 26.0); _, y1 = trn.transform(-110, 56.5)
ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
legend(ax, [('line', RED, 'Trans Mountain 890 kbbl/d (apportioned 7%, Oct)'), ('line', NAVY, 'Enbridge Mainline (heavy apportioned 16%, Oct)'), ('line', '#7A5C99', 'Keystone to Cushing and the Gulf Coast')], x=0.015, y=0.03, dy=0.05, fs=5.9)
fig.savefig(O + 'map_routes.png'); plt.close(fig)

# 3. Middle East chokepoints and shut-ins
pm, trm = projector('EPSG:3857')
fig, ax = canvas(5.45, 3.4)
draw(ax, world, pm, fill='#E3E8ED', edge='white', lw=0.5)
GULF = {'Saudi Arabia', 'Iran', 'Iraq', 'Kuwait', 'United Arab Emirates', 'Qatar', 'Oman', 'Bahrain'}
draw(ax, [f for f in world if f['props'].get('name') in GULF], pm, fill='#D4DCE4', edge='white', lw=0.5)
route(ax, trm, [(49.67, 25.93), (45.0, 25.0), (41.5, 24.6), (38.06, 24.09)], NAVY, 1.8)
route(ax, trm, [(53.6, 23.9), (55.0, 24.6), (56.33, 25.12)], NAVY, 1.5)
route(ax, trm, [(50.3, 28.6), (53.5, 27.3), (56.25, 26.57), (58.5, 25.4), (61.5, 23.5)], AMBER, 1.6, ls=(0, (3, 1.5)), arrow=True)
route(ax, trm, [(38.06, 24.09), (39.5, 20.0), (42.0, 15.5), (43.3, 12.6), (46.5, 12.0)], AMBER, 1.3, ls=(0, (3, 1.5)), arrow=True)
pt(ax, trm, 56.25, 26.57, RED, s=60, m='X', ec='white', lw=0.6, z=12); pt(ax, trm, 43.3, 12.6, RED, s=40, m='X', ec='white', lw=0.6, z=12)
lbl(ax, trm, 56.25, 26.57, 'Strait of Hormuz', dx=8, dy=10, fs=6.6, bold=True, c=RED)
lbl(ax, trm, 43.3, 12.6, 'Bab el-Mandeb', dx=-8, dy=-6, ha='right', fs=6.3, bold=True, c=RED)
lbl(ax, trm, 43.5, 24.8, 'East-West pipeline\n(attacked Sep 2026)', dx=0, dy=16, ha='center', fs=5.9, bold=True)
lbl(ax, trm, 55.3, 24.4, 'Habshan-Fujairah\nbypass', dx=4, dy=-12, ha='left', fs=5.8)
for lo, la, t, dx, dy, ha in [(49.67, 25.93, 'Abqaiq', 4, -6, 'left'), (38.06, 24.09, 'Yanbu', -5, 0, 'right'), (50.16, 26.64, 'Ras Tanura', -5, 4, 'right'),
                              (50.31, 29.24, 'Kharg Island', -5, 3, 'right'), (56.33, 25.12, 'Fujairah', 5, -3, 'left')]:
    pt(ax, trm, lo, la, NAVY, s=10); lbl(ax, trm, lo, la, t, dx=dx, dy=dy, ha=ha, fs=5.8)
x0, y0 = trm.transform(31, 10.5); x1, y1 = trm.transform(64, 33.5); ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
ax.text(0.985, 0.97, 'Middle East crude shut-ins (EIA)\nMay 2026 peak: 10.9 mb/d\nSeptember: 4.8 mb/d\n4Q26 assumption: 4.5 mb/d', transform=ax.transAxes, ha='right', va='top', fontsize=6.2, color=NAVY,
        bbox=dict(boxstyle='round,pad=0.5', fc='white', ec=LIGHT, lw=0.6), zorder=12)
legend(ax, [('line', NAVY, 'Pipelines that bypass Hormuz'), ('line', AMBER, 'Tanker routes'), ('X', RED, 'Chokepoints')], x=0.015, y=0.04, dy=0.055, fs=6)
fig.savefig(O + 'map_hormuz.png'); plt.close(fig)

# ======================= METALS & MINING =======================
# 4. Americas: Northwall gold coverage assets
pa, tra = projector('ESRI:102033') if False else projector('EPSG:3857')
fig, ax = canvas(4.0, 5.2)
draw(ax, world, pa, fill='#E3E8ED', edge='white', lw=0.4)
AGIA = [(-84.55, 48.35, '', 5, -8, 'left'), (-80.65, 47.94, '', 5, 2, 'left'), (-101.05, 56.85, 'Lynn Lake (build)', -5, 4, 'right'),
        (-108.75, 28.65, 'Mulatos District\n(incl. PDA)', 6, -6, 'left')]
FNVA = [(-70.3, -27.5, 'Candelaria', -5, 0, 'right'), (-71.4, -14.9, 'Antapaccay', -5, 0, 'right'), (-80.65, 8.83, 'Cobre Panamá', -5, 2, 'right'),
        (-81.94, 47.53, '', -5, -7, 'right'), (-79.69, 50.02, '', 5, 6, 'left'), (-78.13, 48.13, '', 6, 7, 'left'),
        (-56.3, -5.8, 'Tocantinzinho', 5, 0, 'left'), (-86.95, 49.72, '', -5, 5, 'right'), (-57.7, 48.37, 'Valentine', 5, 0, 'left'),
        (-115.33, 44.9, 'Stibnite (2029)', -5, 0, 'right'), (-110.7, 31.8, 'Copper World (2029)', 5, 2, 'left'), (-115.1, 35.28, 'Castle Mountain', -5, 2, 'right')]
for lo, la, t, dx, dy, ha in FNVA:
    pt(ax, tra, lo, la, AMBER, s=16)
    if t: lbl(ax, tra, lo, la, t, dx=dx, dy=dy, ha=ha, fs=5.5)
for lo, la, t, dx, dy, ha in AGIA:
    pt(ax, tra, lo, la, STEEL, s=28, m='D', ec=NAVY, lw=0.8, z=11)
    if t: lbl(ax, tra, lo, la, t, dx=dx, dy=dy, ha=ha, fs=5.6, bold=True)
lbl(ax, tra, -82.5, 48.6, 'Ontario and Quebec:\nIsland Gold, Magino and\nYoung-Davidson (AGI); Côté,\nDetour, Malartic and\nGreenstone (FNV).\nSee the next exhibit', dx=26, dy=-34, ha='left', fs=5.4, line=True, box=True)
x0, y0 = tra.transform(-128, -40); x1, y1 = tra.transform(-40, 62); ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
legend(ax, [('D', STEEL, 'Alamos Gold (AGI) operations'), ('o', AMBER, 'Franco-Nevada (FNV) key royalties and streams')], x=0.03, y=0.04, dy=0.04, fs=5.8)
fig.savefig(O + 'map_americas.png'); plt.close(fig)

# 5. Ontario-Quebec zoom: the Abitibi and northern Ontario gold belts
fig, ax = canvas(7.3, 3.3)
draw(ax, usa, pc, fill='#F1F3F5', lw=0.3); draw(ax, can, pc, fill='#E3E8ED', edge='white', lw=0.8); draw(ax, lakes, pc, fill='white', edge='white', lw=0.1, z=2)
belt = pc(SP([(-82.6, 48.95), (-77.0, 48.75), (-76.6, 47.95), (-82.4, 47.75)]))
ax.add_patch(matplotlib.patches.Polygon(np.asarray(belt.exterior.coords), fc=AMBER, alpha=0.18, ec=AMBER, lw=0.6, ls=(0, (3, 2)), zorder=3))
lbl(ax, trc, -77.7, 47.55, 'Abitibi greenstone belt', dx=0, ha='center', fs=6.4, c=AMBER, bold=True)
for lo, la, t, dx, dy, ha in [(-84.55, 48.35, 'Island Gold and Magino (AGI)\nPhase 3+ shaft 1Q27; mill to 20,000 tpd 1Q28', -8, -16, 'right'),
                              (-80.65, 47.94, 'Young-Davidson (AGI)\nback toward ~5,000 tpd after June seismic event', 10, -20, 'left')]:
    pt(ax, trc, lo, la, STEEL, s=36, m='D', ec=NAVY, lw=0.9, z=11); lbl(ax, trc, lo, la, t, dx=dx, dy=dy, ha=ha, fs=6, bold=True, line=True, box=True)
for lo, la, t, dx, dy, ha in [(-81.94, 47.53, 'Côté Gold (FNV 7.5% GMR)\nreserve update 4Q26', -14, -18, 'right'), (-79.69, 50.02, 'Detour Lake (FNV)', 6, 6, 'left'),
                              (-78.13, 48.13, 'Canadian Malartic\nand Odyssey (FNV)', 0, 18, 'center'), (-86.95, 49.72, 'Greenstone (FNV)', -6, 6, 'right')]:
    pt(ax, trc, lo, la, AMBER, s=24, z=10); lbl(ax, trc, lo, la, t, dx=dx, dy=dy, ha=ha, fs=6, line=abs(dx) > 10, box=True)
for lo, la, t, dx, dy, ha in [(-81.33, 48.48, 'Timmins', 5, 6, 'left'), (-80.99, 46.49, 'Sudbury', 5, -2, 'left'), (-84.33, 46.52, 'Sault Ste. Marie', -5, -3, 'right'), (-89.25, 48.38, 'Thunder Bay', -5, 0, 'right'), (-79.0, 48.24, 'Rouyn-Noranda', 5, -6, 'left')]:
    pt(ax, trc, lo, la, NAVY, s=7); lbl(ax, trc, lo, la, t, dx=dx, dy=dy, ha=ha, fs=5.6, c=SLATE)
x0, y0 = trc.transform(-90.0, 46.0); x1, y1 = trc.transform(-75.5, 51.0)
fit(ax, x0, x1, y0, y1, 7.3, 3.3)
legend(ax, [('D', STEEL, 'Alamos Gold operations'), ('o', AMBER, 'Franco-Nevada royalties and streams')], x=0.015, y=0.05, dy=0.065, fs=6.2)
fig.savefig(O + 'map_abitibi.png'); plt.close(fig)
print('maps ok')
