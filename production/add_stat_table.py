import sys
from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib import TTFont
from make_designspace import (wghts, ELSHs, ELGRs)

path = sys.argv[1]
font = TTFont(path)

wght_axis = dict(
    tag="wght",
    name="Weight",
    values=[dict(nominalValue=v, name=n, rangeMinValue=min, rangeMaxValue=max) for v, _, n, min, max in wghts if n is not None]
)

shape_axis = dict(
    tag="ELSH",
    name="Element Shape",
    values=[dict(nominalValue=v, name=n, rangeMinValue=min, rangeMaxValue=max) for v, _, n, min, max in ELSHs if n is not None]
)

grid_axis = dict(
    tag="ELGR",
    name="Element Grid",
    values=[dict(nominalValue=v, name=n, rangeMinValue=min, rangeMaxValue=max) for v, _, n, min, max in ELGRs if n is not None]
)

print(wght_axis)
print(shape_axis)
print(grid_axis)

buildStatTable(font, [wght_axis, shape_axis, grid_axis], elidedFallbackName=2)

font.save(path)
print("Added STAT table to %s" % path)
