# Handjet

Handjet is an element-based variable font (aka pixel font, modular font, …) where every glyph is composed using multiple copies of the same element. Each element can take one of 23 shapes and transition smoothly between them while creating various effects. The font currently supports these scripts: Arabic, Armenian, Cyrillic, Greek, Hebrew, and Latin.

![Handjet’s ESHP axis animation](docs/animations/Handjet-ESHP-animation.gif?raw=true)
![Handjet’s EGRD axis animation](docs/animations/Handjet-EGRD-animation.mp4?raw=true)

## The story

In autumn 2018 I was lucky to teach type design to a group of talented graphic design students at the [Faculty of Fine Arts in Brno](https://www.favu.vut.cz/en/studios/graphic-design2). Their first exercise was to build a simple element-based font that would be tailored to work well with [handjet printers](https://duckduckgo.com/?q=handjet+printer&ia=images). The handjet’s 32-pixel vertical matrix defined the constraints, the only contour to draw was the shape of the element, and the rest was “only” a matter of placing the elements on the grid to form letters. The clocks were ticking and the students were fierce. Most of them had their first font with basic English and Czech alphabets done by the end of the day!

Upon realizing the task could be taken even further, I set out to design my own font. I did not leave the house that weekend and ended up with a complete pan-European Latin. A couple of days later I had Greek and Cyrillic too. It was hard to stop. And once I started interpolating the element shapes, it got out of control completely.

In its current version, the Handjet type system contains 23 elemental shapes. Smooth transitions between them create various effects: a triangle appears out of thin air and expands into a square, the square rotates to create a lozenge and then scales into a thin rectangle, a rounded square smoothly turns into a circle, the circle into an oval, a clover becomes a rotating star, and a spindle, and a heart. The size of elements can be changed as well, producing different font weights. Plus, one can choose to use groups of 2x2 or 3x3 smaller elements instead of a single element. All of these work within a single variable font, allowing users to produce their custom variations and animations easily.

In 2019, Google sponsored the extension and open-sourcing of Handjet. All variations and element shapes have been thoroughly revisited and extended. Working with consultants Borna Izadpanah, Khajag Apelian, and Meir Sadan, I have also added support for Arabic, Armenian, and Hebrew (respectively). Selected symbols representing wildlife and domestic animals were included together with various seasonal symbols and patterns. The fonts are provided for free without any artistic aspirations, assumptions of originality, or kerning. I hope you will have as much fun using them as I had designing them.

— David Březina, September 2020

P.S. If you want to do this exercise with your students, have a look at this [Glyphs tutorial](https://glyphsapp.com/tutorials/pixelfont).

P.P.S. To be perfectly clear, I went way overboard of what Handjets’ grids permits. Hence, only some of the fonts are actually good-looking when used with the printers.

## Variable font

Handjet is primarily a variable font with three axes:

- **Weight (wght)** (100-900) controls the size of the element,
- **Element Shape (ESHP)** (0-16.0) controls the shape of the element,
- **Element Grid (EGRD)** (1.0-3.0) controls how many elements are used: a single element (single), a group of 2x2 elements (double), or a group of 3x3 elements (triple).

The interpolation between shapes creates a rotation or disappearing effect for some of the shapes.

## Source files

In principle all glyphs remain structually the same across all masters except for one special glyph: `pixel` which represents the element shape and is different for each master.

The `pixel` glyph is compiled from all non-exporting `pixel.xxx` glyphs and is the only component that changes between the masters of this Variable Font. You can recompile the `pixel` glyph by using the `production/glyphs-scripts/compile pixel glyph.py` GlyphsApp macro.

## Building a the Variable Font from the sources

- In your python3 environment, make sure to install the required pip packages: `$ pip install -r requirements.txt`
- Make sure you make the `production/build.sh` file executable: `$ chmod +x production/build.sh`
- To recompile, run `$ ./production/build.sh` and new fonts will be generated in the `fonts/` directory (it's a complex file and takes a while to recompile)

## Guide to the Element Shape axis (ESHP)

For preview of the available element shapes, see the animations above.

| Value | Description | Instance |
|---:|:---|:---|
| 0.00 | Blank | * |
| 1.00 | Triangle | * |
| 2.00 | Square | * |
| 2.11 | Square at 20 degrees | - |
| 2.25 | Lozenge | * |
| 2.36 | Square at 65 degrees | - |
| 2.50 | Square (transitional master) | x |
| 3.19 | Block | * |
| 3.36 | Rectangle | * |
| 4.00 | Bar (Vertical) | * |
| 4.11 | Bar at 20 degrees | - |
| 4.25 | Bar (Diagonal Up) | * |
| 4.36 | Bar at 65 degrees | - |
| 4.50 | Bar (Horizontal) | * |
| 4.61 | Bar at 110 degrees | - |
| 4.75 | Bar (Diagonal Down) | * |
| 4.86 | Bar at 155 degrees | - |
| 5.00 | Bar at 180 degrees | - |
| 6.50 | Square (transitional master) | x |
| 6.90 | Rounded Square | * |
| 7.63 | Squircle | * |
| 8.00 | Circle | * |
| 8.69 | Egg | * |
| 8.86 | Oval | * |
| 9.50 | Thin Oval | * |
| 11.00 | Circle (transitional master) | x |
| 12.00 | Clover | * |
| 13.00 | Flower | * |
| 14.00 | Star | * |
| 14.11 | Star at 20 degrees | - |
| 14.25 | Star (Diagonal) | * |
| 14.36 | Star at 65 degrees | - |
| 14.50 | Star at 90 degrees | - |
| 14.75 | Big Star | * |
| 15.00 | Spindle | * |
| 15.37 | Pin | * |
| 16.00 | Heart | * |

Rows marked with `*` are available as instances in the STAT table.  
Rows marked with `x` are repeated shapes to allow for a better transition.  
Rows marked with `-` are for example only.

## Scripting

If you would like to animate Handjet using Python and DrawBot, you can see the sources of the animations from this page in `tools/drawbot-scripts/`.
