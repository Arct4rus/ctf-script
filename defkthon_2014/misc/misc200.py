#!/usr/bin/python

import Image
import random

size = (245,245)
im = Image.new('RGB',size)
pix = im.load()

# nb line treated
nb_line = 0
cptLine = 0
cptCol = 0

# load file
img_file = open('/root/01 - Personnel/defkthon_2014/misc/misc200.txt', 'r')
lines = img_file.readlines()

for line in lines:
    colors = line.rstrip('\r\n').split(',')
    pix[cptLine, cptCol] = (int(colors[0]), int(colors[1]), int(colors[2]))

    cptCol += 1

    if cptCol > 244:
        cptLine += 1
        cptCol = 0

    if cptLine > 244:
        cptLine = 0

im.save('/root/01 - Personnel/defkthon_2014/misc/misc200.jpg')
img_file.close()
