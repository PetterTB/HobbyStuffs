import os
from PIL import ImageGrab
from ScreenPositions import pos_around_char, pos_gp_bp
from ScreenGrab import ScreenGrab

class Looter:

    def __init__(self, mouse):
        self.m = mouse
        self.p = pos_around_char

        self.loot_to_grab = []

    def loot_all_squares_around_char(self):

        self.click_all_neighbor_squares()
        self.loot()

    def click_all_neighbor_squares(self):

        for p1,p2 in self.p:
            self.m.right_click(p1,p2)
            self.m.left_click(p1+20,p2+50)

    def loot(self):

        s = ScreenGrab()
        s.set_loot_bb()
        s.grab_screen()

        for gp in s.simple_find_gold():
            self.m.drag(gp[0], gp[1], pos_gp_bp[0], pos_gp_bp[1])

        for meat in s.simple_find_meat():
            self.m.left_click(meat[0],meat[1])

