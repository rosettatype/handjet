"""
Handjet wght axis animation
"""

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

def draw(txt="a", variations={}, caption=""):
    db.newPage(w * scale, h * scale)
    db.scale(scale)
    db.fill(*BACKCOL)
    db.rect(0, 0, w, h)
    txt = db.FormattedString(txt, font=handjetfont, fontSize=500, fontVariations=variations)
    db.fill(*TEXTCOL)
    db.stroke(None)
    path = db.BezierPath()
    path.text(txt, (w / 2, 95), align="center")
    db.drawPath(path)
    txt = db.FormattedString(caption, font="AdapterMonoPE-Regular", fontSize=11, fill=TEXTCOL)
    db.text(txt, (w / 2, 40), align="center")

# Animate wght axis

db.newDrawing()
step = 20
variations = defaults.copy()
for wght in range(100, 900 + step, step):
    caption = "Weight (wght): %.2f" % (wght)
    variations["wght"] = wght
    draw(txt="e", variations=variations, caption=caption)
for wght in range(900, 100 - step, -step):
    caption = "Weight (wght): %.2f" % (wght)
    variations["wght"] = wght
    draw(txt="e", variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-wght-animation.gif")
db.endDrawing()
