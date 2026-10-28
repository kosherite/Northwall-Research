"""Map helpers for the primer: decode Natural Earth TopoJSON (world-atlas, sane-topojson) and draw in the Northwall style."""
import json
import numpy as np
from shapely.geometry import Polygon, MultiPolygon, LineString, MultiLineString
from shapely.ops import transform as stransform
from pyproj import Transformer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from matplotlib import font_manager as fm

for w in ['Regular', 'Bold']:
    fm.fontManager.addfont(f'/usr/share/fonts/truetype/liberation/LiberationSans-{w}.ttf')
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 7})

NAVY = '#0F1A2B'; STEEL = '#2F5D7C'; SLATE = '#5A6B7C'; LIGHT = '#9DB3C6'; PALE = '#E9EEF2'
LAND = '#E4E8EC'; BORDER = '#FFFFFF'; WATER = '#FFFFFF'; AMBER = '#C98A12'
G = '/home/claude/primer/geo/'


def _arcs(topo):
    t = topo.get('transform'); out = []
    for arc in topo['arcs']:
        if t:
            x = y = 0; pts = []
            for dx, dy in arc:
                x += dx; y += dy
                pts.append((x * t['scale'][0] + t['translate'][0], y * t['scale'][1] + t['translate'][1]))
        else:
            pts = [tuple(p) for p in arc]
        out.append(pts)
    return out


def _ring(arcs, idx):
    pts = []
    for i in idx:
        a = arcs[i] if i >= 0 else arcs[~i][::-1]
        pts.extend(a if not pts else a[1:])
    return pts


def _geom(arcs, g):
    t = g['type']
    if t == 'Polygon':
        rings = [_ring(arcs, r) for r in g['arcs']]
        return Polygon(rings[0], rings[1:]) if len(rings[0]) > 3 else None
    if t == 'MultiPolygon':
        polys = []
        for p in g['arcs']:
            rings = [_ring(arcs, r) for r in p]
            if len(rings[0]) > 3: polys.append(Polygon(rings[0], rings[1:]))
        return MultiPolygon(polys) if polys else None
    if t == 'LineString':
        return LineString(_ring(arcs, g['arcs']))
    if t == 'MultiLineString':
        return MultiLineString([_ring(arcs, l) for l in g['arcs']])
    return None


def load(path, obj):
    topo = json.load(open(G + path)); arcs = _arcs(topo); out = []
    for g in topo['objects'][obj]['geometries']:
        geo = _geom(arcs, g)
        if geo is not None and not geo.is_empty:
            out.append({'id': g.get('id'), 'props': g.get('properties', {}), 'geom': geo})
    return out


def world_countries():
    return load('world-atlas-2.0.2/countries-50m.json', 'countries')


def projector(crs):
    tr = Transformer.from_crs('EPSG:4326', crs, always_xy=True)
    return lambda geom: stransform(lambda x, y, z=None: tr.transform(x, y), geom), tr


def _patch(geom, **kw):
    polys = [geom] if geom.geom_type == 'Polygon' else list(geom.geoms)
    verts, codes = [], []
    for p in polys:
        for ring in [p.exterior] + list(p.interiors):
            c = np.asarray(ring.coords)
            if len(c) < 3: continue
            verts.extend(c.tolist()); codes.extend([Path.MOVETO] + [Path.LINETO] * (len(c) - 2) + [Path.CLOSEPOLY])
    return PathPatch(Path(verts, codes), **kw) if verts else None


def draw(ax, feats, proj, fill=LAND, edge=BORDER, lw=0.3, fills=None, z=1):
    for f in feats:
        try:
            g = proj(f['geom'])
        except Exception:
            continue
        if not g.is_valid: g = g.buffer(0)
        if g.is_empty: continue
        col = (fills or {}).get(f['props'].get('name') or f['id'], fill)
        p = _patch(g, facecolor=col, edgecolor=edge, linewidth=lw, zorder=z)
        if p: ax.add_patch(p)


def _fix_dateline(geom):
    from shapely.geometry import box
    from shapely.affinity import translate
    polys = [geom] if geom.geom_type == 'Polygon' else list(geom.geoms)
    out = []
    for p in polys:
        x0, _, x1, _ = p.bounds
        if x1 - x0 <= 180:
            out.append(p); continue
        shifted = Polygon([(x + 360 if x < 0 else x, y) for x, y in p.exterior.coords]).buffer(0)
        a = shifted.intersection(box(0, -90, 180, 90)); b = translate(shifted.intersection(box(180, -90, 360, 90)), -360)
        for g in (a, b):
            if g.is_empty: continue
            out.extend([g] if g.geom_type == 'Polygon' else [q for q in getattr(g, 'geoms', []) if q.geom_type == 'Polygon'])
    return MultiPolygon(out) if len(out) > 1 else out[0]


def clip_world(feats):
    out = []
    for f in feats:
        if f['props'].get('name') == 'Antarctica': continue
        f = dict(f); f['geom'] = _fix_dateline(f['geom']); out.append(f)
    return out
