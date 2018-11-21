#MenuTitle: fix component transformations

__copyright__ = """
Copyright (c) 2013, David Brezina
All rights reserved.
"""

__doc__ = """

"""

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedGlyphs = [x.parent for x in Doc.selectedLayers()]

for gl in selectedGlyphs:
    changed = False
    for l in gl.layers:
        for c in l.components:
            if c.name == "_part":
                transform = list(c.transform)
                if c.transform[0] == -1.0:
                    transform[4] -= 60  # shift
                    transform[0] = 1.0  # scale
                    changed = True
                if c.transform[3] == -1.0:
                    transform[5] -= 60  # shift
                    transform[3] = 1.0  # scale
                    changed = True
                #print(gl.name, c.name, c.transform)
                c.transform = tuple(transform)
    if changed:
        print("Fixed component transformations in", gl.name)
