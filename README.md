# Handjet

By: David Březina  
Released in: May 2020

## Scripts

- Arabic
- Armenian
- Cyrillic
- Greek
- Latin

## Variable font

Handjet is an element-based design (aka pixel font, modular font, …) where every glyph is composed using multiple copies of the same element. Handjet is primarily a variable font with three axes:

- **Weight (wght)** controls the size of the element,
- **Shape (SHAP)** controls the shape of the element,
- **Optical size (opsz)** controls how many elements are used per one grid unit: a single element, a group of 2x2 elements, or a group of 3x3 elements.

The interpolation between shapes creates a rotation or disappearing effect for some of them.

## Source files

In principle all glyphs remain the same across all masters except for one special glyph: `pixel` which represents the element shape.

There are three source files.

`Handjet-Shapes.glyphs` contains individual layers for the `pixel` glyph. Glyphs named `pixel.SHAP-XXXX` become layers in the `pixel` glyph on the `SHAP` axis. Glyphs named `pixel.wght-XXX` specify tranformation (scale) applied to the `pixel` glyph (their content is not copied, only the transformation is copied). Glyphs named `pixel.opsz-XXX` specify the grid/layout changes along the `opsz` axis. All of these layer-glyphs are combined together using a macro `compile pixel glyph.py`. Warning: the grid spacing in Glyphs’ font info is set to 1! This is important, otherwise the contours in the `pixel` glyph may be distorted.

`Handjet-Characters.glyphs` contains all characters with a single layer. Note that `pixel` glyph also has only one layer. Warning: the grid spacing in Glyphs’ font info is set to 120! This makes drawing the composite glyphs simple.

`Handjet-Uprights.glyphs` is the source used for production, it contains all characters in all required masters (27 masters specified in the font info). Note that `pixel` has many brace layers to avoid the need for too many masters in the font info. Warning: the grid spacing in font info is set to 1! This is important, otherwise the contours in the `pixel` glyph may be distorted.

To populate the `Handjet-Uprights.glyphs` one needs to:

1. Remove all glyphs from `Handjet-Uprights.glyphs`.
2. Copy all glyphs from `Handjet-Characters.glyphs` to `Handjet-Uprights.glyphs`.
3. In `Handjet-Uprights.glyphs` replicate the single master to all masters using the `set up masters.py` macro. This also sets up masters values in font info.
4. Copy all glyphs from `Handjet-Shapes.glyphs` to `Handjet-Uprights.glyphs`.
5. In `Handjet-Uprights.glyphs` compile the `pixel` glyph anew using the `compile pixel glyph.py` macro.

NOTE: Make sure you preserve all font info in `Handjet-Uprights.glyphs` during this process.

NOTE: In addition to the created masters, the `pixel` glyph will have additional brace layer masters.

The masters and instances in the `Handjet-Uprights.glyphs` can be set up using macros too, but they are currently left empty. There were too many instances in the font info and it slowed the Glyphs app down significantly.

