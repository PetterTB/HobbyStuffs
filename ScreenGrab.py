import os

from PIL import ImageGrab
from PIL import Image
import unittest
from ScreenPositions import pos_bb_loot_ul, pos_bb_loot_lr
from ScreenPositions import pos_map_lr, pos_map_ul
from ScreenPositions import pos_first_monster
from random import randint

class ScreenGrab:
    def __init__(self):
        self.b_box = ()
        self.im = None
        self.walkable_pixels = [(153,102,51), (0,102,0), (153,153,153)]

    def set_map_bb(self):

        self.b_box = pos_map_ul + pos_map_lr

    def set_loot_bb(self):

        self.b_box = pos_bb_loot_ul + pos_bb_loot_lr

    def load_file_image(self,path):

        self.im = Image.open(path)
        self.im = self.im.crop(self.b_box)

    def grab_screen(self):

        self.im = ImageGrab.grab(self.b_box)

    def find_random_map_point(self):

        for i in range(1000):

            coords = self.get_random_coords()
            if self.is_walkable(coords):
                return self.make_absolute_coords(coords)

        return pos_bb_loot_ul

    def find_similar_map_point(self,last_point):

        if last_point is not None:
            for i in range(20):
                for j in range(20):
                    x = last_point[0] + j
                    y = last_point[0] + i
                    if x<self.get_max_x() and y<self.get_max_y():
                        p = (last_point[0] + i, last_point[1] + j)
                        if self.is_walkable(p):
                            return self.make_absolute_coords(p)
        return self.find_random_map_point()



    def is_walkable(self, c):

        pixel = self.im.getpixel(c)
        if pixel in self.walkable_pixels:
            return True
        return False

    def get_random_coords(self):

        x = randint(0, self.get_max_x()-1)
        y = randint(0, self.get_max_y()-1)
        return(x,y)

    def simple_find_gold(self):

        return self.find_loot_window_matches((239,140,17))

    def simple_find_meat(self):

        return self.find_loot_window_matches((231,147,77))

    def find_loot_window_matches(self, pixel_values):

        x_max = self.get_max_x()
        y_max = self.get_max_y()
        res = []

        y = 0
        while(y< y_max):
            for x in range(x_max):
                if self.im.getpixel((x,y)) == pixel_values:
                    res.append(self.make_absolute_coords((x, y)))
                    y += 30
            y += 1
        return res

    def make_absolute_coords(self, coords):
        return (self.b_box[0] + coords[0]), self.b_box[1] + coords[1]

    def get_max_x(self):
        return self.b_box[2] - self.b_box[0]

    def get_max_y(self):
        return self.b_box[3] - self.b_box[1]

    def is_creature_present(self):

        p = self.im.getpixel(pos_first_monster)
        for color in p:
            if 50 <= color <= 90:
                return False
        return True

class TestScreenGrabber(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_impl(self):

        s = ScreenGrab()
        s.b_box = pos_bb_loot_ul + pos_bb_loot_lr
        s.load_file_image(r'C:\dev\HobbyStuffs\Archive_input\test_img_trolls.png')

    def test_simple_map(self):
        s = ScreenGrab()
        s.set_map_bb()
        s.load_file_image(r'C:\dev\HobbyStuffs\Archive_input\test_img_map.png')
        s.im.show()

    def test_is_creature_present(self):

        s = ScreenGrab()
        s.b_box = (0,0) + (1176,91)
        s.load_file_image(r'C:\dev\HobbyStuffs\Archive_input\full_snap__1509561751.png')
        print("Creature present?", s.is_creature_present())

if __name__ == '__main__':
    unittest.main()
