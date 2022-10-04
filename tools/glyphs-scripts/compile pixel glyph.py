#MenuTitle: compile pixel glyph

"""
Combine pixel.ELSH-XXXX, pixel.wght-XXX, and pixel.ELGR-XXX glyphs to form
a pixel glyph with layers defined by these glyphs.
"""

import copy
from collections import OrderedDict

font = Glyphs.currentDocument.font
# always use the first master
master_id = font.masters[0].id

# get axes values used in pixel.ELSH-XXXX glyphs and transformations
# specified in pixel.wght-XXX and pixel.ELGR-XXX glyphs
axes = OrderedDict()
wght_transforms = OrderedDict()
ELGR_transforms = OrderedDict()
for gl in font.glyphs:
    for an in ["ELSH", "wght", "ELGR"]:
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
            elif an == "ELGR":
                # get the transformations from the ELGR-XXX glyphs
                # change in scale and position
                ELGR_transforms[pos] = []
                for c in font.glyphs[gl.name].layers[master_id].components:
                    ELGR_transforms[pos].append(c.transform)

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
print("Copying contours from pixel.ELSH-XXX glyphs "
      "to layers in the pixel glyph and applying transformations from "
      "pixel.wght-XXX and pixel.ELGR-XXX glyphs.")
for ELSH in axes["ELSH"]:
    ELSH_name = "pixel.ELSH-%s" % ELSH
    for wght in axes["wght"]:
        wght_tr = wght_transforms[wght]
        for ELGR in axes["ELGR"]:
            # find an existing master layer with the same coordinates
            # otherwise, create a brace layer
            for m in font.masters:
                if list(m.axes) == [wght, ELSH, ELGR]:
                    layer = pixel_glyph.layers[m.id]
                    break
            else:
                # the name has to be in this order
                layer = GSLayer()
                layer.name = "{%s,%s,%s}" % (wght, ELSH, ELGR)
                pixel_glyph.layers.append(layer)
            # add transformed paths to this layer
            for ELGR_tr in ELGR_transforms[ELGR]:
                # get the path from the ELSH-XXXX glyph, first master layer
                path = font.glyphs[ELSH_name].layers[master_id].paths[0].copy()
                # apply wght and ELGR transforms in this order
                path.applyTransform(wght_tr)
                path.applyTransform(ELGR_tr)
                layer.paths.append(path)
