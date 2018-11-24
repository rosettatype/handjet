#MenuTitle: set masters
# encoding: utf-8

font = Glyphs.currentDocument.font

customParameters = {
    "underlinePosition": -120,
    "underlineThickness": 10,
    "typoAscender": 900,
    "typoDescender": -300,
    "typoLineGap": 0,
    "hheaAscender": 900,
    "hheaDescender": -300,
    "hheaLineGap": 0,
    "winAscent": 900,
    "winDescent": 300,
}

for m in font.masters:
    for k, v in customParameters.items():
        m.customParameters[k] = v
        if "Big" in m.name:
            m.customParameters["underlineThickness"] = 120
