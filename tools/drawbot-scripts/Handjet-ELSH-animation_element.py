"""
Handjet ELSH interpolation (element shape)
"""

import drawBot as db

# Global settings

w, h = 400, 400
scale = 1
TEXTCOL = (0, 0, 0)
BACKCOL = (230 / 255, 250 / 255, 40 / 255)
NODECOL = (1, 1, 1)
defaults = {"wght": 400, "ELSH": 8, "ELGR": 1.0}
handjetfont = "Handjet-Regular"

# Draw a single frame

def draw(txt="a", variations={}, caption=""):
    db.newPage(w * scale, h * scale)
    db.scale(scale)
    db.fill(*BACKCOL)
    db.stroke(None)
    db.rect(0, 0, w, h)
    fs = db.FormattedString(txt, font=handjetfont, fontSize=4600, fontVariations=variations)
    path = db.BezierPath()
    path.text(fs, (w / 2, 1.58 * h), align="center")
    path_optim = path.copy()
    # remove overlaps when drawing the fill
    # but use the original contour when drawing the nodes
    path_optim.removeOverlap()
    path_optim.optimizePath()
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
    fs = db.FormattedString(caption, font="AdapterMonoPE-Regular", fontSize=10, fill=TEXTCOL)
    if caption:
        db.text(fs, (w / 2, 40), align="center")

# Animate ELSH axis

elsh_steps = [
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
    ("Thinner Oval", 9.50),
    ("Circle again", 11.00),
    ("Clover", 12.00),
    ("Flower", 13.00),
    ("Star", 14.00),
    ("Diagonal Star", 14.25),
    ("Star again", 14.50),
    ("Big Star", 14.75),
    ("Spindle", 15.00),
    ("Pin", 15.37),
    ("Heart", 16.00),
    ]

db.newDrawing()
variations = defaults.copy()
step = 5
max_pos = max([p for _, p in elsh_steps])
current_name = elsh_steps[0][0]
for i, (_, pos) in enumerate(elsh_steps):
    if (i + 1) < len(elsh_steps):
        next_name, next_pos = elsh_steps[i + 1]
    else:
        next_pos = max_pos
    pos, next_pos = int(100 * pos), int(100 * next_pos)
    delay = (next_pos - pos) / 3
    for elsh in range(pos, next_pos, step):
        if elsh > (pos + delay):
            current_name = next_name
        variations["ELSH"] = elsh / 100
        caption = "Element Shape (ELSH): %.2f\n“%s”" % (elsh / 100, current_name)
        draw(txt="﮳", variations=variations, caption=caption)
db.saveImage("../../docs/animations/Handjet-ELSH-animation_element.gif")
db.endDrawing()
