
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


def createDitherTile():
	#convert -size 2x2 xc:black \( +clone -draw 'fill white line 0,0 1,0' \) xc:white dpat_hlines2x2test3.gif
	pipe = subprocess.Popen(["convert", "-size", "2x2", "xc:black", "(", "+clone", "-draw", " ""fill white line 0,0 1,0"" ", ")", "xc:white", "dpat_hlines2x2.gif",], stderr=subprocess.PIPE).stderr
	print str(pipe.read())


def hlinesDither(input_img, output_img):
	#First you need to ammend the thresholds.xml file to include the dither pattern
	#
	#   <threshold map="hlines12x4" alias="hlines">
    #    <description>Horizontal Lines 12x4</description>
    #     <levels width="12" height="4" divisor="9">
    #        7 8 8 8 8 7 6 6 5 5 5 6
    #        2 1 1 1 1 2 3 4 4 4 3 3
    #        6 6 5 5 5 6 7 8 8 8 8 7
    #        3 4 4 4 3 3 2 1 1 1 1 2
    #     </levels>
    #   </threshold>
    #
    #convert test.png -ordered-dither hlines test-hlines.gif
    pipe = subprocess.Popen(["convert",input_img,"-ordered-dither","hlines",output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())

def hlinesDitherGray(input_img, output_img):
	#First you need to ammend the thresholds.xml file to include the dither pattern
	#
	#   <threshold map="hlines12x4" alias="hlines">
    #    <description>Horizontal Lines 12x4</description>
    #     <levels width="12" height="4" divisor="9">
    #        7 8 8 8 8 7 6 6 5 5 5 6
    #        2 1 1 1 1 2 3 4 4 4 3 3
    #        6 6 5 5 5 6 7 8 8 8 8 7
    #        3 4 4 4 3 3 2 1 1 1 1 2
    #     </levels>
    #   </threshold>
    #
    #convert test.png -ordered-dither hlines test-hlines.gif
    temp = tempfile.mkstemp(suffix = ".png")
    tempng = temp[1]

    pipe = subprocess.Popen(["convert",input_img,"-colorspace", "Gray",tempng,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng,"-ordered-dither","hlines",output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())

#### USAGE #####
#createDitherTile()
#hlinesDither("test.png","test-hlines.gif")
hlinesDitherGray("test.png","test-hlinesGray.gif")
#print "Created dither tile"
################




# convert concordia.jpg dpat_hlines2x2.gif  -channel A \
#           -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1].g' \
#           shadow_dpat_hlines2x2.gif


#           convert concordia.jpg  dpat_hlines2x2.gif -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1]' condgrad_hlines2x2.gif