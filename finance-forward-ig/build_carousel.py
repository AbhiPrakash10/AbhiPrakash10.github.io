#!/usr/bin/env python3
"""Finance Forward Instagram carousel builder.
Usage: python3 build_carousel.py piece.json outdir
piece.json keys:
  k  column kicker in caps, e.g. "THE WATCHLIST"
  t  headline as a list of 2-3 short lines
  d  one-sentence dek
  n  EITHER three [number, label] pairs (first is the hero stat) ...
  l  ... OR a list of 3-7 short items, with lk = kicker for that slide
  v  the author's view, at most 30 words
  vk optional kicker for slide 3 (default "MY VIEW")
Writes 1.png, 2.png, 3.png (1080x1350) into outdir.
"""
import json, math, subprocess, sys, glob, os
from PIL import ImageFont
def _font(bold):
    pats = ["LiberationSans-Bold" if bold else "LiberationSans-Regular", "Arial Bold" if bold else "Arial.ttf", "DejaVuSans-Bold" if bold else "DejaVuSans.ttf"]
    fs = glob.glob("/usr/share/fonts/**/*.ttf", recursive=True) + glob.glob("/Library/Fonts/*.ttf") + glob.glob("/System/Library/Fonts/Supplemental/*.ttf")
    for p in pats:
        for f in fs:
            if p in f: return f
    raise SystemExit("No usable font found; install fonts-liberation")
FP, FB = _font(False), _font(True)
def tw(t, s, b=0): return ImageFont.truetype(FB if b else FP, s).getlength(t)
def wrap(t, s, mw, b=0):
    o, c = [], ""
    for w in t.split():
        n = (c + " " + w).strip()
        if tw(n, s, b) > mw and c: o.append(c); c = w
        else: c = n
    if c: o.append(c)
    return o
N, P, R, C, B, O, K, G, U = "#1A2233", "#232D42", "#2B3650", "#F4EEE3", "#9CC1DE", "#E2AE6C", "#E9A1AC", "#A9B4C6", "#34405A"
W, H = 1080, 1350
esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;")
def logo(x, y, size, i):
    s = size / 512
    dots = "".join(f'<circle cx="{256+164*math.cos(math.radians(a)):.1f}" cy="{256+164*math.sin(math.radians(a)):.1f}" r="8" fill="{C}"/>' for a in range(0, 360, 45))
    return (f'<g transform="translate({x},{y}) scale({s})"><defs><clipPath id="l{i}"><circle cx="226.5" cy="256" r="55"/></clipPath></defs>'
            f'<circle cx="256" cy="256" r="186" fill="none" stroke="{C}" stroke-width="16"/><circle cx="256" cy="256" r="142" fill="none" stroke="{C}" stroke-width="6"/>{dots}'
            f'<circle cx="285.5" cy="256" r="55" fill="{K}" clip-path="url(#l{i})"/><circle cx="226.5" cy="256" r="64.5" fill="none" stroke="{B}" stroke-width="20"/>'
            f'<circle cx="285.5" cy="256" r="64.5" fill="none" stroke="{O}" stroke-width="20"/></g>')
def T(x, y, s, f, t, b=0, e=""):
    return f'<text x="{x}" y="{y}" font-size="{s}"{" font-weight=" + chr(34) + "bold" + chr(34) if b else ""} fill="{f}"{e}>{esc(t)}</text>'
def foot(n): return f'<line x1="70" y1="1240" x2="1010" y2="1240" stroke="{U}" stroke-width="2"/>' + logo(70, 1258, 56, "f") + T(140, 1296, 28, C, "Finance Forward", 1) + T(1010, 1296, 24, G, f"{n} / 3", 0, ' text-anchor="end"')
def kick(t): return T(70, 130, 30, O, t, 1, ' letter-spacing="6"')
def svg(b): return f'<svg font-family="Arial, Liberation Sans, Helvetica, sans-serif" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{N}"/>{b}</svg>'
def build(p, out):
    os.makedirs(out, exist_ok=True)
    fs = 116
    while max(tw(l, fs, 1) for l in p["t"]) > 780: fs -= 4
    b = kick(p["k"]) + logo(810, 60, 200, "c"); y = 360
    for l in p["t"]: b += T(70, y, fs, C, l, 1); y += int(fs * 1.1)
    y += 30
    for l in wrap(p["d"], 40, 940)[:6]: b += T(70, y, 40, B, l); y += 52
    if "n" in p:
        num, lab = p["n"][0]; b += f'<rect x="70" y="1010" width="940" height="170" rx="14" fill="{P}"/>' + T(104, 1122, 92, O, num, 1)
        lx = 104 + tw(num, 92, 1) + 40; ll = wrap(lab, 30, 1010 - lx - 30)[:3]; y0 = 1105 - (len(ll) - 1) * 19
        for j, l in enumerate(ll): b += T(lx, y0 + j * 38, 30, G, l)
    else: b += T(70, 1150, 34, O, "Swipe to see them", 1)
    s1 = svg(b + foot(1))
    if "n" in p:
        b = kick("BY THE NUMBERS")
        for j, (num, lab) in enumerate(p["n"][:3]):
            y = 200 + j * 330; b += f'<rect x="70" y="{y}" width="940" height="300" rx="14" fill="{R}"/>' + T(110, y + 150, 128, O if j == 0 else C, num, 1)
            for q, l in enumerate(wrap(lab, 34, 860)[:2]): b += T(110, y + 215 + q * 44, 34, G, l)
    else:
        b = kick(p["lk"]); n = len(p["l"]); rh = min(170, int(1000 / n))
        for j, l in enumerate(p["l"]):
            y = 200 + j * rh; b += f'<rect x="70" y="{y}" width="940" height="{rh-18}" rx="14" fill="{R}"/>' + T(110, y + (rh - 18) / 2 + 22, 60, B, str(j + 1), 1)
            ls = wrap(l, 38, 800, 1)[:2]; yy = y + (rh - 18) / 2 + 14 - (len(ls) - 1) * 23
            for q, x in enumerate(ls): b += T(190, yy + q * 46, 38, C, x, 1)
    s2 = svg(b + foot(2))
    b = kick(p.get("vk", "MY VIEW")) + logo(870, 60, 140, "v"); y = 330
    for l in wrap(p["v"], 58, 940, 1)[:8]: b += T(70, y, 58, C, l, 1); y += 76
    b += f'<rect x="70" y="1010" width="940" height="120" rx="14" fill="{P}"/>' + T(104, 1084, 38, O, "Full piece: link in bio", 1)
    if "n" in p: b += T(70, 1190, 22, G, "A view about the deal, not a forecast or a recommendation.")
    b += T(70, 1220, 22, G, "Educational only, not investment advice.")
    s3 = svg(b + foot(3))
    for i, s in enumerate((s1, s2, s3), 1):
        sp = os.path.join(out, f"{i}.svg"); open(sp, "w").write(s)
        subprocess.run(["rsvg-convert", sp, "-o", os.path.join(out, f"{i}.png")], check=True); os.remove(sp)
if __name__ == "__main__":
    build(json.load(open(sys.argv[1])), sys.argv[2])
