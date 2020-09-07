#MenuTitle: compile pixel glyph

"""
Combine pixel.ESHP-XXXX, pixel.wght-XXX, and pixel.EGRD-XXX glyphs to form
a pixel glyph with layers defined by these glyphs.
"""

import copy
from collections import OrderedDict

font = Glyphs.currentDocument.font
# always use the first master
master_id = font.masters[0].id

# get axes values used in pixel.ESHP-XXXX glyphs and transformations
# specified in pixel.wght-XXX and pixel.EGRD-XXX glyphs
axes = OrderedDict()
wght_transforms = OrderedDict()
EGRD_transforms = OrderedDict()
for gl in font.glyphs:
    for an in ["ESHP", "wght", "EGRD"]:
        if gl.name.startswith("pixel." + an):
            _, pos = gl.name.split("-")
            pos = int(pos.replace("_", "."))
            if an in axes:
                axes[an].append(pos)
            else:
                axes[an] = [pos]
            if an == "wght":
                # get the transformations from the wght-XXX glyphs
                # change in scale only
                c = font.glyphs[gl.name].layers[master_id].components[0]
                wght_transforms[pos] = c.transform
            elif an == "EGRD":
                # get the transformations from the EGRD-XXX glyphs
                # change in scale and position
                EGRD_transforms[pos] = []
                for c in font.glyphs[gl.name].layers[master_id].components:
                    EGRD_transforms[pos].append(c.transform)

print("Cleaning up the pixel glyph")
if "pixel" not in font.glyphs:
    font.glyphs.append(GSGlyph("pixel"))
gl = font.glyphs["pixel"]
for i in range(len(gl.layers))[::-1]:
    ll = gl.layers[i]
    if ll.name[0] in ["[", "{"]:
        # delete brace and bracket layers
        del gl.layers[i]
    else:
        # cleanup master layers
        ll.paths = []
        ll.components = []
        ll.anchors = []
        ll.width = 0
pixel_glyph = font.glyphs["pixel"]


# create new layers in the /pixel glyph
print("Copying contours from pixel.ESHP-XXX glyphs "
      "to layers in the pixel glyph and applying transformations from "
      "pixel.wght-XXX and pixel.EGRD-XXX glyphs.")
for ESHP in axes["ESHP"]:
    ESHP_name = "pixel.ESHP-%s" % ESHP
    for wght in axes["wght"]:
        wght_tr = wght_transforms[wght]
        for EGRD in axes["EGRD"]:
            # find an existing master layer with the same coordinates
            # otherwise, create a brace layer
            for m in font.masters:
                if list(m.axes) == [wght, ESHP, EGRD]:
                    layer = pixel_glyph.layers[m.id]
                    break
            else:
                # the name has to be in this order
                layer = GSLayer()
                layer.name = "{%s,%s,%s}" % (wght, ESHP, EGRD)
                pixel_glyph.layers.append(layer)
            # add transformed paths to this layer
            for EGRD_tr in EGRD_transforms[EGRD]:
                # get the path from the ESHP-XXXX glyph, first master layer
                path = font.glyphs[ESHP_name].layers[master_id].paths[0].copy()
                # apply wght and EGRD transforms in this order
                path.applyTransform(wght_tr)
                path.applyTransform(EGRD_tr)
                layer.paths.append(path)
