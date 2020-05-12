# MenuTitle: reset component transformations

"""
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

                if c.transform[3] == -1.0:
                    newTransform[5] = c.y - c.bounds.size.height

                if newTransform != list(c.transform):
                    c.transform = tuple(newTransform)
                    g.color = 10
                    print "Flipped turned component in place in %s, layer %s. Double-check positioning in gray glyphs" % (g.name, l.name)
                else:
                    g.color = 11
                    c.transform = tuple(newTransform)
                    print "Manually check components in %s, layer %s for correct alignment. Removed rotation/skew (%s), but position might need fixing in glyphs marked black" % (g.name, l.name, str(c.transform))
        g.endUndo()
