import pyautogui
import os
import time
import random
from Looter import Looter, LooterMock
from Mouse import Mouse, MouseMock
from ScreenGrab import ScreenGrab, ScreenGrabStub
import unittest


class CaveHunter:

    def __init__(self, mouse):
        self.m = mouse
        self.l = Looter(self.m)
        self.s = ScreenGrab()
        self.s.set_map_bb()

    def hunt_floor(self, seconds):

        start = time.time()
        end = start + seconds
        met_mobs_last = False
        c = 0
        self.s.grab_screen()
        coords = self.s.find_random_map_point()
        walk_counter = 0

        while time.time() < end:

            time.sleep(1 + random.random())

            creatures_present = self.check_creatures_present()

            if creatures_present or met_mobs_last:
                met_mobs_last = creatures_present
                self.l.loot_all_squares_around_char()
                c+=1
                pyautogui.press('space')
                #Kill creature sleep.
                time.sleep(2 + random.random())
                if c % 15 == 0:
                    pyautogui.press('1')
                if c % 3 == 0:
                    time.sleep(0.3)
                    pyautogui.press('2')
            else:
                if walk_counter<0:
                    self.s.grab_screen()
                    if (random.randint(0, 10) == 10):
                        coords = self.s.find_random_map_point()
                    else:
                       coords = self.s.find_similar_map_point(coords)
                    self.m.left_click(coords[0], coords[1])
                    walk_counter = 5
                else:
                    walk_counter-=1

    def check_creatures_present(self):
        self.s.b_box = (0, 0) + (1176, 91)
        self.s.grab_screen()
        returnval = self.s.is_creature_present()
        self.s.set_map_bb()
        return returnval

    def go_up_with_rope(self):
        pass

    def go_down(self):
        pass

class TestCaveHunter(unittest.TestCase):

    def setUp(self):
        self.hunter = CaveHunter(MouseMock())
        self.hunter.l = LooterMock()
        self.hunter.s = ScreenGrabStub()
        self.hunter.s.test_files = [r'C:\dev\HobbyStuffs\Archive_input\test_wasps.png']*200

    def test_hunt_for_time(self):
        self.hunter.hunt_floor(10)

if __name__ == "__main__":
    unittest.main()
