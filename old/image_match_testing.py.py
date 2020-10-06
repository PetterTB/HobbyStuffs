import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

bigimagepath= 'maps/floor-07-map.png'

me = "C://Privat//me.jpg"
eye = "C://Privat//eye.PNG"

img = cv.imread(bigimagepath,1)
img2 = img.copy()
template = cv.imread('tmp.PNG',1)

h, w, channels = template.shape[:]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print(top_left)

    i = Image.open(bigimagepath)
    i = i.crop((top_left[0], top_left[1], top_left[0] + w, top_left[1] + h))
    i.show()

    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res)
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img)
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
