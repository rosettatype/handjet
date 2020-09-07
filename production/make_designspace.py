"""
A helper script to create a designspace for Handjet
"""
ds_path = "production/Handjet.designspace"

# The default instance
default = (400, 900, 1.0)

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
ESHPs = [
    (100, True, "Empty"),
    (200, True, "Triangle"),
    (300, True, "Square"),
    (333, True, None),
    (349, False, "Lozerge"),
    (366, True, None),
    (400, True, None),
    (425, False, None),
    (450, False, "Rectangle"),
    (500, True, "Bar (Vertical)"),
    (533, True, None),  # Tilted rectangle 30
    (550, False, "Bar (Diagonal Up)"),
    (566, True, None),  # Tilted rectangle 60
    (600, True, "Bar (Horizontal)"),
    (633, True, None),  # Tilted rectangle 120
    (650, False, "Bar (Diagonal Down)"),
    (666, True, None),  # Tilted rectangle 150
    (700, True, None),  # Tilted rectangle 180
    (800, True, None),  # Square transition
    (820, False, "Rounded square"),
    (875, False, "Squircle"),
    (900, True, "Circle"),
    (933, False, "Egg"),
    (950, False, "Oval"),
    (1000, True, None),  # Oval
    (1033, True, None),  # Tilted oval 30
    (1066, True, None),  # Tilted oval 60
    (1100, True, None),  # Tilted oval 90
    (1133, True, None),  # Tilted oval 120
    (1166, True, None),  # Tilted oval 150
    (1200, True, None),  # Tilted oval 180
    (1300, True, "Circle transition"),
    (1350, False, "Clover"),
    (1400, True, "Flower"),
    (1500, True, "Star (Diagonal)"),
    (1533, True, None),  # Tilted star 30
    (1566, True, None),  # Tilted star 60
    (1600, True, None),  # Tilted star 90
    (1650, False, None),  # Big Star
    (1700, True, "Spindle"),
    (1737, False, None),  # Pin
    (1800, True, "Heart"),
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
        minimum="100" maximum="1800" default="900" />
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
        <string>pixel.ESHP-100</string>
        <string>pixel.ESHP-1000</string>
        <string>pixel.ESHP-1033</string>
        <string>pixel.ESHP-1066</string>
        <string>pixel.ESHP-1100</string>
        <string>pixel.ESHP-1133</string>
        <string>pixel.ESHP-1166</string>
        <string>pixel.ESHP-1200</string>
        <string>pixel.ESHP-1300</string>
        <string>pixel.ESHP-1400</string>
        <string>pixel.ESHP-1500</string>
        <string>pixel.ESHP-1533</string>
        <string>pixel.ESHP-1566</string>
        <string>pixel.ESHP-1600</string>
        <string>pixel.ESHP-1700</string>
        <string>pixel.ESHP-1800</string>
        <string>pixel.ESHP-200</string>
        <string>pixel.ESHP-300</string>
        <string>pixel.ESHP-333</string>
        <string>pixel.ESHP-366</string>
        <string>pixel.ESHP-400</string>
        <string>pixel.ESHP-500</string>
        <string>pixel.ESHP-533</string>
        <string>pixel.ESHP-566</string>
        <string>pixel.ESHP-600</string>
        <string>pixel.ESHP-633</string>
        <string>pixel.ESHP-666</string>
        <string>pixel.ESHP-700</string>
        <string>pixel.ESHP-800</string>
        <string>pixel.ESHP-900</string>
        <string>pixel.EGRD-10</string>
        <string>pixel.EGRD-100</string>
        <string>pixel.EGRD-50</string>
        <string>pixel.wght-100</string>
        <string>pixel.wght-400</string>
        <string>pixel.wght-900</string>
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
                        brace = "{%d,%d,%d}" % (w, s, int(g))
                        sources += source % (brace, brace,
                                             w, s, "{0:0.1f}".format(g))

                # If shape and grid are the default, then write a named fvar
                # <instance> for this combination (weight)
                if is_shape_default and is_grid_default:
                    brace = "{%d,%d,%d}" % (w, s, g)
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
