#MenuTitle: set up masters

"""
Set up masters (the script does not create them):
name, axes, custom parameters
"""

from collections import OrderedDict

font = Glyphs.currentDocument.font
# always use the first master
master_id = font.masters[0].id

masters = OrderedDict([
    ("Small Empty", [100, 100, 10]),
    ("Normal Empty", [400, 100, 10]),
    ("Big Empty", [900, 100, 10]),
    ("Small Circle", [100, 1000, 10]),
    ("Normal Circle", [400, 1000, 10]),
    ("Big Circle", [900, 1000, 10]),
    ("Small Heart", [100, 1900, 10]),
    ("Normal Heart", [400, 1900, 10]),
    ("Big Heart", [900, 1900, 10]),
    ("Double Small Empty", [100, 100, 50]),
    ("Double Normal Empty", [400, 100, 50]),
    ("Double Big Empty", [900, 100, 50]),
    ("Double Small Circle", [100, 1000, 50]),
    ("Double Normal Circle", [400, 1000, 50]),
    ("Double Big Circle", [900, 1000, 50]),
    ("Double Small Heart", [100, 1900, 50]),
    ("Double Normal Heart", [400, 1900, 50]),
    ("Double Big Heart", [900, 1900, 50]),
    ("Triple Small Empty", [100, 100, 100]),
    ("Triple Normal Empty", [400, 100, 100]),
    ("Triple Big Empty", [900, 100, 100]),
    ("Triple Small Circle", [100, 1000, 100]),
    ("Triple Normal Circle", [400, 1000, 100]),
    ("Triple Big Circle", [900, 1000, 100]),
    ("Triple Small Heart", [100, 1900, 100]),
    ("Triple Normal Heart", [400, 1900, 100]),
    ("Triple Big Heart", [900, 1900, 100]),
])

metrics = {}
metrics["ascender"] = 2880
metrics["capHeight"] = 2640
metrics["xHeight"] = 1920
metrics["descender"] = -720
metrics["italicAngle"] = 0

customParameters = {
    "underlinePosition": -480,
    "underlineThickness": 40,
    "typoAscender": 3120,
    "typoDescender": -960,
    "typoLineGap": 0,
    "hheaAscender": 3120,
    "hheaDescender": -960,
    "hheaLineGap": 0,
    "winAscent": 3120,
    "winDescent": 960,
}

font.disableUpdateInterface()

# set up custom parameters and axes values
for (name, axes), m in zip(masters.items(), font.masters):
    m.name = name
    m.axes = axes
    for k, v in customParameters.items():
        m.customParameters[k] = v
        if "Small" in m.name:
            m.customParameters["underlineThickness"] = 20
        elif "Big" in m.name:
            m.customParameters["underlineThickness"] = 120
        # no hinting stems
        m.verticalStems = []
        m.horizontalStems = []

# glyphs
# update all glyphs based on the first master
# skip for shape and grid glyphs
for gl in font.glyphs:
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


