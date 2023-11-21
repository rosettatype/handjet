"""
A helper script to create a designspace for Handjet
"""
ds_path = "production/Handjet.designspace"

# The default instance
default = (400, 2.00, 1.0)

# Values for the three axis (value, is master, instance name):
# - Each entry is a design brace layer in the glyphs file
# - Only wghts will get added as fvar instances
# - Each named value will generate a named STAT entry by running
#   add_stat_table.py post font generation

# The weights
wghts = [
    (100, True, "Thin", 0, 150),
    (200, False, "ExtraLight", 151, 250),
    (300, False, "Light", 251, 350),
    (400, True, "Regular", 351, 450),
    (500, False, "Medium", 451, 550),
    (600, False, "SemiBold", 551, 650),
    (700, False, "Bold", 651, 750),
    (800, False, "ExtraBold", 751, 850),
    (900, True, "Black", 851, 1000),
]

# The shapes from the ELSH-xxxx glyph brace layer (In comments original
# "design" names)
# NOTE: In the design sources these brace layer value are multiplied by 100 to
# work around the limitation of not having decimal dots in the layer name.
ELSHs = [
    (0.00, True, "Blank", 0.000, 0.500),
    (1.00, True, "Triangle", 0.501, 1.500),
    (2.00, True, "Square", 1.501, 2.100),
    (2.11, True, None, None, None),
    (2.25, True, "Lozenge", 2.101, 2.500),
    (2.36, True, None, None, None),
    (2.50, True, None, None, None),
    (3.19, False, "Block", 2.501, 3.250),
    (3.36, False, "Rectangle", 3.251, 3.750),
    (4.00, True, "Bar (Vertical)", 3.751, 4.150),
    (4.11, True, None, None, None),
    (4.25, True, "Bar (Diagonal Up)", 4.151, 4.350),
    (4.36, True, None, None, None),
    (4.50, True, "Bar (Horizontal)", 4.351, 4.650),
    (4.61, True, None, None, None),
    (4.75, True, "Bar (Diagonal Down)", 4.651, 5.000),
    (4.86, True, None, None, None),
    (5.00, True, None, None, None),
    (6.50, True, None, None, None),
    (6.90, False, "Rounded square", 5.001, 7.500),
    (7.63, False, "Squircle", 7.501, 7.750),
    (8.00, True, "Circle", 7.751, 8.500),
    (8.69, False, "Egg", 8.501, 8.750),
    (8.86, False, "Oval", 8.751, 9.000),
    (9.50, True, "Thinner Oval", 9.001, 11.000), # "Oval Thin" breaks Indesign (?!)
    (11.00, True, None, None, None),
    (12.00, False, "Clover", 11.001, 12.500),
    (13.00, True, "Flower", 12.501, 13.500),
    (14.00, True, "Star", 13.501, 14.150),
    (14.11, True, None, None, None),
    (14.25, True, "Diagonal Star", 14.151, 14.500), # "Star (Diagonal)" breaks Indesign (?!)
    (14.36, True, None, None, None),
    (14.50, True, None, None, None),
    (14.75, False, "Big Star", 14.501, 14.850),
    (15.00, True, "Spindle", 14.851, 15.250),
    (15.37, False, "Pin", 15.251, 15.500),
    (16.00, True, "Heart", 15.501, 16.000)
]

# The grid configurations from the ELGR-xxxx glyph brace layer
# Note ELGR values here in integer to match non-decimal brace layer names
# from source glyphs file
ELGRs = [
    (1, True, "Single", 0.000, 1.500),
    (2, True, "Double", 1.501, 2.000),
]


# XML templates to write the designspace from

code = """<?xml version='1.0' encoding='UTF-8'?>
<designspace format="4.1">

<!-- Design space generated with production/make_designspaces.py script -->

<axes>
    <axis tag="wght" name="Weight"
        minimum="100" maximum="900" default="400" />
    <axis tag="ELSH" name="Element Shape"
        minimum="0.00" maximum="16.00" default="2.00" />
    <axis tag="ELGR" name="Element Grid"
        minimum="1.0" maximum="2.0" default="1.0" />
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
        <string>pixel.ELSH-0</string>
        <string>pixel.ELSH-100</string>
        <string>pixel.ELSH-200</string>
        <string>pixel.ELSH-211</string>
        <string>pixel.ELSH-225</string>
        <string>pixel.ELSH-236</string>
        <string>pixel.ELSH-250</string>
        <string>pixel.ELSH-400</string>
        <string>pixel.ELSH-411</string>
        <string>pixel.ELSH-425</string>
        <string>pixel.ELSH-436</string>
        <string>pixel.ELSH-450</string>
        <string>pixel.ELSH-461</string>
        <string>pixel.ELSH-475</string>
        <string>pixel.ELSH-486</string>
        <string>pixel.ELSH-500</string>
        <string>pixel.ELSH-650</string>
        <string>pixel.ELSH-800</string>
        <string>pixel.ELSH-950</string>
        <string>pixel.ELSH-1100</string>
        <string>pixel.ELSH-1300</string>
        <string>pixel.ELSH-1400</string>
        <string>pixel.ELSH-1411</string>
        <string>pixel.ELSH-1425</string>
        <string>pixel.ELSH-1436</string>
        <string>pixel.ELSH-1450</string>
        <string>pixel.ELSH-1500</string>
        <string>pixel.ELSH-1600</string>
        <string>pixel.wght-100</string>
        <string>pixel.wght-400</string>
        <string>pixel.wght-900</string>
        <string>pixel.ELGR-1</string>
        <string>pixel.ELGR-2</string>
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

    for w, is_weight_master, weight_name, _, _ in wghts:
        is_weight_default = w == default[0]

        for s, is_shape_master, shape_name, _, _ in ELSHs:
            is_shape_default = s == default[1]

            for g, is_grid_master, grid_name, _, _ in ELGRs:
                is_grid_default = g == default[2]

                if is_weight_master and is_shape_master and is_grid_master:
                    # Write the <source> for this combination
                    print("Adding <source> for location "
                          "(wght %d, ELSH %d, ELGR %d)"
                          % (w, s, int(g)))

                    if is_weight_default and is_shape_default and \
                            is_grid_default:
                        sources += source_base % (w, s, int(g))
                    else:
                        # NOTE For the brace layer (and glyphs sources) the
                        # layer cannot include decimals, so ELGR is 1-3, but
                        # for the actual axis value we want to use a single
                        # decimal to comply with the initial ELGR axis
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
                          "(wght %d, ELSH %d, ELGR %d)"
                          % (stylename, w, s, g))

    # Write all designspace parts
    ds = code % (sources, instances)
    with open(ds_path, "w") as f:
        f.write(ds)
        print("Designspace written to '%s'" % ds_path)


if __name__ == "__main__":
    write_designspace()
