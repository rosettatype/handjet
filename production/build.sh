set -x


# Clean up previous build runs
echo "Cleaning up folders"
rm -r instance_ufo
rm -r master_ufo
rm -r variable_ttf


# Make UFOs from latest sources
echo "Extracting ufo files from glyphs sources"
# Use glyphs2ufo directly instead of fontmake in order to prevent output of
# faulty GDEF (fontmake seems to use the glyphs2ufo --generate-GDEF api)
# See https://github.com/googlefonts/glyphsLib/issues/620
glyphs2ufo --output-dir master_ufo sources/Handjet.glyphs 


# For clarity's sake, explicitly remove the designspace fontmake outputs
# to show we are using the static one in the production folder
rm master_ufo/Handjet-Regular.designspace


# Compile latest designspace
python production/make_designspace.py production/Handjet.designspace


# Compile Variable fonts
echo "Compiling TTF variable font from designspace"
fontmake -m production/Handjet.designspace -o variable --production-names


# Add STAT table
python production/add_stat_table.py variable_ttf/Handjet-VF.ttf


# Fix GASP table
gftools fix-nonhinting variable_ttf/Handjet-VF.ttf variable_ttf/Handjet-VF.ttf.2
gftools fix-dsig --autofix variable_ttf/Handjet-VF.ttf.2


# Move fonts to final destination & cleanup
mkdir fonts
mv variable_ttf/Handjet-VF.ttf.2 fonts/Handjet\[EGRD\,ESHP\,wght\].ttf
rm -r variable_ttf

# Run fontbakery
fontbakery check-googlefonts --ghmarkdown test/Handjet-report.md fonts/Handjet\[EGRD\,ESHP\,wght\].ttf
