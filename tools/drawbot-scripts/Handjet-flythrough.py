"""
Handjet flythrough glyph set animation
"""

import csv
import unicodedata
import drawBot as db

# Global settings

w, h = 400, 400
scale = 1
TEXTCOL = (0, 0, 0)
BACKCOL = (230 / 255, 250 / 255, 40 / 255)
NODECOL = (1, 1, 1)
defaults = {"wght": 400, "ELSH": 8, "ELGR": 1.01}
handjetfont = "Handjet-Regular"

# Draw a single frame

def draw(gn="a", variations={}, caption=""):
    db.newPage(w * scale, h * scale)
    db.scale(scale)
    db.fill(*BACKCOL)
    db.rect(0, 0, w, h)
    fs = db.FormattedString()
    fs.font(handjetfont)
    fs.fontSize(200)
    fs.appendGlyph(gn)
    db.fill(*TEXTCOL)
    db.stroke(None)
    path = db.BezierPath()
    path.text(fs, (w / 2, 145), align="center")
    db.drawPath(path)
    fs = db.FormattedString(caption, font="AdapterMonoPE-Regular", fontSize=10, fill=TEXTCOL)
    db.text(fs, (w / 2, 40), align="center")

# Animate fly-through the whole glyph set

db.newDrawing()
db.font(handjetfont)
variations = defaults.copy()
unicodes = []
with open("glyphnames-unicodes-show.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    # line: glyph name, unicode, whether it should be shown
    for _, u, show in reader:
        if u:
            unicodes.append((u, eval(show)))
        else:
            unicodes.append((None, eval(show)))
for (u, show), gn in list(zip(unicodes, db.listFontGlyphNames())):
    # show only non-empty glyphs with a width (avoiding accents and spaces)
    if show:
        if u:
            try:
                caption = unicodedata.name(chr(int(u, 16))) + "\n" + u
            except ValueError:
                caption = ""
        else:
            caption = ""
        draw(gn, variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-flythrough.gif")
db.endDrawing()
