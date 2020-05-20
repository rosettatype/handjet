#MenuTitle: set up instances

"""
Generate instances for a typeface incl. custom parameters
"""

# Rosetta weight names -> Glyphs weight names
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


def makeInstance(name, family_name, style_name, position):
    """
    Make instance using set parameters.
    """

    i = GSInstance()

    # generic parameters
    i.active = True
    i.name = name

    # names and MM parameters
    i.isItalic = False
    weight = style_name

    i.isBold = (weight == "Bold")
    i.weight = translateWeight[weight]
    i.width = "Medium (normal)"
    i.weightValue = position[0]
    i.widthValue = position[1]
    i.customValue = position[2]
    i.customParameters["familyName"] = family_name

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
              ("Rectangle", 600),
              ("Rounded Square", 820),
              ("Circle", 900),
              ("Flower", 1400),
              ("Star", 1500),
              ("Spindle", 1700),
              ("Heart", 1800),
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
                name = fname + " " + wght_name
                inst = makeInstance(name, fname, wght_name, position)
                font.instances.append(inst)

if __name__ == '__main__':
    main()
