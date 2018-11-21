#MenuTitle: combine glyph alternates as masters
# encoding: utf-8

master_id = font.selectedFontMaster.id

font.disableUpdateInterface()

for target_name in ["_shape", "_grid"]:
    target_glyph = font[target_name]
    target_glyph.beginUndo()
    for gl in font.glyphs:
        if gl.name.startswith(target_name + "."):
            i = int(gl.name.replace(target_name + ".", ""))
            original = gl.layers[master_id]
            lay_id = font.masters[i].id
            newlay = original.copy()
            newlay.name = gl.layers[lay_id].name
            newlay.layerId = lay_id
            target_glyph.layers[lay_id] = newlay
    target_glyph.endUndo()
