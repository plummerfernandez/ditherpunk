
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
    #convert test.png -ordered-dither h16x16o test-h16x16o.gif
    
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

def mpflinesDitherGray(input_img, output_img):
	#First you need to ammend the thresholds.xml file to include the dither pattern

    #convert test.png -ordered-dither hlines test-hlines.gif
    temp = tempfile.mkstemp(suffix = ".png")
    tempng = temp[1]

    pipe = subprocess.Popen(["convert",input_img,"-colorspace", "Gray",tempng,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng,"-ordered-dither","mpf2lines",output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())

def diagDitherGray(input_img, output_img):
	#First you need to ammend the thresholds.xml file to include the dither pattern
	#
	#  <threshold map="diag5x5" alias="diag">
    #   <description>Simple Diagonal Line Dither</description>
    #    <levels width="5" height="5" divisor="6">
    #       4 2 1 3 5
    #       2 1 3 5 4
    #       1 3 5 4 2
    #       3 5 4 2 1
    #       5 4 2 1 3
    #    </levels>
    #  </threshold>
    #
    #convert test.png -ordered-dither diag test-diaggray.gif
    temp = tempfile.mkstemp(suffix = ".png")
    tempng = temp[1]

    pipe = subprocess.Popen(["convert",input_img,"-colorspace", "Gray",tempng,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng,"-ordered-dither","diag",output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())


def bayerDitherGray(input_img, output_img): 
	#found here: https://github.com/polemon/dither/blob/master/ordered.py
	#First you need to ammend the thresholds.xml file to include the dither pattern

    #convert test.png -ordered-dither diag test-diaggray.gif
    temp = tempfile.mkstemp(suffix = ".png")
    tempng = temp[1]

    pipe = subprocess.Popen(["convert",input_img,"-colorspace", "Gray",tempng,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng,"-ordered-dither","bayer3x3",output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())


def contrastAlgoGray(ditheralgo,input_img,output_img):
    temp = tempfile.mkstemp(suffix = ".png")
    tempng = temp[1]
    temp2 = tempfile.mkstemp(suffix = ".png")
    tempng2 = temp2[1]

    pipe = subprocess.Popen(["convert",input_img,"-colorspace", "Gray",tempng,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng,"-contrast", "-contrast",tempng2,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng2,"-ordered-dither",ditheralgo,output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())	
    pipe.close()

def newsDitherGray(input_img, output_img):
	#First you need to ammend the thresholds.xml file to include the dither pattern

    #convert test.png -ordered-dither diag test-diaggray.gif
    temp = tempfile.mkstemp(suffix = ".png")
    tempng = temp[1]

    pipe = subprocess.Popen(["convert",input_img,"-colorspace", "Gray",tempng,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())
    pipe = subprocess.Popen(["convert",tempng,"-ordered-dither","news8x8",output_img,], stderr=subprocess.PIPE).stderr
    print str(pipe.read())    



def vidToStills(input_vid, output_dir):
	# ffmpeg -i video.mpg -r 1 -f image2 ffmpeg_temp/%05d.png
	pipe = subprocess.Popen(["ffmpeg", "-i",input_vid,"-r","1","-f","image2",output_dir+"%07d"+".png"], stderr=subprocess.PIPE).stderr
	print str(pipe.read())


def stillsToDitherStills(ditherdef, input_dir, output_dir):
	for f in os.listdir(input_dir):
		print f
		ditherdef("mpf2lines",input_dir+f, output_dir+f)
		time.sleep(0.5)


def stillsToDitherStills2(ditherdef, input_dir, output_dir):
	#for f in os.listdir(input_dir):
	for i in range(620, 712):
		print i
		f= str('%07d' % i) + ".png"
		print f
		ditherdef("mpf2lines",input_dir+f, output_dir+f)
		time.sleep(0.5)

#### USAGE #####
#createDitherTile()
#hlinesDither("test.png","test-hlines.gif")
#hlinesDitherGray("test.png","test-hlinesGray.gif")
#mpflinesDitherGray("test.png","test-mpf2linesGray.gif")
#bayerDitherGray("test.png","test-bayerGray.gif")
#newsDitherGray("test.png","test-newsGray.gif")
#print "Created dither tile"

#inputVid = "/Users/plummerfernandez/Documents/plummerfernandez/16_01_02_Jumpers/film/lune.avi"
#outputDir = "/Users/plummerfernandez/Documents/plummerfernandez/16_01_02_Jumpers/film/stills/"
#vidToStills(inputVid,outputDir)
ditherInputDir = "/Users/plummerfernandez/Documents/plummerfernandez/16_01_02_Jumpers/film/stills/"
ditherOutputDir = "/Users/plummerfernandez/Documents/plummerfernandez/16_01_02_Jumpers/film/ditherstills2/"
stillsToDitherStills2(contrastAlgoGray,ditherInputDir,ditherOutputDir)
################




# convert concordia.jpg dpat_hlines2x2.gif  -channel A \
#           -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1].g' \
#           shadow_dpat_hlines2x2.gif


#           convert concordia.jpg  dpat_hlines2x2.gif -virtual-pixel tile  -fx 'u[floor((n-1)*u)+1]' condgrad_hlines2x2.gif