import os

from PIL import ImageGrab
from PIL import Image
import unittest
from ScreenPositions import pos_bb_loot_ul, pos_bb_loot_lr
from ScreenPositions import pos_map_lr, pos_map_ul
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

        for i in range(100):

            coords = self.get_random_coords()
            if self.is_walkable(coords):
                return self.make_absolute_coords(coords)

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


class TestScreenGrabber(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_impl(self):

        s = ScreenGrab()
        s.b_box = pos_bb_loot_ul + pos_bb_loot_lr
        s.load_file_image(r'C:\dev\HobbyStuffs\Archive_input\test_img_trolls.png')
        s.im.show()
        print(s.im.getpixel((10,10)))
        print(s.simple_find_gold())
        print(s.simple_find_meat())
        a = input()

    def test_simple_map(self):
        s = ScreenGrab()
        s.set_map_bb()
        s.load_file_image(r'C:\dev\HobbyStuffs\Archive_input\test_img_map.png')
        s.im.show()
        b=input()
        for i in range(5):
            print(s.find_random_map_point())

if __name__ == '__main__':
    unittest.main()
