"""Real maps for the primer, drawn from Natural Earth (world-atlas 50m; sane-topojson North America 50m)."""
from geo import *
from shapely.geometry import Point, box
import numpy as np

O = '/home/claude/primer/img/'
import os; os.makedirs(O, exist_ok=True)
EE = 'EPSG:8857'  # Equal Earth
world = clip_world(world_countries())
proj, tr = projector(EE)


def world_axes(w, h, extent=None):
    fig = plt.figure(figsize=(w, h), dpi=300); ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_aspect('equal')
    x0, _ = tr.transform(-168, 0); x1, _ = tr.transform(180, 0); _, y0 = tr.transform(0, -56); _, y1 = tr.transform(0, 83)
    if extent:
        (lo0, la0, lo1, la1) = extent; x0, y0 = tr.transform(lo0, la0); x1, y1 = tr.transform(lo1, la1)
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
    return fig, ax


# ---------- 1. Major deposits of the world, by deposit type ----------
FAM = {'Copper': '#2F5D7C', 'Gold and silver': '#C98A12', 'Iron ore': '#0F1A2B', 'Nickel and PGMs': '#3E8E7E', 'Lithium and uranium': '#8A5A9E'}
DEP = [  # name, lon, lat, family, dx, dy (label offset in points), ha
    ('Escondida', -69.07, -24.27, 'Copper', -5, -2, 'right'), ('Salar de Atacama', -68.25, -23.5, 'Lithium and uranium', 5, 4, 'left'),
    ('Yanacocha', -78.51, -6.98, 'Gold and silver', -5, 0, 'right'), ('Carajás', -50.17, -6.07, 'Iron ore', 5, 0, 'left'),
    ('Kidd Creek', -81.37, 48.69, 'Copper', -5, 5, 'right'), ('Timmins', -81.33, 48.2, 'Gold and silver', -5, -3, 'right'),
    ('Sudbury', -81.0, 46.5, 'Nickel and PGMs', 5, -5, 'left'), ('Cigar Lake / McArthur River', -104.8, 57.9, 'Lithium and uranium', -5, 3, 'right'),
    ('Nevada (Carlin)', -116.1, 40.9, 'Gold and silver', -5, 0, 'right'), ('Wyoming ISR', -105.6, 43.0, 'Lithium and uranium', 5, -6, 'left'),
    ('Kiruna', 20.22, 67.85, 'Iron ore', 5, 2, 'left'), ('Neves-Corvo', -7.97, 37.57, 'Copper', -5, 0, 'right'),
    ('Kamoa-Kakula / Copperbelt', 26.0, -11.5, 'Copper', 5, 0, 'left'), ('Bushveld', 27.24, -25.67, 'Nickel and PGMs', 5, -3, 'left'),
    ('Norilsk', 88.2, 69.35, 'Nickel and PGMs', 5, 0, 'left'), ('Kazakhstan ISR', 67.0, 45.3, 'Lithium and uranium', 5, 0, 'left'),
    ('Oyu Tolgoi', 106.85, 43.0, 'Copper', 5, 0, 'left'), ('Sulawesi (Morowali)', 122.1, -2.8, 'Nickel and PGMs', -5, 5, 'right'),
    ('Grasberg', 137.11, -4.06, 'Copper', -4, 7, 'right'), ('Lihir', 152.64, -3.12, 'Gold and silver', 5, 2, 'left'),
    ('Pilbara', 117.79, -22.69, 'Iron ore', -5, 0, 'right'), ('Kalgoorlie', 121.47, -30.75, 'Gold and silver', -5, 7, 'right'),
    ('Greenbushes', 116.06, -33.86, 'Lithium and uranium', -5, -3, 'right'), ('Olympic Dam', 136.89, -30.44, 'Copper', 5, 0, 'left'),
    ('New Caledonia', 165.4, -21.3, 'Nickel and PGMs', -5, -6, 'right'),
]
fig, ax = world_axes(7.3, 3.55)
draw(ax, world, proj, lw=0.25)
for name, lon, lat, fam, dx, dy, ha in DEP:
    x, y = tr.transform(lon, lat)
    ax.scatter([x], [y], s=16, color=FAM[fam], edgecolor='white', linewidth=0.6, zorder=5)
    ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va='center', fontsize=5.6, color=NAVY, zorder=6)
for i, (k, c) in enumerate(FAM.items()):
    xx = 0.015 + i * 0.165
    ax.scatter([xx], [0.04], s=18, color=c, edgecolor='white', linewidth=0.6, transform=ax.transAxes, zorder=7)
    ax.text(xx + 0.012, 0.04, k, transform=ax.transAxes, va='center', fontsize=6.2, color=NAVY)
fig.savefig(O + 'map_deposits.png'); plt.close(fig)

# ---------- 2 & 3. Choropleths: gold and copper mine production (USGS MCS 2026, 2025e) ----------
def choropleth(fname, data, ramp, unit, labels, w=5.45, h=2.75):
    vmax = max(data.values())
    def col(v):
        t = (v / vmax) ** 0.6
        a = np.array(matplotlib.colors.to_rgb('#EDF1F4')); b = np.array(matplotlib.colors.to_rgb(ramp))
        return matplotlib.colors.to_hex(a + (b - a) * (0.18 + 0.82 * t))
    fills = {k: col(v) for k, v in data.items()}
    fig, ax = world_axes(w, h)
    draw(ax, world, proj, fills=fills, lw=0.25)
    for name, (dx, dy) in labels.items():
        f = next(x for x in world if x['props'].get('name') == name)
        g = f['geom'];  g = max(g.geoms, key=lambda p: p.area) if g.geom_type == 'MultiPolygon' else g
        c = g.representative_point(); x, y = tr.transform(c.x, c.y)
        short = {'United States of America': 'United States', 'Dem. Rep. Congo': 'DR Congo'}.get(name, name)
        ax.annotate(f'{short} {data[name]:,}', (x, y), xytext=(dx, dy), textcoords='offset points', fontsize=5.6, color=NAVY, ha='center', va='center',
                    arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.4) if (dx or dy) else None, zorder=6,
                    bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.75))
    # legend ramp
    for i, v in enumerate(np.linspace(vmax * 0.05, vmax, 5)):
        ax.add_patch(matplotlib.patches.Rectangle((0.02 + i * 0.035, 0.05), 0.033, 0.03, transform=ax.transAxes, color=col(v), zorder=7))
    ax.text(0.02, 0.11, unit, transform=ax.transAxes, fontsize=5.8, color=SLATE)
    ax.text(0.02, 0.015, 'Low', transform=ax.transAxes, fontsize=5.6, color=SLATE); ax.text(0.19, 0.015, 'High', transform=ax.transAxes, fontsize=5.6, color=SLATE, ha='right')
    fig.savefig(O + fname); plt.close(fig)

GOLD = {'China': 380, 'Russia': 310, 'Australia': 280, 'Canada': 200, 'United States of America': 160, 'Ghana': 150, 'Mexico': 140,
        'Kazakhstan': 130, 'Uzbekistan': 130, 'Peru': 110, 'Indonesia': 90, 'South Africa': 90, 'Brazil': 80}
choropleth('map_gold.png', GOLD, '#C98A12', '2025e mine production (t)',
           {'China': (0, 0), 'Russia': (0, 0), 'Australia': (0, 0), 'Canada': (0, 0), 'United States of America': (0, 0), 'Ghana': (-14, -12),
            'Mexico': (-10, -10), 'Kazakhstan': (-30, 4), 'Uzbekistan': (-8, -12), 'Peru': (-18, 0), 'Indonesia': (0, -12), 'South Africa': (0, -12), 'Brazil': (0, 0)})
COPPER = {'Chile': 5300, 'Dem. Rep. Congo': 3200, 'Peru': 2700, 'China': 1800, 'Russia': 1300, 'United States of America': 1000,
          'Zambia': 940, 'Australia': 730, 'Indonesia': 710, 'Kazakhstan': 710}
choropleth('map_copper.png', COPPER, '#2F5D7C', '2025e mine production (kt Cu)',
           {'Chile': (-34, 26), 'Dem. Rep. Congo': (-22, 6), 'Peru': (-20, 6), 'China': (0, 0), 'Russia': (8, 6), 'United States of America': (0, 0),
            'Zambia': (14, -10), 'Australia': (0, 0), 'Indonesia': (0, -12), 'Kazakhstan': (-34, -14)})

# ---------- 4. Canada: provinces and the main mining camps ----------
na = load('sane-topojson-4.0.0/dist/north-america_50m.json', 'subunits')
nac = load('sane-topojson-4.0.0/dist/north-america_50m.json', 'countries')
lakes = load('sane-topojson-4.0.0/dist/north-america_50m.json', 'lakes')
LCC = 'EPSG:3978'
pc, trc = projector(LCC)
fig = plt.figure(figsize=(7.3, 4.6), dpi=300); ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_aspect('equal')
draw(ax, [f for f in nac if f['id'] in ('USA', 'GRL')], pc, fill='#F1F3F5', lw=0.3)
prov = [f for f in na if f['props'].get('gu') == 'CAN']
draw(ax, prov, pc, fill='#DDE4EA', edge='white', lw=0.6)
draw(ax, lakes, pc, fill='white', edge='white', lw=0.1, z=2)
PN = {'BC': 'British\nColumbia', 'AB': 'Alberta', 'SK': 'Saskatchewan', 'MB': 'Manitoba', 'ON': 'Ontario', 'QC': 'Quebec', 'NL': 'Newfoundland\nand Labrador',
      'YT': 'Yukon', 'NT': 'Northwest\nTerritories', 'NU': 'Nunavut'}
for f in prov:
    if f['id'] in PN:
        lon, lat = f['props']['ct']
        if f['id'] == 'NU': lon, lat = -88, 66
        if f['id'] == 'QC': lon, lat = -71.5, 52.5
        if f['id'] == 'ON': lon, lat = -88.5, 51.8
        if f['id'] == 'NL': lon, lat = -61.5, 53.8
        x, y = trc.transform(lon, lat); ax.text(x, y, PN[f['id']], fontsize=6.4, color='#8A97A6', ha='center', va='center', zorder=3, style='italic')
CAMP = {'Gold': '#C98A12', 'Copper and base metals': '#2F5D7C', 'Nickel': '#3E8E7E', 'Uranium': '#8A5A9E', 'Iron ore, coal and diamonds': '#0F1A2B'}
CAMPS = [  # name, lon, lat, type, dx, dy, ha, northwall
    ('Golden Triangle', -130.3, 56.5, 'Gold', -6, 0, 'right', 0), ('Highland Valley Copper', -121.05, 50.48, 'Copper and base metals', -6, -2, 'right', 0),
    ('Elk Valley coal', -114.88, 49.75, 'Iron ore, coal and diamonds', 6, -6, 'left', 0), ('Ekati and Diavik', -110.6, 64.7, 'Iron ore, coal and diamonds', 6, 0, 'left', 0),
    ('Athabasca Basin', -105.0, 58.0, 'Uranium', 6, 0, 'left', 0), ('Lynn Lake (Alamos)', -101.05, 56.85, 'Gold', 6, 0, 'left', 1),
    ('Meliadine and Meadowbank', -93.0, 64.2, 'Gold', 6, 0, 'left', 0), ('Red Lake', -93.83, 51.02, 'Gold', -6, 0, 'right', 0),
    ('Greenstone', -86.95, 49.72, 'Gold', -26, 16, 'right', 0), ('Hemlo', -85.9, 48.69, 'Gold', -30, 2, 'right', 0),
    ('Island Gold and Magino (Alamos)', -84.55, 48.35, 'Gold', -22, -26, 'right', 1), ('Detour Lake', -79.69, 50.02, 'Gold', 40, 22, 'left', 0),
    ('Timmins', -81.33, 48.48, 'Gold', -14, 26, 'right', 0), ('Young-Davidson (Alamos)', -80.65, 47.94, 'Gold', 48, -22, 'left', 1),
    ('Kirkland Lake / Abitibi', -79.5, 48.2, 'Gold', 48, -6, 'left', 0), ('Sudbury', -80.99, 46.49, 'Nickel', 30, -26, 'left', 0),
    ('Malartic', -78.13, 48.13, 'Gold', 44, 8, 'left', 0), ('Labrador Trough', -66.91, 52.94, 'Iron ore, coal and diamonds', 6, 0, 'left', 0),
    ("Voisey's Bay", -62.1, 56.33, 'Nickel', 6, 0, 'left', 0), ('Raglan', -73.7, 61.7, 'Nickel', 6, 0, 'left', 0),
]
for name, lon, lat, typ, dx, dy, ha, nw in CAMPS:
    x, y = trc.transform(lon, lat)
    ax.scatter([x], [y], s=26 if nw else 18, color=CAMP[typ], edgecolor=NAVY if nw else 'white', linewidth=0.9 if nw else 0.6, zorder=6, marker='D' if nw else 'o')
    far = abs(dx) > 12 or abs(dy) > 12
    ax.annotate(name, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va='center', fontsize=5.8, color=NAVY, zorder=7, fontweight='bold' if nw else 'normal',
                arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.45, shrinkA=1, shrinkB=3) if far else None)
from shapely.ops import unary_union
bx = unary_union([pc(f['geom']).buffer(0) for f in prov]).bounds
ax.set_xlim(bx[0] - 9e5, bx[2] + 1e5); ax.set_ylim(bx[1] - 1e5, bx[3] - 9e5)
for i, (k, c) in enumerate(CAMP.items()):
    ax.scatter([0.02], [0.30 - i * 0.045], s=18, color=c, edgecolor='white', transform=ax.transAxes, zorder=8)
    ax.text(0.035, 0.30 - i * 0.045, k, transform=ax.transAxes, va='center', fontsize=6.2, color=NAVY)
ax.scatter([0.02], [0.30 - 5 * 0.045], s=24, color='white', edgecolor=NAVY, marker='D', linewidth=0.9, transform=ax.transAxes, zorder=8)
ax.text(0.035, 0.30 - 5 * 0.045, 'Northwall coverage (Alamos Gold)', transform=ax.transAxes, va='center', fontsize=6.2, color=NAVY, fontweight='bold')
fig.savefig(O + 'map_canada.png'); plt.close(fig)
print('maps ok')
