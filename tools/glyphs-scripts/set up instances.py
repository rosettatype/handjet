#MenuTitle: set up instances

"""
Generate instances for a typeface incl. custom parameters
"""

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
    font = Glyphs.currentDocument.font

    # Type-family name

    family_name = "Handjet"

    # Widths
    shapes = [("Triangle", 200),
              ("Square", 300),
              ("Lozenge", 349.5),
              ("Rectangle", 700),
              ("Rounded Square", 920),
              ("Circle", 1000),
              ("Flower", 1500),
              ("Star", 1600),
              ("Spindle", 1800),
              ("Heart", 1900),
              ]
    COMPLEX_SHAPES = [
            "Triangle",
            "Flower",
            "Spindle",
            "Heart",
    ]

    wghts = [("Extralight", 200),
             ("Light", 350),
             ("Regular", 400),
             ("Medium", 500),
             ("Semibold", 600),
             ("Bold", 700),
             ("Extrabold", 800),
             ]

    opszs = [("", 10),
             ("Double", 50),
             ("Triple", 100),
             ]


    # delete all instances
    font.setInstances_(None)

    for opsz_name, opsz_value in opszs:
        for shape_name, shape_value in shapes:
            for wght_name, wght_value in wghts:
                if opsz_name != "" and wght_name in COMPLEX_SHAPES:
                    continue
                if opsz_name:
                    fname = family_name + " " + opsz_name + " " + shape_name
                else:
                    # to avoid the extra word space
                    fname = family_name + " " + shape_name
                fname = fname.strip()
                position = (wght_value, shape_value, opsz_value)
                inst = makeInstance(fname, wght_name, position, superfamily=True)
                font.instances.append(inst)

if __name__ == '__main__':
    main()
