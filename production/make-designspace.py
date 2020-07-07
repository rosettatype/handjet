"""
A helper script to create designspace for Handjet
"""

wght_masters = [
    # name, wght axis value, whether it is a default
    ("Thin", 100, False),
    ("Regular", 400, True),
    ("Black", 900, False),
]

SHAP_masters = [
    # name, SHAP axis value, whether it is a default
    ("Empty", 100, False),
    ("Triangle", 200, False),
    ("Square", 300, False),
    ("Tilted square 30", 333, False),
    ("Tilted square 60", 366, False),
    ("Tilted square 90", 400, False),
    ("Rectangle", 500, False),
    ("Tilted rectangle 30", 533, False),
    ("Tilted rectangle 60", 566, False),
    ("Tilted rectangle 90", 600, False),
    ("Tilted rectangle 120", 633, False),
    ("Tilted rectangle 150", 666, False),
    ("Tilted rectangle 180", 700, False),
    ("Square transition", 800, False),
    ("Circle", 900, True),
    ("Oval", 1000, False),
    ("Tilted oval 30", 1033, False),
    ("Tilted oval 60", 1066, False),
    ("Tilted oval 90", 1100, False),
    ("Tilted oval 120", 1133, False),
    ("Tilted oval 150", 1166, False),
    ("Tilted oval 180", 1200, False),
    ("Circle transition", 1300, False),
    ("Flower", 1400, False),
    ("Star", 1500, False),
    ("Tilted star 30", 1533, False),
    ("Tilted star 60", 1566, False),
    ("Tilted star 90", 1600, False),
    ("Spindle", 1700, False),
    ("Heart", 1800, False),
]

GRID_masters = [
    # name, wght axis value, whether it is a default
    ("Single", 10, True),
    ("Double", 50, False),
    ("Triple", 100, False),
]

SHAP_instances = [("Triangle", 200),
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

wght_instances = [("Extralight", 200),
                  ("Light", 300),
                  ("Regular", 400),
                  ("Medium", 500),
                  ("Semibold", 600),
                  ("Bold", 700),
                  ("Extrabold", 800),
                 ]

GRID_instances = [("", 10)]


code = """<?xml version='1.0' encoding='UTF-8'?>
<designspace format="4.1">
  
<!-- Design space generated with make-designspaces.py script -->

<axes>
    <axis tag="wght" name="Weight" minimum="100" maximum="900" default="400" />
    <axis tag="SHAP" name="Shape" minimum="100" maximum="1800" default="900" />
    <axis tag="GRID" name="Grid" minimum="10" maximum="100" default="10" />
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
        <string>pixel.SHAP-100</string>
        <string>pixel.SHAP-1000</string>
        <string>pixel.SHAP-1033</string>
        <string>pixel.SHAP-1066</string>
        <string>pixel.SHAP-1100</string>
        <string>pixel.SHAP-1133</string>
        <string>pixel.SHAP-1166</string>
        <string>pixel.SHAP-1200</string>
        <string>pixel.SHAP-1300</string>
        <string>pixel.SHAP-1400</string>
        <string>pixel.SHAP-1500</string>
        <string>pixel.SHAP-1533</string>
        <string>pixel.SHAP-1566</string>
        <string>pixel.SHAP-1600</string>
        <string>pixel.SHAP-1700</string>
        <string>pixel.SHAP-1800</string>
        <string>pixel.SHAP-200</string>
        <string>pixel.SHAP-300</string>
        <string>pixel.SHAP-333</string>
        <string>pixel.SHAP-366</string>
        <string>pixel.SHAP-400</string>
        <string>pixel.SHAP-500</string>
        <string>pixel.SHAP-533</string>
        <string>pixel.SHAP-566</string>
        <string>pixel.SHAP-600</string>
        <string>pixel.SHAP-633</string>
        <string>pixel.SHAP-666</string>
        <string>pixel.SHAP-700</string>
        <string>pixel.SHAP-800</string>
        <string>pixel.SHAP-900</string>
        <string>pixel.GRID-10</string>
        <string>pixel.GRID-100</string>
        <string>pixel.GRID-50</string>
        <string>pixel.wght-100</string>
        <string>pixel.wght-400</string>
        <string>pixel.wght-900</string>
      </array>
    </dict>
  </lib>
</designspace>
"""

sources = ""
source = """
<source filename="../master_ufo/Handjet-Regular.ufo" name="Handjet Regular %s" layer="%s">
    <location>
        <dimension name="Weight" xvalue="%d"/>
        <dimension name="Shape" xvalue="%d"/>
        <dimension name="Grid" xvalue="%d"/>
    </location>
</source>
"""
source_base = """
<!-- base source -->
<source filename="../master_ufo/Handjet-Regular.ufo" name="Handjet Regular" familyname="Handjet" stylename="Regular">
    <lib copy="1" />
    <groups copy="1" />
    <features copy="1" />
    <info copy="1" />
    <location>
        <dimension name="Weight" xvalue="%d"/>
        <dimension name="Shape" xvalue="%d"/>
        <dimension name="Grid" xvalue="%d"/>
    </location>
</source>
"""
instances = ""
instance = """
<instance filename="../master_ufo/Handjet-Regular.ufo" name="Handjet Regular %s" layer="%s" familyname="Handjet" stylename="%s">
    <location>
        <dimension name="Weight" xvalue="%d"/>
        <dimension name="Shape" xvalue="%d"/>
        <dimension name="Grid" xvalue="%d"/>
    </location>
</instance>
"""

for weight_name, w, is_base in wght_masters:
    for shape_name, s, is_base2 in SHAP_masters:
        for grid_name, g, is_base3 in GRID_masters:
            if is_base and is_base2 and is_base3:
                sources += source_base % (w, s, g)
            else:
                brace = "{%d,%d,%d}" % (w, s, g)
                stylename = "%s %s %s" % (weight_name, shape_name, grid_name)
                sources += source % (brace, brace, w, s, g)
for weight_name, w in wght_instances:
    for shape_name, s in SHAP_instances:
        for grid_name, g in GRID_instances:
            brace = "{%d,%d,%d}" % (w, s, g)
            stylename = " ".join([grid_name, shape_name, weight_name])
            instances += instance % (brace, brace, stylename, w, s, g)

code = code % (sources, instances)
with open("Handjet.designspace", "w") as f:
    f.write(code)
