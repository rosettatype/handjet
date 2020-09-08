"""
A helper script to create a designspace for Handjet
"""
ds_path = "production/Handjet.designspace"

# The default instance
default = (400, 8.00, 1.0)

# Values for the three axis (value, is master, instance name):
# - Each entry is a design brace layer in the glyphs file
# - Only wghts will get added as fvar instances
# - Each named value will generate a named STAT entry by running
#   add_stat_table.py post font generation

# The weights
wghts = [
    (100, True, "Thin"),
    (200, False, "ExtraLight"),
    (300, False, "Light"),
    (400, True, "Regular"),
    (500, False, "Medium"),
    (600, False, "SemiBold"),
    (700, False, "Bold"),
    (800, False, "ExtraBold"),
    (900, True, "Black"),
]

# The shapes from the ESHP-xxxx glyph brace layer (In comments original
# "design" names)
# NOTE: In the design sources these brace layer value are multiplied by 100 to
# work around the limitation of not having decimal dots in the layer name.
ESHPs = [
    (0.00, True, "Blank"),
    (1.00, True, "Triangle"),
    (2.00, True, "Square"),
    (2.11, True, None),
    (2.25, True, "Lozerge"),
    (2.36, True, None),
    (2.50, True, None),
    (3.19, False, "Block"),
    (3.36, False, "Rectangle"),
    (4.00, True, "Bar (Vertical)"),
    (4.11, True, None),
    (4.25, True, "Bar (Diagonal Up)"),
    (4.36, True, None),
    (4.50, True, "Bar (Horizontal)"),
    (4.61, True, None),
    (4.75, True, "Bar (Diagonal Down)"),
    (4.86, True, None),
    (5.00, True, None),
    (6.50, True, None),
    (6.90, False, "Rounded square"),
    (7.63, False, "Squircle"),
    (8.00, True, "Circle"),
    (8.69, False, "Egg"),
    (8.86, False, "Oval"),
    (9.50, True, "Thin Oval"),
    (11.00, True, None),
    (12.00, False, "Clover"),
    (13.00, True, "Flower"),
    (14.00, True, "Star"),
    (14.11, True, None),
    (14.25, True, "Star (Diagonal)"),
    (14.36, True, None),
    (14.50, True, None),
    (14.75, False, "Big Star"),
    (15.00, True, "Spindle"),
    (15.37, False, "Pin"),
    (16.00, True, "Heart")
]

# The grid configurations from the EGRD-xxxx glyph brace layer
# Note EGRD values here in integer to match non-decimal brace layer names
# from source glyphs file
EGRDs = [
    (1, True, "Single"),
    (2, True, "Double"),
    (3, True, "Triple"),
]


# XML templates to write the designspace from

code = """<?xml version='1.0' encoding='UTF-8'?>
<designspace format="4.1">

<!-- Design space generated with production/make_designspaces.py script -->

<axes>
    <axis tag="wght" name="Weight"
        minimum="100" maximum="900" default="400" />
    <axis tag="ESHP" name="Element Shape"
        minimum="0.00" maximum="16.00" default="8.00" />
    <axis tag="EGRD" name="Element Grid"
        minimum="1.0" maximum="3.0" default="1.0" />
</axes>

<sources>
%s
</sources>

<instances>
%s
</instances>

<lib>
    <dict>
      <key>public.skipExportGlyphs</key>
      <array>
        <string>.notef</string>
        <string>pixel.ESHP-0</string>
        <string>pixel.ESHP-100</string>
        <string>pixel.ESHP-200</string>
        <string>pixel.ESHP-211</string>
        <string>pixel.ESHP-225</string>
        <string>pixel.ESHP-236</string>
        <string>pixel.ESHP-250</string>
        <string>pixel.ESHP-400</string>
        <string>pixel.ESHP-411</string>
        <string>pixel.ESHP-425</string>
        <string>pixel.ESHP-436</string>
        <string>pixel.ESHP-450</string>
        <string>pixel.ESHP-461</string>
        <string>pixel.ESHP-475</string>
        <string>pixel.ESHP-486</string>
        <string>pixel.ESHP-500</string>
        <string>pixel.ESHP-650</string>
        <string>pixel.ESHP-800</string>
        <string>pixel.ESHP-950</string>
        <string>pixel.ESHP-1100</string>
        <string>pixel.ESHP-1300</string>
        <string>pixel.ESHP-1400</string>
        <string>pixel.ESHP-1411</string>
        <string>pixel.ESHP-1425</string>
        <string>pixel.ESHP-1436</string>
        <string>pixel.ESHP-1450</string>
        <string>pixel.ESHP-1500</string>
        <string>pixel.ESHP-1600</string>
        <string>pixel.wght-100</string>
        <string>pixel.wght-400</string>
        <string>pixel.wght-900</string>
        <string>pixel.EGRD-1</string>
        <string>pixel.EGRD-2</string>
        <string>pixel.EGRD-3</string>
      </array>
    </dict>
  </lib>
</designspace>
"""

source = """
    <source filename="../master_ufo/Handjet-Regular.ufo"
        name="Handjet Regular %s" layer="%s">
        <location>
            <dimension name="Weight" xvalue="%s"/>
            <dimension name="Element Shape" xvalue="%s"/>
            <dimension name="Element Grid" xvalue="%s"/>
        </location>
    </source>
"""

source_base = """
    <!-- base source -->
    <source filename="../master_ufo/Handjet-Regular.ufo"
        name="Handjet Regular"
        familyname="Handjet" stylename="Regular">
        <lib copy="1" />
        <groups copy="1" />
        <features copy="1" />
        <info copy="1" />
        <location>
            <dimension name="Weight" xvalue="%s"/>
            <dimension name="Element Shape" xvalue="%s"/>
            <dimension name="Element Grid" xvalue="%s"/>
        </location>
    </source>
"""

instance = """
    <instance filename="../master_ufo/Handjet-Regular.ufo"
        name="Handjet Regular %s" layer="%s"
        familyname="Handjet" stylename="%s">
        <location>
            <dimension name="Weight" xvalue="%s"/>
            <dimension name="Element Shape" xvalue="%s"/>
            <dimension name="Element Grid" xvalue="%s"/>
        </location>
    </instance>
"""


def write_designspace():
    """Iterate over the axes and write the designspace"""

    sources = ""
    instances = ""

    for w, is_weight_master, weight_name in wghts:
        is_weight_default = w == default[0]

        for s, is_shape_master, shape_name in ESHPs:
            is_shape_default = s == default[1]

            for g, is_grid_master, grid_name in EGRDs:
                is_grid_default = g == default[2]

                if is_weight_master and is_shape_master and is_grid_master:
                    # Write the <source> for this combination
                    print("Adding <source> for location "
                          "(wght %d, ESHP %d, EGRD %d)"
                          % (w, s, int(g)))

                    if is_weight_default and is_shape_default and \
                            is_grid_default:
                        sources += source_base % (w, s, int(g))
                    else:
                        # NOTE For the brace layer (and glyphs sources) the
                        # layer cannot include decimals, so EGRD is 1-3, but
                        # for the actual axis value we want to use a single
                        # decimal to comply with the initial EGRD axis
                        # defintion which features decimals (to hint for apps
                        # what precision to use in the UI for this axis)
                        brace = "{%d,%d,%d}" % (w, s * 100, int(g))
                        sources += source % (brace, brace,
                                             w, s, "{0:0.1f}".format(g))

                # If shape and grid are the default, then write a named fvar
                # <instance> for this combination (weight)
                if is_shape_default and is_grid_default:
                    brace = "{%d,%d,%d}" % (w, s * 100, g)
                    stylename = weight_name
                    instances += instance % (brace, brace, stylename,
                                             w, s, "{0:0.1f}".format(g))
                    print("Adding named fvar <instance> '%s' for location "
                          "(wght %d, ESHP %d, EGRD %d)"
                          % (stylename, w, s, g))

    # Write all designspace parts
    ds = code % (sources, instances)
    with open(ds_path, "w") as f:
        f.write(ds)
        print("Designspace written to '%s'" % ds_path)


if __name__ == "__main__":
    write_designspace()
