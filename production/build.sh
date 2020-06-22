set -x


# Clean up previous build runs
echo "Cleaning up folders"
rm -r instance_ufo
rm -r master_ufo
rm -r variable_otf
rm -r variable_ttf


# Make UFOs from latest sources
echo "Extracting ufo files from glyphs sources"
fontmake -g sources/Handjet.glyphs -o ufo


# For clarity's sake, explicitly remove the designspace fontmake outputs
# to show we are using the static one in the production folder
rm master_ufo/Handjet-Regular.designspace


# Compile Variable fonts
echo "Compiling TTF variable font from designspace"
fontmake -m production/Handjet.designspace -o variable
mkdir fonts
mv variable_ttf/Handjet-VF.ttf fonts/Handjet-VF.ttf
rm -r variable_ttf
