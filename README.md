# Handjet

By: David Březina  
Completed in: May 2020

## Scripts

- Arabic
- Armenian
- Cyrillic
- Greek
- Hebrew
- Latin

## Variable font

Handjet is an element-based design (aka pixel font, modular font, …) where every glyph is composed using multiple copies of the same element. Handjet is primarily a variable font with three axes:

- **Weight (wght)** (100-900) controls the size of the element,
- **Element Shape (ESHP)** (100-1800) controls the shape of the element,
- **Element Grid (EGRD)** (1.0-3.0) controls how many elements are used per one grid unit: a single element, a group of 2x2 elements (duoble), or a group of 3x3 elements (triple).

The interpolation between shapes creates a rotation or disappearing effect for some of them.

## Source files

In principle all glyphs remain structually the same across all masters except for one special glyph: `pixel` which represents the element shape and is different for each master.

The `pixel` glyph is compiled from all non-exporting `pixel.xxx` glyphs and is the only component that changes between the masters of this Variable Font. You can recompile the `pixel` glyph by using the `production/glyphs-scripts/compile pixel glyph.py` GlyphsApp macro.

## Building a the Variable Font from the sources

- In your python3 environment, make sure to install the required pip packages: `$ pip install -r requirements.txt`
- Make sure you make the `production/build.sh` file executable: `$ chmod +x production/build.sh`
- To recompile, run `$ ./production/build.sh` and new fonts will be generated in the `fonts/` directory (it's a complex file and takes a while to recompile)