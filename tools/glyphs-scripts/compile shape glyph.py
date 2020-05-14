#MenuTitle: compile shape glyph

"""
Combine SHAP-XXXX, wght-XXX, and opsz-XXX glyphs to form
two new glyphs: /shape and /grid with these glyphs as brace layers/masters
"""

import copy
from collections import OrderedDict

font = Glyphs.currentDocument.font
# always use the first master
master_id = font.masters[0].id

# get axes values used in SHAP-XXXX, wght-XXX, and opsz-XXX glyphs
positions = OrderedDict()
for gl in font.glyphs:
    for an in ["SHAP", "wght", "opsz"]:
        if gl.name.startswith(an):
            _, pos = gl.name.split("-")
            pos = int(pos)
            if an in positions:
                positions[an].append(pos)
            else:
                positions[an] = [pos]

print("Cleaning up the shape and grid glyphs")
for gn in ["shape", "grid"]:
    if gn not in font.glyphs:
        font.glyphs.append(GSGlyph(gn))
    gl = font.glyphs[gn]
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
shape_glyph = font.glyphs["shape"]
grid_glyph = font.glyphs["grid"]

# create new layers in shape glyph
# based on SHAP-XXXX and wght-XXX glyphs
print("Copying contours from SHAP-XXX and wght-XXX glyphs "
      "to layers in the shape glyph")
for shap in positions["SHAP"]:
    shap_name = "SHAP-%d" % shap
    for wght in positions["wght"]:
        # get the transformation from the wght-XXX glyph
        wght_name = "wght-%d" % wght
        tr = font.glyphs[wght_name].layers[master_id].components[0].transform
        for opsz in positions["opsz"]:
            # get the contour from the shap-XXXX glyph
            contour_layer = font.glyphs[shap_name].layers[master_id].copy()
            # modify the transformation to better fit different grid layouts
            if opsz == 50:
                tr_ = (tr[0] / 2, 0, 0, tr[3] / 2, 0, 0)
            elif opsz == 100:
                tr_ = (tr[0] / 3, 0, 0, tr[3] / 3, 0, 0)
            else:
                tr_ = tr
            contour_layer.paths[0].applyTransform(tr_)
            # find a master layer with the same coordinates if it exists
            # otherwise, create a brace layer
            master_layer = None
            for m in font.masters:
                if list(m.axes) == [wght, shap, opsz]:
                    master_layer = shape_glyph.layers[m.id]
            if master_layer:
                # master layer
                master_layer.paths.append(contour_layer.paths[0])
            else:
                # brace layer
                # the name has to be in this order
                contour_layer.name = "{%d,%d,%d}" % (wght, shap, opsz)
                shape_glyph.layers.append(contour_layer)

print("Copying componets from opsz-XXX glyphs to corresponding layers "
      "in the grid glyph")
for ll in grid_glyph.layers:
    if ll.name[0] not in ["[", "{"]:
        # get opsz value from the associated master axes coordinates
        mposition = font.masters[ll.layerId].axes
        opsz = mposition[2]
        # get corresponding master glyph
        opsz_name = "opsz-%.f" % float(opsz)
        opsz_glyph = font.glyphs[opsz_name]
        # copy components from relevant opsz-XXX glyph
        # needs to be done one by one to set the layer-links anew
        ll.components = []
        for c in opsz_glyph.layers[master_id].components:
            c_ = GSComponent(c.name)
            c_.automaticAlignment = False
            c_.position = c.position
            ll.components.append(c_)
