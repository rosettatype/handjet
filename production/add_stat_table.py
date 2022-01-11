import sys
from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib import TTFont
from make_designspace import (wghts, ESHPs, EGRDs)

path = sys.argv[1]
font = TTFont(path)

wght_axis = dict(
    tag="wght",
    name="Weight",
    values=[dict(nominalValue=v, name=n) for v, _, n in wghts if n is not None]
)

shape_axis = dict(
    tag="ESHP",
    name="Element Shape",
    values=[dict(nominalValue=v, name=n) for v, _, n in ESHPs if n is not None]
)

grid_axis = dict(
    tag="EGRD",
    name="Element Grid",
    values=[dict(nominalValue=v, name=n) for v, _, n in EGRDs if n is not None]
)

buildStatTable(font, [wght_axis, shape_axis, grid_axis], elidedFallbackName=2)

font.save(path)
print("Added STAT table to %s" % path)
