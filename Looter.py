import os
from PIL import ImageGrab
from ScreenPositions import pos_around_char, pos_gp_bp
from ScreenGrab import ScreenGrab
import time

class Looter:

    def __init__(self, mouse):
        self.m = mouse
        self.p = pos_around_char

        self.loot_to_grab = []

    def loot_all_squares_around_char(self):

        self.click_all_neighbor_squares()
        time.sleep(1)
        self.loot()

    def click_all_neighbor_squares(self):

        for p1,p2 in self.p:
            self.m.right_click(p1,p2)

    def loot(self):

        s = ScreenGrab()
        s.set_loot_bb()

        s.grab_screen()

        for gp in s.simple_find_gold():
            self.m.drag(gp[0], gp[1], pos_gp_bp[0], pos_gp_bp[1])
            time.sleep(0.5)
        s.grab_screen()

        for meat in s.simple_find_meat():
            time.sleep(0.1)
            self.m.right_click(meat[0],meat[1])

