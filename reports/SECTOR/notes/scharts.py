"""Charts for the Northwall sector notes (Metals & Mining; Oil & Gas)."""
import sys, json; sys.path.insert(0, '/home/claude/primer')
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import font_manager as fm
for w in ['Regular', 'Bold']: fm.fontManager.addfont(f'/usr/share/fonts/truetype/liberation/LiberationSans-{w}.ttf')
NAVY = '#0F1A2B'; STEEL = '#2F5D7C'; SLATE = '#5A6B7C'; LIGHT = '#9DB3C6'; PALE = '#E9EEF2'; GRID = '#E6E9EC'; AMBER = '#C98A12'; TEAL = '#3E8E7E'; RED = '#B5473A'
GOOD = '#E2F0E9'; MID = '#F6EEDD'; BAD = '#F6E3E1'
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 6.8, 'axes.edgecolor': SLATE, 'axes.labelcolor': SLATE, 'xtick.color': SLATE, 'ytick.color': SLATE,
                     'xtick.labelsize': 6.4, 'ytick.labelsize': 6.4, 'text.parse_math': False})
O = '/home/claude/sector/img/'; MAIN = 5.45; FULL = 7.3; HALF = 3.55
D = json.load(open('/home/claude/sector/sens.json'))


def style(ax, grid='y'):
    for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.5); ax.tick_params(axis='y', length=0); ax.tick_params(axis='x', length=2)
    if grid: ax.grid(axis=grid, color=GRID, linewidth=0.5); ax.set_axisbelow(True)


def save(fig, name, l=0.09, r=0.99, t=0.96, b=0.14, **kw):
    plt.subplots_adjust(left=l, right=r, top=t, bottom=b, **kw); fig.savefig(O + name); plt.close(fig)


def note(ax, x, y, text, xt, yt, ha='left', c=NAVY, fs=6.1, bold=False):
    ax.annotate(text, (x, y), xytext=(xt, yt), textcoords='offset points', ha=ha, va='center', fontsize=fs, color=c, fontweight='bold' if bold else 'normal',
                arrowprops=dict(arrowstyle='-', color=SLATE, lw=0.45, shrinkA=1, shrinkB=2), bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.9))


def bands(ax, xs, lo=-0.6, hi=1.4):
    ax.axhspan(0.15, hi, color=GOOD, lw=0, zorder=0); ax.axhspan(0, 0.15, color=MID, lw=0, zorder=0); ax.axhspan(lo, 0, color=BAD, lw=0, zorder=0)
    for y, t in [(0.15 + (hi - 0.15) * 0.93, 'Buy: above 15%'), (0.075, 'Hold: 0–15%'), (lo + (0 - lo) * 0.12, 'Sell: below 0%')]:
        ax.text(xs[0], y, '  ' + t, fontsize=6, color=SLATE, va='center', fontweight='bold')


# ======================= METALS & MINING =======================
# M1. Gold price path, 2025 monthly averages and selected 2026 observations
months = np.arange(2025 + 1 / 24, 2026, 1 / 12)
g25 = [2707, 2893, 2975, 3215, 3290, 3355, 3341, 3364, 3659, 4052, 4082, 4309]
pts26 = [(2026.08, 5595), (2026.53, 3999), (2026.75, 4176), (2026.82, 4076)]
fig, ax = plt.subplots(figsize=(FULL, 2.45), dpi=300)
ax.fill_between(months, g25, color=AMBER, alpha=0.1, lw=0); ax.plot(months, g25, color=AMBER, lw=1.8, label='2025 monthly average')
xs = [months[-1]] + [p[0] for p in pts26]; ys = [g25[-1]] + [p[1] for p in pts26]
ax.plot(xs, ys, color=AMBER, lw=1.3, ls=(0, (3, 2)), label='Selected 2026 observations')
ax.scatter([p[0] for p in pts26], [p[1] for p in pts26], s=18, color=NAVY, zorder=5)
note(ax, 2026.08, 5595, 'Record ~US$5,595 (January 2026)', 14, 4, bold=True)
note(ax, 2026.53, 3999, 'Low US$3,999 (July 13): Iran conflict lifts\noil, inflation expectations and yields', -12, -16, ha='right')
note(ax, 2026.75, 4176, 'September: −8.5%; US 10-yr\nhits 5.20% on Sep 24', -10, 26, ha='right')
note(ax, 2026.82, 4076, 'Oct 27: US$4,076', 10, -26, bold=True)
ax.axhline(4000, color=STEEL, lw=0.9, ls='--'); ax.text(2025.02, 4060, 'Northwall 2027E deck: US$4,000/oz', fontsize=6.1, color=STEEL)
ax.axhline(3500, color=SLATE, lw=0.7, ls=':'); ax.text(2025.02, 3560, 'Long-term deck: US$3,500/oz', fontsize=6.1, color=SLATE)
ax.set_xlim(2025, 2027.15); ax.set_ylim(2400, 6000); ax.set_xticks([2025, 2025.5, 2026, 2026.5, 2027]); ax.set_xticklabels(['Jan 2025', 'Jul 2025', 'Jan 2026', 'Jul 2026', 'Jan 2027'])
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'{v:,.0f}')); ax.set_ylabel('US$/oz'); style(ax); ax.legend(frameon=False, fontsize=6.2, loc='upper left', bbox_to_anchor=(0.0, 0.92))
save(fig, 'm_gold_path.png', l=0.07, b=0.11)

# M2. Where our deck sits: scenarios vs deck
fig, ax = plt.subplots(figsize=(MAIN, 1.75), dpi=300)
rows = [('SSGA base case (60%), end-1Q27', 4750, 5500, STEEL), ('SSGA bear case (35%), next 6–9 months', 4000, 4750, LIGHT), ('2026 trading range to date', 3999, 5595, PALE)]
for i, (l, a, b, c) in enumerate(rows):
    y = len(rows) - 1 - i; ax.barh(y, b - a, left=a, height=0.5, color=c, ec=STEEL if c == PALE else 'none', lw=0.5)
    ax.text(a - 30, y, f'{a:,}', ha='right', va='center', fontsize=6.1, color=NAVY); ax.text(b + 30, y, f'{b:,}', ha='left', va='center', fontsize=6.1, color=NAVY)
for x, t, c, ls, ha in [(4076, ' Spot 4,076', NAVY, '-', 'left'), (4000, 'Our 2027E 4,000 ', AMBER, '--', 'right'), (3500, 'Our LT 3,500', AMBER, ':', 'center')]:
    ax.axvline(x, color=c, lw=1, ls=ls); ax.text(x, 2.62, t, ha=ha, fontsize=6, color=c, fontweight='bold')
ax.set_yticks(range(3)); ax.set_yticklabels([r[0] for r in rows][::-1], color=NAVY); ax.set_xlim(3200, 6000); ax.set_ylim(-0.5, 2.9); style(ax, 'x')
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'{v:,.0f}'))
save(fig, 'm_scenarios.png', l=0.33, b=0.13, t=0.97)

# M3. Margins: realized price vs AISC
fig, ax = plt.subplots(figsize=(HALF, 2.3), dpi=300)
names = ['Newmont\nQ3-26', 'Agnico Eagle\nQ2-26', 'Alamos\nH1-26', 'Industry AISC\nQ1-26 vs spot']
aisc = [1454, 1459, 1793, 1785]; px = [4317, 4483, 4660, 4076]
ax.bar(range(4), aisc, 0.55, color=STEEL, label='AISC'); ax.bar(range(4), np.array(px) - np.array(aisc), 0.55, bottom=aisc, color=AMBER, alpha=0.85, label='Margin')
for i, (a, p) in enumerate(zip(aisc, px)): ax.text(i, p + 60, f'US${p - a:,.0f}', ha='center', fontsize=6.2, color=NAVY, fontweight='bold'); ax.text(i, a / 2, f'{a:,}', ha='center', fontsize=5.9, color='white')
ax.set_xticks(range(4)); ax.set_xticklabels(names, fontsize=5.8); ax.set_ylim(0, 5800); ax.set_ylabel('US$/oz'); style(ax)
ax.legend(frameon=False, fontsize=6, loc='upper right', ncol=2, bbox_to_anchor=(1, 1.03))
save(fig, 'm_margins.png', l=0.15, b=0.16, t=0.97)

# M4. Implied return vs flat gold, AGI and FNV
fig, ax = plt.subplots(figsize=(FULL, 2.35), dpi=300)
bands(ax, [3000], lo=-0.25, hi=1.25)
for t, c in [('AGI', STEEL), ('FNV', AMBER)]:
    a = np.array(D['gold'][t]); ax.plot(a[:, 0], a[:, 2], color=c, lw=2, label={'AGI': 'Alamos Gold (AGI)', 'FNV': 'Franco-Nevada (FNV)'}[t])
for x, t in [(4076, 'Spot US$4,076'), (4000, ''), (3500, 'LT deck US$3,500')]:
    if t: ax.axvline(x, color=NAVY if 'Spot' in t else SLATE, lw=0.8, ls='-' if 'Spot' in t else ':'); ax.text(x + 25, 1.17, t, fontsize=6, color=NAVY, fontweight='bold')
a = np.array(D['gold']['FNV']); i = list(a[:, 0]).index(4000)
note(ax, 4000, a[i, 2], 'FNV reaches the Buy band above\n~US$3,960/oz held flat', 60, -24)
a = np.array(D['gold']['AGI']); i = list(a[:, 0]).index(3500)
note(ax, 3500, a[i, 2], 'AGI stays a Buy down to ~US$3,460/oz;\nSell below ~US$3,160/oz', -12, 40, ha='right')
ax.set_xlim(3000, 5600); ax.set_ylim(-0.25, 1.25); ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'US${v:,.0f}')); ax.set_xlabel('Gold price held flat from 2027 (US$/oz)'); ax.set_ylabel('Implied 12-month total return'); style(ax, None)
ax.legend(frameon=False, fontsize=6.4, loc='upper left', bbox_to_anchor=(0.0, 0.88))
save(fig, 'm_returns.png', l=0.08, b=0.16)

# M5. Alamos: production up, AISC down (two panels)
A = D['AGI']['m']; P = ['2025A', '2026E', '2027E', '2028E', '2029E', '2030E']
fig, (a1, a2) = plt.subplots(2, 1, figsize=(HALF, 2.6), dpi=300, sharex=True, gridspec_kw={'height_ratios': [1.25, 1]})
oz = [A['oz'][p] for p in P]; a1.bar(range(6), oz, 0.6, color=[NAVY] + [STEEL] * 5)
for i, v in enumerate(oz): a1.text(i, v + 15, f'{v:,.0f}', ha='center', fontsize=6, color=NAVY)
a1.set_ylim(0, 1150); a1.set_ylabel('Gold (koz)'); style(a1)
ai = [A['aisc'][p] for p in P]; a2.plot(range(6), ai, color=AMBER, lw=1.8, marker='o', ms=3.5)
for i, v in enumerate(ai): a2.text(i, v + 70, f'{v:,.0f}', ha='center', fontsize=6, color=NAVY)
a2.set_ylim(900, 2200); a2.set_ylabel('AISC (US$/oz)'); a2.set_xticks(range(6)); a2.set_xticklabels(P); style(a2)
save(fig, 'm_agi.png', l=0.17, b=0.1, t=0.98, hspace=0.12)

# M6. Comps (two panels)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(FULL, 1.9), dpi=300)
for ax, names, vals, title, hi in [(a1, ['Alamos (AGI)', 'Agnico Eagle (AEM)', 'Kinross (KGC)'], [13.7, 10.3, 5.8], 'Gold producers: P/CF, Q2-26 annualized', 0),
                                   (a2, ['Franco-Nevada (FNV)', 'Wheaton (WPM)', 'Royal Gold (RGLD)'], [22.2, 20.0, 14.8], 'Royalty and streaming: P/CF, H1-26 annualized', 0)]:
    y = np.arange(3)[::-1]; ax.barh(y, vals, 0.5, color=[AMBER, STEEL, STEEL])
    for yy, v in zip(y, vals): ax.text(v + 0.3, yy, f'{v:.1f}x', va='center', fontsize=6.3, color=NAVY, fontweight='bold')
    ax.set_yticks(y); ax.set_yticklabels(names, color=NAVY); ax.set_title(title, loc='left', fontsize=6.8, color=NAVY, fontweight='bold'); ax.set_xlim(0, max(vals) * 1.25); style(ax, 'x'); ax.set_xticks([])
save(fig, 'm_comps.png', l=0.13, r=0.98, b=0.05, t=0.86, wspace=0.55)

# M7. Catalyst timeline, metals
def timeline(name, ev, x0, x1, ticks, labels):
    fig, ax = plt.subplots(figsize=(FULL, 2.0), dpi=300)
    ax.axhline(0, color=NAVY, lw=1.2)
    for x, l in zip(ticks, labels): ax.plot([x, x], [-0.06, 0.06], color=NAVY, lw=0.8); ax.text(x, -0.18, l, ha='center', fontsize=6.2, color=SLATE)
    for i, (x, t, c, lvl) in enumerate(ev):
        ax.plot([x, x], [0, lvl], color=c, lw=0.7); ax.scatter([x], [0], s=22, color=c, zorder=5, edgecolor='white', lw=0.6)
        ax.text(x, lvl + (0.05 if lvl > 0 else -0.05), t, ha='center', va='bottom' if lvl > 0 else 'top', fontsize=5.9, color=NAVY, linespacing=1.25)
    ax.set_xlim(x0 - 1.6, x1); ax.set_ylim(-1.25, 1.25); ax.set_axis_off()
    save(fig, name, l=0.01, r=0.99, b=0.02, t=0.98)

timeline('m_catalysts.png', [
    (0.0, 'AGI Q3\nOct 28', STEEL, 0.45), (0.45, 'FNV Q3; first Cobre\nstockpile ounces\nNov 11', AMBER, -0.45), (1.6, 'Côté reserve and\n40ktpd plan (4Q26)', AMBER, 0.9),
    (2.1, 'AGI shaft equipping\ncomplete (4Q26)', STEEL, -1.0), (3.3, 'AGI 3-yr guidance;\nFNV 2027 guidance\n(early 2027)', NAVY, 0.45), (4.1, 'Island Gold shaft\ncommissioning (1Q27)', STEEL, -0.45),
    (6.6, 'PDA first gold\n(mid-2027)', STEEL, 0.75), (13.1, 'Magino mill to\n20,000 tpd (1Q28)', STEEL, -0.6), (25.0, 'Lynn Lake first gold\n(1H29); Stibnite\nand Copper World', NAVY, 0.6)],
    -0.6, 27.5, [0, 2.1, 5.1, 8.1, 11.1, 14.1, 17.1, 20.1, 23.1, 26.1], ['Nov 26', 'Jan 27', 'Apr 27', 'Jul 27', 'Oct 27', 'Jan 28', 'Apr 28', 'Jul 28', 'Oct 28', 'Jan 29'])

# ======================= OIL & GAS =======================
# O1. Oil: spot vs EIA STEO vs house deck
fig, ax = plt.subplots(figsize=(FULL, 2.4), dpi=300)
ax.plot([2026.875, 2027.5, 2028.5, 2029.5], [95, 80, 72, 70], color=STEEL, lw=2, marker='o', ms=4, label='Northwall WTI deck (4Q26, then annual)')
ax.plot([2026.875, 2027.5], [97.0, 79.74], color=SLATE, lw=1.4, ls='--', marker='s', ms=3.5, label='EIA STEO WTI (4Q26; 2027 average)')
ax.plot([2026.875, 2027.375, 2027.875], [104.69, 87, 74], color=AMBER, lw=1.4, ls='--', marker='s', ms=3.5, label='EIA STEO Brent (4Q26, 2Q27, 4Q27)')
ax.scatter([2026.82], [99.87], s=40, color=NAVY, zorder=6, marker='D'); ax.scatter([2026.82], [109.44], s=40, color=AMBER, zorder=6, marker='D', edgecolor=NAVY, lw=0.6)
note(ax, 2026.82, 109.44, 'Brent spot US$109.44 (Oct 27)', -14, 8, ha='right', bold=True)
note(ax, 2026.82, 99.87, 'WTI spot US$99.87', -14, -6, ha='right', bold=True)
ax.axhline(63.4, color=RED, lw=0.8, ls=':'); ax.text(2029.75, 64.6, 'WCP dividend breakeven US$63.40', fontsize=6, color=RED, ha='right')
ax.axhline(70, color=GRID, lw=0)
ax.set_xlim(2025.85, 2029.8); ax.set_ylim(55, 118); ax.set_xticks([2026.875, 2027.5, 2028.5, 2029.5]); ax.set_xticklabels(['4Q26', '2027', '2028', '2029'])
ax.set_ylabel('US$/bbl'); style(ax); ax.legend(frameon=False, fontsize=6.2, loc='upper right')
save(fig, 'o_deck.png', l=0.07, b=0.11)

# O2. Shut-ins
fig, ax = plt.subplots(figsize=(HALF, 2.0), dpi=300)
lab = ['May 2026\n(peak)', 'Aug 2026', 'Sep 2026', '4Q26\n(EIA assumption)']; v = [10.9, 5.8, 4.8, 4.5]
ax.bar(range(4), v, 0.55, color=[RED, AMBER, AMBER, LIGHT])
for i, x in enumerate(v): ax.text(i, x + 0.25, f'{x:.1f}', ha='center', fontsize=6.6, color=NAVY, fontweight='bold')
ax.set_xticks(range(4)); ax.set_xticklabels(lab, fontsize=6); ax.set_ylim(0, 12.5); ax.set_ylabel('Million bbl/d shut in'); style(ax)
save(fig, 'o_shutins.png', l=0.15, b=0.2, t=0.97)

# O3. WCS differential reference points
fig, ax = plt.subplots(figsize=(HALF, 2.0), dpi=300)
lab = ['Pre-TMX avg\n(2014–Apr 24)', 'Post-TMX avg\n(May 24–Mar 26)', 'Greenfire\nQ2-26', 'Northwall\ndeck', 'Hardisty\nOct 21, 2026']; v = [16, 13, 14.66, 15, 28]
ax.bar(range(5), v, 0.55, color=[LIGHT, LIGHT, STEEL, AMBER, RED])
for i, x in enumerate(v): ax.text(i, x + 0.6, f'~{x:.0f}' if i < 2 else f'{x:.2f}' if i == 2 else f'{x:.0f}', ha='center', fontsize=6.4, color=NAVY, fontweight='bold')
ax.set_xticks(range(5)); ax.set_xticklabels(lab, fontsize=5.5); ax.set_ylim(0, 33); ax.set_ylabel('WCS discount to WTI (US$/bbl)'); style(ax)
save(fig, 'o_wcs.png', l=0.15, b=0.22, t=0.97)

# O4. Canadian supply growth vs announced egress additions
fig, ax = plt.subplots(figsize=(HALF, 2.15), dpi=300)
ax.bar(0, 0.7, 0.5, color=STEEL); ax.text(0, 0.72, '+0.70', ha='center', fontsize=6.6, fontweight='bold', color=NAVY)
parts = [('TMX optimization\n(by end-2028)', 0.30, RED), ('Express-Platte\n(2026)', 0.03, LIGHT), ('Mainline optimization\n(2027 or later, up to)', 0.40, NAVY)]
b = 0
for t, v, c in parts:
    ax.bar(1, v, 0.5, bottom=b, color=c, alpha=0.9 if c != NAVY else 0.55); ax.text(1.3, b + v / 2, f'{t}: +{v:.2f}', va='center', fontsize=5.7, color=NAVY); b += v
ax.text(1, b + 0.02, f'+{b:.2f}', ha='center', fontsize=6.6, fontweight='bold', color=NAVY)
ax.set_xticks([0, 1]); ax.set_xticklabels(['Crude production\n2025 to 2028E', 'Announced\negress additions'], fontsize=6); ax.set_xlim(-0.5, 2.6); ax.set_ylim(0, 0.95); ax.set_ylabel('Million bbl/d'); style(ax)
save(fig, 'o_egress.png', l=0.15, b=0.17, t=0.97)

# O5. Whitecap free funds flow vs WTI and the dividend
g = D['oil']['WCP']; fig, ax = plt.subplots(figsize=(HALF, 2.15), dpi=300)
W = [60, 65, 70, 75, 80, 90, 100]; F = [596, 1030, 1465, 1900, 2335, 3204, 4073]
ax.bar(range(len(W)), F, 0.6, color=[LIGHT if w < 80 else STEEL for w in W])
ax.axhline(887, color=RED, lw=1, ls='--'); ax.text(-0.4, 4350, 'Dashed line: base dividend of C$887M', fontsize=6, color=RED)
for i, f in enumerate(F): ax.text(i, f + 70, f'{f:,}', ha='center', fontsize=5.8, color=NAVY)
ax.set_xticks(range(len(W))); ax.set_xticklabels([f'US${w}' for w in W], fontsize=5.8); ax.set_ylabel('2027E free funds flow (C$M)'); ax.set_ylim(0, 4600); style(ax)
ax.set_xlabel('WTI held flat from 2027')
save(fig, 'o_wcp_fff.png', l=0.17, b=0.2, t=0.97)

# O6. Greenfire target grid: WTI x WCS differential
G = D['gfrgrid']; fig, ax = plt.subplots(figsize=(HALF, 2.2), dpi=300)
diffs = [15, 20, 25, 28]
for r, (w, row) in enumerate(G):
    for c, tv in enumerate(row):
        ret = tv / 7.0 - 1; col = GOOD if ret > 0.15 else MID if ret >= 0 else BAD
        y = len(G) - 1 - r; ax.add_patch(Rectangle((c, y), 1, 1, fc=col, ec='white', lw=1.5))
        bold = (w == 80 and c == 0); ax.text(c + 0.5, y + 0.5, f'US${tv:.2f}', ha='center', va='center', fontsize=6.4, color=NAVY, fontweight='bold' if bold else 'normal')
        if bold: ax.add_patch(Rectangle((c, y), 1, 1, fc='none', ec=NAVY, lw=1.2))
ax.set_xlim(0, 4); ax.set_ylim(0, len(G)); ax.set_xticks(np.arange(4) + 0.5); ax.set_xticklabels([f'US${d}' for d in diffs]); ax.set_yticks(np.arange(len(G)) + 0.5)
ax.set_yticklabels([f'US${w}' for w, _ in G][::-1]); ax.set_xlabel('WCS discount to WTI, held from 2027'); ax.set_ylabel('WTI from 2027')
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(length=0)
save(fig, 'o_gfr_grid.png', l=0.17, b=0.18, t=0.98)

# O7. Implied return vs flat WTI, WCP and GFR
fig, ax = plt.subplots(figsize=(FULL, 2.3), dpi=300)
bands(ax, [50], lo=-0.6, hi=1.0)
for t, c, nm in [('WCP', STEEL, 'Whitecap (WCP)'), ('GFR', AMBER, 'Greenfire (GFR), US$15 WCS discount')]:
    a = np.array(D['oil'][t]); ax.plot(a[:, 0], a[:, 2], color=c, lw=2, label=nm)
ax.axvline(99.87, color=NAVY, lw=0.8); ax.text(99.4, 0.9, 'WTI spot US$99.87', fontsize=6, color=NAVY, fontweight='bold', ha='right')
ax.axvline(80, color=SLATE, lw=0.8, ls=':'); ax.text(80.5, 0.9, 'Our 2027E deck US$80', fontsize=6, color=SLATE, fontweight='bold')
a = np.array(D['oil']['WCP']); note(ax, 77.5, a[list(a[:, 0]).index(77.5), 2], 'WCP: Hold below ~US$79,\nSell below ~US$74', -70, 34)
a = np.array(D['oil']['GFR']); note(ax, 70, a[list(a[:, 0]).index(70), 2], 'GFR: Hold below ~US$78,\nSell below ~US$69', 40, -26)
ax.set_xlim(50, 110); ax.set_ylim(-0.6, 1.0); ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f'US${v:,.0f}')); ax.set_xlabel('WTI held flat from 2027 (US$/bbl)'); ax.set_ylabel('Implied 12-month total return'); style(ax, None)
ax.legend(frameon=False, fontsize=6.4, loc='upper left', bbox_to_anchor=(0, 0.86))
save(fig, 'o_returns.png', l=0.08, b=0.16)

# O8. Comps
fig, (a1, a2) = plt.subplots(1, 2, figsize=(FULL, 1.9), dpi=300)
y = np.arange(3)[::-1]
a1.barh(y + 0.18, [5.0, 8.6, 5.0], 0.34, color=[AMBER, STEEL, STEEL], label='EV/CF (x)'); a1.barh(y - 0.18, [14.9, 3.0, 13.3], 0.34, color=[AMBER, STEEL, STEEL], alpha=0.45, label='FCF yield (%)')
for yy, a, b in zip(y, [5.0, 8.6, 5.0], [14.9, 3.0, 13.3]): a1.text(a + 0.3, yy + 0.18, f'{a:.1f}x', va='center', fontsize=6.1, color=NAVY, fontweight='bold'); a1.text(b + 0.3, yy - 0.18, f'{b:.1f}%', va='center', fontsize=6.1, color=NAVY)
a1.set_yticks(y); a1.set_yticklabels(['Whitecap (WCP)', 'Tourmaline (TOU)', 'Strathcona (SCR)'], color=NAVY); a1.set_xlim(0, 19); a1.set_xticks([]); style(a1, 'x')
a1.set_title('Producers: EV/CF (solid) and FCF yield (light), Q2-26 annualized', loc='left', fontsize=6.6, color=NAVY, fontweight='bold')
a2.barh(y, [86, 93, 146], 0.5, color=[AMBER, STEEL, STEEL])
for yy, v in zip(y, [86, 93, 146]): a2.text(v + 2, yy, f'C${v}k', va='center', fontsize=6.3, color=NAVY, fontweight='bold')
a2.set_yticks(y); a2.set_yticklabels(['Greenfire (GFR)', 'Strathcona (SCR)', 'Athabasca Oil (ATH)'], color=NAVY); a2.set_xlim(0, 175); a2.set_xticks([]); style(a2, 'x')
a2.set_title('Heavy oil: EV per flowing barrel (C$ thousands)', loc='left', fontsize=6.6, color=NAVY, fontweight='bold')
save(fig, 'o_comps.png', l=0.14, r=0.98, b=0.05, t=0.86, wspace=0.6)

# O9. Catalyst timeline, oil and gas
timeline('o_catalysts.png', [
    (0.0, 'Oil above US$100;\nHormuz convoys\n(now)', RED, 0.5), (0.6, 'WCP and GFR Q3\nresults (dates TBC)', NAVY, -0.5), (1.6, 'GFR: first quarter\nwith Connacher', AMBER, 0.95),
    (1.6, 'WCP 2027 budget\n(TBC)', STEEL, -1.05), (5.5, 'EIA: Middle East output\nback near normal by\nend-2Q27', SLATE, 0.5), (8.0, 'Enbridge Mainline\noptimization (2027+)', NAVY, -0.6),
    (13.0, 'EIA: Brent ~US$74\nin 4Q27', SLATE, 0.6), (25.0, 'TMX optimization\n+300 kbbl/d\n(end-2028)', RED, -0.6)],
    -0.6, 27.5, [0, 2.1, 5.1, 8.1, 11.1, 14.1, 17.1, 20.1, 23.1, 26.1], ['Nov 26', 'Jan 27', 'Apr 27', 'Jul 27', 'Oct 27', 'Jan 28', 'Apr 28', 'Jul 28', 'Oct 28', 'Jan 29'])
print('charts ok')
