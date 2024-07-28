#!/usr/bin/env python3


import argparse
import os
import string


# From https://adrianroselli.com/2021/02/cistercian-svg.html
# A template string that requires a number= and classes= substitution.
# The number is a simple decimal number that the Cistercian glyphs represent.
# The classes are the CSS classes that the SVG uses to draw the glyphs.
# E.g. for the number 1234, the classes would be z1000 z200 z30 z4.
cistercian_svg = r"""\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 39.5 58.8" role="img" focusable="false" aria-labelledby="CistercianNumber" aria-describedby="CistercianDesc" id="CistercianGlyph" class="$classes">
  <title id="CistercianNumber">$number</title>
  <desc id="CistercianDesc">A number as represented in Cistercian glyph</desc>
  <style>
  path{fill:none;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10}
    .z1 .c1, .z2 .c2, .z3 .c3, .z4 .c4, .z5 .c5, .z6 .c6, .z7 .c7, .z8 .c8, .z9 .c9, .z10 .t1, .z20 .t2, .z30 .t3, .z40 .t4, .z50 .t5, .z60 .t6, .z70 .t7, .z80 .t8, .z90 .t9, .z100 .h1, .z200 .h2, .z300 .h3, .z400 .h4, .z500 .h5, .z600 .h6, .z700 .h7, .z800 .h8, .z900 .h9, .z1000 .d1, .z2000 .d2, .z3000 .d3, .z4000 .d4, .z5000 .d5, .z6000 .d6, .z7000 .d7, .z8000 .d8, .z9000 .d9 {
      stroke: currentColor;
    }
  </style>
  <path stroke="currentColor" d="M19.8 1v56.8"></path>
  <g id="Zeds">
    <path class="c1 c5 c7 c9" d="M38.5 1H19.8"></path>
    <path class="c2 c8 c9" d="M19.8 20.4h18.7"></path>
    <path class="c3" d="M19.8 1l18.7 19.4"></path>
    <path class="c4 c5" d="M19.8 20.4L38.5 1"></path>
    <path class="c6 c7 c8 c9" d="M38.5 20.4V1"></path>
  </g>
  <g id="Tens">
    <path class="t1 t5 t7 t9" d="M19.8 1H1"></path>
    <path class="t2 t8 t9" d="M1 20.4h18.8"></path>
    <path class="t3" d="M19.8 1L1 20.4"></path>
    <path class="t4 t5" d="M19.8 20.4L1 1"></path>
    <path class="t6 t7 t8 t9" d="M1 1v19.4"></path>
  </g>
  <g id="Hundreds">
    <path class="h1 h5 h7 h9" d="M19.8 57.8h18.7"></path>
    <path class="h2 h8 h9" d="M38.5 38.4H19.8"></path>
    <path class="h3" d="M19.8 57.8l18.7-19.4"></path>
    <path class="h4 h5" d="M19.8 38.4l18.7 19.4"></path>
    <path class="h6 h7 h8 h9" d="M38.5 57.8V38.4"></path>
  </g>
  <g id="Thousands">
    <path class="d1 d5 d7 d9" d="M1 57.8h18.8"></path>
    <path class="d2 d8 d9" d="M19.8 38.4H1"></path>
    <path class="d3" d="M19.8 57.8L1 38.4"></path>
    <path class="d4 d5" d="M19.8 38.4L1 57.8"></path>
    <path class="d6 d7 d8 d9" d="M1 38.4v19.4"></path>
  </g>
</svg>
"""


def main():
    reporoot = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    svgroot = os.path.join(reporoot, "assets", "cistercian", "svg")

    parser = argparse.ArgumentParser(description="Generate Cistercian SVGs.")
    parser.add_argument("--quiet", action="store_true", help="Save quietly")
    parsed = parser.parse_args()

    svg_template = string.Template(cistercian_svg)
    os.makedirs(svgroot, exist_ok=True)
    for thousand in range(10):
        for hundred in range(10):
            for ten in range(10):
                for one in range(10):
                    number = thousand * 1000 + hundred * 100 + ten * 10 + one
                    classlist = []
                    if thousand != 0:
                        classlist.append(f"z{thousand}000")
                    if hundred != 0:
                        classlist.append(f"z{hundred}00")
                    if ten != 0:
                        classlist.append(f"z{ten}0")
                    if one != 0:
                        classlist.append(f"z{one}")
                    classes = " ".join(classlist)
                    filename = f"cistercian-{number:04}.svg"
                    filepath = os.path.join(svgroot, filename)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(
                            svg_template.substitute(number=str(number), classes=classes)
                        )
                    if not parsed.quiet:
                        print(filepath)


if __name__ == "__main__":
    main()
