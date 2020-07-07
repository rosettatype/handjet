#MenuTitle: compile pixel glyph

"""
Combine pixel.SHAP-XXXX, pixel.wght-XXX, and pixel.GRID-XXX glyphs to form
a pixel glyph with layers defined by these glyphs.
"""

import copy
from collections import OrderedDict

font = Glyphs.currentDocument.font
# always use the first master
master_id = font.masters[0].id

# get axes values used in pixel.SHAP-XXXX glyphs and transformations
# specified in pixel.wght-XXX and pixel.GRID-XXX glyphs
axes = OrderedDict()
wght_transforms = OrderedDict()
grid_transforms = OrderedDict()
for gl in font.glyphs:
    for an in ["SHAP", "wght", "GRID"]:
        if gl.name.startswith("pixel." + an):
            _, pos = gl.name.split("-")
            pos = int(pos)
            if an in axes:
                axes[an].append(pos)
            else:
                axes[an] = [pos]
            if an == "wght":
                # get the transformations from the wght-XXX glyphs
                # change in scale only
                c = font.glyphs[gl.name].layers[master_id].components[0]
                wght_transforms[pos] = c.transform
            elif an == "GRID":
                # get the transformations from the GRID-XXX glyphs
                # change in scale and position
                grid_transforms[pos] = []
                for c in font.glyphs[gl.name].layers[master_id].components:
                    grid_transforms[pos].append(c.transform)

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
print("Copying contours from pixel.SHAP-XXX glyphs "
      "to layers in the pixel glyph and applying transformations from "
      "pixel.wght-XXX and pixel.GRID-XXX glyphs.")
for shap in axes["SHAP"]:
    shap_name = "pixel.SHAP-%d" % shap
    for wght in axes["wght"]:
        wght_tr = wght_transforms[wght]
        for GRID in axes["GRID"]:
            # find an existing master layer with the same coordinates
            # otherwise, create a brace layer
            for m in font.masters:
                if list(m.axes) == [wght, shap, GRID]:
                    layer = pixel_glyph.layers[m.id]
                    break
            else:
                # the name has to be in this order
                layer = GSLayer()
                layer.name = "{%d,%d,%d}" % (wght, shap, GRID)
                pixel_glyph.layers.append(layer)
            # add transformed paths to this layer
            for grid_tr in grid_transforms[GRID]:
                # get the path from the shap-XXXX glyph, first master layer
                path = font.glyphs[shap_name].layers[master_id].paths[0].copy()
                # apply wght and GRID transforms in this order
                path.applyTransform(wght_tr)
                path.applyTransform(grid_tr)
                layer.paths.append(path)
