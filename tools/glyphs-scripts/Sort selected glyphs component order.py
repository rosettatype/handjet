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

_parts = ["_shape", "_grid"]
for layer in Glyphs.font.selectedLayers:
    glyph = layer.parent
    glyph.beginUndo()

    design_components = [c for c in layer.components if c.name not in _parts]
    dot_components = [c for c in layer.components if c.name in _parts]

    # Simply rewrite the layer components after sorting them by
    # attributes, y first, x second
    sorted_dot_components = sorted(dot_components, key=attrgetter("y", "x"))
    layer.components = design_components + sorted_dot_components
    glyph.endUndo()
