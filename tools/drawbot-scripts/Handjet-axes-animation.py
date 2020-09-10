"""
Handjet axes interpolation
"""

import drawBot as db

# Global settings

w, h = 800, 400
TEXTCOL = (0, 0, 0)
BACKCOL = (255 / 256, 242 / 256, 0)
NODECOL = (1, 1, 1)
defaults = {"wght": 400, "ESHP": 8, "EGRD": 1.01}
step = 20
caption = ""

# Draw a single frame

def draw(txt="a", variations={}, caption=""):
    db.newPage(w, h)
    db.fill(*BACKCOL)
    db.rect(0, 0, w, h)
    txt = db.FormattedString(txt, font="Handjet-Regular", fontSize=185, fontVariations=variations)
    db.fill(*TEXTCOL)
    db.stroke(None)
    path = db.BezierPath()
    path.text(txt, (w / 2, 150), align="center")
    db.drawPath(path)
    txt = db.FormattedString(caption, font="InputMono-Regular", fontSize=11, fill=TEXTCOL)
    db.text(txt, (w / 2, 40), align="center")

# Animate axes

db.newDrawing()
# weight axis
step = 20
variations = defaults.copy()
for wght in range(100, 900 + step, step):
    caption = "Weight (wght): %.2f" % (wght)
    variations["wght"] = wght
    draw(txt="Possibilities", variations=variations, caption=caption)
for wght in range(900, 400 - step, -step):
    caption = "Weight (wght): %.2f" % (wght)
    variations["wght"] = wght
    draw(txt="Possibilities", variations=variations, caption=caption)
# element grid axis
step = 10
variations = defaults.copy()
for egrd in range(100, 300 + step, step):
    caption = "Element Grid (EGRD): %.2f" % (egrd / 100)
    variations["EGRD"] = egrd / 100
    draw(txt="Possibilities", variations=variations, caption=caption)
for egrd in range(300, 100 - step, -step):
    caption = "Element Grid (EGRD): %.2f" % (egrd / 100)
    variations["EGRD"] = egrd / 100
    draw(txt="Possibilities", variations=variations, caption=caption)
# element shapes axis
step = 10
variations = defaults.copy()
for eshp in range(0, 1600 + step, step):
    caption = "Element Shape (ESHP): %.2f" % (eshp / 100)
    variations["ESHP"] = eshp / 100
    draw(txt="Possibilities", variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-axes-animation.gif")
db.saveImage("../../docs/animations/Handjet-axes-animation.mp4")
db.endDrawing()
