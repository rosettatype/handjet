# Handjet

Handjet is an element-based variable font (aka pixel font, modular font, …) where every glyph is composed using multiple copies of the same element. Each element can take 1 of 23 shapes and transition smoothly between them while creating various effects. The font currently supports these scripts: Arabic, Armenian, Cyrillic, Greek, Hebrew, Latin, and Korean.

![Handjet’s ELSH axis animation](docs/animations/Handjet-ELSH-animation_word.gif?raw=true)
![Handjet’s ELSH axis animation](docs/animations/Handjet-ELSH-animation_element.gif?raw=true)
![Handjet’s ELSH axis animation](docs/animations/Handjet-ELSH-animation_letter.gif?raw=true)
![Handjet’s wght axis animation](docs/animations/Handjet-wght-animation.gif?raw=true)
![Handjet’s ELGR axis animation](docs/animations/Handjet-ELGR-animation.gif?raw=true)


## The story

In autumn 2018, I had the opportunity to teach type design to a group of talented graphic design students at the [Faculty of Fine Arts in Brno](https://www.favu.vut.cz/en/studios/graphic-design2). Their first exercise was to build a simple element-based font that would be tailored to work well with [handjet printers](https://duckduckgo.com/?q=handjet+printer&ia=images). The handjet’s 32-pixel vertical matrix defined the constraints, the only contour to draw was the shape of the element, and the rest of the design job was “only” a matter of placing the elements on the grid to form letters. The clocks were ticking and the students were fierce. Most of them had their font with basic English and Czech alphabets done by the end of the day!

Upon realizing the task could be taken even further, I set out to design my own font. I did not leave the house that weekend and ended up with a complete pan-European Latin. A couple of days later I had Greek and Cyrillic too. It was hard to stop. And once I started interpolating the element shapes, it got out of control completely.

In its current version, the Handjet type system contains 23 elemental shapes. Smooth transitions between them create various effects: a triangle appears out of thin air and expands into a square, the square rotates to create a lozenge and then scales into a thin rectangle, a rounded square smoothly turns into a circle and the circle into an oval, a clover becomes a rotating star, and a spindle, and a heart. The size of elements can be changed as well, producing different font weights. Plus, one can choose to use groups of 2x2 smaller elements instead of a single element. All of these components work together within a single variable font, allowing users to produce their custom variations and animations easily.

In 2019, Google sponsored the extension and open-sourcing of Handjet. All variations and element shapes have been thoroughly revisited and extended. Working with consultants Borna Izadpanah, Khajag Apelian, and Meir Sadan, I have also added support for Arabic, Armenian, and Hebrew (respectively). Selected symbols representing wild and domestic animals were included together with various seasonal symbols and patterns. I hope you will have as much fun using them as I had designing them.

In 2023, Park Ha-neul (박하늘) and Lee-su Yoo (유이수) have included support for the Korean script.

— David Březina, September 2020

P.S. Warning: variable fonts are relatively new and Handjet sometimes challenges the limits. You might get unpredictable, yet beautiful and somewhat amusing, rendering errors in Adobe software. We have found that the InDesign 18 has issues with Handjet. Please, use an older version of InDesign until we find the cause. It works well in browsers as far as we know.

P.P.S. If you want to do this exercise with your students, have a look at this [Glyphs tutorial](https://glyphsapp.com/tutorials/pixelfont).

P.P.P.S. To be perfectly clear, I went way beyond what a handjet's grids permit, so only some of the fonts are suited to use with these printers.

![Handjet preview](docs/previews/Handjet-preview.svg?raw=true)

## Variable font

Handjet is a variable font with the following axes:

- **Weight (wght)** (100-900) controls the size of the element,
- **Element Shape (ELSH)** (0.0-16.0) controls the shape of the element,
- **Element Grid (ELGR)** (1.0-2.0) controls how many elements are used per one grid unit.

### Weight (wght)

The weight is represented by the size of the element used.

| Value | Description | Instance |
|---:|:---|:---|
| 100 | Thin | * |
| 200 | ExtraLight | * |
| 300 | Light | * |
| 400 | Regular | * |
| 500 | Medium | * |
| 600 | SemiBold | * |
| 700 | Bold | * |
| 800 | ExtraBold | * |
| 900 | Black | * |

### Element Shape axis (ELSH)

The interpolation between different element shapes along this axis creates a rotation or disappearing effect for some of them. This was done (instead of having independent rotation and scale axes for example) to simplify the design space, and to keep things manageable for users as well as computers. For a preview of the available element shapes and their transitions, see the animations above.

| Value | Description | Instance |
|---:|:---|:---|
| 0.00 | Blank | * |
| 1.00 | Triangle | * |
| 2.00 | Square (default) | * |
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
| 9.50 | Thinner Oval | * |
| 11.00 | Circle (transitional master) | x |
| 12.00 | Clover | * |
| 13.00 | Flower | * |
| 14.00 | Star | * |
| 14.11 | Star at 20 degrees | - |
| 14.25 | Diagonal Star | * |
| 14.36 | Star at 65 degrees | - |
| 14.50 | Star at 90 degrees | - |
| 14.75 | Big Star | * |
| 15.00 | Spindle | * |
| 15.37 | Pin | * |
| 16.00 | Heart | * |

Rows marked with `*` are available as instances in the STAT table.  
Rows marked with `x` are repeated shapes that allow for a better transition.  
Rows marked with `-` are for example only.

### Element Grid axis (ELGR)

This axis controls how many elements are used per one grid unit.

| Value | Description | Instance |
|---:|:---|:---|
| 1.00 | Single element (single) | * |
| 2.00 | Group of 2x2 elements (double) | * |

## Source files

In principle, all glyphs remain structurally the same across all masters except for one special glyph, `pixel`, which represents the element shape and is different for each master.

The `pixel` glyph is compiled from all non-exporting `pixel.xxx` glyphs and is the only component that changes between the masters of this variable font. You can recompile the `pixel` glyph by using the `production/glyphs-scripts/compile pixel glyph.py` macro in the Glyphs app.

## Building a the Variable Font from the sources

- In your Python 3 environment, make sure to install the required pip packages: `$ pip install -r requirements.txt`
- Make sure you make the `production/build.sh` file executable: `$ chmod +x production/build.sh`
- To recompile, run `$ ./production/build.sh` and new fonts will be generated in the `fonts/` directory (it's a complex file and takes a while to recompile)

## Scripting

If you would like to animate Handjet using Python and [DrawBot](http://drawbot.com), you can check out the [source code for the animations](tools/drawbot-scripts/).
