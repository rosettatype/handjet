#MenuTitle: make instances
# encoding: utf-8

"""
Generate custom parameters in instances
"""

# Rosetta-specif setup

translateWeight = {"Thin": "Thin",
                   "Extralight": "ExtraLight",
                   "Light": "Light",
                   "Regular": "Regular",
                   "Medium": "Medium",
                   "Semibold": "SemiBold",
                   "Bold": "Bold",
                   "Extrabold": "ExtraBold",
                   "Black": "Black"
                   }
translateWidth = {"Compressed": "Condensed",
                  "Condensed": "SemiCondensed",
                  "Normal": "Medium (normal)",
                  "": "Medium (normal)",
                  "Extended": "Semi Expanded"
                  }


def makeInstance(family_name, style_name, position,
                 customParameters={}, width_name="Normal", superfamily=False):
    """
    Make instance using set parameters.
    """

    i = GSInstance()

    # generic parameters
    i.active = True
    i.name = style_name

    # names and MM parameters
    if style_name.find("Italic") != -1:
        i.isItalic = True
        weight = style_name.replace("Italic", "").strip()
        if not weight:
            weight = "Regular"
    else:
        i.isItalic = False
        weight = style_name

    i.isBold = (weight == "Bold")
    i.weight = translateWeight[weight]
    i.width = translateWidth[width_name]
    i.weightValue = position[0]
    i.widthValue = position[1]
    i.customValue = position[2]

    # custom parameters
    if superfamily:
        i.customParameters["familyName"] = family_name

    for key, value in customParameters.items():
        i.customParameters[key] = value

    return i


# Main

def main():
    Font = Glyphs.currentDocument.font

    # Type-family name

    family_name = "Handjet"

    # Widths
    wdths = [("Lozenge", 100),
             ("Slashleft", 200),
             ("Slashright", 300),
             ("Rectangle", 400),
             ("Square", 500),
             ("Circle", 600),
             ("Oval", 700),
             ("Ovalright", 800),
             ("Ovalleft", 900),
             ("Heart", 1000),
             ("Flower", 1100),
             ]

    wghts = [("Thin", 10),
             ("Extralight", 20),
             ("Light", 28),
             ("Regular", 42),
             ("Medium", 56),
             ("Semibold", 60),
             ("Bold", 80),
             ("Extrabold", 100),
             ("Black", 120),
             ]

    opszs = [("", 100),
             ("Double", 200),
             ]

    # delte all instances
    Font.setInstances_(None)

    for opsz_name, opsz_value in opszs:
        for wdth_name, wdth_value in wdths:
            for wght_name, wght_value in wghts:
                fname = family_name + " " + wdth_name + " " + opsz_name
                fname = fname.strip()
                position = (wght_value, wdth_value, opsz_value)
                inst = makeInstance(fname, wght_name, position, superfamily=True)
                Font.instances.append(inst)


if __name__ == '__main__':
    main()
