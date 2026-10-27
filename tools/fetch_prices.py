"""Fetch delayed commodity and market prices for the site's market tape.

Writes a JSON file: {"as_of": ISO-8601 UTC, "source": "...", "items": [{id, name, unit, price, prev, dp}]}.
Tries Yahoo Finance first and Stooq second. Any item that fails keeps its last published value,
read from the live site, so the tape never goes blank. WCS has no free public feed, so it is shown
as WTI less the house WCS differential and labelled as an estimate.

Usage: python tools/fetch_prices.py OUT.json [--previous URL]
"""
import csv, io, json, sys, time, urllib.request, datetime, os

ITEMS = [  # id, display name, unit, Yahoo symbol, Stooq symbol
    ("BRENT", "Brent", "US$/bbl", "BZ=F", "cb.f"),
    ("WTI", "WTI", "US$/bbl", "CL=F", "cl.f"),
    ("NATGAS", "Henry Hub gas", "US$/MMBtu", "NG=F", "ng.f"),
    ("GOLD", "Gold", "US$/oz", "GC=F", "gc.f"),
    ("SILVER", "Silver", "US$/oz", "SI=F", "si.f"),
    ("COPPER", "Copper", "US$/lb", "HG=F", "hg.f"),
    ("PLATINUM", "Platinum", "US$/oz", "PL=F", "pl.f"),
    ("PALLADIUM", "Palladium", "US$/oz", "PA=F", "pa.f"),
    ("USDCAD", "USD/CAD", "", "CAD=X", "usdcad"),
    ("UST10", "US 10-yr", "yield", "^TNX", "10usy.b"),
]
UA = {"User-Agent": "Mozilla/5.0 (compatible; NorthwallResearch/1.0; +https://github.com/kosherite/Northwall-Research)"}


def get(url, timeout=15):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def yahoo(sym):
    j = json.loads(get(f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range=5d&interval=1d"))
    m = j["chart"]["result"][0]["meta"]
    price = m.get("regularMarketPrice")
    prev = m.get("chartPreviousClose") or m.get("previousClose")
    closes = [c for c in (j["chart"]["result"][0].get("indicators", {}).get("quote", [{}])[0].get("close") or []) if c is not None]
    if len(closes) >= 2:
        prev = closes[-2]
    if price is None:
        raise ValueError("no price")
    return float(price), (float(prev) if prev else None)


def stooq(sym):
    rows = list(csv.DictReader(io.StringIO(get(f"https://stooq.com/q/l/?s={sym}&f=sd2t2ohlc&h&e=csv"))))
    c, o = rows[0].get("Close"), rows[0].get("Open")
    if not c or c == "N/D":
        raise ValueError("no price")
    return float(c), (float(o) if o and o != "N/D" else None)


def previous(url):
    try:
        return {i["id"]: i for i in json.loads(get(url, 10)).get("items", [])}
    except Exception:
        return {}


def wcs_diff():
    here = os.path.dirname(os.path.abspath(__file__))
    for p in (os.path.join(here, "..", "app", "seed_full.json"),):
        try:
            d = json.load(open(p))["deck"]["series"]["wcs_diff"]["values"]
            return float(d.get("H2-26E") or d.get("2027E"))
        except Exception:
            pass
    return None


def main():
    out = sys.argv[1]
    prev_url = sys.argv[sys.argv.index("--previous") + 1] if "--previous" in sys.argv else None
    last = previous(prev_url) if prev_url else {}
    items, sources = [], set()
    for iid, name, unit, ysym, ssym in ITEMS:
        got = None
        for src, fn, sym in (("Yahoo Finance", yahoo, ysym), ("Stooq", stooq, ssym)):
            try:
                got = fn(sym); sources.add(src); break
            except Exception as e:
                print(f"{iid}: {src} failed ({e})", file=sys.stderr)
            time.sleep(0.3)
        if got:
            price, prv = got
            items.append({"id": iid, "name": name, "unit": unit, "price": round(price, 4), "prev": prv and round(prv, 4),
                          "dp": round((price / prv - 1) * 100, 2) if prv else None})
        elif iid in last:
            items.append({**last[iid], "stale": True})
    wti = next((i for i in items if i["id"] == "WTI"), None)
    diff = wcs_diff()
    if wti and diff is not None:
        wcs, wcs_prev = wti["price"] - diff, (wti["prev"] - diff) if wti.get("prev") else None
        items.append({"id": "WCS", "name": "WCS (est.)", "unit": f"US$/bbl, WTI less US${diff:g} house diff.", "price": round(wcs, 2),
                      "prev": wcs_prev and round(wcs_prev, 2), "dp": round((wcs / wcs_prev - 1) * 100, 2) if wcs_prev else None})
    doc = {"as_of": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "source": ", ".join(sorted(sources)) or "previous values", "items": items}
    json.dump(doc, open(out, "w"), indent=1)
    print(f"{len(items)} prices written to {out} from {doc['source']}")


if __name__ == "__main__":
    import urllib.parse
    main()
