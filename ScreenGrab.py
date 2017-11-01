from PIL import ImageGrab
from PIL import Image
import os
import time
import unittest
from ScreenPositions import pos_bb_loot_ul, pos_bb_loot_lr

class ScreenGrab:

    def __init__(self):

        self.b_box = ()
        self.im = None

    def set_loot_bb(self):

        self.b_box = pos_bb_loot_ul + pos_bb_loot_lr

    def load_file_image(self,path):

        self.im = Image.open(path)
        self.im = self.im.crop(self.b_box)

    def grab_screen(self):

        self.im = ImageGrab.grab(self.b_box)

    def simple_find_gold(self):

        x_max = self.get_max_x()
        y_max = self.get_max_y()
        res = []

        y = 0
        while(y<y_max):
            for x in range(x_max):
                if self.im.getpixel((x,y)) == (239,140,17):
                    spam = ((self.b_box[0]+x), self.b_box[1]+y)
                    res.append(spam)
                    y += 30
            y += 1
        return res

    def simple_find_meat(self):

        x_max = self.get_max_x()
        y_max = self.get_max_y()
        res = []

        y = 0
        while(y<y_max):
            for x in range(x_max):
                if self.im.getpixel((x,y)) == (231,147,77):
                    spam = ((self.b_box[0]+x), self.b_box[1]+y)
                    res.append(spam)
                    y += 30
            y += 1
        return res

    def get_max_x(self):
        return self.b_box[2] - self.b_box[0]

    def get_max_y(self):
        return self.b_box[3] - self.b_box[1]


class TestScrenGrabber(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()