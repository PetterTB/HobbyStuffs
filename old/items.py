import os
from PIL import Image
from PIL import ImageChops
import random

import math

import unittest

items_folder = "items"

MAX_SUM_OF_SQUARES_DIFF = 50

# Jiggling?
def is_equal(image1, image2):
    h = ImageChops.difference(image1, image2).histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares / float(image1.size[0] * image1.size[1]))

    return rms < MAX_SUM_OF_SQUARES_DIFF

def save_item_image(image):
    for root, folder, files in os.walk(items_folder):
        for file in files:
            if ".png" in file:
                if is_equal(image, Image.open(os.path.join(root, file))):
                    return # Do not save if image is already found.
    im_name = str(random.randint(0,100000)) + ".png"
    print("ImageSaved!")
    image.save(os.path.join(items_folder, im_name))

ITEMS = {}

def get_empty_item():
    d = {}
    d["images"] = []
    d["value"] = ""
    d["name"] = ""
    return d


def make_ITEMS():
    ITEMS["unassigned"] = get_empty_item()
    ITEMS["unassigned"]["name"] = "unassigned"  # not elegant..
    for im in os.listdir(items_folder):
        if (".png" in im):
            ITEMS["unassigned"]["images"].append(os.path.join(items_folder, im))
    for folder in (next(os.walk(items_folder))[1]):
        path = os.path.join(items_folder, folder)
        new_item = get_empty_item()
        new_item["name"] = folder
        for image in os.listdir(path):
            new_item["images"].append(os.path.join(path, image))
        ITEMS[folder] = new_item
    ITEMS["worthless"]["value"] = 0
    ITEMS["gold"]["value"] = 100


make_ITEMS()


def get_item_for_image(input_image):

    for item in ITEMS.values():
        for item_image in item["images"]:
            if is_equal(Image.open(item_image), input_image):
                return item
    save_item_image(input_image)
    make_ITEMS()
    return ITEMS["unassigned"]

class TestImageEqualityWithExamples(unittest.TestCase):

    def setUp(self):
        pass

    def get_item(self, subfolder, number):
        path = f"items_old//{subfolder}//{number}.png"
        return Image.open(path).crop((2,2,38,38))

    def testFoo(self):

        for image_number_1 in range(9):
            for image_number_2 in range(9):
                if image_number_1 != image_number_2:

                    im1 = self.get_item("randoms", image_number_1)
                    im2 = self.get_item("randoms", image_number_2)

                    # Copy pasta from guide. No idea hos it works.
                    h = ImageChops.difference(im1,im2).histogram()
                    sq = (value * ((idx % 256)**2) for idx, value in enumerate(h))
                    sum_of_squares = sum(sq)
                    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))

                    print(rms)

if __name__ == "__main__":
    unittest.main()



