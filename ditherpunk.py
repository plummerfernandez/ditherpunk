
"""
Ditherpunk.py
Imagemagick scripts for dithering with python wrapper - http://www.imagemagick.org/Usage/quantize/
Copyright (C) 2015,  Matthew Plummer-Fernandez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
<http://www.gnu.org/licenses/>
"""

"""
___Threshold Maps for Ordered Dither Operations____

Path: /opt/local/etc/ImageMagick-6/thresholds.xml

Map              Alias        Description
----------------------------------------------------
threshold        1x1          Threshold 1x1 (non-dither)
checks           2x1          Checkerboard 2x1 (dither)
o2x2             2x2          Ordered 2x2 (dispersed)
o3x3             3x3          Ordered 3x3 (dispersed)
o4x4             4x4          Ordered 4x4 (dispersed)
o8x8             8x8          Ordered 8x8 (dispersed)
h4x4a            4x1          Halftone 4x4 (angled)
h6x6a            6x1          Halftone 6x6 (angled)
h8x8a            8x1          Halftone 8x8 (angled)
h4x4o                         Halftone 4x4 (orthogonal)
h6x6o                         Halftone 6x6 (orthogonal)
h8x8o                         Halftone 8x8 (orthogonal)
h16x16o                       Halftone 16x16 (orthogonal)
c5x5b            c5x5         Circles 5x5 (black)
c5x5w                         Circles 5x5 (white)
c6x6b            c6x6         Circles 6x6 (black)
c6x6w                         Circles 6x6 (white)
c7x7b            c7x7         Circles 7x7 (black)
c7x7w                         Circles 7x7 (white)
"""

import subprocess, os
import tempfile, time, datetime

#DITHER.PY

# montage dpat_hlines.gif   -filter box   -geometry 60x20+2+0 \
#           -tile x1 -background none  -frame 2   dpat_hlines_images.gif
#   convert gradient.png  dpat_hlines.gif  \
#           -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1]' \
#           dgrad_dpat_hlines.gif
#   convert shadow.png dpat_hlines.gif  -channel A \
#           -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1].g' \
#           shadow_dpat_hlines.gif


def createDitherTile():
	pipe = subprocess.Popen(["convert", filename, "-blur", "1x2", tempname], stderr=subprocess.PIPE).stderr
	print str(pipe.read())



convert concordia.jpg dpat_hlines2x2.gif  -channel A \
          -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1].g' \
          shadow_dpat_hlines2x2.gif


          convert concordia.jpg  dpat_hlines2x2.gif -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1]' condgrad_hlines2x2.gif