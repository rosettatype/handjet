import sys
from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib import TTFont
from make_designspace import (SHAP_instances, wght_instances, GRID_instances)

path = sys.argv[1]
font = TTFont(path)

wghts = dict(
    tag="wght",
    name="Weight",
    values=[dict(value=v, name=n) for n, v in wght_instances]
)

shaps = dict(
    tag="SHAP",
    name="Shape",
    values=[dict(value=v, name=n) for n, v in SHAP_instances]
)

grids = dict(
    tag="GRID",
    name="Grid",
    values=[dict(value=v, name=n) for n, v in GRID_instances]
)

buildStatTable(font, [wghts, shaps, grids], elidedFallbackName=2)

font.save(path)
