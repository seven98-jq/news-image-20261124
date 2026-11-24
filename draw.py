#!/usr/bin/env python3
"""Draw a one-day newspaper front page: the world news of 24 Nov 2026.

Run: python3 draw.py  -> writes entry.png (1024x1024, under 1 MiB)
Only Pillow is needed. All text is drawn from the six stories below.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 233)      # warm newsprint
INK = (24, 24, 24)           # near-black
RED = (169, 31, 31)          # date line / headline kicker
GREY = (110, 105, 95)        # secondary labels
NAVY = (28, 58, 110)
PURPLE = (104, 52, 140)
GREEN = (38, 110, 58)
GOLD = (168, 118, 20)
TEAL = (16, 110, 110)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(d, lines, f, x, y, leading, fill=INK):
    for line in lines:
        d.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def hrule(d, y, x0=36, x1=988, width=2, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# --- frame: double rule border -------------------------------------------
d.rectangle([12, 12, W - 13, H - 13], outline=INK, width=3)
d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

# --- masthead -------------------------------------------------------------
mast = font(SERIF_B, 64)
title = "THE WORLD IN ONE DAY"
tw = d.textlength(title, font=mast)
d.text(((W - tw) / 2, 34), title, font=mast, fill=INK)

# thick rule + thin rule under the masthead
d.rectangle([36, 116, 988, 120], fill=INK)
hrule(d, 128)

# --- date band: the date must be loud -------------------------------------
date_f = font(SANS_B, 34)
d.text((36, 140), "TUESDAY \u00b7 24 NOVEMBER 2026", font=date_f, fill=RED)
side_f = font(SANS_B, 22)
side = "SIX STORIES"
sw = d.textlength(side, font=side_f)
d.text((988 - sw, 146), side, font=side_f, fill=GREY)
hrule(d, 182)

# --- lead story: COP31 ----------------------------------------------------
y = 198
d.text((36, y), "CLIMATE \u2014 COP31, ANTALYA", font=font(SANS_B, 24), fill=RED)
y += 40
head_f = font(SERIF_B, 52)
head_lines = wrap(d, "COP31 climate talks collapse with no deal", head_f, 660)
y = draw_lines(d, head_lines, head_f, 36, y, 62)
y += 12
sum_f = font(SANS, 23)
sum_lines = wrap(
    d,
    "More than 90 nations reject a final text that omits any move away "
    "from fossil fuels, after talks run nearly 50 hours into overtime.",
    sum_f, 660)
y = draw_lines(d, sum_lines, sum_f, 36, y, 30)

# globe with a crack in it, right of the lead story
cx, cy, r = 838, 300, 100
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=4)
d.line([(cx - r, cy), (cx + r, cy)], fill=NAVY, width=2)          # equator
d.line([(cx, cy - r), (cx, cy + r)], fill=NAVY, width=2)          # prime meridian
d.ellipse([cx - 52, cy - r, cx + 52, cy + r], outline=NAVY, width=2)
d.ellipse([cx - r, cy - 52, cx + r, cy + 52], outline=NAVY, width=2)
crack = [(cx, cy - r + 4), (cx + 14, cy - 60), (cx - 12, cy - 25),
         (cx + 12, cy + 10), (cx - 14, cy + 45), (cx + 6, cy + 80),
         (cx, cy + r - 4)]
d.line(crack, fill=RED, width=5, joint="curve")
cap_f = font(SANS_B, 24)
cap = "TALKS FAIL"
cw = d.textlength(cap, font=cap_f)
d.text((cx - cw / 2, 414), cap, font=cap_f, fill=RED)

hrule(d, y + 14)
grid_top = y + 30

# --- small geometric icons, each drawn centred on (cx, cy) ----------------
def icon_boat(cx, cy, c):
    d.polygon([(cx - 16, cy + 4), (cx + 16, cy + 4), (cx + 11, cy + 13),
               (cx - 11, cy + 13)], fill=c)
    d.line([(cx, cy - 15), (cx, cy + 4)], fill=c, width=3)
    d.polygon([(cx, cy - 15), (cx, cy + 2), (cx + 11, cy + 2)], fill=c)
    d.line([(cx - 16, cy + 17), (cx + 16, cy + 17)], fill=c, width=2)


def icon_chip(cx, cy, c):
    d.rectangle([cx - 12, cy - 12, cx + 12, cy + 12], outline=c, width=3)
    d.rectangle([cx - 5, cy - 5, cx + 5, cy + 5], fill=c)
    for k in (-7, 0, 7):
        d.line([(cx + k, cy - 17), (cx + k, cy - 12)], fill=c, width=2)
        d.line([(cx + k, cy + 12), (cx + k, cy + 17)], fill=c, width=2)
        d.line([(cx - 17, cy + k), (cx - 12, cy + k)], fill=c, width=2)
        d.line([(cx + 12, cy + k), (cx + 17, cy + k)], fill=c, width=2)


def icon_capitol(cx, cy, c):
    d.pieslice([cx - 14, cy - 14, cx + 14, cy + 14], 180, 360, fill=c)
    d.rectangle([cx - 16, cy + 2, cx + 16, cy + 14], fill=c)
    for kx in (-9, 0, 9):
        d.line([(cx + kx, cy + 4), (cx + kx, cy + 12)], fill=PAPER, width=2)


def icon_jet(cx, cy, c):
    d.polygon([(cx + 17, cy), (cx - 12, cy - 11), (cx - 6, cy),
               (cx - 12, cy + 11)], fill=c)
    d.polygon([(cx + 2, cy - 2), (cx - 9, cy - 15), (cx - 5, cy - 2)], fill=c)
    d.polygon([(cx + 2, cy + 2), (cx - 9, cy + 15), (cx - 5, cy + 2)], fill=c)


def icon_mine(cx, cy, c):
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line([(cx + 9 * math.cos(a), cy + 9 * math.sin(a)),
                (cx + 15 * math.cos(a), cy + 15 * math.sin(a))],
               fill=c, width=2)
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], outline=c, width=3)
    d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=c)


def story_cell(x, y, w, kicker, color, headline, summary, icon):
    kick_f = font(SANS_B, 20)
    d.text((x, y), kicker, font=kick_f, fill=color)
    icon(x + w - 18, y + 10, color)
    hy = y + 32
    h_f = font(SERIF_B, 25)
    hy = draw_lines(d, wrap(d, headline, h_f, w), h_f, x, hy, 32)
    s_f = font(SANS, 19)
    sy = draw_lines(d, wrap(d, summary, s_f, w), s_f, x, hy + 8, 24)
    return sy


COL_W = 464
stories = [
    (36, "WAR AT SEA", NAVY,
     "Ukraine says sea drones sank a Russian warship off Libya",
     "Kyiv says seven unmanned boats destroyed a corvette at Benghazi, "
     "taking the Black Sea fight into the Mediterranean.",
     icon_boat),
    (524, "TECHNOLOGY", PURPLE,
     "Nvidia brings back Jensen Huang as chief executive",
     "The board reinstates Huang after intervention by President Trump; "
     "Forbes puts his fortune at $143.8 billion, up almost $34 billion in a day.",
     icon_chip),
    (36, "UNITED STATES", GREEN,
     "Democrats win their biggest House majority in decades",
     "The victory hands the party power to block the president's agenda "
     "and investigate alleged corruption for his final two years.",
     icon_capitol),
    (524, "KOREA", GOLD,
     "Suspected North Korean aircraft breaches South's airspace",
     "Seoul orders residents of Ulleung island to take shelter after the "
     "intrusion near its eastern island.",
     icon_jet),
]

row_y = grid_top
bottoms = [story_cell(stories[i][0], row_y, COL_W, *stories[i][1:])
           for i in (0, 1)]
row_y = max(bottoms) + 12
hrule(d, row_y)
row_y += 14
bottoms = [story_cell(stories[i][0], row_y, COL_W, *stories[i][1:])
           for i in (2, 3)]
row_y = max(bottoms)
d.line([(512, grid_top), (512, row_y)], fill=GREY, width=1)
hrule(d, row_y + 10)

# --- bottom strip: Middle East --------------------------------------------
strip_y = row_y + 24
kick_f = font(SANS_B, 22)
d.text((36, strip_y), "MIDDLE EAST", font=kick_f, fill=TEAL)
kx = 36 + d.textlength("MIDDLE EAST", font=kick_f) + 14
icon_mine(966, strip_y + 13, TEAL)
h_f = font(SERIF_B, 26)
d.text((kx, strip_y), "Oil tankers hit by mines in the Strait of Hormuz",
       font=h_f, fill=INK)
s_f = font(SANS, 19)
draw_lines(d, wrap(d,
                   "Iran says three tankers were struck and caught fire; "
                   "Houthis say a Saudi strike killed 17 in Hodeida.",
                   s_f, 952),
           s_f, 36, strip_y + 34, 24)

if __name__ == "__main__":
    img.save("entry.png", optimize=True)
    print("saved entry.png")
