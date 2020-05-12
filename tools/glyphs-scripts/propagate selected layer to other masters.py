#MenuTitle: propagate selected layer to other masters

import GlyphsApp

selected = [x.parent for x in Glyphs.font.selectedLayers]
font = Glyphs.font
master_id = font.selectedFontMaster.id

font.disableUpdateInterface()

# glyphs
for gl in selected:
    if not gl.name in ["shape", "grid"]:
        original = gl.layers[master_id]
        gl.beginUndo()
        for i in range(len(font.masters)):
            lay_id = font.masters[i].id
            if lay_id != master_id:
                newlay = original.copy()
                newlay.name = gl.layers[lay_id].name
                newlay.layerId = lay_id
                gl.layers[lay_id] = newlay
        gl.endUndo()

# kerning
for i in range(len(font.masters)):
    lay_id = font.masters[i].id
    if lay_id != master_id:
        font.kerning[lay_id] = font.kerning[master_id]

font.enableUpdateInterface()
