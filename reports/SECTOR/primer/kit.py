"""Layout kit for the Northwall primer: sections, callouts, tables and numbered exhibits."""
import html as _h

B = []          # body HTML, in order
EX = [0]        # exhibit counter
TOC = []        # (anchor, title, level)


def esc(s):
    return _h.escape(s, quote=False)


def sec(title, anchor, lede=None, newpage=False):
    TOC.append((anchor, title, 1))
    B.append(f'<h1 class="sec{" np" if newpage else ""}" id="{anchor}">{title}</h1>')
    if lede: B.append(f'<p class="lede">{lede}</p>')


def h2(title, anchor=None):
    if anchor: TOC.append((anchor, title, 2))
    B.append(f'<h2{f" id={chr(34)}{anchor}{chr(34)}" if anchor else ""}>{title}</h2>')


def h3(title):
    B.append(f'<h3>{title}</h3>')


def p(*paras):
    for x in paras: B.append(f'<p>{x}</p>')


def side(text):
    """Pull-quote in the left margin, aligned with the next paragraph."""
    B.append(f'<div class="side">{text}</div>')


def ul(items, cls=''):
    B.append(f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>')


def ol(items):
    B.append('<ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>')


def table(head, rows, widths=None, cls='', bold_last=False, num_cols=()):
    cg = ''.join(f'<col style="width:{w}">' for w in widths) if widths else ''
    th = ''.join(f'<th{" class=n" if i in num_cols else ""}>{h}</th>' for i, h in enumerate(head))
    tr = ''
    for ri, r in enumerate(rows):
        b = ' class="b"' if (bold_last and ri == len(rows) - 1) or (isinstance(r, tuple) and r and r[0] == '__b__') else ''
        cells = r[1:] if isinstance(r, tuple) and r and r[0] == '__b__' else r
        tr += f'<tr{b}>' + ''.join(f'<td{" class=n" if i in num_cols else ""}>{c}</td>' for i, c in enumerate(cells)) + '</tr>'
    return f'<table class="t {cls}"><colgroup>{cg}</colgroup><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def tbl(*a, **k):
    B.append(table(*a, **k))


def exhibit(title, body, source, wide=False, note=None):
    EX[0] += 1
    img = f'<img src="{body}">' if body.endswith('.png') else body
    B.append(f'<div class="ex{" wide" if wide else ""}"><div class="ext">Exhibit {EX[0]}: {title}</div>{img}'
             + (f'<div class="exn">{note}</div>' if note else '') + f'<div class="src">Source: {source}</div></div>')
    return EX[0]


def nextex():
    return EX[0] + 1


def box(title, body, cls='case'):
    B.append(f'<div class="{cls}"><div class="bt">{title}</div>{body}</div>')


def raw(x):
    B.append(x)
