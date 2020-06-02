# MenuTitle: compile pixel glyph

"""
Combine pixel.SHAP-XXXX, pixel.wght-XXX, and pixel.opsz-XXX glyphs to form
two a/pixel glyph with layers defined by these glyphs.
"""

import copy
from collections import OrderedDict

font = Glyphs.currentDocument.font
# always use the first master
master_id = font.masters[0].id

# get axes values used in pixel.SHAP-XXXX glyphs and transformations
# specified in pixel.wght-XXX and pixel.opsz-XXX glyphs
axes = OrderedDict()
wght_transforms = OrderedDict()
opsz_transforms = OrderedDict()
for gl in font.glyphs:
    for an in ["SHAP", "wght", "opsz"]:
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
            elif an == "opsz":
                # get the transformations from the opsz-XXX glyphs
                # change in scale and position
                opsz_transforms[pos] = []
                for c in font.glyphs[gl.name].layers[master_id].components:
                    opsz_transforms[pos].append(c.transform)


print("Cleaning up the pixel glyph")
if "pixel" not in font.glyphs:
    font.glyphs.append(GSGlyph("pixel"))

gl = font.glyphs["pixel"]
for i in reversed(range(len(gl.layers))):
    del gl.layers[i]
pixel_glyph = font.glyphs["pixel"]


# create new layers in the /pixel glyph
print("Copying contours from pixel.SHAP-XXX glyphs "
      "to layers in the pixel glyph and applying transformations from "
      "pixel.wght-XXX and pixel.opsz-XXX glyphs.")
for shap in axes["SHAP"]:
    shap_name = "pixel.SHAP-%d" % shap
    for wght in axes["wght"]:
        wght_tr = wght_transforms[wght]
        for opsz in axes["opsz"]:
            # find an existing master layer with the same coordinates
            # otherwise, create a brace layer
            if list(font.masters[0].axes) == [wght, shap, opsz]:
                layer = pixel_glyph.layers[font.masters[0].id]

            else:
                # create a layer with the axis values as name in this order
                layer = GSLayer()
                layer.name = "{%d,%d,%d}" % (wght, shap, opsz)
                pixel_glyph.layers.append(layer)
                print("Created new pixel layer %s" % layer.name)

            # add transformed paths to this layer
            for opsz_tr in opsz_transforms[opsz]:
                # get the path from the shap-XXXX glyph, first master layer
                path = font.glyphs[shap_name].layers[master_id].paths[0].copy()
                # apply wght and opsz transforms in this order
                path.applyTransform(wght_tr)
                path.applyTransform(opsz_tr)
                layer.paths.append(path)
