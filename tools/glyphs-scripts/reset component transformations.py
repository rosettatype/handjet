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

NOTE: If a component is flipped the position is retained, however rotated or 
skewed components might need to be manually repositioned
"""

from GlyphsApp import Glyphs

noTransform = (1.0, 0.0, 0.0, 1.0)

for g in Glyphs.font.selection:
    g.beginUndo()
    for l in g.layers:
        for c in l.components:
            if c.transform[:4] != noTransform:
                newTransform = list(noTransform) + [c.x, c.y]

                if c.transform[0] == -1.0:
                    newTransform[4] = c.x - c.bounds.size.width

                if c.transform[4] == -1.0:
                    newTransform[5] = c.y - c.bounds.size.height

                if newTransform != list(c.transform):
                    c.transform = tuple(newTransform)
                    g.color = 1
                    print "Flipped turned component in place in %s, layer %s. Double-check positioning in orange glyphs" % (g.name, l.name)
                else:
                    g.color = 0
                    c.transform = tuple(newTransform)
                    print "Manually check components in %s, layer %s for correct alignment. Removed rotation/skew (%s), but position might need fixing" % (g.name, l.name, str(c.transform))
        g.endUndo()

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
