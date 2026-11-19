#!/usr/bin/env python3
"""Composite the final 1024x1024 news front page for 18 Nov 2026."""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap, os

ROOT = os.path.dirname(os.path.abspath(__file__))
HERO = "/home/hatch/workspace/makefun/news-art/media-generation-news-hero-summit-0-1c8d8244-1dfb-403a-8a07-87add5f0f092.webp"
OUT = os.path.join(ROOT, "entry.png")

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"

def F(path, size): return ImageFont.truetype(path, size)

W = H = 1024
PAPER = (244, 239, 230)
INK = (18, 18, 18)
DARK = (17, 20, 24)
WHITE = (255, 255, 255)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead ----
d.text((W//2, 8), "THE WORLD IN ONE DAY", font=F(SERIF_B, 62), fill=INK, anchor="ma")
# rule
d.rectangle([28, 78, W-28, 81], fill=INK)
d.rectangle([28, 84, W-28, 85], fill=INK)
# date band
d.rectangle([0, 90, W, 118], fill=INK)
d.text((W//2, 104), "WEDNESDAY  •  18 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE", font=F(SANS_B, 20), fill=WHITE, anchor="mm")

# ---- Hero ----
hero_top, hero_h = 118, 512
hero = Image.open(HERO).convert("RGB")
hero = ImageOps.fit(hero, (W, hero_h), method=Image.LANCZOS, centering=(0.5, 0.42))
img.paste(hero, (0, hero_top))
d = ImageDraw.Draw(img)

# ---- Headline band under hero ----
hb_top = hero_top + hero_h  # 630
hb_h = 96
d.rectangle([0, hb_top, W, hb_top+hb_h], fill=(142, 22, 22))
d.text((W//2, hb_top+10), "TRUMP, XI & PUTIN MEET IN SHENZHEN", font=F(SERIF_B, 40), fill=WHITE, anchor="ma")
d.text((W//2, hb_top+58), "FIRST TRILATERAL SUMMIT AT APEC", font=F(SANS_B, 26), fill=(255, 222, 160), anchor="ma")

# ---- Bottom grid: 2 rows x 4 cols ----
grid_top = hb_top + hb_h  # 726
grid_h = H - grid_top  # 298
d.rectangle([0, grid_top, W, H], fill=DARK)
cols, rows = 4, 2
cw, ch = W//cols, grid_h//rows

items = [
    ("HORMUZ ESCALATION", "US strikes Iran's Qeshm Island; tankers hit", (255, 92, 92)),
    ("UKRAINE HITS CRIMEA BRIDGE", "Zelensky confirms strike on key link", (110, 180, 255)),
    ("GAZA OPERATION", "Israel launches new operation in central Gaza", (255, 176, 92)),
    ("US LOSES MEASLES-FREE STATUS", "Cases & deaths mount nationwide", (150, 230, 150)),
    ("TECH OUTAGE WAVE", "Flights grounded, NSA hit in wave", (200, 160, 255)),
    ("NVIDIA BEATS, ANTHROPIC IPO $83", "Wall Street ends mixed", (255, 215, 110)),
    ("SIBERIA PLANE CRASH", "19 dead in Siberia crash", (140, 220, 240)),
    ("CYCLONE AKVAN", "Severe storm nears Odisha, India", (255, 140, 190)),
]

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

for i, (head, sub, accent) in enumerate(items):
    r, c = divmod(i, cols)
    x0, y0 = c*cw, grid_top + r*ch
    # accent bar
    d.rectangle([x0+10, y0+10, x0+cw-10, y0+16], fill=accent)
    # dividers
    if c: d.line([x0, y0+8, x0, y0+ch-8], fill=(60, 66, 74), width=1)
    if r: d.line([x0+8, y0, x0+cw-8, y0], fill=(60, 66, 74), width=1)
    hf = F(SANS_B, 20)
    hl = wrap(d, head, hf, cw-24)
    y = y0 + 24
    for ln in hl[:3]:
        d.text((x0+12, y), ln, font=hf, fill=WHITE)
        y += 24
    sf = F(SANS_R, 18)
    sl = wrap(d, sub, sf, cw-24)
    for ln in sl[:3]:
        d.text((x0+12, y), ln, font=sf, fill=(205, 210, 218))
        y += 22

img.save(OUT, format="PNG", optimize=True)
print(OUT, img.size, os.path.getsize(OUT))
# If over 1MiB, fall back to JPEG bytes under entry.png name
if os.path.getsize(OUT) > 1048576:
    img.save(OUT, format="JPEG", quality=88, optimize=True)
    print("converted to JPEG", os.path.getsize(OUT))
