# MenuTitle: Reset component transformations

__copyright__ = """
Copyright (c) 2013, David Brezina
All rights reserved.
"""

__doc__ = """
Check all components in all selected glyphs’ layers and remove any 
mirror/rotation/skew but retain the current mathematical position.
Highlights any affected glyphs red and prints their affected layers to the 
console.

NOTE: Does not retain visual position for affected components
"""
from GlyphsApp import Glyphs

noTransform = (1.0, 0.0, 0.0, 1.0)
for g in Glyphs.font.selection:
    glyph.beginUndo()
    for l in glyph.layers:
        for c in l.components:
            if c.transform[:4] != noTransform:
                g.color = 0
                print "Manually check components in %s, layer %s for correct alignment. Removed mirror/rotation/skew, but position might need fixing" % (glyph.name, layer.name)


# Old version

# Font = Glyphs.font
# Doc = Glyphs.currentDocument
# selectedGlyphs = [x.parent for x in Doc.selectedLayers()]

# for gl in selectedGlyphs:
#     changed = False
#     for l in gl.layers:
#         for c in l.components:
#             if c.name == "_part":
#                 transform = list(c.transform)
#                 if c.transform[0] == -1.0:
#                     transform[4] -= 60  # shift
#                     transform[0] = 1.0  # scale
#                     changed = True
#                 if c.transform[3] == -1.0:
#                     transform[5] -= 60  # shift
#                     transform[3] = 1.0  # scale
#                     changed = True
#                 #print(gl.name, c.name, c.transform)
#                 c.transform = tuple(transform)
#     if changed:
#         print("Fixed component transformations in", gl.name)
