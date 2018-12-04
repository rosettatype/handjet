import drawBot as db

# SETTINGS
# colors
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)
RED = (0.7, 0, 0)
FACEBLUE = (34/255, 64/255, 127/255) # (59, 89, 152)
HANDJETCOLOR = (230/255, 250/255,40/255)  # (50/255, 156/255, 184/255)
# outline
letterFillColor = BLACK
letterStrokeColor = WHITE
letterStrokeWidth = 0.5
# nodes
onCurveNodeSize = 3
offCurveNodeSize = 2
nodeStrokeWidth = 2
nodeFillColor = WHITE
nodeStrokeColor = WHITE
# handles
handleStrokeWidth = 1
handleStrokeColor = WHITE


def draw_letter(sampletext="", glyphname="", fontfile="",
                fontvariations={}, fontsize=1000, features={},
                hatch=None, show_fill=False, show_outline=True,
                show_handles=True, show_coordinates=False,
                dashed_outline=False, dashed_handles=False, alpha=1.0):
    bottom_margin = 0
    with db.savedState():
        if dashed_handles:
            handleStrokeWidth = 2
        else:
            handleStrokeWidth = 1
        # prepare the letter path
        path = db.BezierPath()
        if fontfile not in db.installedFonts():
            print(fontfile, "is not installed")
        features_off = {f: False for f in features}
        fs = db.FormattedString("", font=fontfile, fontSize=fontsize,
                                openTypeFeatures=features,
                                fontVariations=fontvariations)
        if sampletext:
            fs.append(sampletext, fontVariations=fontvariations)
        elif glyphname:
            fs.appendGlyph(glyphname)
        path.text(fs)
        db.openTypeFeatures(**features_off)
        path.closePath()
        path.removeOverlap()
        x1, y1, x2, y2 = path.bounds()
        path_w = x2 - x1
        path_h = y2 - y1
        db.translate((poster_w - path_w)/2 - x1,
                     (poster_h - path_h)/2 - y1 + bottom_margin)
        # Actually draw the character
        if hatch is not None:
            with db.savedState():
                db.clipPath(path)
                db.fill(None)
                db.stroke(*letterStrokeColor)
                db.strokeWidth(letterStrokeWidth)
                db.rotate(hatch, center=(path_w/2, path_h/2))
                miny = -2*poster_h
                maxy = 2*poster_h
                for hx in range(miny, maxy, 15):
                    db.line((hx + miny, miny), (hx + maxy, maxy))
        if show_fill:
            letterFillColor_ = list(letterFillColor) + [alpha]
            db.fill(*letterFillColor_)
        if show_outline:
            db.stroke(*letterStrokeColor)
            if dashed_outline:
                db.lineDash(4, 4)
                db.strokeWidth(2*letterStrokeWidth)
        if show_fill or show_outline:
            db.drawPath(path)
            db.lineDash(None)

        # Draw handles etc.
        origin = path.contours[0][0][0]
        for c in path.contours:
            for s in c:
                for x, y in s:
                    if show_coordinates:
                        db.fill(*nodeStrokeColor)
                        db.stroke(None)
                        db.font("InputMono-Regular")
                        db.fontSize(14)
                        coords = "%d,%d" % (x, y)
                        wb, hb = db.textSize(coords)
                        db.rect(x-wb/2-4, y+8, wb+8, hb-2)
                        db.openTypeFeatures(tnum=True)
                        db.fill(*letterFillColor)
                        db.textBox(coords, (x-wb/2, y+6, wb, hb),
                                   align="center")
                        db.openTypeFeatures(tnum=False)
                if len(s) > 1 and show_handles:
                    db.fill(None)
                    db.stroke(*handleStrokeColor)
                    db.strokeWidth(handleStrokeWidth)
                    if dashed_handles:
                        db.lineDash(handleStrokeWidth, 2*handleStrokeWidth)
                    db.line(origin, s[0])
                    db.line(s[1], s[2])
                    db.lineDash(None)
                origin = s[-1]
        if show_handles:
            for x, y in path.onCurvePoints:
                db.fill(*nodeFillColor)
                db.stroke(*nodeStrokeColor)
                db.strokeWidth(nodeStrokeWidth)
                db.oval(x-onCurveNodeSize/2, y-onCurveNodeSize/2,
                        onCurveNodeSize, onCurveNodeSize)
            for x, y in path.offCurvePoints:
                db.fill(*nodeFillColor)
                db.stroke(*nodeStrokeColor)
                db.strokeWidth(nodeStrokeWidth)
                db.oval(x-offCurveNodeSize/2, y-offCurveNodeSize/2, offCurveNodeSize, offCurveNodeSize)

poster_w, poster_h = 540,540
imageResolution = 150
repete = 5
wght_min, wght_max, step = 11, 120, 10
wdth = 1000
opsz = 100
txt = "Love it!"
size = 150

db.newDrawing()
letterFillColor = BLACK
for wght in range(wght_min, wght_max, step):
    db.newPage(poster_w, poster_h)
    db.fill(*HANDJETCOLOR)
    db.rect(0, 0, poster_w, poster_h)
    draw_letter(txt, fontfile="Handjet-Regular_", fontsize=size, fontvariations={"wght": wght, "wdth": wdth, "opsz": opsz}, show_handles=False, show_fill=True, show_outline=False)
for wght in range(wght_max, wght_min, -step):
    db.newPage(poster_w, poster_h)
    db.fill(*HANDJETCOLOR)
    db.rect(0, 0, poster_w, poster_h)
    draw_letter(txt, fontfile="Handjet-Regular_", fontsize=size, fontvariations={"wght": wght, "wdth": wdth, "opsz": opsz}, show_handles=False, show_fill=True, show_outline=False)

saveImage("handjet_loveit.mp4")

db.font("Handjet-Regular")
for axis, data in db.listFontVariations().items():
    print((axis, data))
