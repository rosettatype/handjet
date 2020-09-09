import drawBot as db

def draw_frame(txt="a", variations={}, shift=0,
               fontsize=6000, guidelines=False, caption="", offset=(-270, 800)):

    w, h = 540, 540
    POINT = (0, 0, 0)
    FILL = (255 / 256, 242 / 256, 0)

    db.newPage(w, h)
    db.fill(*FILL)
    db.rect(0, 0, w, h)
    path = db.BezierPath()
    txt = db.FormattedString(txt, font=fontname, fontSize=fontsize, fontVariations=variations, fill=0, stroke=None)
    path.text(txt, offset)
    path_ = path.copy()
    # remove overlaps when you drawing the base
    # but use the first contour when drawing nodes
    path_.removeOverlap()
    path_.optimizePath()
    with db.savedState():
        # draw letter
        db.fill(0, 0, 0, 0.1)
        db.stroke(1, 1, 1, 0.9)
        db.strokeWidth(3)
        db.lineDash(None)
        db.drawPath(path_)

        # draw points only from the first contour (they are layered)
        if path.contours:
            for s in path.contours[0]:
                for x, y in s:
                    if (x, y) in path.onCurvePoints:
                        db.fill(0, 0, 0, 0.1)
                        db.stroke(*POINT)
                        db.strokeWidth(2)
                        db.oval(x-4, y-4, 8, 8)

    # draw caption
    db.fill(*POINT)
    db.stroke(None)
    db.font("AdapterPEText-Rg")
    db.fontSize(20)
    if caption:
        db.text(caption, (w / 2, 40), align="center")


# ------------------------------------------------------------------------------------
# Handjet shapes interpolation

fontname = "Handjet-Regular"
shape_names = [
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
max_pos = max([p for _, p in shape_names])
step = 5
caption = ""

db.newDrawing()
for i, (name, pos) in enumerate(shape_names):
    if (i + 1) < len(shape_names):
        next_name, next_pos = shape_names[i + 1]
    else:
        next_name, next_pos = name, max_pos
    pos, next_pos = int(100 * pos), int(100 * next_pos)
    delay = (next_pos - pos) / 3
    for eshp in range(pos, next_pos, step):
        if eshp > (pos + delay):
            caption = next_name
        draw_frame(txt="﮳", variations={"wght": 400, "ESHP": eshp / 100, "EGRD": 1.01},
                   caption=caption)
db.saveImage("../../docs/animations/Handjet-shapes-animation.gif")
db.endDrawing()
