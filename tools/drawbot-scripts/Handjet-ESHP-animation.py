"""
Handjet ESHP axis interpolation
"""

import drawBot as db

# Global settings

w, h = 400, 400
TEXTCOL = (0, 0, 0)
BACKCOL = (255 / 256, 242 / 256, 0)
NODECOL = (1, 1, 1)
defaults = {"wght": 400, "ESHP": 8, "EGRD": 1.01}
step = 5
caption = ""

# Draw a single frame

def draw(txt="a", variations={}, caption=""):
    db.newPage(w, h)
    db.fill(*BACKCOL)
    db.stroke(None)
    db.rect(0, 0, w, h)
    txt = db.FormattedString(txt, font="Handjet-Regular", fontSize=4800, fontVariations=variations)
    path = db.BezierPath()
    # path.text(txt, (w / 2, 100))
    path.text(txt, (w / 2, 1.61 * h), align="center")
    path_optim = path.copy()
    # remove overlaps when drawing the fill
    # but use the original contour when drawing the nodes
    path_optim.removeOverlap()
    path_optim.optimizePath()
    with db.savedState():
        # draw the fill
        db.fill(*TEXTCOL)
        db.drawPath(path_optim)
        # draw nodes
        if path.contours:
            # drawing just the first contour is enough
            for s in path.contours[0]:
                for x, y in s:
                    if (x, y) in path.onCurvePoints:
                        db.fill(*NODECOL)
                        db.stroke(*TEXTCOL)
                        db.strokeWidth(1)
                        db.oval(x-4, y-4, 8, 8)
    # draw caption
    txt = db.FormattedString(caption, font="InputMono-Regular", fontSize=11, fill=TEXTCOL)
    if caption:
        db.text(txt, (w / 2, 40), align="center")

# Animate ESHP axis

eshp_steps = [
    ("Blank", 0),
    ("Triangle", 1.00),
    ("Square", 2.00),
    ("Lozenge", 2.25),
    ("Square again", 2.50),
    ("Block", 3.19),
    ("Rectangle", 3.36),
    ("Bar (Vertical)", 4.00),
    ("Bar (Diagonal Up)", 4.25),
    ("Bar (Horizontal)", 4.50),
    ("Bar (Diagonal Down)", 4.75),
    ("Bar (Vertical again)", 5.00),
    ("Square again", 6.50),
    ("Rounded Square", 6.90),
    ("Squircle", 7.63),
    ("Circle", 8.00),
    ("Egg", 8.69),
    ("Oval", 8.86),
    ("Thin Oval", 9.50),
    ("Circle again", 11.00),
    ("Clover", 12.00),
    ("Flower", 13.00),
    ("Star", 14.00),
    ("Star (Diagonal)", 14.25),
    ("Star again", 14.50),
    ("Big Star", 14.75),
    ("Spindle", 15.00),
    ("Pin", 15.37),
    ("Heart", 16.00),
    ]

db.newDrawing()
variations = defaults.copy()
max_pos = max([p for _, p in eshp_steps])
caption = eshp_steps[0][0]
for i, (name, pos) in enumerate(eshp_steps):
    if (i + 1) < len(eshp_steps):
        next_name, next_pos = eshp_steps[i + 1]
    else:
        next_name, next_pos = name, max_pos
    pos, next_pos = int(100 * pos), int(100 * next_pos)
    delay = (next_pos - pos) / 3
    for eshp in range(pos, next_pos, step):
        if eshp > (pos + delay):
            caption = next_name
        variations["ESHP"] = eshp / 100
        draw(txt="﮳", variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-ESHP-animation.gif")
db.saveImage("../../docs/animations/Handjet-ESHP-animation.mp4")
db.endDrawing()
