# MenuTitle: Replicate selected layer to others
__copyright__ = """
Copyright (c) 2016, David Brezina
All rights reserved.
"""

__doc__ = """
Goes through selected glyphs and copies components to other masters if they are missing.
"""
from GlyphsApp import Glyphs, GSComponent, GSAnchor
from Foundation import NSPoint

for thisLayer in Glyphs.font.selectedLayers:
    thisGlyph = thisLayer.parent
    thisGlyph.beginUndo()

    for layer in thisGlyph.layers:
        if layer != thisLayer:

            # Copy components from selected layer
            layer.components = []
            for c in thisLayer.components:
                comp = GSComponent(c.componentName, NSPoint(c.x, c.y))
                comp.automaticAlignment = False
                layer.components.append(comp)

            # Copy anchors from selected layer
            layer.anchors = []
            for a in thisLayer.anchors:
                anch = GSAnchor(a.name, NSPoint(a.x, a.y))
                layer.anchors.append(anch)

            # Sync metrics with selected layer
            layer.LSB = thisLayer.LSB
            layer.width = thisLayer.width

    thisGlyph.endUndo()
