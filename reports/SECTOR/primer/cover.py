from maps import *
fig = plt.figure(figsize=(8.5, 2.9), dpi=300); ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_facecolor('#0F1A2B'); fig.patch.set_facecolor('#0F1A2B')
draw(ax, world, proj, fill='#1E3046', edge='#0F1A2B', lw=0.25)
for name, lon, lat, fam, dx, dy, ha in DEP:
    x, y = tr.transform(lon, lat); ax.scatter([x], [y], s=14, color='#E0A526', edgecolor='#0F1A2B', linewidth=0.5, zorder=5)
x0, _ = tr.transform(-180, 0); x1, _ = tr.transform(180, 0); _, ya = tr.transform(0, -48); _, yb = tr.transform(0, 78)
w = x1 - x0; h = w * 2.9 / 8.5; cy = (ya + yb) / 2
ax.set_xlim(x0, x1); ax.set_ylim(cy - h / 2, cy + h / 2); ax.set_aspect('auto')
fig.savefig(O + 'cover_band.png', facecolor='#0F1A2B'); plt.close(fig)
print('cover ok')
