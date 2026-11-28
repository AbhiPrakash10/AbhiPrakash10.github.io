#!/usr/bin/env python3
"""Finance Forward article image builder (cover + bar chart), 1456 px wide, brand style.
Usage: python3 build_article_images.py <folder>/spec.json <folder>
spec.json keys:
  prefix   file prefix, e.g. "bricks"
  kicker   column name in caps
  title    list of 1-2 headline lines; "gold" = index of the line shown in gold (optional)
  dek      list of 1-2 short lines under the headline
  stats    exactly four [number, label line 1, label line 2]; the first is shown in gold
  sources  one short sources line for the footer
  chart    optional: {"name", "title", "subtitle", "note",
            "rows": [[label, value, text, "blue"|"gold"|"grey"], ...]}  (3 to 6 rows, horizontal bars)
Writes <prefix>-cover.png (1456x816) and <prefix>-<chart name>.png. Needs rsvg-convert and Inter Display.
Every number must come from the piece's numbers ledger. Open both PNGs and check nothing is cut off.
"""
import json, math, subprocess, sys, os
NAVY, CARD, CREAM, BLUE, GOLD, PINK, GREY, RULE = "#1A2233","#232D42","#F4EEE3","#9CC1DE","#E2AE6C","#E9A1AC","#A9B4C6","#34405A"
COL = {"blue": BLUE, "gold": GOLD, "grey": GREY}
FAM = "Inter Display, Inter, Liberation Sans, Arial, sans-serif"
esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;")
def T(x, y, s, fill, t, w=400, extra=""): return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{fill}"{extra}>{esc(t)}</text>'
def logo(x, y, size, i):
    s = size / 512
    dots = "".join(f'<circle cx="{256+164*math.cos(math.radians(a)):.1f}" cy="{256+164*math.sin(math.radians(a)):.1f}" r="8" fill="{CREAM}"/>' for a in range(0, 360, 45))
    return (f'<g transform="translate({x},{y}) scale({s})"><defs><clipPath id="l{i}"><circle cx="226.5" cy="256" r="55"/></clipPath></defs>'
            f'<circle cx="256" cy="256" r="186" fill="none" stroke="{CREAM}" stroke-width="16"/><circle cx="256" cy="256" r="142" fill="none" stroke="{CREAM}" stroke-width="6"/>{dots}'
            f'<circle cx="285.5" cy="256" r="55" fill="{PINK}" clip-path="url(#l{i})"/><circle cx="226.5" cy="256" r="64.5" fill="none" stroke="{BLUE}" stroke-width="20"/>'
            f'<circle cx="285.5" cy="256" r="64.5" fill="none" stroke="{GOLD}" stroke-width="20"/></g>')
def foot(H, src):
    return (f'<line x1="70" y1="{H-78}" x2="1386" y2="{H-78}" stroke="{RULE}" stroke-width="2"/>' + logo(70, H-66, 44, "f")
            + T(126, H-34, 22, CREAM, "Finance Forward", 700) + T(1386, H-35, 18, GREY, src, 400, ' text-anchor="end"'))
def save(out, name, W, H, body):
    svg = f'<svg font-family="{FAM}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{NAVY}"/>{body}</svg>'
    p = os.path.join(out, name + ".svg"); open(p, "w").write(svg)
    subprocess.run(["rsvg-convert", p, "-o", os.path.join(out, name + ".png")], check=True); os.remove(p)

def cover(p, out):
    W, H = 1456, 816
    b = T(70, 132, 26, GOLD, p["kicker"], 700, ' letter-spacing="6"')
    for i, line in enumerate(p["title"]):
        b += T(70, 238 + i * 100, 84, GOLD if p.get("gold") == i else CREAM, line, 800)
    y = 238 + (len(p["title"]) - 1) * 100 + 62
    for i, line in enumerate(p["dek"]): b += T(70, y + i * 40, 30, BLUE, line)
    b += logo(1146, 90, 220, "c")
    for i, (n, l1, l2) in enumerate(p["stats"]):
        x = 70 + i * 334
        b += (f'<rect x="{x}" y="510" width="314" height="200" rx="12" fill="{CARD}"/>' + T(x+24, 584, 56, GOLD if i == 0 else CREAM, n, 800)
              + T(x+24, 628, 19, GREY, l1) + T(x+24, 654, 19, GREY, l2))
    save(out, p["prefix"] + "-cover", W, H, b + foot(H, "Sources: " + p["sources"]))

def chart(p, out):
    c = p["chart"]; rows = c["rows"]; W = 1456; H = 340 + len(rows) * 112
    b = T(70, 92, 40, CREAM, c["title"], 700) + T(70, 134, 24, BLUE, c["subtitle"]) + logo(1300, 50, 76, "c")
    scale = 1070 / max(r[1] for r in rows)
    for i, (lab, v, txt, col) in enumerate(rows):
        y = 200 + i * 112
        b += (T(70, y, 22, CREAM, lab, 700) + f'<rect x="70" y="{y+14}" width="{v*scale:.0f}" height="46" rx="4" fill="{COL[col]}"/>'
              + T(70 + v * scale + 16, y + 48, 30, GOLD if col == "gold" else CREAM, txt, 800))
    if c.get("note"): b += T(70, H-112, 18, GREY, c["note"])
    save(out, p["prefix"] + "-" + c["name"], W, H, b + foot(H, "Sources: " + p["sources"]))

if __name__ == "__main__":
    p = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    cover(p, out)
    if p.get("chart"): chart(p, out)
