#MenuTitle: set masters
# encoding: utf-8

from collections import OrderedDict

font = Glyphs.currentDocument.font

masters_axes = OrderedDict([
    ("Small Lozenge", [10, 100, 100]),
    ("Small Slashleft", [10, 200, 100]),
    ("Small Slashright", [10, 300, 100]),
    ("Small Rectangle", [10, 400, 100]),
    ("Small Square", [10, 500, 100]),
    ("Small Ovalright", [10, 600, 100]),
    ("Small Ovalleft", [10, 700, 100]),
    ("Small Oval", [10, 800, 100]),
    ("Small Circle", [10, 900, 100]),
    ("Small Heart", [10, 1000, 100]),
    ("Small Flower", [10, 1100, 100]),
    ("Big Lozenge", [120, 100, 100]),
    ("Big Slashleft", [120, 200, 100]),
    ("Big Slashright", [120, 300, 100]),
    ("Big Rectangle", [120, 400, 100]),
    ("Big Square", [120, 500, 100]),
    ("Big Ovalright", [120, 600, 100]),
    ("Big Ovalleft", [120, 700, 100]),
    ("Big Oval", [120, 800, 100]),
    ("Big Circle", [120, 900, 100]),
    ("Big Heart", [120, 1000, 100]),
    ("Big Flower", [120, 1100, 100]),
    ("Small Double Lozenge", [10, 100, 100]),
    ("Small Double Slashleft", [10, 200, 100]),
    ("Small Double Slashright", [10, 300, 100]),
    ("Small Double Rectangle", [10, 400, 100]),
    ("Small Double Square", [10, 500, 100]),
    ("Small Double Ovalright", [10, 600, 100]),
    ("Small Double Ovalleft", [10, 700, 100]),
    ("Small Double Oval", [10, 800, 100]),
    ("Small Double Circle", [10, 900, 100]),
    ("Small Double Heart", [10, 1000, 100]),
    ("Small Double Flower", [10, 1100, 100]),
    ("Big Double Lozenge", [120, 100, 100]),
    ("Big Double Slashleft", [120, 200, 100]),
    ("Big Double Slashright", [120, 300, 100]),
    ("Big Double Rectangle", [120, 400, 100]),
    ("Big Double Square", [120, 500, 100]),
    ("Big Double Ovalright", [120, 600, 100]),
    ("Big Double Ovalleft", [120, 700, 100]),
    ("Big Double Oval", [120, 800, 100]),
    ("Big Double Circle", [120, 900, 100]),
    ("Big Double Heart", [120, 1000, 100]),
    ("Big Double Flower", [120, 1100, 100]),
])

metrics = {}
metrics["ascender"] = 720
metrics["capHeight"] = 660
metrics["xHeight"] = 480
metrics["descender"] = -180
metrics["italicAngle"] = 0

customParameters = {
    "underlinePosition": -120,
    "underlineThickness": 10,
    "typoAscender": 780,
    "typoDescender": -240,
    "typoLineGap": 0,
    "hheaAscender": 780,
    "hheaDescender": -240,
    "hheaLineGap": 0,
    "winAscent": 780,
    "winDescent": 240,
}

for m in font.masters:
    for k, v in customParameters.items():
        m.customParameters[k] = v
        if "Big" in m.name:
            m.customParameters["underlineThickness"] = 120
