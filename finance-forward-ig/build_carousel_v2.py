#!/usr/bin/env python3
"""Finance Forward Instagram carousel builder, v2 design.
Usage: python3 build_carousel_v2.py piece.json outdir
Same piece.json keys as build_carousel.py:
  k  column kicker in caps, e.g. "THE WATCHLIST"
  t  headline as a list of 2-3 short lines (words containing a digit are highlighted)
  d  one-sentence dek
  n  EITHER three [number, label] pairs (first is the hero stat) ...
  l  ... OR a list of 3-7 short items, with lk = kicker for that slide
  v  the author's view, at most 30 words
  vk optional kicker for slide 3 (default "MY VIEW")
Writes 1.png, 2.png, 3.png (1080x1350) into outdir.
Uses Inter Display when installed, otherwise falls back to Liberation Sans / Arial / DejaVu.
"""
import json, math, subprocess, sys, glob, os, re
from PIL import ImageFont

_FILES = (glob.glob("/usr/share/fonts/**/*.otf", recursive=True) + glob.glob("/usr/share/fonts/**/*.ttf", recursive=True)
          + glob.glob("/Library/Fonts/*.ttf") + glob.glob("/System/Library/Fonts/Supplemental/*.ttf"))
def _find(*names):
    for n in names:
        for f in _FILES:
            if os.path.basename(f).split(".")[0] == n: return f
    return None
if _find("InterDisplay-ExtraBold") and _find("InterDisplay-Bold") and _find("InterDisplay-Regular"):
    FAMILY = "Inter Display"
    FONT = {400: _find("InterDisplay-Regular"), 700: _find("InterDisplay-Bold"), 800: _find("InterDisplay-ExtraBold")}
else:
    FAMILY = "Arial, Liberation Sans, Helvetica, DejaVu Sans, sans-serif"
    reg = _find("LiberationSans-Regular", "Arial", "DejaVuSans"); bold = _find("LiberationSans-Bold", "Arial Bold", "DejaVuSans-Bold")
    if not (reg and bold): raise SystemExit("No usable font found; install fonts-inter or fonts-liberation")
    FONT = {400: reg, 700: bold, 800: bold}

def tw(t, s, w=400, ls=0): return ImageFont.truetype(FONT[w], s).getlength(t) + ls * len(t)
def wrap(t, s, mw, w=400):
    o, c = [], ""
    for word in t.split():
        n = (c + " " + word).strip()
        if tw(n, s, w) > mw and c: o.append(c); c = word
        else: c = n
    if c: o.append(c)
    return o

NAVY, PANEL, CARD, CREAM, BLUE, GOLD, PINK, GREY, RULE = "#1A2233", "#232D42", "#2B3650", "#F4EEE3", "#9CC1DE", "#E2AE6C", "#E9A1AC", "#A9B4C6", "#34405A"
W, H = 1080, 1350
HANDLE = "@financeforward_1"
esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;")

def T(x, y, s, fill, t, w=400, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{fill}"{extra}>{esc(t)}</text>'
def logo(x, y, size, i):
    s = size / 512
    dots = "".join(f'<circle cx="{256+164*math.cos(math.radians(a)):.1f}" cy="{256+164*math.sin(math.radians(a)):.1f}" r="8" fill="{CREAM}"/>' for a in range(0, 360, 45))
    return (f'<g transform="translate({x},{y}) scale({s})"><defs><clipPath id="l{i}"><circle cx="226.5" cy="256" r="55"/></clipPath></defs>'
            f'<circle cx="256" cy="256" r="186" fill="none" stroke="{CREAM}" stroke-width="16"/><circle cx="256" cy="256" r="142" fill="none" stroke="{CREAM}" stroke-width="6"/>{dots}'
            f'<circle cx="285.5" cy="256" r="55" fill="{PINK}" clip-path="url(#l{i})"/><circle cx="226.5" cy="256" r="64.5" fill="none" stroke="{BLUE}" stroke-width="20"/>'
            f'<circle cx="285.5" cy="256" r="64.5" fill="none" stroke="{GOLD}" stroke-width="20"/></g>')
def backdrop(cx, cy):
    rings = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{CREAM}" stroke-opacity="0.055" stroke-width="3"/>' for r in (210, 330, 450, 570))
    return (f'<defs><radialGradient id="glow" cx="{cx}" cy="{cy}" r="760" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{BLUE}" stop-opacity="0.20"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/><rect width="{W}" height="{H}" fill="url(#glow)"/>{rings}')
def head(kicker):
    """Top bar: brand on the left, column pill on the right."""
    pw = tw(kicker, 24, 700, 4) + 52
    return (logo(70, 62, 60, "h") + T(144, 102, 26, CREAM, "FINANCE FORWARD", 700, ' letter-spacing="3"')
            + f'<rect x="{1010-pw:.0f}" y="66" width="{pw:.0f}" height="52" rx="26" fill="none" stroke="{GOLD}" stroke-width="2.5"/>'
            + T(1010 - pw / 2 + 2, 101, 24, GOLD, kicker, 700, ' letter-spacing="4" text-anchor="middle"'))
def foot(n):
    dots, x = "", 1010
    for i in (3, 2, 1):
        w = 44 if i == n else 14; x -= w
        dots += f'<rect x="{x}" y="1283" width="{w}" height="14" rx="7" fill="{GOLD if i == n else RULE}"/>'; x -= 12
    return f'<line x1="70" y1="1240" x2="1010" y2="1240" stroke="{RULE}" stroke-width="2"/>' + T(70, 1300, 28, GREY, HANDLE, 700) + dots
def svg(body, cx=930, cy=180):
    return f'<svg font-family="{FAMILY}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{backdrop(cx, cy)}{body}</svg>'
def arrow(x, y, c, s=1.0):
    return f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M0 0H44M28 -16L44 0L28 16"/></g>'

def build(p, out):
    os.makedirs(out, exist_ok=True)
    # ---------- slide 1: cover ----------
    fs = 156
    while max(tw(l, fs, 800, -fs * 0.025) for l in p["t"]) > 940: fs -= 4
    b = head(p["k"]); y = 250 + int(fs * 0.86)
    for l in p["t"]:
        spans = "".join(f'<tspan fill="{GOLD if re.search(r"[0-9]", w_) else CREAM}">{esc(w_)} </tspan>' for w_ in l.split())
        b += f'<text x="66" y="{y}" font-size="{fs}" font-weight="800" letter-spacing="{-fs*0.025:.1f}" xml:space="preserve">{spans}</text>'
        y += int(fs * 1.04)
    y += 6 - int(fs * 0.55)
    b += f'<rect x="70" y="{y}" width="120" height="10" rx="5" fill="{GOLD}"/>'; y += 78
    dw = 940; dl = wrap(p["d"], 42, dw)
    while dw > 600 and len(wrap(p["d"], 42, dw - 20)) == len(dl): dw -= 20  # balance lines, no orphan word
    for l in wrap(p["d"], 42, dw)[:4]: b += T(70, y, 42, BLUE, l); y += 56
    if "n" in p:
        num, lab = p["n"][0]
        b += f'<rect x="70" y="1010" width="940" height="170" rx="20" fill="{PANEL}"/><rect x="70" y="1010" width="12" height="170" rx="6" fill="{GOLD}"/>'
        b += T(116, 1127, 96, GOLD, num, 800, ' letter-spacing="-2"')
        lx = 116 + tw(num, 96, 800, -2) + 36; ll = wrap(lab, 30, 880 - lx)[:3]; y0 = 1106 - (len(ll) - 1) * 19
        for j, l in enumerate(ll): b += T(lx, y0 + j * 38, 30, CREAM, l)
        b += f'<circle cx="940" cy="1095" r="36" fill="{GOLD}"/>' + arrow(918, 1095, NAVY)
    else:
        b += f'<rect x="70" y="1050" width="470" height="100" rx="50" fill="{GOLD}"/>' + T(116, 1113, 36, NAVY, "Swipe to see them", 700) + arrow(456, 1100, NAVY, 0.8)
    s1 = svg(b + foot(1))
    # ---------- slide 2: numbers or list ----------
    if "n" in p:
        b = head("BY THE NUMBERS")
        for j, (num, lab) in enumerate(p["n"][:3]):
            y = 190 + j * 340; c = (GOLD, BLUE, PINK)[j]
            b += f'<rect x="70" y="{y}" width="940" height="310" rx="20" fill="{CARD}"/><rect x="70" y="{y}" width="12" height="310" rx="6" fill="{c}"/>'
            b += T(962, y + 66, 28, GREY, f"0{j+1}", 700, ' text-anchor="end" letter-spacing="2"')
            ns = 140
            while tw(num, ns, 800, -3) > 760: ns -= 6
            b += T(116, y + 168, ns, c, num, 800, ' letter-spacing="-3"')
            for q, l in enumerate(wrap(lab, 36, 840)[:2]): b += T(118, y + 230 + q * 46, 36, CREAM, l)
    else:
        b = head(p["lk"]); n = len(p["l"]); rh = min(180, int(1030 / n))
        for j, l in enumerate(p["l"]):
            y = 180 + j * rh; c = (GOLD, BLUE, PINK)[j % 3]; mid = y + (rh - 18) / 2
            b += f'<rect x="70" y="{y}" width="940" height="{rh-18}" rx="18" fill="{CARD}"/><rect x="70" y="{y}" width="12" height="{rh-18}" rx="6" fill="{c}"/>'
            b += T(116, mid + 22, 62, c, str(j + 1), 800)
            ls_ = wrap(l, 38, 780, 700)[:2]; yy = mid + 14 - (len(ls_) - 1) * 23
            for q, x in enumerate(ls_): b += T(196, yy + q * 46, 38, CREAM, x, 700)
    s2 = svg(b + foot(2), 150, 1250)
    # ---------- slide 3: view and call to action ----------
    b = head(p.get("vk", "MY VIEW"))
    b += T(58, 400, 300, GOLD, "“", 800)
    vs = 62; lines = wrap(p["v"], vs, 940, 700)
    while len(lines) > 6 and vs > 44: vs -= 4; lines = wrap(p["v"], vs, 940, 700)
    y = 390
    for l in lines[:8]: b += T(70, y, vs, CREAM, l, 700, ' letter-spacing="-0.5"'); y += int(vs * 1.3)
    y += 10
    b += f'<rect x="70" y="{y}" width="64" height="6" rx="3" fill="{GOLD}"/>' + T(152, y + 14, 30, BLUE, "Abhi Prakash, Finance Forward", 700)
    b += T(70, 985, 30, CREAM, f"Save this for later. Follow {HANDLE} for more.")
    b += f'<rect x="70" y="1020" width="940" height="116" rx="58" fill="{GOLD}"/>' + T(122, 1092, 40, NAVY, "Read the full piece: link in bio", 800) + arrow(910, 1078, NAVY)
    if "n" in p: b += T(70, 1186, 22, GREY, "A view about the deal, not a forecast or a recommendation.")
    b += T(70, 1216, 22, GREY, "Educational only, not investment advice.")
    s3 = svg(b + foot(3), 930, 180)
    for i, s in enumerate((s1, s2, s3), 1):
        sp = os.path.join(out, f"{i}.svg"); open(sp, "w").write(s)
        subprocess.run(["rsvg-convert", sp, "-o", os.path.join(out, f"{i}.png")], check=True); os.remove(sp)

if __name__ == "__main__":
    build(json.load(open(sys.argv[1])), sys.argv[2])
