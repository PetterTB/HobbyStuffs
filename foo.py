import tkinter as tk
import mapper
import ImageProvider
from positions import Positions
import numpy
import time
import math
from PIL import Image

im = Image.open("runData/calib_SS_cut.bmp")

w, h = im.size

pixels = []

for x in range(w):
    for y in range(h):
        pixels.append(im.getpixel((x, y)))

print(pixels)

r = [x[0] for x in pixels]
g = [x[1] for x in pixels]
b = [x[2] for x in pixels]

new_rgb = (sum(r) / len(r), sum(g) / len(g), sum(b) / len(b))

print(new_rgb)