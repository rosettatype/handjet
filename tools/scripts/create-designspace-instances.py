"""
A helper script to write a file with temporary designspace <instance>
declarations based on the below matrix of axes
"""
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

instances = ""
instance = """
<instance filename="../master_ufo/Handjet-Regular.ufo" name="Handjet Regular %s" layer="%s" familyname="Handjet" stylename="%s" >
    <location>
        <dimension name="Weight" xvalue="%d"/>
        <dimension name="Shape" xvalue="%d"/>
        <dimension name="Optical size" xvalue="%d"/>
    </location>
</instance>
"""

for w in wghts:
    for s in shapes:
        for o in opszs:
            brace = "{%d,%d,%d}" % (w[1], s[1], o[1])
            stylename = o[0] + " " if o[0] != "" else ""
            stylename = stylename + "%s %s" % (w[0], s[0])
            instances = instances + instance % (brace, brace, stylename, w[1], s[1], o[1])

with open("production/instances-tmp.xml", "w") as f:
    f.write(instances)
