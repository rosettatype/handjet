"""
Handjet EGRD axis interpolation
"""

import csv
import unicodedata
import drawBot as db

# Global settings

w, h = 400, 400
TEXTCOL = (0, 0, 0)
BACKCOL = (255 / 256, 242 / 256, 0)
NODECOL = (1, 1, 1)
defaults = {"wght": 400, "ESHP": 8, "EGRD": 1.01}

# Draw a single frame

def draw(gn="a", variations={}, caption=""):
    db.newPage(w, h)
    db.fill(*BACKCOL)
    db.rect(0, 0, w, h)
    fs = db.FormattedString()
    fs.font("Handjet-Regular")
    fs.fontSize(250)
    #fs.fontVariations(**variations)
    fs.appendGlyph(gn)
    db.fill(*TEXTCOL)
    db.stroke(None)
    path = db.BezierPath()
    path.text(fs, (w / 2, 130), align="center")
    db.drawPath(path)
    fs = db.FormattedString(caption, font="InputMono-Regular", fontSize=10, fill=TEXTCOL)
    db.text(fs, (w / 2, 40), align="center")

# Animate fly-through the whole glyph set

db.newDrawing()
db.font("Handjet-Regular")
variations = defaults.copy()
unicodes = []
with open("glyphOrder-unicodes.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for _, u, show in reader:
        if u:
            unicodes.append((chr(int(u, 16)), eval(show)))
        else:
            unicodes.append((None, eval(show)))
for (uchr, show), gn in list(zip(unicodes, db.listFontGlyphNames())):
    # show only non-empty glyphs with a width (avoiding accents and spaces)
    if show:
        # wght = random.randrange(100, 900)
        # ESHP = random.randrange(0, 1600) / 100
        # EGRD = random.randrange(1, 3)
        # variations["wght"] = wght
        # variations["ESHP"] = ESHP
        # variations["EGRD"] = EGRD
        # caption = "Weight (wght): %d\nElement Shape (ESHP): %.2f\nElement Shape (EGRD): %.2f" % (wght, ESHP, EGRD)
        if uchr:
            try:
                caption = unicodedata.name(uchr)
            except ValueError:
                caption = ""
        else:
            caption = ""
        draw(gn, variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-flythrough.gif")
db.endDrawing()
