#MenuTitle: save glyph set for flythrough animation

"""
Save glyph names, unicodes, and show status for Handjet flythrough animation
"""

import GlyphsApp

selected = Glyphs.font.selectedLayers

for ll in selected:
	gn = ll.parent.name
	u = ll.parent.unicode
	c = len(ll.components)
	if gn != ".notdef":
		if ("comb" not in gn) and ("space" not in gn) and (ll.width != 0) and (c > 1) and (ll.parent.export == True):
			s = True
		else:
			s = False
		if u:
			print("%s,0x%s,%s" % (gn, u, s))
		else:
			print("%s,,%s" % (gn, s))