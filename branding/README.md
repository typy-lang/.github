# TyPy brand

The TyPy mark is a `T` followed by a colon, as in a type annotation such as
`x: int`. The colon's upper dot is round and its lower dot square: dynamic
Python above, the compiled native program below.

| File | Use |
| --- | --- |
| `mark.svg` | The mark on its rounded tile, for sites, documents and slides |
| `avatar.svg`, `avatar.png` | The organization avatar; the square tile, which GitHub rounds itself |
| `wordmark-on-light.svg` | The mark and the name, on white or light backgrounds |
| `wordmark-on-dark.svg` | The mark and the name, on navy or dark backgrounds |
| `social-preview.svg`, `social-preview.png` | The repository's social preview, 1280 by 640 |
| `build.py` | Builds every file above |

## Colours

| Name | Hex | Use |
| --- | --- | --- |
| Navy | `#0B1F3A` | The tile, dark backgrounds, the name on light backgrounds |
| Navy light | `#173E6B` | The upper end of the tile's gradient |
| Amber | `#FBBF24` | The colon, and "Py" on dark backgrounds |
| Amber deep | `#F59E0B` | The lower end of the colon's gradient |
| Amber on white | `#B45309` | "Py" on light backgrounds, where amber is too pale to read |
| Snow | `#F8FAFC` | The T, and the name on dark backgrounds |
| Mist | `#BCCCDC` | Secondary text on navy |

## Type

The name is Lato Black and secondary text Lato Medium; code is Hack.
Every SVG holds the letters as outlines, so it displays the same without
any font installed. Lato is under the SIL Open Font License 1.1 and Hack
under the MIT license, both of which allow their use in a logo.

## Using the mark

- Keep clear space around the mark of at least a quarter of its width.
- Show it at 20 pixels or more; below that the colon's two shapes merge.
- Use the files as they are: do not recolour, stretch, rotate or outline
  the mark, and do not set the name in another typeface.
- The mark is not the Python logo and is not to be combined with it.

## Building the files

`build.py` needs Python 3 with fontTools, and Lato and Hack installed in
`/usr/share/fonts/truetype`, as Debian and Ubuntu install them. Run
`python3 build.py` in this directory. The PNG files are rendered from the
SVG files with a browser at 1:1, 512 by 512 for the avatar and 1280 by 640
for the social preview.
