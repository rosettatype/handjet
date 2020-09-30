"""
Handjet EGRD axis animation
"""

import drawBot as db

# Global settings

w, h = 400, 400
scale = 1
TEXTCOL = (0, 0, 0)
BACKCOL = (230 / 255, 250 / 255, 40 / 255)
NODECOL = (1, 1, 1)
defaults = {"wght": 400, "ESHP": 8, "EGRD": 1.01}

# Draw a single frame

def draw(txt="a", variations={}, caption=""):
    db.newPage(w * scale, h * scale)
    db.scale(scale)
    db.fill(*BACKCOL)
    db.rect(0, 0, w, h)
    txt = db.FormattedString(txt, font="Handjet-Regular", fontSize=500, fontVariations=variations)
    db.fill(*TEXTCOL)
    db.stroke(None)
    path = db.BezierPath()
    path.text(txt, (w / 2, 95), align="center")
    db.drawPath(path)
    txt = db.FormattedString(caption, font="InputMono-Regular", fontSize=11, fill=TEXTCOL)
    db.text(txt, (w / 2, 40), align="center")

# Animate EGRD axis

db.newDrawing()
variations = defaults.copy()
step = 5
for egrd in range(100, 300 + step, step):
    caption = "Element Grid (EGRD): %.2f" % (egrd / 100)
    variations["EGRD"] = egrd / 100
    draw(txt="n", variations=variations, caption=caption)
for egrd in range(300, 100 - step, -step):
    caption = "Element Grid (EGRD): %.2f" % (egrd / 100)
    variations["EGRD"] = egrd / 100
    draw(txt="n", variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-EGRD-animation.gif")
db.endDrawing()
