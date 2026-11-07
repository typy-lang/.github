"""TyPy's annotation mark: a T and a colon, as in `x: T`.

The colon's upper dot is round and its lower dot square: dynamic Python above, the compiled
native program below. Letters are Lato outlines (SIL Open Font License 1.1) and Hack outlines
(MIT), so the SVG files need no font installed. Building them needs both fonts installed in
/usr/share/fonts/truetype, as Debian and Ubuntu install them; run `python3 build.py`.
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTS = {
    "lato-black": "/usr/share/fonts/truetype/lato/Lato-Black.ttf",
    "lato-heavy": "/usr/share/fonts/truetype/lato/Lato-Heavy.ttf",
    "lato-bold": "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
    "lato-medium": "/usr/share/fonts/truetype/lato/Lato-Medium.ttf",
    "hack-bold": "/usr/share/fonts/truetype/hack/Hack-Bold.ttf",
    "hack": "/usr/share/fonts/truetype/hack/Hack-Regular.ttf",
}
_cache = {}


def _font(name):
    if name not in _cache:
        _cache[name] = TTFont(FONTS[name])
    return _cache[name]


def text(content, font, size, x, y, fill, extra=""):
    """Returns a path for `content` with its baseline at `y`, its width and its ink bounds."""
    face = _font(font)
    glyphs, cmap = face.getGlyphSet(), face.getBestCmap()
    scale = size / face["head"].unitsPerEm
    pairs = {}
    for table in face["kern"].kernTables if "kern" in face else []:
        pairs.update(table.kernTable)
    pen, bounds = SVGPathPen(glyphs), BoundsPen(glyphs)
    cursor, previous = 0.0, None
    for character in content:
        name = cmap[ord(character)]
        if previous:
            cursor += pairs.get((previous, name), 0)
        transform = (scale, 0, 0, -scale, x + cursor * scale, y)
        glyphs[name].draw(TransformPen(pen, transform))
        glyphs[name].draw(TransformPen(bounds, transform))
        cursor += face["hmtx"][name][0]
        previous = name
    return f'<path d="{pen.getCommands()}" fill="{fill}"{extra}/>', cursor * scale, bounds.bounds


def centred(content, font, size, box, fill, dx=0, dy=0, extra=""):
    """Returns `content` with its ink centred in the square `box` = (x, y, side)."""
    _, _, (left, top, right, bottom) = text(content, font, size, 0, 0, fill)
    x0, y0, side = box
    x = x0 + side / 2 - (left + right) / 2 + dx
    y = y0 + side / 2 - (top + bottom) / 2 + dy
    return text(content, font, size, x, y, fill, extra)[0]


def svg(width, height, body, defs="", background=None):
    fill = f'<rect width="{width:g}" height="{height:g}" fill="{background}"/>\n  ' if background else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:g}" height="{height:g}" '
        f'viewBox="0 0 {width:g} {height:g}" role="img" aria-label="TyPy">\n  <title>TyPy</title>\n'
        f"  <defs>{defs}</defs>\n  {fill}{body}\n</svg>\n"
    )


def tile(x, y, side, fill, square):
    corner = "" if square else f' rx="{side * 0.227:g}"'
    return f'<rect x="{x:g}" y="{y:g}" width="{side:g}" height="{side:g}"{corner} fill="{fill}"/>'


NAVY, NAVY_LIGHT, AMBER, AMBER_DEEP, SNOW, MIST = "#0B1F3A", "#173E6B", "#FBBF24", "#F59E0B", "#F8FAFC", "#BCCCDC"
DEFS = (
    '<linearGradient id="tile" x1="0" y1="0" x2="1" y2="1">'
    f'<stop offset="0" stop-color="{NAVY_LIGHT}"/><stop offset="1" stop-color="{NAVY}"/></linearGradient>'
    '<linearGradient id="amber" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{AMBER}"/><stop offset="1" stop-color="{AMBER_DEEP}"/></linearGradient>'
)


def mark(square=False):
    corner = "" if square else ' rx="116"'
    return "\n  ".join([
        f'<rect width="512" height="512"{corner} fill="url(#tile)"/>',
        f'<rect x="108" y="136" width="216" height="64" rx="30" fill="{SNOW}"/>',
        f'<rect x="184" y="136" width="64" height="244" rx="30" fill="{SNOW}"/>',
        '<circle cx="368" cy="236" r="36" fill="url(#amber)"/>',
        '<rect x="332" y="308" width="72" height="72" rx="16" fill="url(#amber)"/>',
    ])


def scaled(x, y, size, square=False):
    return f'<g transform="translate({x:g} {y:g}) scale({size / 512:g})">\n  {mark(square)}\n  </g>'


open("mark.svg", "w").write(svg(512, 512, mark(), DEFS))
open("avatar.svg", "w").write(svg(512, 512, mark(square=True), DEFS))
for name, ink, accent in (("wordmark-on-light", NAVY, "#B45309"), ("wordmark-on-dark", SNOW, AMBER)):
    ty, width, _ = text("Ty", "lato-black", 196, 240, 160, ink)
    py, more, _ = text("Py", "lato-black", 196, 240 + width, 160, accent)
    open(f"{name}.svg", "w").write(svg(240 + width + more + 14, 222, "\n  ".join([scaled(0, 2, 210), ty, py]), DEFS))

# The social preview: typed Python fades into the ground, its annotation colons lit.
code = [
    ("def area(w", ": ", "int, h", ": ", "int) -> int", ":"),
    ("total", ": ", "float = 0.0"),
    ("name", ": ", 'str = "typy"'),
]
lines, y = [], 96
for row in code:
    x = 730
    for part in row:
        colon = part.strip() == ":"
        shape, width, _ = text(part, "hack", 26, x, y, AMBER if colon else "#3B5A80",
                               ' fill-opacity="0.9"' if colon else ' fill-opacity="0.6"')
        lines.append(shape)
        x += width
    y += 44
ty, width, _ = text("Ty", "lato-black", 180, 470, 380, SNOW)
py, _, _ = text("Py", "lato-black", 180, 470 + width, 380, AMBER)
line1 = text("Typed Python, compiled ahead of time", "lato-medium", 34, 474, 470, MIST)[0]
line2 = text("to small native executables.", "lato-medium", 34, 474, 516, MIST)[0]
body = "\n  ".join(lines + [scaled(110, 230, 300), ty, py, line1, line2])
ground = DEFS + ('<linearGradient id="ground" x1="0" y1="0" x2="1" y2="1">'
                 f'<stop offset="0" stop-color="#0E2747"/><stop offset="1" stop-color="#081629"/></linearGradient>')
open("social-preview.svg", "w").write(svg(1280, 640, '<rect width="1280" height="640" fill="url(#ground)"/>\n  ' + body, ground))
