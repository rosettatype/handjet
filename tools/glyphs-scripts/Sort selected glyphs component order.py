# MenuTitle: Sort selected glyphs component order

__copyright__ = """
Copyright (c) 2019, Rosetta Type
All rights reserved.
"""

__author__ = """
Johannes Neumeier
"""

__doc__ = """
Sorts all selected glyphs' layers' components order from top to bottom, left 
to right
"""
from GlyphsApp import Glyphs
from operator import attrgetter

for layer in Glyphs.font.selectedLayers:
    glyph = layer.parent
    glyph.beginUndo()
    # Simply rewrite the layer components after sorting them by
    # attributes, y first, x second
    layer.components = sorted(layer.components, key=attrgetter("y", "x"))
    glyph.endUndo()
